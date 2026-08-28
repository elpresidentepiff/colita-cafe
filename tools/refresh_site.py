from pathlib import Path
import re

p = Path("index.html")
html = p.read_text(encoding="utf-8")

# Public/indexable.
html = re.sub(r'\s*<meta\s+name="robots"[^>]*>\s*', '\n', html, flags=re.I)
html = re.sub(r'\s*<meta\s+name="googlebot"[^>]*>\s*', '\n', html, flags=re.I)

# Remove gross-margin economics block requested by Steven.
html = re.sub(r'(?is)\s*<!--\s*=+\s*ECONOMICS\s*=+\s*-->\s*<section\b.*?</section>\s*', '\n', html, count=1)
html = re.sub(r'(?is)<section\b[^>]*>.*?Gross margin is strong\. Contribution margin is unmodelled\..*?</section>', '', html, count=1)

# Remove older retail-price comparison if still present.
for pattern in (
    r'(?is)<section\b[^>]*>.*?(?:£|&pound;)\s*5\.90.*?(?:21\s*[–-]\s*80\+?|(?:£|&pound;)\s*80\+?).*?</section>',
    r'(?is)<div\b[^>]*>.*?(?:£|&pound;)\s*5\.90.*?(?:21\s*[–-]\s*80\+?|(?:£|&pound;)\s*80\+?).*?</div>',
):
    html = re.sub(pattern, '', html, count=1)

# Remove numbered Shoot/Shot 1–4 planning placeholders only.
html = re.sub(
    r'(?is)<section\b[^>]*>.*?(?:shoot|shot)\s*0?1\b.*?(?:shoot|shot)\s*0?2\b.*?(?:shoot|shot)\s*0?3\b.*?(?:shoot|shot)\s*0?4\b.*?</section>',
    '', html, count=1,
)
for n in range(1, 5):
    html = re.sub(
        rf'(?is)<(?:div|figure)\b[^>]*class="[^"]*(?:shot-frame|shoot-card)[^"]*"[^>]*>.*?(?:shoot|shot)\s*0?{n}\b.*?</(?:div|figure)>',
        '', html, count=1,
    )

# Remove the temporary duplicate expansion added by the refresh automation.
# The earlier site expansion already contains the research, revenue, Carlos and track-record sections.
html = re.sub(r'(?is)\s*<!-- COLITA EXPANSION START -->.*?<!-- COLITA EXPANSION END -->\s*', '\n', html)

p.write_text(html, encoding="utf-8")
Path("robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
print("Colita cleanup complete")
