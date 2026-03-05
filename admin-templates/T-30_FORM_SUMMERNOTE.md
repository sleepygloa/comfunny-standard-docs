# [T-30] FORM_SUMMERNOTE

**용도**: 공지사항, 이메일 에디터, 게시판 본문 등 사용자가 HTML 형식의 위지윅(WYSIWYG) 스타일로 볼드, 색상, 이미지 첨부 등을 자유롭게 조작할 수 있는 리치 텍스트 에디터 컨테이너입니다.

### 1. Template Structure (Summernote WYSIWYG Editor)

기본적으로 `textarea` 폼 태그에 에디터용 클래스(ex: `.summernote`)를 부여하고 자바스크립트로 인터페이스를 치환하는 방식입니다.

```html
<form action="/" name="wysiwyg_form" method="POST">
    <div class="panel panel-inverse">
        <div class="panel-heading">
            <h4 class="panel-title">Summernote Rich Text Editor</h4>
            <div class="panel-heading-btn">
                <a href="javascript:;" class="btn btn-xs btn-icon btn-default" data-toggle="panel-expand"><i class="fa fa-expand"></i></a>
            </div>
        </div>
        <div class="panel-body p-0">
            <!-- 
            * 에디터가 적용될 컨테이너. 보통 textarea 사용.
            * form submit 시 name="content"로 전송됨.
            -->
            <textarea class="summernote" name="content">
                &lt;h1&gt;Welcome to Summernote!&lt;/h1&gt;
                &lt;p&gt;
                    이곳은 초기화 시 제공되는 기본 컨텐츠 영역입니다. 
                    &lt;b&gt;가장 많이 사용되는 위지윅 에디터&lt;/b&gt; 플러그인 중 하나입니다.
                &lt;/p&gt;
            </textarea>
        </div>
        <div class="panel-footer text-end bg-transparent">
            <button type="button" class="btn btn-white btn-sm me-2">Cancel</button>
            <button type="submit" class="btn btn-primary btn-sm">Save Content</button>
        </div>
    </div>
</form>
```

### 2. Implementation Notes
- 패널의 내용물(`panel-body`)이 에디터 영역 캔버스로 온전히 채워지도록 하기 위해 `p-0` 유틸리티를 적용합니다. Summernote 내부에서 툴바 패딩 등을 스스로 관리하기 때문입니다.
- **Javascript Initialization**: `<script>` 태그를 이용해 문서가 로드될 때 `$('.summernote').summernote({ height: 300 });` 를 호출해야 합니다. 이 때 툴바 옵션을 커스텀하여 폰트 색이나 이미지 업로드 버튼 유무를 조절할 수 있습니다.
- 백엔드로 데이터가 전송될 시, 원시 `HTML` 태그(`<h1>`, `<p>`, `<img>` 등)가 그대로 넘어가므로 XSS(크로스 사이트 스크립팅) 공격 방어를 위한 서버단 Sanitizer 렌더링 검사가 필수적으로 동반되어야 합니다.
