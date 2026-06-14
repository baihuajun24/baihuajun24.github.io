# 提前停止：LLM 推理的"何时收手"（公开版）

## 评论

推理模型 30%–70% 的 token 是花在"算对之后还停不下来"上的。这期把这件事的五个层级——层级、token、草稿窗口、推理段落、采样轨迹——串成一条线，最后发现它们收敛到同一个配方：冻结大模型 + 一个微型隐藏态探针。结论是：模型其实早就知道该收手，过去两年的工作是学会去问它。

## 本期重点

这是"提前停止"主题特辑的公开版（8 分钟），从最早的 BERT 层级早退讲到 2026 年的验证侧前沿。主线只有一句话：在五个完全不同的粒度上，研究者各自独立地发现了同一个事实——模型在隐藏状态里其实编码了"我是不是已经想清楚了"，只是被解码层压平、没人去读。LayerSkip 的"早退当草稿、全模型验证"奠定了贯穿全场的"验证兜底"思想；DEER / SpecExit 把它做成隐藏态探针；When2Tool 又在工具调用上独立复现了一次。最后落到三条共同实践和四个尚未解决的硬挑战。

## 时间线

（最终音频 8:23，自然 TTS 语速）

- 0:00 开场：30%–70% 的推理 token 是浪费；核心问题"何时收手"，五层版图
- 1:08 源头：DeeBERT/PABEE → KV cache 困境 → LayerSkip 自投机（验证兜底）
- 2:12 推理早停：Certaindex 答案收敛 → DEER/SpecExit 隐藏态探针；Thinkless/ThinkPrune 与难题争论
- 3:54 投机解码里的停止：草稿长度（AdaEDL/SpecDec++）、草稿树（Sequoia）、2026 验证侧前沿
- 5:12 事前分配与采样/Agent：RouteLLM 路由、Adaptive-Consistency、When2Tool（探针第三次出现）
- 6:46 收敛与挑战：两条共同实践；四个硬挑战（停止理论、引擎接口、信号鲁棒性、冗余度量不可比）

## 论文与链接

- LayerSkip — arXiv 2404.16710
- Certaindex — arXiv 2412.20993
- DEER — arXiv 2504.15895
- SpecExit — arXiv 2509.24248
- Thinkless — arXiv 2505.13379 ／ ThinkPrune — arXiv 2504.01296
- AdaEDL — arXiv 2410.18351 ／ SpecDec++ — arXiv 2405.19715 ／ Sequoia — arXiv 2402.12374
- RouteLLM — arXiv 2406.18665 ／ Adaptive-Consistency — arXiv 2305.11860 ／ When2Tool — arXiv 2605.09252

## 制作元信息

- 文稿：30 turns（Jeff 15 / Ada 15），约 2,552 朗读字符
- 音频：8:23，自然 TTS 语速（loudnorm，无 atempo 加速）
- 主持：Jeff（系统视角）/ Ada（提问者）
- 资料源：内部 early-stopping mini-survey（2026-06-12，arXiv ID 全部 API 核验）
