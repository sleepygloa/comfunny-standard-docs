### 📂 3. `.docs/2_TECH_STACK.md` (기술 스택 확정)
> **변경점:** "MyBatis를 쓴다"가 아니라 "복잡한 쿼리는 MyBatis, 단순 CRUD는 JPA"처럼 **사용 기준**을 명시합니다.

```markdown
# 2. Technology Stack & Decision Records

## 2.1 Backend (Spring Boot)
| 구분 | 기술 / 라이브러리 | 버전 / 선정 이유 |
| :--- | :--- | :--- |
| **Framework** | Spring Boot | 3.2.x (Java 17) |
| **ORM (Command)** | Spring Data JPA | 단순 CRUD 및 도메인 로직 처리 |
| **ORM (Query)** | QueryDSL 5.0 | 동적 쿼리 및 Type-Safe 조회 |
| **SQL Mapper** | MyBatis 3.5 | 통계, 배치, 복잡한 네이티브 SQL 필요 시 사용 |
| **Auth** | Spring Security + JWT | Stateless 인증 아키텍처 |
| **Build** | Gradle (Groovy) | `gradle-node-plugin` 활용한 프론트 빌드 통합 |

## 2.2 Frontend 1 (Next.js - Public Web)
| 구분 | 기술 / 라이브러리 | 버전 / 선정 이유 |
| :--- | :--- | :--- |
| **Core** | Next.js | 14.0+ (App Router 필수) |
| **Language** | TypeScript | 5.x (Strict Mode) |
| **Styling** | Tailwind CSS | Utility-first CSS |
| **State** | Zustand | (필요 시) 전역 상태 관리 |
| **Fetch** | Native Fetch | Server Component 캐싱 활용 (Axios 지양) |

## 2.3 Frontend 2 (Vue.js - Admin)
| 구분 | 기술 / 라이브러리 | 버전 / 선정 이유 |
| :--- | :--- | :--- |
| **Core** | Vue 3 | Composition API (`<script setup>`) |
| **Build** | Vite | 빠른 HMR 및 빌드 속도 |
| **State** | Pinia | Vuex 대체, TypeScript 친화적 |
| **UI Kit** | Tailwind CSS + Headless UI | 커스텀 디자인 시스템 (`ComGrid` 등) 구현 |
| **Http** | Axios | Interceptor를 통한 토큰/에러 공통 처리 |