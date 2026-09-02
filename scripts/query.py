#!/usr/bin/env python3
"""Filter and rank library ideas. Reads the live IC library when present, else the skill's snapshot.
Usage: query.py [--page pdp,cart] [--lever trust,friction,motivation,clarity] [--industry consumables,high_consideration]
                [--min-grade B] [--effort low,medium] [--exclude IC-001,IC-002] [--metric cvr,rpv] [--top 25] [--json]"""
import json,os,argparse,sys
LIVE=os.path.expanduser("~/Claude/resources/experiment-library/ideas.json"); SNAP=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"library","library.json")
LEVER={"risk_reduction":"trust","social_information":"trust","effort_reduction":"friction","search_cost_reduction":"friction","perceived_value":"motivation","price_clarity":"motivation","urgency":"motivation","loss_aversion":"motivation","relevance":"motivation","commitment":"motivation","product_comprehension":"clarity","uncertainty_reduction":"clarity","comparison_support":"clarity","decision_salience":"clarity","attention_focus":"clarity","progress":"clarity"}
GRADE={"A+":5,"A":4,"B":3,"C":2,None:1,"D":0}
a=argparse.ArgumentParser(); [a.add_argument(f"--{k.replace('_','-')}",dest=k) for k in ("page","lever","industry","min_grade","effort","exclude","metric","top","source")]; a.add_argument("--json",action="store_true"); o=a.parse_args()
src=o.source or (LIVE if os.path.exists(LIVE) else SNAP)
d=json.load(open(src)); ideas=d["ideas"] if isinstance(d,dict) else d
ideas=[i for i in ideas if i.get("scope")!="info_product" and i.get("evidence_grade")!="D"]
L=lambda s:[x.strip() for x in s.split(",")] if s else None
page,lever,ind,eff,exc,met=L(o.page),L(o.lever),L(o.industry),L(o.effort),set(L(o.exclude) or []),L(o.metric)
def keep(i):
    if i["id"] in exc: return False
    if page and not any(p in i["page_type"] for p in page): return False
    if lever and LEVER.get((i.get("mechanism") or [""])[0],"clarity") not in lever: return False
    if ind and not (set(i.get("industry_fit") or [])&set(ind) or "all_d2c" in (i.get("industry_fit") or [])): return False
    if eff and i.get("effort") not in eff: return False
    if met and i.get("primary_metric") not in met: return False
    if o.min_grade and GRADE.get(i.get("evidence_grade"),1)<GRADE[o.min_grade]: return False
    return True
res=sorted([i for i in ideas if keep(i)],key=lambda i:-(i.get("priority") or 0))[:int(o.top or 25)]
if o.json: print(json.dumps(res,indent=1)); sys.exit()
print(f"source: {os.path.basename(os.path.dirname(src))}/{os.path.basename(src)}  |  {len(res)} ideas\n")
for i in res:
    print(f'{i["id"]} [{i.get("evidence_grade") or "–"}] {i["title"]}  |  {"/".join(i["page_type"])}  |  {LEVER.get((i.get("mechanism") or [""])[0],"clarity")}  |  effort {i.get("effort")}  |  {i.get("total_wins",i.get("wins",0))}W/{i.get("total_losses",i.get("losses",0))}L  |  metric {i.get("primary_metric")}')
    print(f'   {i.get("plain_english") or ""}\n   run when: {i.get("ideation_hint") or i.get("run_when") or ""}\n')
