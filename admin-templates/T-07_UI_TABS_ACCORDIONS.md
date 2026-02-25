# [T-07] UI_TABS_ACCORDIONS

**용도**: 설정 페이지나 복잡한 통계 화면에서, 하나의 화면(Panel) 안에 여러 영역의 데이터를 탭으로 분리하거나 아코디언으로 접었다 폈다 할 때 쓰이는 표준입니다.
화면 공간을 절약하고 정보의 위계(Depth)성을 가져갑니다.

### 1. Nav Tabs (탭 인터페이스)
> **Reference**: [https://seantheme.com/color-admin/admin/html/ui_tabs_accordions.html](https://seantheme.com/color-admin/admin/html/ui_tabs_accordions.html)

Panel 내부에서 상단 `nav-tabs`를 구성하고 하단 `tab-content`에 내용물을 묶어 그립니다.

```html
<!-- Nav Tabs 영역 -->
<ul class="nav nav-tabs">
  <!-- 활성화 된 기본 탭 -->
  <li class="nav-item">
    <a href="#default-tab-1" data-bs-toggle="tab" class="nav-link active">
      <span class="d-sm-none">일반</span>
      <span class="d-sm-block d-none"><i class="fa fa-cogs fa-fw"></i> 일반 설정</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="#default-tab-2" data-bs-toggle="tab" class="nav-link">
      <span class="d-sm-none">보안</span>
      <span class="d-sm-block d-none"><i class="fa fa-shield-alt fa-fw"></i> 보안 및 권한</span>
    </a>
  </li>
  <li class="nav-item">
    <a href="#default-tab-3" data-bs-toggle="tab" class="nav-link">
      <span class="d-sm-none">알림</span>
      <span class="d-sm-block d-none"><i class="fa fa-envelope fa-fw"></i> 알림 환경</span>
    </a>
  </li>
</ul>

<!-- Tab Contents 영역 -->
<div class="tab-content panel rounded-0 p-3 m-0">
  
  <!-- 첫 번째 탭 본문 -->
  <div class="tab-pane fade active show" id="default-tab-1">
    <h3 class="m-t-10"><i class="fa fa-cog"></i> 일반 설정 내역입니다</h3>
    <p>
      시스템 이름 변경, 시간대 설정 등 전역 환경에 영향을 미치는 내용이 들어갑니다.
    </p>
  </div>
  
  <!-- 두 번째 탭 본문 -->
  <div class="tab-pane fade" id="default-tab-2">
    <blockquote>
      <p>비밀번호 초기화 주기, IP 접속 제한 등의 컴포넌트 추가 영역</p>
    </blockquote>
  </div>

  <!-- 세 번째 탭 본문 -->
  <div class="tab-pane fade" id="default-tab-3">
    <table class="table">
       <!-- 기타 테이블 삽입 가능 -->
    </table>
  </div>
</div>
```

### 2. Accordion (접이식 아코디언)
자주 묻는 질문(FAQ)이나 안내사항, 깊이가 깊은 서브 메뉴 트리를 설명할 때 유용합니다.

```html
<div class="accordion" id="accordionExample">

  <!-- ===============================
       첫 번째 드롭다운 패널
       =============================== -->
  <div class="accordion-item bg-inverse border-0 mb-2 rounded">
    <h2 class="accordion-header" id="headingOne">
      <!-- accordion-button 컨트롤 -->
      <button class="accordion-button bg-inverse text-white rounded" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
        <strong>관리자 권한 추가 방법이 무엇인가요?</strong>
      </button>
    </h2>
    
    <!-- 본문 컨테이너 -->
    <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
      <div class="accordion-body text-white">
        '사용자 관리 > 상세 조회' 메뉴 진입 후 하단의 '권한 그룹' Select Box에서 'Super Admin'을 선택하여 저장하면 됩니다.
      </div>
    </div>
  </div>

  <!-- ===============================
       두 번째 드롭다운 패널
       =============================== -->
  <div class="accordion-item bg-inverse border-0 mb-2 rounded">
    <h2 class="accordion-header" id="headingTwo">
      <button class="accordion-button bg-inverse text-white rounded collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo">
        <strong>서버 재부팅 주기는 얼마인가요?</strong>
      </button>
    </h2>
    <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
      <div class="accordion-body text-white">
        매월 2주차 일요일 새벽 시간대에 무중단 배포 및 자동 재부팅 패치가 진행됩니다.
      </div>
    </div>
  </div>

</div>
```
