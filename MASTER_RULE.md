# MASTER RULES: Enterprise Architecture Standard

## 1. Overview
이 문서는 **전사 아키텍처 및 개발 표준**의 최상위 진입점(Entry Point)입니다.
AI 및 모든 개발자는 이 규칙을 **절대적 기준(Single Source of Truth)**으로 삼아야 합니다.

---

## 2. Document Map (AI Reference Index)

### [A] Global Standards (Path: `.docs/standards/`)
프로젝트의 성격과 무관하게 준수해야 하는 **불변의 원칙**입니다.

- **[01] 기술 스택:** `TECH_STACK.md` (Backend, Frontend, Mobile 선정 기준)
- **[02] 코딩 컨벤션:** `CODING_CONVENTION.md` (네이밍, 주석, FLOW 패턴)
- **[03] 프로젝트 구조:** `PROJECT_STRUCTURE.md` (폴더 구조, 환경설정)
- **[04] 배포 & 운영:** `DEPLOYMENT_OPS.md` (CI/CD, Docker)
- **[05] Git 전략:** `GIT_STRATEGY.md` (Branch, Commit Message)
- **[06] 보안 표준:** `SECURITY_STANDARD.md` (Auth, Encryption)
- **[07] 테스트 전략:** `TEST_STRATEGY.md` (Coverage, Mocking)
- **[08] 에러/로깅:** `ERROR_LOGGING.md` (ErrorCode, JSON Log, Discord Alert)
- **[09] 문서화 표준:** `DOCUMENTATION_STANDARD.md` (README, CHANGELOG)
- **[10] QA 가이드:** `QA_GUIDE.md` (AI Persona, Response Rule)
- **[11] AI 역할 정의:** `AI_ROLE_DEFINITION.md` (CTO, Architect, Security Manager)

---

### [B] Tech Guides (Path: `.docs/tech-guides/`)
특정 기술 스택을 사용하여 프로젝트를 시작할 때 따르는 **Init & Run 매뉴얼**입니다.

- **Batch:** `BATCH_GUIDE.md` (Spring Batch 5 Init)
- **Mobile:** `MOBILE_GUIDE.md` (Flutter, Android, iOS Init)
- **Web Frontend:** `WEB_FRONTEND_GUIDE.md` (Next.js, Vue, React Init)
- **Backend MVC:** `BACKEND_MVC_GUIDE.md` (Spring Boot + Thymeleaf Init)

---

### [C] Project Specifics
개별 프로젝트의 아키텍처 및 도메인 규칙은 각 프로젝트 루트의 `.project-docs/` 디렉토리 내에 정의합니다.

- **표준 위치:** `[Project Root]/.project-docs/1_PROJECT_OVERVIEW.md` (또는 `PLAN.md`)
- **포함 내용:** 기획 의도, 아키텍처, 트러블슈팅, 레거시 마이그레이션 정보 등.

> **참고:** 현재 활성화된 프로젝트 목록과 위치는 저장소 루트의 **`README.md`**를 참조하십시오.
