# [T-12] AUTHENTICATION (Login / Register)

**용도**: 서비스 진입점 역할을 하는 로그인 창, 회원가입 모달, 비밀번호 찾기 등 인증(Auth) 관련 페이지의 특수 레이아웃입니다.
일반적인 콘텐츠 컴포넌트(`T-01`)와 달리, 전체 화면(`100vh`)을 덮고 사이드바와 헤더가 없는 독립적인 뷰를 갖습니다.

### 1. Login V3 (배경 이미지 + 다크 박스 로그인)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/login_v3.html](https://seantheme.com/color-admin/admin/html/login_v3.html)

배경에 브랜드 이미지를 화면에 꽉 차게 깔고, 우측(또는 중앙)에 반투명한 로그인 패널 박스(`login-container`)를 배치하는 세련된 형태입니다.

```html
<!-- [인증 전용 페이지 래퍼] -->
<!-- header, sidebar가 없는 로그인 화면용 단독 뼈대 -->
<div id="page-container">
  
  <!-- ============================================
       1. Login Page Full Wrapper
       ============================================ -->
  <!-- login-v3 클래스가 전체 배경과 사이드 정렬을 제어 -->
  <div class="login login-v3">
     
     <!-- 1-1. 전체 화면 배경 이미지 (Bg Cover) -->
     <div class="login-bg" style="background-image: url('login-bg-1.jpg')"></div>

     <!-- 1-2. 로그인 박스 컨테이너 -->
     <div class="login-container">
        
        <!-- 로고 및 서비스 타이틀 영역 -->
        <div class="login-header">
           <div class="brand">
              <div class="d-flex align-items-center">
                 <span class="logo"></span> <b>Color</b> Admin
              </div>
              <small>Bootstrap 5 Responsive Admin Template</small>
           </div>
           <div class="icon">
              <i class="fa fa-sign-in-alt"></i>
           </div>
        </div>

        <!-- 아이디/비밀번호 폼 입력 영역 -->
        <div class="login-content">
           <form action="/dashboard" method="POST" class="margin-bottom-0">
              
              <!-- 이메일 입력 -->
              <div class="form-floating mb-15px">
                 <!-- form-control 플로팅 라벨 패턴 사용 -->
                 <input type="text" class="form-control h-45px fs-13px" placeholder="Email Address" id="emailAddress" />
                 <label for="emailAddress" class="d-flex align-items-center fs-13px text-gray-600">Email Address</label>
              </div>
              
              <!-- 패스워드 입력 -->
              <div class="form-floating mb-15px">
                 <input type="password" class="form-control h-45px fs-13px" placeholder="Password" id="password" />
                 <label for="password" class="d-flex align-items-center fs-13px text-gray-600">Password</label>
              </div>
              
              <!-- 로그인 유지 체크박스 -->
              <div class="form-check mb-30px">
                 <input class="form-check-input" type="checkbox" value="1" id="rememberMe" />
                 <label class="form-check-label" for="rememberMe">
                    기기에서 로그인 상태 유지
                 </label>
              </div>
              
              <!-- 서브밋 버튼 -->
              <div class="mb-15px">
                 <button type="submit" class="btn btn-theme d-block h-45px w-100 btn-lg fs-14px">Sign me in</button>
              </div>
              
              <!-- 회원 가입 유도 링크 -->
              <div class="mb-40px pb-40px text-inverse">
                 아직 계정이 없으신가요? <a href="/register" class="text-primary">여기를 눌러 가입하세요.</a>
              </div>
              
              <!-- 하단 Copyright -->
              <hr />
              <p class="text-center text-gray-500-darker mb-0">
                 &copy; Color Admin All Right Reserved 2026
              </p>
           </form>
        </div> <!-- /.login-content -->

     </div> <!-- /.login-container -->
  </div> <!-- /.login-v3 -->
</div> <!-- /.page-container -->
```
