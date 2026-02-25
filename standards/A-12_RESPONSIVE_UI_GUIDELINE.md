# A-12 RESPONSIVE UI GUIDELINE

## 1. 개요 (Overview)
본 문서는 모든 애플리케이션(Web, Mobile, Tablet)이 단일 코드베이스 또는 반응형 아키텍처를 통해 **초대형 모니터(1920px 이상)부터 데스크톱, 스마트패드(iPad, Galaxy Tab), 그리고 모바일(세로/가로)** 환경까지 완벽하게 호환되도록 개발하기 위한 전사 표준 가이드입니다.

## 2. 반응형 개발 핵심 원칙 (Core Principles)
1. **Mobile First & Scalable (모바일 우선 및 확장성):** 모바일 뷰를 기준으로 디자인을 시작하되, 큰 화면에서 빈 공간이 어떻게 채워질지 고민합니다.
2. **Flexible over Fixed (유연함 우선):** 하드코딩된 `width/height` 사용을 지양하고, 비율(`Expanded`, `%`) 또는 최대 너비(`MaxWidth`) 제한표현을 사용합니다.
3. **One Design System (통일된 디자인 시스템):** 기기별로 디자인이 파편화되지 않고, 그리드 시스템을 기반으로 레이아웃이 유동적으로 재배치되도록 합니다.

## 3. 웹 컨벤션 (Next.js / Tailwind CSS)
- **Grid Layout:** 리스트나 대시보드 카드를 구현할 때 반응형 그리드 유틸리티를 활용합니다.
  ```tsx
  /* 모바일 1열, 태블릿 2열, 데스크톱 4열 */
  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
  ```
- **Navigation (Sidebar):** 데스크톱에서는 펼쳐진 사이드바를 유지(`hidden md:flex`)하되, 모바일에서는 햄버거 메뉴를 눌렀을 때만 나타나는 오버레이 뷰/바텀 탭으로 구현합니다.
- **Table Data:** 데이터가 꽉 차는 표(`table`)는 모바일 환경에서 화면을 부수지 않도록 반드시 `overflow-x-auto`를 설정한 래퍼(Wrapper)로 감쌉니다.

## 4. 앱 컨벤션 (Flutter)
- **Constraint Box:** 태블릿의 넓은 화면(가로 모드)에서 버튼이나 텍스트 필드가 화면 전체 길이를 덮어 UI가 망가지는 현상을 방지합니다. 화면 전체를 쓰는 폼이나 단일 뷰는 `ConstrainedBox` 로 포장합니다.
  ```dart
  Center(
    child: ConstrainedBox(
      constraints: const BoxConstraints(maxWidth: 600), // 적절한 최대 너비
      child: child,
    ),
  )
  ```
- **SafeArea:** 기기별 노치(Notch) 영역이나 둥근 화면 테두리 침범 방지를 위해 스크린 최상단은 가급적 `SafeArea` 또는 `AppBar` 를 사용합니다.
- **LayoutBuilder / MediaQuery:** 화면 크기에 따라 완전히 다른 위젯 반환이 필요한 경우 분기 처리합니다.
  ```dart
  final isTablet = MediaQuery.of(context).size.width > 600;
  ```

---
> **[Rule Check]** 모든 화면 개발자는 PR을 올리기 전, 반드시 개발 중인 UI를 [모바일 세로/가로, 데스크톱 폭 최소화를 테스트]해야 합니다.
