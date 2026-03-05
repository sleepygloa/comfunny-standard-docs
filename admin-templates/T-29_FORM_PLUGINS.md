# [T-29] FORM_PLUGINS

**용도**: 기본 내장 `<input>` 요소를 넘어서, Datepicker, Select2(다중 선택), Colorpicker, Switchery(토글 스위치) 등 고급 폼 입력 요소가 필요할 때 사용하는 플러그인 랩퍼 템플릿입니다.

### 1. Template Structure (Advanced Form Controls)

부트스트랩의 기본 폼 마크업(`.form-control`)에 플러그인 특화된 클래스와 `data-` 속성을 부여하여 스크립트 단에서 콤포넌트를 활성화하는 구조입니다.

```html
<form class="form-horizontal">
    <!-- ============================================
         1. Select2 (검색 가능한 셀렉트박스 & 다중 선택)
         ============================================ -->
    <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">검색형 셀렉트박스</label>
        <div class="col-md-9">
            <!-- default-select2 클래스는 js에서 바인딩 식별자로 사용 -->
            <select class="default-select2 form-control">
                <optgroup label="Alaskan/Hawaiian Time Zone">
                    <option value="AK">Alaska</option>
                    <option value="HI">Hawaii</option>
                </optgroup>
                <optgroup label="Pacific Time Zone">
                    <option value="CA">California</option>
                    <option value="NV">Nevada</option>
                    <option value="OR">Oregon</option>
                </optgroup>
            </select>
            <div class="mt-2 text-gray-500 fs-12px">Select2 플러그인을 사용하여 수많은 옵션 중 텍스트로 검색할 수 있습니다.</div>
        </div>
    </div>
    
    <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">다중 선택 (Multiple)</label>
        <div class="col-md-9">
            <!-- multiple-select2 클래스와 태그 속성 사용 -->
            <select class="multiple-select2 form-control" multiple="multiple">
                <option value="red" selected>Red</option>
                <option value="blue" selected>Blue</option>
                <option value="green">Green</option>
            </select>
        </div>
    </div>

    <!-- ============================================
         2. Datepicker & Date Range
         ============================================ -->
    <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">단일 날짜 선택</label>
        <div class="col-md-9">
            <div class="input-group" id="default-daterange">
                <input type="text" class="form-control" name="default-date" id="datepicker-default" placeholder="Select Date" value="2026-10-15" />
                <span class="input-group-text"><i class="fa fa-calendar"></i></span>
            </div>
        </div>
    </div>
    
    <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">날짜 범위 선택 (Date Range)</label>
        <div class="col-md-9">
            <div class="input-group" id="advance-daterange">
                <input type="text" name="start" class="form-control" placeholder="Start Date" />
                <span class="input-group-text">to</span>
                <input type="text" name="end" class="form-control" placeholder="End Date" />
            </div>
        </div>
    </div>

    <!-- ============================================
         3. UI Switchery & Sliders
         ============================================ -->
    <div class="row mb-15px">
        <label class="form-label col-form-label col-md-3">iOS 스타일 스위치</label>
        <div class="col-md-9 pt-2">
            <!-- checkbox 클래스에 data-render="switchery" 적용 -->
            <input type="checkbox" data-render="switchery" data-theme="default" checked />
            <span class="ms-3 text-muted">기본 테마</span>
            
            <input type="checkbox" data-render="switchery" data-theme="blue" checked />
            <span class="ms-3 text-muted">블루 테마</span>
        </div>
    </div>
</form>
```

### 2. Implementation Notes
- **Javascript Initialization**: `Select2`나 `Switchery`, `Datepicker` 등은 HTML 태그만 넣는다고 바로 동작하지 않습니다. 반드시 페이지 하단이나 공통 JS 뷰 로더에서 `$('.default-select2').select2();` 등의 호출을 수행해야 합니다.
- 시스템 관리 페이지에서는 단순 체크박스(`checkbox`)보다는 시안성이 우수한 스위치 기반의 UI(`data-render="switchery"`)나 부트스트랩 스위치(`form-switch`)를 선호합니다.
