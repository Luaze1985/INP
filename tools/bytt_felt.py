"""Bytt ut hele feltet: py felt.py "<Feltnavn>" "<Neste feltnavn>" tekstfil.txt"""
import sys

F = "docs/reference/prosjektbeskrivelse/soknadstekst-samlet-kandidat-v2.0.md"
name, nxt, src = sys.argv[1], sys.argv[2], sys.argv[3]
body = open(src, encoding="utf-8").read().replace("\r\n", "\n").strip()
raw = open(F, encoding="utf-8", newline="").read()
nl = "\r\n" if "\r\n" in raw else "\n"
s = raw.index("## " + name + nl)
e = raw.index("## " + nxt)
raw = raw[:s] + "## " + name + nl + nl + body.replace("\n", nl) + nl + nl + raw[e:]
open(F, "w", encoding="utf-8", newline="").write(raw)
print(name, len(body))
