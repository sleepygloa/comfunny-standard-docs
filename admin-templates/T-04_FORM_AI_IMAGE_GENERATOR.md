# [T-04] FORM_AI_IMAGE_GENERATOR

**용도**: 프롬프트를 입력하여 AI 이미지를 생성하거나, 복잡한 파라미터를 설정하는 AI 특화 폼(Form) UI입니다.
단순 데이터 입력 폼(T-03)과 달리, 채팅창 스타일이나 생성 결과 갤러리와 결합된 특수 레이아웃을 사용합니다.

### 1. Template Structure (AI Image Generator)
> **Reference Component**: [https://seantheme.com/color-admin/admin/html/ai_image_generator.html](https://seantheme.com/color-admin/admin/html/ai_image_generator.html)

이 템플릿은 좌측의 **컨트롤러(파라미터 설정 폼)**와 우측의 **결과 갤러리/진행창(Result View)**을 3:9 (또는 4:8) 비율로 분리하는 것이 핵심입니다.

```html
<!-- [AI Feature Component 래퍼] -->
<div class="row align-items-stretch">
  
  <!-- ============================================
       1. Left Sidebar: 프롬프트 입력 및 설정 (col-md-4)
       ============================================ -->
  <div class="col-xl-4 col-lg-5">
    <div class="panel panel-inverse h-100 mb-0">
      <div class="panel-heading">
         <h4 class="panel-title">이미지 생성 파라미터</h4>
      </div>
      <div class="panel-body">
        <form action="/generate" method="POST">
           
           <!-- 프롬프트 텍스트 에어리어 -->
           <div class="mb-3">
             <label class="form-label text-white">프롬프트 (Prompt)</label>
             <textarea class="form-control bg-dark bg-opacity-25" rows="5" placeholder="생성할 이미지를 묘사해주세요..."></textarea>
           </div>
           
           <!-- 부정적 프롬프트 (옵션) -->
           <div class="mb-3">
             <label class="form-label text-white">네거티브 프롬프트 (Negative Prompt)</label>
             <textarea class="form-control bg-dark bg-opacity-25" rows="3" placeholder="제외할 요소를 묘사해주세요..."></textarea>
           </div>

           <!-- 비율 선택기 (Select) -->
           <div class="mb-3">
             <label class="form-label text-white">이미지 비율 (Aspect Ratio)</label>
             <select class="form-select bg-dark bg-opacity-25">
                <option value="1:1">1:1 (Square)</option>
                <option value="16:9">16:9 (Landscape)</option>
                <option value="9:16">9:16 (Portrait)</option>
             </select>
           </div>

           <!-- 슬라이더 컨트롤 (CFG Scale / Steps) -->
           <div class="mb-3">
             <label class="form-label text-white d-flex justify-content-between">
                <span>자유도 (CFG Scale)</span> 
                <span id="cfgValue">7.5</span>
             </label>
             <input type="range" class="form-range" min="1" max="20" step="0.5" id="cfgScale" value="7.5">
           </div>

           <!-- 생성 버튼 -->
           <div class="mt-4">
              <button type="submit" class="btn btn-theme d-block w-100"><i class="fa fa-magic me-2"></i> 생성하기 (Generate)</button>
           </div>

        </form>
      </div>
    </div>
  </div>

  <!-- ============================================
       2. Right Main View: 결과 렌더링 영역 (col-md-8)
       ============================================ -->
  <div class="col-xl-8 col-lg-7 d-flex">
    <div class="card w-100 bg-inverse border-0 text-white p-3 p-md-4">
      
      <!-- 생성 전 빈 상태 (Empty State) -->
      <div class="d-flex align-items-center justify-content-center h-100 flex-column text-muted">
         <i class="fa fa-image fa-5x mb-3 text-white-transparent-2"></i>
         <h5>이미지를 묘사하고 생성 버튼을 눌러주세요.</h5>
      </div>
      
      <!-- 진행 중 스피너 (Progress) - 숨김 상태 기본 -->
      <div class="d-none align-items-center justify-content-center h-100 flex-column">
         <div class="spinner-border text-theme" style="width: 3rem; height: 3rem;" role="status"></div>
         <p class="mt-3 text-white">AI가 이미지를 그리고 있습니다...</p>
      </div>

      <!-- 생성 완료 갤러리 (결과 출력) - 숨김 상태 기본 -->
      <div class="d-none row gx-2">
         <div class="col-6 mb-2">
            <a href="#" class="img-fluid rounded border border-white border-opacity-25"><img src="generated_image_1.jpg" class="w-100 rounded" /></a>
         </div>
         <div class="col-6 mb-2">
            <a href="#" class="img-fluid rounded border border-white border-opacity-25"><img src="generated_image_2.jpg" class="w-100 rounded" /></a>
         </div>
      </div>

    </div>
  </div>
  
</div>
```
