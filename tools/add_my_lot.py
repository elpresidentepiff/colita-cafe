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
      <p class="mono" style="letter-spacing:.17em;text-transform:uppercase;font-size:.78rem;font-weight:700;margin:0;">Colita Café presents · Founding membership</p>
      <h2 style="font-size:clamp(2.5rem,6.5vw,5.8rem);line-height:.92;margin:0;max-width:980px;text-wrap:balance;">MY LOT COFFEE</h2>
      <p style="font-size:clamp(1.3rem,2.7vw,2.15rem);line-height:1.22;max-width:960px;margin:0;font-weight:650;text-wrap:balance;">Not a coffee subscription. A two-year relationship with your own coffee at origin.</p>
      <p style="font-size:1.15rem;line-height:1.75;max-width:930px;margin:0;color:var(--text-2);">Most subscriptions choose a coffee, put it in a bag and send it to you. My Lot Coffee starts before the bag exists. Your membership is connected to a defined allocation of trees in Colombia, the crop they produce, the processing decisions that shape flavour and the people growing it. You follow the coffee from tree to cup — then drink the result every month.</p>
    </div>

    <div class="callout stack">
      <p class="mono" style="letter-spacing:.13em;text-transform:uppercase;font-size:.75rem;font-weight:700;margin:0;">The membership</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;">
        <div class="card stack"><p class="mono" style="margin:0;">€1,500</p><h3 style="margin:0;">24 months</h3><p style="margin:0;">One two-year My Lot membership.</p></div>
        <div class="card stack"><p class="mono" style="margin:0;">40 trees</p><h3 style="margin:0;">Your allocation</h3><p style="margin:0;">A defined coffee-tree allocation linked to your membership.</p></div>
        <div class="card stack"><p class="mono" style="margin:0;">48 kg</p><h3 style="margin:0;">Across two years</h3><p style="margin:0;">The model allocates approximately 48 kg of coffee to each member over 24 months.</p></div>
        <div class="card stack"><p class="mono" style="margin:0;">2 kg / month</p><h3 style="margin:0;">Delivered</h3><p style="margin:0;">Your regular roasted-coffee allocation, month after month.</p></div>
        <div class="card stack"><p class="mono" style="margin:0;">€31.25 / kg</p><h3 style="margin:0;">Effective coffee value</h3><p style="margin:0;">€1,500 divided across the 48 kg membership allocation.</p></div>
      </div>
      <p class="note mono" style="margin:0;">Founding model: limited to 2,500 initial members.</p>
    </div>

    <div class="stack">
      <p class="mono" style="letter-spacing:.13em;text-transform:uppercase;font-size:.75rem;font-weight:700;margin:0;">What you are actually paying for</p>
      <h3 style="font-size:clamp(1.8rem,4vw,3.2rem);line-height:1.05;margin:0;max-width:950px;text-wrap:balance;">Coffee is only the physical part of the membership.</h3>
      <p style="max-width:900px;font-size:1.06rem;line-height:1.7;margin:0;color:var(--text-2);">The value is the complete origin experience: your allocation, your monthly coffee, direct visibility into the farm, participation in processing choices, education, traceability and a route to physically stand at origin with the people producing it.</p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;">
      <article class="card stack"><p class="mono" style="margin:0;">01 · YOUR TREES</p><h3 style="margin:0;">40-tree allocation</h3><p style="margin:0;line-height:1.6;">You are not assigned a random bag each month. Your membership starts with a defined allocation at origin, giving your coffee a place, crop and identity from the beginning.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">02 · LIVE ORIGIN</p><h3 style="margin:0;">24/7 farm access</h3><p style="margin:0;line-height:1.6;">A live farm feed is designed to let members look into origin whenever they want — not only when a marketing video is released.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">03 · THE HARVEST</p><h3 style="margin:0;">Follow the crop</h3><p style="margin:0;line-height:1.6;">See the agricultural journey behind the coffee: crop development, picking, processing and the people responsible for producing it.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">04 · FERMENTATION</p><h3 style="margin:0;">Choose the process</h3><p style="margin:0;line-height:1.6;">Members can explore processing directions including washed, natural, honey, anaerobic and carbonic maceration, connecting process decisions directly to flavour.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">05 · ROAST</p><h3 style="margin:0;">Choose your direction</h3><p style="margin:0;line-height:1.6;">Light, medium or dark roast pathways let members understand how the same origin changes when roast development changes.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">06 · MONTHLY COFFEE</p><h3 style="margin:0;">2 kg to your door</h3><p style="margin:0;line-height:1.6;">The experience becomes tangible every month: roasted coffee tied back to the member allocation and the production journey behind it.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">07 · EDUCATION</p><h3 style="margin:0;">Learn while you drink</h3><p style="margin:0;line-height:1.6;">Monthly coffee and brewing education turns the membership into an ongoing course in origin, fermentation, roasting and extraction.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">08 · TRACEABILITY</p><h3 style="margin:0;">Tree-to-door record</h3><p style="margin:0;line-height:1.6;">The original model records key stages from picking and processing through milling, export, roasting and delivery, creating a persistent production history rather than a generic origin claim.</p></article>
    </div>

    <div class="callout stack">
      <p class="mono" style="letter-spacing:.13em;text-transform:uppercase;font-size:.75rem;font-weight:700;margin:0;">The immersive experience</p>
      <h3 style="font-size:clamp(1.8rem,4vw,3.3rem);line-height:1.05;margin:0;max-width:950px;text-wrap:balance;">Watch it. Shape it. Learn it. Drink it. Then come to Colombia and stand in it.</h3>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;">
        <article class="card stack"><p class="mono" style="margin:0;">LIVE</p><h4 style="margin:0;font-size:1.2rem;">The farm never becomes abstract</h4><p style="margin:0;">24-hour visual access keeps the member connected to the place where the coffee is growing.</p></article>
        <article class="card stack"><p class="mono" style="margin:0;">PARTICIPATE</p><h4 style="margin:0;font-size:1.2rem;">Understand the decisions</h4><p style="margin:0;">Process and roast choices turn fermentation and roasting from labels on a bag into decisions the member can understand and experience.</p></article>
        <article class="card stack"><p class="mono" style="margin:0;">VISIT</p><h4 style="margin:0;font-size:1.2rem;">Seven days at origin</h4><p style="margin:0;">When a group of 10 members is formed, the original programme includes a seven-day Colombia experience with food, accommodation and the farm tour included. Flights are excluded, and members may bring a plus-one.</p></article>
      </div>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;">
      <article class="card stack"><p class="mono" style="margin:0;">FRESHNESS</p><h3 style="margin:0;">Roast close to dispatch.</h3><p style="margin:0;line-height:1.65;">The original service model targets coffee being roasted and shipped within 2–3 days, keeping the physical product aligned with the premium experience.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">FLEXIBILITY</p><h3 style="margin:0;">A membership, not a trap.</h3><p style="margin:0;line-height:1.65;">The original terms included cancellation with 90 days' notice rather than locking a member into the full term without an exit route.</p></article>
      <article class="card stack"><p class="mono" style="margin:0;">IMPACT</p><h3 style="margin:0;">Origin should benefit too.</h3><p style="margin:0;line-height:1.65;">The founding model directs 5% of proceeds to the Colita Farming Foundation, keeping part of the membership value connected to the producing community.</p></article>
    </div>

    <div class="callout stack">
      <p class="mono" style="font-size:.78rem;letter-spacing:.15em;text-transform:uppercase;font-weight:700;margin:0;">Why My Lot is different</p>
      <p style="font-size:clamp(1.6rem,3.7vw,3rem);line-height:1.1;margin:0;font-weight:700;max-width:1020px;text-wrap:balance;">You are not subscribing to bags of coffee. You are subscribing to the life of a coffee crop — from the trees and the decisions at origin to the coffee arriving at your door.</p>
      <p style="font-size:1.1rem;line-height:1.7;max-width:900px;margin:0;color:var(--text-2);">Forty trees. Forty-eight kilograms. Twenty-four months. A live connection to origin. Processing and roast participation. Monthly education. Full production traceability. And a pathway to experience the farm in Colombia yourself. That is My Lot Coffee.</p>
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
print("My Lot Coffee full subscription experience restored")
