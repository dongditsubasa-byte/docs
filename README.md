# SunnyMeteo Developer Docs (Mintlify)

生产地址：**https://docs.sunnymeteo.com**

SunnyMeteo 开发者文档，按 **引言 → 通用技术说明 → 产品 → 平台 → 数据字典** 组织。

## 目录结构

```
docs/
├── docs.json                 # Mintlify 配置与导航
├── index.mdx                 # Introduction / 引言
├── quickstart.mdx            # 快速开始
├── integrations/             # Integrations / 通用技术说明
│   ├── api.mdx
│   ├── sdk.mdx
│   ├── mcp.mdx
│   └── map.mdx
├── products/                 # Products / 产品
│   ├── current-weather.mdx
│   ├── hourly-forecast.mdx
│   ├── daily-forecast.mdx
│   ├── historical-weather.mdx
│   ├── disaster-alerts.mdx
│   ├── air-quality.mdx
│   ├── astronomy.mdx
│   ├── ocean.mdx
│   ├── earthquake.mdx
│   ├── typhoon.mdx
│   └── climate.mdx
├── platform/                 # Platform / 平台 (Coming Soon)
│   ├── map-platform.mdx
│   ├── solar-meteo-saas.mdx
│   └── wind-meteo-saas.mdx
└── reference/                # Reference / 数据字典
    ├── weather-elements.mdx
    ├── units.mdx
    ├── coordinate-systems.mdx
    ├── location-codes.mdx
    └── status-codes.mdx
```

## 本地预览

```bash
npm i -g mint
cd docs
mint dev
```

访问 `http://localhost:3000`。

## 品牌

主题色与 Logo 见 `docs.json`（primary `#3486CF`，Logo 位于 `logo/`）。
