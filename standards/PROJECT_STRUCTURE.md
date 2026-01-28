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
