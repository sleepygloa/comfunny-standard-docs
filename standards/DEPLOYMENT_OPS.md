# 6. Deployment & Operations Standard

## 6.1 CI/CD Pipeline Strategy
본 프로젝트는 **GitHub Actions** (또는 Jenkins)를 통한 자동 배포를 원칙으로 한다.

### Pipeline Stages
1.  **Checkout:** 최신 코드 인출.
2.  **Lint & Test:** `npm run lint`, `./gradlew test` 수행. 실패 시 배포 중단.
3.  **Build Image:**
    - Frontend-Web: `docker build -t comfunny-web:latest .`
    - Backend-API: `docker build -t comfunny-backend:latest .`
4.  **Push Registry:** AWS ECR 또는 Private Docker Registry에 이미지 푸시.
5.  **Deploy:** 운영 서버에서 `docker-compose pull && docker-compose up -d` 실행.

## 6.2 Docker Compose Production Profile
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

## 6.3 Monitoring & Logging
1.Logs: 모든 컨테이너 로그는 Docker Driver를 통해 수집하며, 파일 시스템에 영구 보관하지 않는다 (ELK 스택 등으로 전송 권장).
2.Health Check:
- Backend: GET /actuator/health (Spring Boot Actuator 필수)
- Frontend: GET /api/health (Next.js API Route 구현)
- Alerting: CPU/Memory 사용률 80% 초과 시 Slack 알림 발송.

## 6.4 Rollback Policy
- 배포 실패 또는 치명적 버그 발견 시 **"즉시 롤백"**을 원칙으로 한다.

```bash
# 1. 이전 버전 태그 확인
git tag -l

# 2. 특정 버전으로 체크아웃 및 재배포
git checkout v1.0.5
docker-compose up --build -d