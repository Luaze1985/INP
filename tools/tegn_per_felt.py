import json
import re

base = "docs/reference/prosjektbeskrivelse/"
txt = open(base + "innsendingspakker/v2.1/innlimingstekst-til-godkjenning.md", encoding="utf-8").read().replace("\r\n", "\n")
ps = json.load(open(base + "innsendingspakker/v2.1/portalstruktur.json", encoding="utf-8"))
lim = {f["name"]: f["character_limit"] for s in ps["portal_sections"] for f in s["fields"] if f.get("character_limit")}
for part in re.split(r"(?m)^## ", txt)[1:]:
    head, _, body = part.partition("\n")
    head = head.strip()
    if head.startswith("AP"):
        continue
    n = len(body.strip())
    L = lim.get(head, "?")
    print(f"{head[:42]:42} {n:5} / {L}")
