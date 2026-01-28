# Web Frontend Guide (Init & Run)

## 1. Next.js (Primary Public Web)

### 1.1 Initialization
```bash
# 1. Create App (Trusted)
npx create-next-app@latest ./ --typescript --tailwind --eslint

# 2. Add Standard Libs
npm install zustand @tanstack/react-query lucide-react clsx
```

### 1.2 Structure (App Router)
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

## 2. Vue.js (Admin System)

### 2.1 Initialization
```bash
# 1. Create App (Vite)
npm create vue@latest . 
# Select: TypeScript, Vue Router, Pinia, ESLint, Prettier

# 2. Add Tailwind (PostCSS)
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### 2.2 Structure
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

## 3. React (Legacy or Specific Module)
**Note:** 신규 프로젝트는 Next.js를 우선 고려하십시오. CSR이 필수인 경우 Vite + React를 사용합니다.

### 3.1 Initialization
```bash
npm create vite@latest . -- --template react-ts
```
