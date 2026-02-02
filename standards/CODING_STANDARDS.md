# 코딩 표준 및 컨벤션

## 1. 코드 구조 (섹션 분리)
파일(특히 UI)은 표준 주석 블록을 사용하여 명확한 섹션으로 구분해야 합니다:
```dart
// **************************************************************************
// ********** 섹션 이름 **********
// **************************************************************************
```
**순서**:
1. 상수 및 컨트롤러 (Constants & Controllers)
2. 상태 변수 (State Variables)
3. 수명 주기 메서드 (Lifecycle Methods)
4. 비즈니스 로직 (Business Logic)
5. 데이터 지속성 (Data Persistence)
6. 메인 빌드 메서드 (Main Build Method)
7. 위젯 빌더 (Widget Builders)

## 2. 린터 규칙 (`analysis_options.yaml`)
*   **따옴표**: 엄격하게 작은따옴표(`'`)를 사용합니다.
*   **Const**: 가능한 모든 곳에 `const` 생성자를 사용합니다.
*   **출력**: `print()`를 사용하지 마십시오. `debugPrint()` 또는 로거를 사용하십시오.
*   **타입**: 항상 반환 타입을 선언합니다.

## 3. 에러 처리
*   **파싱**: 사용자 입력에는 `try-catch` 또는 안전한 파싱 도우미(예: `double.tryParse`)를 사용합니다.
*   **Null 안전성**: Firestore의 `null` 값을 명시적으로 처리합니다(기본값 제공).

## 4. 명명 규칙
*   **변수**: `camelCase` (예: `ledgerDate`).
*   **파일**: `snake_case` (예: `transaction_entity.dart`).
*   **클래스**: `PascalCase` (예: `TransactionEntity`).
