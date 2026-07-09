# 客户咨询分流手册

这份手册用于微信咨询场景：快速判断客户处于哪个阶段、该发哪段话、下一步要收什么材料。

## 一键回复脚本

查看所有场景：

```powershell
python scripts\suggest_reply.py --list
```

输出某个场景的回复：

```powershell
python scripts\suggest_reply.py --scenario opening
```

回复库在：

```text
ops/lead-reply-library.tsv
```

## 推荐流程

1. 新客户咨询：发 `opening`。
2. 客户材料不清楚：发 `scope_check`。
3. 客户付款后：发 `payment_received`。
4. 材料太大：发 `too_broad`。
5. 触碰隐私：发 `privacy_sensitive`。
6. 要代写、伪造或保证发表：发 `not_allowed`。
7. 交付后：发 `delivery_sent`。
8. 客户认可：发 `star_request` 或对应 `upsell_*`。

## 接单判断

可接：

- 一篇论文的摘要、链接、引言或方法片段。
- 一段 300-800 字论文文字或 claim 列表。
- 一个 repo 的 README、目录结构或文件清单。
- 已脱敏的项目说明。

谨慎接：

- 完整论文稿件。
- 未发表数据。
- 私有代码仓库。
- 多篇文献综述。
- 需要真实文献检索承诺的引用审计。

不接：

- 代写论文。
- 伪造引用、数据、DOI、PMID 或审稿意见。
- 保证录用或保证引用一定正确。
- 未脱敏敏感隐私材料。
- 医学、法律、伦理、财务或合规结论。

## 阶段定义

| 阶段 | 含义 | 目标 |
| --- | --- | --- |
| `lead` | 还没付款 | 判断服务是否适合 |
| `paid_waiting_materials` | 已付款但材料不完整 | 收齐材料并确认范围 |
| `ready` | 付款、材料、范围都确认 | 创建订单工作区 |
| `working` | 正在交付 | 使用模板和质检脚本 |
| `delivered` | 已发送结果 | 等一次澄清 |
| `closed` | 已完成 | 请求 star、转介绍或推荐下一单 |

## 记录

每个咨询都至少记录到私有表：

```text
orders/order-tracker.csv
orders/growth-metrics.csv
```

不要记录客户真实隐私到公开仓库。公开仓库只保留模板和流程。
