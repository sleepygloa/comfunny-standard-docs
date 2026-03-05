# [T-31] FORM_DROPZONE

**용도**: 첨부파일, 상품 갤러리 이미지 모음, 다중 문서 업로드 등 사용자가 파일을 화면에 직접 끌어다 놓기(Drag & Drop)를 지원하는 다중(Multi) 파일 업로더 템플릿입니다.

### 1. Template Structure (Dropzone Uploader)

일반적인 폼 입력 전송 방식이 아니라, Dropzone 플러그인을 사용하여 `form` 태그 자체가 거대한 드래그 앤 드롭 영역이 되도록 구현합니다.

```html
<div class="panel panel-inverse">
    <div class="panel-heading">
        <h4 class="panel-title">Dropzone File Upload</h4>
        <div class="panel-heading-btn">
            <a href="javascript:;" class="btn btn-xs btn-icon btn-default" data-toggle="panel-expand"><i class="fa fa-expand"></i></a>
        </div>
    </div>
    <div class="panel-body">
        
        <!-- ============================================
             1. Dropzone Form Area 
             ============================================ -->
        <!-- dropzone 클래스를 포함하면 폼 영역 전체가 드래그 패널로 활성화됨 -->
        <form action="/api/upload/files" class="dropzone" id="myDropzone">
            
            <!--Fallback input for older browsers-->
            <div class="fallback">
                <input name="file" type="file" multiple />
            </div>
            
            <!-- Default Message Container (가운데 정렬) -->
            <div class="dz-message needsclick">
                <i class="fa fa-cloud-upload-alt text-gray-500 fa-4x mb-3"></i>
                <br />
                <span class="fs-18px fw-bold text-dark">
                    Drop files here or click to upload.
                </span><br />
                <span class="fs-12px text-muted">
                    (JPG, PNG, GIF, PDF / 최대 10MB)
                </span>
            </div>
            
        </form>
        
    </div>
    
    <!-- 옵션: 별도의 확인 버튼(수동 업로드 시뮬레이션용) -->
    <div class="panel-footer bg-transparent text-end">
        <button type="button" class="btn btn-primary" id="btn-upload-trigger">Submit All Files</button>
    </div>
</div>
```

### 2. Implementation Notes
- `form` 태그에 부여된 `class="dropzone"`은 Dropzone.js 라이브러리에 의해 자동 스캔되어, 시각적인 대시보드 인터페이스로 치환됩니다.
- Dropzone은 기본적으로 파일이 드롭박스에 놓이자마자 바로 `action` 속성에 지정된 경로(`POST /api/upload/files`)로 비동기 Ajax 업로드를 수행하는 AutoProcess 동작을 합니다. 여러 폼 데이터를 함께 저장해야 하는 경우 스크립트 단의 속성 변경(`autoProcessQueue: false`) 처리가 요구됩니다.
- 서버 측에서는 `Multipart` 형태의 개별 파일 단위를 받을 수 있는 Endpoint를 준비해야 합니다.
