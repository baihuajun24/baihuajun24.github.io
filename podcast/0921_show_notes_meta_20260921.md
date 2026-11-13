# 0921 Jev 特辑 · 不写答案的模型，怎么让软件做决定？

音频：12:00 · 本地 Qwen3-TTS · 双主持 Jeff / Ada

Jev 不写文章、不写代码，也不直接执行工具。它读取一份 state，再对开发者定义好的 Choice、Score 或 Noul 问题返回结构化概率判断。

本期以 TypeSafe 官方资料为主，讨论 Jev 真正提供了什么：它与聊天模型、Agent 和传统分类器的区别；Choice 概率为什么不是后端模型成功率；confidence 为什么也不是正确率保证；以及为什么 type-safe 仍然不等于 truth-safe。

> **结构可以合法，判断仍然可能错。**

## 三个核心原语

- **Choice**：从开发者定义的互斥候选中选择，返回完整概率分布和 confidence。
- **Score**：在两到十个有顺序、带语义描述的等级之间判断，返回期望位置、等级概率和 confidence。
- **Noul**：回答 yes / no 问题，返回 yes 的概率。它不是程度分数，也没有单独的 confidence 字段。

如果 Choice 给 Sol 0.7，这表示 Jev 在当前候选描述与分配准则下，把 70% 的选择概率放在 Sol 上；它不表示 Sol 有 70% 概率完成任务。后端成功率需要历史结果、在线评测或专门校准的问题。

## 谁真正执行动作

Jev 做完判断后，应用代码可以：

- 走一个确定性分支；
- 调用专门语言模型；
- 请求人工审核；
- 把建议写回生成式 Agent 的上下文。

真正的 API 调用、数据库写入、下单与文件修改，应由代码中的显式 dispatcher 执行。官方的函数调用、SDE 级联与技能建议案例，都体现了这种分工。

## Type-safe 不等于 truth-safe

Jev 可以保证返回允许的候选与字段形状，避免自由文本解析和非法函数名；但合法选择仍可能在语义上错误。多个独立问题也可能分别合法、联合起来却不相容。

官方列出的薄弱点包括：数学与计数、日期时间比较、过度字面理解、间接表达、长篇无关 state、对抗内容、矛盾指令、跨问题结构约束和开放式生成。精确算术、确定性规则与副作用应该留在代码里。

## 时间线

- **00:00** 一个不写答案的模型
- **00:54** 从客服分流理解动态“菜单”
- **01:38** Choice、Score 与 Noul
- **02:20** 概率、confidence 与成功率
- **03:38** 置信门控：执行、谨慎或升级
- **04:27** 模型做判断，代码做动作
- **05:05** 函数分发与开放参数的边界
- **05:47** SDE 级联与技能建议
- **06:54** 同一份 state 上并行提问
- **07:43** 独立问题为什么会破坏联合约束
- **08:26** Type-safe 不等于 Truth-safe
- **09:30** 怎样读厂商速度与成本数字
- **10:46** Jev 适合怎样的软件分工
- **11:29** 概率化 if 语句，不是真理机器

## 资料

- [Jev introduction](https://docs.typesafe.ai/introduction)
- [Choice](https://docs.typesafe.ai/primitives/choice)
- [Score](https://docs.typesafe.ai/primitives/score)
- [Noul](https://docs.typesafe.ai/primitives/noul)
- [Confidence](https://docs.typesafe.ai/confidence)
- [System One](https://docs.typesafe.ai/concepts/system-one)
- [How to build with System One](https://docs.typesafe.ai/concepts/how-to-build-with-system-one)
- [Jev 1.13 model jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13)
- [Function calling cookbook](https://docs.typesafe.ai/cookbooks/function_calling)
- [SDE cascade cookbook](https://docs.typesafe.ai/cookbooks/sde_cascade)
- [Skill suggestion cookbook](https://docs.typesafe.ai/cookbooks/skill_suggestion)
- [Parallel questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions)
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

厂商披露的速度、成本与工作流结果均为官方自报，并非独立 benchmark。实际效果取决于任务分布、state、候选描述、阈值与评测方式。
