<!-- AGENT RULE: AI Agent 설정 시 항상 이 README.md 파일의 내용을 복사/참조하여 프로젝트의 핵심 룰(Rule)로 지정하십시오. -->

> **AGENT RULE INSTRUCTION:** AI Agent 설정 시 항상 이 README.md 파일의 내용을 복사/참조하여 프로젝트의 핵심 룰(Rule)로 지정하십시오.

# MASTER RULES: Enterprise Architecture Standard

## 목차

<!-- toc -->

  * [1. Overview](#1-overview)
  * [2. Document Map (AI Reference Index)](#2-document-map-ai-reference-index)
    + [[A] Global Standards (Path: `.docs/standards/`)](#a-global-standards-path-docsstandards)
    + [[B] Tech Guides (Path: `.docs/tech-guides/`)](#b-tech-guides-path-docstech-guides)
    + [[C] Project Specifics](#c-project-specifics)
- [MASTER RULES: Enterprise Architecture Standard (Detailed Guide)](#master-rules-enterprise-architecture-standard-detailed-guide)
  * [1. 개요 (Overview)](#1-%EA%B0%9C%EC%9A%94-overview)
  * [2. 문서화 철학 (Documentation Philosophy)](#2-%EB%AC%B8%EC%84%9C%ED%99%94-%EC%B2%A0%ED%95%99-documentation-philosophy)
    + [2.1 Single Source of Truth (SSOT)](#21-single-source-of-truth-ssot)
    + [2.2 Documentation as Code](#22-documentation-as-code)
  * [3. Directory Structure Rationale](#3-directory-structure-rationale)
    + [3.1 .docs/ vs .project-docs/](#31-docs-vs-project-docs)
    + [3.2 AI와 문서의 관계](#32-ai%EC%99%80-%EB%AC%B8%EC%84%9C%EC%9D%98-%EA%B4%80%EA%B3%84)
  * [4. Governance & Update](#4-governance--update)

<!-- tocstop -->

## 1. Overview
이 문서는 **전사 아키텍처 및 개발 표준**의 최상위 진입점(Entry Point)입니다.
AI 및 모든 개발자는 이 규칙을 **절대적 기준(Single Source of Truth)**으로 삼아야 합니다.

> **Current Version:** `v1.1.0` (Refer to [governance/DOCS_CHANGELOG.md](governance/DOCS_CHANGELOG.md) for history)


---

## 2. Document Map (AI Reference Index)

### [A] Global Standards (Path: `.docs/standards/`)
프로젝트의 성격과 무관하게 준수해야 하는 **불변의 원칙**입니다.

- **[01] 기술 스택:** `A-01_TECH_STACK.md` (Backend, Frontend, Mobile 선정 기준)
- **[02] 코딩 컨벤션:** `A-02_CODING_CONVENTION.md` (네이밍, 주석, FLOW 패턴)
- **[03] 프로젝트 구조:** `A-03_PROJECT_STRUCTURE.md` (폴더 구조, 환경설정)
- **[04] 배포 & 운영:** `A-04_DEPLOYMENT_OPS.md` (CI/CD, Docker)
- **[05] Git 전략:** `A-05_GIT_STRATEGY.md` (Branch, Commit Message)
- **[06] 보안 표준:** `A-06_SECURITY_STANDARD.md` (Auth, Encryption)
- **[07] 테스트 전략:** `A-07_TEST_STRATEGY.md` (Coverage, Mocking)
- **[08] 에러/로깅:** `A-08_ERROR_LOGGING.md` (ErrorCode, JSON Log, Discord Alert)
- **[09] 문서화 표준:** `A-09_DOCUMENTATION_STANDARD.md` (README, CHANGELOG)
- **[10] QA 가이드:** `A-10_QA_GUIDE.md` (AI Persona, Response Rule)
- **[11] AI 역할 정의:** `A-11_AI_ROLE_DEFINITION.md` (CTO, Architect, Security Manager)
- **[12] UI/UX 표준:** `A-12_UI_UX_STANDARD.md` (Design System, UX Flow, Error Handle)

---

### [B] Tech Guides (Path: `.docs/tech-guides/`)
특정 기술 스택을 사용하여 프로젝트를 시작할 때 따르는 **Init & Run 매뉴얼**입니다.

- **Batch:** `B-01_BATCH_GUIDE.md` (Spring Batch 5 Init)
- **Mobile:** `B-02_MOBILE_GUIDE.md` (Flutter, Android, iOS Init)
- **Web Frontend:** `B-03_WEB_FRONTEND_GUIDE.md` (Next.js, Vue, React Init)
- **Backend MVC:** `B-04_BACKEND_MVC_GUIDE.md` (Spring Boot + Thymeleaf Init)

---

### [C] Project Specifics
개별 프로젝트의 아키텍처 및 도메인 규칙은 각 프로젝트 루트의 `.project-docs/` 디렉토리 내에 정의합니다.

- **표준 위치:** `[Project Root]/.project-docs/1_PROJECT_OVERVIEW.md` (또는 `PLAN.md`)
- **포함 내용:** 기획 의도, 아키텍처, 트러블슈팅, 레거시 마이그레이션 정보 등.

> **참고:** 현재 활성화된 프로젝트 목록과 위치는 저장소 루트의 **`README.md`**를 참조하십시오.


---

<!-- DETAILED GUIDE START -->

# MASTER RULES: Enterprise Architecture Standard (Detailed Guide)

## 1. 개요 (Overview)
`MASTER_RULE.md`는 이 프로젝트의 **헌법**입니다. 모든 하위 문서는 이 헌법의 정신을 계승해야 하며, 위배되어서는 안 됩니다.
이 문서는 헌법의 **해설서** 역할을 합니다.

## 2. 문서화 철학 (Documentation Philosophy)

### 2.1 Single Source of Truth (SSOT)
- **원칙:** 정보는 한 곳에만 존재해야 합니다.
- **예시:** "자바 버전은 17을 쓴다"라는 정보가 `README.md`, `A-01_TECH_STACK.md`, `A-04_DEPLOYMENT_OPS.md`에 흩어져 있으면 나중에 하나만 수정되고 나머지는 방치되어 혼란을 줍니다.
- **실천:** `A-01_TECH_STACK.md`에 버전을 명시하고, 다른 문서에서는 이를 참조(Link)하는 형태로 작성합니다.

### 2.2 Documentation as Code
- 문서는 코드가 변경될 때 함께 변경되어야 합니다.
- PR 제출 시 "기능 구현" 뿐만 아니라 "관련 문서 업데이트"도 체크리스트에 포함되어야 합니다.

## 3. Directory Structure Rationale

### 3.1 .docs/ vs .project-docs/
- **.docs/ (Global Standard):**
    - 회사의 모든 프로젝트가 공통으로 따르는 "법률"입니다.
    - 개인이나 단위 프로젝트 팀장이 임의로 수정할 수 없습니다. (아키텍처 팀 승인 필요)
    - **Additions:** `A-03_PROJECT_STRUCTURE.md`가 추가되어 디렉토리 구조 및 필수 파일의 표준을 정의합니다.
- **.project-docs/ (Local Specifics):**
    - 이 프로젝트만의 특수한 상황(도메인 규칙, 마이그레이션 절차)을 담습니다.
    - 팀 내부 협의로 자유롭게 수정 가능합니다.

### 3.2 AI와 문서의 관계
- **Context Injection:**
    - AI(Copilot, ChatGPT 등)에게 질문할 때, 이 문서들을 Context로 제공하는 것이 **프롬프트 엔지니어링의 핵심**입니다.
    - "우리 회사 규칙대로 컴포넌트 짜줘"라고 말하려면 `A-02_CODING_CONVENTION.md` 내용을 제공해야 합니다.

## 4. Governance & Update
- 이 문서는 분기별 1회 정기 점검을 통해 최신 기술 트렌드와 팀의 피드백을 반영하여 개정합니다.
- 레거시가 된 규칙은 과감히 삭제하거나 `Legacy` 태그를 달아 격리합니다.

## 5. RESPONSE PROTOCOL (MANDATORY)
- **Rule Application Check (MANDATORY):** 모든 대화의 **첫 답변 최상단**에 아래 상태 체크 문구를 반드시 출력해야 합니다.
  - 규칙이 적용된 경우(이 문서를 정상 참조한 경우): `✅ **[Rule Check]** .docs/README.md 기반 전사 아키텍처 규칙이 적용되었습니다.`
  - 규칙을 찾을 수 없거나 적용되지 않은 경우: `⚠️ **[Rule Check]** 현재 .docs/README.md 전사 아키텍처 규칙이 적용되지 않았습니다. 규칙을 먼저 주입해 주시거나 지침을 확인해 주세요.`
