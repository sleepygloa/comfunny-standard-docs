# 기존 소스 분석 및 문서 역공학 워크플로우 (Legacy Analysis)

> **Trigger:** "레거시 문서화", "기존 소스 분석", "Analyze Source"

이 워크플로우는 소스 코드만 덩그러니 존재하고 문서(`A-09`에서 요구하는 최소 6개 필수 문서)가 누락되거나 심하게 아웃데이트된 프로젝트의 아키텍처를 AI Agent가 역공학하여 현행화하는 지침입니다.

## 1. 프로젝트 스캐닝 및 메타데이터 파악 (Reconnaissance)

- [ ] **패키지 매니저 판독**: 가장 먼저 `package.json`, `pubspec.yaml`, `build.gradle` 등의 핵심 메타(Meta) 파일을 `view_file` 도구로 스캐닝하여 사용 중인 프레임워크(Flutter, React, Spring Boot 등) 뼈대를 알아냅니다.
- [ ] **진입점(Entry Point) 추적**: `list_dir`을 기반으로 `main.dart`, `App.js`, `index.js`, `Application.java` 등의 최초 로드 파일을 파악합니다. 이를 통해 라우팅/의존성 주입(DI) 트리를 탐색할 방향을 잡습니다.
- [ ] **문서/소스 갭(Gap) 검증**: 기존에 작성되어 있던 `.project-docs/1_PROJECT_OVERVIEW.md`의 [현재 구현된 기능]과 실제 코드를 대조해 미구현/과구현 여부를 파악합니다.

## 2. 레이어 및 핵심 모듈 딥 다이브 (Deep Dive)

- [ ] **전역 상태/통신 로직 스캔**: Redux, Riverpod, Vuex, Bloc 등의 스토어/프로바이더 코드를 스캔합니다(예: `app_providers.dart`). 앱의 심장부가 되는 글로벌 상태 전파 구간을 파악하여 구조의 복잡도를 점검합니다.
- [ ] **API 연동부 점검**: 백엔드 또는 Firebase 스키마, OpenAPI 연동부를 점검(`sync_..._repository.dart`)하여 어떤 테이블/문서 구조를 가졌고 어떻게 ORM(Isar, Prisma, JPA)에 바인딩되는지 Mapping 규칙을 캡처해야 합니다.
- [ ] **UI/UX 역변환 설계도 스케치**: 프론트엔드 코드(`Scaffold`, `Component` 등)를 읽고 이를 "버튼 클릭 시 C 로직이 돌아가 D 상태를 E 뷰에 모달로 띄움" 같은 서사형 요구사항 명세로 역-번역(Reverse Translate)합니다.

## 3. 완전한 문서화 (Documentation Generation)

위의 분석이 끝나면, 조사된 결과를 아래 `.project-docs/` 필수 파일 포맷에 맞춰 일괄 업데이트(또는 신규 생성)합니다.

- [ ] **`REQUIREMENTS.md` 생명 불어넣기**: 파악된 UI/UX 동작, 폼 제출 및 유효성 검증, 오프라인 모드 등의 구체적 제약(엣지 케이스)을 텍스트 기반의 **상세 화면 설계서** 수준으로 끌어올립니다.
- [ ] **`ARCHITECTURE.md` 작성**: MVC, MVVM, Clean Architecture 등 사용 중인 패턴을 명시하고 디렉토리별 역할군(Presentation, Domain 등)을 정의합니다.
- [ ] **`BUSINESS_RULES.md` 정리**: 예를 들어 '가계부의 정산 시작일은 기본 1일이지만 -1이면 말일이다'라는 식의 핵심 도메인 로직, 기획 정책, 동기화 룰 등을 따로 빼내어 정리합니다.

## 4. 인프라 정리 및 리포팅 (Reporting)
- [ ] **버전/날짜 갱신**: 보완된 모든 문서의 마지막에 `> 최종 스캔 작성일: YYYY-MM-DD` 식별자를 갱신합니다.
- [ ] **코드 리뷰(/code-review) 선행 작업 완수**: 레거시 역공학이 끝나면 코드 수정(`refactor`) 전에 이 지식들을 Context로 로드해 데일리 스크럼 태스크를 이어나갑니다.
