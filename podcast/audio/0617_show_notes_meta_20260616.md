# 0617 MLSYS 论文简报：编码 Agent 的 KV 缓存管理、Agent 上下文缓存压缩、可迁移技能树搜索
Audio: 13:31

## 内容时间戳
- 00:00 开场
  - 基于 2026-06-16 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:34 CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents
  - 机构：华盛顿大学、弗吉尼亚大学
  - 夯到拉评价：人上人（Jeff 主讲）
  - 亮点：编码 Agent 是长程闭环会话，prefill/decode 比例约 21 倍、KV 缓存压力大；传统先来先服务 + LRU 会在等工具返回的间隙误删缓存，导致抖动重算。CacheWise 在 vLLM 上做前缀感知调度 + 复用感知驱逐（用工具调用元数据做轻量预测），KVCache 驱逐次数降 2.0–2.6 倍、会话完成时间快约 3.5 倍。
  - Link: https://arxiv.org/abs/2606.16824

- 05:23 TokenPilot: Cache-Efficient Context Management for LLM Agents
  - 机构：浙江大学、HomologyAI
  - 夯到拉评价：人上人（Ada 主讲）
  - 亮点：长程 Agent 上下文不断累积推高推理成本，但文本裁剪 / 记忆驱逐会打乱布局、造成前缀失配与缓存失效。TokenPilot 用双粒度管理——全局 Ingestion-Aware Compaction 稳定前缀、本地 Lifecycle-Aware Eviction 按任务相关性过期再卸载，成本降约 56%–87% 且性能基本不掉。
  - Link: https://arxiv.org/abs/2606.17016

- 09:23 OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models
  - 机构：香港理工大学、南洋理工大学
  - 夯到拉评价：顶级（Ada 主讲，探索性）
  - 亮点：Agent 学到的技能换个底座常常失效。提出 Collective Skill Tree Search（CSTS）：用多模型协同生成多样候选技能、再由多模型按质量与跨模型迁移性评分筛选，自动构造结构化、可迁移、可复用的技能树。（论文正文未给出可核实的量化结果，本期只讲思路。）
  - Link: https://arxiv.org/abs/2606.16774

- 快速提及：Skill-to-LoRA（把技能提示词换成可动态加载的 LoRA 适配器省 token）、KVEraser（学习引导 KV cache）、Context-Aware RL for Agentic and Multimodal LLMs、SpInfer（香港科技大学，稀疏 GEMM 推理）。
- 13:01 收尾
  - 总结本期重点与后续阅读优先级。

## 制作元信息
- 论文召回：原始 JSONL 记录 281 篇；新论文 281 篇；带入 backlog 10 篇。
- 筛选链路：新候选 219 篇；backlog 候选 24 篇；粗排 243 篇；LLM 精评 40 篇；本期播客主讲 3 篇；快速提及若干。
- LLM（脚本）：gemini-3.5-flash；input 8767 tokens，output 2807 tokens，总计 11574 tokens。
- TTS：seed-tts-2.0（doubao-ws-v3）；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_vv_uranus_bigtts`；49 turns，4565 字符；自然语速、未做 atempo。

## 本期工作流改进
- 走完整的 PI 候选 review gate：把数字接地性写进候选清单（CacheWise 有正文数字，ExpRL / OpenClaw 正文截断无数字），PI 据此把 Ada 的算法主讲从 ExpRL 换成正文有 56%–87% 成本数字、更扎实的 TokenPilot。
- 首次用本会话新落地的可复用工具 `post-xiaoyuzhou/tools/pin_episode_plan.py` + `gen_episode_script.py`（pins.json 驱动）把 PI 钦定阵容固定进 plan、再就地生成脚本，避免 `--plan-only/--script-only` 重建覆盖钦定。
- 排重：Harness-1、SWITCH 因 0616 已讲，本期不再讲。
