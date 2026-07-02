# Codex for Researchers Launch Posts

This file is the copy-and-paste sales kit for the solo WeChat launch.

Core offer:

- RMB 1.99: 论文精读
- RMB 3.99: 引用审计
- RMB 5.99: 复现包审计
- WeChat: `zhiyanaishe`
- Payment: public WeChat QR code in `assets/payments/wechat-qr.png`

## Positioning

一句话：

```text
我做了一个低价科研 Codex 工作流小服务：1.99 元帮你精读一篇论文，3.99 元帮你查一段文字的引用风险，5.99 元帮你看一个复现包是否容易踩坑。
```

更稳妥的版本：

```text
这是一个科研辅助服务，不代写、不保证发表、不替代导师或同行评审；适合先快速看懂论文、排查引用支撑、整理代码/数据复现清单。
```

## WeChat Moments

### Soft Launch

```text
我把最近用 Codex 做科研阅读和审稿辅助的流程整理成了一个公开项目：

https://github.com/DannyJay2025/codex-for-researchers

现在做一个低价试运营：

1.99 元：论文精读
3.99 元：引用审计
5.99 元：复现包审计

适合：
- 组会前快速读懂一篇论文
- 投稿前检查一句话有没有引用支撑
- 复现实验前看看代码、数据、环境说明哪里容易卡

加微信：zhiyanaishe
付款后发论文链接、摘要、段落或项目说明，我交付 Markdown 结果。
```

### Problem First

```text
很多科研工作不是不会做，而是第一步太耗时间：

- 论文太长，不知道先看哪里
- 引用看起来很多，但不知道是否真的支撑那句话
- 复现包文件很多，不知道缺不缺 README、环境、数据说明

我做了一个低价 Codex 科研工作流服务：

1.99 元：论文精读
3.99 元：引用审计
5.99 元：复现包审计

不是代写，不承诺发表，只做阅读、核查和整理。

需要的话加微信：zhiyanaishe
```

## WeChat Group

Short group post:

```text
我这边试运营一个科研辅助小服务：

1.99 元论文精读
3.99 元引用审计
5.99 元复现包审计

适合组会、投稿前自查、复现前扫雷。不是代写，不保证发表，只给 Markdown 检查结果。

需要可以加我微信：zhiyanaishe
项目地址：https://github.com/DannyJay2025/codex-for-researchers
```

When someone asks "靠谱吗":

```text
定位是低价辅助检查，不是专家审稿，也不替代你自己判断。

我会把结果标成：已明确、需核实、风险点、下一步建议。
尤其是引用和事实部分，会提醒你人工复核。
```

## Xiaohongshu

Title ideas:

- 1.99 元让 AI 帮你先读一篇论文
- 组会前临时读 paper，我整理了一个低价工作流
- 投稿前别急着交，先查一下引用风险
- 复现代码前，先看 README 和数据说明有没有坑

Post body:

```text
我做了一个科研辅助小服务，适合学生、科研作者和刚开始做课题的人。

能做什么：
1. 论文精读：把一篇论文整理成研究问题、方法、结果、局限和组会问题。
2. 引用审计：把一段话拆成 claims，标出哪些需要引用、哪些可能过度表述。
3. 复现包审计：检查代码、数据、环境、README、运行步骤是否完整。

价格：
1.99 元论文精读
3.99 元引用审计
5.99 元复现包审计

边界：
不代写，不保证发表，不做虚假引用，不处理隐私敏感数据公开样例。

微信：zhiyanaishe
GitHub：DannyJay2025/codex-for-researchers
```

## Private Chat Closing Script

Opening:

```text
你好，我是 Codex for Researchers。你想做哪一项？

1. 论文精读：1.99 元
2. 引用审计：3.99 元
3. 复现包审计：5.99 元

付款后请发：
- 付款截图
- 论文链接/摘要/段落/项目说明
- 输出语言：中文/英文/中英双语
- 用途：组会/写作/投稿前检查/复现前检查
```

Payment confirmation:

```text
收到付款截图。我先确认材料范围，然后开始处理。正常 24-72 小时内交付 Markdown 结果。
```

If the material is too broad:

```text
这份材料超过当前低价单范围。可以先选一个最小范围：

- 一篇论文
- 一段 300-800 字文本
- 一个 repo 的文件结构和 README

如果要完整稿件或完整项目审计，我会单独报价。
```

Delivery:

```text
结果已整理好。里面我分了：

- 核心结论
- 风险点
- 建议下一步
- 需要你人工确认的位置

如果这个结果有帮助，欢迎给 GitHub 项目点一个 star，或者转发给需要读论文、查引用、做复现检查的朋友。
```

Upsell after a good first delivery:

```text
如果你后面还有连续需求，可以做小包：

19.9 元：10 篇论文快速精读
39.9 元：一节 manuscript 引用审计
99 元：一个完整复现包审计

先不用急着买，等你确认这次结果有用再说。
```

## Daily Operating Rhythm

20 minutes per day:

1. Post one short message in one channel.
2. Reply to new WeChat leads.
3. Create an order workspace with `python scripts/create_order_workspace.py`.
4. Deliver one small Markdown result before taking large custom work.
5. Record every question customers ask; turn repeated questions into README, FAQ, or templates.

## Boundaries

Do not promise:

- guaranteed acceptance
- fabricated citations
- ghostwriting that violates academic rules
- medical, legal, financial, or regulatory advice
- confidentiality for any material the customer explicitly allows you to publish as a sample

Say this when needed:

```text
我可以帮你做阅读、结构化整理、风险提示和可复核建议；最终学术判断、投稿决定和事实核查需要你自己或专业合作者确认。
```
