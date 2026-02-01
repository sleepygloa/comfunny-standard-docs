# Flutter 개발 표준 가이드

## 1. 아키텍처 패턴: MVVM (with Riverpod)
모든 Flutter 프로젝트는 Riverpod를 활용한 MVVM 패턴을 따릅니다.
- **Model (Data Layer)**: DTO 및 데이터 소스.
- **View (UI Layer)**: 위젯 및 화면. 비즈니스 로직을 포함할 수 없습니다.
- **ViewModel (State Layer)**: Riverpod의 `StateNotifier` 또는 `Notifier`. 비즈니스 로직과 상태 업데이트를 담당합니다.

## 2. 디렉토리 구조
```text
lib/
├── models/                  # DTOs (Data Transfer Objects)
├── repositories/            # 데이터 접근 계층 (API, Firestore, Local DB)
├── viewmodels/              # 상태 관리 (Providers)
├── views/                   # UI 컴포넌트 및 화면
│   ├── [feature]/
│   │   └── [feature]_screen.dart
├── utils/                   # 공통 유틸리티
└── main.dart
```

## 3. 코딩 표준
### 3.1 코드 섹션 분리
파일(특히 UI)은 표준 주석 블록을 사용하여 명확한 섹션으로 나누어야 합니다:
```dart
// **************************************************************************
// ********** Section Name **********
// **************************************************************************
```
**UI 위젯 내 권장 순서**:
1. Constants & Controllers (상수 및 컨트롤러)
2. State Variables (상태 변수)
3. Lifecycle Methods (생명주기 메서드)
4. Business Logic Helpers (비즈니스 로직 헬퍼)
5. Main Build Method (메인 빌드 메서드)
6. Sub-widget Builders (하위 위젯 빌더)

### 3.2 린터 규칙 (Linter Rules)
- **따옴표**: 작은따옴표(`'`)를 엄격하게 사용합니다.
- **Const**: 리빌드 최적화를 위해 가능한 모든 곳에 `const` 생성자를 사용합니다.
- **출력**: `print()`를 사용하지 마세요. `debugPrint()` 또는 구조화된 로거를 사용하세요.
- **타입**: 추론이 명확하지 않은 경우 반환 타입과 변수 타입을 항상 명시적으로 선언하세요.

## 4. 네이밍 규칙
- **파일**: `snake_case` (예: `user_profile_screen.dart`)
- **클래스**: `PascalCase` (예: `UserProfileScreen`)
- **변수/함수**: `camelCase` (예: `fetchUserData`)
