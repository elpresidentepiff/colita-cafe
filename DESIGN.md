# Design standard

The rules this site is built on. Anything added later should be able to point at
a line in here. If it can't, it probably shouldn't ship.

---

## 1. The one rule

**Nothing on the page may undermine the thing the page is asking for.**

This is an investor dossier. A section headed "To be completed" is not a
placeholder — to the reader it is evidence about how the company operates. Empty
states, TODOs, lorem, "coming soon" and unfinished tables cost more credibility
than the missing content would have earned. Cut it or finish it. Never ship it.

---

## 2. Tokens, never literals

Every colour comes from a token on `:root`. No hex codes in markup, ever.

```
--ground --surface --surface-2      grounds, back to front
--border --border-strong            hairlines
--text --text-2 --text-3            primary, secondary, quiet
--accent --accent-2 --accent-wash   amber. one accent, used sparingly
--cherry --verified                 semantic only, never decorative
```

The site renders in the reader's theme. Three states exist, not two: explicit
light, explicit dark, and the unstamped default where only
`prefers-color-scheme` decides. A colour defined **only** inside a media query
or `[data-theme]` block will be missing in the unstamped state — that is how you
ship dark text on a dark ground.

Test both themes before every push. The `#coffee-chemistry` section shipped with
`background:#f4efe5` inline and was unreadable in dark mode for weeks.

---

## 3. Type

Three faces, three jobs. They do not swap.

| Face | Role | Used for |
|---|---|---|
| **Archivo** | Structure | Headlines, UI, anything that must be scanned |
| **Newsreader** | Voice | Leads, pull quotes, big figures |
| **IBM Plex Mono** | Evidence | Numbers, sources, labels, eyebrows |

Mono is the tell that a number is real. Use it for every figure, citation and
source line — never for decoration. When a reader sees mono, they should be
looking at something checkable.

Body copy sits near 65 characters. Headlines get `text-wrap: balance`. Uppercase
labels get letter-spacing; nothing else does.

---

## 4. Evidence is a visual system, not a claim

The site's credibility rests on marking strength of evidence, in public, before
anyone asks.

- `chip-verified` — human trial, measured result, shipped fact
- `chip-target` — mechanism, model, intention, not yet proven
- `.note.mono` — the caveat, stated in the same breath as the claim

**Never state a finding without its strength.** A closing panel that says plainly
what the evidence does *not* show is worth more than three more findings. This is
why the bioactives section ends on "What we will not say".

---

## 5. Numbers earn their size

A figure gets display size only if it carries an argument. `2.2×` earns it.
A section count does not.

Give every big number a caption in plain language and a source line in mono.
A number without provenance reads as marketing; the same number with a source
reads as research. Same digits, opposite effect.

---

## 6. Restraint

One accent. One idea per section. Motion only where it clarifies.

Reveal-on-scroll must be **progressive enhancement** — hidden state scoped to a
class the script itself sets, so with JS off or reduced motion on, everything is
visible. Content that depends on JavaScript to become visible is content you can
lose.

Honour `prefers-reduced-motion` every time.

---

## 7. Structure

Sections close. The footer is the last element before `</body>` — nothing after
it. Content once sat past `</footer>`: the page ended, then kept going.

Wide content — tables, code, diagrams — scrolls inside its own container. The
body never scrolls sideways.

---

## 8. Before pushing

- [ ] Light and dark both render, on the unstamped default too
- [ ] No hex literals in markup
- [ ] Every figure has a caption and a source
- [ ] Every claim carries its evidence chip
- [ ] No placeholder, TODO or "to be completed" text anywhere
- [ ] Content visible with JavaScript disabled
- [ ] Nothing after `</footer>`
- [ ] Read it on a phone
