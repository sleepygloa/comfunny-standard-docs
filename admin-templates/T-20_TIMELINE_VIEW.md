# [T-20] TIMELINE_VIEW

**용도**: 사용자의 활동 이력, 주문 배송 추적, 이슈 처리 과정 등 시간순 이벤트를 시각적으로 나열할 때 사용하는 세로형 타임라인 레이아웃입니다.

### 1. Template Structure (Timeline)

타임라인은 중앙을 관통하는 세로 선(line)을 기준으로 각 이벤트 요소(icon, info, content)가 시간에 따라 위에서 아래로 교차 배치되는 형태입니다.

```html
<ul class="timeline">
    <!-- ============================================
         1. 타임라인 아이템 (Event Block)
         ============================================ -->
    <li>
        <!-- 1-1. Timeline Time (좌측 일자 표시) -->
        <div class="timeline-time">
            <span class="date">today</span>
            <span class="time">04:20</span>
        </div>
        
        <!-- 1-2. Timeline Icon (중앙 교차점) -->
        <div class="timeline-icon">
            <a href="javascript:;">&nbsp;</a>
        </div>
        
        <!-- 1-3. Timeline Body (우측/좌측 내용 표시) -->
        <div class="timeline-body">
            <!-- Header (유저 정보 등) -->
            <div class="timeline-header">
                <span class="userimage">
                    <img src="../assets/img/user/user-1.jpg" alt="User Image" />
                </span>
                <span class="username"><a href="javascript:;">John Smith</a> <small></small></span>
                <span class="views">18 Views</span>
            </div>
            <!-- Content (본문) -->
            <div class="timeline-content">
                <p>
                    시스템 버그 수정을 반영한 핫픽스 배포를 완료했습니다. 현재 모니터링 중입니다.
                </p>
            </div>
            <!-- Footer (액션 버튼) -->
            <div class="timeline-footer">
                <a href="javascript:;" class="m-r-15 text-inverse-lighter"><i class="fa fa-thumbs-up fa-fw fa-lg m-r-3"></i> Like</a>
                <a href="javascript:;" class="m-r-15 text-inverse-lighter"><i class="fa fa-comments fa-fw fa-lg m-r-3"></i> Comment</a> 
            </div>
        </div>
    </li>
    
    <!-- ============================================
         2. 타임라인 아이템 (Media Block)
         ============================================ -->
    <li>
        <div class="timeline-time">
            <span class="date">yesterday</span>
            <span class="time">20:17</span>
        </div>
        <div class="timeline-icon">
            <a href="javascript:;">&nbsp;</a>
        </div>
        <div class="timeline-body">
            <div class="timeline-header">
                <span class="userimage">
                    <img src="../assets/img/user/user-2.jpg" alt="" />
                </span>
                <span class="username">Darren Bignell</span>
                <span class="views">3,128 Views</span>
            </div>
            <!-- 미디어 첨부형 본문 -->
            <div class="timeline-content">
                <p class="lead">
                    <i class="fa fa-quote-left fa-fw p-r-5"></i>
                    새로운 고객사 미팅 결과를 첨부 파일로 공유합니다.
                    <i class="fa fa-quote-right fa-fw p-l-5"></i>
                </p>
                <!-- 이미지 삽입 시 풀스크린 비율 유지 -->
                <div class="ratio ratio-16x9">
                    <img src="../assets/img/gallery/gallery-4.jpg" alt="Meeting Report" class="w-100 h-100 cover-fit" />
                </div>
            </div>
        </div>
    </li>
    
    <!-- ============================================
         3. 타임라인 로딩 스피너 (Infinite Scroll)
         ============================================ -->
    <li>
        <div class="timeline-icon">
            <a href="javascript:;">&nbsp;</a>
        </div>
        <div class="timeline-body">
            Loading...
            <div class="spinner-border spinner-border-sm ms-2" role="status"></div>
        </div>
    </li>
</ul>
```

### 2. Implementation Notes
- 화면 사이즈 축소 시, 양옆 지그재그 구조는 한 방향 정렬로 반응형 변형되도록 CSS에 설계되어 있습니다. 별도의 추가 마크업 없이 모바일을 지원합니다.
- `timeline` 클래스가 부여된 `ul` 리스트 하위에 `li` 엘리먼트를 동적으로 생성하는 방식으로 무한 스크롤 기반 피드(Feed)를 구현합니다.
