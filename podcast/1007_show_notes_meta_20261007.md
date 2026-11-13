1007 MLSYS 论文简报：Agent 写 GPU kernel 的三道坎

编程 Agent 已经能写出正确的 GPU kernel，但“能运行”与“足够快、方便验证”之间，还有很长一段路。本期沿着真实开发流程读三篇论文：先看接口如何改变 Agent 的搜索空间，再看测量反馈怎样支持逐应用专用化，最后看真实设备上的调试工具怎样保住出错现场。

本期重点

SyclKittens 把 Intel GPU 的矩阵布局、预取与通信经验做成可编程的 tile 操作。固定同一 Agent、任务和反馈预算的单 GPU 矩阵乘实验里，最快正确结果从 oneDNN 的 57.5% 提升到 82.1%。论文另有人和 Agent 共同打磨的整套 kernel 与端到端推理结果；这两层证据不能混同。

ForgeStencil 让 Kernel Agent 为具体 stencil 配置合成 CUDA，再让 App Agent 找到真实应用中值得优化的热点。100 个已验证工业与科学计算应用的端到端中位加速为 1.41 倍。值得注意的是，其中 17 个改进不需要新的设备 kernel，只改 host 侧或程序结构。

PKDB 针对 PyKokkos，把 Python 调试器与 GPU/CPU 设备侧调试器接通。它支持断点、变量检查、现场执行与 kernel 调用热替换，让开发者在真实设备状态里找错误，不必一律退回串行 CPU 环境。它不是 Agent 系统，而是生成代码之后的调试反馈工具。

集中讨论

三篇覆盖不同硬件与框架，不构成一条已经集成的生产线。SyclKittens 的接口收益有任务与模型差异；ForgeStencil 的 100 个应用是验证通过的集成集；PKDB 当前主要覆盖 PyKokkos。接下来更值得追问的是，把接口、专用化和调试接起来后，端到端的性能收益是否超过模型调用、编译、测量和人工验证的总成本。

时间线
00:00 开场 · 三道坎
00:42 SyclKittens · 原始接口为什么慢
01:49 把硬件经验放进 tile 接口
02:23 同预算受控实验
04:04 ForgeStencil · 通用性税
05:24 Kernel Agent 与 App Agent
06:22 一百个应用的端到端加速
07:58 PKDB · 真实设备上的调试
08:34 断点、现场执行与热替换
09:34 调试开销与适用范围
10:20 集中讨论
11:28 收尾

论文与链接

SyclKittens: A Tile Programming Model for Programmers and Coding Agents on Intel GPUs
https://arxiv.org/abs/2610.04277

ForgeStencil: Automating Per-Case Stencil Specialization from Kernels to 100+ Real Applications
https://arxiv.org/abs/2609.06694

Interactive Debugger for Performance Portable Python HPC Kernels
https://arxiv.org/abs/2609.07912

Jeff 与 Ada 主持。本期音频由本地 Qwen3-TTS 合成。
