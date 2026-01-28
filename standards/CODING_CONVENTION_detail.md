# 3. Coding Convention & Layout Standards (Detailed Guide)

## 1. 개요 (Overview)
`3_CODING_CONVENTION.md`가 **"지켜야 할 규칙"**을 나열했다면, 이 문서는 **"실제 적용 예시"**와 **"흔한 실수"**를 다룹니다.
코드 리뷰어는 이 문서를 기준으로 코멘트를 남겨야 합니다.

## 2. Java Backend 상세 가이드

### 2.1 Controller 주석 및 구조
컨트롤러는 가장 빈번하게 수정되는 파일이므로 가독성이 최우선입니다.

- **Bad Pattern:** 의존성 주입 필드와 메소드가 섞여 있고, 난잡한 공백.
    ```java
    @RestController
    public class BadController {
        @Autowired // Field injection is deprecated!
        private Service service;
        @GetMapping("/list")
        public void list() {}
        private final OtherService other; // Final without constructor?
    }
    ```

- **Good Pattern:** 명확한 구획(Block Comment).
    ```java
    /* =================================================================
     * [1] Dependency Injection
     * ================================================================= */
    private final BizService bizService;
    
    /* =================================================================
     * [2] Public API Methods
     * ================================================================= */
    // ...
    ```

### 2.2 DTO Naming & Structure
- **Inner Class 사용 지양:**
    - DTO 파일이 너무 많아진다고 클래스 내부에 static class로 DTO를 정의하는 경우가 있습니다.
    - **Rule:** 모든 DTO는 독립적인 파일(`Top-level Class`)로 관리합니다. 재사용성과 탐색 용이성을 위함입니다.
- **Suffix 규칙:**
    - 요청: `~RequestDto`, `~SearchDto`, `~SaveDto`
    - 응답: `~ResponseDto`, `~ListDto`

## 3. Frontend 상세 가이드

### 3.1 Vue 3 Script Setup Order
코드의 흐름을 예측 가능하게 만들기 위해 아래 순서를 강제합니다.

1.  **Imports:** 외부 라이브러리 -> 로컬 컴포넌트 -> 타입/유틸 순.
2.  **Props/Emits:** 외부 인터페이스 정의.
3.  **State:** `ref`, `reactive` 변수 선언.
4.  **Computed/Watch:** 파생 상태 및 감지.
5.  **Lifecycle:** `onMounted` 등.
6.  **Methods:** 함수 정의.

### 3.2 HTML/CSS Formatting
- **Self-closing:** 내용이 없는 태그는 반드시 Self-closing 합니다.
    - Good: `<HelloComponent />`
    - Bad: `<HelloComponent></HelloComponent>`
- **Order of Attributes:**
    - `v-if` / `v-for` (제어문이 가장 먼저)
    - `id` / `ref` / `key` (식별자)
    - `v-model` (데이터 바인딩)
    - `props` ...
    - `events` (@click)

## 4. Naming Convention Deep Dive

### 4.1 Boolean Variables
- **Rule:** `is`, `has`, `can`, `should` 접두사를 사용합니다.
    - `isAvailable` (O), `available` (X - 명사인지 형용사인지 모호함)
    - `hasChildren` (O)

### 4.2 DB Columns
- **Rule:** 약어 사용 시 팀 내 합의된 표준 용어 사전(Term Dictionary)을 따릅니다.
    - `REGIST_DATE` -> `REG_DT` (표준 약어 사용)
    - `NUMBER` -> `NO` or `CNT` or `AMT` (맥락에 따라 구체화)

## 5. Comment & Logic Flow Guide

### 5.1 The "Why" behind FLOW Pattern
코드를 "읽는" 시간은 "쓰는" 시간보다 월등히 깁니다.
`FLOW:` 주석은 개발자가 코드를 한 줄 한 줄 해석하지 않고도, **"이 메서드가 무슨 일을 하는지"** 1초 만에 파악하게 해줍니다.
AI(Copilot)가 코드를 수정할 때도 이 FLOW를 기준으로 더 정확한 제안을 할 수 있습니다.

### 5.2 Swagger Documentation Tips
- **Summary:** 짧고 간결하게 (e.g., "사용자 조회")
- **Description:** 상세한 제약조건이나 로직 흐름 (e.g., "삭제된 사용자는 조회되지 않습니다.")
- **Response:** 성공뿐만 아니라 **에러 응답(4xx, 5xx)**에 대한 명세도 `@ApiResponses`로 남기는 것이 좋습니다.

### 5.3 Bad Comments example
의미 없는 주석은 오히려 가독성을 해칩니다.
```java
// Bad: 코드를 그대로 읽어주는 주석
// i를 1 증가시킨다
i++;

// Bad: 뻔한 Getter/Setter 주석
/** 이름을 반환한다 */
public String getName() { ... }
```
