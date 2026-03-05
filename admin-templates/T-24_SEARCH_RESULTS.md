# [T-24] SEARCH_RESULTS

**용도**: 포털 기반의 전역 검색(Global Search)이나 서비스 핵심 데이터를 키워드로 통합 검색한 결과 목록을 표시할 때 사용하는 템플릿입니다.

### 1. Template Structure (Search Results)

검색 결과 템플릿은 상단의 거대한 검색바 폼과 탭, 하단의 리스트형 결과 블록 아이템들로 구성됩니다. 각 결과 아이템에는 썸네일 우측에 제목, 링크, 요약 설명이 포함됩니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div class="row">
    <div class="col-md-10 offset-md-1">
        
        <!-- ============================================
             1. Search Header (검색 입력창 및 탭)
             ============================================ -->
        <h1 class="page-header">
            Search Results <small>3 results found for "admin template"</small>
        </h1>
        
        <div class="search-wrap">
            <div class="search-input-group input-group">
                <input type="text" class="form-control form-control-lg" placeholder="Search for keywords, items, etc..." value="admin template" />
                <button class="btn btn-primary btn-lg"><i class="fa fa-search"></i> Search</button>
            </div>
        </div>
        
        <ul class="nav nav-tabs nav-tabs-inverse">
            <li class="nav-item"><a href="#all" data-bs-toggle="tab" class="nav-link active">All <span class="badge bg-theme text-black rounded-pill ms-1">3</span></a></li>
            <li class="nav-item"><a href="#users" data-bs-toggle="tab" class="nav-link">Users <span class="badge bg-gray-500 rounded-pill ms-1">0</span></a></li>
            <li class="nav-item"><a href="#files" data-bs-toggle="tab" class="nav-link">Files <span class="badge bg-gray-500 rounded-pill ms-1">0</span></a></li>
        </ul>
        
        <!-- ============================================
             2. Search Body (검색 결과 목록)
             ============================================ -->
        <div class="tab-content bg-transparent p-0 m-0 border-0">
            <div class="tab-pane fade show active" id="all">
                <ul class="result-list border-top mt-3">
                    
                    <!-- Result Item 1 (Image Thumbnail) -->
                    <li>
                        <a href="javascript:;" class="result-image" style="background-image: url(../assets/img/gallery/gallery-1.jpg)"></a>
                        <div class="result-info">
                            <h4 class="title"><a href="javascript:;">Color Admin - Best Selling Dashboard</a></h4>
                            <p class="location">Bootstrap Admin Template</p>
                            <p class="desc">
                                Color Admin is the new premium and fully responsive admin template. 
                                Built with Bootstrap 5, it includes 6 UI theme variations to suit your taste.
                            </p>
                            <div class="btn-row">
                                <a href="javascript:;" data-bs-toggle="tooltip" title="Explore"><i class="fa fa-fw fa-link text-primary"></i></a>
                                <a href="javascript:;" data-bs-toggle="tooltip" title="Download"><i class="fa fa-fw fa-download text-theme"></i></a>
                                <a href="javascript:;" data-bs-toggle="tooltip" title="Share"><i class="fa fa-fw fa-share-alt"></i></a>
                            </div>
                        </div>
                        <div class="result-price">
                            $24 <small>PER ITEM</small>
                            <a href="javascript:;" class="btn btn-theme w-100 mt-2">View Details</a>
                        </div>
                    </li>
                    
                    <!-- Result Item 2 (Icon Thumbnail) -->
                    <li>
                        <div class="result-image bg-gray-200 text-center text-gray-400 d-flex align-items-center justify-content-center">
                            <i class="fa fa-file-alt fa-3x"></i>
                        </div>
                        <div class="result-info">
                            <h4 class="title"><a href="javascript:;">Official Documentation v3.2.1</a></h4>
                            <p class="location">/docs/admin/index.html</p>
                            <p class="desc">
                                We've prepared a comprehensive guide to help you build your enterprise dashboard rapidly.
                            </p>
                            <div class="btn-row">
                                <a href="javascript:;" data-bs-toggle="tooltip" title="Read"><i class="fa fa-fw fa-book text-success"></i></a>
                            </div>
                        </div>
                        <div class="result-price">
                            Free <small>DOCUMENTATION</small>
                            <a href="javascript:;" class="btn btn-outline-theme w-100 mt-2">Read PDF</a>
                        </div>
                    </li>
                    
                </ul>
                
                <!-- Pagination -->
                <div class="d-flex justify-content-center mt-4">
                    <ul class="pagination mb-0">
                        <li class="page-item disabled"><a href="javascript:;" class="page-link">First</a></li>
                        <li class="page-item disabled"><a href="javascript:;" class="page-link">&laquo;</a></li>
                        <li class="page-item active"><a href="javascript:;" class="page-link">1</a></li>
                        <li class="page-item"><a href="javascript:;" class="page-link">2</a></li>
                        <li class="page-item"><a href="javascript:;" class="page-link">&raquo;</a></li>
                        <li class="page-item"><a href="javascript:;" class="page-link">Last</a></li>
                    </ul>
                </div>
            </div>
            
            <!-- 그 외 Users, Files 탭 빈 영역 생략... -->
            <div class="tab-pane fade" id="users">
                <div class="alert alert-secondary mt-3">There are no users found.</div>
            </div>
        </div>
        
    </div>
</div>
```

### 2. Implementation Notes
- `result-list` 패턴 하위에 있는 `result-image`, `result-info`, `result-price` 세 가지 영역은 Flexbox 기반으로 수평 배치됩니다.
- 모바일 디바이스 등으로 화면 영역이 좁아지면 썸네일을 숨기거나 요약 가격(`result-price`) 패널이 정보란(`result-info`) 밑으로 떨어지며 반응형 대응합니다.
