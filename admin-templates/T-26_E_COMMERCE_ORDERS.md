# [T-26] E_COMMERCE_ORDERS

**용도**: 쇼핑몰, 배달앱 등 e커머스 도메인에서 주문 내역 목록을 시각적으로 큼직하게 렌더링하는 전용 리스트 포맷입니다. 일반적인 가로줄 형태의 데이터 그리드(T-02 DataTable)와 달리, 다층적인 데이터(제품 사진, 배송 상태, 구매자 정보)를 포함하는 커스텀 리스트 뷰입니다.

### 1. Template Structure (Orders List)

```html
<!-- [페이지 전체 헤더] -->
<div class="d-flex align-items-center mb-3">
    <div>
        <h1 class="page-header mb-0">Orders</h1>
    </div>
    <div class="ms-auto">
        <a href="#" class="btn btn-success btn-rounded px-4 rounded-pill"><i class="fa fa-plus fa-fw me-1"></i> Create Order</a>
    </div>
</div>

<!-- ============================================
     1. Search & Filter Bar
     ============================================ -->
<div class="mb-3 d-sm-flex align-items-center">
    <div class="dropdown me-2">
        <a href="#" class="btn btn-white dropdown-toggle" data-bs-toggle="dropdown">
            Filter by Status <b class="caret ms-1"></b>
        </a>
        <div class="dropdown-menu">
            <a href="javascript:;" class="dropdown-item">All Orders</a>
            <a href="javascript:;" class="dropdown-item">Pending</a>
            <a href="javascript:;" class="dropdown-item">Processing</a>
            <a href="javascript:;" class="dropdown-item">Shipped</a>
            <a href="javascript:;" class="dropdown-item">Delivered</a>
            <a href="javascript:;" class="dropdown-item text-danger">Cancelled</a>
        </div>
    </div>
    <div class="input-group">
        <input type="text" class="form-control" placeholder="Search order ID, user, or product..." />
        <button class="btn btn-white"><i class="fa fa-search"></i></button>
    </div>
</div>

<!-- ============================================
     2. Orders Content (주문 리스트 컨테이너)
     ============================================ -->
<div class="card border-0 mb-4">
    <div class="table-responsive">
        <table class="table table-hover align-middle mb-0 text-nowrap">
            <thead class="table-light">
                <tr>
                    <th width="1%">
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="selectAll" />
                            <label class="form-check-label" for="selectAll"></label>
                        </div>
                    </th>
                    <th>Order #</th>
                    <th>Date</th>
                    <th>Customer</th>
                    <th>Items (Products)</th>
                    <th>Total Price</th>
                    <th>Payment Status</th>
                    <th>Fulfillment</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                
                <!-- Order Row 1 -->
                <tr>
                    <td>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="chk1" />
                            <label class="form-check-label" for="chk1"></label>
                        </div>
                    </td>
                    <td>
                        <a href="/order/details/ORD-72901" class="text-decoration-none text-theme fw-bold">#ORD-72901</a>
                    </td>
                    <td>13 Oct 2026, 14:23</td>
                    <td>
                        <div class="d-flex align-items-center">
                            <div class="w-30px h-30px bg-gray-200 rounded-circle d-flex align-items-center justify-content-center text-dark fw-bold me-2">JS</div>
                            John Smith
                        </div>
                    </td>
                    <td>
                        <div class="d-flex align-items-center">
                            <!-- 가장 비싼 대표품목 썸네일 노출 -->
                            <img src="../assets/img/product/product-1.png" class="w-40px h-40px rounded me-2" alt="iPhone 15 Pro" />
                            <div>
                                <div class="text-dark fw-bold">iPhone 15 Pro Max</div>
                                <div class="text-muted fs-11px">+ 2 other items</div>
                            </div>
                        </div>
                    </td>
                    <td class="fw-bold">$1,599.00</td>
                    <td><span class="badge bg-success bg-opacity-20 text-success px-2 py-1 rounded fs-12px">Paid</span></td>
                    <td><span class="badge bg-warning bg-opacity-20 text-warning px-2 py-1 rounded fs-12px">Processing</span></td>
                    <td>
                        <a href="#" class="btn btn-sm btn-white w-20px h-20px p-0 d-flex align-items-center justify-content-center" data-bs-toggle="dropdown"><i class="fa fa-ellipsis-h text-gray-500"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                            <a href="#" class="dropdown-item">View Details</a>
                            <a href="#" class="dropdown-item">Edit Order</a>
                            <div class="dropdown-divider"></div>
                            <a href="#" class="dropdown-item text-danger">Cancel Order</a>
                        </div>
                    </td>
                </tr>
                
                <!-- Order Row 2 -->
                <tr>
                    <td>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="chk2" />
                            <label class="form-check-label" for="chk2"></label>
                        </div>
                    </td>
                    <td>
                        <a href="#" class="text-decoration-none text-theme fw-bold">#ORD-72900</a>
                    </td>
                    <td>12 Oct 2026, 09:12</td>
                    <td>
                        <div class="d-flex align-items-center">
                            <img src="../assets/img/user/user-5.jpg" class="w-30px h-30px rounded-circle me-2" alt="Alice Doe" />
                            Alice Doe
                        </div>
                    </td>
                    <td>
                        <div class="d-flex align-items-center">
                            <img src="../assets/img/product/product-2.png" class="w-40px h-40px rounded me-2" alt="AirPods" />
                            <div>
                                <div class="text-dark fw-bold">AirPods Pro Gen 2</div>
                                <div class="text-muted fs-11px">x 1</div>
                            </div>
                        </div>
                    </td>
                    <td class="fw-bold">$249.00</td>
                    <td><span class="badge bg-secondary bg-opacity-20 text-secondary px-2 py-1 rounded fs-12px">Pending</span></td>
                    <td><span class="badge bg-dark bg-opacity-20 text-dark px-2 py-1 rounded fs-12px">Unfulfilled</span></td>
                    <td>
                        <a href="#" class="btn btn-sm btn-white w-20px h-20px p-0 d-flex align-items-center justify-content-center" data-bs-toggle="dropdown"><i class="fa fa-ellipsis-h text-gray-500"></i></a>
                        <div class="dropdown-menu dropdown-menu-end">
                            <a href="#" class="dropdown-item">View Details</a>
                            <a href="#" class="dropdown-item">Mark as Paid</a>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>
    <!-- 3. Pagination Footer -->
    <div class="card-footer bg-transparent border-0 d-flex align-items-center justify-content-between p-3">
        <div class="fs-13px text-gray-500">Showing 1 to 10 of 57 entries</div>
        <ul class="pagination mb-0">
            <li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>
            <li class="page-item active"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
    </div>
</div>
```

### 2. Implementation Notes
- 셀 내용이 두 줄인 경우: 상품 썸네일과 상품명 조합, 유저 아바타와 닉네임 조합은 Flex `align-items-center` 마크업을 사용하여 균형을 맞춥니다.
- `bg-opacity-20` 파스텔 톤 뱃지를 적용하여 결제(Paid)와 배송(Shipped, Processing) 상태를 이질감 없이 산뜻하게 표현하는 것이 Color Admin 최신 V3 커머스 트렌드입니다.
