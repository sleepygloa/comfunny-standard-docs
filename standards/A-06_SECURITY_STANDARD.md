# [A-06] Security Standard

## 목차

<!-- toc -->

  * [A-06-8.1 Overview](#a-06-81-overview)
  * [A-06-8.2 Authentication & Authorization (인증/인가)](#a-06-82-authentication--authorization-%EC%9D%B8%EC%A6%9D%EC%9D%B8%EA%B0%80)
  * [A-06-8.3 Data Encryption (데이터 암호화)](#a-06-83-data-encryption-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%95%94%ED%98%B8%ED%99%94)
  * [A-06-8.4 Network Security (네트워크 보안)](#a-06-84-network-security-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%B3%B4%EC%95%88)
- [[A-06] Security Standard (Detailed Guide)](#a-06-security-standard-detailed-guide)
  * [A-06-1. 개요 (Overview)](#a-06-1-%EA%B0%9C%EC%9A%94-overview)
  * [A-06-2. Spring Security Implementation](#a-06-2-spring-security-implementation)
    + [A-06-2.1 SecurityConfig 템플릿](#a-06-21-securityconfig-%ED%85%9C%ED%94%8C%EB%A6%BF)
    + [A-06-2.2 Password Encoding Strategy](#a-06-22-password-encoding-strategy)
  * [A-06-3. Frontend Security (XSS & CSRF)](#a-06-3-frontend-security-xss--csrf)
    + [A-06-3.1 XSS (Cross Site Scripting)](#a-06-31-xss-cross-site-scripting)
    + [A-06-3.2 Sensitive Data](#a-06-32-sensitive-data)
  * [A-06-4. Audit Logging (감사 로그)](#a-06-4-audit-logging-%EA%B0%90%EC%82%AC-%EB%A1%9C%EA%B7%B8)

<!-- tocstop -->

## A-06-8.1 Overview
보안은 기능이 아니라 **기본 품질**입니다. "나중에 심사 받을 때 고치자"는 허용되지 않습니다.
모든 코드는 작성 시점부터 아래 보안 규칙을 준수해야 합니다.

---

## A-06-8.2 Authentication & Authorization (인증/인가)
- **Token Based:** 전송 계층은 Bearer Type의 **JWT**를 표준으로 합니다.
- **Stateless:** 서버 세션을 사용하지 않으며, 토큰 검증은 모든 API 요청마다 수행합니다.
- **RBAC (Role Based Access Control):** 
    - URL 패턴 매칭이 아닌, 메서드 레벨(`@PreAuthorize`) 제어를 기본으로 합니다.
    - 역할 예시: `ROLE_USER`, `ROLE_ADMIN`, `ROLE_SYSTEM`.

---

## A-06-8.3 Data Encryption (데이터 암호화)
DB에 저장되는 중요 정보는 반드시 암호화해야 합니다.

| 데이터 유형 | 암호화 방식 | 알고리즘 | 비고 |
| :--- | :--- | :--- | :--- |
| **비밀번호** | 단방향(해시) | BCrypt | 복호화 불가능해야 함 |
| **개인정보/계좌** | 양방향 | AES-256 (CBC/GCM) | 키 관리는 KMS/Vault 사용 권장 |
| **일반 텍스트** | Plain | - | - |

---

## A-06-8.4 Network Security (네트워크 보안)
- **SSL/TLS:** 모든 통신은 `HTTPS`를 강제합니다. (운영 환경)
- **CORS:** `*`(Allow-All) 사용을 금지하며, 신뢰할 수 있는 도메인만 명시적으로 허용합니다.
- **Rate Limiting:** IP당 요청 횟수를 제한하여 DDoS 및 Brute-Force 공격을 방어합니다.


---

<!-- DETAILED GUIDE START -->

# [A-06] Security Standard (Detailed Guide)

## A-06-1. 개요 (Overview)
보안 규정의 **실제 구현 가이드**입니다. 프레임워크별 설정 방법과 시큐리티 코딩 체크리스트를 제공합니다.

## A-06-2. Spring Security Implementation

### A-06-2.1 SecurityConfig 템플릿
```java
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .csrf(AbstractHttpConfigurer::disable) // JWT 사용 시 비활성화
        .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/api/auth/**", "/actuator/health").permitAll()
            .requestMatchers("/api/admin/**").hasRole("ADMIN")
            .anyRequest().authenticated()
        )
        .addFilterBefore(jwtAuthFilter, UsernamePasswordAuthenticationFilter.class);
    return http.build();
}
```

### A-06-2.2 Password Encoding Strategy
- **절대 금지:** MD5, SHA-1 등 취약한 알고리즘.
- **권장:** `BCryptPasswordEncoder` (Spring Security 기본) 또는 `Argon2`.

## A-06-3. Frontend Security (XSS & CSRF)

### A-06-3.1 XSS (Cross Site Scripting)
- **Vue/React:** 기본적으로 데이터가 다 이스케이프 (`{{ }}`) 처리되므로 `v-html`이나 `dangerouslySetInnerHTML` 사용을 **엄격히 금지**합니다.
- **Sanitizer:** 부득이하게 HTML을 렌더링해야 한다면 `DOMPurify` 라이브러리를 통해 스크립트를 제거해야 합니다.

### A-06-3.2 Sensitive Data
- **LocalStorage 금지:** Access Token이나 중요 정보를 LocalStorage에 저장하면 XSS에 취약해집니다.
- **대안:** `HttpOnly Cookie` 또는 메모리 변수(새로고침 시 사라짐) + Refresh Token 전략을 사용하십시오.

## A-06-4. Audit Logging (감사 로그)
보안 사고 발생 시 추적을 위해 "누가, 언제, 무엇을" 했는지 기록해야 합니다.
- **대상:** 로그인/로그아웃, 개인정보 조회, 관리자 설정 변경.
- **저장소:** 애플리케이션 로그와 분리하여 별도 저장소(별도 테이블 or Audit System)에 보관하는 것을 권장합니다.
