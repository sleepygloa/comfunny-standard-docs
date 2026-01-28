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
