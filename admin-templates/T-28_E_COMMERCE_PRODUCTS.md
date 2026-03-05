# [T-28] E_COMMERCE_PRODUCTS

**용도**: 서비스에 등록된 전체 실물/가상 상품 포트폴리오를 카드 기반의 갤러리 뷰로 나열하는 템플릿입니다. 이커머스 외에도 갤러리 이미지 브라우저, 콘텐츠 아카이브 리스트로 응용할 수 있습니다.

### 1. Template Structure (Products Gallery)

상품 목록은 부트스트랩 그리드 컨테이너 안에서 좌측 필터(Sidebar) 영역과 우측 아이템(.gallery) 그리드 영역으로 구획됩니다. 하단에는 무한 스크롤 또는 페이징 내비게이션 처리가 들어갑니다.

```html
<!-- [페이지 전체 헤더] -->
<div class="d-flex align-items-center mb-3">
    <div>
        <h1 class="page-header mb-0">Products <small>1,248 items found</small></h1>
    </div>
    <div class="ms-auto">
        <a href="#" class="btn btn-theme btn-rounded px-4 rounded-pill"><i class="fa fa-plus fa-fw me-1"></i> Add Product</a>
    </div>
</div>

<div class="row">
    <!-- ============================================
         1. Left Area: Filters & Categories
         ============================================ -->
    <div class="col-md-3 col-lg-2">
        <!-- 카테고리 필터 -->
        <h5 class="mb-3">Categories</h5>
        <div class="nav flex-column nav-pills mb-4">
            <a href="#" class="nav-link active">All Products <span class="badge bg-gray-500 float-end">1,248</span></a>
            <a href="#" class="nav-link text-gray-600">Electronics <span class="badge bg-gray-200 text-gray-600 float-end">348</span></a>
            <a href="#" class="nav-link text-gray-600">Apparel <span class="badge bg-gray-200 text-gray-600 float-end">512</span></a>
            <a href="#" class="nav-link text-gray-600">Home & Kitchen <span class="badge bg-gray-200 text-gray-600 float-end">120</span></a>
            <a href="#" class="nav-link text-gray-600">Sports <span class="badge bg-gray-200 text-gray-600 float-end">268</span></a>
        </div>
        
        <!-- 상태 다중 체크박스 필터 -->
        <h5 class="mb-3">Availability</h5>
        <div class="form-check mb-2">
            <input class="form-check-input" type="checkbox" id="av_instock" checked />
            <label class="form-check-label text-gray-600" for="av_instock">In Stock</label>
        </div>
        <div class="form-check mb-2">
            <input class="form-check-input" type="checkbox" id="av_outstock" />
            <label class="form-check-label text-gray-600" for="av_outstock">Out of Stock</label>
        </div>
    </div>
    
    <!-- ============================================
         2. Right Area: Products Grid 
         ============================================ -->
    <div class="col-md-9 col-lg-10">
        
        <!-- 검색/정렬 툴바 -->
        <div class="d-flex align-items-center mb-3">
            <div class="input-group w-50">
                <input type="text" class="form-control form-control-sm" placeholder="Search physical/digital products..." />
                <button class="btn btn-sm btn-white"><i class="fa fa-search"></i></button>
            </div>
            <div class="ms-auto d-flex align-items-center">
                <span class="text-gray-500 me-2 fs-12px">Sort by:</span>
                <select class="form-select form-select-sm w-150px">
                    <option>Latest Updates</option>
                    <option>Price: High to Low</option>
                    <option>Price: Low to High</option>
                    <option>Best Selling</option>
                </select>
            </div>
        </div>
        
        <!-- ============================================
             3. Gallery Card List 
             ============================================ -->
        <div class="row gx-3">
            
            <!-- Product Item 1 -->
            <div class="col-xl-3 col-lg-4 col-sm-6 mb-3">
                <div class="card h-100 border-0 shadow-sm">
                    <!-- 썸네일 -->
                    <div class="position-relative overflow-hidden bg-light rounded-top text-center p-4">
                        <span class="badge bg-danger position-absolute top-0 end-0 m-2 mt-2 me-2">-20%</span>
                        <img src="../assets/img/product/product-1.png" class="mw-100 mh-100" style="height: 120px;" alt="Product" />
                    </div>
                    <!-- 내용 -->
                    <div class="card-body p-3">
                        <div class="fs-11px text-gray-500 mb-1">Electronics &middot; Apple</div>
                        <h6 class="card-title text-dark fw-bold text-truncate mb-2">iPhone 15 Pro Max 256GB</h6>
                        <div class="d-flex align-items-center">
                            <!-- 가격 -->
                            <div class="fs-14px fw-bold text-dark">$1,199.00</div>
                            <div class="fs-12px text-muted text-decoration-line-through ms-2">$1,499.00</div>
                            <!-- 드롭다운 메뉴 -->
                            <div class="ms-auto">
                                <a href="#" class="btn btn-sm btn-white d-flex align-items-center justify-content-center p-1 w-25px h-25px" data-bs-toggle="dropdown"><i class="fa fa-ellipsis-h text-gray-500"></i></a>
                                <div class="dropdown-menu dropdown-menu-end">
                                    <a class="dropdown-item" href="#">Edit Details</a>
                                    <a class="dropdown-item" href="#">Manage Inventory</a>
                                    <a class="dropdown-item text-danger" href="#">Delete Product</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- 상태 푸터 -->
                    <div class="card-footer bg-transparent border-top-0 px-3 pb-3 pt-0">
                        <div class="progress h-4px mb-1">
                            <div class="progress-bar bg-success" style="width: 80%;"></div>
                        </div>
                        <div class="fs-11px text-gray-500 d-flex justify-content-between">
                            <span>85 In Stock</span>
                            <span>Sales: 162</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Product Item 2 -->
            <div class="col-xl-3 col-lg-4 col-sm-6 mb-3">
                <div class="card h-100 border-0 shadow-sm">
                    <div class="position-relative overflow-hidden bg-light rounded-top text-center p-4">
                        <img src="../assets/img/product/product-2.png" class="mw-100 mh-100" style="height: 120px;" alt="Product" />
                    </div>
                    <div class="card-body p-3">
                        <div class="fs-11px text-gray-500 mb-1">Electronics &middot; Wearables</div>
                        <h6 class="card-title text-dark fw-bold text-truncate mb-2">AirPods Pro Gen 2</h6>
                        <div class="d-flex align-items-center">
                            <div class="fs-14px fw-bold text-dark">$249.00</div>
                            <div class="ms-auto">
                                <a href="#" class="btn btn-sm btn-white d-flex align-items-center justify-content-center p-1 w-25px h-25px" data-bs-toggle="dropdown"><i class="fa fa-ellipsis-h text-gray-500"></i></a>
                                <div class="dropdown-menu dropdown-menu-end">
                                    <a class="dropdown-item" href="#">Edit Details</a>
                                    <a class="dropdown-item" href="#">Manage Inventory</a>
                                    <a class="dropdown-item text-danger" href="#">Delete Product</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer bg-transparent border-top-0 px-3 pb-3 pt-0">
                        <div class="progress h-4px mb-1 bg-gray-200">
                            <!-- 로우 인벤토리(경고) 표현 -->
                            <div class="progress-bar bg-warning" style="width: 15%;"></div>
                        </div>
                        <div class="fs-11px text-warning d-flex justify-content-between fw-bold">
                            <span>15 In Stock (Low)</span>
                            <span class="text-gray-500 fw-normal">Sales: 88</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 추가 Item은 반복문으로 구성... -->
            
        </div>
        
        <!-- 하단 페이저 -->
        <div class="d-flex justify-content-center mt-3">
            <button class="btn btn-white btn-rounded px-4 shadow-sm"><i class="fa fa-sync fa-fw me-1"></i> Load More Items</button>
        </div>
        
    </div>
</div>
```

### 2. Implementation Notes
- 상품 이미지가 담기는 카드 상단부(`.bg-light.rounded-top`)는 이미지 비율이 각기 다를 수 있으므로 `h-120px` 등의 고정 높이를 주거나 `mw-100 mh-100` 속성으로 영역을 보장해 찌그러짐을 방지하는 것이 매우 중요합니다.
- 재고(In Stock) 막대 바를 통해 퍼센테이지나 가용 물량을 시각적으로 보여줌으로써 관리자가 재고 위기를 직관적으로 파악할 수 있도록 돕습니다.
