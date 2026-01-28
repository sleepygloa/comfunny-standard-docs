# 3. Coding Convention & Layout Standards

이 문서는 **유지보수성**을 위해 코드의 **시각적 구조(Visual Structure)**를 정의합니다.
AI는 코드 생성 시 아래의 **Block Comment(주석)**와 **정렬 순서**를 100% 준수해야 합니다.

---

## 3.1 [Backend] Java Controller/Service Pattern
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

## 3.2 [Frontend] Vue 3 (Script Setup) Pattern
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


## 3.3 [Database] SQL (MyBatis) XML Pattern
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

## 3.4 Naming Standards (Naming Convention)
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

## 3.5 Code Formatting & Layout
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


## 3.6 Comment & Documentation Standard
모든 주석과 문서는 **한국어**로 작성하는 것을 원칙으로 합니다.

### 3.6.1 Business Logic FLOW Pattern
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

### 3.6.2 Swagger (API Documentation)
Controller의 모든 `public` 메서드는 `@Operation`을 사용하여 API 명세를 코드 레벨에서 관리합니다.

```java
@Operation(
    summary = "주문 생성", 
    description = "사용자 정보와 상품 정보를 받아 주문을 생성합니다. (FLOW: 검증 -> 재고차감 -> 결제 -> 저장)"
)
@PostMapping("/orders")
public ApiResponse<OrderResponse> createOrder(...) { ... }
```

