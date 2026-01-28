### 📂 7. `.docs/7_GIT_STRATEGY.md` (협업 및 버전 관리)
> **핵심:** "커밋 메시지만 봐도 어떤 기능인지 알 수 있어야 하며, `main` 브랜치는 언제나 배포 가능해야 한다."

```markdown
# 7. Git Collaboration Strategy

## 7.1 Branching Model (Git-Flow Lite)
대기업 표준에 맞춰 간소화된 Git-Flow를 사용한다.

- **`main` (Protected):** 운영 서버에 배포되는 브랜치. **직접 푸시 금지.** PR(Pull Request)로만 병합 가능.
- **`develop`:** 개발계 서버에 배포되는 통합 브랜치.
- **`feat/이슈번호-기능명`:** 개별 기능 개발 브랜치. (예: `feat/WMS-102-login-page`)
- **`fix/이슈번호-버그명`:** 버그 수정 브랜치.
- **`hotfix/날짜-내용`:** 운영 긴급 수정.

## 7.2 Commit Convention (Conventional Commits)
모든 커밋 메시지는 아래 포맷을 엄격히 준수한다. (AI가 코드 생성 시 자동 적용)

`type(scope): subject`

- **Types:**
  - `feat`: 새로운 기능 추가
  - `fix`: 버그 수정
  - `docs`: 문서 수정 (`.docs` 폴더 등)
  - `style`: 코드 포맷팅, 세미콜론 누락 등 (로직 변경 없음)
  - `refactor`: 코드 리팩토링 (기능 변경 없음)
  - `chore`: 빌드 업무 수정, 패키지 매니저 설정 등

- **Example:**
  - `feat(auth): Add JWT validation logic`
  - `fix(biz): Resolve grid paging error on mobile`

## 7.3 Pull Request (PR) Rules
1.  **Title:** `[FEAT] WMS-102 로그인 페이지 구현`
2.  **Reviewers:** 최소 1명 이상의 동료 개발자 승인(Approve) 필수.
3.  **Checks:** CI(빌드/테스트)가 통과하지 못한 PR은 병합 불가.
4.  **Merge Strategy:** `Squash and Merge`를 사용하여 커밋 히스토리를 깔끔하게 유지한다.