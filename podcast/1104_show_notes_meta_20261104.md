一段上下文，模型已经算过了，怎样才能不再算第二遍？本期分三段讲：存（FlatCake 把 KV 缓存的落盘决策提前到写入时）、传（ACCT 尝试跨规模模型直接转换 KV）和算账（The Physical Cost of Context 区分发送的 token 和真正重算的 token）。三篇是互补视角，并未共同验证一条完整流程。

时间线

00:00 开场：缓存为什么放不下、用不上、被改坏
00:29 FlatCake：存储层次在 Agent 负载上哪里失灵，写入时定位置
03:34 ACCT：跨模型转换 KV，以及摘要和表格之间的差距
05:55 算账：省 token 为什么可能多算
07:46 评级和三个问题

论文与链接

FlatCake: A Flat KVCache Storage Architecture for LLM Serving
复旦大学、北京大学等
https://arxiv.org/abs/2610.38355
说明：命中率 94% 对 64% 的对比对象是走主机中转的 Mooncake，它在低负载时命中率为 88%；直读显卡的 Mooncake-GDS 未在这条 trace 上运行，在 Llama 上 16K 打平、64K 差 1.8 倍。评测为单机。

ACCT: Asymmetric Cross-LLM Context Transfer
清华大学
https://arxiv.org/abs/2610.42116
说明：6.5 到 21.2 倍只算转换阶段，前提是上一个模型已算过这段上下文。计入其计算后，约 19K token 时小转大为 1.16 到 3.35 倍，大转小更慢。4 倍压缩下，六个方向在 11 个任务上赢过完整上下文的任务数为 4、4、2、2、1、0。评测均为单提示，没有多轮 Agent 交接。

The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents
加州大学圣迭戈分校、马萨诸塞大学阿默斯特分校，NeurIPS 2026 Resource-Aware Agentic AI 研讨会
https://arxiv.org/abs/2610.34763
说明：100 个 SWE-bench Verified 任务上，只留最近五条观测使 prompt 减少 33.3%，未缓存计算从 10.0k 涨到 70.8k token（增加 608.5%），GPU 能耗代理增加 125.6%，解决数 26 对 29。实验为单机串行，缓存处于最佳工况；该策略没有关缓存的对照。

本期评级

FlatCake：人上人。想法干净，基线还不够硬。
ACCT：NPC。方向新，但证据撑不起摘要。
The Physical Cost of Context：人上人。账本清楚，只是工况太理想。

主持：Jeff、Ada。音频由本地 Qwen3-TTS 生成。
