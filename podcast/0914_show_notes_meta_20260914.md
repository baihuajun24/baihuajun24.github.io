# 0914 Handoff Tax 特辑 · 换模型，为什么账单会重算？

音频：13:41 · 本地 Qwen3-TTS · 双主持 Jeff / Ada

> 大模型换小模型不一定省钱，小模型换大模型也不一定救得回来。多轮 Agent 真正需要路由的，是模型、交接接口、物理缓存状态与剩余任务长度的组合。

## 本期重点

- 一个 Agent 已用大模型工作四十轮，只剩简单收尾。换小模型的输出单价更低，但如果它无法复用大模型的 KV cache，就要重新预填充全部历史；继续用大模型反而可能更便宜。缓存过期、被驱逐或请求落到另一服务副本时，同一个决策又会翻转。
- The Handoff Tax 在 500 个 SWE-bench Verified 任务上发现：小→大时直接继承完整轨迹，两组模型只恢复高能力模型质量优势的 47% / 36%；Claude 组甚至比从第一步一直用大模型更贵。
- 交接接口有方向性。升级时删除小模型文字轨迹、保留工作区，质量恢复变好；降级时删除大模型轨迹，质量反而下降。强模型可能需要摆脱低质量推理，小模型却更依赖强模型留下的计划和验证事实。
- handoff 至少混合三种切换摩擦：语义、工作状态与缓存；另有一笔端到端策略总账——前任已消耗的 token、时间、工具调用和操作步数。
- 研究空白不是“没人算缓存”。已有论文按 cache read/write、模型切换和 TTL 计价；缺的是 same-model warm vs forced-cold 的受控实验，把重新预填充成本与跨模型残余效应分开。

## 时间线

- 00:00 降级为什么可能更贵：四十轮热缓存与完整重算
- 01:54 The Handoff Tax：升级救不回来，降级却可能成立
- 04:23 三种交接摩擦与一笔策略总账
- 06:28 三种都叫 routing、但所有权结构不同
- 08:32 缓存已经有人计价，因果问题为何仍未回答
- 10:25 最小实验：same-model warm / forced-cold
- 12:41 下一代 router：模型、接口与缓存迁移
- 13:26 收尾：路由器也是交接经理与缓存调度器

## 三种不同的 routing

1. Router-R1：中央策略模型不交权，只调用候选模型做顾问。
2. SWE-Router：弱模型先侦察；若需升级，强模型从原始问题重新开始，不续写弱模型的推理。
3. MTRouter：每一轮都可能换实际执行模型，新模型读取完整对话历史。

它们都叫 routing，却没有在测同一种 handoff。比较结论前，得先问任务所有权到底有没有转移。

## 推荐的最小实验

选择 30–50 个 SWE-bench Verified 任务、一个同系列大小模型对，在固定切换点双向运行：

1. same model + warm cache；
2. same model + forced-cold；
3. cross model + raw trace + cold；
4. cross model + compact trace + cold；
5. cross model + no textual trace + same working state + cold。

除了成功率与美元，还应报告缓存读写、预填充时间、首字延迟、墙钟时间和接手后的重复工作。策略对照至少包括 always-small、always-large、首轮选完固定、最多切一次与每轮自由切，并让动态策略共用同一个首轮 router。

真正想找到的是一条盈亏分界线：前缀多长、还剩多少轮、缓存存活概率多高时，切换的未来收益才能覆盖重新预填充和交接风险。

## 论文与资料

- The Handoff Tax: https://arxiv.org/abs/2608.24358
- Session-Aware Agentic Routing: https://vllm-project.github.io/2026/06/02/session-aware-agentic-routing.html
- Router-R1: https://arxiv.org/abs/2506.09033
- SWE-Router: https://arxiv.org/abs/2607.00053
- MTRouter: https://arxiv.org/abs/2604.23530
- Agent-as-a-Router: https://arxiv.org/abs/2606.22902
- TwinRouterBench: https://arxiv.org/abs/2605.18859
- Performance Drift from Model Switching: https://arxiv.org/abs/2603.03111
- Handoff Debt: https://arxiv.org/abs/2606.02875
- Cross-Model KV Cache Transfer: https://arxiv.org/abs/2608.03893

## 制作信息

本地 Qwen3-TTS 合成；Jeff=`uncle_fu`，Ada=`serena`，均未加速。所有论文数字均为作者自报；不同 benchmark、模型、价格与预算不可横向比较。Handoff Tax 已计入服务商的缓存读写价格；本期追问的是它尚未通过 warm/cold 对照做因果拆分。
