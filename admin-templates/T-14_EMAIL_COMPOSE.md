# [T-14] EMAIL_COMPOSE

**용도**: 신규 메일/쪽지를 작성할 때 사용하는 이메일 작성(Compose) 뷰입니다.
T-05_EMAIL_INBOX.md와 패밀리 디자인으로 묶이며, 동일한 좌측 사이드바 구조를 재사용하고 우측 콘텐츠 영역에 작성 폼을 배치합니다.

### 1. Template Structure (Email Compose)

이 레이아웃은 왼쪽에 메일함 사이드바(`.mailbox-sidebar`), 오른쪽에 작성 폼(`.mailbox-content`)이 수평 분할된 형태입니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div class="mailbox">
    <!-- ============================================
         1. Left Area: Mailbox Sidebar (인박스와 동일)
         ============================================ -->
    <div class="mailbox-sidebar">
        <div class="mailbox-sidebar-header d-flex justify-content-center">
            <a href="#email-compose" data-bs-toggle="collapse" class="btn btn-inverse btn-sm w-100">
                <i class="fa fa-edit me-1"></i> Compose
            </a>
        </div>
        <div class="mailbox-sidebar-content collapse d-md-block" id="email-compose">
            <!-- Mail Folders -->
            <div data-scrollbar="true" data-height="100%" data-skip-mobile="true">
                <div class="nav-title"><b>FOLDERS</b></div>
                <ul class="nav nav-inbox">
                    <li><a href="#"><i class="fa fa-hdd fa-lg fa-fw me-2"></i> Inbox <span class="badge bg-gray-600 fs-10px rounded-pill ms-auto fw-bolder pt-4px pb-5px px-8px">52</span></a></li>
                    <li><a href="#"><i class="fa fa-flag fa-lg fa-fw me-2"></i> Important</a></li>
                    <li><a href="#"><i class="fa fa-envelope fa-lg fa-fw me-2"></i> Sent</a></li>
                    <li class="active"><a href="#"><i class="fa fa-save fa-lg fa-fw me-2"></i> Drafts</a></li>
                    <li><a href="#"><i class="fa fa-trash-alt fa-lg fa-fw me-2"></i> Trash</a></li>
                </ul>
                <div class="nav-title mt-4"><b>LABEL</b></div>
                <ul class="nav nav-inbox">
                    <li><a href="#"><i class="fa fa-fw fa-lg fa-circle text-dark me-2"></i> Admin</a></li>
                    <li><a href="#"><i class="fa fa-fw fa-lg fa-circle text-primary me-2"></i> Designer &amp; Employer</a></li>
                    <li><a href="#"><i class="fa fa-fw fa-lg fa-circle text-success me-2"></i> Staff</a></li>
                    <li><a href="#"><i class="fa fa-fw fa-lg fa-circle text-warning me-2"></i> Sponsorer</a></li>
                    <li><a href="#"><i class="fa fa-fw fa-lg fa-circle text-danger me-2"></i> Client</a></li>
                </ul>
            </div>
        </div>
    </div>
    
    <!-- ============================================
         2. Right Area: Mailbox Content (작성 폼)
         ============================================ -->
    <div class="mailbox-content">
        <!-- 메일 작성 툴바 -->
        <div class="mailbox-content-header">
            <div class="btn-toolbar">
                <div class="btn-group me-2">
                    <button class="btn btn-white btn-sm"><i class="fa fa-save mt-1 mb-1"></i> <span class="d-none d-lg-inline">Save</span></button>
                    <button class="btn btn-white btn-sm"><i class="fa fa-trash mt-1 mb-1"></i> <span class="d-none d-lg-inline">Discard</span></button>
                </div>
                <div class="btn-group">
                    <button class="btn btn-white btn-sm px-3 border-end-0">
                        <i class="fa fa-paperclip mt-1 mb-1"></i> <span class="d-none d-lg-inline">Attach</span>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- 이메일 입력 영역 -->
        <div class="mailbox-content-body">
            <div data-scrollbar="true" data-height="100%" data-skip-mobile="true">
                <form action="/" method="POST" name="email_to_form" class="mailbox-form">
                    <!-- 수신자 / CC / BCC -->
                    <div class="mailbox-to">
                        <label class="control-label">To:</label>
                        <ul id="email-to" class="primary line-mode">
                            <li>bootstrap@gmail.com</li>
                        </ul>
                        <div class="mailbox-float-link">
                            <a href="#" data-email-action="cc"><i class="fa fa-plus me-1"></i> Cc</a>
                            <a href="#" data-email-action="bcc"><i class="fa fa-plus me-1"></i> Bcc</a>
                        </div>
                    </div>
                    <!-- CC 입력 (초기 숨김) -->
                    <div class="mailbox-to d-none text-inverse" data-email-target="cc">
                        <label class="control-label">Cc:</label>
                        <input type="text" class="form-control" />
                    </div>
                    <!-- BCC 입력 (초기 숨김) -->
                    <div class="mailbox-to d-none text-inverse" data-email-target="bcc">
                        <label class="control-label">Bcc:</label>
                        <input type="text" class="form-control" />
                    </div>
                    
                    <!-- 제목 -->
                    <div class="mailbox-to">
                        <label class="control-label">Subject:</label>
                        <input type="text" class="form-control" placeholder="Email Subject" />
                    </div>
                    
                    <!-- 에디터 영역 (Wysiwyg/Summernote 등) -->
                    <div class="mailbox-input text-gray-800">
                        <textarea class="summernote" name="content"></textarea>
                    </div>
                </form>
            </div>
        </div>
        
        <!-- 하단 전송 버튼 역역 -->
        <div class="mailbox-content-footer d-flex align-items-center justify-content-end">
            <button type="button" class="btn btn-white btn-sm me-2">Discard</button>
            <button type="submit" class="btn btn-primary btn-sm">Send <i class="fa fa-paper-plane ms-1"></i></button>
        </div>
    </div>
</div>
```

### 2. Implementation Notes
1. **Third-Party Integrations**:
   - 수신자(To/Cc/Bcc) 입력 영역은 주로 `Tag-It` 플러그인이나 `Select2` 라이브러리를 바인딩하여 복수 선택이 가능하게 구성합니다.
   - 메일 본문 작성 공간(`<textarea class="summernote">`)은 보통 `Summernote` 리치 텍스트 에디터 플러그인을 사용하여 초기화합니다.
2. `.mailbox` 래퍼는 T-05_EMAIL_INBOX.md의 래퍼 클래스와 일치시키므로 두 뷰간 트랜지션이 부드럽게 유지됩니다.
