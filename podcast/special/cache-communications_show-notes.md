# 缓存通信：从 KV 复用到模型间直连

## 评论

把围绕 KV cache 的一批 2025–2026 系统/算法工作连成一条线：复用（让非前缀、不连续的缓存也能拼接）→ 放置（HBM/CXL/host/PIM 的层级权衡）→ RAG/Agent 工作负载 → 缓存即通信（模型间直接传 KV 语义而非文本）→ 安全。读这条线的方法论：把缓存当成 serving 的一等资源，而不是推理实现细节。

## 本期重点

这是一期缓存通信主题特辑，主播 Jeff（systems，主讲）+ Ada（algorithm，提问）。中心问题只有一个：KV cache 能不能被复用、被高效搬运、甚至在不同模型之间直接共享？我们从 CacheBlend 的「选择性重算 + 融合」讲起，说明为什么生产环境里传统 prefix cache 会因为文档位置变化而失效；再到 Beluga 用 CXL 2.0 把缓存放进一张总线级共享内存池；最后落到 Cache-to-Cache——让源模型把 KV 语义直接投影进目标模型，省掉「解码成文本再编码回去」的损耗。沿途用 SubGCache、PAT、CoDec、HedraRAG、Auditing Prompt Caching 等作为这条线上的证据点。三篇精读（CacheBlend / Beluga / Cache-to-Cache）的关键数字都来自公开 arXiv 全文。

## 时间线

- `00:00` 开场 · 中心问题：缓存能否被复用、搬运、跨模型共享
- `01:36` Act 1 · 为什么缓存是瓶颈：生产环境里 prefix cache 为何不够（KVCache Cache in the Wild）
- `02:37` Act 2 · 跨请求复用 prefix → fusion（CacheBlend 精读 + SubGCache / PAT / CoDec / Prompt Choreography）
- `07:25` Act 3 · 缓存放在哪里：HBM / CXL / host / PIM（Beluga 精读 + HeterRAG / ELORA / 调度）
- `11:33` Act 4 · RAG / Agent 把复用变成核心问题（HedraRAG / Agentic 服务 / Bat）
- `13:11` Act 5 · 前沿：缓存即通信 Cache-to-Cache（精读，对比文本通信）
- `17:05` Act 6 · 三条共识、缓存安全侧信道与开放问题

## 论文与链接（按 act）

**Act 1** — CacheBlend (EuroSys'25, arXiv 2405.16444) · KVCache Cache in the Wild (USENIX ATC'25, arXiv 2506.02634)
**Act 2** — From Prefix Cache to Fusion RAG Cache (SIGMOD'26, arXiv 2601.12904) · SubGCache (AAAI'25, arXiv 2505.10951) · Sparse Attention across Multiple-context KV Cache (AAAI'25, arXiv 2508.11661) · PAT (ASPLOS'25, arXiv 2511.22333) · CoDec (SIGMOD'25, arXiv 2505.17694) · Prompt Choreography (ACL'25, arXiv 2512.23049)
**Act 3** — Beluga / CXL KVCache (SIGMOD'25, arXiv 2511.20172) · HeterRAG / PIM (ISCA'25) · ELORA (HPCA'26) · PrefillOnly (SOSP'25, arXiv 2505.07203) · Prefill-Decode Multiplexing (ASPLOS'25, arXiv 2504.14489) · DeepServe (USENIX ATC'25, arXiv 2501.14417)
**Act 4** — HedraRAG (SOSP'25) · Efficient LLM Serving for Agentic Workflows (SIGMOD'26, arXiv 2603.16104) · Bat (ASPLOS'26)
**Act 5** — Cache-to-Cache (arXiv 2510.03215)
**Act 6** — Auditing Prompt Caching (ICML'25, arXiv 2502.07776) · The Cost of Dynamic Reasoning (HPCA'25, arXiv 2506.04301)

资料源：公开 arXiv / 会议论文与对应论文全文卡片。

## 制作元信息

- 文稿：57 turns（Jeff / Ada），约 6,499 朗读字符
- 音频：19:32，自然 TTS 语速（未做 atempo 加速）
- 主持：Jeff（系统视角）/ Ada（提问者）
- 资料源：公开 arXiv / 会议论文；三篇精读的关键数字（CacheBlend 的 TTFT 2.2–3.3×、<15% 重算；Beluga 的 TTFT −89.6%、吞吐最高 7.35×；C2C 的 +3.1–5.4% vs 文本通信、2.5× 加速）均来自公开 arXiv 全文卡片，已核对。
