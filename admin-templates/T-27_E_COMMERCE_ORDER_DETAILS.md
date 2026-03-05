# [T-27] E_COMMERCE_ORDER_DETAILS

**용도**: E-commerce 시스템 내 특정 개별 주문 건(Order ID 기준)의 납품서, 결제 상태, 배송 정보, 구매 품목 상세를 총망라하여 보여주는 그리드 정보 화면입니다.

### 1. Template Structure (Order Details)

오더 디테일은 좌측에 핵심 구매 품목 리스트와 결제 요약(Subtotal/Tax/Total)을, 우측에 구매자, 결제정보, 배송지(Shipping)를 패널 형태로 나누어 배치하는 전형적인 이커머스 상세 뷰 형식을 취합니다.

```html
<!-- [페이지 전체 헤더] -->
<div class="d-flex align-items-center mb-3">
    <div>
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
            <li class="breadcrumb-item"><a href="javascript:;">Orders</a></li>
            <li class="breadcrumb-item active">Order Details</li>
        </ol>
        <h1 class="page-header mb-0">Order #ORD-72901</h1>
    </div>
    <!-- 상단 뱃지 및 액션 -->
    <div class="ms-auto d-flex align-items-center">
        <span class="badge bg-success bg-opacity-20 text-success px-2 py-1 rounded fs-12px me-2">Paid</span>
        <span class="badge bg-warning bg-opacity-20 text-warning px-2 py-1 rounded fs-12px me-3">Processing</span>
        <a href="#" class="btn btn-outline-default btn-rounded me-2"><i class="fa fa-print"></i></a>
        <a href="#" class="btn btn-theme btn-rounded px-4"><i class="fa fa-truck fa-fw me-1"></i> Fulfill Order</a>
    </div>
</div>

<div class="row gx-4">
    <!-- ============================================
         1. Left Column: 구매 품목 리스트 및 요약
         ============================================ -->
    <div class="col-lg-8">
        <div class="card border-0 mb-4">
            <div class="card-header bg-transparent border-0 d-flex align-items-center fw-bold text-dark p-3">
                <i class="fa fa-box fa-fw text-theme fs-16px me-2"></i> Products (3 Items)
                <a href="#" class="btn btn-sm btn-white ms-auto">Edit</a>
            </div>
            <div class="card-body p-0">
                <div class="table-responsive">
                    <table class="table table-borderless table-sm align-middle mb-0 text-nowrap">
                        <thead class="table-light">
                            <tr>
                                <th class="ps-3 border-bottom border-gray-200">Product</th>
                                <th width="15%" class="text-center border-bottom border-gray-200">Price</th>
                                <th width="15%" class="text-center border-bottom border-gray-200">Quantity</th>
                                <th width="15%" class="text-end pe-3 border-bottom border-gray-200">Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Item 1 -->
                            <tr>
                                <td class="ps-3 py-3">
                                    <div class="d-flex align-items-center">
                                        <div class="w-50px h-50px bg-light rounded d-flex align-items-center justify-content-center p-1 me-3">
                                            <img src="../assets/img/product/product-1.png" class="mw-100 mh-100" />
                                        </div>
                                        <div>
                                            <div class="text-dark fw-bold mb-1">iPhone 15 Pro Max</div>
                                            <div class="text-gray-500 fs-12px">Color: Titanium Blue, Storage: 512GB</div>
                                        </div>
                                    </div>
                                </td>
                                <td class="text-center">$1,199.00</td>
                                <td class="text-center">1</td>
                                <td class="text-end fw-bold text-dark pe-3">$1,199.00</td>
                            </tr>
                            
                            <!-- Item 2 -->
                            <tr>
                                <td class="ps-3 py-3 border-top border-gray-100">
                                    <div class="d-flex align-items-center">
                                        <div class="w-50px h-50px bg-light rounded d-flex align-items-center justify-content-center p-1 me-3">
                                            <img src="../assets/img/product/product-2.png" class="mw-100 mh-100" />
                                        </div>
                                        <div>
                                            <div class="text-dark fw-bold mb-1">AirPods Gen 3</div>
                                            <div class="text-gray-500 fs-12px">Color: White, Type: MagSafe</div>
                                        </div>
                                    </div>
                                </td>
                                <td class="text-center">$179.00</td>
                                <td class="text-center">2</td>
                                <td class="text-end fw-bold text-dark pe-3">$358.00</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <!-- Amount Summary -->
            <div class="card-footer bg-transparent border-top p-3 text-end">
                <div class="row fw-bold text-dark mb-2">
                    <div class="col-9 text-gray-600 fw-normal">Subtotal:</div>
                    <div class="col-3">$1,557.00</div>
                </div>
                <div class="row fw-bold text-dark mb-2">
                    <div class="col-9 text-gray-600 fw-normal">Shipping (Standard):</div>
                    <div class="col-3">$15.00</div>
                </div>
                <div class="row fw-bold text-dark mb-3">
                    <div class="col-9 text-gray-600 fw-normal">Tax (10%):</div>
                    <div class="col-3">$27.00</div>
                </div>
                <div class="row fw-bold text-dark fs-16px mb-1">
                    <div class="col-9">Total:</div>
                    <div class="col-3">$1,599.00</div>
                </div>
            </div>
        </div>
        
        <!-- Timeline (History) -->
        <div class="card border-0 mb-4">
            <div class="card-header bg-transparent border-0 fw-bold text-dark p-3">
                <i class="fa fa-history fa-fw text-theme fs-16px me-2"></i> Order History
            </div>
            <div class="card-body p-3">
                <!-- T-20의 미니 타임라인 형태를 빌려와 간단한 배송/결제 히스토리 출력 -->
                <div class="alert alert-secondary fs-13px m-0 border-0">
                    <strong class="d-block mb-1">13 Oct 2026, 14:23</strong> Order placed by the customer. Payment Gateway (Stripe) approved the charge.
                </div>
            </div>
        </div>
    </div>
    
    <!-- ============================================
         2. Right Column: 고객 및 배송/결제 정보 요약
         ============================================ -->
    <div class="col-lg-4">
        <!-- Customer Info -->
        <div class="card border-0 mb-4">
            <div class="card-header bg-transparent border-0 fw-bold text-dark p-3">
                <i class="fa fa-user fa-fw text-theme fs-16px me-2"></i> Customer
            </div>
            <div class="card-body p-3 border-top border-gray-100">
                <div class="d-flex align-items-center mb-3">
                    <div class="w-40px h-40px bg-gray-200 rounded-circle d-flex align-items-center justify-content-center fw-bold text-dark me-2">JS</div>
                    <div>
                        <div class="text-dark fw-bold">John Smith</div>
                        <div class="text-theme fs-12px"><i class="fa fa-check-circle me-1"></i> Verified Account</div>
                    </div>
                </div>
                <div class="fs-13px text-gray-600 mb-1"><i class="fa fa-envelope fa-fw me-1 text-gray-400"></i> john.smith@gmail.com</div>
                <div class="fs-13px text-gray-600"><i class="fa fa-phone fa-fw me-1 text-gray-400"></i> +1 (555) 123-4567</div>
            </div>
        </div>
        
        <!-- Shipping Address -->
        <div class="card border-0 mb-4">
            <div class="card-header bg-transparent border-0 d-flex align-items-center fw-bold text-dark p-3">
                <i class="fa fa-truck fa-fw text-theme fs-16px me-2"></i> Shipping Address
                <a href="#" class="btn btn-sm btn-white ms-auto">Edit</a>
            </div>
            <div class="card-body p-3 border-top border-gray-100 fs-13px text-gray-600 lh-lg">
                <div class="text-dark fw-bold mb-1">John Smith</div>
                1234 Tech Blvd, Suite 500<br />
                San Francisco, CA 94107<br />
                United States
            </div>
        </div>
        
        <!-- Payment Information -->
        <div class="card border-0 mb-4">
            <div class="card-header bg-transparent border-0 fw-bold text-dark p-3">
                <i class="fa fa-credit-card fa-fw text-theme fs-16px me-2"></i> Payment Details
            </div>
            <div class="card-body p-3 border-top border-gray-100 fs-13px text-gray-600">
                <div class="d-flex align-items-center mb-2">
                    <i class="fab fa-cc-visa fa-2x me-2 text-dark"></i>
                    <div>
                        <div class="text-dark fw-bold">Visa ending in 4242</div>
                        <div class="fs-11px">Exp: 08/2028</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### 2. Implementation Notes
- **이커머스 그리드 레이아웃**: 쇼핑 콘텐츠의 상세 페이지는 패널 제목란에 어울리는 `FontAwesome` 아이콘(fa-box, fa-truck, fa-user 등)을 적극적으로 동반하여 어떤 묶음 단위인지 가시성을 높이는 것을 권장합니다.
- `Order Details`는 T-11의 `Invoice`(명세서) 템플릿과 흡사한 정보를 다루나, T-11은 출력을 위한 백지(프린트 친화적) 화면이고 현재 템플릿(T-27)은 어드민 조작 및 관리 통제용 UI를 갖추기 위한 카드 위젯의 집합입니다.
