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

> **주의사항 (MANDATORY)**
> 디자인 일관성을 위해 템플릿에 명시된 `class` 명칭(예: `panel-inverse`, `page-header`)과 래퍼(Wrapper) 계층 구조를 임의로 변경하지 마십시오.
