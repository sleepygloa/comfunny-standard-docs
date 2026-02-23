# [A-08] Error Handling & Logging Standard

## 목차

<!-- toc -->

  * [A-08-10.1 Overview](#a-08-101-overview)
  * [A-08-10.2 Global Error Code System](#a-08-102-global-error-code-system)
  * [A-08-10.3 API Error Response Format](#a-08-103-api-error-response-format)
  * [A-08-10.4 Log Level Policy](#a-08-104-log-level-policy)
- [[A-08] Error Handling & Logging Standard (Detailed Guide)](#a-08-error-handling--logging-standard-detailed-guide)
  * [A-08-1. 개요 (Overview)](#a-08-1-%EA%B0%9C%EC%9A%94-overview)
  * [A-08-2. Advanced Error Handling](#a-08-2-advanced-error-handling)
    + [A-08-2.1 Exception Hierarchy](#a-08-21-exception-hierarchy)
    + [A-08-2.2 GlobalExceptionHandler](#a-08-22-globalexceptionhandler)
  * [A-08-3. Structured Logging (JSON)](#a-08-3-structured-logging-json)
    + [A-08-3.1 Why JSON?](#a-08-31-why-json)
    + [A-08-3.2 Trace ID (Correlation ID)](#a-08-32-trace-id-correlation-id)
  * [A-08-4. PII (Personal Identifiable Information) Masking](#a-08-4-pii-personal-identifiable-information-masking)
  * [A-08-5. Discord Alert Integration](#a-08-5-discord-alert-integration)
    + [A-08-5.1 Webhook Payload Format](#a-08-51-webhook-payload-format)
    + [A-08-5.2 Implementation Guide](#a-08-52-implementation-guide)

<!-- tocstop -->

## A-08-10.1 Overview
에러 처리는 사용자에게는 **친절한 안내**를, 개발자에게는 **명확한 원인**을 제공해야 합니다.
로그는 **데이터**입니다. 기계가 파싱할 수 있는 형태로 남겨야 합니다.

---

## A-08-10.2 Global Error Code System
모든 예외는 고유의 에러 코드를 가집니다. `E-{Domain}-{Number}` 형식을 따릅니다.

| 코드(Prefix) | 도메인 | 예시 |
| :--- | :--- | :--- |
| **CMM** | 공통 (Common) | `E-CMM-001` (잘못된 요청) |
| **USR** | 사용자 (User) | `E-USR-002` (비밀번호 불일치) |
| **ORD** | 주문 (Order) | `E-ORD-404` (주문 없음) |
| **BIZ** | 사업자 (Biz) | `E-BIZ-500` (PG사 연동 실패) |

---

## A-08-10.3 API Error Response Format
성공 응답(`isSuccessful: true`)과 동일한 봉투 패턴(Envelope Pattern)을 사용하되, `body`는 null입니다.

```json
{
  "header": {
    "resultCode": "E-USR-002",
    "resultMessage": "비밀번호가 일치하지 않습니다.",
    "isSuccessful": false
  },
  "body": null
}
```

---

## A-08-10.4 Log Level Policy
| Level | Usage | Alerting |
| :--- | :--- | :--- |
| **ERROR** | 시스템 동작 불가, 데이터 유실, 즉시 조치 필요 | **Discord Webhook** + SMS |
| **WARN** | 예상치 못한 상황이나 자동 복구됨 (Retry 성공 등) | **Discord Webhook** (Topic별 분리) |
| **INFO** | 주요 흐름(시작/종료), 상태 변경 Audit | - |
| **DEBUG** | 개발/테스트용 상세 데이터 (운영 금지) | - |


---

<!-- DETAILED GUIDE START -->

# [A-08] Error Handling & Logging Standard (Detailed Guide)

## A-08-1. 개요 (Overview)
운영 환경에서 로그는 **Blackbox**의 유일한 단서입니다. 검색 가능하고 분석 가능한 로그를 쌓기 위한 상세 가이드입니다.

## A-08-2. Advanced Error Handling

### A-08-2.1 Exception Hierarchy
- **BusinessException:** 개발자가 의도적으로 발생시킨 예외 (비즈니스 로직 위배). `RuntimeException`을 상속받습니다.
- **SystemException:** DB 다운, 네트워크 타임아웃 등 시스템 장애.

### A-08-2.2 GlobalExceptionHandler
Spring의 `@RestControllerAdvice`를 사용하여 모든 예외를 한곳에서 처리합니다.
- `StandardException` -> 정의된 에러 코드 리턴.
- `Exception` (Unchecked) -> `E-CMM-500` (Internal Server Error)로 마스킹하여 리턴 (보안상 StackTrace 노출 금지).

## A-08-3. Structured Logging (JSON)

### A-08-3.1 Why JSON?
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

### A-08-3.2 Trace ID (Correlation ID)
- MSA 환경에서는 요청 하나가 여러 서비스를 거쳐갑니다.
- **MDC (Mapped Diagnostic Context)** 를 활용하여 트랜잭션 시작 시 `TraceID`를 생성하고, 모든 로그에 함께 찍어야 트랜잭션 추적이 가능합니다.

## A-08-4. PII (Personal Identifiable Information) Masking
개인정보(주민번호, 전화번호, 카드번호)는 절대 로그에 원본 그대로 남기면 안 됩니다.

- **Bad:** `log.info("User created: {}", userDto);` -> `phone: 010-1234-5678` 노출.
- **Good:**
    - DTO의 `toString()`을 오버라이딩하여 마스킹 처리.
    - DTO의 `toString()`을 오버라이딩하여 마스킹 처리.
    - 또는 Logback의 Masking Pattern 적용 (정규식 치환).

## A-08-5. Discord Alert Integration
운영 중 발생하는 Critical Error는 **Discord**로 즉시 전송하여 팀이 인지할 수 있도록 합니다.

### A-08-5.1 Webhook Payload Format
Discord Incoming Webhook 규격을 준수합니다. 가독성을 위해 `embeds`를 활용합니다.
```json
{
  "content": "🚨 **Critical Error Detected**",
  "embeds": [
    {
      "title": "E-ORD-500: Payment Gateway Failure",
      "description": "KG 이니시스 결제 연동 중 타임아웃 발생",
      "color": 15548997, // Red
      "fields": [
        { "name": "Service", "value": "backend-payment", "inline": true },
        { "name": "TraceID", "value": "abc-123-def", "inline": true },
        { "name": "Time", "value": "2024-03-20 15:00:01", "inline": false }
      ]
    }
  ]
}
```

### A-08-5.2 Implementation Guide
Logback의 `AsyncAppender`를 커스텀하여 비동기로 전송하는 것을 권장합니다.
- **Why Async?** 로깅이 메인 비즈니스 로직(결제 등)의 Latency에 영향을 주면 안 됩니다.
- **Failover:** Discord 장애 시 로깅은 실패하더라도 비즈니스는 계속 돌아가야 합니다. (Exception Swallowing)

```yaml
# application-prod.yml
logging:
  discord:
    webhook-url: ${DISCORD_WEBHOOK_URL} # Kubernetes Secret으로 관리
    enabled: true
```
