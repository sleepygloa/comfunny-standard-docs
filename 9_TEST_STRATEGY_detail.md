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
