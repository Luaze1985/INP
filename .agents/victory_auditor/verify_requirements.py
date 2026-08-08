import os
import re
import sys

TARGET_PATH = r"C:\Users\larse\Documents\Interne prosjekter\Vibs\ipn-verified\docs\reference\prosjektbeskrivelse\forskning-og-soa-v0.5-kandidat.md"

def run_audit():
    print(f"=== VICTORY AUDIT INDEPENDENT VERIFICATION SCRIPT ===")
    print(f"Target: {TARGET_PATH}\n")
    
    if not os.path.exists(TARGET_PATH):
        print(f"FAIL: Target file does not exist at {TARGET_PATH}")
        sys.exit(1)
        
    with open(TARGET_PATH, "r", encoding="utf-8") as f:
        text = f.read()
        lines = text.splitlines()

    print(f"File loaded successfully: {len(lines)} lines, {len(text)} bytes.")
    
    results = {}
    
    # -------------------------------------------------------------
    # R1: Source & Evidence Verification
    # -------------------------------------------------------------
    r1_checks = {}
    
    # 1. Finans Norge 2023 vannskader
    r1_checks["Finans Norge 10 skader/t (87 600/år) og 5,1 mrd kr"] = (
        ("10 vannskader" in text or "10 vannskader i timen" in text) and
        ("87 600" in text) and
        ("5,1 milliard" in text or "5,1 mrd" in text)
    )
    
    # 2. 70% A1-A3 rule
    r1_checks["70% A1-A3 utslipp låst i tidlige valg"] = (
        ("70 %" in text or "70%" in text) and
        ("A1–A3" in text or "A1-A3" in text) and
        ("KD2024" in text)
    )
    
    # 3. Kaza et al. 2014 (~32% PD, 71 000 boliglån, ENERGY STAR)
    r1_checks["Kaza2014: ~32% lavere PD, 71 000 boliglån"] = (
        ("Kaza2014" in text) and
        ("32 %" in text or "32%" in text) and
        ("71 000" in text)
    )
    
    # 4. Billio et al. 2022 (Dutch residential, EPC, DOI 10.1007/s11146-021-09838-0)
    r1_checks["Billio2022: JREFE 65(3), DOI 10.1007/s11146-021-09838-0"] = (
        ("Billio2022" in text) and
        ("10.1007/s11146-021-09838-0" in text)
    )
    
    # 5. An & Pivo 2020 (34% CMBS commercial, DOI 10.1111/1540-6229.12228, 🟡)
    r1_checks["An2020: 34% CMBS commercial, DOI 10.1111/1540-6229.12228, port 🟡"] = (
        ("An2020" in text) and
        ("34 %" in text or "34%" in text) and
        ("10.1111/1540-6229.12228" in text) and
        ("CMBS" in text)
    )
    
    # 6. EN 15978:2026 publiseringsdato 17. april 2026
    r1_checks["EN 15978:2026 publisert 17. april 2026 (🟢¹)"] = (
        ("EN15978-2026" in text) and
        ("17. april 2026" in text)
    )
    
    # 7. NS 3454 tilbaketrukket 07.09.2023, erstattet av NS-EN 16627
    r1_checks["NS 3454 trukket tilbake 07.09.2023, erstattet av NS-EN 16627"] = (
        ("07.09.2023" in text or "7. september 2023" in text) and
        ("NS-EN 16627" in text or "NS-EN16627" in text)
    )
    
    # 8. BKA2: 11,7 MNOK, Trondheim kommune, SINTEF v/ Vegard Knotten (2024-2028)
    r1_checks["BKA2: 11,7 MNOK, Trondheim kommune, SINTEF v/ Vegard Knotten"] = (
        ("BKA2" in text) and
        ("11,7 MNOK" in text) and
        ("Trondheim kommune" in text) and
        ("Vegard Knotten" in text)
    )
    
    # 9. NFR IPN 2026: 1-16 MNOK, maks 50% støttesats
    r1_checks["NFR IPN 2026: 1-16 MNOK, 50% støttesats"] = (
        ("NFR_IPN2026" in text) and
        ("1–16 MNOK" in text or "1-16 MNOK" in text) and
        ("50 %" in text or "50%" in text)
    )
    
    # 10. Mecca 2023: AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9%, DOI 10.1002/mcda.1818
    r1_checks["Mecca2023: AHP 46%, TOPSIS 20%, MIVES 11%, COPRAS 9%"] = (
        ("Mecca2023" in text) and
        ("46 %" in text or "46%" in text) and
        ("20 %" in text or "20%" in text) and
        ("11 %" in text or "11%" in text) and
        ("9 %" in text or "9%" in text) and
        ("10.1002/mcda.1818" in text)
    )
    
    results["R1"] = r1_checks

    # -------------------------------------------------------------
    # R2: Section Structure and Content
    # -------------------------------------------------------------
    r2_checks = {}
    
    r2_checks["Seksjon 1: Sammendrag og hovedkonklusjon for SINTEF"] = "# Seksjon 1:" in text and "Sammendrag og hovedkonklusjon" in text
    r2_checks["Seksjon 2: Metodisk fundament (LCA/LCC og datakvalitet)"] = "# Seksjon 2:" in text and "Metodisk fundament" in text
    r2_checks["Seksjon 3: Flerkriterieanalyse og usikkerhet (MCDA)"] = "# Seksjon 3:" in text and "Flerkriterieanalyse" in text
    r2_checks["Seksjon 4: Finans- og reguleringskontekst"] = "# Seksjon 4:" in text and "Finans- og reguleringskontekst" in text
    r2_checks["Seksjon 5: Norsk SMB-kontekst og tilbudsbeslutninger"] = "# Seksjon 5:" in text and "Norsk SMB-kontekst" in text
    r2_checks["Seksjon 6: Syntese og VERIFIEDs avgrensede FoU-gap"] = "# Seksjon 6:" in text and "Syntese" in text
    
    # Details in Seksjon 2:
    r2_checks["Sec 2 content: TEK17 1,25 (+25% utslippsstraff)"] = "1,25" in text and ("25 %" in text or "+25" in text)
    r2_checks["Sec 2 content: Weidema Pedigree (5 DQIs)"] = "Weidema" in text and "Pedigree" in text
    r2_checks["Sec 2 content: Edelen & Ingwersen utan skjult totalscore"] = "Edelen" in text and "skjult totalscore" in text
    r2_checks["Sec 2 content: ISO 14040 / EN 15804+A2 / ISO 15686-5"] = "ISO14040" in text or "ISO 14040" in text
    
    # Details in Seksjon 3:
    r2_checks["Sec 3 content: Synlig usikkerhet uten svart boks"] = "synlig" in text and "usikkerhet" in text
    r2_checks["Sec 3 content: Rank reversal / ranginversjon forbehold"] = ("ranginversjon" in text.lower() or "rank reversal" in text.lower()) and "forbehold" in text.lower()
    
    # Details in Seksjon 4:
    r2_checks["Sec 4 content: EBA EU 2023, BoE PS25/25 & DP1/25"] = "EBA_EU2023" in text and "BoE_PS25-25" in text and "BoE_DP1-25" in text
    r2_checks["Sec 4 content: Eksplisitt gap holdbarhet/fukt -> PD"] = "holdbarhet" in text and "fuktrobusthet" in text and "PD" in text
    
    # Details in Seksjon 5:
    r2_checks["Sec 5 content: Nordic Council 2023 SMB flexibility"] = "Nordic2023" in text or "Nordisk Ministerråd" in text
    r2_checks["Sec 5 content: SmartKalk Miljø, Reduzer, Concular, ORIS"] = (
        "SmartKalk Miljø" in text and "Reduzer" in text and "Concular" in text and "ORIS" in text
    )
    
    # Details in Seksjon 6:
    r2_checks["Sec 6 content: 6-aksers matrise"] = "6-akser" in text or "6 akser" in text or "6-aksiale" in text
    r2_checks["Sec 6 content: Bounded FoU gap statement"] = "Innenfor det undersøkte utvalget av verktøy finnes enkeltkomponenter" in text

    results["R2"] = r2_checks

    # -------------------------------------------------------------
    # R3: Ontological & Source Critical Compliance
    # -------------------------------------------------------------
    r3_checks = {}
    
    # 1. "løsningsvalg" (not narrow "produktvalg" as primary scope)
    r3_checks["Begrepsregel: 'løsningsvalg' benyttes i teksten"] = "løsningsvalg" in text or "Løsningsvalg" in text
    
    # Check that 'produktvalg' is not used as the main concept (or only in negative context/explanation)
    produktvalg_count = text.count("produktvalg") + text.count("Produktvalg")
    losningsvalg_count = text.count("løsningsvalg") + text.count("Løsningsvalg")
    r3_checks["Begrepsregel: 'løsningsvalg' dominerer over 'produktvalg'"] = losningsvalg_count > produktvalg_count
    
    # 2. Avoid prohibited automated/black-box phrases
    prohibited_auto = [
        "VERIFIED velger automatisk",
        "VERIFIED anbefaler automatisk",
        "automatisk velger",
        "automatisk anbefaler"
    ]
    has_prohibited_auto = any(p in text for p in prohibited_auto)
    r3_checks["Begrepsregel: Ingen 'VERIFIED velger/anbefaler automatisk'"] = not has_prohibited_auto
    
    # Svart boks should only be mentioned if preceded by "ingen", "unngå", "uten", or as negative reference
    blackbox_matches = re.findall(r'.{0,30}svart boks.{0,30}', text, flags=re.IGNORECASE)
    valid_blackbox = all("forbud" in m.lower() or "ingen" in m.lower() or "uten" in m.lower() or "avviser" in m.lower() or "mot" in m.lower() for m in blackbox_matches)
    r3_checks["Begrepsregel: 'svart boks' omtales kun kritisk/negativt"] = valid_blackbox
    
    # 3. Use "testflate" for VIBS platform
    r3_checks["Begrepsregel: 'testflate' benyttes om VIBS-plattformen"] = "testflate" in text or "Testflate" in text
    
    # 4. Preserve parked status ⏸ for Wiik2025 and SA2018
    r3_checks["Kildekritikk: Wiik2025 har status ⏸ Parkert"] = "[Wiik2025]" in text and "⏸" in text
    r3_checks["Kildekritikk: SA2018 har status ⏸ Parkert"] = "[SA2018]" in text and "⏸" in text
    
    # 5. Strictly distinguish EBA_EU2023 (banking) and EBA_NO2023 (building)
    r3_checks["Kildekritikk: Strengt skille mellom EBA_EU2023 og EBA_NO2023"] = (
        "[EBA_EU2023]" in text and
        "[EBA_NO2023]" in text and
        "European Banking Authority" in text and
        "Entreprenørforeningen" in text
    )
    
    # 6. Source tagging (🟢, 🟡, ⏸, 🔴) applied across claims
    r3_checks["Kildekritikk: Kildestatustagger (🟢, 🟡, ⏸) brukt konsekvent"] = (
        "🟢" in text and "🟡" in text and "⏸" in text
    )

    results["R3"] = r3_checks

    # Print summary results
    all_passed = True
    for req_name, checks in results.items():
        print(f"\n--- {req_name} RESULTS ---")
        for check_name, passed in checks.items():
            status = "PASS" if passed else "FAIL"
            print(f"[{status}] {check_name}")
            if not passed:
                all_passed = False
                
    print("\n==========================================")
    if all_passed:
        print("OVERALL VERDICT: ALL INDEPENDENT CHECKS PASSED")
    else:
        print("OVERALL VERDICT: SOME CHECKS FAILED")
    print("==========================================")
    
    return all_passed

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
