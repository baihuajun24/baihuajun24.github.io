# 0706 MLSYS 特辑 · RL 的瓶颈，怎么成了「环境」？

## 评论

当 agent 要在真实 sandbox 里一遍遍试错，卡住 agentic RL 吞吐的往往不是 policy
gradient，而是环境本身：怎么建、怎么复位、要不要建。本期用三篇论文串一条线——把环境
复位做到毫秒级、把环境和训练解耦、再到干脆把环境从奖励回路里删掉。读这波论文的方法论：
别只看 SWE-bench 涨了几个点，去看它对「环境」这层动了什么刀。

## 本期重点

这是一期关于 agentic RL「系统底座」的特辑。过去两三年，RL 的讨论集中在 reward 设计和
policy 更新；但当 agent 变成在 sandbox 里真敲命令、改磁盘、改进程的存在，训练与测试期
的高频存档/回滚、以及每个仓库的环境搭建，正在成为吞吐的真正瓶颈。

我们按「递进的三个动作」组织：

- **复位环境**：上海交大 IPADS 与华为的 **DeltaBox**，用 OS 层的 DeltaState 抽象
  （DeltaFS 分层 copy-on-write + DeltaCR 从冻结模板 fork），把 sandbox 的 checkpoint
  压到十毫秒级、rollback 一两毫秒；对照香港科技大学的 **Crab**（eBPF 语义感知，>75%
  的 turn 无需存档）。
- **解耦环境**：NVIDIA 的 **Polar**，把 agent harness 当黑盒，用 API proxy 记录
  token 级交互、重建 token-faithful 轨迹，异步喂给独立 trainer；简单 GRPO 就把
  Qwen3.5-4B 在 SWE-Bench Verified 上跨多种 harness 提了最多二十多个点。同一方向还有
  清华与 Z.AI 的 **AgentRL**、小红书的 **Relax**。
- **删掉环境**：上海交大与抖音的 **Dockerless**，提出环境无关的 agentic verifier，
  不执行代码、靠仓库探索判 patch 对错，构成全程无环境的后训练管线，并追平基于真实环境
  的后训练——与 DeltaBox 恰好构成一组正反命题。

最后用 iFlow 的 **ALE 生态**（ROLL + ROCK + iFlow CLI，ROME，IPA 按语义交互块分
credit）作为「完整分工长什么样」的收尾锚点。

## 时间线

- 00:00 开场：agentic RL 的瓶颈，正从训练算法搬到「环境」
- 01:01 DeltaBox（上海交大 IPADS · 华为）· 毫秒级 sandbox checkpoint/rollback（对照 HKUST 的 Crab）
- 03:47 Polar（NVIDIA）· 把 agent harness 当黑盒、解耦训练（旁及 AgentRL、Relax）
- 05:48 Dockerless（上海交大 · 抖音）· 环境无关的 agentic verifier：删掉 Docker
- 08:04 ALE 生态收尾：ROLL / ROCK / ROME 与 IPA
- 09:37 总结与「看它对环境这层动了什么刀」的方法论提醒

## 论文与链接

- DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback — 上海交大 IPADS · 华为 — arXiv:2605.22781
- Polar: Agentic RL on Any Harness at Scale — NVIDIA — arXiv:2605.24220
- Dockerless: Environment-Free Program Verifier for Coding Agents — 上海交大 · 抖音 — arXiv:2606.28436
- Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes — HKUST — arXiv:2604.28138
- WEBSERV: A Full-Stack and RL-Ready Web Environment for Training Web Agents at Scale — Northeastern · Amazon — arXiv:2510.16252
- ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents — NVIDIA — arXiv:2603.18815
- AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework — 清华 · Z.AI — arXiv:2510.04206
- Relax: An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at Scale — 小红书 — arXiv:2604.11554
- Let It Flow (ROLL / ROCK / ROME, ALE 生态) — iFlow · ALE 联合团队 — arXiv:2512.24873

## 制作元信息

- 文稿：主题特辑，源自公开 arXiv 论文，人工撰写脚本、逐段事实核对（机构、标题、关键数字
  均对 PDF 首页/摘要复核）。
- 音频：本地合成（mlx-audio Qwen3-TTS-12Hz-1.7B-CustomVoice），双主持 Jeff / Ada。
- 主持：Jeff（系统/基础设施视角）· Ada（算法/推理视角）。
- 口径：本期只讨论公开论文与其公开基准；话题由一条小红书帖引出，但该帖正文未能打开，
  未作为事实来源，论文清单为独立复核确认。
- 数字口径：DeltaBox 采用 v2 正文的 checkpoint 约十毫秒 / rollback 一两毫秒（v1 摘要
  的 14ms/5ms 未采用）。
