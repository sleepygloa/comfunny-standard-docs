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

### 2.2 Project Structure & Pattern (BLoC + Clean Arch)
Flutter는 **BLoC Pattern**을 표준으로 합니다.

```text
lib/
├── main.dart
├── core/                       # Config, Constants, DI (GetIt)
├── src/
│   ├── data/                   # [Data Layer] RepositoryImpl, DTO, Datasource
│   │   ├── datasource/         # remote, local
│   │   ├── repository_impl/
│   │   └── models/             # DTO (fromJson)
│   ├── domain/                 # [Domain Layer] Entity, Repository (Interface), Usecase
│   │   ├── entities/           # Pure Dart Object
│   │   ├── repositories/       # Interface
│   │   └── usecases/           # Business Logic
│   └── presentation/           # [Presentation Layer] BLoC, Screen, Widget
│       ├── bloc/               # State Management
│       ├── view/               # Screen (Scaffold)
│       └── widget/             # Reusable UI
└── assets/
```
**Rule:**
- UI는 오직 BLoC의 State만 바라봅니다.
- Business Logic은 Usecase에 위임합니다.

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
