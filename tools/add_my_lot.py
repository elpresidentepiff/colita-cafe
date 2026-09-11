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
<section id="my-lot-coffee" style="padding:84px 6%;background:#152018;color:#f7f1e6;">
  <div style="max-width:1180px;margin:0 auto;">
    <p style="letter-spacing:.17em;text-transform:uppercase;font-size:.78rem;font-weight:700;margin:0 0 14px;opacity:.78;">Colita Café presents</p>
    <h2 style="font-size:clamp(2.5rem,6.5vw,5.8rem);line-height:.92;margin:0 0 22px;max-width:980px;">MY LOT COFFEE</h2>
    <p style="font-size:clamp(1.25rem,2.5vw,2rem);line-height:1.25;max-width:920px;margin:0 0 24px;font-weight:600;">Your trees. Your lot. Your process. Your coffee.</p>
    <p style="font-size:1.15rem;line-height:1.75;max-width:920px;margin:0;opacity:.92;">This is not a conventional coffee subscription. My Lot Coffee is a fully immersive origin experience built around a defined allocation of coffee at source. Instead of receiving anonymous beans chosen from a warehouse, you follow your coffee from the farm through harvest, fermentation, drying, roasting and delivery. You do not simply subscribe to coffee. You build a relationship with the coffee that becomes yours.</p>

    <div style="margin-top:38px;padding:30px;border:1px solid rgba(247,241,230,.22);border-radius:20px;background:rgba(255,255,255,.035);">
      <p style="letter-spacing:.13em;text-transform:uppercase;font-size:.75rem;font-weight:700;margin:0 0 10px;opacity:.72;">Why it is different</p>
      <h3 style="font-size:clamp(1.7rem,4vw,3rem);line-height:1.05;margin:0 0 18px;max-width:900px;">A coffee subscription unlike the standard subscription model.</h3>
      <p style="font-size:1.05rem;line-height:1.7;max-width:900px;margin:0;">The normal model sells you a bag. My Lot Coffee connects you to a living crop, a real origin and the decisions that shape flavour. Traceability is not a QR code added at the end. It begins with the lot itself.</p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin-top:28px;">
      <article style="padding:24px;border-radius:18px;background:#f7f1e6;color:#172017;"><p style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 8px;">01 · Reserve</p><h3 style="margin:0 0 10px;font-size:1.35rem;">Your allocation</h3><p style="margin:0;line-height:1.6;">Your membership is linked to a defined coffee allocation at origin, giving your coffee a real place and identity from the beginning.</p></article>
      <article style="padding:24px;border-radius:18px;background:#f7f1e6;color:#172017;"><p style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 8px;">02 · Follow</p><h3 style="margin:0 0 10px;font-size:1.35rem;">The crop</h3><p style="margin:0;line-height:1.6;">Follow the journey at farm level: crop development, harvest and the people responsible for producing your coffee.</p></article>
      <article style="padding:24px;border-radius:18px;background:#f7f1e6;color:#172017;"><p style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 8px;">03 · Shape</p><h3 style="margin:0 0 10px;font-size:1.35rem;">The process</h3><p style="margin:0;line-height:1.6;">Experience how fermentation and processing decisions change flavour. Where the programme allows, members can help shape the profile they want to explore.</p></article>
      <article style="padding:24px;border-radius:18px;background:#f7f1e6;color:#172017;"><p style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 8px;">04 · Receive</p><h3 style="margin:0 0 10px;font-size:1.35rem;">Your coffee</h3><p style="margin:0;line-height:1.6;">Receive coffee connected back to your allocated origin and process, with the story and production journey intact.</p></article>
      <article style="padding:24px;border-radius:18px;background:#f7f1e6;color:#172017;"><p style="font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 8px;">05 · Immerse</p><h3 style="margin:0 0 10px;font-size:1.35rem;">Visit origin</h3><p style="margin:0;line-height:1.6;">The ultimate expression of the experience is origin itself: the opportunity to visit the farm, meet the people and see where your coffee begins.</p></article>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:28px;">
      <article style="padding:28px;border-radius:18px;border:1px solid rgba(247,241,230,.22);"><p style="font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 10px;opacity:.7;">Total traceability</p><h3 style="font-size:1.5rem;margin:0 0 10px;">Know where it came from.</h3><p style="line-height:1.65;margin:0;opacity:.9;">Farm, lot, process and production story remain connected. The point is not more marketing information. The point is genuine origin knowledge.</p></article>
      <article style="padding:28px;border-radius:18px;border:1px solid rgba(247,241,230,.22);"><p style="font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 10px;opacity:.7;">Process participation</p><h3 style="font-size:1.5rem;margin:0 0 10px;">Understand why it tastes that way.</h3><p style="line-height:1.65;margin:0;opacity:.9;">Members learn the relationship between fruit, fermentation, drying, roasting and final cup profile instead of seeing coffee only as a finished retail product.</p></article>
      <article style="padding:28px;border-radius:18px;border:1px solid rgba(247,241,230,.22);"><p style="font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:0 0 10px;opacity:.7;">Origin relationship</p><h3 style="font-size:1.5rem;margin:0 0 10px;">From customer to participant.</h3><p style="line-height:1.65;margin:0;opacity:.9;">The experience is designed to close the distance between the person drinking the coffee and the people, land and decisions that created it.</p></article>
    </div>

    <div style="margin-top:36px;padding:34px;border-radius:20px;background:#f7f1e6;color:#172017;">
      <p style="font-size:.78rem;letter-spacing:.15em;text-transform:uppercase;font-weight:700;margin:0 0 10px;">The idea in one sentence</p>
      <p style="font-size:clamp(1.55rem,3.4vw,2.8rem);line-height:1.12;margin:0;font-weight:700;max-width:980px;">Most subscriptions deliver coffee to your door. My Lot Coffee takes you all the way back to where your coffee begins.</p>
    </div>
  </div>
</section>
<!-- MY LOT COFFEE END -->
'''

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
print("My Lot Coffee flagship experience added")
