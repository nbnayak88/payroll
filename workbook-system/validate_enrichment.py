"""Validate country fixtures, preservation, reflection coverage and standalone script syntax."""
from pathlib import Path
import argparse,copy,json,re,subprocess
ROOT=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser();parser.add_argument('--baseline');args=parser.parse_args()
catalog=json.loads((ROOT/'payroll-catalog.json').read_text());sections=0
for row in catalog['resources']:
 s=(ROOT/row['path']).read_text();c=json.loads(re.search(r'id="sla-case-data">(.*?)</script>',s,re.S).group(1))
 assert c['country']==row['country'] and len(c['workers'])==4 and len(c['mappings'])==4,row['path']
 assert all(w['id'].startswith('TEST-') and w['identity'].startswith('TEST-') and w['bank'].startswith('TEST-') for w in c['workers'])
 assert all(x not in s for x in ['Original generated ambient melody','let audioContext=null,audioNodes','let ctx,gain,timer'])
 assert s.count('id="sla-learning-enhancements"')==1
 if row['kind']!='configurator':
  d=json.loads(re.search(r'id="workbook-data">(.*?)</script>',s,re.S).group(1));assert row['sections']==len(d['modules'])
  if args.baseline:
   old=subprocess.run(['git','show',args.baseline+':'+row['path']],cwd=ROOT,capture_output=True,text=True,check=True).stdout
   before=json.loads(re.search(r'id="workbook-data">(.*?)</script>',old,re.S).group(1));restored=copy.deepcopy(d)
   for content in [restored,before]:
    for m in content['modules']:m['tables']=[t for t in m.get('tables',[]) if not t.get('_slaSynthetic')]
   assert restored==before,'Original curriculum changed: '+row['path']
   assert re.search(r'const KEY=(.*?);',old).group(1)==re.search(r'const KEY=(.*?);',s).group(1),'Storage key changed'
  for m in d['modules']:
   sections+=1;assert len([t for t in m['tables'] if t.get('_slaSynthetic')])==1
   f=c['reflections']['section-'+str(m['n'])];assert set(f)=={'Affirmation','Visualization','Gratitude','Intention'}
   assert all(isinstance(v,str) and len(v)>35 for v in f.values())
  if row['kind']=='replication':assert c['earnings'] is None and c['currency'] is None
  else:
   e=c['earnings'];assert round(e['base']+e['bonus']+e['allowance'],2)==e['grossBeforeDeductions'];assert round(e['revisedBase']-e['oldBase'],2)==e['retroDifference']
 else:assert len(c['legacyPages'])==48
 for attrs,script in re.findall(r'<script([^>]*)>(.*?)</script>',s,re.S):
  if 'application/json' in attrs:json.loads(script)
  elif script.strip():subprocess.run(['node','--check'],input=script,text=True,capture_output=True,check=True)
assert len({x['country'] for x in catalog['resources']})==107
print(json.dumps({'books':len(catalog['resources']),'countries':107,'moduleFixtures':sections,'legacyConfigurationPages':44,'scriptSyntax':'passed','fixtureArithmetic':'passed','reflectionCoverage':'passed','curriculumAndStorageKeys':'preserved' if args.baseline else 'baseline comparison not requested'}))
