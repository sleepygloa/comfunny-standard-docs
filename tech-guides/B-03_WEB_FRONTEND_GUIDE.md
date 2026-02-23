# [B-03] Web Frontend Guide (Init & Run)

## 목차

<!-- toc -->

- [B-03-1. Next.js (Primary Public Web)](#b-03-1-nextjs-primary-public-web)
  * [B-03-1.1 Initialization](#b-03-11-initialization)
  * [B-03-1.2 Structure (App Router)](#b-03-12-structure-app-router)
- [B-03-2. Vue.js (Admin System)](#b-03-2-vuejs-admin-system)
  * [B-03-2.1 Initialization](#b-03-21-initialization)
  * [B-03-2.2 Structure](#b-03-22-structure)
- [B-03-3. React (Legacy or Specific Module)](#b-03-3-react-legacy-or-specific-module)
  * [B-03-3.1 Initialization](#b-03-31-initialization)

<!-- tocstop -->

## B-03-1. Next.js (Primary Public Web)

### B-03-1.1 Initialization
```bash
# 1. Create App (Trusted)
npx create-next-app@latest ./ --typescript --tailwind --eslint

# 2. Add Standard Libs
npm install zustand @tanstack/react-query lucide-react clsx
```

### B-03-1.2 Structure (App Router)
```text
src/
├── app/                        # Pages & Layouts
│   ├── (public)/               # Route Group (Public)
│   └── (admin)/                # Route Group (Admin)
├── components/
│   ├── ui/                     # Atoms (Button, Input)
│   └── widget/                 # Business Components
├── lib/                        # Utils (fetcher, utils)
└── store/                      # Zustand Stores
```

---

## B-03-2. Vue.js (Admin System)

### B-03-2.1 Initialization
```bash
# 1. Create App (Vite)
npm create vue@latest . 
# Select: TypeScript, Vue Router, Pinia, ESLint, Prettier

# 2. Add Tailwind (PostCSS)
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### B-03-2.2 Structure
```text
src/
├── app.vue
├── main.ts
├── api/                        # Axios Wrapper
├── stores/                     # Pinia Stores
├── views/                      # Pages
└── components/                 # Shared Components
```

---

## B-03-3. React (Legacy or Specific Module)
**Note:** 신규 프로젝트는 Next.js를 우선 고려하십시오. CSR이 필수인 경우 Vite + React를 사용합니다.

### B-03-3.1 Initialization
```bash
npm create vite@latest . -- --template react-ts
```
