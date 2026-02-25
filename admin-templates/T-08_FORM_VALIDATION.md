# [T-08] FORM_VALIDATION

**용도**: 회원가입, 결제 정보 입력 등 사용자 데이터의 무결성 검증(Validation) 피드백을 전달할 때 필요한 폼의 상태 변화 및 에러 메시지 렌더링 표준입니다.
Bootstrap 5 및 Color Admin V3의 Validation 룰에 기반합니다.

### 1. Form Validation (상태 시각화)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/form_validation.html](https://seantheme.com/color-admin/admin/html/form_validation.html)

일반적인 폼 입력 태그(`form-control`)에 상태 클래스(`is-valid` 또는 `is-invalid`)를 바인딩하여 유저에게 즉각적인 시각 피드백을 주어야 합니다.

```html
<form class="needs-validation" novalidate>
  
  <div class="panel panel-inverse">
    <div class="panel-heading">
      <h4 class="panel-title">사용자 인증 정보</h4>
    </div>
    
    <div class="panel-body">
      
      <!-- ============================================
           성공(Valid) 상태 피드백
           ============================================ -->
      <div class="row mb-3">
        <label class="col-form-label col-md-3" for="validationValid">이름</label>
        <div class="col-md-9 position-relative"> 
          <!-- 입력값이 올바를 경우 'is-valid' 클래스 추가 -->
          <input type="text" class="form-control is-valid" id="validationValid" value="홍길동" required>
          <!-- 성공 메세지 출력 블록 -->
          <div class="valid-tooltip">
             멋진 이름이네요!
          </div>
        </div>
      </div>

      <!-- ============================================
           에러(Invalid) 상태 피드백
           ============================================ -->
      <div class="row mb-3">
        <label class="col-form-label col-md-3" for="validationInvalid">이메일 계정 <span class="text-danger">*</span></label>
        <div class="col-md-9">
          <div class="input-group has-validation">
            <span class="input-group-text" id="inputGroupPrepend">@</span>
            <!-- 입력값이 누락되거나 이메일 형식이 아닐 경우 'is-invalid' 추가 -->
            <input type="email" class="form-control is-invalid" id="validationInvalid" placeholder="example@gmail.com" aria-describedby="inputGroupPrepend" required>
            <!-- 에러 메세지 출력 블록 -->
            <div class="invalid-feedback">
               유효한 이메일 주소를 입력해 주셔야 합니다.
            </div>
          </div>
        </div>
      </div>

      <!-- ============================================
           체크박스/라디오 유효성 검증
           ============================================ -->
      <div class="row mb-3">
         <label class="col-form-label col-md-3">약관 동의</label>
         <div class="col-md-9">
            <div class="form-check pt-2">
               <!-- 체크하지 않고 넘어가려 할 때 'is-invalid' 렌더링 -->
               <input class="form-check-input is-invalid" type="checkbox" value="" id="invalidCheck" required>
               <label class="form-check-label" for="invalidCheck">
                 안내 문구와 책임 한계에 모두 동의합니다.
               </label>
               <div class="invalid-feedback">
                 서비스 이용을 위해 약관 동의는 필수입니다.
               </div>
            </div>
         </div>
      </div>
      
      <!-- ============================================
           통합 에러 알림 패널 (선택 사항)
           ============================================ -->
      <div class="alert alert-danger fade show mb-0">
          <i class="fa fa-exclamation-triangle fa-fw me-2"></i> <strong>2개</strong> 의 입력 항목에 오류가 발견되었습니다. 다시 확인해주세요.
      </div>
      
    </div>
  </div>
  
  <div class="text-center mt-3">
    <button class="btn btn-primary btn-lg" type="submit">인증하기</button>
  </div>

</form>
```
