# [T-19] SETTINGS_PAGE

**용도**: 서비스 환경설정, 사용자 계정 설정, 알림 및 보안 옵션을 제어할 때 사용하는 템플릿입니다.

### 1. Template Structure (Settings Page)

설정 화면은 좌측의 Navigation Menu 컴포넌트와 우측의 각 설정 항목(Section) 폼으로 이루어집니다.

```html
<div class="row">
    <!-- ============================================
         1. Left Area: Settings Navigation
         ============================================ -->
    <div class="col-xl-3 col-lg-4">
        <!-- 모바일 화면용 드롭다운 메뉴 (옵션) -->
        <div class="d-print-none mb-3 d-lg-none">
            <button class="btn btn-default w-100 dropdown-toggle text-start" data-bs-toggle="dropdown">
                Settings Menu
            </button>
            <div class="dropdown-menu w-100">
                <a href="#general" class="dropdown-item"><i class="fa fa-cog fa-fw me-2"></i> General</a>
                <a href="#notifications" class="dropdown-item"><i class="fa fa-bell fa-fw me-2"></i> Notifications</a>
                <a href="#security" class="dropdown-item"><i class="fa fa-shield-alt fa-fw me-2"></i> Security</a>
            </div>
        </div>
        
        <!-- 데스크톱용 수직 리스트 메뉴 -->
        <nav class="nav nav-pills flex-column d-none d-lg-flex mb-4">
            <a class="nav-link active" href="#general" data-bs-toggle="pill">
                <i class="fa fa-cog fa-fw fa-lg me-2"></i> General Settings
            </a>
            <a class="nav-link" href="#notifications" data-bs-toggle="pill">
                <i class="fa fa-bell fa-fw fa-lg me-2"></i> Notifications
            </a>
            <a class="nav-link" href="#security" data-bs-toggle="pill">
                <i class="fa fa-shield-alt fa-fw fa-lg me-2"></i> Security &amp; Privacy
            </a>
            <a class="nav-link" href="#billing" data-bs-toggle="pill">
                <i class="fa fa-credit-card fa-fw fa-lg me-2"></i> Billing
            </a>
        </nav>
    </div>
    
    <!-- ============================================
         2. Right Area: Settings Content Panels
         ============================================ -->
    <div class="col-xl-9 col-lg-8">
        <div class="tab-content border-0 p-0 bg-transparent">
            <!-- 2-1. General Settings 탭 -->
            <div class="tab-pane fade show active" id="general">
                <div class="panel panel-inverse">
                    <div class="panel-heading">
                        <h4 class="panel-title">General Settings</h4>
                    </div>
                    <div class="panel-body">
                        <form action="/" method="POST">
                            <h5 class="mb-3">Account Setup</h5>
                            <div class="row mb-3">
                                <label class="col-md-3 col-form-label">Site Name</label>
                                <div class="col-md-9">
                                    <input type="text" class="form-control" value="COMFUNNY System" />
                                </div>
                            </div>
                            <div class="row mb-3">
                                <label class="col-md-3 col-form-label">Support Email</label>
                                <div class="col-md-9">
                                    <input type="email" class="form-control" value="support@comfunny.com" />
                                </div>
                            </div>
                            
                            <hr class="bg-gray-500" />
                            <h5 class="mb-3">Localization</h5>
                            <div class="row mb-3">
                                <label class="col-md-3 col-form-label">Language</label>
                                <div class="col-md-9">
                                    <select class="form-select">
                                        <option value="ko" selected>Korean (한국어)</option>
                                        <option value="en">English (US)</option>
                                    </select>
                                </div>
                            </div>
                            <div class="text-end mt-4">
                                <button type="submit" class="btn btn-primary w-100px">Save</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            
            <!-- 2-2. Notification Settings 탭 -->
            <div class="tab-pane fade" id="notifications">
                <div class="panel panel-inverse">
                    <div class="panel-heading">
                        <h4 class="panel-title">Notifications</h4>
                    </div>
                    <div class="panel-body">
                        <div class="list-group list-group-flush border-bottom mb-3">
                            <div class="list-group-item d-flex align-items-center">
                                <div class="flex-1">
                                    <div><strong>Email Alerts</strong></div>
                                    <div class="text-gray-500 fs-12px">Receive email notifications for important system events.</div>
                                </div>
                                <div>
                                    <div class="form-check form-switch ps-0">
                                        <input type="checkbox" class="form-check-input ms-auto" id="switch1" checked />
                                    </div>
                                </div>
                            </div>
                            <div class="list-group-item d-flex align-items-center">
                                <div class="flex-1">
                                    <div><strong>Weekly Report</strong></div>
                                    <div class="text-gray-500 fs-12px">Receive a weekly summary of your account activity.</div>
                                </div>
                                <div>
                                    <div class="form-check form-switch ps-0">
                                        <input type="checkbox" class="form-check-input ms-auto" id="switch2" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 그 외 기타 탭 생략... -->
        </div>
    </div>
</div>
```

### 2. Implementation Notes
- 세팅 메뉴는 부트스트랩 `.nav-pills`와 `.tab-content`를 활용해 SPA(Single Page Application)처럼 화면 깜빡임 없이 패널 전환이 이루어지게 설계되어 있습니다.
- 모바일 환경 화면을 대비하여 `d-lg-none` 클래스가 적용된 드롭다운 메뉴를 좌측 패널 상단에 추가하여 반응성을 확보합니다.
- 토글 옵션의 경우 `<div class="form-check form-switch">` 부트스트랩 스위치를 사용하여 직관적인 ON/OFF 기능을 제공합니다.
