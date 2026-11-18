Harness 不再是写死的脚手架。本期三篇论文问的是同一件事：包在模型外面的提示词、工具和控制逻辑，能不能不靠人手写，改了之后又怎么确认没改坏。一篇靠开发集挡回退，一篇靠留出集加经验回放，一篇靠干净沙箱重放。三篇是互补视角，并未共同验证一条完整流程。

时间线

00:00 开场：脚手架能不能自动改，又怎么确认没改坏
00:37 AutoSaddler：从执行轨迹生成结构化补丁，两道验证关
02:43 ModHarness-RL：把脚手架写成小程序，改动先过经验回放
05:07 HerAgent：语义块检查点，写回脚本再干净重放
07:23 评级和读法

论文与链接

AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces
微软、POSTECH、KAIST 等
https://arxiv.org/abs/2608.23041
说明：三个长程基准上对基础脚手架的提升：GAIA2 Pass@1 53.0% 到 62.0%；SWE-Bench Pro 37.3% 到 46.9%；Terminal-Bench 2.0 40.0% 到 50.0%，高于专家调优的 Terminus KIRA（47.5%），以及自动基线 GEPA（42.5%）和 Meta-Harness（43.3%）。可执行的能力补丁后续回退率 8%，纯文字补丁 17%。主实验中每种优化算法只做了一次搜索；优化器依赖闭源强模型；方法要求任务有标准答案且任务相互独立。预印本。

ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL
宾夕法尼亚州立大学、领英、加州大学圣巴巴拉分校
https://arxiv.org/abs/2611.18533
说明：代码定位任务（SWE-Bench Lite、Verified、Pro 平均 F1）上，四个设定均高于固定手写脚手架 14% 到 24%，比各设定下最强基线高 5% 到 12%；Qwen3-8B 上下文受限设定 F1 从 0.333 到 0.412。完整系统与第三方基线只在这一个任务上跑过，另两个环境只测了单个模块；程序生成与裁判依赖外部闭源模型；门控用 128 个任务单次评估。预印本。

HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup
伦敦大学学院、乌普萨拉大学、卡内基梅隆大学
https://arxiv.org/abs/2611.18443
说明：Installamatic-Bench 52.0% 到 85.0%（gpt-4o-mini），SetupBench 对 OpenHands 46.3% 到 70.4%，成本 0.12 美元对 2.20 美元；Repo2Run-Bench 86.0% 到 87.1%，仅高 1.1 个百分点。去掉补丁写回成功率降到 25.9%。对照数字取自原论文，未统一重跑，Installamatic 基线用 any@10、本方法用 any@3；跨块回滚在全部实验中仅触发 20 次。预印本。

主持：Jeff、Ada。音频由本地 Qwen3-TTS 生成。
