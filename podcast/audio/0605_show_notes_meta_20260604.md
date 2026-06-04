# 0605 MLSYS 论文简报
Audio: 09:48
## 内容时间戳
- 00:00 Opening: 0605 MLSYS 论文简报
  - 基于 2026-06-04 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:33 D^2SD: Accelerating Speculative Decoding with Dual Diffusion Draft Models
  - 机构：北京大学; 清华大学
  - 亮点：这篇全名是 D²SD: Accelerating Speculative Decoding with Dual Diffusion Draft Models，第一作者来自北京大学，合作单位还有清华大学。它瞄准的是现在比较流行的 diffusion-based drafter 路线——也就是用扩散模型一次性并行生成一整块 draft token，然后丢给 target model 一次 forward 验证。
  - Link: https://arxiv.org/abs/2606.04446

- 03:33 RUBAS: Rubric-Based Reinforcement Learning for Agent Safety
  - 机构：清华大学; 华为诺亚方舟实验室
  - 亮点：下一篇是清华那边出来的 RUBAS: Rubric-Based Reinforcement Learning for Agent Safety，第一作者来自清华大学，合作单位还有华为诺亚方舟实验室。 这是 agent safety 方向？
  - Link: https://arxiv.org/abs/2606.04051

- 05:25 Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference
  - 机构：爱荷华大学; 阿贡国家实验室
  - 亮点：下面这篇我想聊一下，叫 Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference，第一作者来自爱荷华大学，合作单位还有阿贡国家实验室。已经被 ICS'26 接收。
  - Link: https://arxiv.org/abs/2606.02430

- 07:33 Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories
  - 机构：谷歌研究院; 康奈尔大学
  - 亮点：一篇是谷歌研究院和康奈尔大学的 Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories。它提了一个"睡眠"范式，让模型把短期 in-context 记忆通过两个阶段固化进长期参数：一个叫 Memory Consolidation，用 on-policy distillation 加 RL imitation 把小模型的知识"播种"到大模型；
  - Link: https://arxiv.org/abs/2606.03979

- 08:12 Using Reward Uncertainty to Induce Diverse Behaviour in Reinforcement Learning
  - 机构：纽约大学; 谷歌 DeepMind
  - 亮点：最后一篇是纽约大学和谷歌 DeepMind 合作的 Using Reward Uncertainty to Induce Diverse Behaviour in Reinforcement Learning。核心论点是：行为多样性不应该靠 entropy bonus 这种硬塞，而应该作为"对 reward 不确定性的理性回应"自然涌现。
  - Link: https://arxiv.org/abs/2606.03962

- 09:18 Wrap-up
  - 总结本期重点论文和后续阅读优先级。

## 制作元信息
- 论文召回：原始 JSONL 记录 276 篇；新论文 276 篇；带入 backlog 10 篇。
- 筛选链路：新候选 246 篇；backlog 候选 10 篇；粗排 256 篇；LLM 精评 20 篇；本期播客选讲 5 篇。
- LLM：friday / aws.claude-opus-4.7；input 5420 tokens，output 3569 tokens，总计 8989 tokens
- TTS：Volcengine / seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_vv_uranus_bigtts`；34 turns，输入 4405 字符，计费文本 4405 words
