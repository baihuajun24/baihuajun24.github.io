# CVPR 2026 特别篇：为什么 10 年后，ResNet 仍在改写 AI

## 评论

这期我们不是按获奖名单逐篇报菜名，而是把 ResNet、D4RT、draft-and-verify 和 cache 串成一条方法论主线：真正持久的 AI 进步，常常来自对信息路径和计算路径的重写。

10 年后的 ResNet 仍然重要，是因为它教会了深度模型一个朴素但耐用的原则：先保留稳定通路，再让模型学习必要的增量。

## 本期重点

这期不是单纯盘点 CVPR 2026 获奖论文，而是抓住一条更耐看的主线：AI 的很多关键进步，不只是把模型做大，而是重新设计信息、计算和推理的默认路径。

从十年前的 ResNet residual path，到今年 CVPR Best Paper D4RT 的 4D query path，再到长视频里的 draft-and-verify、扩散模型里的 cache path，这些工作共同指向一个启发：真正经得起时间考验的 idea，往往会从一个架构 trick，变成跨模型、跨系统的设计语言。

## 时间线

00:00 开场：从 ResNet 作为 Test-of-Time 锚点切入，说明 CVF 奖项档案已列出 ResNet 和 YOLO 为 2026 Longuet-Higgins Prize 论文。

00:31 CVPR 2026 背景：Denver 会场、16,092 投稿、4,089 接收、141 oral、578 highlight、74 篇 award candidate；最终 Best Paper 为 D4RT。

01:11 Deep Residual Learning for Image Recognition

ResNet 主线：为什么 identity path / residual path 改变了深层网络默认信息路径，并继续影响 Transformer residual stream、adapter、U-Net skip connection、cache reuse 和 speculative decoding。

03:17 Efficiently Reconstructing Dynamic Scenes One D4RT at a Time

CVPR 2026 Best Paper。节目重点解释 D4RT 如何把动态 4D reconstruction 从密集逐帧输出改成统一表示上的时空点查询，并把它连接到“改路径，而不是只堆 decoder”的系统设计思想。

05:17 NitroGen: An Open Foundation Model for Generalist Gaming Agents

官方 Award Candidate / Oral。用 1000 多个游戏、4 万小时 gameplay video 训练通用 vision-action foundation model，代表从静态观察语料到 action-conditioned rollout 的预训练路径变化。

06:29 Thinking with Drafts: Speculative Temporal Reasoning for Efficient Long Video Understanding

官方 Award Candidate / Oral。用轻量 draft MLLM 选择证据帧，再由 target MLLM 验证和推理，作为长视频理解里的 draft-and-verify 路径。

07:40 快速补充：SeaCache 与 VGGT-Ω

SeaCache 讨论扩散模型缓存有效性与频谱演化；VGGT-Ω 代表 feed-forward 3D reconstruction 的基础模型接口与内存路径设计。

08:54 3DReflecNet 一线对照

保留为复杂材质数据集的简短背景，不再作为主线段落。

09:11 Takeaways

核心启发：ResNet 的 identity path，D4RT 的 query path，NitroGen 的 trajectory pretraining path，Thinking with Drafts 的 draft/verify path，SeaCache 的 cache path，以及 VGGT-Ω 的几何接口路径，都在回答同一个问题：系统默认让信息怎么走，往往决定了模型能走多远。

## 论文与链接

- PI-approved WeChat report
  - Link: https://mp.weixin.qq.com/s/KieRMknWe2ZJx2BNw_0BmA
- CVF Computer Vision Awards archive
  - Link: https://www.thecvf.com/?page_id=413
- Deep Residual Learning for Image Recognition
  - CVF paper: https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
- Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
  - CVF paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html
  - Project page: https://d4rt-paper.github.io/
- NitroGen: An Open Foundation Model for Generalist Gaming Agents
  - CVPR poster: https://cvpr.thecvf.com/virtual/2026/poster/39333
  - CVF paper: https://openaccess.thecvf.com/content/CVPR2026/html/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.html
- Thinking with Drafts: Speculative Temporal Reasoning for Efficient Long Video Understanding
  - CVPR poster: https://cvpr.thecvf.com/virtual/2026/poster/37426
  - CVF paper: https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Thinking_with_Drafts_Speculative_Temporal_Reasoning_for_Efficient_Long_Video_CVPR_2026_paper.html
- SeaCache: Spectral-Evolution-Aware Cache for Accelerating Diffusion Models
  - CVPR poster: https://cvpr.thecvf.com/virtual/2026/poster/38909
  - CVF paper: https://openaccess.thecvf.com/content/CVPR2026/html/Chung_SeaCache_Spectral-Evolution-Aware_Cache_for_Accelerating_Diffusion_Models_CVPR_2026_paper.html
- VGGT-Ω
  - CVPR poster: https://cvpr.thecvf.com/virtual/2026/poster/39730
  - CVF paper: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_VGGT-ohm_CVPR_2026_paper.html
- 3DReflecNet: A Large-Scale Dataset for 3D Reconstruction of Reflective, Transparent, and Low-Texture Objects
  - CVPR poster: https://cvpr.thecvf.com/virtual/2026/poster/37703
  - CVF paper: https://openaccess.thecvf.com/content/CVPR2026/html/Liang_3DReflecNet_A_Large-Scale_Dataset_for_3D_Reconstruction_of_Reflective_Transparent_CVPR_2026_paper.html

## 制作元信息

- 状态：送审草稿。音频已重新生成，时长 10:18。
- 来源说明：本版按 PI 确认的微信报道重写叙事，奖项和论文事实用 CVPR/CVF 官方页面、CVF Open Access 页面、CVF Computer Vision Awards archive、D4RT project page 交叉核对。
- 微信直读限制：WeChat 页面返回环境/CAPTCHA gate，本地 Camoufox reader 目录缺失，`miku_ai` 未安装。因此本稿记录为“PI-approved WeChat report via snippets/secondary evidence”，不声称已完整抓取原文。
- 奖项来源：CVF awards archive 确认 D4RT 为 CVPR 2026 Best Paper，确认 ResNet 与 YOLO 为 2026 Longuet-Higgins Prize 论文。
- 脚本：29 turns；口播文本 4,305 字符；无口播 URL、Markdown footnote、反引号或 citation clutter。
- TTS：seed-tts-2.0；Jeff voice `zh_male_m191_uranus_bigtts`，Ada voice `zh_female_yingyujiaoxue_uranus_bigtts`；29 turns，输入 4,305 字符，计费文本 4,305 words。
- 音频处理：原始合成 `audio_raw_11m45s.mp3` 为 11:45，经 `atempo=1.14` 和 loudnorm 处理后得到最终 `audio.mp3`，时长 10:18，24 kHz mono，约 128 kbps。
