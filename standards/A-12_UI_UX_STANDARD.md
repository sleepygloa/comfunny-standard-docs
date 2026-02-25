# [12] 전사 UI/UX 및 디자인 표준 (UI/UX Standards)

이 문서는 회사 내 모든 어플리케이션(Web, Mobile, Admin Desktop)의 사용자 인터페이스(UI) 설계와 사용자 경험(UX) 흐름에 대한 공통 원칙을 정의합니다. 

특히 AI 기반 애플리케이션인 만큼, 복잡한 인지 과정을 줄이고 직관적인 흐름을 유도하는 것에 중점을 둡니다.

---

## 1. 핵심 철학 (Design Philosophy)

### 1-1. 단순함과 일관성 (Simplicity & Consistency)
- 유저는 한 화면에서 **단 하나의 핵심 행동(Call to Action)**에만 집중할 수 있어야 합니다.
- 메뉴, 버튼 위치, 색상, 타이포그래피는 모든 프로덕트 간에 일관된 디자인 시스템(Design System)을 공유해야 합니다.

### 1-2. 능동적인 피드백 (Proactive Feedback)
- AI 모델 추론, 오디오 변환 등 백그라운드 처리가 길어지는 작업의 경우, 반드시 화면이 멈춘 것처럼 보이지 않게 처리해야 합니다.
- 스켈레톤 로딩(Skeleton UI), 진행률 바(Progress Bar), **백그라운드 알림 도크(Notification Bell)**를 활용하여 유저가 대기 시간 동안 다른 작업을 할 수 있게 격리합니다.

### 1-3. 데이터 시각화의 투명성 (Transparency)
- AI 서비스가 제공한 데이터(채점 결과, TTS 품질 등)가 왜 그렇게 도출되었는지 사용자가 납득할 수 있는 근거(예: 오답노트 비교 UI)를 직관적으로 제공해야 합니다.

---

## 2. 레이아웃 및 뷰 플로우 (Layout & Flow)

### 2-1. 모바일 (Mobile App - MyLangFunnySkillUp 등)
1. **네비게이션**: 
   - `BottomNavigationBar`를 기본 골격으로 삼아 핵심 탭(홈, 학습, 통계, 마이페이지)으로 배치합니다.
   - 깊은 내비게이션(Depth 3 이상)은 지양하며, 필요시 `BottomSheet` 또는 모달 팝업으로 사용자 이탈을 방지합니다.
2. **제스처와 터치 존**:
   - 화면 하단 1/3 영역에 핵심 인터랙션 버튼(마이크 잡기 채점, 드래그 드롭 등)을 집중시켜 엄지손가락(Thumb Zone) 조작성을 극대화합니다.
3. **접근성(Accessibility)**:
   - 고대비(High Contrast)를 유지하고 시스템 단말기의 폰트 크기 변경에 유연하게 대응할 수 있는 가변 레이아웃을 사용합니다.

### 2-2. 데스크탑/웹 (Web App - MyVoiceTts 등)
1. **대시보드 패턴**:
   - 좌측에 LNB(Local Navigation Bar), 상단에 GNB(Global Navigation Bar) 및 알림 종소리를 고정하는 레이아웃을 표준으로 삼습니다.
2. **콘텐츠 영역 분리**:
   - 그리드 시스템(Grid System)을 도입하여, 데이터를 나열하는 부분(Data Grid)과 상태를 제어하는 부분(Action Panel)을 시각적으로 명확히 가릅니다.
   - 드래그 앤 드롭 파일 업로드(`Drag & Drop`) 등 마우스 특화 이벤트를 적극 지원합니다.

---

## 3. 에러 처리 및 언어 가이드 (Error Handling & Copywriting)

### 3-1. 글로벌 에러 핸들링 (Global Error Modal)
- 부분적인 기능 장애가 전체 앱의 크래시로 이어지지 않게 처리합니다.
- 토스트(Toast)는 "저장 완료" 등 가벼운 성공 알림에만 사용합니다.
- 조치가 필요한 치명적 에러, API 통신 실패의 경우 화면 중앙을 덮는 **모달 다이얼로그(Dialog)**를 사용하여 명확한 해법(재시도 등)과 함께 안내합니다.

### 3-2. 알림 메시지 어조 (Tone and Manner)
- 오류 메시지는 전문 용어(`NullReferenceException` 등)를 노출하지 않고 사용자 친화적인 자연어(예: "연결이 불안정하여 오디오를 들고 오지 못했어요.")로 작성합니다.
- AI 페르소나와 튜터 챗봇은 항상 친절하고, 부드러운 격려형 대화체(Gentle, Encouraging)를 기본값으로 유지합니다.

---

## 4. 모션 및 인터랙션 (Motion)

- 뷰 전환(Screen Transition)이나 데이터의 등장 시 딱딱하게 끊기지 않고 자연스러운 페이드 앤 슬라이드(Fade & Slide) 애니메이션을 0.2~0.3초 사이로 적용합니다.
- AI가 응답을 생성하는 구간에는 타이핑 인디케이터(`...` 말풍선 애니메이션)를 사용하여 살아있는 개체와 소통하는 듯한 감각적 피드백을 부여합니다.

---

## 5. 관리자(Admin) / 백오피스 UI 표준 가이드
회사 내부용 백오피스, CMS, 어드민 대시보드 구축 시에는 빠르고 데이터 집약적인 처리를 위해 다음 테마를 레퍼런스로 준수합니다.

### 5-1. Reference Design Theme (Color Admin V3)
모든 어드민 페이지(Web)는 **[Color Admin - Dashboard V3](https://seantheme.com/color-admin/admin/html/index_v3.html)** 의 룩앤필(Look and Feel)을 표준 디자인 가이드로 삼아 동일하게 가져갑니다.

### 5-2. Color Admin V3 디자인 핵심 규약
1. **Layout (레이아웃):**
    - 좌측 다크 톤 사이드바(`#sidebar` - 폭 약 250px)와 상단 화이트 헤더(`#header` - 높이 약 50~60px) 고정.
    - 본문 배경은 연한 회색(`#f0f3f4` 계열)을 사용하여 하얀색 위젯(Widget) 카드를 강조.
2. **Typography & Color:**
    - 데이터와 텍스트의 가시성이 최우선이므로, 또렷하고 장식이 없는 산세리프 글꼴(예: `Inter`, `Roboto`) 단일 폰트 체제 구축.
    - 테마의 기본 포인트 컬러(`Teal #00acac`, `Blue #348fe2`, `Red #ff5b57` 등)를 상태 표시(진행률, 알림 뱃지)에 적극 활용.
3. **Data Grid & Widget Boxes (핵심 컴포넌트 구조):**
    - 데이터를 담는 표(Table)와 차트는 상단에 타이틀 라인이 있는 **Panel** 형태로 감싸서 표현해야 함. (`.panel > .panel-heading + .panel-body`).
    - 박스는 옅은 그림자와 부드러운 모서리 라운딩 처리를 통해 정보 블록을 격리.

### 5-3. 구조적 템플릿 표준 (Structural Template)
외부 URL(Color Admin V3)이 변경되거나 접속 불가할 경우를 대비해, AI와 프론트엔드 개발자가 최우선으로 준수해야 할 **HTML/DOM 컨테이너 구조**의 골격을 아래와 같이 박제합니다. 프레임워크(React, Next.js, Flutter Web 등)를 막론하고 이 시멘틱 구조와 클래스 구조(명명 규칙)를 모방하여 구현해야 합니다.

```html
<!-- [페이지 최상위 래퍼] -->
<div id="page-container" class="page-sidebar-fixed page-header-fixed">
  
  <!-- 1. Header (상단바) -->
  <div id="header" class="header navbar-default">
    <div class="navbar-header">
      <a href="#" class="navbar-brand"><span class="navbar-logo"></span> <b>Color</b> Admin</a>
    </div>
    <!-- 우측 프로필/알림 메뉴 -->
    <ul class="navbar-nav navbar-right">
       <li class="dropdown"><a href="#">알림 뱃지</a></li>
       <li class="dropdown navbar-user"><a href="#">프로필 드롭다운</a></li>
    </ul>
  </div>

  <!-- 2. Sidebar (좌측 메뉴) -->
  <div id="sidebar" class="sidebar">
    <div data-scrollbar="true" data-height="100%">
      <ul class="nav">
        <li class="nav-profile">사용자 미니 프로필 영역</li>
        <li class="nav-header">네비게이션 분류 타이틀</li>
        <li class="has-sub active"> <!-- 활성화된 메뉴 -->
          <a href="#">
            <i class="fa fa-th-large"></i> <span>Dashboard</span>
          </a>
        </li>
      </ul>
    </div>
  </div>

  <!-- 3. Main Content (본문 영역) -->
  <div id="content" class="content">
    <!-- Breadcrumb & Page Title -->
    <ol class="breadcrumb float-xl-end">
      <li class="breadcrumb-item"><a href="#">Home</a></li>
      <li class="breadcrumb-item active">Dashboard</li>
    </ol>
    <h1 class="page-header">Dashboard <small>세부 설명 텍스트...</small></h1>

    <!-- 4. Panel Component (내부 데이터 래퍼 - 핵심) -->
    <div class="row">
      <div class="col-xl-12">
        <div class="panel panel-inverse">
          <!-- Panel Header: 검은색/어두운 배경 영역에 타이틀과 도구(접기/닫기) 배치 -->
          <div class="panel-heading">
            <h4 class="panel-title">데이터 패널 타이틀</h4>
            <div class="panel-heading-btn">
              <a href="#" class="btn btn-xs btn-icon btn-circle btn-default"><i class="fa fa-expand"></i></a>
              <a href="#" class="btn btn-xs btn-icon btn-circle btn-success"><i class="fa fa-redo"></i></a>
            </div>
          </div>
          <!-- Panel Body: 하얀색 배경의 실제 데이터 표출 공간 -->
          <div class="panel-body">
            <!-- DataTable, Form, Chart 등 배치 -->
            <table class="table table-striped table-bordered align-middle">
               <!-- ... -->
            </table>
          </div>
        </div>
      </div>
    </div>
  </div><!-- /content -->
</div><!-- /page-container -->
```

> **AI Agent 적용 규칙 (MANDATORY):**
> AI가 신규 관리자 페이지 컴포넌트(HTML/CSS, React, Vue 등)를 생성할 때는 위 `5-3. 구조적 템플릿 표준`의 HTML DOM 계층(`page-container` > `header`, `sidebar`, `content` > `panel`) 과 CSS 클래스 구조를 반드시 모방하여 작성하십시오. 외부 URL에 의존하지 않고 이 레이아웃 골격을 최우선 뼈대로 삼아야 합니다.
