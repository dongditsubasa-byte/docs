# SunnyMeteo Developer Docs (Mintlify)

生产地址：

- 中文：**https://docs.sunnymeteo.com/zh**
- 英文：**https://docs.sunnymeteo.com/en**

SunnyMeteo 开发者文档按 **引言 → 通用技术说明 → 产品 → 平台 → 数据字典** 组织，中英文各一套 MDX，路径结构一致。

## 目录结构

```
docs/
├── docs.json                 # Mintlify 配置（navigation.languages）
├── zh/                       # 中文文档
│   ├── index.mdx
│   ├── quickstart.mdx
│   ├── integrations/
│   ├── products/
│   ├── platform/
│   └── reference/
├── en/                       # 英文文档
│   ├── index.mdx
│   ├── quickstart.mdx
│   └── …（与 zh/ 同结构）
├── scripts/localize_mdx.py   # 批量生成/更新双语占位页
├── custom.css                # 淡蓝背景 / 侧栏紧凑 / 隐藏滚动条
├── sidebar-layout.js         # 侧栏折叠箭头右对齐（配合 custom.css）
└── website-link.js           # 文档站 → 主站语言回跳
```

## 本地预览

```bash
npm i -g mint
cd docs
mint dev
```

访问 `http://localhost:3000`，Mintlify 会显示语言切换器。

## 更新文案

1. 编辑 `scripts/localize_mdx.py` 中的 `PAGES` 元数据，或手动改 `zh/`、`en/` 下对应 MDX
2. 运行 `python3 scripts/localize_mdx.py` 可批量同步占位页
3. Push 到 Mintlify 连接的 Git 仓库后自动发布

## 品牌与侧栏

- 主题色见 `docs.json`（primary `#3486CF`）
- 侧栏采用**嵌套分组**（`expanded` 控制折叠，参考 [Xweather Weather API](https://www.xweather.com/docs/weather-api)）
- 视觉微调见 `custom.css`（淡蓝背景、紧凑行距、隐藏滚动条）

## 主站链接

官网 `sunnymeteo_web` 通过 `docsBaseUrl(locale)` 跳转：

- 中文主站 → `https://docs.sunnymeteo.com/zh`
- 英文主站 → `https://docs.sunnymeteo.com/en`

文档站返回主站（点击 logo / 官网 / Footer 官网图标）：

- 中文文档 → `https://www.sunnymeteo.com/zh/`
- 英文文档 → `https://www.sunnymeteo.com/en/`

实现方式：`docs.json` 中 `logo.href` + 各语言 `navbar.links` / `footer.socials.website`，并由根目录 `website-link.js` 按当前路径 `/zh` 或 `/en` 动态修正链接，同时写入主站语言 Cookie `sunnymeteo_locale`。
