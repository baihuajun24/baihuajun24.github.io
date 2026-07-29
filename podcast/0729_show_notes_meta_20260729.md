# 0729 MLSYS 论文简报：长上下文 KV 的三种省法
Audio: 09:57

> 长上下文推理里越堆越大的 KV cache 怎么省着用？三篇给了三种打法：把每页压成小摘要、把稀疏注意力的选择摊薄、把驱逐重新想成一个估计问题。压、挑、扔。

## 内容时间戳

- 00:00 开场 · 长上下文 KV 的三种省法
- 00:44 LOCKS（单作者预印本）· 页级低秩摘要，只读 top 页
- 03:34 PIVOT（腾讯）· 稀疏注意力 indexer 的 query 轴摊销
- 05:53 Eviction as Estimation（北卡教堂山 / 纽约大学）· 把驱逐重述为估计
- 08:42 快速一览 · Kimi K3 / Agentic Context Management / Agentic CPU-GPU Scheduling
- 09:52 收尾

## 本期主讲

**1. LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding**（单作者预印本，无机构署名，arXiv:2607.24555）
长上下文推理的瓶颈是 KV cache 的读带宽——cache 常驻显存，但每个 decode step 得整段全读。想稀疏地只读一部分又有死结：精确挑 top key 就得先读每个 key。LOCKS 给每页配一个常驻的低秩谱摘要（对该页做特征分解、留 rank-8，约占本页 KV 的十分之一），选择时只读摘要就能重构每页注意力质量、只挑 top 页去真读，全程不碰候选 key/value。还证了一个结构性不可能结论：任何跨页共享的固定投影必然对某些页自己独有的方向瞎掉。十万以上上下文、预算 2048 下平均分追平满 cache；一百万上下文每 token 延迟低 2.0×、每步读字节少约 9.8×；作为免训练插件挂进原版 vLLM 并跑进完整 CUDA graph。诚实点：保真度理论界仅对未量化摘要成立，量化版靠实测；效率优势集中在极长上下文/大 batch，短上下文仅持平。评级：夯。

**2. PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention**（腾讯，arXiv:2607.24593）
DSA 这类 token 级稀疏注意力让下游算得便宜了，但瓶颈转移到 indexer——为每个 query 从整段前缀挑 top-k，每层仍是平方复杂度（文中引用：200K 时约占 prefill 端到端延迟 81%，注：该数字引自 IndexCache、非本文实测）。观察：相邻 query 的 top-k 重叠高达 0.8–0.9。于是把一组 query 按均值池化成一个代理 query 只扫一次前缀拿候选集；快变体直接把候选分给全组，精度版让每个 query 在小候选集内再各自精挑。全程不丢 token、下游仍看到完整前缀，只共享"挑选"这一步。indexer 层最高约 4×、端到端最高 1.6×，精度追平稠密；诚实报边界（极长上下文快变体掉点、短序列精度版更慢并加护栏回退稠密）。评级：顶级。

**3. Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory**（北卡罗来纳大学教堂山分校 / 纽约大学，arXiv:2607.24667）
把 KV 驱逐重述为估计问题：驱逐时你其实在猜这个 item 未来还有没有用，而有用是未来才揭晓的。借估计理论的三种姿态——过滤估计现在、预测估计未来、平滑等几步回看过去——发现现有方法都挤在"到达即决定"（H=0），Belady 最优在 H→∞，中间的 fixed-lag smoothing 是空白。只要把决策延迟有界的 H 步，不可观测的未来就变成可测量的近期使用。提出的训练无关策略本质是给 H2O 加一个"预测正确才算数"的权重。难得的诚实：它明说自己不是新 SOTA——独立 benchmark 上仅 H2O 级，流式多轮里甚至同时输给 H2O 和 SnapKV，对 H2O 一胜一平三负。价值在框架，和一张"何时测量胜过累积"的诚实地图。评级：人上人。

## 快速一览

- Kimi K3: Open Frontier Intelligence（arXiv:2607.24653）· 开源前沿大模型报告，MoE 架构，对做推理 infra 有参考价值。
- Agentic Context Management: Solving Agent Memory and Cost（arXiv:2607.21503）· 把 agent 的记忆与成本当统一问题来管，思路对味但较早期。
- Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads（arXiv:2607.22242）· 给异构 AI 负载做 agent 化的 CPU/GPU 调度。

## 论文与链接
- LOCKS — arXiv:2607.24555
- PIVOT — arXiv:2607.24593
- Eviction as Estimation — arXiv:2607.24667

## 制作元信息
- 检索：薄批次日（07-29），watermark 补 07-28 + 部分 07-29，87 篇 → 判 60（Claude-as-judge, 8 子代理）→ 6 入选。
- 三篇主讲全文 PDF 出卡定级（评级冻结）：LOCKS 夯 / PIVOT 顶级 / Eviction as Estimation 人上人。
- 音频：本地合成（mlx-audio Qwen3-TTS-12Hz-1.7B-CustomVoice），双主持 Jeff（uncle_fu）/ Ada（serena），1.0x。
- 口径：LOCKS 保真度界仅对未量化成立；PIVOT 的"占八成延迟"为引用他人；Eviction as Estimation 明确非 SOTA。
