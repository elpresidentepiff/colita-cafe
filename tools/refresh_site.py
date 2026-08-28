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
html = re.sub(r'(?is)\s*<!-- COLITA EXPANSION START -->.*?<!-- COLITA EXPANSION END -->\s*', '\n', html)

# Research belongs near the top of the story: coffee is chemistry before it is a beverage.
# Rebuild this block on every run so edits stay idempotent.
html = re.sub(r'(?is)\s*<!-- COFFEE CHEMISTRY EDUCATION START -->.*?<!-- COFFEE CHEMISTRY EDUCATION END -->\s*', '\n', html)
chemistry = r'''
<!-- COFFEE CHEMISTRY EDUCATION START -->
<section id="coffee-chemistry" style="padding:72px 6%;background:#f4efe5;color:#182018;">
  <div style="max-width:1180px;margin:0 auto;">
    <p style="letter-spacing:.16em;text-transform:uppercase;font-size:.78rem;font-weight:700;margin:0 0 12px;">Research · Coffee Chemistry · Education</p>
    <h2 style="font-size:clamp(2rem,5vw,4.4rem);line-height:.98;margin:0 0 22px;max-width:980px;">Coffee is a chemical system. Fermentation changes the system.</h2>
    <p style="font-size:1.12rem;line-height:1.7;max-width:900px;">We treat fermentation as controlled post-harvest engineering: time, process, fruit state, temperature, pH, sugars and microbial activity can change the precursor chemistry that later becomes flavour. The important question is not simply whether a coffee was fermented. It is <strong>what changed, by how much, and why.</strong></p>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(235px,1fr));gap:18px;margin-top:34px;">
      <article style="background:#fff;padding:26px;border-radius:18px;"><h3>Chlorogenic acids · CGAs</h3><p>Green coffee is a major dietary source of chlorogenic acids, with 5-CQA one of the principal forms. CGAs contribute to bitterness, acidity, antioxidant chemistry and the pool of compounds transformed by processing and heat.</p><p><strong>Key finding:</strong> recent controlled fermentation work shows CGA concentration is not fixed. It can vary with processing route, fermentation duration and growing environment. That makes process control a chemistry decision, not just a flavour decision.</p></article>
      <article style="background:#fff;padding:26px;border-radius:18px;"><h3>Trigonelline</h3><p>Trigonelline is a naturally occurring coffee alkaloid and an important aroma precursor. During roasting it contributes to downstream aroma chemistry and is partially transformed into other compounds.</p><p><strong>Key finding:</strong> multiple fermentation studies report trigonelline remaining comparatively stable while other chemical markers move. That stability makes it useful when separating what fermentation changes from what it leaves largely intact.</p></article>
      <article style="background:#fff;padding:26px;border-radius:18px;"><h3>Caffeine</h3><p>Caffeine is only one part of coffee chemistry, but it is a useful compositional marker. Its concentration is influenced strongly by species and genetics and can respond differently from acids and volatile precursors during post-harvest processing.</p><p><strong>Key finding:</strong> controlled studies show caffeine may remain stable in some fermentation windows while changing under other process × time combinations. There is no honest one-rule-fits-all fermentation claim.</p></article>
      <article style="background:#fff;padding:26px;border-radius:18px;"><h3>Organic acids & volatiles</h3><p>Microorganisms consume sugars and produce acids, alcohols, esters and other metabolites. These compounds, together with bean precursors, influence the sensory material available before and after roasting.</p><p><strong>Key finding:</strong> anaerobic and inoculated fermentations have been associated with intensified fruity character and measurable shifts in acids, esters and other volatile families. Fermentation can therefore be mapped chemically as well as tasted.</p></article>
    </div>

    <div style="margin-top:28px;padding:30px;border:1px solid rgba(24,32,24,.18);border-radius:18px;">
      <h3 style="font-size:1.55rem;margin-top:0;">What the research is telling producers</h3>
      <p><strong>1. Time alone is not a recipe.</strong> A 2026 Huila study found fermentation/holding time interacted with agroecological zone: CGAs changed while caffeine and trigonelline were comparatively stable, and longer holding increased physical defects. The lesson is control the environment, not the stopwatch alone.</p>
      <p><strong>2. Process changes chemistry and flavour together.</strong> A separate 0–300 hour study identified 79 volatile compounds and linked process × time to distinct sensory directions. Whole-fruit and pulped routes did not behave the same chemically or sensorially.</p>
      <p><strong>3. Anaerobiosis is biologically active, not a marketing word.</strong> Research on self-induced anaerobiosis identified diverse yeasts and lactic-acid bacteria, measurable metabolites including chlorogenic acid, sucrose, lactic acid and trigonelline, and an intensification of fruity sensory attributes.</p>
      <p><strong>4. Roasting rewrites the molecule map.</strong> Research consistently shows that green-bean compounds are precursors: CGAs are reduced/transformed, trigonelline is partially degraded, and Maillard/Strecker chemistry generates much of coffee's familiar aroma. This is why understanding the green bean matters before the roaster ever receives it.</p>
    </div>

    <div style="margin-top:28px;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;">
      <article style="padding:26px;background:#172017;color:#f6f0e4;border-radius:18px;"><p style="font-size:.76rem;text-transform:uppercase;letter-spacing:.14em;">Our operating thesis</p><h3>Design upstream.</h3><p>Flavour is not created at one machine at the end of the chain. Picking, fruit condition, fermentation environment, duration, washing and drying establish the chemical starting material. We work at that beginning.</p></article>
      <article style="padding:26px;background:#172017;color:#f6f0e4;border-radius:18px;"><p style="font-size:.76rem;text-transform:uppercase;letter-spacing:.14em;">Evidence, not miracle claims</p><h3>Measure first. Claim second.</h3><p>Cell, animal, mechanistic and observational studies can reveal promising biological activity, but they do not make coffee a treatment or cure. We separate established coffee chemistry from emerging health research and label the strength of evidence.</p></article>
    </div>

    <p style="font-size:.82rem;line-height:1.6;opacity:.72;margin-top:24px;">Research basis includes peer-reviewed work on coffee biochemistry, chlorogenic acids, trigonelline, controlled coffee fermentation, self-induced anaerobiosis and recent Colombian fermentation-time studies. Educational content only; not medical advice.</p>
  </div>
</section>
<!-- COFFEE CHEMISTRY EDUCATION END -->
'''

# Insert immediately inside <main> when available; otherwise immediately after the first header.
m = re.search(r'(?is)<main\b[^>]*>', html)
if m:
    html = html[:m.end()] + chemistry + html[m.end():]
else:
    m = re.search(r'(?is)</header\s*>', html)
    if m:
        html = html[:m.end()] + chemistry + html[m.end():]
    else:
        m = re.search(r'(?is)<body\b[^>]*>', html)
        if m:
            html = html[:m.end()] + chemistry + html[m.end():]

p.write_text(html, encoding="utf-8")
Path("robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
print("Colita cleanup + chemistry education refresh complete")
