# 11. Documentation Standard (Detailed Guide)

## 1. Changelog Convention
**"무엇이 바뀌었는지"**를 명확히 기록해야 배포 시 리스크를 줄일 수 있습니다.
[Keep a Changelog](https://keepachangelog.com/ko/1.0.0/) 형식을 따릅니다.

### 1.1 Format Example
```markdown
# Changelog

## [1.2.0] - 2024-03-20
### Added
- 사용자 소셜 로그인 기능 추가 (Kakao, Google)
- 마이페이지 프로필 수정 API

### Changed
- 로그인 토큰 만료 시간을 1시간에서 24시간으로 변경
- `PaymentService` 로직 리팩토링 (트랜잭션 분리)

### Fixed
- 결제 취소 시 포인트가 환불되지 않던 버그 수정
- 간헐적으로 발생하던 Redis Connection Timeout 해결
```

## 2. README Best Practices
- **Badge 활용:** 프로젝트의 상태(Build Status, Coverage, Version)를 시각적으로 보여줍니다.
- **Prerequisites:** 실행을 위해 필요한 사전 요구사항(Java 17 설치, Docker 실행 등)을 명시합니다.
- **Diagrams:** 복잡한 아키텍처는 Mermaid 다이어그램을 삽입하여 이해를 돕습니다.

## 3. Documentation as Code
- `README.md`도 코드입니다.
- 오타 수정, 버전 업데이트 등도 PR을 통해 리뷰 받고 Merge 되어야 합니다.
- Wiki(Confluence)보다는 Repository 내부의 마크다운 문서를 1순위(SSOT)로 유지하십시오.
