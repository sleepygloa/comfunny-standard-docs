# [B-04] Backend MVC Guide (Spring Boot + Thymeleaf)

## 목차

<!-- toc -->

- [B-04-1. Overview](#b-04-1-overview)
- [B-04-2. Initialization](#b-04-2-initialization)
  * [B-04-2.1 Dependencies (`build.gradle`)](#b-04-21-dependencies-buildgradle)
  * [B-04-2.2 VM Options (Live Reload)](#b-04-22-vm-options-live-reload)
- [B-04-3. Project Structure](#b-04-3-project-structure)
  * [B-04-3.1 Layout Standard](#b-04-31-layout-standard)

<!-- tocstop -->

## B-04-1. Overview
SEO가 중요하지 않거나, 빠른 어드민 프로토타이핑이 필요할 때 **SSR (Server Side Rendering)** 방식을 사용합니다.

---

## B-04-2. Initialization

### B-04-2.1 Dependencies (`build.gradle`)
```groovy
dependencies {
    // Web
    implementation 'org.springframework.boot:spring-boot-starter-web'
    
    // Template Engine
    implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
    implementation 'nz.net.ultraq.thymeleaf:thymeleaf-layout-dialect' // Layout
    
    // DevTools (Hot Reload)
    developmentOnly 'org.springframework.boot:spring-boot-devtools'
}
```

### B-04-2.2 VM Options (Live Reload)
IntelliJ에서 html 변경 시 바로 반영되도록 설정합니다.
```bash
-Dspring.devtools.restart.enabled=true
-Dspring.thymeleaf.cache=false
```

---

## B-04-3. Project Structure
```text
src/main/resources/
├── static/                     # Public Assets
│   ├── css/
│   ├── js/
│   └── images/
└── templates/                  # Thymeleaf HTML
    ├── layout/                 # Base Layout (header.html, footer.html)
        └── default_layout.html
    ├── index.html
    └── user/
        └── list.html
```

### B-04-3.1 Layout Standard
`default_layout.html`:
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org"
      xmlns:layout="http://www.ultraq.net.nz/thymeleaf/layout">
<head>
    <title layout:title-pattern="$CONTENT_TITLE :: $LAYOUT_TITLE">App</title>
</head>
<body>
    <div th:replace="~{fragments/header :: header}"></div>
    
    <div layout:fragment="content"></div>
    
    <div th:replace="~{fragments/footer :: footer}"></div>
</body>
</html>
```
