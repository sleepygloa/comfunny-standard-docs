# [T-01] DASHBOARD_LAYOUT

**용도**: 모든 어드민 페이지, 백오피스, CMS 플랫폼의 최상위 루트 뼈대(Skeleton)로 사용됩니다.
새로운 페이지 컴포넌트를 만들 때, 이 구조 위에 Content 레이아웃을 작성해야 합니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div id="page-container" class="page-sidebar-fixed page-header-fixed">
  
  <!-- ===============================
       1. Top Header Area (상단 고정 헤더)
       =============================== -->
  <div id="header" class="header navbar-default">
    <div class="navbar-header">
      <a href="/" class="navbar-brand">
        <span class="navbar-logo"></span> <b>Admin</b> Portal
      </a>
      <!-- 모바일용 사이드바 토글 버튼 -->
      <button type="button" class="navbar-toggle" data-click="sidebar-toggled">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
    </div>

    <ul class="navbar-nav navbar-right">
       <!-- 알림 뱃지 -->
       <li class="dropdown">
           <a href="#" data-bs-toggle="dropdown" class="dropdown-toggle f-s-14">
               <i class="fa fa-bell"></i>
               <span class="badge">0</span>
           </a>
       </li>
       <!-- 프로필 -->
       <li class="dropdown navbar-user">
           <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown">
               <div class="image image-icon bg-black text-grey-darker"><i class="fa fa-user"></i></div>
               <span class="d-none d-md-inline">User Name</span> <b class="caret"></b>
           </a>
       </li>
    </ul>
  </div>

  <!-- ===============================
       2. Sidebar Area (좌측 다크 메뉴)
       =============================== -->
  <div id="sidebar" class="sidebar">
    <div data-scrollbar="true" data-height="100%">
      <ul class="nav">
        <!-- 네비게이션 헤더 -->
        <li class="nav-header">Navigation</li>
        
        <!-- 단일 메뉴 아이템 -->
        <li class="active">
          <a href="/dashboard">
            <i class="fa fa-th-large bg-gradient-orange"></i> 
            <span>Dashboard</span>
          </a>
        </li>

        <!-- 서브 메뉴 트리 -->
        <li class="has-sub">
          <a href="#">
            <b class="caret"></b>
            <i class="fa fa-cogs bg-gradient-blue"></i>
            <span>설정 관리</span>
          </a>
          <ul class="sub-menu">
            <li><a href="/settings/users">사용자 리스트</a></li>
            <li><a href="/settings/auth">권한 관리</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>

  <!-- ===============================
       3. Main Content Area (메인 본문)
       =============================== -->
  <div id="content" class="content">
    
    <!-- 3-1. Breadcrumb (네비게이션 뎁스) -->
    <ol class="breadcrumb float-xl-end">
      <li class="breadcrumb-item"><a href="/">Home</a></li>
      <li class="breadcrumb-item active">Dashboard</li>
    </ol>
    
    <!-- 3-2. Page Title -->
    <h1 class="page-header">Dashboard <small>데이터 모니터링 허브</small></h1>

    <!-- 3-3. 위젯 렌더링 존 (T-02_DATA_TABLE_PANEL.md 참조) -->
    <div class="row">
       <div class="col-xl-12">
           <!-- 컴포넌트 삽입 영역 -->
       </div>
    </div>

  </div> <!-- /content -->
</div> <!-- /page-container -->
```
