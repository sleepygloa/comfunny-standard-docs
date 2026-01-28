# 2. Technology Stack & Decision Records (Detailed Guide)

## 1. 개요 (Overview)
본 문서는 `2_TECH_STACK.md`에 정의된 기술 스택에 대한 상세한 선정 근거와 활용 전략을 기술합니다.
단순히 "무엇을 쓰는가"를 넘어 **"왜 쓰는가"**와 **"어떻게 최적화하여 사용하는가"**를 설명합니다.

## 2. Backend (Spring Boot) 상세 전략

### 2.1 Hybrid ORM 전략 (JPA + MyBatis)
엔터프라이즈 환경에서는 생산성과 성능, 유연성 세 마리 토끼를 다 잡아야 합니다.

- **JPA (Command - C/U/D):**
    - **Why:** 비즈니스 객체(Entity)의 상태 변경을 안전하게 관리하기 위함. Dirty Checking을 통해 SQL 실수를 방지를 보장합니다.
    - **Usage:**
        - 단순 CRUD (findById, save, delete)
        - 도메인 로직이 포함된 상태 변경 (e.g. `order.cancel()`)
    - **Best Practice:** `@DynamicUpdate`는 컬럼이 많을 때만 사용하며, 기본적으로는 전체 필드를 업데이트하는 것이 캐시 히트율에 유리합니다.

- **MyBatis / JOOQ (Query - R):**
    - **Why:** 통계 쿼리, 복잡한 조인, 윈도우 함수 등 SQL 최적화가 필수적인 조회 영역에서 JPA는 오버헤드가 큽니다.
    - **Usage:**
        - 대시보드 통계 데이터 조회 (GROUP BY, UNION 다수 포함)
        - 엑셀 다운로드용 대용량 데이터 조회
    - **Tip:** `ResultMap`을 재사용하여 DTO 매핑 생산성을 높이십시오.

### 2.2 인증/인가 (Spring Security + JWT)
- **Stateful vs Stateless:**
    - 우리는 **Stateless**를 지향하므로 Session 대신 **JWT (Access + Refresh Token)** 방식을 채택합니다.
    - **Rotation 전략:** Refresh Token은 DB(Redis)에 저장하여 탈취 시 강제 만료(Logout)시킬 수 있도록 구현해야 합니다.

## 3. Frontend 상세 전략

### 3.1 Next.js (Public Web) - SEO & Performance
- **Server Components (RSC):**
    - **Why:** 클라이언트 번들 사이즈를 줄이고, 초기 로딩 속도(FCP)를 개선하며, 검색 엔진 크롤러에게 완성된 HTML을 제공하기 위함입니다.
    - **Rule:**
        - `useState`, `useEffect`가 필요한 경우에만 `"use client"`를 명시합니다.
        - 데이터 페칭은 가능한 서버 컴포넌트(`page.tsx`)에서 수행합니다.

### 3.2 Vue 3 (Admin) - Productivity
- **Composition API:**
    - **Why:** Options API는 코드가 분산되어 유지보수가 어렵습니다. 관련된 로직(상태, 메서드)을 한 곳에 뭉칠 수 있는 Composition API가 대규모 어드민 개발에 더 적합합니다.
    - **Guide:** `composables/` 폴더를 적극 활용하여 비즈니스 로직(예: 페이징, 폼 검증)을 재사용 가능한 함수로 분리하십시오.

## 4. Build & CI Integration
- **Mono-build Strategy:**
    - Gradle이 빌드의 주체가 되어 `node` 환경까지 제어합니다.
    - **이점:** 백엔드 개발자가 프론트엔드 환경 세팅 없이 `./gradlew build` 하나로 전체 아티팩트를 생성할 수 있습니다.
