# AI 컨텍스트 & 프로젝트 참조

이 파일은 AI 어시스턴트와 CLI 도구가 프로젝트 컨텍스트를 이해하기 위한 진입점 역할을 합니다.
자세한 규칙 및 구성은 아래 링크된 문서를 참조하십시오.

## 문서 색인

1.  **아키텍처**: [docs/ARCHITECTURE_MVVM.md](docs/ARCHITECTURE_MVVM.md)
    *   MVVM 패턴, Riverpod, 레이어 책임, 디렉토리 구조.

2.  **환경**: [docs/ENVIRONMENT_AND_SETUP.md](docs/ENVIRONMENT_AND_SETUP.md)
    *   설정 가이드, 키, 빌드 구성, Java/Gradle 설정.

3.  **비즈니스 규칙**: [docs/BUSINESS_RULES_AND_LOGIC.md](docs/BUSINESS_RULES_AND_LOGIC.md)
    *   핵심 로직 (날짜, 동기화, AI), 요구사항 히스토리 (예: `ledgerDate`).

4.  **코딩 표준**: docs/CODING_STANDARDS.md
    *   스타일 가이드, 린터 규칙, 코드 섹션 패턴.

## 빠른 요약
*   **프로젝트**: 콤퍼니 가계부 (Flutter).
*   **상태**: Riverpod + StateNotifier.
*   **DB**: Isar (로컬) + Firestore (원격).
*   **핵심 규칙**: `ledgerDate`는 거래 타이밍의 진실 공급원(source of truth)입니다.
*   **스타일**: 엄격한 린터 규칙, 섹션 주석 필수.
