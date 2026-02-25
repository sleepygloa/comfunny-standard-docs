# [A-04] Deployment & Operations Standard

## 목차

<!-- toc -->

- [A-04-6.1 CI/CD Pipeline Strategy](#a-04-61-cicd-pipeline-strategy)
  * [Pipeline Stages](#pipeline-stages)
- [A-04-6.2 Docker Compose Production Profile](#a-04-62-docker-compose-production-profile)

<!-- tocstop -->

## A-04-6.1 CI/CD Pipeline Strategy
본 프로젝트는 **GitHub Actions** (또는 Jenkins)를 통한 자동 배포 또는 **개발자의 수동 배포**를 원칙으로 한다.

> ⚠️ **[AI AGENT RESTRICTION]** 
> AI Agent는 **절대로** 운영/개발 환경에 대한 배포 명령(`firebase deploy`, `docker-compose up`, `flutter build` 후 서버 전송 등)을 **자동으로 또는 임의로 실행해서는 안 됩니다.** 
> 배포 파이프라인 트리거 및 서버 업로드는 **무조건 인간 개발자(USER)가 수동으로 진행**합니다. AI는 배포 스크립트 작성 및 빌드 아티팩트 점검까지만 보조합니다.

### Pipeline Stages
1.  **Checkout:** 최신 코드 인출.
2.  **Lint & Test:** `npm run lint`, `./gradlew test` 수행. 실패 시 배포 중단.
3.  **Build Image:**
    - Frontend-Web: `docker build -t comfunny-web:latest .`
    - Backend-API: `docker build -t comfunny-backend:latest .`
4.  **Push Registry:** AWS ECR 또는 Private Docker Registry에 이미지 푸시.
5.  **Deploy:** 운영 서버에서 `docker-compose pull && docker-compose up -d` 실행.

## A-04-6.2 Docker Compose Production Profile
운영 환경(Production)에서는 반드시 아래 환경 변수와 설정을 적용해야 한다.

```yaml
# docker-compose.prod.yml 예시
version: '3.8'
services:
  backend:
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - LOG_LEVEL=INFO
    restart: always
    logging: # 로그 로테이션 설정 필수
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  frontend-web:
    environment:
      - NODE_ENV=production
    restart: always
```

## A-04-6.3 Monitoring & Logging
1.Logs: 모든 컨테이너 로그는 Docker Driver를 통해 수집하며, 파일 시스템에 영구 보관하지 않는다 (ELK 스택 등으로 전송 권장).
2.Health Check:
- Backend: GET /actuator/health (Spring Boot Actuator 필수)
- Frontend: GET /api/health (Next.js API Route 구현)
- Alerting: CPU/Memory 사용률 80% 초과 시 Slack 알림 발송.

## A-04-6.4 Rollback Policy
- 배포 실패 또는 치명적 버그 발견 시 **"즉시 롤백"**을 원칙으로 한다.

```bash
# 1. 이전 버전 태그 확인
git tag -l

# 2. 특정 버전으로 체크아웃 및 재배포
git checkout v1.0.5
docker-compose up --build -d
```

---

<!-- DETAILED GUIDE START -->

# [A-04] Deployment & Operations Standard (Detailed Guide)

## A-04-1. 개요 (Overview)
`6_DEPLOYMENT_OPS.md`는 파이프라인의 **뼈대**를 정의했습니다. 본 문서는 그 위에서 돌아가는 **프로세스의 디테일**과 **장애 대응 매뉴얼**을 다룹니다.

## A-04-2. CI/CD 상세 전략

### A-04-2.1 Docker Build Optimization (Multi-stage Build)
이미지 용량을 줄이기 위해 반드시 Multi-stage 빌드를 사용해야 합니다.

- **Builder Stage:**
    - Gradle, Node.js 등을 포함한 무거운 이미지(JDK 포함) 사용.
    - 소스 코드 빌드 및 테스트 수행.
- **Runner Stage:**
    - 운영에 필요한 최소한의 런타임(JRE-headless, Nginx-alpine)만 포함.
    - Builder Stage에서 생성된 JAR 파일이나 정적 리소스만 `COPY` 해옴.

### A-04-2.2 Blue/Green Deployment (Zero Downtime)
- 현재 구성은 `docker-compose up -d`로 다운타임이 발생할 수 있습니다 (Recreate strategy).
- **Advanced Strategy:**
    - Nginx 앞단에서 트래픽을 제어하여 `Blue(Old)` -> `Green(New)` 컨테이너로 스위칭하는 방식을 권장합니다.
    - 또는 Kubernetes(K8s) 도입 시 Rolling Update 전략을 기본으로 사용합니다.

## A-04-3. Operational Best Practices

### A-04-3.1 Log Management Strategy
- **Why File Logging is Bad:** 컨테이너가 삭제되면 로그도 사라집니다.
- **Solution:**
    - **Stdout/Stderr:** 애플리케이션은 오직 표준 출력으로만 로그를 뱉습니다.
    - **Docker Log Driver:** Docker 데몬이 이 로그를 잡아 AWS CloudWatch나 ELK(Filebeat)로 전송합니다.
    - 로컬 개발 시에만 `json-file` 드라이버를 사용하여 `docker logs -f`로 확인합니다.

### A-04-3.2 Configuration Management (Environment Variables)
- **Secrets:** DB 비밀번호, API Key 등은 절대 코드(`application.yml`, `.env`)에 포함하지 않습니다.
- **Rule:**
    - CI/CD 파이프라인(Github Secrets, Jenkins Credentials)에서 주입받거나,
    - AWS Parameter Store, Vault 같은 외부 저장소를 연동합니다.

## A-04-4. Emergency Response (Troubleshooting)

### A-04-4.1 CPU Spike Check
1. `docker stats` 로 문제 컨테이너 식별.
2. `docker exec -it <container_id> /bin/sh` 접속.
3. (Java의 경우) `jstack <pid> > dump.txt` 로 스레드 덤프 확보 후 분석.

### A-04-4.2 DB Connection Pool Exhaustion
- 증상: API 타임아웃 발생, 로그에 `Connection is not available` 발생.
- 조치: HikariCP 설정 점검 (`maximum-pool-size`), 트랜잭션이 오래 걸리는 쿼리(Long Transaction) 킬.

## A-04-5. Firebase Hosting Deployment (Flutter Web / Static Web)

Flutter Web 프로젝트 등 정적 웹사이트를 Firebase Hosting을 통해 배포할 때는 다음 표준을 따릅니다.

### A-04-5.1 Firebase 초기 설정 (`firebase.json`)
Flutter Web 빌드 결과물은 기본적으로 `build/web` 폴더에 생성되므로, Firebase Hosting의 `public` 디렉토리를 해당 경로로 올바르게 지정해야 404 에러가 발생하지 않습니다.

```json
{
  "hosting": {
    "public": "build/web",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "headers": [
      {
        "source": "**/*.apk",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache, no-store, must-revalidate"
          }
        ]
      }
    ]
  }
}
```

### A-04-5.2 자동화 배포 스크립트 (`deploy_web.bat` / `deploy_web.sh`)
단순 반복되는 배포 작업을 자동화하고 휴먼 에러를 방지하기 위해 프로젝트 루트에 배포 스크립트를 작성하여 사용합니다. 스크립트에는 다음의 단계가 포함되어야 합니다.

1. **Pre-flight Check**: `flutter` 및 `firebase` CLI 설치 여부 확인
2. **Version Bump**: 배포 전 버전 번호 자동/수동 증가 (e.g. `pubspec.yaml` 수정)
3. **Build**: `flutter build web --release` 실행
4. **Deploy**: `firebase deploy --only hosting` 실행

**스크립트 예시 (Windows Batch):**
```bat
@echo off
chcp 65001 > nul
echo [1/3] Building Web App...
call flutter build web --release
if errorlevel 1 exit /b 1

echo [2/3] Uploading to Firebase Hosting...
call firebase deploy --only hosting
if errorlevel 1 exit /b 1

echo [DONE] Web Deployment Complete!
```
