# 13. Batch System Standard

## 13.1 Overview
배치(Batch) 시스템은 대용량 데이터를 안정적으로 처리하기 위한 필수 컴포넌트입니다.
본 표준은 **Spring Batch 5** (Spring Boot 3.x) 버전을 기준으로 작성되었습니다.

---

## 13.2 System Architecture
- **Framework:** Spring Batch 5.0+ (Boot 3.1+)
- **Execution Mode:**
    - **Tasklet:** 단순 작업, 파일 처리, Stored Procedure 호출 등.
    - **Chunk-Oriented:** 대용량 데이터 Read -> Process -> Write 구조.
- **Repository:** `JobRepository`는 DB(MySQL)를 사용하며, 트랜잭션 관리를 위해 필수입니다.

---

## 13.3 Package Structure
`egflexs-if-batch`의 구조를 표준으로 채택합니다.

```text
com.comfunny.batch/
├── config/             # Batch Config (Async, ThreadPool)
├── job/                # Job Configuration (JobBuilder)
├── step/               # Step Configuration (StepBuilder)
├── task/               # Tasklet & ItemWriter/Processor/Reader 구현체
└── domain/             # Batch 전용 DTO/Entity
```

---

## 13.4 Naming Convention
| Component | Postfix | Example |
| :--- | :--- | :--- |
| **Job Config** | `JobConfig` | `SettlementJobConfig.java` |
| **Step Config** | `StepConfig` | `SettlementStepConfig.java` |
| **Tasklet** | `Tasklet` | `FileDeleteTasklet.java` |
| **Job Name** | `Job` | `settlementJob` |
| **Step Name** | `Step` | `fileDeleteStep` |
