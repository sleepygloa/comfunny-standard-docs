# Admin Page Templates (UI/UX)

이 디렉토리는 회사 백오피스, CMS, 어드민 대시보드 구축에 필요한 **화면 단위/컴포넌트 단위의 HTML/CSS 템플릿 표준**을 제공합니다.
AI 모델과 프론트엔드 개발자는 새로운 어드민 페이지 생성 요구사항을 받으면 **반드시 이 폴더의 템플릿 코드를 최우선으로 복사(Copy & Paste)하여 사용**해야 합니다.

## Template Index (템플릿 목록)
모든 템플릿은 `Color Admin - Dashboard V3`의 룩앤필(Look and Feel)을 기반으로 작성되었습니다.

1. **[T-01_DASHBOARD_LAYOUT.md](T-01_DASHBOARD_LAYOUT.md)**
   - **용도**: 신규 메뉴/페이지를 생성할 때 사용하는 최상단 뼈대(Skeleton)
   - **내용**: Header, Sidebar, Breadcrumb, 기본 Content Wrapper 구조 지정
2. **[T-02_DATA_TABLE_PANEL.md](T-02_DATA_TABLE_PANEL.md)**
   - **용도**: 데이터를 목록 형태로 표출할 때 사용하는 그리드(Grid) 컨테이너
   - **내용**: Panel Header(제목/버튼 영역)와 Panel Body(DataTable) 구성 방식
3. **[T-03_FORM_INPUTS.md](T-03_FORM_INPUTS.md)**
   - **용도**: 데이터 등록/수정 화면(Form) 뷰 생성
   - **내용**: 가독성 높은 Input Group 라벨링, Select Box, Submit 버튼 배치 표준
4. **[T-04_FORM_AI_IMAGE_GENERATOR.md](T-04_FORM_AI_IMAGE_GENERATOR.md)**
   - **용도**: AI 프롬프트 입력 및 결과물 전시 뷰 생성
   - **내용**: 패널 3:9 분리, 갤러리 영역 분할, 스피너 로딩 처리
5. **[T-05_EMAIL_INBOX.md](T-05_EMAIL_INBOX.md)**
   - **용도**: 수신 메일 리스트 및 쪽지함 UI 생성
   - **내용**: 좌측 Mailbox Sidebar 분할, 메일 리스트 체크박스 그룹화
6. **[T-06_UI_GENERAL_ELEMENTS.md](T-06_UI_GENERAL_ELEMENTS.md)**
   - **용도**: 기타 서브 컴포넌트 추가
   - **내용**: Alert, Notifications, Cards, Progress Bars, Badges
7. **[T-07_UI_TABS_ACCORDIONS.md](T-07_UI_TABS_ACCORDIONS.md)**
   - **용도**: 다중 탭 화면 및 확장형 아코디언 메뉴 UI 생성
   - **내용**: `nav-tabs` 패턴, `accordion-collapse` 패턴 구성 요소
8. **[T-08_FORM_VALIDATION.md](T-08_FORM_VALIDATION.md)**
   - **용도**: 폼 서브밋 전 데이터 유효성 검사 피드백 디자인 명시
   - **내용**: `is-valid`, `is-invalid`, 툴팁 및 피드백 텍스트 렌더링
9. **[T-09_ADVANCED_TABLES.md](T-09_ADVANCED_TABLES.md)**
   - **용도**: 엑셀/PDF 다운로드, 반응형 테이블 등 고도화된 그리드 뷰
   - **내용**: DataTables 툴바 및 반응형(`table-responsive`) 래퍼 패턴 구성
10. **[T-10_POS_SYSTEM.md](T-10_POS_SYSTEM.md)**
   - **용도**: 상품 판매 계산대, 테이블 예약 등 풀스크린 판매 관리 UI 구성
   - **내용**: 패널 분할 없는 `pos-content`와 우측 `pos-sidebar` 영수증 영역
11. **[T-11_EXTRA_PAGES.md](T-11_EXTRA_PAGES.md)**
   - **용도**: 명세서(Invoice), 사용자 프로필, 404 에러 화면 등 특수 단일 화면
   - **내용**: `invoice-company`, `invoice-header` 기반의 프린트 친화적 레이아웃
12. **[T-12_AUTHENTICATION.md](T-12_AUTHENTICATION.md)**
   - **용도**: 로그인, 회원가입, 암호 찾기 화면 등 인증 전용 레이아웃 생성
   - **내용**: 플로팅 라벨(`form-floating`), 풀스크린 바탕화면(`login-bg`) 구조
13. **[T-13_AI_CHAT.md](T-13_AI_CHAT.md)**
   - **용도**: 대화형 AI 웹 챗봇 환경 렌더링용 풀스크린 뷰
   - **내용**: 뷰포트 스크롤 고정, 툴바, 스피너 로딩, 우측 옵션 사이드바 구조
14. **[T-14_EMAIL_COMPOSE.md](T-14_EMAIL_COMPOSE.md)**
   - **용도**: 신규 메일/쪽지를 작성할 때 사용하는 이메일 작성(Compose) 뷰
   - **내용**: 좌측 메일함 네비게이션과 우측 작성 폼(`.mailbox` 패턴)
15. **[T-15_FORM_WIZARDS.md](T-15_FORM_WIZARDS.md)**
   - **용도**: 스텝 바이 스텝 다단계 정보 입력 폼
   - **내용**: 진행 상태를 나타내는 `wizard` 헤더 요소와 단계별 `fieldset` 필드
16. **[T-16_FILE_MANAGER.md](T-16_FILE_MANAGER.md)**
   - **용도**: 클라우드 파일함 및 탐색기 UI
   - **내용**: 디렉토리 트리 구조와 파일 그리드 뷰(`.file-manager` 패턴)
17. **[T-17_CALENDAR_VIEW.md](T-17_CALENDAR_VIEW.md)**
   - **용도**: 일정 및 예약 관리 화면
   - **내용**: FullCalendar 바인딩 컨테이너와 드래그 가능한 외부 이벤트 패널
18. **[T-18_CHARTS_GRAPHS.md](T-18_CHARTS_GRAPHS.md)**
   - **용도**: 대시보드 통계 시각화 패널
   - **내용**: Chart.js 및 ApexCharts용 `canvas`/`div` 래퍼 그리드 배치
19. **[T-19_SETTINGS_PAGE.md](T-19_SETTINGS_PAGE.md)**
   - **용도**: 시스템 환경설정, 알림 제어 화면
   - **내용**: `.nav-pills` 기반의 탭 메뉴와 설정 전용 패널 리스트 폼

20. **[T-20_TIMELINE_VIEW.md](T-20_TIMELINE_VIEW.md)**
   - **용도**: 시간순 이벤트 나열(타임라인) 화면
   - **내용**: `.timeline` 래퍼 내 `timeline-time`, `timeline-icon`, `timeline-body` 구성
21. **[T-21_PRICING_TABLE.md](T-21_PRICING_TABLE.md)**
   - **용도**: 요금제 및 구독 플랜 선택 화면
   - **내용**: `pricing-table` 리스트와 `highlight` 강조 클래스 부가
22. **[T-22_ERROR_PAGE.md](T-22_ERROR_PAGE.md)**
   - **용도**: 404/500 에러 처리 대기 페이지
   - **내용**: 중앙 정렬된 거대 에러 코드(.error-code) 및 복구 액션
23. **[T-23_COMING_SOON.md](T-23_COMING_SOON.md)**
   - **용도**: 서비스 공식 오픈 전 랜딩 페이지
   - **내용**: 전체 배경 위 카운트다운 타이머(.coming-soon) 컴포넌트

24. **[T-24_SEARCH_RESULTS.md](T-24_SEARCH_RESULTS.md)**
   - **용도**: 전역 검색 통합 결과 목록
   - **내용**: 대형 검색창 영역과 탭으로 구성된 결과 아이템 리스트
25. **[T-25_SCRUM_BOARD.md](T-25_SCRUM_BOARD.md)**
   - **용도**: 칸반(Kanban)/스크럼 관리 보드
   - **내용**: 드래그 앤 드롭 이동이 가능한 상태(Todo/In Progress/Done)별 카드 열
26. **[T-26_E_COMMERCE_ORDERS.md](T-26_E_COMMERCE_ORDERS.md)**
   - **용도**: 이커머스 주문 접수 및 조회 목록
   - **내용**: 상태 뱃지와 상품 썸네일 정보가 조합된 커스텀 데이터 그리드
27. **[T-27_E_COMMERCE_ORDER_DETAILS.md](T-27_E_COMMERCE_ORDER_DETAILS.md)**
   - **용도**: 이커머스 개별 주문건 상세 내역
   - **내용**: 제품 구매 리스트와 구매자 정보 패널(고객/배송지/결제정보)의 분할 구성
28. **[T-28_E_COMMERCE_PRODUCTS.md](T-28_E_COMMERCE_PRODUCTS.md)**
   - **용도**: 상품 포트폴리오 갤러리 뷰
   - **내용**: 그리드형 제품 카드와 좌측 필터 패널 조합 디자인

29. **[T-29_FORM_PLUGINS.md](T-29_FORM_PLUGINS.md)**
   - **용도**: Datepicker, Select2, Switchery 등 고급 폼 컨트롤 래퍼
   - **내용**: `default-select2`, `data-render="switchery"` 등의 JS 바인딩 마크업 패턴
30. **[T-30_FORM_SUMMERNOTE.md](T-30_FORM_SUMMERNOTE.md)**
   - **용도**: 웹 브라우저 리치 텍스트 WYSIWYG 에디터
   - **내용**: `textarea`에 씌워지는 `.summernote` 폼 컨테이너와 패널 구조
31. **[T-31_FORM_DROPZONE.md](T-31_FORM_DROPZONE.md)**
   - **용도**: 드래그 앤 드롭 파일/이미지 대용량 멀티 업로더
   - **내용**: `form` 태그 전체를 업로드 타겟으로 잡는 `.dropzone` 클래스 래퍼
32. **[T-32_DATA_MANAGEMENT.md](T-32_DATA_MANAGEMENT.md)**
   - **용도**: 엑셀 형식의 대량 Row 데이터 열람 및 계층형 자료 관리 UI
   - **내용**: 좌측 `.nav-tree`와 우측 스프레드시트 테이블의 Split Layout 분할
33. **[T-33_HELPER_CLASSES.md](T-33_HELPER_CLASSES.md)**
   - **용도**: 마진, 패딩, 폰트, 색상을 제어하는 전역 CSS 유틸리티 가이드 문서
   - **내용**: `.text-theme`, `.mb-3`, `.fs-12px` 등 하드코딩을 방지하는 재사용 클래스 목록

> **주의사항 (MANDATORY)**
> 디자인 일관성을 위해 템플릿에 명시된 `class` 명칭(예: `panel-inverse`, `page-header`)과 래퍼(Wrapper) 계층 구조를 임의로 변경하지 마십시오.
