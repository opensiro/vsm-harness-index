from pathlib import Path

path = Path('experiments/functional-capability-depth/system-observations/render_registry.py')
text = path.read_text(encoding='utf-8')
old = '_escape_md(row.benchmark_labels),'
assert old in text
text = text.replace(old, '_escape_md(row.evidence_surfaces),', 1)
path.write_text(text, encoding='utf-8')
