# Writes heatmap.svg (dark, green) from public contribution data. Run: python3 heatmap.py
import json, urllib.request, datetime as dt
d = json.load(urllib.request.urlopen("https://github-contributions-api.jogruber.de/v4/n-stau?y=last"))
days = d["contributions"]
col = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
first = dt.date.fromisoformat(days[0]["date"])
off = (first.weekday() + 1) % 7  # GitHub weeks start on Sunday
S, G = 11, 3
w = (len(days) + off) // 7 + 2
rects = []
for i, x in enumerate(days):
    n = i + off
    rects.append(f'<rect x="{30 + n // 7 * (S + G)}" y="{20 + n % 7 * (S + G)}" width="{S}" height="{S}" rx="2" fill="{col[x["level"]]}"><title>{x["date"]}: {x["count"]}</title></rect>')
open("heatmap.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{30 + w * (S + G)}" height="130" viewBox="0 0 {30 + w * (S + G)} 130">'
    f'<rect width="100%" height="100%" rx="8" fill="#0d1117"/>' + "".join(rects) + "</svg>")
