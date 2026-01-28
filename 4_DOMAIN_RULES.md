## 📂 5. `.docs/4_DOMAIN_RULES.md` (API & 보안 표준)
> **변경점:** API 응답 포맷을 JSON 형태로 박제하고, 에러 처리 방식을 구체화했습니다.

```markdown
# 4. Domain, API & Security Rules

## 4.1 API Response Standard (JSend Like)
모든 REST API 응답은 아래의 JSON 구조를 반드시 따라야 한다. 프론트엔드는 `header.resultCode`를 보고 성공 여부를 판단한다.

**Success Response:**
```json
{
  "header": {
    "resultCode": "0000",
    "resultMessage": "요청이 성공하였습니다.",
    "isSuccessful": true
  },
  "body": {
    "data": [ ... ],
    "page": 1,
    "total": 100
  }
}

** Error Response ** 
```json
{
  "header": {
    "resultCode": "E-4001",
    "resultMessage": "필수 입력값이 누락되었습니다.",
    "isSuccessful": false
  },
  "body": null
}