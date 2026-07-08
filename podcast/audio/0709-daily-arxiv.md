# 0709 MLSYS 论文简报：给推理省时间省成本

今天三篇，主题很集中——都是在"别浪费每一份计算、每一个 token"上做文章：把投机的思想搬到 KV
cache 的网络传输、把投机解码的草稿模型训练目标对齐推理、把模型路由和 KV 缓存复用耦合起来一起算账。

## 时间线

- 00:00 开场 · 三篇主题：给推理省时间省成本
- 00:17 Lynx（伦敦大学学院·华为）· 投机式 KV 传输
- 02:52 Spec-AUF（北京大学）· 草稿训练对齐推理
- 05:08 HyDRA（微软·GitHub）· 异构模型路由 + cache-aware
- 07:57 收束：别浪费每一份计算、每一个 token

## 本期论文

**1. Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference**（伦敦大学学院 · 华为，arXiv:2607.01831）
disaggregated 推理里，长上下文的大 KV cache 要跨网络从 prefill 传到 decode，decode 必须等传完才能开始，网络传输成了瓶颈。Lynx 挑战"KV cache 不可分割"的假设：按比特重要性拆成 Anchor（高位、先传）和 Residual（低位、后到）两股流，decode 收到 Anchor 就投机式开跑、Residual 到了再补精度校验。拿到 INT4 级传输延迟、精度却匹配高精度量化（比 SOTA 高 5.1 个百分点），TTFT 与到第 32 个 token 的时间最多降 30.5%。

**2. Spec-AUF: Accept-Until-Fail Training under Train-Inference Misalignment for Masked Block Drafters**（北京大学，arXiv:2607.01893）
block 草稿模型一次并行猜一整块，却用整块 cross-entropy 监督每个位置——而推理时 verifier 从左到右验、第一个被拒之后全丢，训练与推理错配。之前用加权衰减打补丁仍不够（靠后位置的价值是"有条件的"）。Spec-AUF 用 teacher-forcing 只监督"会被接受的前缀"（Accept-Until-Fail），把 verifier 的左到右接受契约写进训练目标。Qwen3-8B、DFlash/Domino 两种草稿、六个 benchmark 上，平均接受长度稳定提升——接受越长，投机加速比越高。

**3. HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools**（微软 · GitHub，arXiv:2605.17106）
GitHub Copilot Auto 背后的路由器。不预测"用哪个模型"，而是预测 query 在四维能力（推理/代码生成/调试/工具使用）上各需多强（ModernBERT + 4 个 sigmoid 头），再与配置化模型档案做 shortfall matching，选满足需求里最便宜的——与模型身份解耦，换目录只改配置不重训。亮点是 cache-aware 粘滞路由：每轮切模型会让 prompt 缓存（省九成）失效，所以只在缓存本会失效的边界（首轮、compaction、总结后）才重路由。同池对比与 OpenRouter Auto 解题率打平但省成本 3.3×，路由器 CPU 上 55ms。

## 论文与链接
- Lynx — arXiv:2607.01831
- Spec-AUF — arXiv:2607.01893
- HyDRA — arXiv:2605.17106

## 制作元信息
- 检索：pool 07-03→07-08 六天（hours_back 168，gap-pool CAP 500），抓取 1671 篇 → 去重去历史 1309 → rough-rank 取 60 + backlog 9 判。
- 评分：本地无 API key，走 Claude-as-judge（9 个并行子代理按 llm_judge rubric 评分）→ 回灌真实 pipeline，状态已更新。
- 三篇为 PI 从判后 shortlist 中钦定（Lynx + Spec-AUF + HyDRA，HyDRA 系 PI 本周 inbound 从召回池命中）。
- 音频：本地合成（mlx-audio Qwen3-TTS-12Hz-1.7B-CustomVoice），双主持 小白（本人克隆声）/ Ada（serena）。
- 口径：GRPO/路由等数字均对各自 PDF 首页/正文复核。

## 本期工作流改进
给本地 TTS 合成加了 AR-runaway 长度守卫（每段时长上限 + 重试、成品逐段扫 chars/sec），并把成因与做法写进 daily-paper-podcast skill——起因是 07-07 A3C 特辑一段 72 字被模型"停不下来"生成成 122.8s 乱码。
