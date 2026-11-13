内存不够时，KV 缓存该丢头，还是丢尾？本期三篇论文都想让 Agent 少做重复工作：Penelope 改变 KV 淘汰的位置和粒度，SWE-Trail 用历史决定在哪里多采集训练轨迹，Exo 让 Agent 在任务运行中修改自己的 harness。三篇是互补视角，并未共同验证一条完整流程。

时间线

00:00 开场：丢头还是丢尾
00:25 Penelope：重算为什么越靠后越贵，以及消融表里的答案
03:12 SWE-Trail：历史留给采集器，不进 Agent 的上下文
05:14 Exo：边干活边改自己，以及守护层到底守什么
07:25 评级和读法

论文与链接

Rethinking KV Cache Eviction for Agentic LLM Serving
弗吉尼亚理工大学、加州大学默塞德分校等
https://arxiv.org/abs/2611.00391
说明：和 SGLang 比，平均首 token 时间 6.7 秒降到 2.7 秒，是并发扫描的峰值，缓存为人为封顶。消融显示，只改成块级释放（仍从尾部）即减少 45%，节点级下只改位置减少 6%，完整方案 63%。相对块级尾部淘汰，净位置效应为 12% 到 29%。工具等待占主导的负载上，任务完成时间约缩短 2%。没有运行先前的同类策略。

SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training
康涅狄格大学、蚂蚁集团
https://arxiv.org/abs/2611.02074
说明：相对独立采样提升 2.33 和 1.60 个百分点。同流程不用历史的差距为 2.22 和 0.87，95% 置信区间都跨零。每种条件只采集一批语料，重复训练三次。“最多多 3.7% token”不含先跑五条历史的成本。

Exo: A Harness Architecture for Runtime Self-Improvement
加州大学伯克利分校等
https://arxiv.org/abs/2611.00463
说明：AppWorld 留出任务每题成本 0.141 美元对 0.359 美元，通过率都是 96.9%，含学习总成本低 43%。留出任务是同一批场景的其他变体。游戏实验每种条件只跑一次，没有同起点对照。默认守护层只检查构建是否成功。重复度低的任务上比 Codex 和 Pi 更贵。

本期评级

Penelope：人上人。想法清楚，但收益大头来自块级释放。
SWE-Trail：人上人。设计干净，历史的增量还没被统计证实。
Exo：人上人。架构清楚，头条数字的对照不够干净。

主持：Jeff、Ada。音频由本地 Qwen3-TTS 生成。
