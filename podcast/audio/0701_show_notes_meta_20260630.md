# 0701 MLSYS 论文简报：让 agent 自己管上下文，正确率翻倍
Audio: 10:07

> 本期从过去几天（06-25→06-30）的论文里合并打分挑出三篇，覆盖 token 经济、serving 系统、agent 上下文三块。
> 音频不口播 arXiv 编号，编号见下方链接。

## 内容时间戳
- 00:00 开场 · 今日三篇导览
- 01:18 ① EntMTP：用 entropy 动态调 multi-token prediction 深度（推理提速 / token 经济）
- 02:48 ② Festina：serverless LLM serving 的能耗优先联合调度（系统 / serving）
- 06:25 ③ VISTA：让 agent 看见并自己管理 context（agent 上下文 / 记忆）
- 09:29 收尾 · 三篇小结

## 本期主讲

### ① EntMTP · 推理提速 / token 经济 · 评级：夯
- **EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction** — arXiv 2606.27550
- 亮点：现有带 MTP 头的模型把 speculative decoding 的深度写死，与自然语言变化的 entropy 不匹配。EntMTP 是一个 training-free 的 scheduler，按实时 local entropy 在一组 pareto-optimal 的 tree 拓扑间切换——低 entropy 多草拟、高 entropy 保守。
- 数字：相比 Hydra 稳定快约 1.15×，相比 Medusa 峰值 1.36×（Humaneval / ShareGPT / GSM8k / Litbench）。

### ② Festina · serving 系统 / 能耗 · 评级：夯
- **Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs** — arXiv 2606.30391
- 亮点：serverless serving 让多模型共享 GPU，但也让能耗优化变难。Festina 是 power-aware 的 control plane，做 energy-first 决策，把 request placement、SM partitioning、GPU operating point 三层在 TTFT/TBT SLO 下联合调度（global 查表 + per-GPU phase-aware 本地调度 + SLO-aware migration 合并负载）。
- 数字：对比 4 个 SOTA serving 系统 + 1 个 DVFS，能耗最高降 56%，SLO 达成基本持平（2% 以内）。

### ③ VISTA · agent 上下文 / 记忆 · 评级：夯（接近顶级）
- **LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via a Proprioceptive Dashboard** — arXiv 2606.30005
- 亮点：长程 tool agent 的瓶颈是 context 顶到上限；论文指出模型对自己的 context 是 "proprioceptively blind"。VISTA 是 training-free、model-agnostic 的一层：把 working memory 表示成有类型、可寻址的 block，给一个显示每块 token 用量 / recency / access history 的 runtime dashboard，并把 block 归档成可完整恢复的 payload——假设是"管理能力本就 latent，缺的是接口"。
- 数字：LOCA-Bench / BrowseComp-Plus / GAIA 上跨百万→十万→一万 token 迁移；LOCA-Bench 上把 Gemini-3-Flash 从 22.7% 提到 50.7%，context 压力越大提升越多，且跨 backbone。ablation 确认 dashboard 本身才是关键。

## 制作元信息
- 文稿：双人对谈（Jeff 主讲系统 + Ada 提问）。
- 音频：本地 Qwen3-TTS 合成，约 10:07。
- 主持：Jeff（系统）· Ada（算法）。
- 口径：论文数字均据原文；arXiv 编号不口播、仅留链接。
