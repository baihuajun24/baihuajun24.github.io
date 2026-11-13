预算快用完了，下一次该叫哪个模型？本期三篇论文都把 Agent 的决策放回约束里：一篇管钱，预算会在某次长回答之后突然停机；一篇管环境，仿真 App 必须经得起真实录屏的独立回放；一篇管搭档，不同厂商的 Agent 第一次见面，往往对不上各自默认的暗号。三篇是互补视角，并未共同验证一条完整流程。

时间线

00:00 开场：预算快用完了，该叫哪个模型
00:26 预算路由：越线即停机的预算，和偏保守的费用上限
03:04 Trace to World：规格与实现分离，用真实录屏做差分测试
05:49 零样本协调：第一次见面的 Agent，为什么对不上暗号
08:03 引用观察：给草稿模型第二次猜的机会
08:30 评级和读法

论文与链接

Pathwise-Budgeted LLM Routing: Online Allocation with K-Bit Tail-Cost Learning
清华大学、新加坡国立大学等
https://arxiv.org/abs/2611.05835
说明：策略名为 ADP-HT。五个便宜模型、每题最多四次调用、总预算 0.025 美元时，MATH500 解出 216.2 题，最强已实现基线 Position-aware LinUCB 为 100.8 题；GPQA 为 85.0 对 29.8。五次重复之间波动很大，预算放宽后优势基本消失（MATH500 在 0.30 美元时只领先 0.6 题）。LiveCodeBench 上，预算放宽后 OpenRouter AutoRouter 省钱模式以 1.62 美元解出 732 题，超过本方法。超参数按数据集单独调过。

Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training
阿里巴巴 Token Hub、南京大学
https://arxiv.org/abs/2610.30792
说明：10 个 App、200 条流程上六项检查全过 91.1%，作者复现的最强基线 GUI-GENESIS-style 为 59.8%，只换掉源录屏验证的自验证对照为 79.1%。100 个配对真机任务上，仿真增益保留约 94%，自验证约 55%（第一阶段策略，3 个种子）。这是样本内检验：评测流程就是构建时回放修复过的录屏，真机任务也都来自训练用过的 App。预印本。

Zero-Shot Coordination among LLM Agents
牛津大学
https://arxiv.org/abs/2611.06409
说明：猫狗灯泡游戏里，代码 Agent 自我配对平均 9.75 分，同模型另一次生成配对 2.41，跨模型配对 -0.51；拆墙的安全回报是 5。加入共享的协调友好定义后，对话 Agent 4×4 跨模型配对全部为 5.00（每格 10 局）。代价是欠协调：可临场建立约定的十轮游戏里，一个模型的自我配对分数从 95.8 跌到 50。没有实跑传统强化学习的协调方法。论文页脚标注 NeurIPS 2026。

引用观察

Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding
谷歌、莱斯大学
https://arxiv.org/abs/2611.05724
引用了我们的 PARD: Accelerating LLM Inference with Low-Cost PARallel Draft Model Adaptation（arXiv 2504.18583），并认为重猜可以叠加在这类并行草稿方法之上。

本期评级

Trace2World：顶级。规格与实现分离，证据链三篇里最完整。
ADP-HT：人上人。问题刻画有用，大幅优势只在极紧预算里。
零样本协调：人上人。诊断干净，解法主要是把模型推向保守。

主持：Jeff、Ada。音频由本地 Qwen3-TTS 生成。
