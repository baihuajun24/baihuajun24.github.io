# 0616 MLSYS 论文简报：并行 KV 合成、隐状态推理、Agent 状态外置
Audio: 11:53
## 内容时间戳
- 00:00 Opening: 0616 MLSYS 论文简报
  - 基于 2026-06-15 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:24 Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows
  - 机构：佐治亚理工学院、Meta
  - 夯到拉评价：顶级（Jeff champion）
  - 亮点：并行 Agent 工作流里，让合成器直接消费各分支 worker 的 KV Cache（Cache Mapper 对齐 + Synthesizer LoRA），免去文本重拼与重复 Prefill；9 个下游数据集中 7 个达到或超过文本拼接基线，首字延迟（TTFT）降低 2.5–11×。约束：所有 worker 与合成器需共享同一自回归骨干，跨模型暂不适用。
  - Link: https://arxiv.org/abs/2606.14672

- 04:05 Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy Reinforcement Learning (SWITCH)
  - 机构：香港科技大学（广州）、剑桥大学
  - 夯到拉评价：顶级（Ada champion）
  - 亮点：用一对显式边界 token `<swi>`/`</swi>` 把隐状态推理显式切出来，既让标准 on-policy RL（GRPO）在文本位置上可定义概率、又为机制分析提供离散锚点；MATH-500 上比同规模最强 Coconut 式基线高 25.7 个百分点，GRPO 后隐式推理调用率减半且准确率再 +12.6 个百分点。
  - Link: https://arxiv.org/abs/2606.13106

- 08:09 Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses
  - 机构：伊利诺伊大学厄巴纳-香槟分校、UC Berkeley
  - 夯到拉评价：人上人（Ada champion）
  - 亮点：把候选池管理、去重、状态摘要、证据整理等"机械记账"从策略剥离、卸到环境侧 harness，让 RL 只学"搜什么、留什么、何时停"的语义决策——关注点分离换样本效率。（注：本期卡片取自摘要，正文具体数字未核实，节目中未作事实陈述。）
  - Link: https://arxiv.org/abs/2606.02373

- 11:23 Wrap-up
  - 三篇共同主题：重新切分"策略该做什么、环境/接口该做什么"——KV 接口聚合、边界 token 显式化、状态记账外置。
  - 快速提及：AdaSR（东方理工高等研究院（宁波）、上海交通大学），用层次化相对策略优化 HRPO 在流式/部分观测下动态分配推理算力、管理延迟。https://arxiv.org/abs/2606.14694

## 制作元信息
- 论文召回：原始 JSONL 记录 141 篇；新论文 141 篇；带入 backlog 10 篇。
- 筛选链路：新候选 105 篇；backlog 候选 15 篇；粗排 120 篇；LLM 精评 40 篇；本期播客主讲 3 篇；快速提及 1 篇。
- LLM：aws.claude-opus-4.7；input 13401 tokens，output 4249 tokens，总计 17650 tokens。
- TTS：seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_vv_uranus_bigtts`；38 turns，输入 4499 字符，计费文本 4340 words。
