#!/usr/bin/env python3
"""Generate zh/en MDX copies from shared page metadata."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES: dict[str, dict[str, str]] = {
    "index": {
        "zh_title": "引言",
        "en_title": "Introduction",
        "zh_desc": "SunnyMeteo 开发者文档 — 气象、气候与环境数据 API",
        "en_desc": "SunnyMeteo developer documentation — weather, climate, and environmental data APIs",
    },
    "quickstart": {
        "zh_title": "快速开始",
        "en_title": "Quickstart",
        "zh_desc": "几分钟内完成第一次 SunnyMeteo API 调用",
        "en_desc": "Get your first SunnyMeteo API request working in minutes",
    },
    "integrations/api": {
        "zh_title": "REST 接口",
        "en_title": "REST API",
        "zh_desc": "SunnyMeteo REST API 概览、鉴权与约定",
        "en_desc": "SunnyMeteo REST API overview, authentication, and conventions",
        "zh_overview": "REST API 接入说明：基址、鉴权、限流、版本约定与通用请求/响应格式。",
        "en_overview": "REST API access: base URL, authentication, rate limits, versioning, and common request/response formats.",
    },
    "integrations/sdk": {
        "zh_title": "SDK",
        "en_title": "SDK",
        "zh_desc": "官方与社区 SDK 接入说明",
        "en_desc": "Official and community SDK integration guides",
        "zh_overview": "各语言 SDK 的安装、初始化与调用示例。",
        "en_overview": "Install, initialize, and call SunnyMeteo APIs with language SDKs.",
    },
    "integrations/mcp": {
        "zh_title": "MCP",
        "en_title": "MCP",
        "zh_desc": "Model Context Protocol 接入说明",
        "en_desc": "Model Context Protocol integration guide",
        "zh_overview": "在 AI 应用与 IDE 中通过 MCP 调用 SunnyMeteo 数据能力。",
        "en_overview": "Use SunnyMeteo data in AI apps and IDEs through MCP.",
    },
    "integrations/map": {
        "zh_title": "地图",
        "en_title": "Map",
        "zh_desc": "地图可视化与瓦片服务接入",
        "en_desc": "Map visualization and tile service integration",
        "zh_overview": "地图组件、图层与交互能力接入说明。",
        "en_overview": "Integrate map components, layers, and interactions.",
    },
    "products/current-weather": {
        "zh_title": "实况天气",
        "en_title": "Current weather",
        "zh_desc": "城市与经纬度实况天气数据",
        "en_desc": "Real-time weather conditions for cities and coordinates",
        "zh_overview": "城市级或经纬度实况：温度、湿度、风力、降水、天气现象等。",
        "en_overview": "City or coordinate-based conditions: temperature, humidity, wind, precipitation, and weather codes.",
    },
    "products/hourly-forecast": {
        "zh_title": "24 小时预报",
        "en_title": "Hourly forecast",
        "zh_desc": "逐小时天气预报",
        "en_desc": "Hour-by-hour weather forecasts",
        "zh_overview": "未来 24 小时逐小时温度、降水、风力等预报字段。",
        "en_overview": "Hourly temperature, precipitation, wind, and related fields for the next 24 hours.",
    },
    "products/daily-forecast": {
        "zh_title": "15 日预报",
        "en_title": "Daily forecast",
        "zh_desc": "逐日天气预报",
        "en_desc": "Multi-day daily weather forecasts",
        "zh_overview": "未来 15 日最高/最低温、天气现象、降水概率等。",
        "en_overview": "Up to 15 days of daily high/low temperature, conditions, and precipitation probability.",
    },
    "products/historical-weather": {
        "zh_title": "历史天气",
        "en_title": "Historical weather",
        "zh_desc": "历史气象数据查询与下载",
        "en_desc": "Historical weather data query and delivery",
        "zh_overview": "按区域与时间范围获取历史实况与再分析数据。",
        "en_overview": "Retrieve historical observations and reanalysis data by region and time range.",
    },
    "products/disaster-alerts": {
        "zh_title": "灾害预警",
        "en_title": "Disaster alerts",
        "zh_desc": "气象灾害与预警信息",
        "en_desc": "Meteorological disaster and alert information",
        "zh_overview": "官方预警、极端天气事件与相关元数据。",
        "en_overview": "Official alerts, extreme weather events, and related metadata.",
    },
    "products/air-quality": {
        "zh_title": "空气质量",
        "en_title": "Air quality",
        "zh_desc": "AQI 与污染物浓度",
        "en_desc": "AQI and pollutant concentrations",
        "zh_overview": "AQI、PM2.5、PM10 等空气质量指标与等级说明。",
        "en_overview": "AQI, PM2.5, PM10, and related air quality indices.",
    },
    "products/astronomy": {
        "zh_title": "天文",
        "en_title": "Astronomy",
        "zh_desc": "太阳、月亮与空间天气",
        "en_desc": "Sun, moon, and space weather data",
        "zh_overview": "日出日落、月相、空间天气等相关要素。",
        "en_overview": "Sunrise/sunset, moon phase, and space weather parameters.",
    },
    "products/ocean": {
        "zh_title": "海洋",
        "en_title": "Ocean",
        "zh_desc": "海温、海浪与洋流",
        "en_desc": "Sea temperature, waves, and currents",
        "zh_overview": "海洋环境要素与近海预报说明。",
        "en_overview": "Ocean parameters and coastal forecast documentation.",
    },
    "products/earthquake": {
        "zh_title": "地震",
        "en_title": "Earthquake",
        "zh_desc": "地震事件与震情信息",
        "en_desc": "Earthquake events and seismic information",
        "zh_overview": "国内外地震事件列表与字段说明。",
        "en_overview": "Domestic and global earthquake event listings and field definitions.",
    },
    "products/typhoon": {
        "zh_title": "台风",
        "en_title": "Typhoon",
        "zh_desc": "台风路径与强度预报",
        "en_desc": "Typhoon track and intensity forecasts",
        "zh_overview": "台风实况、路径预报与相关字段。",
        "en_overview": "Typhoon observations, track forecasts, and related fields.",
    },
    "products/climate": {
        "zh_title": "气候",
        "en_title": "Climate",
        "zh_desc": "气候统计与长期预估",
        "en_desc": "Climate statistics and long-range outlooks",
        "zh_overview": "历史气候统计与未来气候预估产品说明。",
        "en_overview": "Historical climate statistics and long-range outlook products.",
    },
    "platform/map-platform": {
        "zh_title": "地图平台",
        "en_title": "Map platform",
        "zh_desc": "SunnyMeteo 地图平台能力",
        "en_desc": "SunnyMeteo map platform capabilities",
        "zh_overview": "地图平台组件、图层管理与发布流程（规划中）。",
        "en_overview": "Map platform components, layer management, and publishing workflow (planned).",
    },
    "platform/solar-meteo-saas": {
        "zh_title": "光伏气象 SaaS",
        "en_title": "Solar meteo SaaS",
        "zh_desc": "新能源光伏行业气象服务",
        "en_desc": "Meteorological services for solar energy",
        "zh_overview": "光伏场站辐照、发电预估等行业能力（规划中）。",
        "en_overview": "Irradiance, generation estimates, and industry workflows for solar sites (planned).",
    },
    "platform/wind-meteo-saas": {
        "zh_title": "风电气象 SaaS",
        "en_title": "Wind meteo SaaS",
        "zh_desc": "新能源风电行业气象服务",
        "en_desc": "Meteorological services for wind energy",
        "zh_overview": "风电场风速、功率预估等行业能力（规划中）。",
        "en_overview": "Wind speed, power estimates, and industry workflows for wind farms (planned).",
    },
    "reference/weather-elements": {
        "zh_title": "气象要素",
        "en_title": "Weather elements",
        "zh_desc": "气象与环境参数字典",
        "en_desc": "Dictionary of weather and environmental parameters",
        "zh_overview": "各产品返回字段对应的气象要素含义、取值范围与示例。",
        "en_overview": "Meanings, ranges, and examples for weather and environmental fields returned by each product.",
    },
    "reference/units": {
        "zh_title": "单位",
        "en_title": "Units",
        "zh_desc": "API 返回单位约定",
        "en_desc": "Units used in API responses",
        "zh_overview": "温度、风速、降水等字段的默认单位与换算说明。",
        "en_overview": "Default units and conversions for temperature, wind, precipitation, and more.",
    },
    "reference/coordinate-systems": {
        "zh_title": "坐标系",
        "en_title": "Coordinate systems",
        "zh_desc": "经纬度与投影约定",
        "en_desc": "Latitude/longitude and projection conventions",
        "zh_overview": "WGS84 等坐标系及空间查询约定。",
        "en_overview": "WGS84 and other coordinate systems used in spatial queries.",
    },
    "reference/location-codes": {
        "zh_title": "位置编码",
        "en_title": "Location codes",
        "zh_desc": "城市 ID 与区域编码",
        "en_desc": "City IDs and region codes",
        "zh_overview": "城市 UID、行政编码与 POI 编码说明。",
        "en_overview": "City UIDs, administrative codes, and POI identifiers.",
    },
    "reference/status-codes": {
        "zh_title": "状态码",
        "en_title": "Status codes",
        "zh_desc": "HTTP 与业务错误码",
        "en_desc": "HTTP and business error codes",
        "zh_overview": "常见 HTTP 状态码与 API 业务错误码对照。",
        "en_overview": "Common HTTP status codes and SunnyMeteo business error codes.",
    },
}


def _related_block(locale: str) -> str:
    if locale == "zh":
        return """## 相关链接

- [状态码](/reference/status-codes)
- [API Explorer](https://api.sunnymeteo.com/docs)
"""
    return """## Related

- [Status codes](/reference/status-codes)
- [API Explorer](https://api.sunnymeteo.com/docs)
"""


def write_index(locale: str) -> None:
    meta = PAGES["index"]
    title = meta[f"{locale}_title"]
    desc = meta[f"{locale}_desc"]
    if locale == "zh":
        body = f"""---
title: "{title}"
description: "{desc}"
---

SunnyMeteo（小晴天科技）为开发者与企业提供**高精度气象、气候与环境数据**服务，支持 REST API、SDK、MCP 与地图能力。

## 基础信息

| 项目 | 说明 |
|------|------|
| 生产 API 基址 | `https://api.sunnymeteo.com` |
| 协议 | HTTPS + JSON（UTF-8） |
| 鉴权 | `X-API-Key` 请求头 |
| 稳定前缀 | `/v1/...` |

## 文档结构

文档按 **引言 → 通用技术说明 → 产品 → 平台 → 数据字典** 组织，便于按业务场景查阅。

<CardGroup cols={{2}}>
  <Card title="通用技术说明" icon="plug" href="/integrations/api">
    API、SDK、MCP、Map 接入方式
  </Card>
  <Card title="产品" icon="cloud-sun" href="/products/current-weather">
    实况、预报、历史、灾害、环境等产品能力
  </Card>
  <Card title="平台" icon="layer-group" href="/platform/map-platform">
    地图平台与行业 SaaS（规划中）
  </Card>
  <Card title="数据字典" icon="book" href="/reference/weather-elements">
    气象要素、单位、坐标、编码与状态码
  </Card>
</CardGroup>

## API Explorer

<Card title="Open API Explorer" icon="code" href="https://api.sunnymeteo.com/docs">
  在浏览器中测试 SunnyMeteo API
</Card>
"""
    else:
        body = f"""---
title: "{title}"
description: "{desc}"
---

SunnyMeteo provides **high-precision weather, climate, and environmental data** for developers and enterprises via REST API, SDK, MCP, and map capabilities.

## Essentials

| Item | Details |
|------|---------|
| Production API base | `https://api.sunnymeteo.com` |
| Protocol | HTTPS + JSON (UTF-8) |
| Authentication | `X-API-Key` header |
| Stable prefix | `/v1/...` |

## Documentation map

Content is organized as **Introduction → Integrations → Products → Platform → Reference** so you can browse by use case.

<CardGroup cols={{2}}>
  <Card title="Integrations" icon="plug" href="/integrations/api">
    API, SDK, MCP, and map integration guides
  </Card>
  <Card title="Products" icon="cloud-sun" href="/products/current-weather">
    Current, forecast, historical, alerts, and environmental data
  </Card>
  <Card title="Platform" icon="layer-group" href="/platform/map-platform">
    Map platform and industry SaaS (planned)
  </Card>
  <Card title="Reference" icon="book" href="/reference/weather-elements">
    Weather elements, units, coordinates, codes, and status codes
  </Card>
</CardGroup>

## API Explorer

<Card title="Open API Explorer" icon="code" href="https://api.sunnymeteo.com/docs">
  Test SunnyMeteo APIs in your browser
</Card>
"""
    (ROOT / locale / "index.mdx").write_text(body, encoding="utf-8")


def write_quickstart(locale: str) -> None:
    meta = PAGES["quickstart"]
    title = meta[f"{locale}_title"]
    desc = meta[f"{locale}_desc"]
    if locale == "zh":
        body = f"""---
title: "{title}"
description: "{desc}"
---

本页帮助你在几分钟内完成第一次 API 调用。

## 前置条件

- SunnyMeteo API Key（`X-API-Key`）
- 可访问 `https://api.sunnymeteo.com` 的网络环境
- 任意 HTTP 客户端（curl、Postman 或 SDK）

## 开始

<Steps>
  <Step title="获取 API Key">
    联系 SunnyMeteo 获取 API Key，或在控制台创建密钥（即将开放）。
  </Step>
  <Step title="发起第一次请求">
    使用城市 ID 或经纬度请求实况天气（示例路径，以 API Explorer 为准）：

    ```bash
    curl -s "https://api.sunnymeteo.com/v1/weather/condition?cityId=101010100" \\
      -H "X-API-Key: YOUR_API_KEY"
    ```
  </Step>
  <Step title="浏览产品文档">
    在左侧导航 **产品** 中按业务场景查阅数据说明与字段定义。
  </Step>
</Steps>

<Tip>
  需要联调？使用 [API Explorer](https://api.sunnymeteo.com/docs) 查看完整路径与参数。
</Tip>
"""
    else:
        body = f"""---
title: "{title}"
description: "{desc}"
---

This page walks you through your first SunnyMeteo API request.

## Prerequisites

- SunnyMeteo API key (`X-API-Key`)
- Network access to `https://api.sunnymeteo.com`
- Any HTTP client (curl, Postman, or an SDK)

## Get started

<Steps>
  <Step title="Obtain an API key">
    Contact SunnyMeteo for an API key, or create one in the console (coming soon).
  </Step>
  <Step title="Make your first request">
    Request current weather by city ID or coordinates (example path; see API Explorer for the latest spec):

    ```bash
    curl -s "https://api.sunnymeteo.com/v1/weather/condition?cityId=101010100" \\
      -H "X-API-Key: YOUR_API_KEY"
    ```
  </Step>
  <Step title="Explore products">
    Browse **Products** in the sidebar for field definitions by use case.
  </Step>
</Steps>

<Tip>
  Need to debug live requests? Use the [API Explorer](https://api.sunnymeteo.com/docs) for full paths and parameters.
</Tip>
"""
    (ROOT / locale / "quickstart.mdx").write_text(body, encoding="utf-8")


def write_page(locale: str, slug: str) -> None:
    if slug in ("index", "quickstart"):
        return
    meta = PAGES[slug]
    title = meta[f"{locale}_title"]
    desc = meta[f"{locale}_desc"]
    overview = meta[f"{locale}_overview"]
    note = (
        "本文档为占位页，完整内容即将发布。"
        if locale == "zh"
        else "This page is a placeholder. Full content is coming soon."
    )
    overview_heading = "概述" if locale == "zh" else "Overview"
    parts = [
        "---",
        f'title: "{title}"',
        f'description: "{desc}"',
        "---",
        "",
        "<Note>",
        f"  {note}",
        "</Note>",
        "",
        f"## {overview_heading}",
        "",
        overview,
        "",
    ]
    if slug == "integrations/api":
        parts.extend(["", _related_block(locale).rstrip(), ""])
    (ROOT / locale / f"{slug}.mdx").write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    for locale in ("zh", "en"):
        write_index(locale)
        write_quickstart(locale)
        for slug in PAGES:
            write_page(locale, slug)
    print(f"Wrote {len(PAGES) * 2} localized pages under {ROOT}/zh and {ROOT}/en")


if __name__ == "__main__":
    main()
