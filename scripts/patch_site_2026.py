#!/usr/bin/env python3
from pathlib import Path
import re, html

p = Path('index.html')
s = p.read_text(encoding='utf-8')
original = s

sections = list(re.finditer(r'<section\b[^>]*>.*?</section>', s, flags=re.I|re.S))
remove_spans = []
removed_labels = []
for m in sections:
    block = m.group(0)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', block))
    text = re.sub(r'\s+', ' ', text).strip()
    compact = text.lower().replace(',', '')
    price_hit = ('5.90' in compact or '£5.90' in compact or '&pound;5.90' in block.lower())
    range_hit = bool(re.search(r'\b21\b.{0,90}\b80\+?\b', compact)) or ('21' in compact and ('80+' in compact or '80 plus' in compact))
    if price_hit or range_hit:
        remove_spans.append((m.start(), m.end()))
        removed_labels.append(text[:240])
for a,b in reversed(remove_spans):
    s = s[:a] + s[b:]

marker = '<!-- COLITA_EXPANSION_2026 -->'
if marker not in s:
    new_sections = r'''
<!-- COLITA_EXPANSION_2026 -->
<section id="research-science">
  <div class="wrap stack-lg">
    <div class="stack narrow">
      <p class="eyebrow">Research / Coffee Chemistry</p>
      <h2>Beyond flavour: the chemistry inside coffee.</h2>
      <p class="lead">Colita's research programme follows the molecules, processing variables and extraction technologies that sit behind coffee quality — from chlorogenic acids and trigonelline to fermentation ecology and assisted extraction.</p>
    </div>
    <div class="grid-3">
      <article class="card stack"><span class="chip chip-verified">Human cohort</span><h3>Imperial College London / EPIC</h3><p>A 2017 European cohort of more than 500,000 people across 10 countries found higher coffee consumption was associated with lower all-cause mortality. The study was observational: it establishes an association, not proof that coffee causes longer life.</p><p class="note mono">Imperial College London · Annals of Internal Medicine · 2017</p></article>
      <article class="card stack"><span class="chip chip-target">Emerging biology</span><h3>Trigonelline → NAD+ pathway</h3><p>Nature Metabolism research in 2024 identified trigonelline as an NAD+ precursor through the NAPRT-dependent Preiss–Handler pathway. Human associations were paired with experiments in primary muscle cells, mice and C. elegans.</p><p class="note mono">Nature Metabolism · 2024 · research evidence, not a Colita product claim</p></article>
      <article class="card stack"><span class="chip chip-target">Longevity model</span><h3>Trigonelline &amp; lifespan research</h3><p>A 2021 C. elegans study reported approximately 17.9% lifespan extension at the tested trigonelline condition and implicated AMPK, DAF-16/FOXO and HSF-1 signalling. This was a worm model, not a human longevity trial.</p><p class="note mono">Preclinical model · 2021</p></article>
      <article class="card stack"><span class="chip chip-verified">Coffee chemistry</span><h3>Green coffee bioactives</h3><p>Published green-Arabica research has measured substantial natural variation in chlorogenic acids, trigonelline and caffeine. That makes origin, variety and processing relevant not only to flavour, but also to the molecular starting material.</p><p class="note mono">Research range: CGAs 3.29–7.73%; trigonelline 0.53–1.27%; caffeine 0.78–1.55% dry mass in one 2024 Arabica dataset</p></article>
      <article class="card stack"><span class="chip chip-target">Extraction R&amp;D</span><h3>Ultrasound-Assisted Extraction (UAE)</h3><p>UAE uses acoustic cavitation and microstreaming to increase mass transfer. Coffee studies have investigated recovery of chlorogenic acid, trigonelline, caffeine and caffeic acid while controlling time, temperature, particle size and solvent system.</p><p class="note mono">R&amp;D route · parameters and yields must be validated lot by lot</p></article>
      <article class="card stack"><span class="chip chip-target">Research frontier</span><h3>More than CGA</h3><p>Our watchlist includes 5-CQA and other CGA isomers, trigonelline, caffeine, caffeic acid, cafestol, kahweol, tocopherols, minor methylxanthines and coffee polysaccharides. Roasting also creates compounds such as melanoidins — coffee chemistry is transformed, not simply "destroyed" by heat.</p><p class="note mono">Measure first. Claim second.</p></article>
    </div>
  </div>
</section>

<section id="revenue-platform">
  <div class="wrap stack-lg">
    <div class="stack narrow"><p class="eyebrow">Commercial Platform / One Bean</p><h2>One bean. Multiple revenue paths.</h2><p class="lead">The green bean is not a single finished product. Selection, processing, format and extraction create several distinct commercial routes from the same coffee knowledge base.</p></div>
    <div class="grid-4">
      <article class="card stack"><span class="chip chip-verified">Core</span><h3>Curated green lots</h3><p>Traceable coffees selected for quality, provenance, variety and buyer fit — supplied as green coffee for specialty customers.</p></article>
      <article class="card stack"><span class="chip chip-verified">Core</span><h3>Made-to-order coffee</h3><p>Buyers define a sensory direction; we design the processing and fermentation route around the target rather than asking them to choose only from a fixed catalogue.</p></article>
      <article class="card stack"><span class="chip chip-verified">Core</span><h3>Fermentation development</h3><p>Controlled and prolonged fermentation protocols developed around origin, coffee material and desired cup profile.</p></article>
      <article class="card stack"><span class="chip chip-verified">Format</span><h3>Ground &amp; finished formats</h3><p>Coffee can move downstream into ground and convenience formats where the commercial brief requires a consumer-ready product.</p></article>
      <article class="card stack"><span class="chip chip-target">Development</span><h3>Bioactive extracts</h3><p>Research into standardised coffee-derived extracts centred on chlorogenic acids, trigonelline and the wider green-coffee molecular matrix.</p></article>
      <article class="card stack"><span class="chip chip-target">Development</span><h3>Molecular fractions</h3><p>Potential CGA-rich, trigonelline-rich and controlled-caffeine fractions, subject to process validation, analytical specification and regulatory review.</p></article>
      <article class="card stack"><span class="chip chip-target">Development</span><h3>Natural caffeine recovery</h3><p>Extraction and fractionation can create more than one useful stream. Recovered coffee caffeine is being assessed as part of the whole-bean value model.</p></article>
      <article class="card stack"><span class="chip chip-gap">Future</span><h3>Process IP &amp; licensing</h3><p>Validated fermentation and extraction protocols may create licensable know-how, private-development work and technology partnerships.</p></article>
    </div>
  </div>
</section>

<section id="recognition-track-record">
  <div class="wrap stack-lg">
    <div class="stack narrow"><p class="eyebrow">Track Record / Independent Evidence</p><h2>Years of work before the pitch.</h2><p class="lead">The archive shows practical coffee work, professional profiling and export preparation alongside the research programme.</p></div>
    <div class="grid-3">
      <article class="card stack"><span class="chip chip-verified">Featured</span><h3>Perfect Daily Grind</h3><p>Steven Restrepo, Head of Coffee at Café de Colita, was interviewed by Perfect Daily Grind for industry perspective on infused and flavoured coffee processing — alongside voices including Saša Šestić of ONA Coffee / Project Origin.</p><p class="note mono">Independent specialty-coffee media recognition</p></article>
      <article class="card stack"><span class="chip chip-verified">Archive · 2019</span><h3>Professional cupping &amp; profiling</h3><p>Historical records with Cony Perez document repeated cupping and profiling work across Colombian coffees, including June 2019 results for 10 cuppings and later files covering harvest dates, annual production, available quantities, pricing and coffees prepared for export.</p><p class="note mono">Archived: cupping sheets, profile PDFs, supplier/export workbooks</p></article>
      <article class="card stack"><span class="chip chip-target">Competition signal</span><h3>Cup of Excellence — Experimental</h3><p>Cup of Excellence competitions in multiple countries now include formal Experimental categories. That creates a recognised competition lane for coffees whose value is built through advanced processing and fermentation.</p><p class="note mono">International category development; not a claim that Colombia currently runs the same category</p></article>
    </div>
    <div class="card stack"><p class="eyebrow">Archive depth</p><h3>From cup profile to export decision</h3><p>The 2019 email archive includes named profile sheets for multiple producers and processes, spreadsheets of coffees cupped for export, supplier quotations, quantities available, harvest timing and annual production. This is operating history — not a newly invented brand narrative.</p></div>
  </div>
</section>

<section id="fermentists-people">
  <div class="wrap stack-lg">
    <div class="stack narrow"><p class="eyebrow">Fermentists of Origin™ / People</p><h2>Carlos Andrés</h2><p class="lead">The people behind the process.</p></div>
    <div class="card stack"><span class="chip chip-target">Profile in development</span><h3>Origin, fermentation and the work on the ground</h3><p>This section is reserved for Carlos Andrés' story, role and contribution to Fermentists of Origin™. The final account will be added from his real history and your first-hand record — not filled with generic biography.</p></div>
  </div>
</section>
'''
    low = s.lower()
    anchor = '</main>' if '</main>' in low else '</body>'
    idx = low.rfind(anchor)
    if idx == -1:
        raise SystemExit('Could not find </main> or </body> insertion anchor')
    s = s[:idx] + new_sections + '\n' + s[idx:]

p.write_text(s, encoding='utf-8')
Path('SITE_EXPANSION_REPORT.md').write_text(f'''# Colita site expansion report\n\n- Expansion marker present: {marker in s}\n- Old price sections removed: {len(remove_spans)}\n- Original bytes: {len(original.encode("utf-8")):,}\n- Updated bytes: {len(s.encode("utf-8")):,}\n\n## Removed section previews\n\n''' + ('\n\n'.join('- ' + x for x in removed_labels) if removed_labels else '- No exact price/range section was automatically matched; manual follow-up required.') + '''\n\n## Added\n- Research & Science\n- One Bean / Multiple Revenue Paths\n- Track Record / Independent Evidence\n- Carlos Andrés / Fermentists of Origin scaffold\n''', encoding='utf-8')
print(Path('SITE_EXPANSION_REPORT.md').read_text())
