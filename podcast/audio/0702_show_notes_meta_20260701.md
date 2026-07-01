# 0702 MLSYS 论文简报：给长思维链省 token 的三种打法

> 本期三篇论文盯着同一个敌人——长思维链（long CoT）动辄上万 token 带来的延迟与显存开销，从调度、KV cache、推理表征三个层面各出一招。
> 音频不口播 arXiv 编号，编号见下方链接。

## 内容时间戳
- 00:00 开场 · 今日三篇导览（三篇都在砍长思维链的 token 开销）
- 01:01 ① LASER：负载感知 early-exit，边缘 serving 按实时负载动态决定"想多深"（系统/调度）
- 04:12 ② EpiKV：不看 attention、从 residual stream 打分的 KV cache 驱逐（推理系统）
- 07:58 ③ CLSR：多 agent 自主进化符号语言，精度不变、token 降 3–6×（多智能体/token economy）
- 11:10 📌 引用观察 · 投机解码"草稿何时被接受"的理论
- 11:45 收尾 · 三篇小结

## 本期主讲

### ① LASER · 边缘 serving / early-exit 调度 · 评级：人上人
- **Load-Aware Serving with Early-Exit for Reasoning LLMs at the Edge** — arXiv 2606.31580 · 北京师范大学（珠海）+ 澳门大学
- 亮点：把 reasoning 模型的 confidence-based early-exit 从"单请求、固定阈值"升级成"负载感知的可调度变量"。两个机制：(1) 用 tanh(EMA 负载) 在一个事先验证过的安全区间里在线微调 exit 阈值——负载高早停、负载低多想；(2) 按题目难度 + 当前负载给每个请求预分一个 token 预算作为硬上限。
- 数字：平均延迟降 17–38%、SLO 达成率 +3–6pp，平均精度代价约 1%（注意是平均，个别 benchmark 掉到约 5pp）；token 压缩 42–80%；突发流量下延迟砍约 22%。
- 诚实声明：系统级数字来自离散事件仿真（单张 RTX 4090、两个 4–7B 小模型），非线上真部署。

### ② EpiKV · KV cache 驱逐 / 推理系统 · 评级：人上人（偏夯）
- **Epiphany-Aware KV Cache Eviction Without the Attention Matrix** — arXiv 2606.26472 · Carnegie Mellon University
- 亮点：现有 KV cache eviction 几乎都按 attention 权重排 token 重要性——信号噪声大，还逼模型物化 n×n attention 矩阵、用不了 FlashAttention。EpiKV 改用 epiphany score：token 前后 residual stream（隐藏状态）的 L2 变化量，直接从前向传播读出，不碰 attention 矩阵、FlashAttention 兼容、免训练。背后有可解释性支撑（中间层与偏上层变化方向相反的两个 band，取差值）。
- 数字：MATH-500、缓存压到 4096 时准确率 72%（H2O 67%），离无损天花板 75% 仅差约 3 点；比最快的 attention 基线快约 1.6×；FlashAttention 让可行上下文从 eager 8192 就 OOM 撑到 65,536 token；缓存极小（1024）时 H2O 崩到 5%，EpiKV 仍站得住。
- 诚实声明：单模型（DeepSeek-R1-Distill-LLaMA-8B）验证；AIME 仅 30 题，作者明确说属方向性证据；主打"近无损省显存/提吞吐"，非宣称精度大涨；部分吞吐数字为投影。

### ③ CLSR · 多智能体 / token economy（探索性） · 评级：人上人
- **When LLMs Develop Languages: Symbolic Communication for Efficient Multi-Agent Reasoning** — arXiv 2606.29354 · 中国科学院计算技术研究所 + 国科大
- 亮点：自然语言 CoT 对机器不是信息密度最高的表达。CLSR 让多个 black-box LLM agent 自主发明、演化、共享一套紧凑符号语言（LSF：符号表+语法+使用规则），离线用 Pareto 准则（先对错、再省 token）一代代进化出一批，在线由一个 latent-free router 按 query 挑选/组合。等于"给机器造方言并让方言优胜劣汰"。
- 数字：保持精度基本不变下生成 token 降 3–6×（约省 3/4）。例：8B 模型 GPQA 从 73.2%/5380 token → 73.1%/1326 token；Qwen3-32B 在 MATH-500 从 845 → 206 token、精度纹丝不动。
- 诚实声明：离线语言进化很贵（8×RTX 4090 跑数天、需带标准答案的样例）；最亮眼的精度数字来自较费 token 的模式，默认 router 模式有时以少量精度换 token。（注：论文文件套用了会议模板，接收与否未独立核实，本节目不据此背书。）

## 📌 引用观察
- **When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding** — arXiv 2606.30265。给贪心解码 / 放松接受准则 / 树状候选这些实际系统常用、但过去理论没覆盖好的设定，补了一个"草稿何时被接受"的理论刻画。

## 制作元信息
- 文稿：双人对谈（Jeff 主讲系统两篇 + Ada 主讲多智能体一篇并负责质询）。
- 音频：本地 Qwen3-TTS 合成，约 12:09。
- 主持：Jeff（系统）· Ada（算法）。
- 口径：论文数字均据原文，每篇附诚实声明；arXiv 编号不口播、仅留链接。
