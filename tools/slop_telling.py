import re
from collections import defaultdict

F = "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v2.0.md"
txt = open(F, encoding="utf-8").read().replace("\r\n", "\n")
fields = []
for part in re.split(r"(?m)^## ", txt)[1:]:
    head, _, body = part.partition("\n")
    head = head.strip()
    if head.startswith(("PROSJEKTTITTEL", "KORTNAVN", "Referanseliste")) or " · " in head:
        continue
    fields.append((head, body.strip()))

LADDER = r"(?m)(?:^|(?<=[.!?] ))(Da|Derfor|Deretter|Først|Så|Til slutt|Slik|Dermed|Samtidig)\b"
rows = []
grams = defaultdict(set)
for head, body in fields:
    sents = [s for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]
    words = re.findall(r"\w+", body)
    nw = max(len(words), 1)
    lists = 0
    for s in sents:
        # 3+ ledd: minst to komma før siste og/eller i samme setning
        for m in re.finditer(r"([^,.;:]+,){2,}[^,.;:]+\b(og|eller)\b", s):
            lists += 1
    ladder = len(re.findall(LADDER, body))
    dash = body.count("—") + len(re.findall(r" – ", body))
    colon = len(re.findall(r":\s", body))
    contrast = len(re.findall(r"\bikke\b[^.]{0,80}\bmen\b", body))
    nomin = sum(1 for w in words if re.search(r"(ing|ingen|else|elsen|het|heten|asjon|asjonen)$", w.lower()) and len(w) > 6)
    bullets = len(re.findall(r"(?m)^- ", body))
    avg = nw / max(len(sents), 1)
    rows.append((head, nw, lists, ladder, dash, colon, contrast, round(100 * nomin / nw, 1), bullets, round(avg, 1)))
    toks = [w.lower() for w in words]
    for i in range(len(toks) - 4):
        grams[" ".join(toks[i:i + 5])].add(head)

print(f"{'Felt':38} ord ramse trapp strek kolon kontr nom% pkt snittsetn")
for r in rows:
    print(f"{r[0][:38]:38} {r[1]:4} {r[2]:5} {r[3]:5} {r[4]:5} {r[5]:5} {r[6]:5} {r[7]:5} {r[8]:3} {r[9]:6}")

print("\nGjentatte 5-ord-fraser på tvers av felt (3+ felt):")
rep = sorted(((g, fs) for g, fs in grams.items() if len(fs) >= 3), key=lambda x: -len(x[1]))
for g, fs in rep[:15]:
    print(f"  '{g}' -> {len(fs)} felt: {', '.join(sorted(f[:18] for f in fs))}")
