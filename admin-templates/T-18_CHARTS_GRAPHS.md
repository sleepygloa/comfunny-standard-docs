# [T-18] CHARTS_GRAPHS

**용도**: KPI 지표, 통계 자료 등 데이터를 시각적으로 표현하기 위해 사용하는 차트 패널 집합 템플릿입니다. Chart.js와 ApexCharts 구조를 모두 수용합니다.

### 1. Template Structure (Charts Panel)

이 템플릿은 하나의 페이지 내 여러 개의 차트 패널을 그리드 형태로 균형 있게 배치하는 레이아웃 구조를 제공합니다.

```html
<div class="row">
    <!-- ============================================
         1. Line Chart Widget (주요 트렌드 - 가로형)
         ============================================ -->
    <div class="col-xl-8">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">Monthly Revenue Trend</h4>
                <div class="panel-heading-btn">
                    <a href="javascript:;" class="btn btn-xs btn-icon btn-default" data-toggle="panel-expand"><i class="fa fa-expand"></i></a>
                </div>
            </div>
            <div class="panel-body">
                <div>
                    <!-- Chart.js 용 캔버스 또는 ApexChart용 div -->
                    <canvas id="line-chart" data-render="chart-js"></canvas>
                </div>
            </div>
        </div>
    </div>
    
    <!-- ============================================
         2. Doughnut Chart Widget (비중형 통계 - 정사각형)
         ============================================ -->
    <div class="col-xl-4">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">Sales by Region</h4>
            </div>
            <div class="panel-body text-center">
                <!-- ApexCharts 용 div -->
                <div id="apex-pie-chart" class="mb-3"></div>
                <!-- 하단 범례 추가 옵션 -->
                <div class="row text-center mt-4">
                    <div class="col-4">
                        <div class="fs-12px mb-1 fw-bold text-truncate">Seoul</div>
                        <div class="fs-16px mb-2 text-primary">54.3%</div>
                    </div>
                    <div class="col-4">
                        <div class="fs-12px mb-1 fw-bold text-truncate">Busan</div>
                        <div class="fs-16px mb-2 text-teal">21.5%</div>
                    </div>
                    <div class="col-4">
                        <div class="fs-12px mb-1 fw-bold text-truncate">Others</div>
                        <div class="fs-16px mb-2 text-warning">24.2%</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <!-- ============================================
         3. Bar Chart Widget (비교형)
         ============================================ -->
    <div class="col-lg-6">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">Weekly Traffic Pattern</h4>
            </div>
            <div class="panel-body">
                <div>
                    <canvas id="bar-chart" data-render="chart-js"></canvas>
                </div>
            </div>
        </div>
    </div>
    <!-- 4. Area Chart Widget -->
    <div class="col-lg-6">
        <div class="panel panel-inverse">
            <div class="panel-heading">
                <h4 class="panel-title">Growth Rate</h4>
            </div>
            <div class="panel-body">
                <div id="apex-area-chart"></div>
            </div>
        </div>
    </div>
</div>
```

### 2. Implementation Notes
- **라이브러리 혼용 방지**: 실전 프로젝트 시 가급적 `Chart.js` 또는 `ApexCharts` 중 팀 내 표준으로 지정된 하나의 시각화 라이브러리로 통일하십시오(T-01 기술 표준 문서 참고).
- 차트 캔버스 영역(`canvas` 또는 `div`)의 주변에 외부 마진/패딩을 없애고 꽉 차게 만들 때는 `panel-body p-0` 클래스를 사용하십시오.
