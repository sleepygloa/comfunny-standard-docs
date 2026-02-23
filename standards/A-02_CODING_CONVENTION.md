# [A-02] Coding Convention & Layout Standards

## 목차

<!-- toc -->

  * [A-02-3.1 [Backend] Java Controller/Service Pattern](#a-02-31-backend-java-controllerservice-pattern)
  * [A-02-3.6 Comment & Documentation Standard](#a-02-36-comment--documentation-standard)
    + [A-02-3.6.1 Business Logic FLOW Pattern](#a-02-361-business-logic-flow-pattern)
    + [A-02-3.6.2 Swagger (API Documentation)](#a-02-362-swagger-api-documentation)
- [[A-02] Coding Convention & Layout Standards (Detailed Guide)](#a-02-coding-convention--layout-standards-detailed-guide)
  * [A-02-1. 개요 (Overview)](#a-02-1-%EA%B0%9C%EC%9A%94-overview)
  * [A-02-2. Java Backend 상세 가이드](#a-02-2-java-backend-%EC%83%81%EC%84%B8-%EA%B0%80%EC%9D%B4%EB%93%9C)
    + [A-02-2.1 Controller 주석 및 구조](#a-02-21-controller-%EC%A3%BC%EC%84%9D-%EB%B0%8F-%EA%B5%AC%EC%A1%B0)
    + [A-02-2.2 DTO Naming & Structure](#a-02-22-dto-naming--structure)
  * [A-02-3. Frontend 상세 가이드](#a-02-3-frontend-%EC%83%81%EC%84%B8-%EA%B0%80%EC%9D%B4%EB%93%9C)
    + [A-02-3.1 Vue 3 Script Setup Order](#a-02-31-vue-3-script-setup-order)
    + [A-02-3.2 HTML/CSS Formatting](#a-02-32-htmlcss-formatting)
  * [A-02-4. Naming Convention Deep Dive](#a-02-4-naming-convention-deep-dive)
    + [A-02-4.1 Boolean Variables](#a-02-41-boolean-variables)
    + [A-02-4.2 DB Columns](#a-02-42-db-columns)
  * [A-02-5. Comment & Logic Flow Guide](#a-02-5-comment--logic-flow-guide)
    + [A-02-5.1 The "Why" behind FLOW Pattern](#a-02-51-the-why-behind-flow-pattern)
    + [A-02-5.2 Swagger Documentation Tips](#a-02-52-swagger-documentation-tips)
    + [A-02-5.3 Bad Comments example](#a-02-53-bad-comments-example)

<!-- tocstop -->

이 문서는 **유지보수성**을 위해 코드의 **시각적 구조(Visual Structure)**를 정의합니다.
AI는 코드 생성 시 아래의 **Block Comment(주석)**와 **정렬 순서**를 100% 준수해야 합니다.

---

## A-02-3.1 [Backend] Java Controller/Service Pattern
**규칙:** 클래스 내부는 반드시 `DI` -> `Public Method` -> `Private Method` 순서로 배치하며, 각 섹션은 주석으로 구분한다.

```java
@RestController
@RequestMapping("/api/v1/biz")
@RequiredArgsConstructor
public class BizController {

    /* =================================================================
     * [1] Dependency Injection & Constants
     * ================================================================= */
    private final BizService bizService;
    private final CommonCodeService commonCodeService;

    /* =================================================================
     * [2] Public API Methods (Request Handling)
     * ================================================================= */
    /**
     * 사업자 목록 조회 (페이징)
     */
    @PostMapping("/list")
    public ApiResponse<PageResponse<BizDto>> getBizList(@RequestBody @Valid BizSearchDto searchDto) {
        return ApiResponse.success(bizService.getBizList(searchDto));
    }

    @PostMapping("/save")
    public ApiResponse<Long> saveBiz(@RequestBody @Valid BizSaveDto saveDto) {
        return ApiResponse.success(bizService.saveBiz(saveDto));
    }

    /* =================================================================
     * [3] Private Helper Methods (Internal Logic)
     * ================================================================= */
    private void validateBizStatus(BizSaveDto dto) {
        // Validation logic...
    }
}

## A-02-3.2 [Frontend] Vue 3 (Script Setup) Pattern
**규칙:** <script setup> 내부는 Import -> State -> Lifecycle -> Methods 순서로 작성한다.

```html
<script setup lang="ts">
/* -----------------------------------------------------------------
 * [1] Imports & Props/Emits
 * ----------------------------------------------------------------- */
import { ref, onMounted, computed } from 'vue';
import { useBizStore } from '@/stores/biz';
import type { BizDto } from '@/types/biz';

const props = defineProps<{ id: number }>();
const emit = defineEmits(['saved', 'closed']);

/* -----------------------------------------------------------------
 * [2] State & Reactive Variables
 * ----------------------------------------------------------------- */
const bizStore = useBizStore();
const isLoading = ref<boolean>(false);
const formData = ref<BizDto>({ bizNm: '', bizNo: '' });

/* -----------------------------------------------------------------
 * [3] Lifecycle Hooks
 * ----------------------------------------------------------------- */
onMounted(async () => {
    await fetchDetail();
});

/* -----------------------------------------------------------------
 * [4] Methods (Event Handlers & API Calls)
 * ----------------------------------------------------------------- */
const fetchDetail = async () => {
    try {
        isLoading.value = true;
        formData.value = await bizStore.getBiz(props.id);
    } finally {
        isLoading.value = false;
    }
};

const onSave = () => {
    emit('saved', formData.value);
};
</script>

<template>
</template>


## A-02-3.3 [Database] SQL (MyBatis) XML Pattern
**규칙:** ResultMap -> Select -> Insert/Update/Delete 순서로 정렬한다.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" ...>
<mapper namespace="com.comfunny.domain.biz.repository.BizMapper">

    <resultMap id="BizResultMap" type="com.comfunny.domain.biz.dto.BizDto">
        <id property="id" column="ID" />
        <result property="bizNm" column="BIZ_NM" />
    </resultMap>

    <select id="selectBizList" resultMap="BizResultMap">
        SELECT * FROM TB_BIZ
        WHERE USE_YN = 'Y'
    </select>

    <insert id="insertBiz">
        INSERT INTO TB_BIZ (...) VALUES (...)
    </insert>


</mapper>

## A-02-3.4 Naming Standards (Naming Convention)
AI는 코드 생성 시 아래 명명 규칙을 **엄격히** 준수해야 한다.

### [Common]
- **File Names:**
  - Classes/Components: `PascalCase` (e.g., `BizController.java`, `BizGraph.vue`)
  - Config/Resources: `kebab-case` (e.g., `application-prod.yml`, `common-style.css`)
  - Folders/Packages: `kebab-case` (e.g., `domain-biz`, `components/ui`)

### [Backend - Java]
- **Classes:** `PascalCase` (Noun). Suffix 필수 (`Controller`, `Service`, `Repository`, `Dto`).
- **Methods:** `camelCase` (Verb).
  - 조회: `find...` (JPA), `select...` (Mapper), `get...` (Simple Getter)
  - 저장/수정: `save...`, `update...`
  - 삭제: `delete...`, `remove...`
- **Variables:** `camelCase`.
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_RETRY_COUNT`).

### [Frontend - JS/TS]
- **Components:** `PascalCase` (e.g., `UserCard.vue`).
- **Props:** `camelCase`.
- **Event Emits:** `kebab-case` in template (`@save-data`), `camelCase` in script.
- **Functions:** `camelCase` (e.g., `fetchData`, `handleClick`).

### [Database]
- **Tables:** `tb_` prefix + `UPPER_SNAKE_CASE` (e.g., `TB_BIZ_INFO`).
- **Columns:** `UPPER_SNAKE_CASE` (e.g., `BIZ_NM`, `REG_DT`).

---

## A-02-3.5 Code Formatting & Layout
**Prettier/Checkstyle** 설정과 일치하도록 코드를 생성한다.

### [Indentation]
- **Java:** 4 Spaces.
- **Web (JS/Vue/HTML/CSS):** 2 Spaces.
- **XML/YAML:** 2 Spaces.

### [Structure]
- **Line Length:** 최대 120자. 초과 시 적절히 줄바꿈.
- **Chaining:** 메서드 체이닝 시 점(`.`)을 기준으로 줄바꿈하고 수직 정렬.
  ```java
  // Good
  return bizRepository.findById(id)
          .filter(Biz::isActive)
          .orElseThrow(() -> new NotFoundException());
  ```
- **Vertical Spacing:** 논리적 단위(메서드, inner class 등) 사이에는 빈 줄 1개 삽입.


## A-02-3.6 Comment & Documentation Standard
모든 주석과 문서는 **한국어**로 작성하는 것을 원칙으로 합니다.

### A-02-3.6.1 Business Logic FLOW Pattern
복잡한 비즈니스 로직(Service method)은 **반드시** 상단에 전체 흐름(FLOW)을 요약하고, 코드 라인과 1:1 매핑해야 합니다.

```java
/**
 * 주문 생성 처리
 * 
 * NOTE: 재고 차감 후 결제를 시도한다.
 */
@Transactional
public OrderResponse createOrder(OrderRequest request) {
    // FLOW:
    // 1. 사용자 유효성 검증
    // 2. 상품 재고 확인 및 차감
    // 3. 결제 요청 (외부 PG)
    // 4. 주문 정보 저장 및 결과 반환

    // 1. 사용자 유효성 검증
    User user = userService.validateUser(request.getUserId());

    // 2. 상품 재고 확인 및 차감
    productService.decreaseStock(request.getProductId(), request.getQuantity());

    // 3. 결제 요청 (외부 PG)
    PaymentResult payment = paymentClient.approve(user, request.getAmount());

    // 4. 주문 정보 저장 및 결과 반환
    return orderRepository.save(Order.from(user, payment));
}
```

### A-02-3.6.2 Swagger (API Documentation)
Controller의 모든 `public` 메서드는 `@Operation`을 사용하여 API 명세를 코드 레벨에서 관리합니다.

```java
@Operation(
    summary = "주문 생성", 
    description = "사용자 정보와 상품 정보를 받아 주문을 생성합니다. (FLOW: 검증 -> 재고차감 -> 결제 -> 저장)"
)
@PostMapping("/orders")
public ApiResponse<OrderResponse> createOrder(...) { ... }
```



---

<!-- DETAILED GUIDE START -->

# [A-02] Coding Convention & Layout Standards (Detailed Guide)

## A-02-1. 개요 (Overview)
`3_CODING_CONVENTION.md`가 **"지켜야 할 규칙"**을 나열했다면, 이 문서는 **"실제 적용 예시"**와 **"흔한 실수"**를 다룹니다.
코드 리뷰어는 이 문서를 기준으로 코멘트를 남겨야 합니다.

## A-02-2. Java Backend 상세 가이드

### A-02-2.1 Controller 주석 및 구조
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

### A-02-2.2 DTO Naming & Structure
- **Inner Class 사용 지양:**
    - DTO 파일이 너무 많아진다고 클래스 내부에 static class로 DTO를 정의하는 경우가 있습니다.
    - **Rule:** 모든 DTO는 독립적인 파일(`Top-level Class`)로 관리합니다. 재사용성과 탐색 용이성을 위함입니다.
- **Suffix 규칙:**
    - 요청: `~RequestDto`, `~SearchDto`, `~SaveDto`
    - 응답: `~ResponseDto`, `~ListDto`

## A-02-3. Frontend 상세 가이드

### A-02-3.1 Vue 3 Script Setup Order
코드의 흐름을 예측 가능하게 만들기 위해 아래 순서를 강제합니다.

1.  **Imports:** 외부 라이브러리 -> 로컬 컴포넌트 -> 타입/유틸 순.
2.  **Props/Emits:** 외부 인터페이스 정의.
3.  **State:** `ref`, `reactive` 변수 선언.
4.  **Computed/Watch:** 파생 상태 및 감지.
5.  **Lifecycle:** `onMounted` 등.
6.  **Methods:** 함수 정의.

### A-02-3.2 HTML/CSS Formatting
- **Self-closing:** 내용이 없는 태그는 반드시 Self-closing 합니다.
    - Good: `<HelloComponent />`
    - Bad: `<HelloComponent></HelloComponent>`
- **Order of Attributes:**
    - `v-if` / `v-for` (제어문이 가장 먼저)
    - `id` / `ref` / `key` (식별자)
    - `v-model` (데이터 바인딩)
    - `props` ...
    - `events` (@click)

## A-02-4. Naming Convention Deep Dive

### A-02-4.1 Boolean Variables
- **Rule:** `is`, `has`, `can`, `should` 접두사를 사용합니다.
    - `isAvailable` (O), `available` (X - 명사인지 형용사인지 모호함)
    - `hasChildren` (O)

### A-02-4.2 DB Columns
- **Rule:** 약어 사용 시 팀 내 합의된 표준 용어 사전(Term Dictionary)을 따릅니다.
    - `REGIST_DATE` -> `REG_DT` (표준 약어 사용)
    - `NUMBER` -> `NO` or `CNT` or `AMT` (맥락에 따라 구체화)

## A-02-5. Comment & Logic Flow Guide

### A-02-5.1 The "Why" behind FLOW Pattern
코드를 "읽는" 시간은 "쓰는" 시간보다 월등히 깁니다.
`FLOW:` 주석은 개발자가 코드를 한 줄 한 줄 해석하지 않고도, **"이 메서드가 무슨 일을 하는지"** 1초 만에 파악하게 해줍니다.
AI(Copilot)가 코드를 수정할 때도 이 FLOW를 기준으로 더 정확한 제안을 할 수 있습니다.

### A-02-5.2 Swagger Documentation Tips
- **Summary:** 짧고 간결하게 (e.g., "사용자 조회")
- **Description:** 상세한 제약조건이나 로직 흐름 (e.g., "삭제된 사용자는 조회되지 않습니다.")
- **Response:** 성공뿐만 아니라 **에러 응답(4xx, 5xx)**에 대한 명세도 `@ApiResponses`로 남기는 것이 좋습니다.

### A-02-5.3 Bad Comments example
의미 없는 주석은 오히려 가독성을 해칩니다.
```java
// Bad: 코드를 그대로 읽어주는 주석
// i를 1 증가시킨다
i++;

// Bad: 뻔한 Getter/Setter 주석
/** 이름을 반환한다 */
public String getName() { ... }
```
