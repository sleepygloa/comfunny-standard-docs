# 9. Migration Workflow Guide (Legacy -> Enterprise)

## 9.1 Introduction
이 문서는 기존 레거시 코드를 현재의 **Enterprise Monorepo Architecture**로 이관하기 위한 **단계별 실행 매뉴얼**입니다.
각 단계(Phase)는 순차적으로 진행되어야 하며, 각 단계가 끝날 때마다 빌드/구동 테스트를 수행해야 합니다.

---

## Phase 1. Foundation (기반 마련)
**목표:** 빈 껍데기지만 완벽하게 동작하는 Docker 통합 환경 구축.

1.  **Init:** `comfunny-system` 폴더 생성 및 `.docs/` 문서 파일 9개 배치.
2.  **Infra:** `nginx/`, `docker-compose.yml` 생성 (AI에게 `MASTER_RULE.md` 참조 요청).
3.  **Verification:** `docker-compose up` 실행 시 Nginx, DB 컨테이너가 정상 구동되는지 확인.

---

## Phase 2. Public Web (Next.js) Migration
**목표:** React CSR 코드를 Next.js SSR로 변환.

1.  **Setup:** `frontend-nextjs` 폴더에 Next.js 설치.
2.  **Page Migration (반복 작업):**
    > **[CLI Prompt]**
    > "`.docs/3_CODING_CONVENTION.md`의 **Next.js** 규칙을 참고해.
    > 내가 주는 이 React 컴포넌트(`Home.jsx`)를 **Server Component**(`page.tsx`)로 변환해줘.
    > SEO 메타데이터를 포함하고, API 호출은 `fetch`로 변경해."
3.  **Verification:** `http://localhost:3000` 접속 확인.

---

## Phase 3. Backend & Admin Migration
**목표:** Spring Boot 구조 재정렬 및 Vue Admin 내장.

1.  **Backend Setup:** `backend` 폴더에 Spring Boot 생성.
2.  **Admin Setup:** `backend/src/main/vue-admin` 폴더에 Vue 3 + Vite 생성.
3.  **Build Config:** `build.gradle`에 `gradle-node-plugin` 설정 (AI에게 요청).
4.  **Code Refactoring:**
    > **[CLI Prompt]**
    > "`.docs/3_CODING_CONVENTION.md`의 **Java Controller** 규칙을 참고해.
    > 기존 `BizController.java`를 주석 섹션(DI, Public, Private)에 맞춰 재정렬하고,
    > 리턴 타입을 `ApiResponse`로 감싸줘."
5.  **Grid Migration:**
    > **[CLI Prompt]**
    > "`.docs/3_CODING_CONVENTION.md`의 **Vue.js** 규칙을 참고해.
    > 기존 React Grid(`Biz.tsx`)를 Vue Composition API로 변환해줘.
    > `<ComGrid>` 컴포넌트를 사용하고, API는 별도 모듈로 분리해."

---

## Phase 4. Final Verification
**목표:** 전체 시스템 유기적 동작 확인.

1.  **Full Build:** 루트에서 `docker-compose up --build -d` 실행.
2.  **Flow Test:**
    - 홈페이지 접속 (`localhost`) -> 정상?
    - 관리자 접속 (`localhost/admin`) -> 로그인 페이지 뜸?
    - 로그인 시도 -> Spring Boot API 호출 (`/api/auth/login`) -> 성공?
    - 관리자 메뉴 이동 -> 권한에 따른 메뉴 로딩 확인.