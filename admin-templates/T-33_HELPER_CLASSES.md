# [T-33] HELPER_CLASSES

**용도**: UI 요소에 반복적으로 적용되는 유틸리티 CSS 클래스(마진, 패딩, 폰트, 색상)의 표준화된 목록 및 사용법을 개발자/기획자에게 명시하는 가이드 템플릿입니다. 어드민 페이지 개발 속도를 높이기 위해 별도의 `<style>` 작성 없이 제공된 클래스를 재사용하도록 통제해야 합니다.

### 1. Template Context (Helper CSS)

이 템플릿은 HTML 뷰 코드가 아니라 **퍼블리싱 원칙**을 서술한 컴포넌트에 가깝습니다. Color Admin v3(Bootstrap 5) 표준 유틸리티 클래스 활용법을 요약 서술합니다.

```html
<div class="panel panel-inverse">
    <div class="panel-heading">
        <h4 class="panel-title">Helper CSS Classes</h4>
    </div>
    <div class="panel-body">
        
        <!-- ============================================
             1. Text Colors (텍스트 색상)
             ============================================ -->
        <h5 class="mb-3">1. Text Color Utilities</h5>
        <div class="row mb-5">
            <div class="col-md-12">
                <code>.text-theme</code> <span class="text-theme fw-bold">Theme Color (Primary)</span><br>
                <code>.text-blue</code> <span class="text-blue fw-bold">Blue Color</span><br>
                <code>.text-teal</code> <span class="text-teal fw-bold">Teal Color</span><br>
                <code>.text-cyan</code> <span class="text-cyan fw-bold">Cyan Color</span><br>
                <code>.text-orange</code> <span class="text-orange fw-bold">Orange Color</span><br>
                <code>.text-dark</code> <span class="text-dark fw-bold">Dark (Black)</span><br>
                <code>.text-gray-500</code> <span class="text-gray-500 fw-bold">Gray Medium</span><br>
                <code>.text-white-transparent-5</code> <span class="bg-dark p-1 text-white-transparent-5">White 50% Opacity</span>
            </div>
        </div>

        <!-- ============================================
             2. Background Colors (배경 색상)
             ============================================ -->
        <h5 class="mb-3">2. Background Color Utilities</h5>
        <div class="row mb-5">
            <div class="col-md-12">
                <div class="d-inline-block p-2 me-2 mb-2 bg-theme text-black">.bg-theme</div>
                <div class="d-inline-block p-2 me-2 mb-2 bg-blue text-white">.bg-blue</div>
                <div class="d-inline-block p-2 me-2 mb-2 bg-indigo text-white">.bg-indigo</div>
                <div class="d-inline-block p-2 me-2 mb-2 bg-gray-200 text-dark">.bg-gray-200</div>
                <div class="d-inline-block p-2 me-2 mb-2 bg-gray-900 text-white">.bg-gray-900</div>
            </div>
        </div>

        <!-- ============================================
             3. Padding & Margin (여백) - Bootstrap 5 Style
             ============================================ -->
        <h5 class="mb-3">3. Spacing (여백 유틸리티)</h5>
        <p class="mb-3 fs-13px text-muted">
            `m(margin)` / `p(padding)` + `t(top) / b(bottom) / s(start=left) / e(end=right) / x(left-right) / y(top-bottom)` + `-(0~5 또는 px단위)`
        </p>
        <div class="row mb-5">
            <div class="col-md-6">
                <h6>Margin</h6>
                <code>.m-0</code> (Margin 0)<br>
                <code>.m-auto</code> (Margin Auto)<br>
                <code>.mb-3</code> (Margin Bottom ~1rem)<br>
                <code>.mt-15px</code> (Margin Top 15px)<br>
                <code>.mx-2</code> (Margin Left/Right)<br>
            </div>
            <div class="col-md-6">
                <h6>Padding</h6>
                <code>.p-0</code> (Padding 0)<br>
                <code>.p-4</code> (Padding ~1.5rem)<br>
                <code>.ps-3</code> (Padding Start/Left)<br>
                <code>.pe-3</code> (Padding End/Right)<br>
                <code>.py-20px</code> (Padding Top/Bottom 20px)<br>
            </div>
        </div>
        
        <!-- ============================================
             4. Font Size & Weight (글꼴)
             ============================================ -->
        <h5 class="mb-3">4. Typography</h5>
        <div class="row mb-5">
            <div class="col-md-6">
                <h6>Sizes</h6>
                <code>.fs-10px</code> <span class="fs-10px">Very Small text</span><br>
                <code>.fs-12px</code> <span class="fs-12px">Small text (standard UI desc)</span><br>
                <code>.fs-14px</code> <span class="fs-14px">Normal text</span><br>
                <code>.fs-16px</code> <span class="fs-16px">Large text</span><br>
                <code>.fs-20px</code> <span class="fs-20px">Title text</span><br>
            </div>
            <div class="col-md-6">
                <h6>Weights</h6>
                <code>.fw-bold</code> <span class="fw-bold">Bold Text (700)</span><br>
                <code>.fw-bolder</code> <span class="fw-bolder">Bolder Text (800)</span><br>
                <code>.fw-normal</code> <span class="fw-normal">Normal Text (400)</span><br>
                <code>.fw-light</code> <span class="fw-light">Light Text (300)</span><br>
            </div>
        </div>
        
        <!-- ============================================
             5. Border & Radius (외곽선 및 둥글기)
             ============================================ -->
        <h5 class="mb-3">5. Border Utilities</h5>
        <div class="row">
            <div class="col-md-6">
                <code>.border</code>, <code>.border-0</code> (All borders)<br>
                <code>.border-top</code>, <code>.border-bottom</code><br>
                <code>.border-theme</code> (Border Color)<br>
                <code>.border-gray-500</code><br>
            </div>
            <div class="col-md-6">
                <code>.rounded</code>, <code>.rounded-0</code><br>
                <code>.rounded-pill</code> (알약 형태)<br>
                <code>.rounded-circle</code> (원형 형태, 아바타용)<br>
            </div>
        </div>
        
    </div>
</div>
```

### 2. Implementation Notes
- **Inline Style 남용 금지**: 새로운 요소를 디자인할 때 `style="margin-top: 15px;"` 식으로 HTML 내 인라인 스타일을 박아넣는 행위(Hard-coding)는 지양해야 합니다. 반드시 만들어져 있는 위 유틸리티 클래스(`.mt-15px`)를 사용하십시오.
- **반응형(Responsive) 접두사**: 특정 화면 크기에서만 작동하는 마진/패딩을 원하면 `d-none d-md-block`(태블릿 이상 표시) 혹은 `mb-sm-3` 과 같이 `-sm`, `-md`, `-lg`, `-xl` 접두사를 끼워넣어 사용합니다.
