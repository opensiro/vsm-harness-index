#!/usr/bin/env python3
import csv
import subprocess
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
cat_path = repo / 'data' / 'catalog.psv'
sig_path = repo / 'data' / 'signatures.psv'

new_catalog = [
    dict(harness_id='vibe-kanban', project_name='Vibe Kanban', repository='https://github.com/BloopAI/vibe-kanban', repository_created_at='2025-06-14T19:10:21Z', source_membership='index-addition', review_ref='735654971bd396aa97b65166955678e4c34f8bf8', pinned_at='2026-09-16'),
    dict(harness_id='eigent', project_name='Eigent', repository='https://github.com/eigent-ai/eigent', repository_created_at='2025-07-29T15:56:02Z', source_membership='index-addition', review_ref='6c49956b2aa878c08bee5edcf8a1eb63122c2cd9', pinned_at='2026-09-16'),
    dict(harness_id='jcode', project_name='jcode', repository='https://github.com/1jehuang/jcode', repository_created_at='2026-01-05T09:43:36Z', source_membership='index-addition', review_ref='5f33d6239b56b3d381d6b2c0e9b151eef0b54cbe', pinned_at='2026-09-16'),
    dict(harness_id='reasonix', project_name='Reasonix', repository='https://github.com/esengine/DeepSeek-Reasonix', repository_created_at='2026-04-21T08:27:02Z', source_membership='index-addition', review_ref='ce278545461225dfd4c77840ad2a756bfb2095b9', pinned_at='2026-09-16'),
    dict(harness_id='omnigent', project_name='Omnigent', repository='https://github.com/omnigent-ai/omnigent', repository_created_at='2026-06-11T12:18:13Z', source_membership='index-addition', review_ref='4d963a360e798f076d4fdbd4665e7188e4da05df', pinned_at='2026-09-16'),
]
new_signatures = {
    'omnigent': 'Polly autonomously coordinates dependency-aware isolated workers, regulates the live team, and routes a separate cross-vendor review into corrective fix tasks, establishing agent-owned S2, S3 and S3* without S4/S5 closure.',
    'vibe-kanban': 'Autonomous coding agents run under workspace-global concurrency exclusion that prevents conflicting simultaneous workspace mutation as constructor-owned S2; lifecycle and human PR review do not establish S3, S3* or S5.',
    'eigent': 'A model-driven workforce uses dependency-gated task publication and coordinator-owned assignment/replanning to close autonomous S2 and S3 across autonomous workers; ordinary human controls do not create S5.',
    'reasonix': 'The autonomous coding engine serializes overlapping subagent write claims as constructor-owned S2, while planner/executor composition, permissions, checkpoints and review labels do not establish S3-S5.',
    'jcode': 'A shared live swarm plan closes autonomous dependency coordination and coordinator-owned assignment/reclamation as S2 and S3; ambient proactive work and experiential memory remain operational rather than S4.',
}

with cat_path.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f, delimiter='|'))
existing = {r['harness_id'] for r in rows}
for r in new_catalog:
    if r['harness_id'] not in existing:
        rows.append({'catalog_position':'0', **r})
rows.sort(key=lambda r: (r['repository_created_at'], r['harness_id']))
for i, r in enumerate(rows, 1):
    r['catalog_position'] = str(i)
fields = ['catalog_position','harness_id','project_name','repository','repository_created_at','source_membership','review_ref','pinned_at']
with cat_path.open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='|', lineterminator='\n')
    w.writeheader(); w.writerows(rows)

with sig_path.open(encoding='utf-8', newline='') as f:
    sig_rows = list(csv.DictReader(f, delimiter='|'))
sigs = {r['harness_id']: r['signature'] for r in sig_rows}
sigs.update(new_signatures)
pos = {r['harness_id']: int(r['catalog_position']) for r in rows}
out = [(pos[h], h, s) for h, s in sigs.items() if h in pos]
out.sort()
with sig_path.open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter='|', lineterminator='\n')
    w.writerow(['catalog_position','harness_id','signature'])
    for p,h,s in out: w.writerow([p,h,s])

subprocess.run(['python','scripts/render_tldr.py'], cwd=repo, check=True)
subprocess.run(['python','scripts/check_index.py'], cwd=repo, check=True)
