模型权重不变，智能体还能怎样变好？从一个反复读文件、修改、测试的修 Bug 场景出发，本期讨论执行框架、工具组织与经验积累，能否成为另一条能力提升路径。

本期重点
SoL-Pi：自动发现执行中的浪费，把降本与质量放在同一张账上。
Harness²：通过实际试跑和行为对比改善当前交付，为后续任务积累有条件的流程经验。
Rethinking v4：同样资源，改框架是否优于把任务多试几次？终端任务与长程游戏为什么会呈现不同结果？
最后集中讨论改进信号、经验复用与搜索成本摊销，再连接缓存复用的系统问题。

时间线
00:00 模型不换，Agent 还能怎样进化？
02:05 SoL-Pi：寻找原本不需要发生的推理
04:10 降本与质量，放进同一本账
05:09 Harness²：让改流程的经验进入下一项任务
08:29 Rethinking：改框架，还是把任务再做几次？
10:12 长程游戏为什么给出不同结果？
11:32 集中讨论：改进信号、复用与成本摊销
13:52 总结：改什么、证据何在、是否值得

论文与链接
SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness（v1）
https://arxiv.org/abs/2609.20519v1

Harness²: Recursive Agent Harnessing for an Open World（v1）
https://arxiv.org/abs/2610.14224v1

Rethinking the Evaluation of Harness Evolution for Agents（2026-10-05 v4）
https://arxiv.org/abs/2607.12227v4

关键口径
SoL-Pi 完整效率方案的降本伴随平均分回落；Harness² 主实验另有框架编辑模型与试跑投入；Rethinking 的终端比较匹配执行轮数，游戏分数衡量完成与行动效率，并非通过率。三篇不是同一环境下的直接横评。

制作说明
Jeff／Ada 双人解读，依据公开论文制作，未复现实验。声音由本地 Qwen3-TTS 生成；内容经过来源核查与音频检查。面向有系统背景的 CS 听众，优先讲问题、核心思路与关键证据。
