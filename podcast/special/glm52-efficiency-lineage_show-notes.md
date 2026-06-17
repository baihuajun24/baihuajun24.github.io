# GLM-5.2 的效率谱系：从多 token 预测到稀疏注意力索引（公开版）

## 评论

GLM-5.2 那两个效率数字——投机解码接受长度 +20%、IndexShare 在 1M 上下文下省 2.9× 算力——到底从哪来？这一期把它拆回 MTP、DeepSeek 和稀疏注意力索引这几条公开技术链，并分清哪些是官方口径、哪些被公开论文坐实。

## 本期重点

GLM-5.2（智谱/Z.ai，开源 MIT）的两个效率卖点，本质是两条公开技术链的工业合流。第一条：多 token 预测（MTP）从训练目标变成推理期的草稿器——Meta 的 MTP 论文打通这一跳，DeepSeek-V3 把它工业化。关于"接受长度 +20%"，关键不在更花哨的草稿头，而在把草稿的 KV 与主模型对齐：GLM-5 技术报告写明"让模型与 DeepSeek-V3 一致以提升接受率"，官方对照的就是 DeepSeek-V3.2 的接受长度；据技术解读，5.2 用 IndexShare + KVShare 复用第一步的索引与 KV，使后续步骤的 KV 全来自主模型，再叠拒绝采样与端到端 TV loss。第二条：长上下文里索引器从配角变成新瓶颈（DeepSeek-V3.2 的 DSA 讲清），而 GLM-5.2 的 IndexShare 就是官方 README 直接引的那篇公开论文（arXiv 2603.12201）：相邻层 top-k 高度重叠，于是每四层只第一层算索引、后三层复用，1M 下每 token FLOPs 降约 2.9×。我们也对照了刚出的 DeepSeek-V4（CSA+HCA，1M 下 27%/10%）确认同代方向。一句口径：机制大多有出处，但两个数字的完整消融与 serving 吞吐说法仍停在产品页与技术解读，尚无单独的 5.2 论文与第三方复现。

## 时间线

（最终音频 9:17，自然 TTS 语速）

- 0:00 开场：GLM-5.2 的两个效率数字 + 中心问题——官方口径还是公开复现
- 1:16 MTP vs NTP（Meta）→ 额外头转 self-speculative
- 2:19 DeepSeek-V3 工业化 MTP（顺序 MTP 模块，可改造做投机解码）
- 2:42 定义接受长度（EAGLE-2）；EAGLE-3 的七点五是这条线公开高点
- 3:17 +20% 的真实机制：让草稿 KV 与主模型对齐（GLM-5 报告，对照 DeepSeek-V3.2）；IndexShare + KVShare + 拒绝采样 + TV loss
- 4:13 投机解码大家族：Leviathan / Chen、Medusa
- 4:43 DeepSeek-V4（CSA+HCA，1M 下 27%/10%）确认方向但不讲索引器
- 5:32 DeepSeek-V3.2 的 DSA / lightning indexer：索引器成新瓶颈
- 6:05 IndexShare = README 直引的公开论文 2603.12201（每四层共享一个 indexer，2.9×）；MISA 作为另一条路
- 7:15 serving：1M 下瓶颈转向 KV 容量与长上下文（技术解读，尚无论文坐实）
- 7:48 口径更新 + 从夯到拉评级（夯）+ 三篇必读收尾

## 论文与链接

- GLM-5.2：github.com/zai-org/GLM-5 · huggingface.co/zai-org/GLM-5.2 · GLM-5 报告 arXiv 2602.15763
- MTP：Better & Faster LLMs via Multi-token Prediction — arXiv 2404.19737（Meta）· DeepSeek-V3 — arXiv 2412.19437
- 投机解码：2211.17192 · 2302.01318 · Medusa 2401.10774 · EAGLE 2401.15077 · EAGLE-2 2406.16858 · EAGLE-3 2503.01840 · LayerSkip 2404.16710
- DeepSeek-V4：Towards Highly Efficient Million-Token Context Intelligence（官方报告 PDF）
- 稀疏注意力索引：DeepSeek-V3.2 2512.02556 · IndexShare 2603.12201 · MISA 2605.07363 · NSA 2502.11089

## 制作元信息

- 文稿：32 turns（Jeff 16 / Ada 16），约 3,167 朗读字符
- 音频：9:17，自然 TTS 语速（loudnorm，无 atempo 加速）
- 主持：Jeff（系统视角）/ Ada（提问者）
- 口径：GLM-5.2 的 +20% / 2.9× 为智谱官方数据；机制大多有出处（IndexShare 论文 2603.12201、MTP 对齐之道见 GLM-5 报告），KVShare / serving 吞吐为技术解读；DeepSeek-V4 数字经报告核对。
