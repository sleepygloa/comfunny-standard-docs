### 📂 3. `.docs/2_TECH_STACK.md` (기술 스택 확정)
> **변경점:** "MyBatis를 쓴다"가 아니라 "복잡한 쿼리는 MyBatis, 단순 CRUD는 JPA"처럼 **사용 기준**을 명시합니다.

```markdown
# [A-01] Technology Stack & Decision Records

## 목차

<!-- toc -->

  * [A-01-2.1 Backend (Spring Boot)](#a-01-21-backend-spring-boot)
  * [A-01-2.2 Frontend 1 (Next.js - Public Web)](#a-01-22-frontend-1-nextjs---public-web)
  * [A-01-2.3 Frontend 2 (Vue.js - Admin)](#a-01-23-frontend-2-vuejs---admin)
  * [A-01-2.4 Mobile Application](#a-01-24-mobile-application)
- [[A-01] Technology Stack & Decision Records (Detailed Guide)](#a-01-technology-stack--decision-records-detailed-guide)
  * [A-01-1. 개요 (Overview)](#a-01-1-%EA%B0%9C%EC%9A%94-overview)
  * [A-01-2. Backend (Spring Boot) 상세 전략](#a-01-2-backend-spring-boot-%EC%83%81%EC%84%B8-%EC%A0%84%EB%9E%B5)
    + [A-01-2.1 Hybrid ORM 전략 (JPA + MyBatis)](#a-01-21-hybrid-orm-%EC%A0%84%EB%9E%B5-jpa--mybatis)
    + [A-01-2.2 인증/인가 (Spring Security + JWT)](#a-01-22-%EC%9D%B8%EC%A6%9D%EC%9D%B8%EA%B0%80-spring-security--jwt)
  * [A-01-3. Frontend 상세 전략](#a-01-3-frontend-%EC%83%81%EC%84%B8-%EC%A0%84%EB%9E%B5)
    + [A-01-3.1 Next.js (Public Web) - SEO & Performance](#a-01-31-nextjs-public-web---seo--performance)
    + [A-01-3.2 Vue 3 (Admin) - Productivity](#a-01-32-vue-3-admin---productivity)
  * [A-01-4. Build & CI Integration](#a-01-4-build--ci-integration)

<!-- tocstop -->

## A-01-2.1 Backend (Spring Boot)
| 구분 | 기술 / 라이브러리 | 버전 / 선정 이유 |
| :--- | :--- | :--- |
| **Framework** | Spring Boot | 3.2.x (Java 17) |
| **ORM (Command)** | Spring Data JPA | 단순 CRUD 및 도메인 로직 처리 |
| **ORM (Query)** | QueryDSL 5.0 | 동적 쿼리 및 Type-Safe 조회 |
| **SQL Mapper** | MyBatis 3.5 | 통계, 배치, 복잡한 네이티브 SQL 필요 시 사용 |
| **Auth** | Spring Security + JWT | Stateless 인증 아키텍처 |
| **Build** | Gradle (Groovy) | `gradle-node-plugin` 활용한 프론트 빌드 통합 |

## A-01-2.2 Frontend 1 (Next.js - Public Web)
| 구분 | 기술 / 라이브러리 | 버전 / 선정 이유 |
| :--- | :--- | :--- |
| **Core** | Next.js | 14.0+ (App Router 필수) |
| **Language** | TypeScript | 5.x (Strict Mode) |
| **Styling** | Tailwind CSS | Utility-first CSS |
| **State** | Zustand | (필요 시) 전역 상태 관리 |
| **Fetch** | Native Fetch | Server Component 캐싱 활용 (Axios 지양) |

## A-01-2.3 Frontend 2 (Vue.js - Admin)
| 구분 | 기술 / 라이브러리 | 버전 / 선정 이유 |
| :--- | :--- | :--- |
| **Core** | Vue 3 | Composition API (`<script setup>`) |
| **Build** | Vite | 빠른 HMR 및 빌드 속도 |
| **State** | Pinia | Vuex 대체, TypeScript 친화적 |
| **UI Kit** | Tailwind CSS + Headless UI | 커스텀 디자인 시스템 (`ComGrid` 등) 구현 |
| **Http** | Axios | Interceptor를 통한 토큰/에러 공통 처리 |

## A-01-2.4 Mobile Application
| 구분 | 기술 / 라이브러리 | 아키텍처 / 선정 이유 |
| :--- | :--- | :--- |
| **Android** | Kotlin, Jetpack Compose | **MVVM + Clean Architecture** (Hilt, Coroutines, Flow) |
| **iOS** | Swift, SwiftUI | **MVVM + Clean Architecture** (Combine, Async/Await) |
| **Flutter** | Dart, Flutter 3.x | **BLoC Pattern + Clean Architecture** (GetIt, Dio) |

## A-01-2.5 Local AI Worker (Hybrid Architecture)
| 구분 | 기술 / 라이브러리 | 버전 / 선정 이유 |
| :--- | :--- | :--- |
| **Language** | Python | 3.11.x (머신러닝 및 AI 라이브러리 생태계 표준) |
| **Framework** | Native (또는 FastAPI) | 가벼운 폴링(Polling) 스크립트 또는 마이크로서비스 |
| **TTS** | `edge-tts` | 빠르고 자연스러운 무료 고품질 음성 합성 |
| **Avatar (Lip-Sync)** | `SadTalker` / `Wav2Lip` | 이미지 + 음성 기반 립싱크 비디오 생성 (로컬 GPU 가속: PyTorch, CUDA 12.1+) |
| **Media Edit** | `moviepy` / `ffmpeg` | 파이썬 레벨의 빠르고 유연한 미디어 후처리(병합/컷 편집) |


---

<!-- DETAILED GUIDE START -->

# [A-01] Technology Stack & Decision Records (Detailed Guide)

## A-01-1. 개요 (Overview)
본 문서는 `2_TECH_STACK.md`에 정의된 기술 스택에 대한 상세한 선정 근거와 활용 전략을 기술합니다.
단순히 "무엇을 쓰는가"를 넘어 **"왜 쓰는가"**와 **"어떻게 최적화하여 사용하는가"**를 설명합니다.

## A-01-2. Backend (Spring Boot) 상세 전략

### A-01-2.1 Hybrid ORM 전략 (JPA + MyBatis)
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

### A-01-2.2 인증/인가 (Spring Security + JWT)
- **Stateful vs Stateless:**
    - 우리는 **Stateless**를 지향하므로 Session 대신 **JWT (Access + Refresh Token)** 방식을 채택합니다.
    - **Rotation 전략:** Refresh Token은 DB(Redis)에 저장하여 탈취 시 강제 만료(Logout)시킬 수 있도록 구현해야 합니다.

## A-01-3. Frontend 상세 전략

### A-01-3.1 Next.js (Public Web) - SEO & Performance
- **Server Components (RSC):**
    - **Why:** 클라이언트 번들 사이즈를 줄이고, 초기 로딩 속도(FCP)를 개선하며, 검색 엔진 크롤러에게 완성된 HTML을 제공하기 위함입니다.
    - **Rule:**
        - `useState`, `useEffect`가 필요한 경우에만 `"use client"`를 명시합니다.
        - 데이터 페칭은 가능한 서버 컴포넌트(`page.tsx`)에서 수행합니다.

### A-01-3.2 Vue 3 (Admin) - Productivity
- **Composition API:**
    - **Why:** Options API는 코드가 분산되어 유지보수가 어렵습니다. 관련된 로직(상태, 메서드)을 한 곳에 뭉칠 수 있는 Composition API가 대규모 어드민 개발에 더 적합합니다.
    - **Guide:** `composables/` 폴더를 적극 활용하여 비즈니스 로직(예: 페이징, 폼 검증)을 재사용 가능한 함수로 분리하십시오.

## A-01-4. Build & CI Integration
- **Mono-build Strategy:**
    - Gradle이 빌드의 주체가 되어 `node` 환경까지 제어합니다.
    - **이점:** 백엔드 개발자가 프론트엔드 환경 세팅 없이 `./gradlew build` 하나로 전체 아티팩트를 생성할 수 있습니다.

## A-01-5. AI Local Worker (Hybrid AI Architecture) 상세 전략

### A-01-5.1 Cloud-Local 하이브리드 구조의 당위성
- 비싼 클라우드 GPU(인스턴스) 비용을 절감하기 위해, **제어/웹 인스턴스는 Cloud(Firebase/Next.js)**에, 무거운 **AI 추론(Inference)은 로컬 PC의 GPU(RTX 4060 등)**를 활용하는 분리 아키텍처를 권장합니다.
- **Workflow:** Web App (Job 지시) ➡️ Firestore (Queue/PENDING) ➡️ Local Python Worker (감지 및 생성) ➡️ Firebase Storage (업로드) ➡️ Web App (결과 확인)

### A-01-5.2 Python 환경 관리의 파편화 방지
- **Why:** 파이썬은 패키지 의존성 출돌이 매우 잦으므로 글로벌 환경(`pip install`) 설치를 엄격히 금지합니다.
- **Rule:** 
  1. 각 Worker 프로젝트는 반드시 최상단에 `venv` (가상환경)를 구성해야 합니다.
  2. 추론 모델(SadTalker 등) 구동을 위한 서브 모듈도 각각의 전용 가상환경을 분리 생성하여 서브프로세스(`subprocess.run`)로 호출합니다.
  3. 모든 의존성은 명시적인 `requirements.txt` 로 관리합니다.
