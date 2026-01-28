# 13. Batch System Standard (Init & Run Guide)

## 1. Quick Start Guide
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

### 1.2 VM Options (Required)
Spring Batch 5부터는 Job Name을 파라미터로 전달하거나, 특정 설정이 필요할 수 있습니다.
또한, 우리 시스템은 서버 식별을 위해 아래 옵션을 필수로 사용합니다.
```bash
-Dspring.profiles.active=local
-Dbatch.server.name=local-node-1
```

## 2. Code Pattern (Template)

### 2.1 Simple Job Configuration
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

## 3. Deployment Checklist
- [ ] `BATCH_JOB_INSTANCE` 등 메타 테이블이 DB에 생성되어 있는가? (옵션: `spring.batch.jdbc.initialize-schema=always` or `embedded`)
- [ ] Jenkins/Quartz 등 스케줄러에서 실행 명령어가 올바른가?
