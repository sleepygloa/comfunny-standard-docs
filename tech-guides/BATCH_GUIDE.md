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


---

<!-- DETAILED GUIDE START -->

# 13. Batch System Standard (Init & Run Guide - Detailed)

## 1. 빠른 시작 가이드 (Quick Start Guide)
신규 배치 프로젝트 생성 시 다음 절차를 따릅니다.

### 1.1 Dependencies (`build.gradle`)
```groovy
dependencies {
    // Spring Boot 3.x + Batch 5
    implementation 'org.springframework.boot:spring-boot-starter-batch'
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    
    // DB (MySQL/H2)
    runtimeOnly 'com.mysql:mysql-connector-j'
    
    // Test
    testImplementation 'org.springframework.batch:spring-batch-test'
}
```

### 1.2 VM Options (필수)
Spring Batch 5부터는 Job Name을 파라미터로 전달하거나, 특정 설정이 필요할 수 있습니다.
또한, 우리 시스템은 서버 식별을 위해 아래 옵션을 필수로 사용합니다.
```bash
-Dspring.profiles.active=local
-Dbatch.server.name=local-node-1
```

## 2. 코드 패턴 (Code Pattern)

### 2.1 간단한 Job 구성 (Simple Job Configuration)
```java
@Configuration
@RequiredArgsConstructor
public class SampleJobConfig {

    private final JobRepository jobRepository;
    private final PlatformTransactionManager transactionManager;

    @Bean
    public Job sampleJob(Step sampleStep) {
        return new JobBuilder("sampleJob", jobRepository)
                .start(sampleStep)
                .build();
    }

    @Bean
    public Step sampleStep() {
        return new StepBuilder("sampleStep", jobRepository)
                .tasklet((contribution, chunkContext) -> {
                    System.out.println("Hello, Batch!");
                    return RepeatStatus.FINISHED;
                }, transactionManager)
                .build();
    }
}
```

## 3. 배포 체크리스트 (Deployment Checklist)
- [ ] `BATCH_JOB_INSTANCE` 등 메타 테이블이 DB에 생성되어 있는가? (옵션: `spring.batch.jdbc.initialize-schema=always` 또는 `embedded`)
- [ ] Jenkins/Quartz 등 스케줄러에서 실행 명령어가 올바른가?
