# 0624 MLSYS 论文简报：JIT 持久内核检查点、学习搜索聚合与自压实 Agent
Audio: 14:44

## 内容时间戳
- 00:00 开场与导览
- 00:28 第一篇 · Concordia：JIT 编译持久化内核检查点（系统 / 容错推理）
- 05:30 第二篇 · SPIRAL：学习搜索与聚合（test-time scaling 算法）
- 09:11 第三篇 · Self-Compacting Language Model Agents（自压实 Agent，探索方向）
- 12:56 快速提及 · Draft-Agreement Routing、StateKV / Linear Scaling Video VLMs
- 14:13 收尾

## 本期主讲

### 1. systems_champion / Jeff / 夯
- **Concordia: JIT-Compiled Persistent-Kernel Checkpointing** (arxiv:2606.23521)
- 机构：待确认
- 亮点：JIT 编译持久化内核检查点，系统侧 serving/推理优化。
- Link: https://arxiv.org/abs/2606.23521

### 2. algorithm_champion / Ada / 夯
- **SPIRAL: Learning to Search and Aggregate** (arxiv:2606.23595)
- 机构：待确认
- 亮点：学习搜索与聚合，agent/算法侧。
- Link: https://arxiv.org/abs/2606.23595

### 3. exploratory_champion / Ada / 夯
- **Self-Compacting Language Model Agents** (arxiv:2606.23525)
- 机构：待确认
- 亮点：自压实语言模型 agent，探索性方向。
- Link: https://arxiv.org/abs/2606.23525

## 快速提及
- **Draft-Agreement Routing for Training-Free Speculative Decoding** — 免训练的投机解码草稿一致性路由，推理加速方向。
- **StateKV: Linear Scaling Video VLMs for Long Video Understanding** — 面向长视频理解、对 KV 状态做线性扩展压缩的 VLM。

## 制作元信息
- 论文召回：24h 窗口，286 fresh → 37 judged → 本期主讲 3 篇。
- Judge：gemini-3.5-flash（新方向 profile：token economy + 大小模型协同 + 多智能体，弱化 RL）。
- 卡片：glm-5.2（3/3 一次成功，html/pdf provenance）。
- 脚本：gemini-3.5-flash，32 turns。
- TTS：本地离线合成（Mac M4 Pro）。中文主播用 Higgs Audio v2（克隆音色）Jeff=`dylan` / Ada=`vivian`；英文论文标题改由专属英文音色 Qwen3-TTS `ryan` 朗读；语速约 279 字/分；arXiv 编号不口播，仅保留 ShowNotes 链接。

## 本期工作流改进
- 新方向 profile 持续生效（token economy / 大小模型协同 / 多智能体，弱化 RL）。
- digest + 播客候选合并为一文件推送（不再分两次 Feishu）。
- 自动排除历史 champion + special 已讲论文（本期 3 篇均无重复）。
- 音频改为本地离线合成（Higgs v2 + Qwen3-TTS 混音色）：中文主播 + 英文标题专属音色；arXiv 编号从口播移除、仅留 ShowNotes 链接。
