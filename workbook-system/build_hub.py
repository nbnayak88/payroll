from pathlib import Path
import base64,json
ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent
catalog=json.loads((OUT/'payroll-catalog.json').read_text())
resources=catalog['resources']
assert len({r['id'] for r in resources})==len(resources)
assert len({r['url'] for r in resources})==len(resources)
font=base64.b64encode((ROOT/'comfortaa.woff').read_bytes()).decode()
logo=base64.b64encode((ROOT/'successlabs-academy-logo.png').read_bytes()).decode()
html=(ROOT/'hub-template.html').read_text().replace('__FONT__',font).replace('__LOGO__',logo)
(OUT/'index.html').write_text(html)
print(f"Hub generated: {len(resources)} resources, {len({r['country'] for r in resources})} countries and regions")
