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


---

<!-- DETAILED GUIDE START -->

# 9. Test Strategy (Detailed Guide)

## 1. 개요 (Overview)
테스트 코드는 작성하고 끝이 아니라, **살아있는 문서**여야 합니다. 유지보수하기 쉬운 테스트 코드를 작성하는 방법을 가이드합니다.

## 2. Unit Testing Best Practices (Backend)

### 2.1 Mocking Strategy (Mockito)
- **Don't Mock Everything:** 너무 많은 Mocking은 테스트를 취약하게 만듭니다. 순수 자바 객체(Domain/Utils)는 Mock 없이 실제 객체를 쓰세요.
- **Service Test:** Repository 등의 `IO` 작업만 Mocking 합니다.

```java
// Good: 의존성만 가짜 객체로 대체
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {
    @Mock OrderRepository orderRepository;
    @InjectMocks OrderService orderService;
    
    @Test
    void 주문취소_성공() {
        // given
        given(orderRepository.findById(1L)).willReturn(Optional.of(testOrder));
        // when
        orderService.cancel(1L);
        // then
        assertThat(testOrder.getStatus()).isEqualTo(OrderStatus.CANCEL);
    }
}
```

## 3. Integration Testing Best Practices

### 3.1 @SpringBootTest slicing
- `@SpringBootTest`는 너무 무겁습니다. 필요한 레이어만 로드하십시오.
    - Controller 테스트: `@WebMvcTest`
    - Repository 테스트: `@DataJpaTest` (내장 DB 사용)

### 3.2 Test Data Management
- 테스트 간의 **데이터 오염**을 막아야 합니다.
- `@Transactional`: 테스트 메서드 종료 후 자동 롤백 (가장 권장).
- `@Sql`: 테스트 실행 전 `schema.sql`, `data.sql`로 초기화.

## 4. Frontend Testing (Jest / Vitest)
- **Snapshot Test:** UI 변경 감지에는 유용하나, 깨지기 쉬우므로 남용하지 않습니다.
- **User Interaction:** 내부 구현(`state.value = ...`)을 테스트하지 말고, 사용자 행위(`fireEvent.click`)를 테스트하십시오. (Implementation Details vs Behavior)
