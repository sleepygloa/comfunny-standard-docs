# [T-03] FORM_INPUTS

**용도**: 회원 등록, 상품 수정, 설정 변경 등 관리자가 데이터를 입력하고 전송(Submit)해야 하는 모든 Form 레이아웃의 표준 구성입니다. 
가독성 확보를 위해 수평(Horizontal) 폼 구조를 주로 권장하며, Label과 Input의 그리드 분배를 3:9 비율로 맞추는 것이 표준입니다.

```html
<!-- 
     [Form Panel 기본 구조]
-->
<div class="panel panel-inverse">
  
  <!-- 1. Panel Header -->
  <div class="panel-heading">
    <h4 class="panel-title">회원 정보 등록 폼</h4>
  </div>

  <!-- 2. Panel Body -->
  <div class="panel-body">
    <!-- form-horizontal 클래스를 통해 Label과 Input을 좌우 수평 배치 -->
    <form action="/" method="POST" class="form-horizontal">
      
      <!--=========================================
          [Field 1] 일반 Text Input (가로 행)
          =========================================-->
      <div class="row mb-15px">
        <!-- Label 영역 (12 그리드 중 3 할당, 우측 정렬) -->
        <label class="form-label col-form-label col-md-3">사용자명 <span class="text-danger">*</span></label>
        
        <!-- Input 영역 (12 그리드 중 9 할당) -->
        <div class="col-md-9">
          <input type="text" class="form-control" name="username" placeholder="공백 없이 영문 소문자 입력" required />
          <!-- 도움말(Hint) 텍스트 -->
          <small class="fs-13px text-gray-500-darker">로그인 시 사용될 고유 아이디입니다.</small>
        </div>
      </div>
      
      <!--=========================================
          [Field 2] Select Box (드롭다운)
          =========================================-->
      <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">부서 선택</label>
        <div class="col-md-9">
          <select class="form-select" name="department">
            <option value="">부서를 선택하세요</option>
            <option value="dev">개발팀</option>
            <option value="hr">인사팀</option>
            <option value="sales">영업팀</option>
          </select>
        </div>
      </div>

      <!--=========================================
          [Field 3] Radio Buttons (단일 옵션)
          =========================================-->
      <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">회원 상태</label>
        <div class="col-md-9">
          <div class="pt-2"> <!-- 라벨과 높이 맞춤 보정 -->
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="radio" name="status" id="status1" value="active" checked>
              <label class="form-check-label" for="status1">활성</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="radio" name="status" id="status2" value="inactive">
              <label class="form-check-label" for="status2">비활성</label>
            </div>
          </div>
        </div>
      </div>

      <!--=========================================
          [Field 4] Textarea (다중 로우 텍스트)
          =========================================-->
      <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">관리자 메모</label>
        <div class="col-md-9">
          <textarea class="form-control" name="memo" rows="4" placeholder="특이사항을 입력하세요"></textarea>
        </div>
      </div>

      <!--=========================================
          [Form Action Buttons] 하단 제출/취소 버튼
          =========================================-->
      <!-- submit 버튼은 항상 Primary 색상을 주어 액션을 유도합니다 -->
      <div class="row mt-4">
        <div class="col-md-9 offset-md-3">
          <button type="submit" class="btn btn-primary w-100px me-5px">등록하기</button>
          <button type="button" class="btn btn-default w-100px">취소</button>
        </div>
      </div>

    </form>
  </div> <!-- /.panel-body -->

</div> <!-- /.panel -->
```
