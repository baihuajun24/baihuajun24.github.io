# 投机解码特辑 · 草稿模型，为什么追不动了？（公开版）

## 评论

投机解码的战场，正从"怎么验证"移到"草稿模型该长什么样"。When Hidden States Drift 把长程衰减重新读成一个信息问题——hidden state 是为下一个字优化的有损压缩，KV cache 才保留了完整的 per-token 信号；它诚实地报告 KV 复用当下换不来端到端加速，并拆出三个训练瓶颈。DFlash 用块扩散换掉自回归草稿，LongSpec 把 SD 撑到长上下文，正好是两条对症的破法。

## 本期重点

围绕投机解码的草稿模型设计，串四篇（含一篇上周旧作），连接它们的是同一个现象：long-range decay。

背景是 EAGLE-3 与 MTP 这一脉 hidden-state 草稿加 training-time test：好用，但草稿越往后猜、接受率掉得越快，而且上了 TTT 也消不掉。

主讲一，When Hidden States Drift（顶级）：把衰减归因为"hidden state 是 query-dependent 的有损压缩"——目标模型按当前 query 聚合 value，弱相关 token 权重接近零被抹掉；KV cache 保留原件，草稿可用自己的 query 重新 attend，把"信息恢复"难题换成"query 估计"难题。它用 KVShot 比了 hidden-only / KV-only / hybrid 三档：小规模平均接受长度 2.37→2.54、长程保持率升到 77.3%，但端到端 HF-MAT 只从 5.01 到 5.04（+0.6%）还多花 5–10% 草稿延迟——作者直言当前流程榨不出可用加速，并拆出三个瓶颈：浅草稿难估多层 query、草稿侧 KV 投影梯度稀疏、门控早期塌陷饿死 KV 支路。价值在框架与诚实度。

主讲二，DFlash（顶级）：既然自回归草稿本身是串行瓶颈，就用轻量 block diffusion 一次前向并行出一整块草稿，以目标模型的 context feature 为条件；六倍以上无损、最高比 EAGLE-3 再快 2.5×。更深草稿 + 块并行恰好命中前一篇诊断的头两个瓶颈。

主讲三，LongSpec（人上人）：把 SD 撑到长上下文——常数大小草稿 KV cache、位置索引修正短训长推错配、prefix 快算 + tree attention 聚合；最高比 Flash-Attention 基线 3.26×，QwQ 上 AIME24 长推理 2.25×。

收尾把这几篇跟上周的 Windowed-MTP 对上：一个治草稿 KV 的读成本，一个谈草稿信号的表达损失，同一个草稿步上的两种税。草稿模型的设计，正被"读什么信号 / 怎么训 / 撑到多长"三个方向同时拉扯。

## 时间线

（最终音频 10:14，自然 TTS 语速）

- 00:00 开场 · 草稿模型，为什么追不动了？
- 01:34 When Hidden States Drift（诊断）· 把长程衰减读成信息压缩问题
- 05:57 DFlash · 块扩散换掉自回归草稿
- 07:35 LongSpec · 把投机解码撑到长上下文
- 08:56 收尾 · 对照 Windowed-MTP，读成本 vs 信号损失
- 10:09 结束

## 论文与链接

- When Hidden States Drift: Can KV Caches Rescue Long-Range Speculative Decoding? — arXiv:2604.26412
- DFlash: Block Diffusion for Flash Speculative Decoding — arXiv:2602.06036
- LongSpec: Long-Context Lossless Speculative Decoding — arXiv:2502.17421
- EAGLE-3: Scaling up Inference Acceleration via Training-Time Test — arXiv:2503.01840
- HASS: Learning Harmonized Representations for Speculative Sampling — arXiv:2408.15766
- Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context — arXiv:2607.21535

## 制作元信息

- 文稿：33 turns（Jeff 17 / Ada 16），约 2,954 朗读字符；全部基于公开 arXiv 预印本，与任何评审无关。
- 音频：10:14，自然 TTS 语速（loudnorm，无 atempo 加速）。
- 主持：Jeff（系统视角）/ Ada（提问者）。
- 口径：Hidden States Drift 的 KV 复用"更抗衰减"为小规模 step-wise 结论、端到端当前无可用加速（作者自述）；各篇加速倍数为论文自报，硬件口径不同，不可横比；三档评级为对公开工作的评论。
