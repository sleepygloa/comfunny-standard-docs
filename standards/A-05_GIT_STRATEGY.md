### 📂 7. `.docs/7_GIT_STRATEGY.md` (협업 및 버전 관리)
> **핵심:** "커밋 메시지만 봐도 어떤 기능인지 알 수 있어야 하며, `main` 브랜치는 언제나 배포 가능해야 한다."

```markdown
# [A-05] Git Collaboration Strategy

## 목차

<!-- toc -->

  * [A-05-7.1 Branching Model (Git-Flow Lite)](#a-05-71-branching-model-git-flow-lite)
  * [A-05-7.2 Commit Convention (Conventional Commits)](#a-05-72-commit-convention-conventional-commits)
  * [A-05-7.3 Pull Request (PR) Rules](#a-05-73-pull-request-pr-rules)
- [[A-05] Git Collaboration Strategy (Detailed Guide)](#a-05-git-collaboration-strategy-detailed-guide)
  * [A-05-1. 개요 (Overview)](#a-05-1-%EA%B0%9C%EC%9A%94-overview)
  * [A-05-2. Advanced Workflow](#a-05-2-advanced-workflow)
    + [A-05-2.1 Rebase vs Merge (Why Squash?)](#a-05-21-rebase-vs-merge-why-squash)
    + [A-05-2.2 Feature Branch 관리](#a-05-22-feature-branch-%EA%B4%80%EB%A6%AC)
  * [A-05-3. Commit Message Detail](#a-05-3-commit-message-detail)
    + [A-05-3.1 Scope의 중요성](#a-05-31-scope%EC%9D%98-%EC%A4%91%EC%9A%94%EC%84%B1)
    + [A-05-3.2 Body와 Footer 활용](#a-05-32-body%EC%99%80-footer-%ED%99%9C%EC%9A%A9)
  * [A-05-4. PR Etiquette](#a-05-4-pr-etiquette)
    + [A-05-4.1 Reviewer Guide](#a-05-41-reviewer-guide)
    + [A-05-4.2 Author Guide](#a-05-42-author-guide)

<!-- tocstop -->

## A-05-7.1 Branching Model (Git-Flow Lite)
대기업 표준에 맞춰 간소화된 Git-Flow를 사용한다.

- **`main` (Protected):** 운영 서버에 배포되는 브랜치. **직접 푸시 금지.** PR(Pull Request)로만 병합 가능.
- **`develop`:** 개발계 서버에 배포되는 통합 브랜치.
- **`feat/이슈번호-기능명`:** 개별 기능 개발 브랜치. (예: `feat/WMS-102-login-page`)
- **`fix/이슈번호-버그명`:** 버그 수정 브랜치.
- **`hotfix/날짜-내용`:** 운영 긴급 수정.

## A-05-7.2 Commit Convention (Conventional Commits)
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

## A-05-7.3 Pull Request (PR) Rules
1.  **Title:** `[FEAT] WMS-102 로그인 페이지 구현`
2.  **Reviewers:** 최소 1명 이상의 동료 개발자 승인(Approve) 필수.
3.  **Checks:** CI(빌드/테스트)가 통과하지 못한 PR은 병합 불가.
4.  **Merge Strategy:** `Squash and Merge`를 사용하여 커밋 히스토리를 깔끔하게 유지한다.

---

<!-- DETAILED GUIDE START -->

# [A-05] Git Collaboration Strategy (Detailed Guide)

## A-05-1. 개요 (Overview)
Git은 단순한 저장소가 아닙니다. **프로젝트의 역사(History)이자 의사소통 수단**입니다.
이 문서는 충돌 해결, 리베이스 전략, PR 에티켓 등 심화 주제를 다룹니다.

## A-05-2. Advanced Workflow

### A-05-2.1 Rebase vs Merge (Why Squash?)
우리는 **Squash and Merge** 전략을 사용하여 `main` 브랜치의 히스토리를 깔끔하게 유지합니다.

- **Squash Merge의 이점:**
    - 기능 개발 중 발생한 자잘한 커밋(`typo fix`, `wip`)들이 `main`에 남지 않습니다.
    - 롤백 시 PR 단위(`Revert PR`)로 깔끔하게 되돌릴 수 있습니다.

### A-05-2.2 Feature Branch 관리
- **브랜치 수명:** 기능 브랜치는 길어도 3일 이상 유지하지 않는 것을 권장합니다 (Long-lived feature branch 문제 방지).
- **동기화:** `develop` 브랜치가 업데이트되면 즉시 내 브랜치로 가져와야 충돌을 최소화할 수 있습니다.
    ```bash
    git checkout develop
    git pull origin develop
    git checkout feat/my-feature
    git merge develop  # 또는 git rebase develop (숙련자 권장)
    ```

## A-05-3. Commit Message Detail

### A-05-3.1 Scope의 중요성
`type(scope): subject` 형식에서 `scope`는 변경된 모듈을 명시합니다.

- **Good Scopes:**
    - `auth`: 인증 관련 (Login, JWT)
    - `order`: 주문 도메인
    - `ui`: 공통 UI 컴포넌트
    - `infra`: Docker, Jenkins 설정

### A-05-3.2 Body와 Footer 활용
복잡한 버그 수정이나 중요한 변경 사항은 Subject만으로 부족합니다.

```text
fix(auth): Fix JWT expiration time check

(Body)
기존 로직은 JWT 만료 시간을 UTC로 계산하지 않고 KST로 계산하여
서버 시간대 설정에 따라 9시간 오차가 발생하는 버그가 있었음.
Instant 타입을 사용하여 Timezone-safe하게 변경함.

(Footer)
Resolves: #102
See: https://github.com/jwt-lib/issues/55
```

## A-05-4. PR Etiquette

### A-05-4.1 Reviewer Guide
- **비난 금지:** "왜 이렇게 짰어요?" (X) -> "이 부분을 이렇게 고치면 성능상 이점이 있을 것 같은데 어떻게 생각하세요?" (O)
- **Blocking vs Non-blocking:** 반드시 수정해야 할 사항(`Request Changes`)과 권장 사항(`Comment`)을 명확히 구분합니다.

### A-05-4.2 Author Guide
- **Self Review:** PR을 올리기 전, 스스로 Files Changed 탭을 보며 불필요한 공백이나 주석이 없는지 확인합니다.
- **Description:** "로그인 수정" (X) -> "로그인 시 비밀번호 암호화 알고리즘을 SHA256에서 BCrypt로 변경" (O) 상세히 작성.
