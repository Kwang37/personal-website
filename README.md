# Kaibo Wang — Personal Website / 王楷博个人网站

A bilingual **English / 简体中文** portfolio focused on product management, AI products, human-centered design, and technical implementation.

## Live site

Once GitHub Pages is enabled and the deploy workflow succeeds:
**https://kwang37.github.io/personal-website/**

The site has a first-visit language chooser and persistent **EN / 中文** switcher.

## Pages

| English | 简体中文 |
| --- | --- |
| [Home](index.html) | [主页](zh/index.html) |
| [AI Defender](ai-defender.html) | [AI Defender 案例](zh/ai-defender.html) |
| [GreenTail](greentail.html) | [GreenTail 案例](zh/greentail.html) |
| [QuotaQuest](quotaquest.html) | [QuotaQuest 案例](zh/quotaquest.html) |
| [Interactive application demo](quotaquest-demo.html) | [申请管理演示](zh/quotaquest-demo.html) |
| [Wordplay](wordplay.html) | [Wordplay 案例](zh/wordplay.html) |

## Enable publishing (one-time GitHub setting)

The repository has an automatic GitHub Pages workflow at `.github/workflows/deploy.yml`.
For a new repository, an owner must first:

1. Open [Settings → Pages](https://github.com/Kwang37/personal-website/settings/pages).
2. Under **Build and deployment → Source**, select **GitHub Actions**.
3. Open [Actions](https://github.com/Kwang37/personal-website/actions) and check the most recent **Deploy bilingual portfolio to GitHub Pages** run. If needed, click **Run workflow** or push a change.

The workflow builds a downloadable PDF resume from `scripts/build_resume.py` using ReportLab, then uploads the static site as the Pages artifact. No secret or API key is required.

## Project sources and scope

- AI Defender: https://github.com/KatKho/healthcare-email-defense
- GreenTail: https://github.com/UW-INFO442-AU25/GreenTail-G2
- Wordplay: https://github.com/wordplaydev/wordplay

The QuotaQuest interaction uses **synthetic sample data**, not real student records. The AI Defender walkthrough does not connect to the original AWS backend. The GreenTail localStorage demonstration writes a harmless browser-local preference and does not transmit it to a server.

Some Chinese case-study text was adapted for bilingual presentation, retaining distinctions between individual contributions, team outcomes, and demonstrations.

© 2026 Kaibo Wang
