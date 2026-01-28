# 1. Project Overview & Directory Structure

## 1.1 Architecture Pattern
본 프로젝트는 **Hybrid Monorepo** 구조입니다.
- **Frontend (Public):** Next.js (SSR) -> Node.js Container
- **Frontend (Admin):** Vue 3 (CSR) -> Built into Spring Boot Static Resources
- **Backend:** Spring Boot (API) -> Java Container
- **Gateway:** Nginx -> Reverse Proxy & Load Balancer

## 1.2 Detailed Directory Map
AI는 파일 생성 시 아래 경로 규칙을 엄격히 준수해야 합니다.

```text
comfunny-system/ (Root)
├── docker-compose.yml
├── nginx/
│   └── conf.d/default.conf       # Gateway Configuration
├── frontend-nextjs/              # [Service 1] Homepage & Blog
│   ├── src/app/                  # App Router Root
│   ├── src/components/ui/        # Shadcn/UI Components
│   └── public/                   # Static Assets
└── backend/                      # [Service 2] Backend & Admin
    ├── build.gradle              # Gradle Build Script (Vue Plugin included)
    ├── src/main/java/com/comfunny/
    │   ├── common/               # Global Config, AOP, Utils
    │   ├── domain/               # Business Domains (User, Biz, Wms...)
    │   │   ├── controller/       # Web Layer
    │   │   ├── service/          # Business Layer
    │   │   ├── repository/       # Data Access Layer (JPA/MyBatis)
    │   │   ├── dto/              # Data Transfer Objects
    │   │   └── entity/           # JPA Entities
    │   └── Application.java
    └── src/main/vue-admin/       # [Embedded] Vue 3 Project
        ├── src/api/              # Axios API Modules
        ├── src/components/common/# Shared Components (ComGrid, StandardLayout)
        └── src/views/            # Page Components