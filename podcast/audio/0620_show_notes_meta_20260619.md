# 0620 MLSYS 论文简报：CXL 稀疏 KV 池、RL 乘性信用分配与对抗式深度研究智能体
Audio: 15:04
## 内容时间戳
- 00:00 Opening: 0620 MLSYS 论文简报
  - 基于 2026-06-19 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:37 SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL
  - 夯到拉评价：顶级（Jeff champion）
  - 亮点：没错，今天我要重点推荐的第一篇系统方向论文叫做 SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL。这篇论文针对的是一个非常切中痛点的问题。
  - Link: https://arxiv.org/abs/2606.19746

- 04:59 Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards
  - 夯到拉评价：顶级（Ada champion）
  - 亮点：我今天挑出的算法 champion 论文标题是 Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards。这篇工作聚焦在可验证奖励强化学习，也就是 RLVR 场景下的信用分配问题。
  - Link: https://arxiv.org/abs/2606.18810

- 08:59 MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments
  - 夯到拉评价：夯（Ada champion）
  - 亮点：这篇论文叫 MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments。之前有一个叫 LiteResearcher 的系统，仅仅用四B参数的模型在 GAIA 评测上就拿到了 71.3%，超越了 GPT-4o。
  - Link: https://arxiv.org/abs/2606.19893

- 14:34 Wrap-up
  - 总结本期重点论文和后续阅读优先级。

## 制作元信息
- 论文召回：原始 JSONL 记录 273 篇；新论文 273 篇；带入 backlog 10 篇。
- 筛选链路：新候选 215 篇；backlog 候选 23 篇；粗排 238 篇；LLM 精评 38 篇；本期播客主讲 3 篇；快速提及 3 篇。
- LLM：gemini-3.5-flash；input 7811 tokens，output 3136 tokens，总计 10947 tokens。
- TTS：seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_vv_uranus_bigtts`；43 turns，输入 5259 字符，计费文本 5259 words。

## 本期工作流改进
- 等 arXiv 当日批次：晨跑 24h 窗口返回 0 篇（arXiv 06-17 后无新公告），等到 06-18 批次上线后 24h 抓到 273 篇，避免产出过期选题。
- 修复脚本生成 null-crash：_generate_script_openai_native 现按 llm_judge 同款 null-safe + glm-5.2 fallback（gemini reasoning 耗尽 9000 预算返回 message:null 时不再崩溃）。
- 卡片改用 glm-5.2（3/3 一次成功，html provenance），脚本用 gemini-3.5-flash（长文完成度更好）。
