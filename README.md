# Kaibo Wang — Personal Website / 王楷博个人网站

A bilingual, responsive product portfolio in **English** and **简体中文** with a first-visit language chooser and persistent EN / 中文 switcher.

## Pages

- `index.html` — English homepage, first-visit language selection
- `zh/index.html` — Chinese homepage
- `ai-defender.html` / `zh/ai-defender.html` — AI email-defense product case study
- `greentail.html` / `zh/greentail.html` — sustainable pet-food product design case study
- `quotaquest.html` / `zh/quotaquest.html` — entrepreneurship and client-delivery case
- `quotaquest-demo.html` / `zh/quotaquest-demo.html` — synthetic-data interactive application dashboard
- `wordplay.html` / `zh/wordplay.html` — English-to-Chinese localization and accessibility case study

## Run locally

Open `index.html` in a browser, or serve the project folder with `python3 -m http.server 8000` and visit `http://localhost:8000`.

## GitHub Pages setup

1. Create a public GitHub repository named `personal-website` in your preferred GitHub account.
2. Upload **the entire contents of this folder**, preserving `.github/workflows/deploy.yml`, `.nojekyll`, `assets/`, and `zh/`.
3. Under **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**.
4. A push to `main` will trigger `Deploy bilingual portfolio to GitHub Pages`.
5. Verify the Actions workflow has succeeded before sharing the resulting Pages URL; expected URL for `Kwang37` is `https://kwang37.github.io/personal-website/` **only after deployment actually succeeds**.

## Site privacy / scope

The QuotaQuest interactive dashboard uses synthetic data; no real applicant data is included. The GreenTail browser storage example stores one harmless preference locally. The AI Defender walkthrough runs in the browser and does not connect to the original AWS backend. Source links and attribution notes distinguish direct contributions from team work.

## Attribution

- AI Defender: https://github.com/KatKho/healthcare-email-defense
- GreenTail: https://github.com/UW-INFO442-AU25/GreenTail-G2
- Wordplay: https://github.com/wordplaydev/wordplay

No original project repository is modified by generating this website.