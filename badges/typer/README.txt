Calrec - Type R IO & Surface Badge
=================================

Hosted URLs (after upload & GitHub Pages deploy):
- Landing page: https://ultanmolloy-lgtm.github.io/calrec-certifications/badges/typer/
- Assertion:    https://ultanmolloy-lgtm.github.io/calrec-certifications/badges/typer/assertion.json
- BadgeClass:   https://ultanmolloy-lgtm.github.io/calrec-certifications/badges/typer/badgeclass.json
- Issuer:       https://ultanmolloy-lgtm.github.io/calrec-certifications/badges/issuer.json
- Image:        https://ultanmolloy-lgtm.github.io/calrec-certifications/badges/typer/badge.png

Steps to issue:
1) Replace `badge.png` with your Calrec artwork.
2) Update `badgeclass.json` → `criteria.id` to a public doc (`/view?usp=sharing`).
3) Update `assertion.json` → `recipient.identity` if issuing to someone else.
4) Commit to `main`; wait ~60s; load the URLs above.
5) Bake the PNG: set `openbadges_id` to `https://ultanmolloy-lgtm.github.io/calrec-certifications/badges/typer/assertion.json` and upload to your platform.
