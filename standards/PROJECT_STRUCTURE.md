# 5. Project Structure & Environment Standard

## 5.1 Overview
모든 프로젝트는 **예측 가능한(Predictable)** 구조를 가져야 합니다.
개발자가 새로운 프로젝트(폴더)를 열었을 때, 어디에 설정 파일이 있고 어디에 비즈니스 로직이 있는지 즉시 파악할 수 있어야 합니다.

---

## 5.2 [Backend] Spring Boot Standard

### 5.2.1 Directory Layout
```text
backend/
├── Dockerfile                  # (Essential) Production Build Recipe
├── build.gradle                # (Essential) Dependency Management
├── .gitignore
├── src/
│   ├── main/
│   │   ├── java/com/comfunny/
│   │   │   ├── global/         # 공통 설정 (Config, Error, Util, Security)
│   │   │   └── domain/         # 비즈니스 도메인 (User, Order, Biz)
│   │   │       ├── [domainName]/
│   │   │       │   ├── api/        # Presentation Layer (Controller, Dto)
│   │   │       │   ├── application/# Business Layer (Service, Facade)
│   │   │       │   ├── dao/        # Persistence Layer (Repository, Entity)
│   │   │       │   └── domain/     # Domain Core (Aggregate Root, Value Object)
│   │   └── resources/
│   │       ├── application.yml      # (Essential) Common Config (UTF-8, Timezone)
│   │       ├── application-local.yml
│   │       ├── application-dev.yml
│   │       └── application-prod.yml # (Essential) Production Config
```

### 5.2.2 Essential Files Checklist
- [ ] `Dockerfile`: Multi-stage build 포함.
- [ ] `application.yml`: 공통 설정.
- [ ] `global/config/SecurityConfig.java`: 보안 설정.

### 5.2.3 Directory Layout (Spring Boot + Thymeleaf)
SSR(Server Side Rendering)이 필요한 경우, `resources` 하위 구조를 따릅니다.
```text
src/main/resources/
├── static/                     # (Public) JS, CSS, Images
│   ├── css/
│   ├── js/
│   └── images/
└── templates/                  # (Private) HTML Templates
    ├── layout/                 # Base Layouts (header, footer included)
    ├── fragments/              # Reusable Components
    └── domain/                 # Domain specific pages (user, order)
```

---

## 5.3 [Frontend] Next.js / Vue.js Standard

### 5.3.1 Directory Layout (Next.js)
```text
frontend-nextjs/
├── Dockerfile
├── package.json
├── next.config.js
├── src/
│   ├── app/                    # App Router Root
│   │   ├── layout.tsx          # Global Layout
│   │   └── page.tsx            # Home Page
│   ├── components/
│   │   ├── ui/                 # Atomic UI Components (Buttons, Inputs)
│   │   └── features/           # Domain Specific Components
│   └── lib/                    # Utils, API Clients
├── .env.local                  # (Essential) Local Secrets
├── .env.production             # (Essential) Production Variables
└── public/                     # Static Assets
```
> **Note:**
> All projects must include the **Applied Standard Version** in their `PROJECT_DEFINITION.md` or `README.md`.
> Example: `> **Applied Standard Version:** v1.0.0`

### 5.3.2 Directory Layout (Vue.js - Vite)
```text
frontend-admin/
├── Dockerfile
├── package.json
├── vite.config.ts
├── index.html                  # (Entry) Vite Root Entry
├── src/
│   ├── main.ts                 # App Mount Point
│   ├── App.vue                 # Root Component
│   ├── router/                 # Vue Router Configuration
│   ├── stores/                 # Pinia State Management
│   ├── components/             # Shared UI Components
│   ├── views/                  # Page Components (matches Router)
│   └── composables/            # Reusable Logic (Hooks)
└── public/                     # Static Assets (favicon, robots.txt)
```

---

## 5.5 Mobile Application Standard
모바일 앱은 **Clean Architecture**와 **MVVM/Bloc** 패턴을 준수합니다.

### 5.5.1 Flutter (Cross Platform)
```text
lib/
├── main.dart
├── src/
│   ├── data/                   # Data Layer (Repository Impl, Datasource)
│   ├── domain/                 # Domain Layer (Entity, Repository Interface, Usecase)
│   └── presentation/           # UI Layer (Widgets, Bloc/Provider)
│       ├── common/             # Shared Widgets
│       └── features/           # Feature-based folders (login, home)
└── assets/                     # Fonts, Images (pubspec.yaml registered)
```

### 5.5.2 Android (Native Kotlin)
```text
app/src/main/
├── AndroidManifest.xml
├── java/com/comfunny/app/
│   ├── di/                     # Dependency Injection (Hilt/Koin)
│   ├── data/                   # API, DB, Repository Impl
│   ├── domain/                 # Usecase, Model
│   └── ui/                     # Activities, Fragments, ViewModels
└── res/
    ├── layout/                 # XML layouts
    └── values/                 # Strings, Colors, Themes
```

### 5.5.3 iOS (Native Swift)
```text
App/
├── Sources/
│   ├── Application/            # AppDelegate, SceneDelegate
│   ├── Presentation/           # Views (SwiftUI/UIKit), ViewModels
│   ├── Domain/                 # Entities, Usecases, Repository Protocols
│   └── Data/                   # Network, Persistent Storage
└── Resources/
    ├── Assets.xcassets         # Images, Colors
    └── Localizable.strings     # i18n
```

---

## 5.4 Environment Profiles (Env Strategy)
각 환경은 아래 기준에 따라 엄격히 분리 운영합니다.

| Feature | Local | Dev | Prod |
| :--- | :--- | :--- | :--- |
| **DB** | H2 / Dockerized MySQL | Shared Dev DB (AWS RDS) | Production DB (AWS RDS) |
| **Logging** | DEBUG (Console) | INFO (File/Console) | INFO (JSON -> CloudWatch) |
| **DDL** | `create-drop` or `update` | `validate` or `none` | `validate` or `none` |
| **Swagger** | Enable | Enable | **Disable** |


---

<!-- DETAILED GUIDE START -->

# 5. Project Structure & Environment Standard (Detailed Guide)

## 1. 개요 (Overview)
`5_PROJECT_STRUCTURE.md`가 뼈대를 설명했다면, 이 문서는 **"왜 이렇게 나누었는가"**와 **"환경별 상세 설정 템플릿"**을 제공합니다.

## 2. Backend 구조 상세 (Layered Architecture)

### 2.1 Global vs Domain
- **global/**: 프로젝트 전반에 영향을 미치는 인프라성 코드를 모읍니다.
    - `config/`: Spring 설정 (`WebMvcConfig`, `SwaggerConfig`)
    - `error/`: 전역 예외 처리 (`GlobalExceptionHandler`)
    - `security/`: 인증/인가 필터 (`JwtAuthenticationFilter`)
- **domain/**: 실제 비즈니스 로직이 위치합니다. 도메인별로 패키지를 격리하여(Package by Feature) 향후 마이크로서비스 분리(MSA)를 용이하게 합니다.

### 2.2 Domain 내부 계층 (Hexagonal Style 지향)
- **api (Presentation):** 외부 요청을 받아 DTO로 변환하고 응답을 반환. 비즈니스 로직 금지.
- **application (Application):** 트랜잭션 관리, 도메인 객체 간의 조율.
- **dao (Infrastructure):** DB, Redis 등 외부 저장소와의 통신.
- **domain (Domain Core):** 순수 자바 객체(Entity, VO). 프레임워크 의존성 최소화.

## 3. Configuration Templates (환경 설정 예시)

### 3.1 application-local.yml (개발자 PC용)
로컬에서는 개발 편의성을 최우선으로 합니다. P6Spy 등을 통해 쿼리를 직관적으로 볼 수 있게 합니다.

```yaml
spring:
  datasource:
    url: jdbc:h2:mem:testdb;MODE=MySQL
    username: sa
  jpa:
    hibernate:
      ddl-auto: update # 개발 중엔 스키마 자동 변경 허용
    show-sql: true
    properties:
      hibernate.format_sql: true
logging:
  level:
    root: INFO
    com.comfunny: DEBUG # 우리 프로젝트 로그는 자세히
```

### 3.2 application-prod.yml (운영용)
운영 환경은 **안정성**과 **보안**이 최우선입니다.

```yaml
spring:
  datasource:
    url: ${DB_URL} # 환경 변수로 주입 (보안)
    username: ${DB_USER}
    password: ${DB_PASS}
  jpa:
    hibernate:
      ddl-auto: validate # 스키마 변경 절대 금지
    show-sql: false # 성능 저하 방지
logging:
  level:
    root: INFO
    com.comfunny: INFO
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n" # JSON 포맷 권장
```

## 4. Initializing a New Project (Checklist)
새 프로젝트 생성(`init`) 시 아래 단계를 반드시 수행하십시오.

1.  **Clone Skeleton:** 기존 잘 된 프로젝트나 스켈레톤 코드를 복제합니다.
2.  **Rename Packages:** 패키지명을 서비스에 맞게 일괄 변경합니다 (Refactor -> Rename).
3.  **Clean Up:** 불필요한 예제 코드(`HelloController`) 삭제.
4.  **Health Check:** `Local` 프로파일로 구동하여 `GET /actuator/health` 정상 응답 확인.

## 5. Platform Specific Details

### 5.1 Thymeleaf (SSR) Strategy
- **Layout Dialect:** `nz.net.ultraq.thymeleaf:thymeleaf-layout-dialect`를 사용하여 중복(Header/Footer)을 제거합니다.
- **Fragment:** 재사용 가능한 UI 조각(버튼, 모달)은 `templates/fragments/`에 두어 `th:replace`로 주입합니다.

### 5.2 Vue.js (Vite) Strategy
- **Index.html Location:** Vite는 `index.html`이 프로젝트 루트에 있어야 합니다. (Webpack 기반인 Vue CLI와 다름)
- **Env Variables:**
    - `.env` 파일의 변수는 `VITE_` 접두사가 있어야 클라이언트(`import.meta.env`)에서 접근 가능합니다.

### 5.3 Mobile Architecture Strategy
- **Flutter:**
    - **Bloc/Cubit:** 상태 관리는 Bloc 패턴을 표준으로 합니다.
    - **Freezed:** 불변 객체(Immutability)와 Union Type 사용을 위해 `freezed` 패키지 사용을 권장합니다.
- **Native (Android/iOS):**
    - **Jetpack Compose / SwiftUI:** 선언형 UI(Declarative UI)를 기본으로 채택합니다.
    - **Dependency Injection:** Android는 `Hilt`, iOS는 `Swinject` (또는 Native Factory)를 사용합니다.
