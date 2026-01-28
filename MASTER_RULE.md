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

---

### [B] Tech Guides (Path: `.docs/tech-guides/`)
특정 기술 스택을 사용하여 프로젝트를 시작할 때 따르는 **Init & Run 매뉴얼**입니다.

- **Batch:** `BATCH_GUIDE.md` (Spring Batch 5 Init)
- **Mobile:** `MOBILE_GUIDE.md` (Flutter, Android, iOS Init)
- **Web Frontend:** `WEB_FRONTEND_GUIDE.md` (Next.js, Vue, React Init)
- **Backend MVC:** `BACKEND_MVC_GUIDE.md` (Spring Boot + Thymeleaf Init)

---

### [C] Project Specifics (Path: `.project-docs/`)
특정 도메인이나 현장 상황에 특화된 가이드입니다.

- **[Mobile] WMS App:** `frontend-mobile-wms/.project-docs/1_PROJECT_PLAN.md`
- **[Legacy] Analysis (Batch/CRN/Open/Internal):** `.project-docs/LEGACY_ANALYSIS.md`




- **레거시 분석:** `LEGACY_ANALYSIS.md`
- **[신규] 나의 아이의 책읽기:** `frontend-mobile-mychild-reading/.project-docs/1_PROJECT_PLAN.md`

프로젝트 진행 시 위 문서들의 최신 내용을 항상 참조하십시오.