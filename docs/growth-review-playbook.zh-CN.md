# 增长复盘手册

这份手册用于每周复盘 Codex for Researchers 的获客和成交。目标不是做复杂数据系统，而是用最小记录判断：哪种渠道带来咨询、哪种文案带来付款、交付是否拖慢复购。

## 私有数据表

从公开模板复制一份到本地私有目录：

```powershell
Copy-Item ops\growth-metrics-template.csv orders\growth-metrics.csv
```

`orders/` 已被 git 忽略，用来保存真实运营数据。不要把真实客户微信号、付款截图、论文内容或私有备注提交到公开仓库。

## 每日记录字段

| 字段 | 含义 |
| --- | --- |
| `date` | 发布或成交日期 |
| `channel` | 渠道，如 wechat-moments、wechat-group、xiaohongshu、github |
| `post_type` | 文案类型，如 soft-launch、problem-first、faq-reply |
| `content_id` | 自己给文案起的编号 |
| `impressions_est` | 粗略曝光估计，没有就填 0 |
| `profile_clicks` | 主页/仓库/资料点击估计 |
| `wechat_adds` | 新增微信咨询数 |
| `paid_orders` | 付款订单数 |
| `revenue_rmb` | 收入金额 |
| `fulfilled_orders` | 已交付订单数 |
| `refunds` | 退款/作废数 |
| `notes` | 简短复盘，不放隐私内容 |

## 每周汇总

运行：

```powershell
python scripts\summarize_growth.py orders\growth-metrics.csv
```

如果只是测试公开模板：

```powershell
python scripts\summarize_growth.py ops\growth-metrics-template.csv
```

## 复盘问题

每周只回答 5 个问题：

1. 哪个渠道带来的微信咨询最多？
2. 哪类文案带来的付款最多？
3. 哪个服务最容易成交：1.99 论文精读、3.99 引用审计，还是 5.99 复现包审计？
4. 哪个环节最慢：咨询、付款、材料收集、交付，还是澄清？
5. 下周只改一个东西，应该改文案、FAQ、样例、交付模板，还是价格梯度？

## 简单判断规则

- 有曝光但没微信添加：文案钩子或 CTA 不清楚。
- 有微信添加但没付款：FAQ、价格解释、样例或信任感不足。
- 有付款但交付慢：订单工作区和质检流程需要压缩。
- 有交付但没复购：交付结果缺少下一步建议或加购路径。
- 退款或作废增加：范围说明不够清楚，需要加强 FAQ 和私聊话术。

## 下周实验

每周只做一个实验，避免同时改太多：

```text
实验名称：
渠道：
文案：
目标指标：
预期结果：
实际结果：
下周动作：
```

可以实验的内容：

- 换一个开头：从“低价服务”换成“组会前读不完论文怎么办”。
- 换一个渠道：微信群、小红书、GitHub README、朋友圈。
- 换一个主推服务：先推 1.99 论文精读，再引导到 19.9 小包。
- 换一个样例入口：直接发交付样例，而不是只发主页。
- 换一个 FAQ 回答：先讲边界和隐私，再讲价格。

## 不要做的事

- 不要为了转化承诺录用、保证引用正确或代写。
- 不要把客户隐私作为案例。
- 不要同时改价格、文案、渠道和交付范围。
- 不要用没有记录的数据判断“哪个渠道有效”。
