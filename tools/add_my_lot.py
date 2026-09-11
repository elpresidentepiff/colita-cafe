from pathlib import Path
import re

p = Path("index.html")
html = p.read_text(encoding="utf-8")

# Rebuild My Lot Coffee cleanly on every run.
html = re.sub(
    r'(?is)\s*<!-- MY LOT COFFEE START -->.*?<!-- MY LOT COFFEE END -->\s*',
    '\n',
    html,
)

my_lot = r'''
<!-- MY LOT COFFEE START -->
<section id="my-lot-coffee" style="padding-block:84px;background:var(--surface-2);color:var(--text);border-block:1px solid var(--border);">
  <div class="wrap stack-lg">
    <div class="stack">
      <p class="mono" style="letter-spacing:.17em;text-transform:uppercase;font-size:.78rem;font-weight:700;margin:0;">Colita Café presents</p>
      <h2 style="font-size:clamp(2.5rem,6.5vw,5.8rem);line-height:.92;margin:0;max-width:980px;text-wrap:balance;">MY LOT COFFEE</h2>
      <p style="font-size:clamp(1.25rem,2.5vw,2rem);line-height:1.25;max-width:920px;margin:0;font-weight:600;text-wrap:balance;">Your trees. Your lot. Your process. Your coffee.</p>
      <p style="font-size:1.15rem;line-height:1.75;max-width:920px;margin:0;color:var(--text-2);">This is not a conventional coffee subscription. My Lot Coffee is a fully immersive origin experience built around a defined allocation of coffee at source. Instead of receiving anonymous beans chosen from a warehouse, you follow your coffee from the farm through harvest, fermentation, drying, roasting and delivery. You do not simply subscribe to coffee. You build a relationship with the coffee that becomes yours.</p>
    </div>

    <div class="callout stack">
      <p class="mono" style="letter-spacing:.13em;text-transform:uppercase;font-size:.75rem;font-weight:700;margin:0;">Why it is different</p>
      <h3 style="font-size:clamp(1.7rem,4vw,3rem);line-height:1.05;margin:0;max-width:900px;text-wrap:balance;">A coffee subscription unlike the standard subscription model.</h3>
      <p style="font-size:1.05rem;line-height:1.7;max-width:900px;margin:0;">The normal model sells you a bag. My Lot Coffee connects you to a living crop, a real origin and the decisions that shape flavour. Traceability is not a QR code added at the end. It begins with the lot itself.</p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;">
      <article class="card stack"><p class="mono" style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">01 · Reserve</p><h3 style="margin:0;font-size:1.35rem;">Your allocation</h3><p style="margin:0;line-height:1.6;">Your membership is linked to a defined coffee allocation at origin, giving your coffee a real place and identity from the beginning.</p></article>
      <article class="card stack"><p class="mono" style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">02 · Follow</p><h3 style="margin:0;font-size:1.35rem;">The crop</h3><p style="margin:0;line-height:1.6;">Follow the journey at farm level: crop development, harvest and the people responsible for producing your coffee.</p></article>
      <article class="card stack"><p class="mono" style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">03 · Shape</p><h3 style="margin:0;font-size:1.35rem;">The process</h3><p style="margin:0;line-height:1.6;">Experience how fermentation and processing decisions change flavour. Where the programme allows, members can help shape the profile they want to explore.</p></article>
      <article class="card stack"><p class="mono" style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">04 · Receive</p><h3 style="margin:0;font-size:1.35rem;">Your coffee</h3><p style="margin:0;line-height:1.6;">Receive coffee connected back to your allocated origin and process, with the story and production journey intact.</p></article>
      <article class="card stack"><p class="mono" style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">05 · Immerse</p><h3 style="margin:0;font-size:1.35rem;">Visit origin</h3><p style="margin:0;line-height:1.6;">The ultimate expression of the experience is origin itself: the opportunity to visit the farm, meet the people and see where your coffee begins.</p></article>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;">
      <article class="card stack"><p class="mono" style="font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">Total traceability</p><h3 style="font-size:1.5rem;margin:0;">Know where it came from.</h3><p style="line-height:1.65;margin:0;">Farm, lot, process and production story remain connected. The point is not more marketing information. The point is genuine origin knowledge.</p></article>
      <article class="card stack"><p class="mono" style="font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">Process participation</p><h3 style="font-size:1.5rem;margin:0;">Understand why it tastes that way.</h3><p style="line-height:1.65;margin:0;">Members learn the relationship between fruit, fermentation, drying, roasting and final cup profile instead of seeing coffee only as a finished retail product.</p></article>
      <article class="card stack"><p class="mono" style="font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0;">Origin relationship</p><h3 style="font-size:1.5rem;margin:0;">From customer to participant.</h3><p style="line-height:1.65;margin:0;">The experience is designed to close the distance between the person drinking the coffee and the people, land and decisions that created it.</p></article>
    </div>

    <div class="callout stack">
      <p class="mono" style="font-size:.78rem;letter-spacing:.15em;text-transform:uppercase;font-weight:700;margin:0;">The idea in one sentence</p>
      <p style="font-size:clamp(1.55rem,3.4vw,2.8rem);line-height:1.12;margin:0;font-weight:700;max-width:980px;text-wrap:balance;">Most subscriptions deliver coffee to your door. My Lot Coffee takes you all the way back to where your coffee begins.</p>
    </div>
  </div>
</section>
<!-- MY LOT COFFEE END -->
'''

if re.search(r'#[0-9a-fA-F]{3,8}\b', my_lot):
    raise RuntimeError("My Lot Coffee markup must use site colour tokens, not hex literals")

marker = '<!-- COFFEE CHEMISTRY EDUCATION END -->'
pos = html.find(marker)
if pos != -1:
    pos += len(marker)
    html = html[:pos] + my_lot + html[pos:]
else:
    m = re.search(r'(?is)<main\b[^>]*>', html)
    if m:
        html = html[:m.end()] + my_lot + html[m.end():]
    else:
        m = re.search(r'(?is)<body\b[^>]*>', html)
        if m:
            html = html[:m.end()] + my_lot + html[m.end():]

p.write_text(html, encoding="utf-8")
print("My Lot Coffee flagship experience added using Colita design tokens")
