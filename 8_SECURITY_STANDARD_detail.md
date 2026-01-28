# 8. Security Standard (Detailed Guide)

## 1. 개요 (Overview)
보안 규정의 **실제 구현 가이드**입니다. 프레임워크별 설정 방법과 시큐리티 코딩 체크리스트를 제공합니다.

## 2. Spring Security Implementation

### 2.1 SecurityConfig 템플릿
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

### 2.2 Password Encoding Strategy
- **절대 금지:** MD5, SHA-1 등 취약한 알고리즘.
- **권장:** `BCryptPasswordEncoder` (Spring Security 기본) 또는 `Argon2`.

## 3. Frontend Security (XSS & CSRF)

### 3.1 XSS (Cross Site Scripting)
- **Vue/React:** 기본적으로 데이터가 다 이스케이프 (`{{ }}`) 처리되므로 `v-html`이나 `dangerouslySetInnerHTML` 사용을 **엄격히 금지**합니다.
- **Sanitizer:** 부득이하게 HTML을 렌더링해야 한다면 `DOMPurify` 라이브러리를 통해 스크립트를 제거해야 합니다.

### 3.2 Sensitive Data
- **LocalStorage 금지:** Access Token이나 중요 정보를 LocalStorage에 저장하면 XSS에 취약해집니다.
- **대안:** `HttpOnly Cookie` 또는 메모리 변수(새로고침 시 사라짐) + Refresh Token 전략을 사용하십시오.

## 4. Audit Logging (감사 로그)
보안 사고 발생 시 추적을 위해 "누가, 언제, 무엇을" 했는지 기록해야 합니다.
- **대상:** 로그인/로그아웃, 개인정보 조회, 관리자 설정 변경.
- **저장소:** 애플리케이션 로그와 분리하여 별도 저장소(별도 테이블 or Audit System)에 보관하는 것을 권장합니다.
