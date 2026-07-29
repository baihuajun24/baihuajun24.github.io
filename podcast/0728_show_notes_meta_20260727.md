# 0728 MLSYS 论文简报：给大模型推理省钱的三招
Audio: 11:06

> 今天三篇，主题很集中——省钱三招：从三个正交维度砍大模型推理的成本。一篇砍投机解码里被忽视的 draft 全读 KV 税，一篇砍跨分词器蒸馏的浪费，一篇砍权重和激活里的冗余。

## 内容时间戳

- 00:00 开场 · 省钱三招
- 00:46 Windowed-MTP（英伟达）· 投机解码的 draft-KV 税
- 04:04 Cross-Tokenizer Distillation（中科院大学 / 快手）· 字节空间蒸馏
- 06:58 SPDP（首尔国立大学）· 静态+动态剪枝统一 GPU kernel
- 09:30 快速一览 · MoE 通信重叠 / 小模型编排 / HiKV
- 10:55 收尾

## 本期主讲

**1. Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context**（英伟达，arXiv:2607.21535）
投机解码假设 draft "几乎免费"，但内置的 MTP draft 头每猜一个 token 都要对整个 KV cache 做全注意力，读取量随上下文线性涨。当 target 转向便宜的 hybrid/linear attention，这个 draft 税就暴露出来，1M 上下文下几乎让每个解码步翻倍。解法极简：只给 draft attention 套一个 StreamingLLM 式滑窗加 sink，verify 仍全上下文——训练无关、drop-in、**构造上无损**（接受哪个 token 由全注意力 target 说了算）。单 decode step 成本降 28–44%，H100 复现是不投机的 2.43 倍，窗口外约 99% 的 draft KV 可回收显存。诚实度突出（区分构造无损 vs bf16 非确定性、单 seed 口径）；单作者 preprint。评级：人上人。

**2. Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization**（中科院大学 · 快手 KwaiKAT，arXiv:2607.22334）
想拿强的大模型蒸馏一个小模型，但两个模型分词器完全不同、token 对不上，没法做稠密蒸馏。洞察很漂亮：师生把同一句话切成不同 token，但都 decode 到同一个字节流。于是把老师监督搬到共享字节空间，把老师每个 token 的概率路由给"字节前缀正好是它的最长学生 token"，再聚合回学生词表——天然满足词表完整、字节对齐、质量守恒，且字节层面是精确解。六个数学/代码基准比最强跨分词器 baseline 高 3.7–6.6 分。还主动挖出并诊断了 whitespace collapse 失效模式（纯字节精确监督把代码通过率从 49% 打到 9%，一个只遮 3.5% 对齐行的 mask 就解决）。评级：顶级。

**3. Unified Static-Dynamic Pruning for Efficient LLM Inference (SPDP)**（首尔国立大学，arXiv:2607.21985）
静态剪枝离线定 mask 去权重、动态剪枝运行时跳激活，一个沿行、一个沿列，正交维度稀疏本可相乘，但数据格式一直不兼容。SPDP 设计一个统一的列主 Tiled-CBC 格式配两个分阶段 GPU kernel，第一次真正在 GPU 上把这两种稀疏叠起来跑。A10G/L4 上比 SpInfer 快 1.24–1.37×（最高 2.5×），同困惑度多吃 25% 稀疏；端到端平均 1.34×，受内存瓶颈与 Amdahl 上界限制。诚实报负结果（极端稀疏打不过 CSR、prefill 打不过 cuBLAS）。venue 口径：作者 arXiv 标注 VLDB 录用，但 PDF 用的是占位模板，按"作者标注"表述。评级：人上人。

## 快速一览

- Fine-grained Computation-Communication Overlap for Mixture-of-Experts（ICPP'26，arXiv:2607.19539）· tile 级信号量重叠 MoE 的两次 all-to-all 通信与专家计算，四卡端到端最高 2.64×。
- Small, Free, and Effective: Orchestrating Open-Weight SLMs for Malware Analysis（RAID，arXiv:2607.20216）· 一堆开源小模型编排能不能打过单个大模型？4B+8B 组合在恶意软件分析上做到 35.30%，反超最强前沿 baseline——route-to-small 的正面证据。
- HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration（arXiv:2607.22389）· 分层的、重要性感知的 KV cache 配硬件加速。

## 论文与链接
- Windowed-MTP — arXiv:2607.21535
- Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization — arXiv:2607.22334
- Unified Static-Dynamic Pruning for Efficient LLM Inference (SPDP) — arXiv:2607.21985

## 制作元信息
- 检索：watermark 自动补 07-24→07-27 四天跳过批次，406 篇 → 去重 316 → rough-rank 取 60 判。
- 评分：本地无 API key，走 Claude-as-judge（8 个并行子代理按 llm_judge rubric 评分）→ 回灌真实 pipeline，状态已更新。
- 三篇主讲全文 PDF 出卡定级（评级冻结）：BPM 顶级 / Windowed-MTP 人上人 / SPDP 人上人。
- 音频：本地合成（mlx-audio Qwen3-TTS-12Hz-1.7B-CustomVoice），双主持 Jeff（uncle_fu）/ Ada（serena），1.0x。
- 口径：Windowed-MTP 无损为构造性；BPM 师生为 2026 命名模型、数字无法独立复核；SPDP 的 VLDB 录用为作者标注、PDF 是占位模板。
