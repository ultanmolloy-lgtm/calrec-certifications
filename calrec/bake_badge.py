# Bake a Calrec badge image with Open Badges metadata
from PIL import Image
from PIL.PngImagePlugin import PngInfo

PAGES_BASE = "https://ultanmolloy-lgtm.github.io/calrec-certifications"
BADGE_SLUG = "typer"
ASSERTION_URL = f"{PAGES_BASE}/badges/{BADGE_SLUG}/assertion.json"

INPUT = f"./badges/{BADGE_SLUG}/badge.png"
OUTPUT = f"./badges/{BADGE_SLUG}/badge_baked.png"

img = Image.open(INPUT).convert("RGBA")
meta = PngInfo()
meta.add_text("openbadges_id", ASSERTION_URL)
img.save(OUTPUT, pnginfo=meta, optimize=True)
print("Baked:", OUTPUT)
