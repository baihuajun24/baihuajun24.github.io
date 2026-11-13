音频：10:19 · 本地 Qwen3-TTS · 双主持 Jeff / Ada

CodeMidas 不发明新的 RL 算法，而是研究如何从正常工作的开源代码库里，反向生产 coding agent 可操作、可自动判分的训练环境。

本期从一个“挖空已有功能”的例子出发，依次讲任务设计、reference-grounded tests、容器清理、对抗式泄漏探测、verifier 审查与难度筛选。核心结果是：MiMo-V2.5 用这批环境做 GRPO 后，五类外部评测均提升；高质量 3k 环境在三项消融评测上胜过未经完整清理和筛选的 vanilla 8k。

评论
代码文本很多，可信的训练环境却不够。CodeMidas 把已有功能反向编译成“可操作、可判分的软件世界”；难的不是挖空代码，而是让题目和判分真正可靠。

时间线
00:00 代码很多，可信的 RL 环境为什么少？
00:54 从 issue、commit 到“源码自己出题”
01:26 挖空功能：原实现同时成为行为 oracle
02:17 如何避免把偶然实现细节写进测试
02:40 隐藏 verifier 与判分接口
03:33 六次容器一致性检查及泄漏探测
04:33 5,545 个任务的环境工厂
04:57 MiMo-V2.5、GRPO 与五类外部结果
05:54 高质量 3k 为什么能赢 vanilla 8k
06:37 Agent 的读代码与自检行为
07:13 Function-Aware FIM：同样用源码，不同训练阶段
08:06 集中讨论：证明了什么，还缺什么对照？
08:43 哪层 QA 最值钱，造环境到底多贵？
09:44 结论：环境本身成了基础设施

论文与链接
CodeMidas: Scaling Agentic Coding RL Environments from Code Itself
https://arxiv.org/abs/2609.22068
Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models
https://arxiv.org/abs/2607.12463
R2E-Gym
https://arxiv.org/abs/2504.07164
SWE-smith
https://arxiv.org/abs/2504.21798

制作元信息
以 arXiv 原文为技术事实来源。CodeMidas 结果为作者报告，不是不同论文之间的直接排行榜。ProgramBench 的 21.5 是 Almost Solved，即至少通过 95% hidden tests 的任务比例，不是 fully solved。本期为 AI 合成双主持音频。
