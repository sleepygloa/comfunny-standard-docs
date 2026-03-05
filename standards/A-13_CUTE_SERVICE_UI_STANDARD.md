# [A-13] Cute Service UI Standard

## 1. 개요 (Overview)
본 문서는 B2C 서비스(MyVoice-TTS, 동화책 읽기, 영어 회화 등)에서 일관되게 사용되는 "아기자기한 서비스 UI (Cute Service UI)"의 디자인 시스템 및 구현 표준을 정의합니다. 
기존 Admin 중심의 딱딱하고 각진 레이아웃(Color Admin V3)에서 벗어나, 친근하고 따뜻하며 접근성이 높은 사용자 경험을 제공하는 것이 목적입니다.

---

## 2. 디자인 원칙 (Design Principles)
- **따뜻한 색감 (Warm & Pastel Colors):** 핑크, 피치, 민트, 스카이블루 계열의 파스텔톤을 주 테마로 사용합니다.
- **둥근 형태 (Rounded Shapes):** 모서리는 둥글게(Pill-shape, `rounded-2xl`, `rounded-[2rem]`, `rounded-full`) 처리하여 부드러운 인상을 줍니다.
- **부드러운 깊이감 (Soft Shadows & Glassmorphism):** 진하고 날카로운 그림자 대신 투명도 10~15% 수준의 은은하고 넓게 퍼지는 그림자를 사용하여 카드가 공중에 떠 있는 듯한 느낌을 줍니다. 
- **친근한 폰트 (Friendly Typography):** 무거운 고딕 대신 둥글둥글한 느낌의 폰트(Nunito, NanumSquareRound, Jua, Quicksand)를 사용합니다.
- **마이크로 애니메이션 (Playful Animations):** 마우스 호버 시 가볍게 위로 떠오르거나(`-translate-y-1`), 심장 박동처럼 부드럽게 뛰는 효과(`animate-pulse-soft`)를 활용합니다.

---

## 3. 글로벌 토큰 (Global Design Tokens)
`globals.css` 등에 다음의 색상을 CSS 변수 또는 Tailwind 테마로 선언하여 사용합니다.

```css
  --color-primary: #ff8fa3;    /* 핑크 메인 (버튼, 강조) */
  --color-secondary: #ffb3c6;  /* 핑크 서브 (보조 강조) */
  --color-accent: #ffccd5;     /* 매우 연한 핑크 (배경, 호버) */
  --color-bg-start: #fff0f3;   /* 바디 배경 그라디언트 시작 */
  --color-bg-end: #ffffff;     /* 바디 배경 그라디언트 끝 */
  --color-text-main: #4a4a4a;  /* 진한 웜 그레이 (제목, 본문) */
  --color-text-muted: #8b8b8b; /* 연한 웜 그레이 (설명, 흐린 텍스트) */
```

전역 바디 배경 및 폰트는 다음과 같이 설정합니다.
```css
body {
    @apply text-[#4a4a4a] antialiased bg-gradient-to-br from-[#fff0f3] to-white min-h-screen selection:bg-[#ffb3c6] selection:text-white;
    font-family: 'Nunito', 'NanumSquareRound', 'Jua', 'Quicksand', sans-serif;
}
```

---

## 4. UI 컴포넌트 표준 (UI Component Standards)

### 4.1 글로벌 유틸리티 클래스
Tailwind를 사용하여 자주 쓰이는 형태를 클래스로 만들어 사용합니다. (또는 직접 인라인으로 적용 가능)

#### 1) 큐트 카드 (`.card-cute`)
기본적인 컨테이너로 `.panel`을 대체합니다.
```css
.card-cute {
    @apply bg-white/80 backdrop-blur-md border border-white/40 shadow-[0_8px_30px_rgba(0,0,0,0.04)] rounded-[2rem] p-6 lg:p-8 transition-all duration-300;
}
.card-cute:hover {
    @apply shadow-[0_20px_40px_rgba(255,143,163,0.12)] -translate-y-1;
}
```

#### 2) 메인 버튼 (`.btn-cute-primary`)
저장, 완료, 중요 액션 등에 사용합니다.
```css
.btn-cute-primary {
    @apply bg-gradient-to-r from-[#ff8fa3] to-[#ffb3c6] text-white font-bold py-3 px-6 rounded-full shadow-[0_4px_15px_rgba(255,143,163,0.3)] transition-all duration-300 hover:shadow-[0_8px_25px_rgba(255,143,163,0.4)] hover:-translate-y-1;
}
```

#### 3) 보조 버튼 (`.btn-cute-secondary`)
취소, 돌아가기, 보조 액션 등에 사용합니다.
```css
.btn-cute-secondary {
    @apply bg-white text-[#ff8fa3] font-bold py-3 px-6 rounded-full border-2 border-[#ffb3c6] shadow-sm transition-all duration-300 hover:bg-[#fff0f3] hover:-translate-y-0.5;
}
```

#### 4) 큐트 인풋 창 (`.input-cute`)
텍스트, 드롭다운 입력 등에 사용합니다.
```css
.input-cute {
    @apply bg-white/60 border-2 border-transparent focus:border-[#ffb3c6] focus:bg-white rounded-2xl px-5 py-3 text-gray-700 outline-none transition-all duration-300 shadow-sm focus:shadow-[0_0_15px_rgba(255,143,163,0.15)];
}
```

#### 5) 글래스모피즘 네비게이션바 (`.glass-nav`)
상단 헤더(Header) 전용 스타일입니다. 화면 폭에 꽉 차지 않고, 컨텐츠 상단에 `알약 모양(Pill-shape)`으로 둥둥 떠 있는 것이 특징입니다.
```css
.glass-nav {
    @apply fixed top-4 left-1/2 -translate-x-1/2 w-[95%] max-w-5xl bg-white/70 backdrop-blur-lg border border-white/50 shadow-[0_8px_30px_rgba(0,0,0,0.06)] rounded-full z-50 transition-all duration-300;
}
```
> **참고:** `.glass-nav` 적용 후, 컨텐츠 영역 상단 간격을 `pt-24` ~ `pt-32` 정도로 확보해주어야 헤더에 내용이 가려지지 않습니다.

---

## 5. 레이아웃 구조체 (Layout Structure)
모든 컴포넌트 진입 시 `.animate-in .fade-in .slide-in-from-bottom-4` 클래스를 활용해 화면이 부드럽게 등장하도록 구성합니다.

```tsx
return (
    <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 pt-28">
        
        {/* 서비스 타이틀 */}
        <div className="text-center mb-10">
            <h1 className="text-4xl font-extrabold text-[#4a4a4a] tracking-tight mb-2 flex items-center justify-center gap-3">
                서비스 메인 타이틀 ✨
            </h1>
            <p className="text-[#8b8b8b] font-medium">따뜻하고 친절한 설명 텍스트를 적어줍니다.</p>
        </div>

        {/* 2단 구성 카드 레이아웃 */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
            <div className="card-cute h-full"> ... </div>
            <div className="card-cute h-full"> ... </div>
        </div>
    </div>
)
```

## 6. 적용 범위
- **MyVoice-TTS:** B2C 지향 (Studio, Dashboard 등) 적용 완료.
- **동화책 읽기 시스템:** 신규 디자인 구조를 이 문서 기준으로 설계
- **영어 회화 서비스:** 신규 디자인 구조를 이 문서 기준으로 설계

> **버전:** 1.0  
> **최근 갱신일:** 2026-02-28
