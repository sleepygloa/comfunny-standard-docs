# 8. Security Standard

## 8.1 Overview
보안은 기능이 아니라 **기본 품질**입니다. "나중에 심사 받을 때 고치자"는 허용되지 않습니다.
모든 코드는 작성 시점부터 아래 보안 규칙을 준수해야 합니다.

---

## 8.2 Authentication & Authorization (인증/인가)
- **Token Based:** 전송 계층은 Bearer Type의 **JWT**를 표준으로 합니다.
- **Stateless:** 서버 세션을 사용하지 않으며, 토큰 검증은 모든 API 요청마다 수행합니다.
- **RBAC (Role Based Access Control):** 
    - URL 패턴 매칭이 아닌, 메서드 레벨(`@PreAuthorize`) 제어를 기본으로 합니다.
    - 역할 예시: `ROLE_USER`, `ROLE_ADMIN`, `ROLE_SYSTEM`.

---

## 8.3 Data Encryption (데이터 암호화)
DB에 저장되는 중요 정보는 반드시 암호화해야 합니다.

| 데이터 유형 | 암호화 방식 | 알고리즘 | 비고 |
| :--- | :--- | :--- | :--- |
| **비밀번호** | 단방향(해시) | BCrypt | 복호화 불가능해야 함 |
| **개인정보/계좌** | 양방향 | AES-256 (CBC/GCM) | 키 관리는 KMS/Vault 사용 권장 |
| **일반 텍스트** | Plain | - | - |

---

## 8.4 Network Security (네트워크 보안)
- **SSL/TLS:** 모든 통신은 `HTTPS`를 강제합니다. (운영 환경)
- **CORS:** `*`(Allow-All) 사용을 금지하며, 신뢰할 수 있는 도메인만 명시적으로 허용합니다.
- **Rate Limiting:** IP당 요청 횟수를 제한하여 DDoS 및 Brute-Force 공격을 방어합니다.
