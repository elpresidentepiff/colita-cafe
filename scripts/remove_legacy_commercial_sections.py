#!/usr/bin/env python3
from pathlib import Path
import re, html
p=Path('index.html')
s=p.read_text(encoding='utf-8')
removed=[]
for m in reversed(list(re.finditer(r'<section\b[^>]*>.*?</section>',s,flags=re.I|re.S))):
    block=m.group(0)
    text=html.unescape(re.sub(r'<[^>]+>',' ',block))
    text=re.sub(r'\s+',' ',text).strip()
    low=text.lower()
    if low.startswith('business model stop buying coffee') or low.startswith('why london first'):
        removed.append(text[:300])
        s=s[:m.start()]+s[m.end():]
p.write_text(s,encoding='utf-8')
Path('LEGACY_SECTION_REMOVAL.md').write_text('# Legacy commercial sections removed\n\n' + ('\n\n'.join('- '+x for x in reversed(removed)) if removed else '- No matching legacy sections found.') + '\n',encoding='utf-8')
print(f'Removed {len(removed)} legacy sections')
