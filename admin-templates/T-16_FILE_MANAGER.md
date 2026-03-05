# [T-16] FILE_MANAGER

**용도**: 클라우드 파일함, 미디어 갤러리 관리, 문서 관리 아카이브에서 사용하는 탐색기 스타일의 파일 매니저 UI입니다.

### 1. Template Structure (File Manager)

이 레이아웃은 페이지 전체를 덮는 `<div class="file-manager">` 블록을 사용하며, 좌반부는 디렉토리 사이드바, 우반부는 파일 리스팅 영역으로 구분됩니다.

```html
<div class="file-manager" id="fileManager">
    <!-- ============================================
         1. FileManager Sidebar (폴더 네비게이션)
         ============================================ -->
    <div class="file-manager-sidebar">
        <div class="file-manager-sidebar-mobile-toggle">
            <button type="button" class="btn" data-bs-toggle="file-manager-sidebar">
                <i class="fa fa-folder-open text-theme"></i> Folders
            </button>
        </div>
        <div class="file-manager-sidebar-content" data-scrollbar="true" data-height="100%">
            <ul class="nav">
                <!-- 메인 항목 -->
                <li class="nav-title"><b>Folders</b></li>
                <li class="nav-item active">
                    <a href="#" class="nav-link"><i class="fa fa-fw fa-home text-gray-500 me-2"></i> Home Device</a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link"><i class="fa fa-fw fa-hdd text-gray-500 me-2"></i> Documents</a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link"><i class="fa fa-fw fa-image text-gray-500 me-2"></i> Pictures</a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link"><i class="fa fa-fw fa-film text-gray-500 me-2"></i> Videos</a>
                </li>
                <!-- 공간 부족 및 드라이브 -->
                <li class="nav-title mt-4"><b>Drives</b></li>
                <li class="nav-item">
                    <a href="#" class="nav-link"><i class="fa fa-fw fa-cloud text-gray-500 me-2"></i> Google Drive</a>
                </li>
            </ul>
            <div class="mt-4 px-3 fs-12px">
                <b>Storage Usage</b>
                <div class="progress progress-sm mt-1 mb-1 bg-gray-600">
                    <div class="progress-bar bg-theme" style="width: 60%"></div>
                </div>
                <div class="text-white-transparent-5">45.5 GB / 100 GB</div>
            </div>
        </div>
    </div>
    
    <!-- ============================================
         2. FileManager Content (메인 브라우저 영역)
         ============================================ -->
    <div class="file-manager-content">
        <!-- 상단 툴바 -->
        <div class="file-manager-content-header">
            <div class="d-flex align-items-center">
                <a href="#" class="btn btn-default btn-sm me-2"><i class="fa fa-upload fa-fw text-theme me-1"></i> Upload</a>
                <a href="#" class="btn btn-white btn-sm me-2"><i class="fa fa-folder-plus fa-fw me-1"></i> New Folder</a>
                <a href="#" class="btn btn-white btn-sm disabled"><i class="fa fa-trash fa-fw me-1"></i> Delete</a>
            </div>
            <div class="d-flex align-items-center ms-auto">
                <!-- 리스트/그리드 모드 토글 -->
                <div class="btn-group me-3">
                    <a href="#" class="btn btn-white btn-sm active"><i class="fa fa-th-large"></i></a>
                    <a href="#" class="btn btn-white btn-sm"><i class="fa fa-list"></i></a>
                </div>
            </div>
        </div>
        
        <!-- 본문 (그리드형 리스팅) -->
        <div class="file-manager-content-body">
            <div data-scrollbar="true" data-height="100%">
                <div class="file-manager-grid">
                    <!-- 폴더 아이템 -->
                    <div class="file-manager-grid-item">
                        <a href="#" class="file-manager-grid-item-link">
                            <div class="file-manager-grid-item-icon">
                                <i class="fa fa-folder text-warning"></i>
                            </div>
                            <div class="file-manager-grid-item-info">
                                <div class="title">Work Projects</div>
                                <div class="desc">1.2 GB, 42 files</div>
                            </div>
                        </a>
                    </div>
                    
                    <!-- 파일 아이템 (이미지) -->
                    <div class="file-manager-grid-item">
                        <a href="#" class="file-manager-grid-item-link">
                            <div class="file-manager-grid-item-image bg-cover" style="background-image: url(../assets/img/gallery/gallery-1.jpg);"></div>
                            <div class="file-manager-grid-item-info">
                                <div class="title">image_01.jpg</div>
                                <div class="desc">4 MB, 10/11/2026</div>
                            </div>
                        </a>
                    </div>
                    
                    <!-- 파일 아이템 (문서) -->
                    <div class="file-manager-grid-item">
                        <a href="#" class="file-manager-grid-item-link">
                            <div class="file-manager-grid-item-icon">
                                <i class="fa fa-file-pdf text-danger"></i>
                            </div>
                            <div class="file-manager-grid-item-info">
                                <div class="title">Q3_Report.pdf</div>
                                <div class="desc">450 KB, 10/10/2026</div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### 2. Implementation Notes
- 화면 사이즈 축소 시 모바일에서 사이드바가 숨겨지고, 토글 버튼으로 나타내기 위해 `file-manager-sidebar-mobile-toggle` 블록을 활용합니다.
- 그리드 기반 목록 렌더링에 최적화되어 있으므로, 데이터 바인딩 시 파일의 확장자에 따라 아이콘(fa-file-pdf, fa-file-excel 등)을 동적으로 할당하도록 로직을 구현하십시오.
