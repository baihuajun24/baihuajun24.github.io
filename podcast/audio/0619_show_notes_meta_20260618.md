# 0619 MLSYS 论文简报：RL Rollout 投机解码、NPU 推理延迟预测与并行树状草稿
Audio: 10:01
## 内容时间戳
- 00:00 Opening: 0619 MLSYS 论文简报
  - 基于 2026-06-18 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。
- 00:25 EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts
  - 夯到拉评价：夯（Jeff champion）
  - 亮点：这篇论文叫 EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts，来自飞瑞傲 AI。它直击了目前大语言模型强化学习训练中最大的痛点，也就是 Rollout 阶段的延迟。
  - Link: https://arxiv.org/abs/2606.18967

- 03:40 Latency Prediction for LLM Inference on NPU Systems
  - 夯到拉评价：顶级（Ada champion）
  - 亮点：我要分享的第二篇论文叫 Latency Prediction for LLM Inference on NPU Systems。 现在的 LLM 部署在 GPU 之外，确实越来越多地采用 NPU 了。
  - Link: https://arxiv.org/abs/2606.18042

- 06:15 JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting
  - 夯到拉评价：夯（Jeff champion）
  - 亮点：既然聊到推理加速，那我们再来看第三篇探索性的工作：JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting，来自加州大学圣迭戈分校郝张老师的团队。 郝张老师团队在投机解码上的工作一直很受关注。
  - Link: https://arxiv.org/abs/2606.18394

- 09:31 Wrap-up
  - 总结本期重点论文和后续阅读优先级。

## 制作元信息
- 论文召回：原始 JSONL 记录 434 篇；新论文 434 篇；带入 backlog 10 篇。
- 筛选链路：新候选 361 篇；backlog 候选 28 篇；粗排 389 篇；LLM 精评 24 篇；本期播客主讲 3 篇；快速提及 4 篇。
- LLM：gemini-3.5-flash；input 8748 tokens，output 2123 tokens，总计 10871 tokens。
- TTS：seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_vv_uranus_bigtts`；32 turns，输入 3663 字符，计费文本 3663 words。

## 本期工作流改进
- 96h catch-up 窗口：上次 digest 06-15，本次跨周末补抓 434 篇新论文。
- 修复 gemini judge：null-message（reasoning 耗尽 max_tokens）现 fallback 到 glm-5.2；shared-AppId 20 RPM 改 15 RPM + 15s/30s 429 退避。
- 算法主讲位经 PI review 由 ZPPO 换为 Latency Prediction (NPU/LENS)；LENS 卡片因 gemini 间歇 JSON 解析失败，重抽得到 html 级 grounding。
