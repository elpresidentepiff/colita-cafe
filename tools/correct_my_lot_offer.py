from pathlib import Path

p = Path("index.html")
html = p.read_text(encoding="utf-8")

replacements = {
    "€1,500": "£900",
    "48 kg": "24 kg",
    "48 kg of coffee": "24 kg of coffee",
    "2 kg / month": "1 kg / month",
    "2 kg to your door": "1 kg to your door",
    "€31.25 / kg": "£37.50 / kg",
    "€1,500 divided across the 48 kg membership allocation.": "£900 divided across the 24 kg membership allocation.",
    "approximately 48 kg of coffee to each member over 24 months": "24 kg of coffee to each member over 24 months",
    "Forty-eight kilograms.": "Twenty-four kilograms.",
}

for old, new in replacements.items():
    html = html.replace(old, new)

p.write_text(html, encoding="utf-8")
print("My Lot Coffee offer corrected to £900 / 24 months / 24 kg / 1 kg monthly")
