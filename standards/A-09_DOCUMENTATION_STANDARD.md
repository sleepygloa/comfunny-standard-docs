# [A-09] Documentation Standard

## 목차

<!-- toc -->

  * [A-09-11.1 Overview](#a-09-111-overview)
  * [A-09-11.2 Mandatory Documents (필수 문서)](#a-09-112-mandatory-documents-%ED%95%84%EC%88%98-%EB%AC%B8%EC%84%9C)
  * [A-09-11.3 README Template](#a-09-113-readme-template)
- [[A-09] Documentation Standard (Detailed Guide)](#a-09-documentation-standard-detailed-guide)
  * [A-09-1. Changelog Convention](#a-09-1-changelog-convention)
    + [A-09-1.1 Format Example](#a-09-11-format-example)
  * [A-09-2. README Best Practices](#a-09-2-readme-best-practices)
  * [A-09-3. Documentation as Code](#a-09-3-documentation-as-code)

<!-- tocstop -->

## A-09-11.1 Overview
코드가 아무리 좋아도 **문서**가 없으면 죽은 프로젝트입니다.
모든 프로젝트(서비스)는 루트에 아래 필수 문서를 반드시 포함해야 합니다.

---

## A-09-11.2 Mandatory Documents (필수 문서)
| 파일명 | 필수 여부 | 내용 |
| :--- | :--- | :--- |
| `README.md` | **Required** | 프로젝트 개요, 아키텍처, 실행 방법 (아래 템플릿 준수) |
| `CHANGELOG.md` | **Required** | 버전별 변경 이력 (Keep a Changelog 포맷) |
| `TECH_STACK.md` | Optional | 프로젝트별 특이 기술 스택 (Global과 다를 경우만 작성) |
| `API_DOCS.md` | Optional | Swagger URL 링크 또는 API 명세 (Swagger 권장) |

---

## A-09-11.3 README Template
모든 프로젝트의 `README.md`는 아래 포맷을 복사하여 작성합니다.

```markdown
# [Project Name]

![Badge](https://img.shields.io/badge/Spring%20Boot-3.2-green)
![Badge](https://img.shields.io/badge/Java-17-blue)

## A-09-1. Overview
> 한 줄 요약: (예: 전사 알림 발송을 담당하는 푸시 서버)
- **담당자:** 홍길동 (메일)
- **JIRA Key:** [NOTI]

## A-09-2. Architecture
- **Layer:** Presentation -> Application -> Domain -> Infrastructure
- **Tech:** Spring Boot 3.2, JPA, QueryDSL, MySQL 8, Redis

## A-09-3. Getting Started
(로컬 실행 방법)
\`\`\`bash
# 1. Clone
git clone ...

# 2. Env Setup
cp src/main/resources/application-local.yml.example src/main/resources/application-local.yml

# 3. Run
./gradlew bootRun
\`\`\`

## A-09-4. Key Features
- 실시간 웹소켓 푸시
- 카카오 알림톡 연동
```


---

<!-- DETAILED GUIDE START -->

# [A-09] Documentation Standard (Detailed Guide)

## A-09-1. Changelog Convention
**"무엇이 바뀌었는지"**를 명확히 기록해야 배포 시 리스크를 줄일 수 있습니다.
[Keep a Changelog](https://keepachangelog.com/ko/1.0.0/) 형식을 따릅니다.

### A-09-1.1 Format Example
```markdown
# Changelog

## [1.2.0] - 2024-03-20
### Added
- 사용자 소셜 로그인 기능 추가 (Kakao, Google)
- 마이페이지 프로필 수정 API

### Changed
- 로그인 토큰 만료 시간을 1시간에서 24시간으로 변경
- `PaymentService` 로직 리팩토링 (트랜잭션 분리)

### Fixed
- 결제 취소 시 포인트가 환불되지 않던 버그 수정
- 간헐적으로 발생하던 Redis Connection Timeout 해결
```

## A-09-2. README Best Practices
- **Badge 활용:** 프로젝트의 상태(Build Status, Coverage, Version)를 시각적으로 보여줍니다.
- **Prerequisites:** 실행을 위해 필요한 사전 요구사항(Java 17 설치, Docker 실행 등)을 명시합니다.
- **Diagrams:** 복잡한 아키텍처는 Mermaid 다이어그램을 삽입하여 이해를 돕습니다.

## A-09-3. Documentation as Code
- `README.md`도 코드입니다.
- 오타 수정, 버전 업데이트 등도 PR을 통해 리뷰 받고 Merge 되어야 합니다.
- Wiki(Confluence)보다는 Repository 내부의 마크다운 문서를 1순위(SSOT)로 유지하십시오.
