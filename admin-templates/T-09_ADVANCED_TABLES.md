# [T-09] ADVANCED_TABLES

**용도**: 수천 건 이상의 방대한 데이터를 다루거나, 엑셀 다운로드, 컬럼 숨김, 다중 정렬 등 복잡한 제어가 필요한 화면에 쓰입니다.
DataTables.js 플러그인(또는 그에 상응하는 Frontend Table 라이브러리)의 UI 레이아웃 표준입니다.

### 1. Advanced Table Structure (Buttons & Responsive)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/table_manage_buttons.html](https://seantheme.com/color-admin/admin/html/table_manage_buttons.html)

일반 `T-02` 패널 구조에서 표출되는 테이블 위에 **기능 버튼(Copy, CSV, Excel, PDF, Print)** 랜더링 구역이 삽입됩니다.

```html
<div class="panel panel-inverse">
  <div class="panel-heading">
    <h4 class="panel-title">결제 내역 조회 (Advanced)</h4>
  </div>

  <div class="panel-body">
    <!-- ============================================
         1. Table Toolbar (데이터 추출 버튼 그룹)
         ============================================ -->
    <!-- DataTables 렌더링 시 통상적으로 자동 삽입되지만, 커스텀 시 아래 컨테이너 구조를 유지합니다 -->
    <div class="dt-buttons btn-group mb-3">
        <button class="btn btn-default btn-sm" tabindex="0" type="button"><span><i class="fa fa-copy"></i> Copy</span></button>
        <button class="btn btn-default btn-sm" tabindex="0" type="button"><span><i class="fa fa-file-csv"></i> CSV</span></button>
        <button class="btn btn-default btn-sm" tabindex="0" type="button"><span><i class="fa fa-file-excel text-success"></i> Excel</span></button>
        <button class="btn btn-default btn-sm" tabindex="0" type="button"><span><i class="fa fa-file-pdf text-danger"></i> PDF</span></button>
        <button class="btn btn-default btn-sm" tabindex="0" type="button"><span><i class="fa fa-print"></i> Print</span></button>
    </div>

    <!-- ============================================
         2. Table (Fixed Header & Responsive)
         ============================================ -->
    <!-- table-responsive 클래스를 통해 모바일 환경에서 가로 스크롤을 허용 -->
    <!-- table-hover 설정으로 마우스 이동 시 행 식별 용이 -->
    <div class="table-responsive">
      <table id="data-table-buttons" class="table table-striped table-bordered table-hover align-middle mb-0">
        <thead class="table-dark">
          <!-- 멀티 라인 헤더(Complex Header)의 경우 rowspan, colspan 적극 활용 -->
          <tr>
            <th width="1%">No.</th>
            <th class="text-nowrap">고객명</th>
            <th class="text-nowrap">상품명</th>
            <th class="text-nowrap text-center">결제금액</th>
            <th class="text-nowrap">상태</th>
          </tr>
        </thead>
        <tbody>
          <!-- Data Rows -->
          <tr>
            <td>1</td>
            <td>김철수</td>
            <td>Premium 요금제 1년권</td>
            <td class="text-center text-theme fw-bold">120,000 원</td>
            <td><span class="badge bg-success">결제완료</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
```
