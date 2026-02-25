# [T-10] POS_SYSTEM

**용도**: 결제(Counter Checkout), 고객 문의 접수, 식당 테이블 예약 현황(Table Booking)같이 태블릿 기기 등에서 특화되어 사용되는 전체화면형(POS) 인터페이스 구조입니다.
일반 Admin 레이아웃(T-01)과 달리 사이드바가 닫혀있거나 고정 결제 금액 패널이 우측에 위치하는 형태입니다.

### 1. POS Counter Checkout (계산원 결제 패널)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/pos_counter_checkout.html](https://seantheme.com/color-admin/admin/html/pos_counter_checkout.html)

이 레이아웃은 페이지 전체를 덮으며(Header/Sidebar 미사용 가능), 좌측에 상품 그리드(Menu Board)와 우측에 장바구니/결제 패널(Order Sidebar)을 7:5 또는 8:4 비율로 배치합니다.

```html
<!-- [POS 특화 페이지 컨테이너] 
     class="pos" 및 "pos-with-sidebar" 구조를 통해 양분 레이아웃 구성
-->
<div class="pos pos-with-sidebar" id="pos">
  
  <!-- ============================================
       1. Left Area: POS 컨텐츠 영역 (상품 리스트)
       ============================================ -->
  <div class="pos-content">
    
    <!-- POS 상단 서브 헤더 (카테고리 탭 등) -->
    <div class="pos-content-header" style="height: 60px;">
       <ul class="nav nav-tabs nav-tabs-inverse">
          <li class="nav-item"><a href="#" class="nav-link active">전체 메뉴</a></li>
          <li class="nav-item"><a href="#" class="nav-link">세트 상품</a></li>
          <li class="nav-item"><a href="#" class="nav-link">단품 사이드</a></li>
       </ul>
    </div>
    
    <!-- POS 진짜 본문 (상품 그리드 렌더링) -->
    <div class="pos-content-body p-3" data-scrollbar="true" data-height="100%">
      <div class="row gx-2 gy-2">
        <!-- 단일 상품 카드 아이템 (클릭 가능) -->
        <div class="col-xl-3 col-lg-4 col-md-6 pb-2">
          <a href="#" class="pos-product">
            <div class="img" style="background-image: url(product_img1.jpg)"></div>
            <div class="info">
              <div class="title text-truncate">메가 커피 Ice</div>
              <div class="desc text-truncate">라지 사이즈 아메리카노</div>
              <div class="price">₩3,000</div>
            </div>
          </a>
        </div>
        <!-- 또 다른 상품 ... -->
        <div class="col-xl-3 col-lg-4 col-md-6 pb-2">
           <!-- ... -->
        </div>
      </div>
    </div>
  </div>

  <!-- ============================================
       2. Right Area: POS 장바구니/영수증 사이드바
       ============================================ -->
  <!-- 장바구니 및 총계산 내역을 보여주는 고정 패널 -->
  <div class="pos-sidebar" id="pos-sidebar">
    
    <div class="pos-sidebar-header">
      <div class="d-flex align-items-center justify-content-between">
         <div class="title">Current Order (테이블 5번)</div>
         <div class="order-no">#0014</div>
      </div>
    </div>
    
    <div class="pos-sidebar-body" data-scrollbar="true" data-height="100%">
      <!-- 선택된 상품 행(Cart Item) -->
      <div class="pos-table-row">
         <div class="row w-100 align-items-center m-0">
             <div class="col-8">
                 <div class="pos-product-thumb">
                     <div class="img" style="background-image: url(product_img1.jpg)"></div>
                     <div class="info">
                         <div class="title">메가 커피 Ice</div>
                         <div class="desc">- 얼음 많이<br>- 시럽 추가</div>
                     </div>
                 </div>
             </div>
             <!-- 수량 증감 버튼 영역 -->
             <div class="col-4 text-end">
                 <div class="pos-qty input-group">
                     <a href="#" class="btn btn-default"><i class="fa fa-minus"></i></a>
                     <input type="text" class="form-control" value="2" readonly>
                     <a href="#" class="btn btn-default"><i class="fa fa-plus"></i></a>
                 </div>
             </div>
         </div>
         <div class="row w-100 m-0 pt-2 pb-2 text-end">
             <div class="col-12 fw-bold text-dark">₩6,000</div>
         </div>
      </div>
      <!-- End Cart Item -->
    </div>
    
    <!-- 장바구니 총합계 & 결제 버튼 영역 -->
    <div class="pos-sidebar-footer">
       <div class="d-flex align-items-center mb-2">
           <div class="flex-1 fw-bold fs-14px">Total</div>
           <div class="text-end fw-bold fs-16px text-theme">₩6,000</div>
       </div>
       <div class="mt-3">
           <button class="btn btn-theme w-100 p-2 fs-16px"><i class="fa fa-credit-card fa-fw"></i> 결제 진행하기 (Checkout)</button>
       </div>
    </div>
    
  </div> <!-- /.pos-sidebar -->
</div> <!-- /.pos -->
```
