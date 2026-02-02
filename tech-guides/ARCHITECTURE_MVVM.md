# 아키텍처: MVVM + 클린 아키텍처

## 개요
이 프로젝트는 **클린 아키텍처** 원칙과 통합된 엄격한 **MVVM (Model-View-ViewModel)** 패턴을 따릅니다.
상태 관리는 **Riverpod**에 의해 처리됩니다.

## 레이어 (계층)

### 1. 프레젠테이션 레이어 (View)
*   **경로**: `lib/presentation/`
*   **역할**: UI 렌더링 및 사용자 상호작용.
*   **구성 요소**: `ConsumerStatefulWidget`, `ConsumerWidget`.
*   **규칙**:
    *   UI에 비즈니스 로직 없음.
    *   반응형 업데이트를 위해 `ref.watch(provider)` 사용.
    *   작업 트리거를 위해 `ref.read(provider.notifier)` 사용.

### 2. 애플리케이션 레이어 (ViewModel)
*   **경로**: `lib/application/`
*   **역할**: 상태 관리, 비즈니스 로직 조정, UI와 도메인 간의 브리지.
*   **구성 요소**: `StateNotifier` (`LedgerNotifier`), 서비스 (`AiService`).
*   **규칙**:
    *   상태 관리 (`LedgerState`).
    *   사이드 이펙트 처리 (AI 호출, 알림).
    *   Flutter UI 위젯에 직접 의존하지 않음.

### 3. 도메인 레이어 (Model)
*   **경로**: `lib/domain/`
*   **역할**: 순수 비즈니스 엔티티 및 로직.
*   **구성 요소**: 엔티티 (`TransactionEntity`), 도메인 서비스 (`StatisticsService`).
*   **규칙**:
    *   순수 Dart 코드.
    *   인프라스트럭처 또는 프레젠테이션 레이어에 대한 의존성 없음.

### 4. 인프라스트럭처 레이어 (Model/Data)
*   **경로**: `lib/infrastructure/`
*   **역할**: 데이터 지속성 및 외부 API 통신.
*   **구성 요소**: 리포지토리 (`SyncLedgerRepository`), DTO.
*   **규칙**:
    *   데이터 액세스 구현 (Isar, Firestore).
    *   오프라인 우선 동기화 로직 처리.

## 디렉토리 구조
```
lib/
├── application/       # StateNotifiers, Providers, 앱 서비스
├── domain/            # 엔티티, 도메인 서비스
├── infrastructure/    # 리포지토리 (Isar/Firestore 구현)
├── presentation/      # 화면, 위젯
└── utils/             # 헬퍼, 확장
```
