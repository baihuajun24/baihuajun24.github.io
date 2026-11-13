1006 MLSYS Weekly · 复用之前，先问什么还有效

音频：15:32 · 本地 Qwen3-TTS · 双主持 Jeff / Ada

Osprey：先建立可迁移的草稿模型底座，再适配目标。
MegaFlux：用专家复制分担热点，把额外通信藏进执行流水线。
Retire：旧执行撤权以后，仍可安全继承有效的计算状态。

章节顺序：问题与场景 → Osprey → MegaFlux → Retire → 证据边界 → 阅读建议。

论文：
https://arxiv.org/abs/2609.09338
https://arxiv.org/abs/2610.00671
https://arxiv.org/abs/2610.01160

结果口径：Osprey 的约18%来自指定单请求吞吐对照；MegaFlux 的1.45倍是层级前向，集成首token为1.13–1.26倍；Retire 的17.1%是指定受控条件下的中位配对降幅。三者不能相乘。
