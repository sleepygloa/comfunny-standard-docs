# [T-17] CALENDAR_VIEW

**용도**: 일정 관리, 예약 시스템, 업무 스케줄링 대시보드에서 사용하는 풀 캘린더 화면입니다.

### 1. Template Structure (Calendar View)

캘린더 레이아웃은 주로 우측 패널에 FullCalendar 라이브러리를 바인딩할 대형 `div` 컨테이너를 배치하고, 좌측이나 상단에 외부 이벤트 소스(Drag & Drop) 패널을 구성합니다.

```html
<div class="row">
    <!-- ============================================
         1. Left Area: 외부 드래그 이벤트 생성기
         ============================================ -->
    <div class="col-lg-3">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">Draggable Events</h4>
            </div>
            <div class="panel-body">
                <p>드래그하여 캘린더 패널에 일정을 손쉽게 추가할 수 있습니다.</p>
                <div id="external-events" class="fc-event-list">
                    <div class="fc-event bg-blue" data-color="bg-blue">
                        <div class="fc-event-icon"><i class="fa fa-circle fa-fw fs-9px text-white"></i></div>
                        Meeting
                    </div>
                    <div class="fc-event bg-teal" data-color="bg-teal">
                        <div class="fc-event-icon"><i class="fa fa-circle fa-fw fs-9px text-white"></i></div>
                        Group Discussion
                    </div>
                    <div class="fc-event bg-success" data-color="bg-success">
                        <div class="fc-event-icon"><i class="fa fa-circle fa-fw fs-9px text-white"></i></div>
                        Brainstorming
                    </div>
                    <div class="fc-event bg-danger" data-color="bg-danger">
                        <div class="fc-event-icon"><i class="fa fa-circle fa-fw fs-9px text-white"></i></div>
                        System Maintenance
                    </div>
                </div>
                <!-- 캘린더 드롭 완료 후 목록에서 삭제 여부 체크박스 -->
                <div class="form-check mt-3">
                    <input class="form-check-input" type="checkbox" id="drop-remove" />
                    <label class="form-check-label" for="drop-remove">
                        Remove after drop
                    </label>
                </div>
            </div>
        </div>
    </div>
    
    <!-- ============================================
         2. Right Area: 캘린더 메인 컨테이너
         ============================================ -->
    <div class="col-lg-9">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">Calendar</h4>
                <div class="panel-heading-btn">
                    <a href="javascript:;" class="btn btn-xs btn-icon btn-default" data-toggle="panel-expand"><i class="fa fa-expand"></i></a>
                    <a href="javascript:;" class="btn btn-xs btn-icon btn-success" data-toggle="panel-reload"><i class="fa fa-redo"></i></a>
                </div>
            </div>
            <div class="panel-body">
                <!-- 캘린더가 렌더링 될 훅 컨테이너 -->
                <div id="calendar" class="calendar"></div>
            </div>
        </div>
    </div>
</div>
```

### 2. Implementation Notes
- 본 HTML은 **FullCalendar v5** (또는 이후 버전)와 연동됩니다. `script` 영역에서 `new FullCalendar.Calendar(document.getElementById('calendar'), { ... })`로 초기화해야 활성화됩니다.
- 드래그 & 드롭 이벤트의 경우, `FullCalendar.Draggable` 플러그인을 `#external-events` 요소에 바인딩하여 활성화시킵니다.
