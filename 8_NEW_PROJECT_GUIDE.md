# 8. New Service Integration Guide

## 8.1 Overview
본 프로젝트는 **Monorepo** 구조이므로, 신규 서비스(예: Chat Server, Batch Server) 추가 시 기존 인프라에 녹여내야 한다.
독자적인 포트 사용이나 외부 노출은 금지하며, 반드시 **Gateway(Nginx)**를 통해야 한다.

## 8.2 AI Request Prompt (CLI 작업 시)
신규 서비스를 추가할 때, AI에게 아래 프롬프트를 입력하여 초기 구조를 잡는다.

> **[CLI Prompt]**
> "현재 프로젝트의 `MASTER_RULE.md`와 `docker-compose.yml`을 분석해줘.
> 이 아키텍처 규칙을 준수하면서 새로운 **[서비스명]** 프로젝트를 추가하려고 해.
>
> **요구사항:**
> 1. **서비스 목적:** (예: 실시간 알림 서버)
> 2. **기술 스택:** (예: Node.js + Socket.io)
> 3. **폴더명:** (예: `backend-noti`)
> 4. **내부 포트:** (예: 4000)
>
> **작업 요청:**
> - 프로젝트 기본 폴더 구조와 `Dockerfile`을 생성해줘.
> - 루트 `docker-compose.yml`에 서비스를 등록하고 `app-network`에 연결해줘.
> - `nginx/conf.d/default.conf`에 `/noti` 경로 라우팅을 추가해줘.
> - `PROJECT_RULES.md`의 기술 스택 섹션을 업데이트해줘."

## 8.3 Integration Checklist
신규 서비스 추가 후 반드시 아래 항목을 점검한다.

- [ ] **Folder:** 루트 바로 아래에 폴더가 생성되었는가? (Submodule 금지)
- **Docker:** `docker-compose up` 실행 시 컨테이너가 정상적으로 뜨는가?
- **Network:** 컨테이너 내부에서 `curl http://backend-api:8080` 호출이 되는가?
- **Gateway:** `http://localhost/신규서비스` 접속 시 Nginx가 라우팅을 잘 해주는가?
- **Docs:** `.docs/2_TECH_STACK.md`에 신규 기술 스택이 기록되었는가?