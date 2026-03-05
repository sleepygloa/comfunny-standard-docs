# [T-21] PRICING_TABLE

**용도**: 서비스 구독 결제, 요금제 안내, B2B 기업용 플랜 선택 등 고객에게 여러 옵션의 가격을 비교 제시할 때 사용하는 화면 템플릿입니다.

### 1. Template Structure (Pricing Page)

이 템플릿은 통상적으로 화면 중앙에 N개의 리스트 형태(Pricing Table)를 가로로 늘어놓는 형태로 구성됩니다.
강조하고자 하는 주력 요금제(예: Premium 플랜)에는 `highlight` 클래스를 주입하여 약간 더 크고 색상이 부각되도록 처리합니다.

```html
<!-- Pricing Container 래퍼 -->
<div class="pricing-container">
    <!-- ============================================
         1. Basic Plan (일반 요금제)
         ============================================ -->
    <!-- pricing-table 클래스는 각각 1개의 열(Column)에 해당 -->
    <ul class="pricing-table col-md-4">
        <li class="pricing-header">
            <!-- 요금제 명칭 -->
            <div class="price-title">BASIC</div>
            <!-- 요금 표시 -->
            <div class="price">
                <div class="price-figure">
                    <span class="price-number">Free</span>
                </div>
            </div>
            <!-- 간단한 요약 -->
            <div class="price-desc">퍼스널 사용자 및 테스트 목적에 적합합니다.</div>
        </li>
        <!-- 제공 기능 스펙 리스트 -->
        <li><i class="fa fa-user fa-fw me-2"></i> 1 User</li>
        <li><i class="fa fa-database fa-fw me-2"></i> 1GB Storage Space</li>
        <li><i class="fa fa-envelope fa-fw me-2"></i> Basic Support</li>
        <!-- 결제 진행 버튼 -->
        <li class="pricing-footer">
            <a href="javascript:;" class="btn btn-dark btn-theme">Sign Up Now</a>
        </li>
    </ul>

    <!-- ============================================
         2. Premium Plan (추천 요금제 - Highlight)
         ============================================ -->
    <!-- highlight 클래스는 높이/너비/그림자를 주변 요소보다 크게 나타냄 -->
    <!-- col-md-4는 부트스트랩 그리드로 한 줄에 3개 배치 시 사용 -->
    <ul class="pricing-table highlight col-md-4">
        <li class="pricing-header">
            <div class="price-title">PREMIUM</div>
            <div class="price">
                <div class="price-figure">
                    <span class="price-number">$9.99</span>
                    <span class="price-tenure">/mo</span>
                </div>
            </div>
            <div class="price-desc">전문적인 소상공인 사업체 운영에 가장 최적화되어 있습니다.</div>
        </li>
        <li><i class="fa fa-users fa-fw me-2"></i> Up to 10 Users</li>
        <li><i class="fa fa-database fa-fw me-2"></i> 50GB Storage Space</li>
        <li><i class="fa fa-envelope fa-fw me-2"></i> 24/7 Priority Support</li>
        <li class="pricing-footer">
            <a href="javascript:;" class="btn btn-theme">Sign Up Now</a>
        </li>
    </ul>

    <!-- ============================================
         3. Enterprise Plan (기업용 요금제)
         ============================================ -->
    <ul class="pricing-table col-md-4">
        <li class="pricing-header">
            <div class="price-title">ENTERPRISE</div>
            <div class="price">
                <div class="price-figure">
                    <span class="price-number">Custom</span>
                </div>
            </div>
            <div class="price-desc">초대형 엔터프라이즈 환경에서의 사용을 위한 맞춤 상담 플랜입니다.</div>
        </li>
        <li><i class="fa fa-users fa-fw me-2"></i> Unlimited Users</li>
        <li><i class="fa fa-database fa-fw me-2"></i> Unlimited Storage Space</li>
        <li><i class="fa fa-envelope fa-fw me-2"></i> Dedicated Service Engineer</li>
        <li class="pricing-footer">
            <a href="javascript:;" class="btn btn-dark btn-theme">Contact Us</a>
        </li>
    </ul>
</div>
```

### 2. Implementation Notes
- `pricing-container` 하위에 나오는 개별 요소 `ul.pricing-table`은 부트스트랩 컬럼(`col-*`) 사이즈를 사용해 줄바꿈 및 열 제어가 가능합니다. (예: 4개의 요금제를 보여주려면 `col-md-3`, 2개라면 `col-md-6`)
- `price-tenure`는 표시된 가격 문자열 뒤에 '/mo', '/year' 같은 기간 단위를 붙일 때 사용합니다.
