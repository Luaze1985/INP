import re
import sys

target_file = r"C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\docs\reference\prosjektbeskrivelse\k3-forskning-sannhetsserum-v0.5.md"

with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

content = "".join(lines)

print("=== EMPIRICAL SCAN REPORT FOR K3 CANDIDATE NOTE ===")
print(f"Total Lines: {len(lines)}")
print(f"Total Characters: {len(content)}\n")

# 1. FORBIDDEN / GUARDRAIL TERMS
print("--- CHECK 1: FORBIDDEN / GUARDRAIL TERMS ---")

# 1a. produktvalg
produktvalg_matches = []
for idx, line in enumerate(lines, 1):
    if re.search(r"\bproduktvalg\b", line, re.IGNORECASE):
        produktvalg_matches.append((idx, line.strip()))

print(f"Occurrences of 'produktvalg': {len(produktvalg_matches)}")
for line_num, text in produktvalg_matches:
    print(f"  Line {line_num}: {text}")

# 1b. velger automatisk / anbefaler automatisk / automatisk
auto_matches = []
for idx, line in enumerate(lines, 1):
    if re.search(r"velger\s+automatisk|anbefaler\s+automatisk|automatisk\s+velger|automatisk\s+anbefaler|automatisk\s+beslutning", line, re.IGNORECASE):
        auto_matches.append((idx, line.strip()))

print(f"\nOccurrences of 'velger automatisk / anbefaler automatisk': {len(auto_matches)}")
for line_num, text in auto_matches:
    print(f"  Line {line_num}: {text}")

# Also check any other usage of "anbefaler" or "velger" where VERIFIED is the subject
verified_auto = []
for idx, line in enumerate(lines, 1):
    if ("VERIFIED" in line or "modellen" in line or "verktøyet" in line) and re.search(r"\b(velger|anbefaler)\b", line, re.IGNORECASE):
        # Filter out if preceded by "ikke" or "aldri" or in list of forbidden
        verified_auto.append((idx, line.strip()))

print(f"\nOccurrences of VERIFIED/modellen/verktøyet + velger/anbefaler: {len(verified_auto)}")
for line_num, text in verified_auto:
    print(f"  Line {line_num}: {text}")

# 1c. svart boks
svart_boks_matches = []
for idx, line in enumerate(lines, 1):
    if re.search(r"svart\s*boks", line, re.IGNORECASE):
        svart_boks_matches.append((idx, line.strip()))

print(f"\nOccurrences of 'svart boks': {len(svart_boks_matches)}")
for line_num, text in svart_boks_matches:
    print(f"  Line {line_num}: {text}")

# 1d. integrasjonsflate
integrasjon_matches = []
for idx, line in enumerate(lines, 1):
    if re.search(r"integrasjonsflate", line, re.IGNORECASE):
        integrasjon_matches.append((idx, line.strip()))

print(f"\nOccurrences of 'integrasjonsflate': {len(integrasjon_matches)}")
for line_num, text in integrasjon_matches:
    print(f"  Line {line_num}: {text}")

# 1e. unqualified EBA
eba_matches = []
for idx, line in enumerate(lines, 1):
    # Match EBA not followed by _NO2023 or _EU2023 or preceded by EBA Norge / European Banking Authority if alone
    # Find all occurrences of word EBA
    tokens = re.findall(r"\bEBA\b(?!\s*(?:Norge|_NO2023|_EU2023|EU\b))", line)
    if tokens:
        # Check if line contains context
        eba_matches.append((idx, line.strip()))

print(f"\nOccurrences of potentially unqualified 'EBA': {len(eba_matches)}")
for line_num, text in eba_matches:
    print(f"  Line {line_num}: {text}")

# 2. PARKED SOURCES ([Wiik2025], [SA2018])
print("\n--- CHECK 2: PARKED SOURCES ---")
wiik_matches = []
sa_matches = []
for idx, line in enumerate(lines, 1):
    if "Wiik2025" in line:
        wiik_matches.append((idx, line.strip()))
    if "SA2018" in line:
        sa_matches.append((idx, line.strip()))

print(f"Occurrences of 'Wiik2025': {len(wiik_matches)}")
for line_num, text in wiik_matches:
    print(f"  Line {line_num}: {text}")

print(f"Occurrences of 'SA2018': {len(sa_matches)}")
for line_num, text in sa_matches:
    print(f"  Line {line_num}: {text}")

# 3. NORWEGIAN PRIMARY BASES (8 mandatory sources)
print("\n--- CHECK 3: NORWEGIAN PRIMARY BASES ---")
norwegian_keys = [
    "KD2024", "Multiconsult2023DiBK", "EBA_NO2023", 
    "GullbrekkenHolme2025", "Ingvaldsen2008", 
    "FinansNorge2024VASK", "BKA2", "Bjørheim2026"
]
for key in norwegian_keys:
    count = sum(1 for line in lines if key in line)
    print(f"  {key}: {count} occurrences")

# 4. DURABILITY / MOISTURE RISK MASKING
print("\n--- CHECK 4: DURABILITY & MOISTURE RISK MASKING ---")
moisture_lines = []
for idx, line in enumerate(lines, 1):
    if re.search(r"fukt|levetid|skade|holdbarhet|gate|filtrer", line, re.IGNORECASE):
        moisture_lines.append((idx, line.strip()))

print(f"Lines discussing moisture/durability/technical risk gate: {len(moisture_lines)}")
for line_num, text in moisture_lines[:10]:
    print(f"  Line {line_num}: {text}")

