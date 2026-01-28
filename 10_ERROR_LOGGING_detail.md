# 10. Error Handling & Logging Standard (Detailed Guide)

## 1. 개요 (Overview)
운영 환경에서 로그는 **Blackbox**의 유일한 단서입니다. 검색 가능하고 분석 가능한 로그를 쌓기 위한 상세 가이드입니다.

## 2. Advanced Error Handling

### 2.1 Exception Hierarchy
- **BusinessException:** 개발자가 의도적으로 발생시킨 예외 (비즈니스 로직 위배). `RuntimeException`을 상속받습니다.
- **SystemException:** DB 다운, 네트워크 타임아웃 등 시스템 장애.

### 2.2 GlobalExceptionHandler
Spring의 `@RestControllerAdvice`를 사용하여 모든 예외를 한곳에서 처리합니다.
- `StandardException` -> 정의된 에러 코드 리턴.
- `Exception` (Unchecked) -> `E-CMM-500` (Internal Server Error)로 마스킹하여 리턴 (보안상 StackTrace 노출 금지).

## 3. Structured Logging (JSON)

### 3.1 Why JSON?
Text 로그(`2024-01-01 ERROR...`)는 ELK에서 파싱하기 어렵고, 줄바꿈(Stacktrace) 처리도 까다롭습니다.
운영 환경(`prod`)에서는 반드시 **LogstashEncoder** 등을 사용하여 JSON으로 출력합니다.

```json
{
  "@timestamp": "2024-01-01T10:00:00.000Z",
  "level": "ERROR",
  "service": "backend-api",
  "traceId": "a1b2c3d4",
  "message": "Payment failed",
  "stack_trace": "java.lang.NullPointerException..."
}
```

### 3.2 Trace ID (Correlation ID)
- MSA 환경에서는 요청 하나가 여러 서비스를 거쳐갑니다.
- **MDC (Mapped Diagnostic Context)** 를 활용하여 트랜잭션 시작 시 `TraceID`를 생성하고, 모든 로그에 함께 찍어야 트랜잭션 추적이 가능합니다.

## 4. PII (Personal Identifiable Information) Masking
개인정보(주민번호, 전화번호, 카드번호)는 절대 로그에 원본 그대로 남기면 안 됩니다.

- **Bad:** `log.info("User created: {}", userDto);` -> `phone: 010-1234-5678` 노출.
- **Good:**
    - DTO의 `toString()`을 오버라이딩하여 마스킹 처리.
    - 또는 Logback의 Masking Pattern 적용 (정규식 치환).
