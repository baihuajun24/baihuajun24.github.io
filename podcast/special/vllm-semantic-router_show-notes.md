# 模型路由特辑 · 把每个 query 送到刚好够用的模型（公开版）

## 评论

不必每个请求都用最贵的模型——把每个 query 路由到"最便宜的够用模型"。这两年模型路由从学术的强/弱二选一，长成了生产级、可编程的 Mixture-of-Models 调度层。本期以开源项目 vLLM Semantic Router 为锚，串 RouteLLM、VDAR-Router、RouteBalance，讲清这条线要往哪走。

## 本期重点

主题是模型路由。为什么是现在：前沿闭源模型强但按 token 贵，开源模型很多任务已追平且能自部署；对那部分质量差收窄的请求还硬上最贵的模型就是烧钱，路由是在捡这笔白扔的钱。

起点 RouteLLM：学一个 router，用人类偏好数据在一强一弱两模型间按 query 动态选，把 cost-quality 推到更好前沿——很大一部分请求用弱模型就够，只要准确挑出需要强模型的少数，就能几乎不掉质量地省一大块成本（评级顶级，打下地基）。

前沿两条：VDAR-Router 指出路由多看表面语义/embedding、忽略 query 内在难度，改做难度感知的检索式路由；RouteBalance 指出 serving 里路由只看质量成本、负载均衡只看队列、两层各自为政，于是把二者融成一个在线分配、在具体实例上联合权衡质量/延迟/成本（热路径约 32ms@12req/s，13 实例/28 卡）——两篇均人上人。

锚点 vLLM Semantic Router（vllm-project/semantic-router，⭐5k+）：把这些拧成一个信号驱动、可编程的生产路由层——16 类信号（领域/复杂度/PII/越狱/工具/历史…）、12 种路由算法、以 Envoy ExtProc 挂在网关数据面；不止选模型，还判"该不该开思考模式"、带语义缓存、隐私与越狱护栏、结果感知的工具选择，把质量/成本/延迟/隐私/安全收进一个决策（评级顶级）。口径：其官网自报"闭源池追平前沿、8B 追回 235B 大部分性能省 96% 成本、延迟秒级→几十毫秒"均为项目自报、无第三方复现，按厂商口径听。快速一览：WISERouter（带工作负载预算约束、预算跨流量自适应）。

## 时间线

（最终音频 9:32，自然 TTS 语速）

- 00:00 开场 · 模型路由：送到刚好够用的模型
- 01:21 RouteLLM · 学一个路由器（顶级）
- 02:31 前沿两条 · VDAR-Router 懂难度 / RouteBalance 懂系统（人上人）
- 05:16 vLLM Semantic Router · 生产级 MoM 调度层（顶级）
- 07:59 口径 · 自报 benchmark 掂量着信 + WISERouter
- 09:21 收尾

## 论文与链接

- vLLM Semantic Router（项目）— github.com/vllm-project/semantic-router · vllm-sr.ai
- RouteLLM: Learning to Route LLMs with Preference Data — arXiv:2406.18665
- VDAR-Router: Adaptive LLM Routing via Verbalized Query Difficulty Analysis Retrieval — arXiv:2607.18098
- RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving — arXiv:2606.17949
- WISERouter: LLM Routing with Workload Budget Constraint — arXiv:2607.23765

## 制作元信息

- 文稿：话题特辑，以开源项目 vLLM Semantic Router 为锚、串近期路由论文；锚点来源为其 README + vllm-sr.ai 官网（2026-08-04）。
- 音频：9:32，自然 TTS 语速（loudnorm，无 atempo 加速）。
- 主持：Jeff（系统视角）/ Ada（提问者）。
- 口径：项目 benchmark 为官网自报、缺第三方复现（"8B 追平 235B、省 96%"按厂商口径听）；引用论文数字为各自摘要自报、口径不同不可横比；全程公开材料，与任何内部产品无关。
