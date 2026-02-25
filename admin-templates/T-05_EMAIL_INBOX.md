# [T-05] EMAIL_INBOX

**용도**: 사용자 피드백 메일함, 시스템 알림함(Notification 결합), 사내 쪽지 기능 등 연락/소통 수단의 리스트와 본문 보기를 담당하는 템플릿입니다.

### 1. Template Structure (Email Inbox)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/email_inbox.html](https://seantheme.com/color-admin/admin/html/email_inbox.html)

일반 Data Table과 다르게 메일 리스트는 **좌측 폴더 네비게이션**과 **우측 메세지 리스트(또는 읽기 화면)**로 나뉘는 `mailbox` 클래스 구조를 가집니다.

```html
<!-- [Mailbox 래퍼] 패널(panel) 없이 전체를 컨테이너로 씁니다 -->
<div class="mailbox">
  
  <!-- ============================================
       1. Mailbox Sidebar (좌측 폴더 네비게이션)
       ============================================ -->
  <div class="mailbox-sidebar">
    <div class="mailbox-sidebar-header d-flex justify-content-center">
      <!-- 메일 쓰기 버튼 -->
      <a href="#compose" class="btn btn-inverse btn-sm w-100"><i class="fa fa-pen me-2"></i> 쪽지 쓰기</a>
    </div>
    <div class="mailbox-sidebar-content" data-scrollbar="true" data-height="100%">
      
      <!-- 고정 폴더 리스트 -->
      <div class="nav-title"><b>FOLDERS</b></div>
      <ul class="nav nav-inbox">
        <li class="active">
          <a href="#"><i class="fa fa-inbox fa-fw me-2"></i> 받은 편지함 <span class="badge bg-danger rounded-pill ms-auto">52</span></a>
        </li>
        <li><a href="#"><i class="fa fa-paper-plane fa-fw me-2"></i> 보낸 편지함</a></li>
        <li><a href="#"><i class="fa fa-pencil-alt fa-fw me-2"></i> 임시보관함</a></li>
        <li><a href="#"><i class="fa fa-trash fa-fw me-2"></i> 휴지통</a></li>
      </ul>
      
      <!-- 커스텀 라벨 리스트 (태그형) -->
      <div class="nav-title mt-4"><b>LABELS</b></div>
      <ul class="nav nav-inbox">
        <li><a href="#"><i class="fa fa-circle text-primary fa-fw me-2"></i> 시스템 오류</a></li>
        <li><a href="#"><i class="fa fa-circle text-warning fa-fw me-2"></i> 사용자 문의</a></li>
        <li><a href="#"><i class="fa fa-circle text-success fa-fw me-2"></i> 제휴사 연락</a></li>
      </ul>
    </div>
  </div>

  <!-- ============================================
       2. Mailbox Content (우측 메일 리스트 영역)
       ============================================ -->
  <div class="mailbox-content">
    
    <!-- 상단 툴바 (체크박스, 휴지통, 스팸 처리, 페이징 정보) -->
    <div class="mailbox-content-header d-flex align-items-center">
      <div class="btn-group me-2">
        <button class="btn btn-white btn-sm" data-email-action="select-all">
          <i class="fa fa-square fa-fw"></i>
        </button>
      </div>
      <div class="btn-group me-2">
        <button class="btn btn-white btn-sm" data-bs-toggle="tooltip" title="삭제"><i class="fa fa-trash fa-fw text-danger"></i></button>
        <button class="btn btn-white btn-sm" data-bs-toggle="tooltip" title="읽음 처리"><i class="fa fa-envelope-open fa-fw"></i></button>
      </div>
      
      <!-- 우측 페이징 수치 표기 -->
      <div class="ms-auto">
        <span class="text-inverse text-opacity-50 fs-12px me-3">1 - 50 of 1,200</span>
        <div class="btn-group">
          <button class="btn btn-white btn-sm"><i class="fa fa-chevron-left"></i></button>
          <button class="btn btn-white btn-sm"><i class="fa fa-chevron-right"></i></button>
        </div>
      </div>
    </div>
    
    <!-- 메일 리스트 본문 (리스트 그룹 형태) -->
    <div class="mailbox-content-body">
      <div data-scrollbar="true" data-height="100%">
        <ul class="list-group list-group-flush mailbox-list">
          
          <!-- An unread email item -->
          <li class="list-group-item d-flex align-items-center unread">
            <div class="mailbox-checkbox">
              <input class="form-check-input" type="checkbox">
            </div>
            <div class="mailbox-star">
              <i class="fa fa-star text-warning"></i> <!-- 중요 표시 활성화 됨 -->
            </div>
            <div class="mailbox-sender" style="width: 150px;">
              <span class="text-truncate d-block">Apple Support</span>
            </div>
            <div class="mailbox-message flex-1">
              <a href="#email-detail" class="text-dark text-decoration-none">
                 <span class="mailbox-title fw-bold">당신의 계정이 잠금 처리되었습니다.</span>
                 <span class="mailbox-desc text-muted ms-2 d-none d-md-inline">보안 관련 업데이트를 위해 로그인 내역을 확인해주세요...</span>
              </a>
            </div>
            <div class="mailbox-time text-muted fs-12px" style="width: 80px; text-align: right;">
              10:14 AM
            </div>
          </li>
          
          <!-- A read email item -->
          <li class="list-group-item d-flex align-items-center">
             <div class="mailbox-checkbox">
                <input class="form-check-input" type="checkbox" />
             </div>
             <div class="mailbox-star">
                <i class="fa fa-star text-muted"></i>
             </div>
             <div class="mailbox-sender" style="width: 150px;">
                <span class="text-truncate d-block">Twitter</span>
             </div>
             <div class="mailbox-message flex-1">
                <a href="#email-detail" class="text-dark text-decoration-none">
                   <span class="mailbox-title fw-semibold">새로운 팔로워 안내</span>
                </a>
             </div>
             <div class="mailbox-time text-muted fs-12px" style="width: 80px; text-align: right;">
                Oct 10
             </div>
          </li>
          
        </ul>
      </div>
    </div>
  </div> <!-- /mailbox-content -->

</div> <!-- /mailbox -->
```
