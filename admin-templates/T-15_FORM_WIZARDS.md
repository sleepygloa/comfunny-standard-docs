# [T-15] FORM_WIZARDS

**용도**: 회원가입, 결제 단계, 다단계 데이터 수집 등 사용자가 순차적으로 정보를 입력해야 할 때 사용하는 스텝 바이 스텝 위저드(Wizard) 폼 템플릿입니다.

### 1. Template Structure (Form Wizard)

```html
<div class="panel panel-inverse">
    <div class="panel-heading">
        <h4 class="panel-title">Form Wizard</h4>
        <div class="panel-heading-btn">
            <a href="javascript:;" class="btn btn-xs btn-icon btn-default" data-toggle="panel-expand"><i class="fa fa-expand"></i></a>
        </div>
    </div>
    <div class="panel-body">
        <form action="/" method="POST" name="form-wizard" class="form-control-with-bg">
            <!-- 1. Wizard Header (진행 상태 바) -->
            <div id="wizard">
                <ol>
                    <li>
                        Personal Info 
                        <small>Name, Email, Phone</small>
                    </li>
                    <li>
                        Company Profile 
                        <small>Mailing Address, Business Type</small>
                    </li>
                    <li>
                        Completed 
                        <small>Review &Submit</small>
                    </li>
                </ol>
                
                <!-- 2. Wizard Content (스텝별 입력 폼) -->
                <!-- Step 1 -->
                <div>
                    <fieldset>
                        <legend class="mb-3">Personal Information</legend>
                        <div class="row mb-3">
                            <label class="col-form-label col-md-3">First Name *</label>
                            <div class="col-md-9">
                                <input type="text" name="firstname" class="form-control" placeholder="John" required />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <label class="col-form-label col-md-3">Last Name *</label>
                            <div class="col-md-9">
                                <input type="text" name="lastname" class="form-control" placeholder="Doe" required />
                            </div>
                        </div>
                    </fieldset>
                </div>
                <!-- Step 2 -->
                <div>
                    <fieldset>
                        <legend class="mb-3">Company Information</legend>
                        <div class="row mb-3">
                            <label class="col-form-label col-md-3">Company Name</label>
                            <div class="col-md-9">
                                <input type="text" name="company" class="form-control" placeholder="Company Inc." />
                            </div>
                        </div>
                    </fieldset>
                </div>
                <!-- Step 3 -->
                <div>
                    <div class="jumbotron m-b-0 text-center">
                        <h2 class="display-4">Thank You!</h2>
                        <p class="lead">모든 단계 입력을 마쳤습니다. 제출 버튼을 눌러 완료하십시오.</p>
                        <p><a href="javascript:;" class="btn btn-primary btn-lg">Submit Form</a></p>
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>
```

### 2. Implementation Notes
1. **Third-Party Integrations**:
   - T-15는 `smartwizard` jQuery 플러그인과 연동되는 것을 목적으로 합니다.
   - `$('#wizard').smartWizard();` 스크립트를 페이지 하단에 초기화하여 사용하여 단계별 탭의 전환 및 유효성 검사 로직을 함께 구현합니다.
2. 각 스텝 내부의 입력 요소 배치는 `T-03_FORM_INPUTS.md`의 규칙을 따르는 것이 좋습니다.
