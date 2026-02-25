# [T-02] DATA_TABLE_PANEL

**용도**: 백오피스에서 가장 흔하게 쓰이는 **목록형 데이터(Grid/Table)** 및 **차트 표출**을 위한 표준 컴포넌트 래퍼(Wrapper)입니다.
`.panel` 컴포넌트는 정보를 시각화 그룹으로 묶고 집중도를 높여주는 핵심 역할을 합니다.

```html
<!-- 
     [Panel Component 기본 구조]
     class="panel panel-inverse" : Dark 계열 헤더를 가진 기본 패널
     class="panel panel-default" : Light 계열 헤더 패널
-->
<div class="panel panel-inverse">
  
  <!-- ===============================
       1. Panel Header (제목 및 제어부)
       =============================== -->
  <div class="panel-heading">
    <!-- 패널 제목 (필수) -->
    <h4 class="panel-title">직원 목록 관리 Data Table</h4>
    
    <!-- 패널 헤더 우측 컨트롤 버튼 (선택 사항) -->
    <div class="panel-heading-btn">
      <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-default" data-click="panel-expand" title="전체화면">
        <i class="fa fa-expand"></i>
      </a>
      <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-success" data-click="panel-reload" title="새로고침">
        <i class="fa fa-redo"></i>
      </a>
      <a href="javascript:;" class="btn btn-xs btn-icon btn-circle btn-warning" data-click="panel-collapse" title="접기">
        <i class="fa fa-minus"></i>
      </a>
    </div>
  </div>

  <!-- ===============================
       2. Panel Body (본문)
       =============================== -->
  <div class="panel-body">
    <!-- 상단 도구 모음 (검색 필터, 엑셀 다운로드 버튼 등) -->
    <div class="d-flex justify-content-between mb-3">
        <div>
            <!-- 좌측 정렬 버튼 그룹 -->
            <button class="btn btn-primary btn-sm"><i class="fa fa-plus me-1"></i> 신규 등록</button>
        </div>
        <div>
            <!-- 우측 정렬 검색창 -->
            <div class="input-group input-group-sm">
                <input type="text" class="form-control" placeholder="회원 이름 검색...">
                <button class="btn btn-default" type="button"><i class="fa fa-search"></i></button>
            </div>
        </div>
    </div>

    <!-- 데이터 테이블 -->
    <div class="table-responsive">
      <table class="table table-striped table-bordered align-middle">
        <thead class="table-dark">
          <tr>
            <th width="1%"><input type="checkbox" class="form-check-input"></th>
            <th width="5%">ID</th>
            <th class="text-nowrap">이름</th>
            <th class="text-nowrap">부서</th>
            <th class="text-nowrap text-center">상태</th>
            <th width="10%">관리</th>
          </tr>
        </thead>
        <tbody>
          <!-- Data Row 1 -->
          <tr>
            <td><input type="checkbox" class="form-check-input"></td>
            <td>1</td>
            <td>홍길동</td>
            <td>개발팀</td>
            <td class="text-center">
              <span class="badge bg-success">활성</span>
            </td>
            <td>
              <button class="btn btn-xs btn-info">수정</button>
              <button class="btn btn-xs btn-danger">삭제</button>
            </td>
          </tr>
          <!-- Data Row 2 ... -->
        </tbody>
      </table>
    </div>

    <!-- 하단 페이징(Pagination) -->
    <div class="d-flex justify-content-end mt-3">
        <ul class="pagination pagination-sm m-0">
            <li class="page-item disabled"><a href="#" class="page-link">이전</a></li>
            <li class="page-item active"><a href="#" class="page-link">1</a></li>
            <li class="page-item"><a href="#" class="page-link">2</a></li>
            <li class="page-item"><a href="#" class="page-link">다음</a></li>
        </ul>
    </div>
  </div> <!-- /.panel-body -->

</div> <!-- /.panel -->
```
