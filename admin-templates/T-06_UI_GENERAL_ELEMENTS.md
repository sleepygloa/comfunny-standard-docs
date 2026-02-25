# [T-06] UI_GENERAL_ELEMENTS

**용도**: 데이터를 시각적으로 분리하기 위한 기본 컴포넌트인 부트스트랩 Card, Alert, Progress Bar, Badge 등의 템플릿입니다. Panel 외의 서브 요소로 자주 활용됩니다.

### 1. Alert & Notifications (경고/알림)
> **Reference**: [https://seantheme.com/color-admin/admin/html/ui_general.html](https://seantheme.com/color-admin/admin/html/ui_general.html)

어드민 페이지 상단이나 폼 내부에서 에러/성공 메시지를 띄울 때 사용합니다.

```html
<!-- 성공 알림 (초록색) -->
<div class="alert alert-success alert-dismissible fade show mb-0">
  <strong>Success!</strong> 회원 정보가 성공적으로 수정되었습니다.
  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>

<!-- 에러 알림 (빨간색) -->
<div class="alert alert-danger alert-dismissible fade show mb-0">
  <strong>Error!</strong> 데이터베이스 연결에 실패했습니다. 관리자에게 문의하세요.
  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>

<!-- 주의 알림 (노란색) -->
<div class="alert alert-warning alert-dismissible fade show">
  <strong>Warning!</strong> 아직 인증을 완료하지 않은 사용자입니다.
</div>
```

### 2. Cards (서브 콘텐츠 카드)
기본 `Panel` 내부에서 영역을 한번 더 쪼개거나, 여러 통계를 바둑판처럼 배치할 때 사용합니다.

```html
<div class="card border-0 mb-3 bg-dark text-white text-center">
  <div class="card-body">
    <div class="mb-3 text-white-transparent-5">
      <i class="fa fa-users fa-3x"></i>
    </div>
    <h5 class="card-title">오늘 가입자 수</h5>
    <h3 class="text-white mb-0">1,245 명</h3>
  </div>
</div>
```

### 3. Progress Bars (진행률 상태 바)
기능 진행 상황이나 쿼터 사용량을 직관적으로 보여줍니다.

```html
<div class="mb-3">
  <div class="d-flex justify-content-between mb-1">
    <span>스토리지 사용량</span>
    <span class="text-success">75%</span>
  </div>
  <div class="progress rounded-pill" style="height: 10px;">
    <!-- bg-success, bg-danger, bg-warning 등으로 색상 분리 -->
    <div class="progress-bar bg-success progress-bar-striped progress-bar-animated" style="width: 75%"></div>
  </div>
</div>
```
