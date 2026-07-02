# Customer Delivery Flow

This is the operating flow for a solo developer using WeChat payment and manual delivery.

## Public Funnel

1. Customer finds the GitHub repo.
2. Customer sees the low-cost launch offers and QR code.
3. Customer adds WeChat `zhiyanaishe`.
4. Customer chooses one service:
   - RMB 1.99: paper reading brief
   - RMB 3.99: citation support audit
   - RMB 5.99: reproducibility package audit
5. Customer pays and sends payment screenshot.
6. Customer sends source material.
7. You deliver Markdown output.

## Intake Message

Send this when a buyer contacts you:

```text
你好，我是 Codex for Researchers。
请选择服务：
1. 论文精读：1.99 元
2. 引用审计：3.99 元
3. 复现包审计：5.99 元

付款后请发送：
- 付款截图
- 论文链接 / 摘要 / 段落 / 项目说明
- 期望交付语言：中文 / 英文 / 中英双语
- 是否允许我使用脱敏内容做公开案例：是 / 否
```

## Delivery Promise

Use these conservative promises:

| Service | Normal delivery | Output |
| --- | --- | --- |
| Paper reading brief | 24-72 hours | Markdown brief |
| Citation support audit | 24-72 hours | Claim table |
| Reproducibility package audit | 24-72 hours | Checklist and risks |

Do not promise real-time delivery until the workflow is stable.

## After Delivery

Ask:

```text
如果这个结果对你有帮助，欢迎给 GitHub 仓库点个 star，或者把这个项目转发给需要读论文、查引用或做复现检查的朋友。
```

GitHub:

```text
https://github.com/DannyJay2025/codex-for-researchers
```

## Upsell Path

After the first delivery, offer:

- RMB 19.9: 10-paper reading pack.
- RMB 39.9: one manuscript section citation audit.
- RMB 99: one complete reproducibility review.
- Custom price: lab workflow setup.
