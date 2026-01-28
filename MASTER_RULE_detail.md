# MASTER RULES: Enterprise Architecture Standard (Detailed Guide)

## 1. 개요 (Overview)
`MASTER_RULE.md`는 이 프로젝트의 **헌법**입니다. 모든 하위 문서는 이 헌법의 정신을 계승해야 하며, 위배되어서는 안 됩니다.
이 문서는 헌법의 **해설서** 역할을 합니다.

## 2. 문서화 철학 (Documentation Philosophy)

### 2.1 Single Source of Truth (SSOT)
- **원칙:** 정보는 한 곳에만 존재해야 합니다.
- **예시:** "자바 버전은 17을 쓴다"라는 정보가 `README.md`, `TECH_STACK.md`, `DEPLOYMENT_OPS.md`에 흩어져 있으면 나중에 하나만 수정되고 나머지는 방치되어 혼란을 줍니다.
- **실천:** `TECH_STACK.md`에 버전을 명시하고, 다른 문서에서는 이를 참조(Link)하는 형태로 작성합니다.

### 2.2 Documentation as Code
- 문서는 코드가 변경될 때 함께 변경되어야 합니다.
- PR 제출 시 "기능 구현" 뿐만 아니라 "관련 문서 업데이트"도 체크리스트에 포함되어야 합니다.

## 3. Directory Structure Rationale

### 3.1 .docs/ vs .project-docs/
- **.docs/ (Global Standard):**
    - 회사의 모든 프로젝트가 공통으로 따르는 "법률"입니다.
    - 개인이나 단위 프로젝트 팀장이 임의로 수정할 수 없습니다. (아키텍처 팀 승인 필요)
    - **Additions:** `5_PROJECT_STRUCTURE.md`가 추가되어 디렉토리 구조 및 필수 파일의 표준을 정의합니다.
- **.project-docs/ (Local Specifics):**
    - 이 프로젝트만의 특수한 상황(도메인 규칙, 마이그레이션 절차)을 담습니다.
    - 팀 내부 협의로 자유롭게 수정 가능합니다.

### 3.2 AI와 문서의 관계
- **Context Injection:**
    - AI(Copilot, ChatGPT 등)에게 질문할 때, 이 문서들을 Context로 제공하는 것이 **프롬프트 엔지니어링의 핵심**입니다.
    - "우리 회사 규칙대로 컴포넌트 짜줘"라고 말하려면 `3_CODING_CONVENTION.md` 내용을 제공해야 합니다.

## 4. Governance & Update
- 이 문서는 분기별 1회 정기 점검을 통해 최신 기술 트렌드와 팀의 피드백을 반영하여 개정합니다.
- 레거시가 된 규칙은 과감히 삭제하거나 `Legacy` 태그를 달아 격리합니다.
