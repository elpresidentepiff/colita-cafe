from pathlib import Path
import re

p = Path("index.html")
html = p.read_text(encoding="utf-8")

start = html.find('<!-- COFFEE CHEMISTRY EDUCATION START -->')
end_marker = '<!-- COFFEE CHEMISTRY EDUCATION END -->'
end = html.find(end_marker)

if start != -1 and end != -1 and end > start:
    end += len(end_marker)
    block = html[start:end]
    block = block.replace(
        '<section id="coffee-chemistry" style="padding:72px 6%;background:#f4efe5;color:#182018;">',
        '<section id="coffee-chemistry" style="background:var(--surface-2);border-block:1px solid var(--border)">',
    )
    block = block.replace(
        '<div style="max-width:1180px;margin:0 auto;">',
        '<div class="wrap stack-lg">',
        1,
    )
    block = block.replace(
        '<article style="background:#fff;padding:26px;border-radius:18px;">',
        '<article class="card stack">',
    )
    block = block.replace(
        '<div style="margin-top:28px;padding:30px;border:1px solid rgba(24,32,24,.18);border-radius:18px;">',
        '<div class="callout">',
    )
    block = block.replace(
        '<article style="padding:26px;background:#172017;color:#f6f0e4;border-radius:18px;">',
        '<article class="card stack" style="background:var(--text);color:var(--ground)">',
    )
    if re.search(r'#[0-9a-fA-F]{3,8}\b', block):
        raise RuntimeError("Coffee chemistry block still contains hard-coded hex colours")
    html = html[:start] + block + html[end:]

p.write_text(html, encoding="utf-8")
print("Existing Colita design system restored")
