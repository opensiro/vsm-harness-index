import pathlib,tempfile,shutil,subprocess,os,json,urllib.request
import argparse
parser=argparse.ArgumentParser(description='No-model frozen anima_sdk shell smoke fixtures')
parser.add_argument('source',type=pathlib.Path)
src=parser.parse_args().source.resolve()
out=[]
scripts=list(src.glob('*.sh'))+list((src/'harnesses').glob('*.sh'))
for f in scripts:
 r=subprocess.run(['bash','-n',str(f)],capture_output=True,text=True)
 assert r.returncode==0,(str(f),r.stderr)
out.append({'bash_syntax_files':len(scripts),'exit':0})
tree=json.load(urllib.request.urlopen('https://api.github.com/repos/Rai220/anima_sdk/git/trees/b6451ef44d2f97959fe7bfaab32c27907c9ddd77?recursive=1',timeout=15))
modes={x['path']:x['mode'] for x in tree['tree']}
def setup(d):
 for n in ['run.sh','loop.sh','meta_loop.sh','AGENTS.md','MAIN_GOAL.md']:
  shutil.copy2(src/n,d/n)
 shutil.copytree(src/'harnesses',d/'harnesses')
 for f in list(d.glob('*.sh'))+list((d/'harnesses').glob('*.sh')):
  os.chmod(f,0o755 if modes[str(f.relative_to(d))]=='100755' else 0o644)
def env():
 e=os.environ.copy()
 for k in list(e):
  if k.startswith('ANIMA_'):e.pop(k)
 return e
with tempfile.TemporaryDirectory(prefix='anima-static-smoke-') as t:
 d=pathlib.Path(t);setup(d);e=env();e['ANIMA_HARNESS_CMD']='printf "mock-step\\n" >> "$ANIMA_TASK_DIR/steps.log"; printf "done\\n" > "$ANIMA_TASK_DIR/STOP"'
 r=subprocess.run(['bash','loop.sh'],cwd=d,env=e,capture_output=True,text=True,timeout=10)
 assert r.returncode==0,r.stderr
 assert (d/'steps.log').read_text().splitlines()==['mock-step']
 out.append({'loop_fixture':'one custom stub step then STOP','exit':r.returncode})
with tempfile.TemporaryDirectory(prefix='anima-meta-smoke-') as t:
 d=pathlib.Path(t);setup(d);e=env();e['ANIMA_HARNESS_CMD']='if [[ "$ANIMA_TASK_DIR" == */generation_1 ]]; then printf "\\nmock-marker\\n" >> "$ANIMA_TASK_DIR/AGENTS.md"; printf "local changed goal\\n" > "$ANIMA_TASK_DIR/MAIN_GOAL.md"; printf "done\\n" > "$ANIMA_TASK_DIR/STOP"; else exit 23; fi'
 r=subprocess.run(['bash','meta_loop.sh'],cwd=d,env=e,capture_output=True,text=True,timeout=10)
 assert r.returncode==23,(r.returncode,r.stdout,r.stderr)
 assert (d/'generation_1/STOP').is_file() and (d/'generation_2').is_dir()
 assert 'mock-marker' in (d/'generation_2/AGENTS.md').read_text()
 assert (d/'generation_2/MAIN_GOAL.md').read_text()==(src/'MAIN_GOAL.md').read_text()
 assert not (d/'generation_2/STOP').exists()
 assert (d/'generation_2/INBOX.md').read_text()==''
 out.append({'meta_fixture':'STOP creates generation_2; modified agent instructions persist; goal restored from root; deliberate stub exit 23 stops loop','exit':r.returncode,'expected_exit':23})
print(json.dumps(out))
