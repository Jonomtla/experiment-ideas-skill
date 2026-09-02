#!/usr/bin/env python3
"""Build the shareable library snapshot inside the skill folder.
Strips everything that is client-confidential or licensed to IC internal use:
client_notes, external_refs, design references, and every GoodUI evidence row.
Keeps: idea fields, grades, win/loss counts, public case-study evidence (CRE, Blend, Conversion, SplitBase, MECLABS, Optimizely, Evidoo free tier)."""
import json,os,datetime
SRC=os.path.expanduser("~/Claude/resources/experiment-library"); HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ideas=json.load(open(f"{SRC}/ideas.json"))["ideas"]; ev=json.load(open(f"{SRC}/evidence.json"))["evidence"]; tax=json.load(open(f"{SRC}/taxonomy.json"))
KEEP=("id","slug","title","scope","page_type","device","change_type","mechanism","fogg_axis","law_ref","primary_metric","hypothesis","run_when","do_not_run_when","evidence_grade","wins","losses","inconclusive","external_evidence_count","total_wins","total_losses","median_win_lift_pct","effort","risk","industry_fit","priority","plain_english","ideation_hint")
out=[{k:i.get(k) for k in KEEP} for i in ideas if i.get("scope")!="info_product"]
PUBLIC={"SRC-CRE","SRC-BLEND","SRC-CONVERSION","SRC-SPLITBASE","SRC-MECLABS","SRC-OPTIMIZELY","SRC-EVIDOO-FREE","SRC-CHATGPT-DR"}
pev=[{k:e.get(k) for k in ("idea_id","source_id","brand","industry","url","variant","metric_label","lift_pct","lift_note","confidence_pct","sample","device","verdict","analysis","context")} for e in ev if e.get("source_id") in PUBLIC]
json.dump({"_meta":{"built":str(datetime.date.today()),"ideas":len(out),"evidence":len(pev),"note":"Shareable snapshot. IC client detail and GoodUI member data removed. Third-party results are benchmarks from public case studies, not the library owner's own results."},"taxonomy":tax,"ideas":out,"evidence":pev},open(f"{HERE}/library/library.json","w"),indent=1,ensure_ascii=False)
print("snapshot:",len(out),"ideas",len(pev),"public evidence rows")
