# 0703 MLSYS 论文简报：顺着长上下文，从 KV cache 到 agent 记忆的三层省法
Audio: 09:31

> 三篇顺着「长上下文 / 长推理」这条线，从下往上各出一招：serving 层压 KV cache、推理层决定"想多久"、agent 层学"怎么记"。
> 音频不口播 arXiv 编号，编号见下方链接。

## 内容时间戳
- 00:00 开场 · 三篇顺着长上下文 / 长推理，从下往上各出一招
- 00:23 ① MosaicKV：serving 层同时压 KV cache 的两个维度（系统 / 长上下文服务）
- 03:53 ② CAT：用模型自信度决定"想多久"，省 token 还涨精度（token economy）
- 06:28 ③ AutoMem：把记忆管理学成一门可训练技能（agent 记忆 / 探索）
- 09:05 收尾 · 三篇小结

## 本期主讲

### ① MosaicKV · serving / KV cache · 评级：夯
- **MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression** — arXiv 2607.00760 · 上海交通大学 IPADS
- 亮点：长上下文 serving 里 KV cache 是头号成本（8 并发 × 128K 用 LLaMA-3.1-8B 要 128GB＝权重的 8×，1M 时 64×）。现有方法只压一个维度（序列如 Quest，或通道如 ThinK），天真叠加会崩（反例：通道压 30% 掉 24.5%、70% 掉 82.8%）。MosaicKV 同时压两维、且贯穿整个 decode：靠 per-vector 选元素 + per-segment 自适应策略保精度；又发现 decode attention 是带宽瓶颈（带宽利用率 90%、CUDA core 仅 10%、CPU 闲置），把稀疏 attention 塞进闲置的 CUDA core/CPU。
- 数字：相比不压缩基线，attention 最高 16×、解码延迟降到约 1/4.8、吞吐最高 7.3×，显存 3×，精度平均只掉 1.76%（LongBench + RULER）。
- 诚实声明：以上是峰值；平均约解码 3.8× / 吞吐 5.5×；个别模型（Ministral）RULER 掉 3.55%；>512K 的部分数字为按层采样外推；仅加速 decode（prefill 是未来工作）。

### ② CAT · token economy / adaptive compute · 评级：人上人
- **CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models** — arXiv 2607.00862 · 电子科技大学（UESTC）
- 亮点：大推理模型对简单题"过度思考"浪费 token；现有方法要么一刀切砍长度（伤难题）、要么用粗粒度难度估计。CAT 用模型自己的自信度（每步 token 分布离均匀分布多远）当细粒度难度信号——它能分开答对/答错轨迹且对长度不敏感——据此构造偏好对（对的偏短"简洁对"、错的偏长"深思对"）+ 置信度加权的偏好优化。
- 数字：R1-Distill-Qwen-7B 在 MATH-500 从 91.7→93.9 且省约 1/3 token；AIME24 53.3→58.9；GPQA 49.2→54.0。罕见地在压缩同时还涨精度。
- 诚实声明：其压缩率其实低于更激进的方法，卖点是"精度-压缩折得最好"而非砍最狠；只报 token 下降、没有墙钟加速；仅 STEM 任务、训练仍依赖 ground-truth 正确性。

### ③ AutoMem · agent 记忆（探索性） · 评级：夯
- **AutoMem: Automated Learning of Memory as a Cognitive Skill** — arXiv 2607.01224 · Stanford University
- 亮点：长程 agent（游戏，几千到十万步）远超上下文，一个坏的记忆决定会潜伏几百步才发作、人无法逐条 review。AutoMem 把文件操作（读/写/搜索/追加）提升成与任务动作平级的一等动作——每个记忆决定都可追溯，一个前沿元模型就能像 code review 一样看完整条轨迹、指出错在哪一步。两个外层循环：元模型重写记忆结构/schema；再用 LoRA 把"记忆专家"小模型在 agent 自己的好决定上微调出来。
- 数字：底座 Qwen2.5-32B，只优化记忆就拿 2–4× 提升：Crafter 25→51%、MiniHack 7.5→30%、NetHack 0.42→1.85%，据称让 32B 开源模型在这些游戏上追平 Claude Opus 4.5 / Gemini-3.1-Pro；NetHack 每步记忆从 138 字符压到 6（−95%），冗余写入降 68–83%。
- 诚实声明：记忆一局一清、无跨局持久化；仅 3 个程序生成游戏、无真实/工具任务；第二个循环（LoRA 记忆专家）的增益误差棒重叠、统计不显著；强依赖前沿元模型（Claude Opus）当 reviewer。

## 制作元信息
- 文稿：双人对谈（Jeff 主讲 serving 一篇 + Ada 主讲推理/agent 两篇并互相质询）。
- 音频：本地 Qwen3-TTS（mlx-audio）合成，约 09:31。
- 主持：Jeff（系统）· Ada（算法）。
- 口径：论文数字均据原文，每篇附诚实声明；arXiv 编号不口播、仅留链接。
