# [T-23] COMING_SOON

**용도**: 서비스 공식 오픈 전 대기 열이나, 대규모 점검 중일 때 유저들이 이메일 구독 등을 통해 출시 알림을 받게 하는 사전 공지용 랜딩 페이지입니다.

### 1. Template Structure (Coming Soon Page)

커밍순 화면은 전체 화면 비율을 차지하며, 화려한 스플래시 배경 이미지 위에 시일 카운트다운 타이머 계기판과 뉴스레터 폼이 조합되는 형태입니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div id="page-container" class="page-container">
    
    <!-- ============================================
         1. Coming Soon Background (배경)
         ============================================ -->
    <div class="coming-soon-bg" style="background-image: url('../assets/img/login-bg/login-bg-14.jpg');"></div>
    
    <!-- ============================================
         2. Coming Soon Content Box
         ============================================ -->
    <div class="coming-soon">
        <div class="coming-soon-header">
            <!-- 타이틀 코어 텍스트 -->
            <div class="bg-cover"></div>
            <div class="brand">
                <span class="logo"></span> <b>COMFUNNY</b> NextGen
            </div>
            <div class="desc">
                지금껏 보지 못했던 혁신적인 협업 관리 도구가 곧 찾아옵니다. 
                가장 먼저 소식을 접하려면 뉴스레터를 구독해 주세요.
            </div>
            
            <!-- 오픈 예정일 카운트다운 (JS 바인딩 대상) -->
            <div class="timer">
                <div id="timer">
                    <!-- Javascript 로직으로 갱신되는 항목 -->
                    <div class="is-countdown">
                        <span class="countdown-row countdown-show4">
                            <!-- 일(Days) -->
                            <span class="countdown-section">
                                <span class="countdown-amount">15</span>
                                <span class="countdown-period">Days</span>
                            </span>
                            <!-- 시간(Hours) -->
                            <span class="countdown-section">
                                <span class="countdown-amount">08</span>
                                <span class="countdown-period">Hours</span>
                            </span>
                            <!-- 분(Minutes) -->
                            <span class="countdown-section">
                                <span class="countdown-amount">45</span>
                                <span class="countdown-period">Minutes</span>
                            </span>
                            <!-- 초(Seconds) -->
                            <span class="countdown-section">
                                <span class="countdown-amount">20</span>
                                <span class="countdown-period">Seconds</span>
                            </span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- ============================================
             3. Coming Soon Action Area (이메일 구독 폼)
             ============================================ -->
        <div class="coming-soon-content">
            <div class="desc">
                정식 출시 알림을 보내드립니다. 알림 수신을 위한 이메일을 남겨주세요.
            </div>
            <div class="input-group mb-2">
                <!-- 둥근 형태가 강조되는 인풋 그룹 라인 -->
                <input type="text" class="form-control" placeholder="Email Address" />
                <button type="button" class="btn btn-theme">Notify Me</button>
            </div>
            <p class="text-gray-500 mb-5">우리는 스팸 메일을 보내지 않으니 안심하십시오.</p>
            
            <!-- 개발사 혹은 SNS 채널 링크 -->
            <p>
                <a href="#" class="btn btn-icon btn-white btn-circle"><i class="fab fa-twitter"></i></a>
                <a href="#" class="btn btn-icon btn-white btn-circle"><i class="fab fa-facebook-f"></i></a>
                <a href="#" class="btn btn-icon btn-white btn-circle"><i class="fab fa-instagram"></i></a>
                <a href="#" class="btn btn-icon btn-white btn-circle"><i class="fab fa-dribbble"></i></a>
            </p>
        </div>
        
    </div> <!-- /.coming-soon -->
    
</div> <!-- /.page-container -->
```

### 2. Implementation Notes
- **카운트다운 스크립트 연동**: `#timer` 하위에 있는 숫자들은 정적인 마크업이 아니라, 서드파티 제이쿼리 플러그인인 `jquery.countdown` 모듈과 연동되어 1초마다 갱신(Tick)되어야 합니다.
- **`coming-soon-bg` 영역**: 사이트 서비스의 전체적인 테마 컬러 톤앤매너에 맞는 배경 이미지가 반드시 들어가야 화면 배치가 틀어지지 않고 깔끔하게 보입니다.
