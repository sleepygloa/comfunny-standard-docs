# 문서 업데이트 가이드 (Documentation Update Guide)

이 가이드는 `.docs` 표준이 업데이트(버전 업)되었을 때의 대응 절차를 설명합니다.

## 트리거 (Trigger)
`.docs/README.md` 내의 **`Current Version`** 텍스트가 변경되었을 때 (예: v1.0.0 -> v1.1.0).

## AI 및 개발자 대응 프로세스

### 1. 변경 로그 확인 (Check Changelog)
`.docs/governance/DOCS_CHANGELOG.md`를 읽고 다음 내용을 식별합니다:
- **새로운 기능 (New Features):** 표준에 추가된 사항 (예: 새로운 기술 스택 추가).
- **주요 변경 사항 (Breaking Changes):** 코드 리팩토링이 필요한 규칙 변경 (예: 폴더 구조 변경).
- **Deprecated:** 더 이상 따르면 안 되는 규칙.

### 2. 프로젝트 문서 업데이트 (Update Project Documentation)
각 프로젝트(예: `comfunnyFamilyLedger`)에 대해 다음을 수행합니다:
1.  해당 프로젝트 루트의 메인 진입점 문서(예: `.project-docs/1_PROJECT_OVERVIEW.md` 또는 `README.md`)를 엽니다.
2.  `Applied Standard Version` 배지를 최신 버전으로 업데이트합니다.
    ```markdown
    > **Applied Standard Version:** v1.1.0
    ```
3.  **변경 사항 반영:**
    - 규칙이 변경되었다면(예: "이제 `src/model` 대신 `src/domain` 사용"), 코드베이스에 변경 사항을 일괄 적용하는 리팩토링(`/refactor`)을 수행합니다.
    - 새로운 필수 파일이 추가되었다면(예: 사내 규정에 `QA_GUIDE.md`가 필수가 됨), 해당 파일을 AI 봇을 통해 스캐닝 생성을 지시합니다.

## 버저닝 정책 (Versioning Scheme)
우리는 [Semantic Versioning](https://semver.org/)을 따릅니다:
- **Major (X.y.z):** 호환되지 않는 전면적인 아키텍처 변경 (구조 전면 개편, 기술 프레임워크 스택 교체).
- **Minor (x.Y.z):** 새로운 룰 확립, 기존 개발 방식과 하위 호환성 유지.
- **Patch (x.y.Z):** 가이드라인의 오타 수정, 구체화된 예시 추가, 설명 보강.
