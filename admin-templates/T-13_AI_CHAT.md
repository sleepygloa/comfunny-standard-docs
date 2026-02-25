# [T-13] AI_CHAT

**용도**: ChatGPT나 Copilot처럼 화면 전면을 사용하는 대화형 AI 인터페이스(Chat Application)입니다.
일반적인 폼 입력과 다르게 하단의 프롬프트 입력창 패널, 중앙의 대화 내역(Scrollable) 패널, 우측 보조 사이드바로 구성됩니다.

### 1. Template Structure (AI Chat)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/ai_chat.html](https://seantheme.com/color-admin/admin/html/ai_chat.html)

이 레이아웃은 페이지 스크롤을 제한하고 뷰포트 높이(100vh) 안에서 각 패널이 내부 스크롤을 갖도록 제어하는 것이 특징입니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div class="pos pos-with-sidebar" id="pos">
  
  <!-- ============================================
       1. Left Area: AI 챗봇 대화방 영역
       ============================================ -->
  <div class="pos-content">
    
    <!-- 1-1. Chat Header (현재 세션 정보) -->
    <div class="pos-content-header" style="height: 60px;">
       <h5 class="mb-0 text-white">
          <i class="fa fa-robot text-theme me-2"></i> COMFUNNY AI Assistant
       </h5>
       <div class="ms-auto flex-1 text-end">
          <a href="#" class="btn btn-sm btn-outline-theme"><i class="fa fa-download me-1"></i> Export Chat</a>
       </div>
    </div>
    
    <!-- 1-2. Chat Body (실제 대화 리스트 - Scrollable) -->
    <div class="pos-content-body p-0" id="chat-body">
      <div data-scrollbar="true" data-height="100%" class="p-4">
        
        <!-- Welcome Message (AI) -->
        <div class="d-flex align-items-start mb-4">
          <div class="bg-dark bg-opacity-50 text-white p-3 rounded" style="max-width: 80%;">
             <p class="mb-0">
               안녕하세요! 저는 사내 데이터 분석을 돕는 AI 어시스턴트입니다.<br/>
               어떤 도움이 필요하신가요? 아래 예시처럼 질문해 보세요.
             </p>
             <div class="mt-2">
                <span class="badge bg-theme text-black cursor-pointer">"이번 달 매출 결산을 예약해 줘"</span>
                <span class="badge bg-theme text-black cursor-pointer">"새로운 사용자 등록해 줘"</span>
             </div>
          </div>
        </div>
        
        <!-- User Request (User) -->
        <div class="d-flex align-items-start mb-4 flex-row-reverse">
          <div class="bg-theme text-black p-3 rounded" style="max-width: 80%; text-align: right;">
             <p class="mb-0">
               내일 오전 10시 회의 준비를 위해 최근 고객 불만 건수를 요약해 줄래?
             </p>
             <div class="text-black-transparent-5 fs-11px mt-1">방금 전</div>
          </div>
        </div>

        <!-- AI Response (AI) -->
        <div class="d-flex align-items-start mb-4">
          <div class="bg-dark bg-opacity-50 text-white p-3 rounded" style="max-width: 80%;">
             <p class="mb-2">
               네, 최근 7일간 접수된 고객 불만 요약입니다.
             </p>
             <ul class="mb-0">
                <li><b>결제 오류:</b> 총 14건 발생 (모두 환불 처리 진행 중)</li>
                <li><b>네트워크 지연:</b> 서버 패치 후 4건 접수 (현재 정상화 완료)</li>
             </ul>
             <div class="text-white-transparent-5 fs-11px mt-1">AI가 작성함</div>
          </div>
        </div>
        
        <!-- Typing Indicator ... -->
        <div class="d-flex align-items-start mb-4" id="typing-indicator" style="display: none !important;">
          <div class="bg-dark bg-opacity-50 text-white p-2 px-3 rounded">
             <i class="fa fa-circle text-theme fs-8px fa-fade"></i>
             <i class="fa fa-circle text-theme fs-8px mx-1 fa-fade" style="animation-delay: 0.1s;"></i>
             <i class="fa fa-circle text-theme fs-8px fa-fade" style="animation-delay: 0.2s;"></i>
          </div>
        </div>
        
      </div>
    </div>
    
    <!-- 1-3. Chat Footer (프롬프트 입력창) -->
    <div class="pos-content-footer" style="min-height: 80px;">
       <div class="input-group">
          <!-- 어태치먼트 버튼 -->
          <button class="btn btn-outline-default"><i class="fa fa-paperclip"></i></button>
          
          <!-- 자동 확장이 들어가는 Textarea 권장 -->
          <textarea class="form-control" rows="1" placeholder="AI에게 질문 내용을 입력하세요 (Enter 입력 시 전송)..." style="resize: none;"></textarea>
          
          <!-- 전송 버튼 -->
          <button class="btn btn-theme"><i class="fa fa-paper-plane fa-lg"></i></button>
       </div>
       <div class="text-center mt-2 fs-12px text-white-transparent-3">
          AI 응답은 정확하지 않을 수 있습니다. 중요한 정보는 확인이 필요합니다.
       </div>
    </div>
  </div> <!-- /.pos-content -->

  <!-- ============================================
       2. Right Area: AI 설정/보조 사이드바
       ============================================ -->
  <!-- 모델 선택이나 프롬프트 환경을 제어하는 고정 패널 -->
  <div class="pos-sidebar" id="pos-sidebar">
    
    <div class="pos-sidebar-header">
      <div class="title">Chat Options</div>
    </div>
    
    <div class="pos-sidebar-body p-3" data-scrollbar="true" data-height="100%">
      
      <div class="mb-4">
         <label class="form-label fw-bold text-white">AI 모델</label>
         <select class="form-select bg-inverse text-white">
            <option>GPT-4o (권장)</option>
            <option>Claude 3.5 Sonnet</option>
            <option>Gemini 1.5 Pro</option>
         </select>
      </div>

      <div class="mb-4">
         <label class="form-label fw-bold text-white">대화 언어/스타일</label>
         <div class="form-check">
            <input class="form-check-input" type="radio" name="tone" id="tone1" checked>
            <label class="form-check-label" for="tone1">친절하고 전문적으로</label>
         </div>
         <div class="form-check">
            <input class="form-check-input" type="radio" name="tone" id="tone2">
            <label class="form-check-label" for="tone2">짧고 간결하게 요약</label>
         </div>
      </div>
      
      <div class="mb-4">
         <label class="form-label fw-bold text-white">최근 대화 내역 (History)</label>
         <ul class="list-group list-group-flush bg-transparent">
            <a href="#" class="list-group-item list-group-item-action bg-transparent text-white border-white border-opacity-25 px-0"><i class="fa fa-comment-alt text-theme me-2"></i> 결제 버그 리포트 (어제)</a>
            <a href="#" class="list-group-item list-group-item-action bg-transparent text-white border-white border-opacity-25 px-0"><i class="fa fa-comment-alt text-theme me-2"></i> 신규 프로모션 기획 (3일 전)</a>
         </ul>
      </div>

    </div>
    
  </div> <!-- /.pos-sidebar -->
</div> <!-- /.pos -->
```
