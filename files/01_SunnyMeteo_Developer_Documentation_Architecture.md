#请重构 SunnyMeteo 的 Mintlify 文档结构。

目标：按“引言+通用技术说明 + 产品 + 平台 + 数据字典”组织，而不是按接口组织。

#一级导航：
引言（Introduction）
通用技术说明（Integrations）
产品（Products）
平台（Platform）
数据字典（Reference）


##通用技术说明包含：
API
SDK
MCP
Map


##产品包含：
实况天气
小时预报
逐日预报
历史天气
灾害预警
空气质量
天文
海洋
地震
台风
气候

##平台包含：
地图平台
光伏气象 SaaS
风电气象 SaaS

##数据字典包含：
气象要素字典
单位说明
坐标系统
国家与城市编码
状态码


#要求：
创建完整目录结构。
创建所有 .mdx 占位页面。
更新 docs.json 的 navigation。
保持现有主题、Logo 和颜色不变。
未来规划页面标注 “Coming Soon”。
输出所有修改的文件列表。
