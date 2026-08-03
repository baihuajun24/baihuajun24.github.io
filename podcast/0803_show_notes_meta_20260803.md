# 0803 MLSYS 论文简报：给推理省钱的三个层面
Audio: 08:42

> 给大模型推理省钱，可以从三个层面下手：少解码几步、每个 token 少算一点、把 KV cache 里没用的早点扔掉。今天三篇正好各占一个层面，都训练无关、都有真实加速。

## 内容时间戳

- 00:00 开场 · 给推理省钱的三个层面
- 00:46 SparseSpec-L（中国科学技术大学）· 自投机解码，草稿用可召回稀疏 KV
- 02:36 WIDE（东方理工 / 慕尼黑 LMU）· token 级动态宽度剪枝 + 算子协同
- 05:16 Back from the Future · 逆因果惊奇度做 KV 驱逐
- 08:12 快速一览 · ReTopK / ARES
- 08:39 收尾

## 本期主讲

**1. WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning**（东方理工 / 慕尼黑 LMU，arXiv:2607.28418）
结构化剪枝的老毛病：静态剪枝对所有输入一刀切、砍狠了精度掉；动态剪枝又只会粗粒度地跳整层、跳子模块，不规则执行在硬件上跑不出真加速。WIDE 把动态路由从"跳整层"下推到 token 级的宽度——每个 token 自选注意力头组与前馈通道组——再配一个 GPU 算子协同设计：把每个 token 稀疏的掩码重排成连续块，让细粒度稀疏也保持稠密式高效访存，不用物化 token 专属权重。50% 稀疏下精度保住八成六到八成八，比只会跳层的动态基线最高高出二十多个点；算子层面预填充最高 1.98×、解码 4.95×，端到端预填充 1.68×、解码 1.55×。学出来的稀疏注意力砍到 66%、前馈只砍 28%。诚实点：只在两个 Llama 模型上验证，端到端 ~1.6× 远低于算子上限，50% 稀疏绝对精度仍掉约 13 点。评级：顶级。

**2. A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding (SparseSpec-L)**（中国科学技术大学，arXiv:2607.27735）
投机解码要草稿便宜、接受率高、还能一次猜够长，三者常顾此失彼：训练小草稿泛化差，静态压 KV 又永久丢上下文、长文接受率崩。SparseSpec-L 让目标模型自己当草稿，用一份"可召回"的稀疏 KV——重要性分数从上一次全量验证的注意力统计里免费回收，稠密 KV 一个不扔、只在起草时用稀疏视图，目标分布不变；再用熵控制器在线选投机步长。长上下文最高 2.79×、接受率 72.9%、平均一次过 11 个 token，另一长文基准 2.60×。它给了个干净的公式解释"步长不是越长越好"（边际接受率低于相对草稿成本时加速回落）。诚实点：加速建立在非 FlashAttention 的验证核上、对优化引擎是否提速未测，单卡 ≤64K、输出 128 token，且自承认不是首个稀疏-KV 自投机。评级：人上人。

**3. Back from the Future: Key-Value Cache Management by Counter-Causal Surprise**（Metacognition AI / 澳国立 / 阿德莱德，arXiv:2607.27600）
换个角度问 KV cache 该扔谁：一个 token 若光看它后面的内容就能预测出来，就是冗余可扔——用"逆因果惊奇度"（1 减去从未来预测该 token 的概率）当保留信号。实现上把因果掩码换成上三角、每个位置只看其后位置，复用已存 K/V、只重算 query，全程不训练。全量成本是序列平方乘层数，故给了个只用最后一层的快速近似，刷新延迟 54ms→7.9ms（快 7–9 倍），代价是多存约占 KV 12% 的中间激活。MATH500 上四个模型里三个是最优驱逐法、AIME 上也是驱逐法里最好，但离满 cache 仍有差距。诚实点：增益温和、部分结果只在图里、未与最近更强的驱逐法正面比、全量版预填充成本近翻倍。评级：人上人。

## 快速一览

- Recall Before You Rank (ReTopK)（arXiv:2607.27692）· 训练无关地复用历史 Top-K 选择、省稀疏注意力选择器开销，128K 下几乎不掉精度、注意力提速 3×。
- ARES: Adaptive Reasoning-Effort Steering（arXiv:2607.27879）· 按每次调用自适应分配 reasoning 力气、带显式美元成本核算，用在 agent 回路做成本感知推理。

## 论文与链接

- WIDE — arXiv:2607.28418
- SparseSpec-L — arXiv:2607.27735
- Back from the Future — arXiv:2607.27600
- ReTopK — arXiv:2607.27692
- ARES — arXiv:2607.27879

## 制作元信息

- 检索：watermark 自动补 07-29→08-02 跳过批次，874 篇检索 / 678 候选 → Claude-as-judge（8 子代理）判 60 → 8 入选。
- 三篇主讲全文 PDF 出卡定级（评级冻结）：WIDE 顶级 / SparseSpec-L 人上人 / Back-from-the-Future 人上人。
- 音频：本地合成（mlx-audio Qwen3-TTS-12Hz-1.7B-CustomVoice），双主持 Jeff（uncle_fu）/ Ada（serena），1.0x。
- 口径：各篇加速倍数为论文自报、硬件与基准不同不可横比；主讲边界见正文诚实点。
