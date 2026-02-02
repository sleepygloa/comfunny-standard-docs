# Mobile Application Guide (Init & Run)

## 1. Overview
모바일 애플리케이션은 **Clean Architecture** 원칙을 준수하여 **Presentation**, **Domain**, **Data** 레이어를 엄격히 분리합니다.
플랫폼별 최신 디자인 패턴(MVVM, BLoC)을 채택하여 유지보수성과 테스트 용이성을 확보합니다.

---

## 2. Flutter (Cross Platform)

### 2.1 Initialization
```bash
# 1. Create Project
flutter create --org com.comfunny --project-name comfunny_app .

# 2. Add Dependencies (pubspec.yaml)
flutter pub add flutter_bloc get_it go_router dio
flutter pub add --dev build_runner from_json_generator
```

### 2.2 아키텍처 패턴 (MVVM + Clean Architecture)
우리는 **Riverpod**를 활용한 MVVM 패턴과 **Clean Architecture** 계층 구조를 엄격히 준수합니다.

#### 2.2.1 레이어 정의 (Layer Definition)
1.  **Presentation Layer (UI)**: `lib/presentation/`
    -   **역할**: UI 렌더링 및 사용자 상호작용.
    -   **규칙**: 비즈니스 로직 포함 금지. `ref.watch`로 상태를 구독하고, `ref.read`로 작업을 트리거합니다.
2.  **Application Layer (ViewModel)**: `lib/application/`
    -   **역할**: 상태 관리, 비즈니스 로직 조율.
    -   **구성 요소**: `Notifier` (Riverpod), Service.
    -   **규칙**: Flutter UI 위젯에 의존하지 않습니다 (순수 Dart 지향).
3.  **Domain Layer (Model)**: `lib/domain/`
    -   **역할**: 핵심 비즈니스 로직 및 엔티티 정의.
    -   **구성 요소**: Entity, Repository Interface, Usecase.
    -   **규칙**: 외부 라이브러리 의존성을 최소화한 순수 Dart 영역입니다.
4.  **Infrastructure Layer (Data)**: `lib/infrastructure/`
    -   **역할**: 실제 데이터 입출력 (API, DB).
    -   **구성 요소**: Repository Impl, DTO, Datasource.

### 2.3 디렉토리 구조 (Directory Structure)
```text
lib/
├── core/                       # 공통 설정 (Config, Constants, Extensions)
├── application/                # [App Layer] StateNotifiers, Providers
├── domain/                     # [Domain Layer] Entity, Repository Interface
│   ├── entities/
│   └── repositories/
├── infrastructure/             # [Infra Layer] Repository Impl, DTO
│   ├── datasources/
│   ├── models/                 # DTO
│   └── repositories/           # Impl
├── presentation/               # [Presentation Layer] Screens, Widgets
│   ├── common/
│   └── features/               # 기능별 폴더 (예: login, home)
│       └── [feature_name]/
│           ├── [feature]_screen.dart
│           └── widgets/
└── main.dart
```

### 2.4 코딩 표준 (Coding Standards)
#### 2.4.1 코드 섹션 분리 (Section Separator)
파일(특히 UI)은 표준 주석 블록을 사용하여 명확히 구분해야 합니다.
```dart
// **************************************************************************
// ********** Section Name **********
// **************************************************************************
```
**순서 (UI 위젯):**
1. Constants & Controllers
2. State Variables (`ref.watch`)
3. Lifecycle Methods (`useEffect`)
4. Main Build Method
5. Sub-widget Builders

#### 2.4.2 린터 규칙 (Linter Rules)
- **따옴표**: 작은따옴표(`'`)를 강제합니다.
- **Const**: 가능한 모든 곳에 `const`를 사용하여 리빌드를 최적화합니다.
- **Print 금지**: `debugPrint()` 또는 로거를 사용하십시오.

### 2.3 Run Command
```bash
# Run Dev
flutter run --flavor dev -t lib/main_dev.dart

# Build APK
flutter build apk --flavor prod -t lib/main_prod.dart
```

---

## 3. Android (Native Kotlin)

### 3.1 Initialization (Hilt Setup)
`build.gradle.kts` (Module):
```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("com.google.dagger.hilt.android") // Hilt
}

dependencies {
    implementation("com.google.dagger:hilt-android:2.48")
    kapt("com.google.dagger:hilt-android-compiler:2.48")
}
```

### 3.2 Structure & Pattern (MVVM + Clean Arch)
Android는 **MVVM** 패턴과 **Unidirectional Data Flow**를 지향합니다.

```text
com.comfunny.app
├── di/                         # Hilt Modules
├── data/                       # [Data Layer]
│   ├── api/                    # Retrofit Interfaces
│   ├── repository/             # Repository Impl
│   └── source/                 # Room DB, SharedPref
├── domain/                     # [Domain Layer]
│   ├── usecase/                # Execute Business Logic
│   ├── model/                  # Data Class
│   └── repository/             # Repository Interface
└── ui/                         # [Presentation Layer]
    ├── theme/                  # Compose Theme
    └── features/               # Feature-based Separation
        └── login/
            ├── LoginScreen.kt  # Composable (Stateless)
            ├── LoginViewModel.kt # StateFlow Holder
            └── LoginRoute.kt   # Navigation & State-Hoisting
```
**Rule:**
- `ViewModel`은 `StateFlow`를 통해 UI 상태를 노출합니다.
- `Composable`은 상태를 직접 변경하지 않고 `Event`를 `ViewModel`로 전달합니다.

---

## 4. iOS (Native Swift)

### 4.1 Initialization (SPM)
- **Dependency Manager:** Swift Package Manager (SPM) 권장.
- **Libs:** `TheComposableArchitecture` (TCA) or `ReactorKit` + `Moya` (Network)

### 4.2 Structure & Pattern (MVVM + Clean Arch)
iOS는 **MVVM**을 기본으로 하되, 복잡한 상태 관리가 필요한 경우 **TCA**를 허용합니다.

```text
App/
├── Sources/
│   ├── App.swift
│   ├── Data/                   # [Data Layer] Network, Persistent
│   │   ├── Network/            # Moya/Alamofire Target
│   │   └── Repositories/       # Repository Implementation
│   ├── Domain/                 # [Domain Layer]
│   │   ├── Entities/           # Struct Models
│   │   ├── UseCases/           # Business Logic
│   │   └── Interfaces/         # Repository Protocols (Dependency Inversion)
│   └── Presentation/           # [Presentation Layer]
│       ├── Components/         # Common SwiftUI Views
│       └── Scenes/             # Pages
│           └── Home/
│               ├── HomeView.swift      # SwiftUI View
│               └── HomeViewModel.swift # ObservableObject
└── Tests/
```
**Rule:**
- `ViewModel`은 `ObservableObject` 프로토콜을 따릅니다.
- View는 `ViewModel`의 Published 프로퍼티를 바인딩합니다.
