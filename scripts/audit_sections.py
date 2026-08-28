#!/usr/bin/env python3
from pathlib import Path
import re, html
s=Path('index.html').read_text(encoding='utf-8')
rows=[]
for i,m in enumerate(re.finditer(r'<section\b[^>]*>.*?</section>',s,flags=re.I|re.S),1):
    block=m.group(0)
    tag=block.split('>',1)[0]+'>'
    text=html.unescape(re.sub(r'<[^>]+>',' ',block))
    text=re.sub(r'\s+',' ',text).strip()
    nums=' '.join(re.findall(r'(?:£|\$|€)?\d+(?:\.\d+)?%?\+?',text))
    rows.append(f'## Section {i}\n\n`{tag[:180]}`\n\n**Numbers:** {nums[:500]}\n\n{text[:700]}\n')
Path('SECTION_AUDIT.md').write_text('# Section audit\n\n'+ '\n'.join(rows),encoding='utf-8')
print(f'Wrote {len(rows)} sections')
