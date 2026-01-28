### 7. `.docs/5_LOCAL_DEV_GUIDE.md` (로컬 가이드)

```markdown
# 5. Local Development Guide

## Setup Steps
1. **Repository Clone:** `git clone ...`
2. **Environment:** `.env` 파일 생성 (팀장에게 요청)
3. **Run Backend:** IntelliJ -> `backend` 폴더 Open -> `Application.java` Run.
   - Vue Admin 개발 시: `cd backend/src/main/vue-admin` -> `npm run dev`
4. **Run Web:** VS Code -> `frontend-nextjs` 폴더 Open -> `npm run dev`.

## Docker Run (Full Stack)
```bash
docker-compose up -d