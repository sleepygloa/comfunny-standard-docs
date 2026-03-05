# [T-25] SCRUM_BOARD

**용도**: 애자일 프로젝트 관리, 이슈 트래킹, 세일즈 파이프라인 칸반(Kanban) 보드 등 각 단계(Status)별로 업무 카드를 드래그 앤 드롭으로 이동할 수 있는 형태의 뷰입니다.

### 1. Template Structure (Scrum Board)

각 열(Column)은 `list-group` 패널 구조로 구획되며, 내부 항목(Card)들은 위아래 혹은 다른 상태창으로 자유롭게 이동할 수 있는 마크업 구조를 따릅니다. 가로 스크롤 레이아웃에 최적화됩니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div class="row w-100 flex-nowrap overflow-x-auto pb-4" style="min-height: 80vh;">
    <!-- ============================================
         1. TODO (할 일 열)
         ============================================ -->
    <div class="col-xl-4 col-lg-6">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">To Do (2)</h4>
                <div class="panel-heading-btn">
                    <a href="javascript:;" class="btn btn-xs btn-icon btn-default" data-toggle="panel-expand"><i class="fa fa-expand"></i></a>
                </div>
            </div>
            <!-- sortable 영역으로 지정될 부모 리스트 -->
            <div class="list-group list-group-flush sortable-list" id="todoBoard">
                
                <!-- 태스크 카드 1 -->
                <div class="list-group-item list-group-item-action d-flex align-items-center">
                    <div class="me-3 fs-16px">
                        <i class="far fa-question-circle text-gray-500 fa-fw"></i>
                    </div>
                    <div class="flex-fill">
                        <div class="fs-14px lh-12 mb-2px fw-bold text-dark">UI/UX Revamp for Dashboard</div>
                        <div class="mb-1 fs-12px">
                            <div class="text-gray-600 flex-1">Create new design prototype using Figma.</div>
                        </div>
                        <div class="mb-1">
                            <span class="badge bg-primary">Design</span>
                            <span class="badge bg-gray-300 text-black">High Priority</span>
                        </div>
                    </div>
                </div>
                
                <!-- 태스크 카드 2 -->
                <div class="list-group-item list-group-item-action d-flex align-items-center">
                    <div class="me-3 fs-16px">
                        <i class="far fa-question-circle text-gray-500 fa-fw"></i>
                    </div>
                    <div class="flex-fill">
                        <div class="fs-14px lh-12 mb-2px fw-bold text-dark">Database Migration</div>
                        <div class="mb-1 fs-12px">
                            <div class="text-gray-600 flex-1">Move legacy MySQL tables to new PostgreSQL cluster.</div>
                        </div>
                        <div class="mb-1">
                            <span class="badge bg-danger">Backend</span>
                            <span class="badge bg-gray-300 text-black">Critical</span>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
    
    <!-- ============================================
         2. IN PROGRESS (진행 중 열)
         ============================================ -->
    <div class="col-xl-4 col-lg-6">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">In Progress (1)</h4>
            </div>
            <div class="list-group list-group-flush sortable-list pb-5" id="inProgressBoard">
                
                <!-- 진행 중 태스크 (스피너 아이콘) -->
                <div class="list-group-item list-group-item-action d-flex align-items-center">
                    <div class="me-3 fs-16px">
                        <i class="fa fa-cog fa-spin text-theme fa-fw"></i>
                    </div>
                    <div class="flex-fill">
                        <div class="fs-14px lh-12 mb-2px fw-bold text-dark">API Documentation Update</div>
                        <div class="mb-1 fs-12px">
                            <div class="text-gray-600 flex-1">Update Swagger endpoints for v2.0 release.</div>
                        </div>
                        <div class="mb-1">
                            <span class="badge bg-warning">Docs</span>
                        </div>
                    </div>
                    <div class="ms-3 text-center">
                        <img src="../assets/img/user/user-1.jpg" class="rounded-circle w-30px h-30px" alt="assigned_user" />
                    </div>
                </div>
                
            </div>
        </div>
    </div>
    
    <!-- ============================================
         3. DONE (완료 열)
         ============================================ -->
    <div class="col-xl-4 col-lg-6">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">Done (1)</h4>
            </div>
            <div class="list-group list-group-flush sortable-list pb-5" id="doneBoard">
                
                <!-- 완료된 태스크 (체크 아이콘) -->
                <div class="list-group-item list-group-item-action d-flex align-items-center bg-gray-100">
                    <div class="me-3 fs-16px">
                        <i class="far fa-check-circle text-success fa-fw"></i>
                    </div>
                    <div class="flex-fill">
                        <div class="fs-14px lh-12 mb-2px fw-bold text-gray-500 text-decoration-line-through">Fix memory leak in batch job</div>
                        <div class="mb-1 fs-12px">
                            <div class="text-gray-500 flex-1">Resolved issue #144 in scheduler.</div>
                        </div>
                        <div class="mb-1">
                            <span class="badge bg-gray-400">Bug</span>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</div>
```

### 2. Implementation Notes
- **Drag & Drop 바인딩**: 각 상태 열의 부모 `.sortable-list`는 `SortableJS` 또는 jQuery UI Sortable을 통하여 서로 간에 아이템 드래그를 허용하도록 스크립트 단에서 묶어주어야 합니다. (예: `new Sortable(document.getElementById('todoBoard'), { group: 'shared' });`)
- 열(Column) 갯수가 늘어날 것을 대비하여, 가장 바깥 `.row` 래퍼에 `flex-nowrap overflow-x-auto` 속성을 부여하여 뷰포트 바깥으로 이어지는 네이티브 좌우 스크롤을 활성화합니다.
