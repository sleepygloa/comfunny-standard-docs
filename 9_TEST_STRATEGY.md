# 9. Test Strategy

## 9.1 Overview
테스트 없는 코드는 **레거시(기술 부채)**입니다.
우리는 **Test Pyramid** 전략을 따르며, 빠르고 신뢰성 있는 테스트를 지향합니다.

---

## 9.2 Test Pyramid Strategy
| Level | Scope | Tool | Frequency |
| :--- | :--- | :--- | :--- |
| **Unit** | 클래스/메서드 단위 격리 테스트 | JUnit5, Mockito, Jest | 매 빌드/커밋 시 |
| **Integration** | DB/API 연동 포함 모듈 테스트 | @SpringBootTest | CI 파이프라인 |
| **E2E** | 사용자 시나리오 전체 테스트 | Cypress, Selenium | 배포 전 (Nightly) |

---

## 9.3 Minimum Coverage Requirement
- **Business Logic (Service/Domain):** **80%** 이상 (필수)
- **Utils/Helper:** **90%** 이상
- **UI Components:** 핵심 컴포넌트 위주 작성 (수치 강제 없음)
- **Exclusion:** DTO, Getter/Setter, 단순 Configuration 등 로직 없는 코드.

---

## 9.4 Test Naming Convention
한글로 명확하게 작성하는 것을 권장합니다 (DCI 패턴).

- **Format:** `메서드명_상황_기대결과()` or `@DisplayName("...")`
- **Example:**
    ```java
    @Test
    @DisplayName("회원가입_이메일중복시_예외발생")
    void join_duplicateEmail_throwException() { ... }
    ```
