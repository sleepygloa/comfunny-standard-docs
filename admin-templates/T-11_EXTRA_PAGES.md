# [T-11] EXTRA_PAGES

**용도**: 목록형(T-02)이나 등록형(T-03) 폼 구조에 속하지 않는, 특수한 단일 화면용 템플릿입니다.
주로 사용자의 프로필 조회, 온라인 영수증/인보이스 출력, 특정 개체의 상세 화면(Details) 페이지로 사용됩니다.

### 1. Invoice (영수증 / 명세서)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/extra_invoice.html](https://seantheme.com/color-admin/admin/html/extra_invoice.html)

인쇄(Print)가 가능하도록 최적화된 하얀색 배경의 A4 비율 문서 컨테이너입니다.

```html
<div class="invoice">
  <!-- 1. Invoice Company Header (발행인 정보) -->
  <div class="invoice-company text-inverse f-w-600">
    <span class="pull-right hidden-print">
      <a href="javascript:;" class="btn btn-sm btn-white m-b-10 p-l-5"><i class="fa fa-file-pdf t-plus-1 text-danger fa-fw fa-lg"></i> Export as PDF</a>
      <a href="javascript:;" onclick="window.print()" class="btn btn-sm btn-white m-b-10 p-l-5"><i class="fa fa-print t-plus-1 fa-fw fa-lg"></i> Print</a>
    </span>
    COMFUNNY Inc. <!-- 사명 -->
  </div>
  
  <!-- 2. Invoice Header (송장 정보 및 수신자) -->
  <div class="invoice-header">
    <div class="invoice-from">
      <small>from</small>
      <address class="m-t-5 m-b-5">
        <strong class="text-inverse">COMFUNNY, Inc.</strong><br>
        서울시 강남구 테헤란로 123<br>
        사업자번호: 123-45-67890<br>
        Phone: (02) 1234-5678<br>
      </address>
    </div>
    <div class="invoice-to">
      <small>to</small>
      <address class="m-t-5 m-b-5">
        <strong class="text-inverse">김철수 고객님</strong><br>
        경기도 성남시 분당구 판교역로 152<br>
        Phone: 010-9876-5432<br>
      </address>
    </div>
    <div class="invoice-date">
      <small>Invoice / July period</small>
      <div class="date text-inverse m-t-5">July 15, 2026</div>
      <div class="invoice-detail">
        #0000123DSS<br>
        정기 구독 결제건
      </div>
    </div>
  </div>

  <!-- 3. Invoice Content (상세 청구 내역 표) -->
  <div class="invoice-content">
    <!-- table-invoice 클래스를 사용하여 외곽선 없이 렌더링 -->
    <div class="table-responsive">
      <table class="table table-invoice">
        <thead>
          <tr>
            <th>품목 내역</th>
            <th class="text-center" width="10%">단가</th>
            <th class="text-center" width="10%">수량</th>
            <th class="text-right" width="20%">합계</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="text-inverse">Pro 멤버십 1년 구독권</span><br>
              <small>2026.07.15 ~ 2027.07.14 무제한 이용권</small>
            </td>
            <td class="text-center">₩120,000</td>
            <td class="text-center">1</td>
            <td class="text-right">₩120,000</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 4. Invoice Price (총 결제 요약) -->
    <div class="invoice-price">
      <div class="invoice-price-left">
        <div class="invoice-price-row">
          <div class="sub-price">
            <small>SUBTOTAL</small>
            <span class="text-inverse">₩109,090</span>
          </div>
          <div class="sub-price">
            <i class="fa fa-plus text-muted"></i>
          </div>
          <div class="sub-price">
            <small>VAT (10%)</small>
            <span class="text-inverse">₩10,910</span>
          </div>
        </div>
      </div>
      <div class="invoice-price-right">
        <small>TOTAL</small> <span class="f-w-600">₩120,000</span>
      </div>
    </div>
  </div>
  
  <!-- 5. Invoice Footer (하단 정책) -->
  <div class="invoice-footer">
    <p class="text-center m-b-5 f-w-600">
      이용해 주셔서 감사합니다.
    </p>
    <p class="text-center">
      <span class="m-r-10"><i class="fa fa-fw fa-lg fa-globe"></i> comfunny.com</span>
      <span class="m-r-10"><i class="fa fa-fw fa-lg fa-phone-volume"></i> T:02-123-4567</span>
      <span class="m-r-10"><i class="fa fa-fw fa-lg fa-envelope"></i> contact@comfunny.com</span>
    </p>
  </div>
</div>
```
