# 推理算力特辑 · 错在哪一步，就从哪重来（公开版）

## 评论

推理期该怎么花算力？这一期把 test-time scaling 拆成一个信用分配问题：环境只对整条轨迹判对错，不告诉你哪个 token 开始跑偏。TTEL 把训练里用来算梯度的那条自蒸馏散度信号，反手当成推理期的剪枝判据，训练无关地定位错点、截断、从那儿分支，复用有效前缀；Recursive Self-Aggregation 则用种群进化来组织搜索。两条近作，同一个问题——怎么把算力花在错的那一步上。

## 本期重点

围绕 test-time compute 的"花法"，串起框架、两条老路的通病、一个精准定位的新解，和一条种群进化的对照。

框架：Snell 2024 说推理期最优地花算力，可比堆更大模型更划算；Large Language Monkeys 说反复采样时 coverage 随样本数四个数量级近似 log-linear——可靠但盲目，像买彩票。两条主流路子各有通病：并行 best-of-N 各样本互不知情、丢掉有效前缀；串行 refine 会 stagnate，模型定位不到自己错在哪一步。共同缺口：没有 token 级信用分配。

主讲一，TTEL（顶级）：把信用分配做到 token 级、且训练无关。它复用自蒸馏那条散度信号——train-time 拿去算梯度，TTEL 拿来当推理期剪枝判据。三步：带反馈重打分得 teacher 散度尖峰；用非诊断性反馈基线扣掉上下文噪声；取最高置信错点截断、分支，组织成前缀共享树。Qwen3-8B 在 LiveCodeBench 上 pass@64 到 71.0%、生成 token 约独立采样的一半（360.4k vs 735.0k）；AIME-2025 / HMMT-2025 对 Qwen3-8B 与 Qwen3-4B-Thinking 均严格占优 Pareto。口径：吃反馈质量（代码测试用例最理想）、主要在 Qwen3 家族验证、重打分成本需计入。价值在这个视角本身。

主讲二，Recursive Self-Aggregation（人上人）：受进化算法启发，每步对一群候选推理链做子集聚合、迭代出更优的群，兼取并行与串行之长，和 TTEL 是组织 test-time 搜索的两种近期答案——一个外科手术式定位，一个群体进化。

谱系一句：信用分配这事，早年 Uesato 比过 process vs outcome 反馈，后来 PRM 靠训练一个步级验证器；TTEL 反其道，直接从策略概率位移里免费读出错点。收尾还留了个更大的想象：这条 token 级信号既能训练用、又能推理用，可能把训练期的自我改进和推理期的搜索，缝成同一个闭环。

## 时间线

（最终音频 9:37，自然 TTS 语速）

- 00:00 开场 · 推理算力该怎么花，不只是花多少
- 02:00 TTEL 登场 · 把信用分配做到 token 级
- 03:43 三步机制 + 效率数字（LiveCodeBench pass@64 71.0%，约半数 token）
- 05:30 递归自聚合 · 用种群进化组织搜索
- 07:30 信用分配的谱系 + 训练与推理的闭环
- 09:33 收尾

## 论文与链接

- Test-Time Scaling via Error Localization (TTEL) — arXiv:2607.21453
- Recursive Self-Aggregation Unlocks Deep Thinking — arXiv:2509.26626
- Scaling LLM Test-Time Compute Optimally — arXiv:2408.03314
- Large Language Monkeys: Scaling Inference Compute with Repeated Sampling — arXiv:2407.21787
- Solving math word problems with process- and outcome-based feedback — arXiv:2211.14275
- Training Language Models to Self-Correct via RL (SCoRe) — arXiv:2409.12917
- DeepSeek-R1 — arXiv:2501.12948
- LiveCodeBench — arXiv:2403.07974

## 制作元信息

- 文稿：32 turns（Jeff / Ada 双人），约 2,781 朗读字符；全部基于公开 arXiv 预印本，与任何评审无关。
- 音频：9:37，自然 TTS 语速（loudnorm，无 atempo 加速）。
- 主持：Jeff（系统视角）/ Ada（提问者）。
- 口径：TTEL 的效率优势建立在有信息量反馈上、主要在 Qwen3 家族验证、"严格占优"限其测过的域、重打分成本需计入；Snell / Monkeys / RSA / R1 的数字均为各自论文自报，硬件口径不同，不可横比；两档评级为对公开工作的评论。
