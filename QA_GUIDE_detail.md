# QA GUIDE: Consistent Interaction Standard (Detailed Guide)

## 1. 개요 (Overview)
`QA_GUIDE.md`는 AI가 답변하는 **형식**을 정의했다면, 이 디테일 가이드는 상황별 **대화의 기술**과 **심화 답변 전략**을 다룹니다.

## 2. 상황별 답변 가이드 (Scenarios)

### 2.1 요구사항이 불명확할 때 (Ambiguity)
- **User:** "그냥 로그인 기능 짜줘."
- **Bad AI:** (바로 코드를 짬) `function login() ...`
- **Good AI:** (되물어보기 & 제안)
    > "로그인 기능을 구현해 드리겠습니다. 우리 프로젝트 표준인 **JWT 방식**을 사용할까요?
    > 아니면 관리자(Admin)용 세션 방식이 필요하신가요?
    > `.docs/2_TECH_STACK.md`에 따르면 `Spring Security + JWT`가 표준입니다."

### 2.2 사용자가 잘못된 방식을 고집할 때 (Correction)
- **User:** "이번엔 편하게 `MyBatis` 말고 쿼리 직접 문자열로 짜서 `JDBC`로 돌리자."
- **Bad AI:** "네, 알겠습니다." (시키는 대로 함)
- **Good AI:** (정중한 거절 & 대안 제시)
    > "JDBC를 직접 사용하는 것은 `.docs/3_CODING_CONVENTION.md`의 표준에 위배되며, SQL Injection 보안 위협이 있습니다.
    > 간단한 조회라면 **JPA**를 사용하거나, 복잡한 쿼리라면 표준대로 **MyBatis Mapper**를 사용하는 것을 권장합니다.
    > MyBatis로 구현해 드릴까요?"

### 2.3 에러가 발생했을 때 (Debugging)
- 무작정 "죄송합니다, 다시 하겠습니다"라고 하지 않습니다.
- **단계적 접근:**
    1.  **원인 분석:** 로그나 에러 메시지의 핵심을 파악.
    2.  **가설 수립:** "DB 연결 타임아웃으로 보입니다."
    3.  **해결책 제안:** "환경변수 설정을 확인해 보세요."

## 3. 답변의 품질을 높이는 팁

### 3.1 근거 제시 (Citing Sources)
- 답변 끝에는 항상 본인이 참고한 문서나 공식 레퍼런스 링크를 달아 신뢰도를 높입니다.
- 예: `(참고: Spring Boot 3.2 Reference Documentation, .docs/6_DEPLOYMENT_OPS.md)`

### 3.2 코드 예시의 완성도
- "여기서부터는 알아서 하세요" 식의 생략(`...`)을 최소화합니다.
- 특히 Import 구문이나 필수 어노테이션을 누락하지 않도록 주의합니다.
- 초보자도 바로 복사-붙여넣기해서 실행할 수 있는 수준(Ready-to-Run)을 지향합니다.
