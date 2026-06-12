# 0613 MLSYS 论文简报
Audio: 11:06
## 内容时间戳
- 00:00 Opening: 0613 MLSYS 论文简报
  - 基于 2026-06-12 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:29 MiniPIC: Flexible Position-Independent Caching in <100LOC
  - 机构：IBM 研究院（苏黎世）
  - 夯到拉评价：夯（Jeff champion）
  - 亮点：没错，这篇论文叫 MiniPIC: Flexible Position-Independent Caching in <100LOC，来自 IBM 研究院（苏黎世）。它解决的是目前大语言模型在 Agent 和检索增强生成，也就是 RAG 场景下一个非常痛的系统瓶颈：重复输入片段的 KV 缓存复用。
  - Link: https://arxiv.org/abs/2606.13126

- 03:41 ESPO: Early-Stopping Proximal Policy Optimization
  - 机构：通义实验室（阿里巴巴）; 北京大学
  - 夯到拉评价：夯（Ada champion）
  - 亮点：我选的是 ESPO: Early-Stopping Proximal Policy Optimization，来自通义实验室（阿里巴巴）和北京大学。这篇论文直击大模型在进行强化学习，特别是做复杂推理和 Agent 任务时的训练算力浪费问题。

- 06:57 SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research
  - 机构：清华大学; 蚂蚁集团
  - 夯到拉评价：顶级（Jeff champion）
  - 亮点：你说的是 SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research 吧。这篇论文确实很有意思，它提出了一种委派智能，也就是 Delegation Intelligence 的新范式，专门用来解决超长程深度研究任务中，主 Agent 上下文窗口装不下的问题。

- 10:36 Wrap-up
  - 总结本期重点论文和后续阅读优先级。

## 制作元信息
- 论文召回：原始 JSONL 记录 251 篇；新论文 251 篇；带入 backlog 10 篇。
- 筛选链路：新候选 188 篇；backlog 候选 27 篇；粗排 215 篇；LLM 精评 20 篇；本期播客主讲 3 篇；快速提及 4 篇。
- LLM：gemini-3.5-flash；input 6080 tokens，output 2253 tokens，总计 8333 tokens。
- TTS：seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_vv_uranus_bigtts`；35 turns，输入 3998 字符，计费文本 3998 words。
