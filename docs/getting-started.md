# Getting Started

This project is a Codex workflow pack. It does not run like a web app. To make it "run", make the skills usable in Codex, publish the public repo, and set up a simple paid delivery flow.

## 1. Run Local Checks

From the project folder:

```powershell
cd "C:\Users\Danny Jay\Documents\副业\codex-for-researchers"
python scripts\check_project.py
python skills\reproducibility-packager\scripts\audit_reproducibility.py .
```

Expected result:

```text
[OK] Codex for Researchers project checks passed.
```

## 2. Use It In Codex

Open this folder in Codex and ask:

```text
Use research-paper-reader on this PDF and create a journal club reading brief.
```

```text
Use citation-support-finder on this introduction and produce a claim-to-citation table.
```

```text
Use manuscript-polisher in journal-ready mode. Preserve all scientific claims.
```

```text
Use reproducibility-packager to audit this project folder.
```

## 3. Add Payment Flow

Choose one of these:

- Public QR code: save your WeChat payment code as `assets/payments/wechat-qr.png`.
- Private QR code: keep the QR code off GitHub and send it manually after a buyer contacts you.

Use `premium-templates/order-form.md` to collect:

- buyer name
- WeChat ID
- GitHub username or email
- requested product
- payment screenshot
- delivery method

For local fulfillment, create a private order workspace:

```powershell
python scripts\create_order_workspace.py --service paper-reading --buyer buyer-name
```

Customer materials should stay inside `orders/`, which is ignored by git.

Current public contact:

```text
WeChat: zhiyanaishe
GitHub: https://github.com/DannyJay2025
```

## 4. Publish The Public Repo

Create an empty GitHub repository named `codex-for-researchers`, then run:

```powershell
cd "C:\Users\Danny Jay\Documents\副业\codex-for-researchers"
git add .
git commit -m "Initial Codex for Researchers"
git remote add origin https://github.com/DannyJay2025/codex-for-researchers.git
git push -u origin main
```

## 5. Create The Paid Delivery Channel

Start simple:

1. Create a private GitHub repo named `codex-for-researchers-premium`.
2. Put full paid templates and examples there.
3. After payment, invite the buyer's GitHub username manually.
4. If the buyer does not use GitHub, send a zip archive instead.

## 6. First Sellable Offer

The easiest first offer is:

```text
RMB 1.99: one paper reading brief
RMB 3.99: citation support audit for one manuscript section
RMB 5.99: reproducibility package audit for one repo
```

Do not sell everything at once. Start with one clear outcome, deliver it manually, then turn repeated work into premium templates.

## 7. Weekly Operating Loop

- Publish one example output or use case.
- Answer one issue or user question.
- Convert repeated requests into a premium template.
- Keep paid assets private.
- Run `python scripts\check_project.py` before every release.
