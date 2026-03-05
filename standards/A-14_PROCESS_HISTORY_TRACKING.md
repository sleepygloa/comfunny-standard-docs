# A-14: Process History Tracking Standard

## 1. 개요 (Overview)
AI-Local-Worker, 백엔드 배치 등 시간이 오래 걸리거나 비동기적으로 처리되는 백그라운드 작업(Job)의 상태 및 세부 처리 이력을 통일된 규격으로 데이터베이스에 로깅하는 표준입니다.
이를 통해 Admin CMS 등에서 작업의 흐름, 소요 시간, 실패 원인 등을 일관된 UX 모달 창에서 추적하고 디버깅할 수 있습니다.

## 2. Firestore 로깅 표준 구조

모든 비동기 작업 문서는 상태코드(`status`) 외에 **`events`** 라는 배열(Array) 속성을 필수적으로 가져야 합니다.

### 2.1 `events` 객체 명세 (Event Object Spec)
`events` 배열에 추가되는 개별 이벤트 객체는 다음의 속성을 포함해야 합니다:

- `event` (String): 이벤트 고유 상태코드 (대문자 스네이크 케이스, 예: `JOB_STARTED`, `TTS_COMPLETED`, `UPLOAD_STARTED`, `JOB_FAILED`)
- `details` (String): 이벤트에 대한 구체적인 설명, 진행 상황, 또는 에러 메시지
- `timestamp` (Timestamp/Datetime): 이벤트가 발생한 정확한 UTC 시간 (Firestore 기준 Date/Timestamp)

### 2.2 예시 (Firestore JSON 형태)
```json
{
  "id": "job_12345",
  "title": "안녕하세요 테스트",
  "status": "PUBLISHED",
  "events": [
    {
      "event": "JOB_STARTED",
      "details": "AI Local Worker picked up the avatar job.",
      "timestamp": "2024-03-02T10:00:00Z"
    },
    {
      "event": "AVATAR_STARTED",
      "details": "Start generating Avatar video using SadTalker.",
      "timestamp": "2024-03-02T10:00:05Z"
    },
    {
      "event": "JOB_COMPLETED",
      "details": "Avatar video completely published.",
      "timestamp": "2024-03-02T10:05:12Z"
    }
  ]
}
```

## 3. 구현 가이드 (Implementation Guide)

### 3.1 Python (AI-Local-Worker)
Python의 Firestore SDK를 사용할 때는 `firestore.ArrayUnion` 내부에서 `firestore.SERVER_TIMESTAMP`를 직접 사용할 수 없는 제약이 있습니다. 따라서 `datetime` 패키지를 이용해 현재 UTC 시간을 직접 주입해야 합니다.

**[코드 예시]**
```python
from datetime import datetime, timezone
from firebase_admin import firestore

doc.reference.update({
    'status': 'PROCESSING_AI',
    'events': firestore.ArrayUnion([{
        'event': 'JOB_STARTED',
        'details': 'AI Local Worker picked up the job.',
        'timestamp': datetime.now(timezone.utc)
    }])
})
```

### 3.2 Node.js / TypeScript (Backend/CMS)
Node.js 관리자 환경에서 이벤트를 추가할 경우의 표준 형태입니다.

**[코드 예시]**
```typescript
import { getFirestore, FieldValue } from 'firebase-admin/firestore';

await db.collection('automated_shorts').doc(jobId).update({
  events: FieldValue.arrayUnion({
    event: 'REVIEW_COMPLETED',
    details: '관리자가 최종 검수를 완료했습니다.',
    timestamp: new Date()
  })
});
```

## 4. 프론트엔드 뷰어 UI (History Viewer)
Admin CMS에서 위 데이터를 랜더링할 때는 다음 규칙을 따릅니다:
1. `timestamp` 기준으로 이벤트를 오름차순 또는 내림차순으로 정렬합니다.
2. 타임라인(Timeline) 형식 또는 읽기 쉬운 목록 형태로 렌더링합니다.
3. `JOB_FAILED`와 같은 에러 이벤트는 붉은색 텍스트/뱃지로 경고 표시를 명확히 해야 합니다.
