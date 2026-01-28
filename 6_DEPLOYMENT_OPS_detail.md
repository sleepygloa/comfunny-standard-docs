# 6. Deployment & Operations Standard (Detailed Guide)

## 1. 개요 (Overview)
`6_DEPLOYMENT_OPS.md`는 파이프라인의 **뼈대**를 정의했습니다. 본 문서는 그 위에서 돌아가는 **프로세스의 디테일**과 **장애 대응 매뉴얼**을 다룹니다.

## 2. CI/CD 상세 전략

### 2.1 Docker Build Optimization (Multi-stage Build)
이미지 용량을 줄이기 위해 반드시 Multi-stage 빌드를 사용해야 합니다.

- **Builder Stage:**
    - Gradle, Node.js 등을 포함한 무거운 이미지(JDK 포함) 사용.
    - 소스 코드 빌드 및 테스트 수행.
- **Runner Stage:**
    - 운영에 필요한 최소한의 런타임(JRE-headless, Nginx-alpine)만 포함.
    - Builder Stage에서 생성된 JAR 파일이나 정적 리소스만 `COPY` 해옴.

### 2.2 Blue/Green Deployment (Zero Downtime)
- 현재 구성은 `docker-compose up -d`로 다운타임이 발생할 수 있습니다 (Recreate strategy).
- **Advanced Strategy:**
    - Nginx 앞단에서 트래픽을 제어하여 `Blue(Old)` -> `Green(New)` 컨테이너로 스위칭하는 방식을 권장합니다.
    - 또는 Kubernetes(K8s) 도입 시 Rolling Update 전략을 기본으로 사용합니다.

## 3. Operational Best Practices

### 3.1 Log Management Strategy
- **Why File Logging is Bad:** 컨테이너가 삭제되면 로그도 사라집니다.
- **Solution:**
    - **Stdout/Stderr:** 애플리케이션은 오직 표준 출력으로만 로그를 뱉습니다.
    - **Docker Log Driver:** Docker 데몬이 이 로그를 잡아 AWS CloudWatch나 ELK(Filebeat)로 전송합니다.
    - 로컬 개발 시에만 `json-file` 드라이버를 사용하여 `docker logs -f`로 확인합니다.

### 3.2 Configuration Management (Environment Variables)
- **Secrets:** DB 비밀번호, API Key 등은 절대 코드(`application.yml`, `.env`)에 포함하지 않습니다.
- **Rule:**
    - CI/CD 파이프라인(Github Secrets, Jenkins Credentials)에서 주입받거나,
    - AWS Parameter Store, Vault 같은 외부 저장소를 연동합니다.

## 4. Emergency Response (Troubleshooting)

### 4.1 CPU Spike Check
1. `docker stats` 로 문제 컨테이너 식별.
2. `docker exec -it <container_id> /bin/sh` 접속.
3. (Java의 경우) `jstack <pid> > dump.txt` 로 스레드 덤프 확보 후 분석.

### 4.2 DB Connection Pool Exhaustion
- 증상: API 타임아웃 발생, 로그에 `Connection is not available` 발생.
- 조치: HikariCP 설정 점검 (`maximum-pool-size`), 트랜잭션이 오래 걸리는 쿼리(Long Transaction) 킬.
