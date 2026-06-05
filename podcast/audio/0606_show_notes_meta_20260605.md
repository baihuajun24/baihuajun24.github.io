# 0606 MLSYS 论文简报
Audio: 10:50
## 内容时间戳
- 00:00 Opening: 0606 MLSYS 论文简报
  - 基于 2026-06-05 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:29 Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving
  - 机构：汉阳大学; Rebellions
  - 夯到拉评价：顶级（Jeff champion）
  - 亮点：对，我的 champion 是来自汉阳大学和 Rebellions 的 Tangram，全名是 Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving。背景是这样的：多轮对话场景里，KV cache 会随着对话轮数线性膨胀，对显存和带宽都是巨大压力。
  - Link: https://arxiv.org/abs/2606.06302

- 03:15 Rethinking Continual Experience Internalization for Self-Evolving LLM Agents
  - 机构：中国人民大学高瓴人工智能学院; 北京航空航天大学
  - 夯到拉评价：人上人（Ada champion）
  - 亮点：我选了中国人民大学高瓴人工智能学院和北京航空航天大学的 Rethinking Continual Experience Internalization for Self-Evolving LLM Agents。背景是 self-evolving agent 的一个长期梦想：把过去交互里的 contextual experience，蒸馏成模型权重里的能力，这样 agent 就能持续变强。
  - Link: https://arxiv.org/abs/2606.04703

- 05:57 LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents
  - 机构：上海交通大学; 中山大学
  - 夯到拉评价：人上人（Jeff champion）
  - 亮点：好，第三篇是上海交通大学和中山大学的 LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents。问题背景挺有意思：现在很多 agent 系统会维护一堆 textual skills，就是可复用的任务流程片段，每次调用都塞进 prompt。
  - Link: https://arxiv.org/abs/2606.06087

- 10:20 Wrap-up
  - 总结本期重点论文和后续阅读优先级。

## 制作元信息
- 论文召回：原始 JSONL 记录 305 篇；新论文 305 篇；带入 backlog 10 篇。
- 筛选链路：新候选 236 篇；backlog 候选 10 篇；粗排 246 篇；LLM 精评 20 篇；本期播客主讲 3 篇；快速提及 6 篇。
- LLM：aws.claude-opus-4.7；input 10756 tokens，output 3359 tokens，总计 14115 tokens。
- TTS：seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_yingyujiaoxue_uranus_bigtts`；26 turns，输入 4873 字符，计费文本 4873 words。
