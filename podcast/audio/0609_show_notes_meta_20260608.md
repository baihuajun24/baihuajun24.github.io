# 0609 MLSYS 论文简报
Audio: 09:22
## 内容时间戳
- 00:00 Opening: 0609 MLSYS 论文简报
  - 基于 2026-06-08 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:16 Clairvoyant: Predictive SJF Scheduling to Mitigate Head-of-Line Blocking in Serial LLM Backends
  - 机构：独立研究者
  - 夯到拉评价：顶级（Jeff champion）
  - 亮点：这篇叫 Clairvoyant: Predictive SJF Scheduling to Mitigate Head-of-Line Blocking in Serial LLM Backends，作者是一位独立研究者。问题背景非常具体：像 Ollama、llama.cpp 这种串行的 LLM 推理后端，本质上是 FCFS 准入，一次只跑一个请求。
  - Link: https://arxiv.org/abs/2606.07248

- 03:07 Self-evolving LLM agents with in-distribution Optimization
  - 机构：埃因霍温理工大学; 利物浦大学
  - 夯到拉评价：人上人（Ada champion）
  - 亮点：我这篇是算法侧的 champion，叫 Self-evolving LLM agents with in-distribution Optimization，作者是埃因霍温理工大学和利物浦大学的团队，方法名叫 Q-Evolve，已经被 ICML 2026 收了。问题是 LLM agent 做长程决策时的 credit assignment：奖励通常只在 episode 末尾给一次，sparse reward 让策略学习非常不稳。
  - Link: https://arxiv.org/abs/2606.07367

- 05:45 SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating
  - 机构：浙江大学; 蚂蚁集团
  - 夯到拉评价：顶级（Ada champion）
  - 亮点：论文叫 SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating，作者来自浙江大学和蚂蚁集团。问题很直接：现在的 deep research agent 在 GAIA、BrowseComp 这种长程信息检索任务上能力很强，但都是暴力解法——盲目调工具、堆冗长 reasoning，token 和 tool call 都极度浪费。
  - Link: https://arxiv.org/abs/2606.07074

- 08:52 Wrap-up
  - 总结本期重点论文和后续阅读优先级。

## 制作元信息
- 论文召回：原始 JSONL 记录 356 篇；新论文 356 篇；带入 backlog 8 篇。
- 筛选链路：新候选 295 篇；backlog 候选 5 篇；粗排 300 篇；LLM 精评 15 篇；本期播客主讲 3 篇；快速提及 3 篇。
- LLM：aws.claude-opus-4.7；input 9564 tokens，output 3219 tokens，总计 12783 tokens。
- TTS：seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_yingyujiaoxue_uranus_bigtts`；25 turns，输入 3848 字符，计费文本 3848 words。
