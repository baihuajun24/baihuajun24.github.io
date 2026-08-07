0807 MLSYS 论文简报：你以为的路由收益，可能只是重跑噪声

Audio: 09:31

评论
今天换个打法：只深讲两篇，快速轮加长到四篇——今天这批真正过线的就两篇，与其硬凑不如讲透。两篇共用一句话：先量对东西，再谈优化。SAKI 发现大家优化的目标压根不是 attention 真正在用的量；路由那篇更狠，发现六模态路由看起来很大的收益，大半是重跑的噪声，而路由标签恰恰只在 agent 已经成功的地方才存在。两篇都评人上人。

本期重点
第一篇 SAKI（Cotality）。长上下文解码已经变成检索问题：8B 模型百万 token 的 bf16 KV cache 约 130 GB，真实系统先用一个 rank-r 的 key 索引粗选候选、再取精确 value，索引质量决定下游一切。现有两类做法——截断权重矩阵、或在激活分布下重建缓存张量——优化的都不是 attention 真正使用的量：attention 用的是 q 点乘 k 的打分排序，不是 key 的重建误差。把"key 侧低秩压缩造成的期望打分失真"直接写出来求期望，得到的是一个双边协方差加权的低秩逼近，打分算子被 query 与 key 的真实统计量从两侧夹住。关键结论：这个目标的 rank-r 最优解不是投影器，而是不对称的低秩双线性映射；由于正交投影器只是 rank-r 映射类的严格子集，所有 span-based 方法（含 PCA）在原理上就表达不了它。落地只要每个 head 一次校准前向加一次 128x128 的 SVD，两个因子还能离线折进权重。实测（LLaMA-3.1-8B 全 1024 个 head，4096 上下文）top-64 召回中位数 r=32 时 0.799 对 PCA 的 0.748，r=64 时 0.876 对 0.833；跨四个模型没有任何一个（模型, rank）格子输给 PCA；校准效率约 8 倍（512 token 校准即达 PCA 用 4096 token 的水平）。最漂亮的一点：理论预测的 per-head 打分 MSE 下降与真实 query-key 对上的实测下降，跨 1024 个 head 的 Pearson r 达到 0.9969。评级人上人。

第二篇是个负结果：Routing Is Least Learnable Where It Is Most Valuable（伦敦大学学院 / Holistic AI）。web agent 要操作网页得先"看见"页面——可访问性树（文本）、截图（像素）、或两者融合的标注图；今天这个选择建站时定一次、之后对所有任务不变。7686 次评分 episode、36 个条件之后，表面收益很诱人：六模态 oracle 成功率 7.1–51.9%，而最好的单模态只有 2.2–35.6%。但两刀砍下来：其一，先给"重跑一次"定价——同一条件什么都不改再跑一遍，就有 12.1–14.3% 的任务结果翻转，而真正加一个不同模态只多买到 +1.97 到 +7 个点，那个大 oracle 收益大半是六臂并集比一臂基线的虚高。其二，路由标签只在"有东西成功了"的地方存在，每个 cell 六个类合计仅 15 到 97 个标签，按每类最少十行筛，6 个 cell 里有 4 个根本训不出分类器——agent 成功率越低标签越稀缺，于是路由最该帮忙的地方恰恰最没有监督。唯一活下来的正收益是离线重组：保留最好模态、只把从没解出的任务丢给最便宜的臂，8 个 cell 全部省 9.5–30.6% 成本且成功率不变。论文还公开撤回了自己五条早先写死的结论。评级人上人。

快速一览：Comparative Approaches to Agent Retrieval over Large Skill Libraries（大技能库里怎么召回技能，正好接上昨天那篇 Wix 的确定性门，一个管召回一个管拦截）、RAC（端云切分推理的边界激活压缩编解码）、LLM Inference Under Bursty Workload Distribution（把排队论调度里需要预知的到达率换成在线估计，注意是模拟环境）、AV-AIVAT（anytime-valid 停机让 agent 评测证据够了就停）。

时间线
00:00 开场 · 今天为什么只深讲两篇
00:46 SAKI · KV 索引该优化打分失真而不是重建 key（人上人）
04:59 路由不可学 · 收益大半是重跑噪声（人上人）
08:12 快速一览 · 技能召回 / 切分推理 / 突发流量调度 / anytime-valid 评测
09:18 收尾

论文与链接
SAKI: Score-Aware Low-Rank Key Indexing with Random-Matrix Noise Correction for KV Retrieval — arXiv:2608.03228
Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents — arXiv:2608.06171
Comparative Approaches to Agent Retrieval over Large Skill Libraries — arXiv:2608.06196
RAC: Reference-Aware Activation Compression for Communication-Efficient Split LLM Inference — arXiv:2608.04991
LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm — arXiv:2608.06135
AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping — arXiv:2608.06362

制作说明
检索：watermark 窗口 08-06 至 08-07（14 小时），117 检索 / 90 候选，判 60 篇 → 6 篇入选。
格式：今天只有两篇过线，三个探索位候选出卡后均为 NPC，故改为两篇深讲加四篇快速，不硬凑第三篇。
文稿：两篇主讲全文 PDF 出卡定级，评级冻结于卡片。
音频：本地 Qwen3-TTS 合成，双主持 Jeff（uncle_fu）/ Ada（serena），未加速。
口径：SAKI 正文两处明说尚未投稿，不可当已发表；它只有 recall 代理指标，4K 上下文、单一校准域，全文无延迟/显存/吞吐等系统指标，绝对增益 0.748 到 0.799 对上线仍偏薄。路由那篇成功率仅 2–36%，仪器分辨率与效应量相当；重跑波动带只在 2 个 cell 实测、外推到另外 6 个；作者自述该负结论标记当下能力水位并预测自身会被推翻。快速轮里 WAIT 那篇全程为模拟环境且正文未给出吞吐与时延数字；AV-AIVAT 标题的 74 倍来自其引用方法 2018 年对弱基线的方差削减，该文自身证明的是 54 倍方差削减仅换来 1.37 倍更早停机。
