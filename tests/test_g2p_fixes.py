"""g2p fixes made in this fork. Run: python tests/test_g2p_fixes.py"""
import tltk

CASES = {
    # สระ "vowel" before a vowel name (issue attapol/tltk#11)
    "สระอา": "sa1'ra1~?aa0",
    "สระอี": "sa1'ra1~?ii0",
    "สระเอือ": "sa1'ra1~?UUa0",
    "สระอัวะ": "sa1'ra1~?ua1",
    "สระอัว": "sa1'ra1~?uua0",
    "สระไอไม้มลาย": "sa1'ra1~?aj0~maaj3~ma3'laaj0",
    "สระอีกับสระอา": "sa1'ra1~?ii0~kap1~sa1'ra1~?aa0",
    "ลงท้ายด้วยสระอี": "loN0~thaaj3~duuaj2~sa1'ra1~?ii0",
    "สระเสียงยาว": "sa1'ra1~siiaN4~jaaw0",
    "เสียงสระ": "siiaN4~sa1'ra1",
    "สระบุรี": "sa1'ra1~bu1~rii0",
    # สระ "pond", "wash", and words that only start like a vowel name
    "ขุดสระอยู่": "khut1~sa1~juu1",
    "สระน้ำ": "sa1~naam3",
    "สระผม": "sa1~phom4",
    "สระออก": "sa1~?OOk1",
    "สระอำเภอ": "sa1~?am0~ph@@0",
    "สระอากาศ": "sa1~?aa0~kaat1",
    # misreadings (issue attapol/tltk#12)
    "สิบเอ็ด": "sip1~?et1",
    "ยี่สิบเอ็ด": "jii2~sip1~?et1",
    "สิบเอ็ดโมง": "sip1~?et1~mooN0",
    "สารเลว": "saan4~leew0",
    "ชานมเย็น": "chaa0~nom0~jen0",
    "ผมชอบชานมเย็นมาก": "phom4~chOOp2~chaa0~nom0~jen0~maak2",
    "บุรุษ": "bu1~rut1",
    "สุภาพบุรุษ": "su1~phaap2~bu1~rut1",
    "บรรพบุรุษ": "ban0'pha3~bu1~rut1",
    "แอปเปิล": "?xxp1~p@@n2",
    "วอลเลย์บอล": "wOOn0~lee2~bOOn0",
    # unchanged
    "ผลไม้": "phon4'la3~maaj3",
    "เด็กๆ": "dek1|dek1",
}

bad = 0
for word, want in CASES.items():
    got = tltk.nlp.g2p(word).split("<tr/>", 1)[1].split("|<s/>")[0]
    if got != want:
        bad += 1
        print(f"FAIL {word}: {got} (want {want})")
print(f"{len(CASES) - bad}/{len(CASES)} ok")
raise SystemExit(bad > 0)
