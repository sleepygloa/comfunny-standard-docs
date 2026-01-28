# 11. Documentation Standard

## 11.1 Overview
코드가 아무리 좋아도 **문서**가 없으면 죽은 프로젝트입니다.
모든 프로젝트(서비스)는 루트에 아래 필수 문서를 반드시 포함해야 합니다.

---

## 11.2 Mandatory Documents (필수 문서)
| 파일명 | 필수 여부 | 내용 |
| :--- | :--- | :--- |
| `README.md` | **Required** | 프로젝트 개요, 아키텍처, 실행 방법 (아래 템플릿 준수) |
| `CHANGELOG.md` | **Required** | 버전별 변경 이력 (Keep a Changelog 포맷) |
| `TECH_STACK.md` | Optional | 프로젝트별 특이 기술 스택 (Global과 다를 경우만 작성) |
| `API_DOCS.md` | Optional | Swagger URL 링크 또는 API 명세 (Swagger 권장) |

---

## 11.3 README Template
모든 프로젝트의 `README.md`는 아래 포맷을 복사하여 작성합니다.

```markdown
# [Project Name]

![Badge](https://img.shields.io/badge/Spring%20Boot-3.2-green)
![Badge](https://img.shields.io/badge/Java-17-blue)

## 1. Overview
> 한 줄 요약: (예: 전사 알림 발송을 담당하는 푸시 서버)
- **담당자:** 홍길동 (메일)
- **JIRA Key:** [NOTI]

## 2. Architecture
- **Layer:** Presentation -> Application -> Domain -> Infrastructure
- **Tech:** Spring Boot 3.2, JPA, QueryDSL, MySQL 8, Redis

## 3. Getting Started
(로컬 실행 방법)
\`\`\`bash
# 1. Clone
git clone ...

# 2. Env Setup
cp src/main/resources/application-local.yml.example src/main/resources/application-local.yml

# 3. Run
./gradlew bootRun
\`\`\`

## 4. Key Features
- 실시간 웹소켓 푸시
- 카카오 알림톡 연동
```
