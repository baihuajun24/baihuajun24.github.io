0810 MLSYS 论文简报：别把上一步的输出当定稿

Audio: 09:33

评论
今天三篇干的是同一个动作：回头去改上一阶段已经定死的东西。量化把整数码当定局、记忆把老师的经验原样搬、技能库把检索到的文档直接塞进 prompt——三篇都说，那只是草稿。ReQuant 在冻住位宽与推理 kernel 的前提下反复翻整数码，Agent Memory Distillation 把老师记忆按学生能力重切粒度，SkillAligner 在执行前把检索到的技能重写一遍。三篇都评人上人，而且都罕见地诚实。

本期重点
量化这一步：ReQuant（北京大学 / 香港中文大学深圳 / 中兴）。训练后量化流水线产出一份整数分配就停了，权重一旦映到格点，这个离散决策就当最终答案；GPTQ 那套贪心逐列扫描里前面的列冻住、只让后面的列补偿。ReQuant 的观察是层重建损失按输出行可分解，行内对量化误差是凸二次，所以把一个坐标挪到相邻格点的损失变化有闭式解，从缓存梯度里 O(1) 可算，于是能做离散坐标下降。它接在任何已完成的 PTQ 输出之后，冻住位宽、scale、zero-point、格点布局、存储格式与推理 kernel，只反复翻整数码，且只接受严格降低重建误差的翻转，并有有限步终止证明。实测弱初始化收益很猛：Llama-3 8B W4A4+QuaRot 下 RTN 十任务均值 53.33 到 61.94，70B 上 32.78 到 66.93；低比特 W2A4 下 GPTQ 35.88 到 41.00、WikiText-2 困惑度 31.98 到 15.06。诚实点：对上已经很强的 GPTAQ，增益只有 0.04 到 0.81 分，低于它自己五个种子的正负 0.55 波动，也就是与噪声分不开；离线代价是初始化器的 5 到 16 倍。评级人上人。

记忆这一步：Agent Memory Distillation（KAIST / DeepAuto.ai）。小模型 agent 自己成功率低，攒出来的记忆库全是失败轨迹，所以记忆系统在小模型上基本没用；而把大老师的记忆原样塞给学生也不行，老师写的是先登录再放歌这种高层策略，学生根本不会执行登录那一步。洞察是记忆的粒度与表示形式要和学生能力对齐，而且这点被做成了消融：子任务记忆用代码格式 49.40 对纯自然语言 23.21，工作流记忆反过来自然语言 49.40 优于代码 44.05。老师只从成功轨迹抽三层记忆，工作流与子任务开场注入，函数级记忆只在工具报错时按函数名反应式检索，全程只取一条、不训练任何参数。Qwen3-4B 在 AppWorld 上 14.88 到 49.40，逼近老师 GPT-5-mini 的 50.00；五次重复 49.60 正负 0.91。诚实点：标题里的蒸馏有轻微夸大，它不更新任何参数，本质是免训练的结构化 prompt 注入；收益高度集中在 AppWorld，ToolSandbox 只有 3.4 个点；最反直觉的是老师不是越强越好，更强的老师带 4B 学生反而不如较弱的老师。评级人上人。

技能这一步：SkillAligner（浙江大学）。先给了一个很值钱的诊断：语义相关不等于执行有用。把检索到的 top-5 技能文档原样注入，会把本来做对的任务变成失败，九个设定里全部出现这种技能引起的退化，比例 5.80 到 17.91，而且换更强的模型不解决。原因是查询、执行接口、以及同时检索到的其它技能三者都在变，所以这个技能该怎么用没法提前写死。做法是执行前加一次 LLM 调用，把 top-5 技能连同执行规范一起重写成一份四字段的紧凑指南，免训练、与检索器无关。九个设定平均 47.07 到 58.17，退化率 17.91/9.40/10.29 降到 2.24/2.80/3.57。诚实点：38.26% 的净 token 节省是平均值且被 SearchQA 拉高（SearchQA 62.77% 对 ALFWorld 26.33%）；指南生成后全程冻结，轨迹中途发现不匹配也改不了；退化原因的分类由另一个大模型打标、未报人工一致性。评级人上人。

快速一览：Routing LLM Inference to the Cleanest Grid（生产 GPU 路由器上的碳排放项，线上实测只省 1.45%，约 51% 来自一整年历史回放的建模值）、A Picture is Worth a Thousand Tokens（爱立信，把电信 KPI 时序画成二维图喂 VLM，输入 token 降 3.6 到 10.4 倍、实测每查询 GPU 能耗降 1.8 到 2.5 倍）、DASH（自蒸馏里把每 token 的损失权重改成由散度决定的自适应门控）。

时间线
00:00 开场 · 三篇干的是同一个动作
00:39 ReQuant · 量化后回头翻整数码（人上人）
03:32 Agent Memory Distillation · 老师记忆按学生能力重切粒度（人上人）
06:23 SkillAligner · 执行前把检索到的技能重写一遍（人上人）
08:28 快速一览 · 碳感知路由 / VLM 看图省 token / 自蒸馏门控
09:21 收尾

论文与链接
ReQuant: Fixed-Grid Discrete Refinement for Post-Training Quantization — arXiv:2608.07019
Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory — arXiv:2608.07169
SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time — arXiv:2608.06880
Routing LLM Inference to the Cleanest Grid in Real Time — arXiv:2608.06188
A Picture is Worth a Thousand Tokens: How Vision Language Models Cut AI Energy — arXiv:2608.07427
DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation — arXiv:2608.06243

制作说明
检索：watermark 自动补上周末缺口，窗口 08-07 至 08-10，286 检索 / 220 候选，判 60 篇 → 6 篇入选，无 truncation。
文稿：五篇候选全文 PDF 出卡，择优取三篇主讲，评级冻结于卡片；两篇出卡 NPC 的降为快速轮。
音频：本地 Qwen3-TTS 合成，双主持 Jeff（uncle_fu）/ Ada（serena），未加速。
口径：各篇数字均为论文自报，硬件与基准不同不可横比。ReQuant 的增益集中在弱初始化，对强初始化的提升低于其自身种子波动，离线代价为初始化器的 5 到 16 倍。Agent Memory Distillation 不更新任何参数（作者正文自述 training-free），标题的"蒸馏"易被误读，收益集中在单一基准。SkillAligner 的 token 节省为被单一基准拉高的平均值，其指南全程冻结，退化归因由模型打标且未报人工一致性。快速轮的碳感知路由线上实测仅 1.45%，其大数字为历史回放建模值。
