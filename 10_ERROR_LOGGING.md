# 10. Error Handling & Logging Standard

## 10.1 Overview
에러 처리는 사용자에게는 **친절한 안내**를, 개발자에게는 **명확한 원인**을 제공해야 합니다.
로그는 **데이터**입니다. 기계가 파싱할 수 있는 형태로 남겨야 합니다.

---

## 10.2 Global Error Code System
모든 예외는 고유의 에러 코드를 가집니다. `E-{Domain}-{Number}` 형식을 따릅니다.

| 코드(Prefix) | 도메인 | 예시 |
| :--- | :--- | :--- |
| **CMM** | 공통 (Common) | `E-CMM-001` (잘못된 요청) |
| **USR** | 사용자 (User) | `E-USR-002` (비밀번호 불일치) |
| **ORD** | 주문 (Order) | `E-ORD-404` (주문 없음) |
| **BIZ** | 사업자 (Biz) | `E-BIZ-500` (PG사 연동 실패) |

---

## 10.3 API Error Response Format
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

## 10.4 Log Level Policy
| Level | Usage | Alerting |
| :--- | :--- | :--- |
| **ERROR** | 시스템 동작 불가, 데이터 유실, 즉시 조치 필요 | **SLA 위반 알림 (Call/SMS)** |
| **WARN** | 예상치 못한 상황이나 자동 복구됨 (Retry 성공 등) | Slack 알림 |
| **INFO** | 주요 흐름(시작/종료), 상태 변경 Audit | - |
| **DEBUG** | 개발/테스트용 상세 데이터 (운영 금지) | - |
