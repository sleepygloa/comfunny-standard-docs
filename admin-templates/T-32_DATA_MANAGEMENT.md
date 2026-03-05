# [T-32] DATA_MANAGEMENT

**용도**: 백업 파일, 시스템 이력 등 여러 리소스를 단순 나열하고 대량의 로우 데이터(Raw Data)를 엑셀 형식으로 직관적으로 편집하거나 검토할 때 유용한 데이터 관제 템플릿입니다.

### 1. Template Structure (Data Management View)

좌측의 카테고리/폴더 트리 영역과 우측의 데이터 목록을 병렬로 제공한다는 점에서 `T-16_FILE_MANAGER`와 유사하나, 우측이 아이콘 타일 대신 테이블(Table) 형태로 렌더링되는 것이 특징입니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div class="d-flex gx-0 h-100 data-management">
    
    <!-- ============================================
         1. Left Area: Data Category / Group List
         ============================================ -->
    <div class="w-250px border-end bg-light-subtle d-none d-md-flex flex-column h-100">
        
        <div class="p-3 border-bottom fs-14px fw-bold text-dark d-flex align-items-center">
            <i class="fa fa-database fa-fw text-theme me-2"></i> System Schemas
        </div>
        
        <!-- 스크롤러블 네비게이션 트리 -->
        <div class="flex-fill" data-scrollbar="true" data-height="100%">
            <div class="nav-tree">
                <!-- 폴더 1 -->
                <div class="nav-tree-item opened">
                    <a href="javascript:;" class="nav-tree-link d-flex align-items-center bg-gray-200">
                        <i class="fa fa-folder-open text-warning me-2"></i> <span>Core Logs</span> <span class="badge bg-secondary ms-auto">2</span>
                    </a>
                    <!-- 하위 자식 노드 -->
                    <div class="nav-tree-children">
                        <div class="nav-tree-item active">
                            <a href="javascript:;" class="nav-tree-link text-theme"><i class="fa fa-file-csv text-muted me-2"></i> access_log_202610.csv</a>
                        </div>
                        <div class="nav-tree-item">
                            <a href="javascript:;" class="nav-tree-link"><i class="fa fa-file-csv text-muted me-2"></i> error_log_202610.csv</a>
                        </div>
                    </div>
                </div>
                
                <!-- 폴더 2 -->
                <div class="nav-tree-item">
                    <a href="javascript:;" class="nav-tree-link d-flex align-items-center bg-transparent">
                        <i class="fa fa-folder text-warning me-2"></i> <span>DB Snapshots</span> <span class="badge bg-secondary ms-auto">12</span>
                    </a>
                </div>
                
                <!-- 폴더 3 -->
                <div class="nav-tree-item">
                    <a href="javascript:;" class="nav-tree-link d-flex align-items-center bg-transparent">
                        <i class="fa fa-archive text-gray-500 me-2"></i> <span>Archive Backups</span>
                    </a>
                </div>
            </div>
        </div>
        
    </div>
    
    <!-- ============================================
         2. Right Area: Data Viewer (Data Grid)
         ============================================ -->
    <div class="flex-fill d-flex flex-column h-100 bg-white">
        
        <!-- 데이터 툴바 -->
        <div class="d-flex align-items-center p-3 border-bottom bg-light">
            <div class="fw-bold fs-16px text-dark me-auto">
                <i class="fa fa-table text-gray-500 me-2"></i> access_log_202610.csv
            </div>
            
            <div class="btn-group me-2">
                <button class="btn btn-sm btn-outline-default"><i class="fa fa-file-excel text-success me-1"></i> Export XLSX</button>
                <button class="btn btn-sm btn-outline-default"><i class="fa fa-file-code text-danger me-1"></i> Export JSON</button>
            </div>
            <button class="btn btn-sm btn-theme px-3"><i class="fa fa-play fa-fw"></i> Run Query</button>
        </div>
        
        <!-- 데이터 테이블 (Spreadsheet 형식) -->
        <div class="flex-fill position-relative">
            <!-- T-02, T-09 와 같은 DataTables.js 또는 Handsontable을 바인딩하여 엑셀 뷰어처럼 만듦 -->
            <div class="table-responsive h-100" data-scrollbar="true" data-height="100%">
                <table class="table table-bordered table-sm m-0 text-nowrap table-hover">
                    <thead class="bg-gray-200">
                        <tr>
                            <th width="1%" class="text-center">#</th>
                            <th>TIMESTAMP</th>
                            <th>IP_ADDRESS</th>
                            <th>HTTP_METHOD</th>
                            <th>ENDPOINT</th>
                            <th>STATUS_CODE</th>
                            <th>RESPONSE_TIME (ms)</th>
                        </tr>
                    </thead>
                    <tbody class="fs-12px font-monospace text-gray-700">
                        <tr>
                            <td class="text-center bg-gray-100">1</td>
                            <td>2026-10-15T08:12:44Z</td>
                            <td>192.168.0.144</td>
                            <td class="text-success fw-bold">GET</td>
                            <td>/api/v1/users/profile</td>
                            <td>200</td>
                            <td>42.5</td>
                        </tr>
                        <tr>
                            <td class="text-center bg-gray-100">2</td>
                            <td>2026-10-15T08:12:45Z</td>
                            <td>10.0.12.5</td>
                            <td class="text-primary fw-bold">POST</td>
                            <td>/api/v1/orders/create</td>
                            <td>201</td>
                            <td>124.8</td>
                        </tr>
                        <tr>
                            <td class="text-center bg-gray-100">3</td>
                            <td>2026-10-15T08:12:48Z</td>
                            <td>172.16.88.2</td>
                            <td class="text-success fw-bold">GET</td>
                            <td>/api/v1/auth/verify</td>
                            <td class="text-danger fw-bold">401</td>
                            <td>12.2</td>
                        </tr>
                        <!-- 100~1000줄 이상의 데이터 렌더링 구역 -->
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- 하단 상태 표시줄 -->
        <div class="border-top p-2 bg-light fs-11px text-gray-600 d-flex justify-content-between">
            <span>Size: 4.2 MB (324,199 rows)</span>
            <span>Last Indexed: 1 hour ago</span>
        </div>
        
    </div>
</div>
```

### 2. Implementation Notes
- 화면 설계의 주된 패러다임은 **분할(Split)** 뷰입니다. 부트스트랩 `d-flex h-100` 및 `flex-fill` 컨테이너를 영리하게 배치해 별도 마진이나 스크롤 간섭 없이 페이지 내 앱(In-app) 경험을 제공합니다.
- 많은 열이 들어가는 데이터를 표시하기 위해 테이블에 `text-nowrap`과 `font-monospace` (가독성을 위한 등폭 글꼴) 처리를 추가합니다.
