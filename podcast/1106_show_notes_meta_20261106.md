1106 MLSYS 特辑 · 模型给模型做手术

评论
"大模型能改权重"，先问改的是谁：这次是 GPT-6 Astra 读写别人家的小模型，最大到 0.8B，"改自己"仍是展望。数学分数暴涨来自拆掉一个停不下来的循环，而不是教会了数学。判断这类工作，先问改的是谁、改掉了什么、靠什么验证。

本期重点
MIT CSAIL 的博客 Sparks of Weight-Space Programming 让一个通用大模型不经专门训练、不跑梯度下降，直接读写神经网络权重：从权重猜出游戏，从零写出能打砖块的策略，一次修好冲不上坡的小车，并把 Qwen3.5-0.8B 在 MATH-500 上的正确率从 7.9% 提到 48.1%（思考模式，32,768 token 上限）。

作者公开的日志显示：在 1,152 道留出练习题中，原模型本来能写完的 114 道，改前改后都是 93.9%，提升全部来自原本被循环卡死的题；换成不怎么循环的 Gemma 3 270M 就改不动了。我们也肯定作者的公开程度：全部提示、代码、输出和比特级权重差异都可核查，第三方据此重建并重跑得到 51.0%。

时间线
00:00 开场：头条数字，改的是谁
00:53 它实际是什么：读、写、修三类例子
02:03 数学头条的真相：拆掉一个循环
03:49 之前做过什么：四条研究脉络
05:49 公认的、新的与争议
06:55 集中批判：优化还是诊断，能否扩展与验证
08:05 肯定公开：全部日志与第三方重跑
08:41 前景：审计、初始化、自我改写与安全

博客与日志
https://rikiyat.github.io/blog/weight-space-programming/
https://github.com/RikiyaT/lm_understand-logs
https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming

相关研究
Schmidhuber, A self-referential weight matrix (ICANN 1993)
Irie et al., A Modern Self-Referential Weight Matrix That Learns to Modify Itself https://arxiv.org/abs/2202.05780
SEAL: Self-Adapting Language Models https://arxiv.org/abs/2506.10943
HyperNetworks https://arxiv.org/abs/1609.09106
Text-to-LoRA https://arxiv.org/abs/2506.06105
Predicting Neural Network Accuracy from Weights https://arxiv.org/abs/2002.11448
Weight Oracles https://arxiv.org/abs/2610.07334
ROME https://arxiv.org/abs/2202.05262
Arditi et al., Refusal in Language Models Is Mediated by a Single Direction https://arxiv.org/abs/2406.11717
Why Do Reasoning Models Loop? https://arxiv.org/abs/2512.12895

说明
原始材料是博客与公开日志，不是同行评审论文，作者自称早期结果；每个预算只跑了一次。练习集结果是 Astra 自己的报告。Gemma 跟进实验与 Qwen 的条件不同。文中提到的复现与跨代对比是评论者本人的说法。
