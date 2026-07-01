# 0623 MLSYS 论文简报：执行态检查点、token 级解耦与 agent 4-bit KV 缓存
Audio: 11:21

> 基于 2026-06-22 晚间完成的 arXiv 论文召回与筛选；音频不朗读链接。

## 内容时间戳
- 00:00 开场 · 0623 MLSYS 论文简报
- 00:26 ① Execution-State Capsules：图绑定执行态检查点与恢复（系统 / 低延迟设备端推理）
- 04:09 ② ADaPT：面向高效大推理模型的 token 级解耦（算法 / 推理开销）
- 07:12 ③ UltraQuant：长上下文 agent 的 4-bit KV 缓存（算法 + 系统，探索方向）
- 11:00 收尾 · 三篇小结与阅读优先级

## 本期主讲

### ① Execution-State Capsules · 系统 · 评级：夯（Jeff champion）
- **Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving** — arXiv 2606.20537
- 亮点：系统方向最佳论文，提出一种图绑定的执行态检查点与恢复机制，面向低延迟、小批量、设备端的 Physical-AI serving。

### ② ADaPT · 算法 · 评级：顶级（Ada champion）
- **ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models** — arXiv 2606.19919
- 亮点：直指大推理模型（如 o1 / DeepSeek-R1）的推理开销问题，做 token 级解耦以提效。

### ③ UltraQuant · 算法 + 系统（探索） · 评级：夯（Jeff champion）
- **UltraQuant: 4-bit KV Caching for Context-Heavy Agents** — arXiv 2606.20474
- 亮点：长上下文 agent 场景下的 4-bit KV cache，算法与系统结合得很好，是当前竞争激烈的方向。

## 制作元信息
- 文稿：双人对谈（Jeff 系统 · Ada 算法）。
- 音频：本地 Qwen3-TTS（mlx-audio）合成，约 11:21。
- 主持：Jeff（voice `ryan`）· Ada（voice `vivian`）。
- 口径：arXiv 编号不口播、仅留链接。
