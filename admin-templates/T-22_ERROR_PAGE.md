# [T-22] ERROR_PAGE

**용도**: 잘못된 라우트 접근(404), 서버 장애(500), 권한 부족(403) 발생 시 단독 뷰포트 영역에서 안내 메시지를 표시하는 전체 화면 전용 에러 화면입니다.
인증 템플릿(T-12)과 마찬가지로 헤더, 사이드바를 숨기고 페이지를 전체 영역으로 채웁니다.

### 1. Template Structure (Error Overlay)

에러 레이아웃은 수직/수평 중앙 정렬을 자동으로 생성하는 구조로 이루어집니다. `error` 래퍼는 다른 콘텐츠 간섭 없이 사용자 포커스를 하단의 돌아가기 버튼(Call to Action)으로 유도해야 합니다.

```html
<!-- [페이지 전체 Wrapper] -->
<div id="page-container" class="page-container">
    
    <!-- ============================================
         1. Error Container (중앙 배치)
         ============================================ -->
    <div class="error">
        
        <!-- 1-1. Error Code (거대 텍스트) -->
        <div class="error-code">404</div>
        
        <!-- 1-2. Error Content (안내 문구) -->
        <div class="error-content">
            <!-- 상태를 설명하는 제목 -->
            <div class="error-message">We couldn't find it...</div>
            <!-- 세부 사유 및 조치 안내 -->
            <div class="error-desc mb-4">
                오류가 발생했습니다. 요청하신 페이지를 찾을 수 없습니다. <br />
                직접 URL을 입력하셨다면 스펠링을 다시 확인해 주십시오.<br />
            </div>
            <!-- 복구 액션 (뒤로가기 또는 홈으로 이동) -->
            <div>
                <a href="/dashboard" class="btn btn-theme px-3">Go Home</a>
            </div>
        </div>
        
    </div> <!-- /.error -->
    
</div> <!-- /.page-container -->
```

### 2. Implementation Notes
- **동적 상태 주입**: Spring/Thymeleaf 또는 Next.js 등의 프레임워크와 결합될 경우, `error-code`에 담길 문자열(예: '500')과 `error-message` 값을 서버로부터 동적으로 바인딩(Binding)하십시오.
- 해당 페이지만의 특징으로, 이전에 세션이나 라우터상 진입했던 히스토리를 `window.history.back()` 스크립트를 통해 `Go Back` 버튼을 구현하는 패턴도 자주 쓰입니다.
