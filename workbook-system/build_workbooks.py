from pathlib import Path
import base64, copy, hashlib, json, re, subprocess

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent
TEMPLATE=ROOT/'template.html'
GUIDE='https://help.sap.com/doc/b24aa110d63d4602830fc57424142556/2611/en-US/SF_ECPAY_CountrySpec.pdf'
DATE='8 November 2026'

MAIN={
 'Mexico':dict(currency='MXN',city='Mexico City',person='Elena Rivera',chapter='28',page=202,
   authority='SAT for salary withholding and payroll receipts; IMSS for employer affiliation and contribution administration',
   identity='Validate CURP, RFC and NSS independently against the relevant employee and employer records.',
   tax='Build an ISR withholding decision for the actual payment period using the operative SAT instructions. Numeric rates and subsidy eligibility must be evidenced before configuration.',
   social='Investigate the applicable IMSS contribution categories, insured salary basis, population and dated parameters; distinguish these from gross cash earnings.',
   filing='Trace salary withholding, the payroll CFDI receipt and employer affiliation changes as separate obligations.',
   focus='Trace a pay change through compensation replication, insured salary, salary withholding and the payroll receipt. Investigate a concurrent-employment design before enabling it.',
   localyear='Select the relevant calendar-year instructions and payment-period basis; retain separate effective dates for each obligation.',
   topics=['Personal data and identity mapping','Address and payment mapping','Generic contract and dependent replication','Concurrent employment design and irreversible-enablement review','Absence and personal-ID replication'],
   refs=[('sat-isr','SAT · salary withholding framework','https://wwwmat.sat.gob.mx/articulo/36534/articulo-96'),('sat-receipt','SAT · payroll receipt requirements','https://wwwmat.sat.gob.mx/consultas/97722/comprobante-de-nomina'),('imss','IMSS · employee affiliation and salary movements','https://www.imss.gob.mx/tramites/imss02009')]),
 'South Africa':dict(currency='ZAR',city='Johannesburg',person='Thandi Mokoena',chapter='43',page=293,
   authority='SARS for employer tax reporting and reconciliation; confirm the relevant contribution and labour authorities for the employer',
   identity='Validate the employee identity, income-tax reference and employer registration as separate records; use synthetic identifiers in this workbook.',
   tax='Separate PAYE calculation, tax-certificate source-code classification and any directive-controlled payment. Record the year of assessment and operative calculation instructions.',
   social='Assess UIF, SDL and ETI scope independently. Do not treat a contribution, levy or incentive as an interchangeable deduction.',
   filing='Reconcile monthly EMP201 declarations, payments and employee tax certificates through the EMP501 process using the applicable BRS.',
   focus='Trace a bonus through its replication, directive evidence, certificate classification and employer reconciliation. Diagnose a mismatch between declarations and certificates.',
   localyear='Record the SARS year of assessment and its March-to-February boundary, including the applicable 2026/2027 BRS version.',
   topics=['Personal and address data mapping','Payment and dependent replication','Additional-payment and tax-directive date mapping','Tax-certificate classification and BRS evidence'],
   refs=[('sars-reconciliation','SARS · employer reconciliation','https://www.sars.gov.za/types-of-tax/pay-as-you-earn/reconciliations/'),('sars-validation','SARS · 2027 reconciliation validation guidance','https://www.sars.gov.za/guide-for-validation-rules-applicable-to-reconciliation-declarations-2027/')]),
 'United Kingdom':dict(currency='GBP',city='Manchester',person='Jamie Morgan',chapter='53',page=349,
   authority='HMRC for PAYE, National Insurance and RTI; assess workplace-pension duties and scheme evidence separately',
   identity='Maintain the employee payroll identity, National Insurance information and starter evidence; check country-specific personal and payment fields in the SAP guide.',
   tax='Select the employee tax code, jurisdiction, basis and correct pay-period instructions. Verify each 2026/2027 parameter against current HMRC guidance rather than copying an annual slice into payroll.',
   social='Choose the evidenced National Insurance category and applicable worker treatment; distinguish employee and employer contributions and assess any director or special-category rules.',
   filing='Report employee payments and deductions using FPS, assess whether EPS is needed, and reconcile the employer account separately from bank settlement.',
   focus='Compare a regular employee, a director and a starter with incomplete evidence. Trace the resulting pay-period decisions through RTI, payment and Finance.',
   localyear='The 2026/2027 tax-year boundary starts on 6 April 2026. Preserve the separate pay-period and payment-date controls.',
   topics=['Personal, address and payment mapping','National-ID and starter evidence','Contract and dependent replication','Country payroll replication and statutory-data validation'],
   refs=[('hmrc-rates','HMRC · employer rates and thresholds 2026/2027','https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027'),('hmrc-fps','HMRC · reporting employee payments','https://www.gov.uk/running-payroll/reporting-to-hmrc'),('hmrc-eps','HMRC · employer payment summary','https://www.gov.uk/running-payroll/reporting-to-hmrc-eps')])
}

LABS=[
 'Write a scope brief for a fictional 120-person subsidiary and identify the decisions that need an owner.',
 'Propose a dated change and trace its impact into master data, calculation, reporting and regression tests.',
 'Arrange five sections into a dependency path and explain why each handoff matters.',
 'Compare two worker populations and record an assumption that changes the implementation scope.',
 'Map a fictional legal employer to its accounting owner, establishment and registration evidence.',
 'Build a classification decision tree and find two employees whose insurance and pay-frequency groups differ.',
 'Place a hire, transfer and late termination on a timeline; explain each affected target record.',
 'Create a synthetic identity record with one missing item and explain the controlled resolution.',
 'Predict the result of a future-dated address change; compare current and historical target records.',
 'Challenge a bank-account change with valid syntax and incomplete approval evidence.',
 'Separate employment, earning, payment and submission dates in one boundary scenario.',
 'Trace one recurring component and one bonus from EC into a proposed target record and downstream result.',
 'Compare a part-time schedule with a mid-period hire and explain the payable units.',
 'Split one absence into entitlement, funding and reporting decisions before calculating its effect.',
 'Design a sandbox check for a historical change during an area lock and record the safe recovery sequence.',
 'Build a calendar covering cutoff, calculation, approval, payment and recipient feedback.',
 'Specify a wage-type decision record with valuation, deduction, reporting and posting evidence.',
 'Reconcile a payment proposal to its control totals before release and to settlement afterwards.',
 'Choose an off-cycle scenario and document why it cannot be treated as an ordinary duplicate run.',
 'Record a fictional attachment order and identify the legal evidence needed before any deduction.',
 'Trace three payslip fields back to source data, calculated results and disclosure rules.',
 'Create an employment-income withholding decision using the linked authority source; keep missing numerical parameters pending.',
 'Compare gross earnings with a separately evidenced contribution base and test a category boundary.',
 'Map one reporting obligation from source data to submission, recipient feedback and reconciliation.',
 'Compare two potential pension or benefit populations; identify the enrolment and provider evidence required.',
 'Separate a cash allowance, reimbursement and non-cash benefit before choosing their payroll treatment.',
 'Trace an absence from first record through employer liability and any external reimbursement.',
 'Create a dated minimum-pay or agreement record and identify what would prove its actual worker scope.',
 'Test two competing deduction instructions and record the authority for any priority or protection rule.',
 'Explain a calculation sequence and show how changing the order can change its result.',
 'Trace a retroactive change while preserving the earlier rule version and original result evidence.',
 'Reconcile the closing period and identify which year-end opening conditions need separate approval.',
 'Read an authority update and separate its publication, effective date and implementation decision.',
 'Introduce a missing mandatory field into a synthetic EC record and define a targeted correction.',
 'Investigate a bank acknowledgement with unknown settlement before authorising any replacement payment.',
 'Design a balancing check from payroll liabilities to Finance posting and an exception owner.',
 'Trace one replicated employee through trigger, target record, acknowledgement and safe retry.',
 'Choose an integration extension and define authentication, validation, retry and ownership boundaries.',
 'Write one normal, one boundary and one negative test with independent expected results.',
 'Prepare a cutover rehearsal with reconciled counts, retained history and a measurable go/no-go gate.',
 'Teach one decision to a peer in five minutes and use their questions to improve the explanation.',
 'Classify three hypercare incidents and separate data correction from configuration and recipient issues.',
 'Draw the complete source-to-recipient path and identify evidence at every handoff.',
 'Choose two failure modes and assign preventive, detective and recovery controls with owners.',
 'Create a parameter register entry with source, scope, valid-from date, rounding and boundary evidence.',
 'Separate tax, insurance, immigration and reporting questions for a fictional cross-border assignment.',
 'Review notes and backups for personal data and replace every real identifier with synthetic evidence.',
 'Prepare a next-year release brief with confirmed changes, pending questions and first-run reconciliation.'
]

APPENDIX=[
 ('Guide boundary & learning case','Setup','Establish what the cited appendix entry actually documents.','A documented replication entry is an evidence starting point; it does not establish a complete statutory payroll service.',['Open the pinned country entry.','Record its documented data topics.','Separate delivered mapping evidence from employer-specific decisions.','Set a synthetic employee and test objective.'],'Write a country scope statement that a new learner can use without assuming tax rates or production readiness.'),
 ('Version & landscape record','Setup','Connect the document edition to an actual implementation landscape.','A mapping decision must be reproducible against a known product and tenant version.',['Record the SAP guide edition and section.','Identify the actual ECP basis and release.','Record legal entity, country and replication route.','Assign a reviewer and a next review date.'],'Compare the same mapping decision across two imagined releases and identify what needs revalidation.'),
 ('Synthetic employee contract','Foundation','Define the minimum source record for one safe experiment.','Reliable identity and effective dates make it possible to diagnose a mapping failure without exposing personal data.',['Create a fictional employee ID.','Choose a legal entity and country.','Separate mandatory business data from optional examples.','Record consent and privacy assumptions for real implementations.'],'Create a positive and negative source record; explain why neither should contain a real national ID or bank account.'),
 ('Address model exploration','Foundation','Inspect the country-specific address model referenced by SAP.','A familiar address label can map differently across country models.',['Follow the address topic linked from the country entry.','Inspect source labels and target technical fields.','Record optionality, length and any value mapping from the guide.','Keep the original rule reference beside your proposed decision.'],'Choose two technical fields listed in the guide and predict a valid, missing and over-length input for each.'),
 ('Field mapping decision sheet','Configuration','Turn a documented field into a traceable mapping decision.','A target value is only useful when its source, transformation and meaning are known.',['Record the precise source field.','Confirm the target infotype and technical field in the document.','Describe the transformation in your own words.','Capture a synthetic source/target comparison.'],'Complete one mapping row from the guide, then ask a peer to reconstruct the expected output from your explanation.'),
 ('Codes & regional values','Configuration','Validate code values independently from their displayed labels.','A meaningful label can still carry a code that the receiving system cannot accept.',['Identify every coded field actually used.','Check the documented value-mapping requirement.','Separate country and region codes from display names.','Test an unmapped code and define who corrects it.'],'Design a case in which a readable region label has an invalid target code; document the observable failure and repair.'),
 ('Effective dates & changes','Configuration','Preserve history while changing employee address data.','A current address correction and a future move can require different target-record behaviour.',['Record source valid-from dates.','Distinguish correction, insertion and future change.','Predict the target time slices.','Reconcile the actual result without deleting historical evidence.'],'Compare a future-dated move and a historical correction for the same synthetic employee.'),
 ('Validation & negative cases','Configuration','Convert source constraints into explicit tests.','A positive example alone cannot show whether a boundary or omission is controlled.',['Select an actual documented constraint.','Define valid and invalid inputs.','Write expected behaviour before testing.','Keep document requirements separate from organisation-specific controls.'],'Create a missing-value, length-boundary and invalid-code case, recording whether each constraint comes from SAP or your design.'),
 ('Replication & recovery','Integration','Trace one record through replication and a controlled retry.','A retry should repair a failed handoff without silently duplicating or overwriting valid records.',['Record the actual delivered replication route.','Trace source identity, dates and target record.','Capture an error and its acknowledgement state.','Reconcile the target after a controlled replay.'],'Inject one mapping failure in a sandbox plan and demonstrate how you would prove that its retry did not create an unintended record.'),
 ('Reconciliation & evidence','Integration','Prove the source-to-target outcome using counts and selected field values.','A completed technical job does not by itself show that employee data arrived correctly.',['Compare source and target population counts.','Compare the selected documented fields.','Explain every exception.','Retain synthetic evidence with a named reviewer.'],'Build a reconciliation sheet for ten fictional employees and investigate one mismatch before accepting the handoff.'),
 ('Ownership, access & handover','Governance','Assign ownership and protect the evidence used in the learning experiment.','Useful learning evidence needs clear access, retention and incident responsibilities.',['Name the source, mapping and target owners.','Apply least-privilege evidence access.','Set retention and safe backup practices.','Give the next operator an actionable recovery note.'],'Write a handover note that another learner can follow without gaining access to real employee data.'),
 ('Next experiment & release review','Governance','Turn the completed experiment into a repeatable learning path.','A small tested result is a better baseline than an unchecked claim of full country readiness.',['Explain one finding and one unresolved question.','Compare the next document release with the pinned baseline.','Retest the changed mapping boundary.','Choose the next skill or country to explore.'],'Prepare a teach-back showing the document scope, one tested mapping decision and the next validation experiment.')
]

def table(title,heads,rows):return dict(title=title,heads=heads,rows=rows)
def source(ref,title,url):return dict(ref=ref,title=title,url=url)
def profile(name,info,appendix=False):
 return dict(name=name,currency=info.get('currency','units'),city=info.get('city','Learning sandbox'),person=info.get('person','Riley Example'),
  authority=info.get('authority','SAP country replication documentation; statutory authorities must be identified separately for a payroll implementation.'),
  identity=info.get('identity','Use a synthetic employee identity; confirm country-specific identifier requirements from the relevant official evidence.'),
  tax=[],taxnote=info.get('tax','This appendix replication workbook does not supply a statutory tax method. It focuses on documented data mapping and original learning experiments.'),
  social=[],socnote=info.get('social','Contribution eligibility, bases and rates are outside this appendix mapping scope and remain a separately evidenced implementation task.'),
  filing=info.get('filing','Employee-data replication and source-to-target reconciliation within the documented guide boundary.'),
  deadline='Maintain an owned operational calendar and verify the applicable recipient instructions before choosing any deadline.',reportnote=info.get('filing','Recipient acceptance and field reconciliation are separate from a successful technical transmission.'),
  pension='Confirm actual provider, population and enrolment duties through operative employer evidence; no unverified rate is activated here.',benefit='Separate cash, non-cash and reimbursement decisions using applicable employer evidence.',
  leave='Confirm entitlement, payer, duration, eligibility and reporting separately for each absence category.',minimum='Record the governing wage or agreement evidence, its worker scope and valid-from date before implementation.',
  yearend='Retain source and target history; reconcile the final affected period and open the next one with approved evidence.',
  change=info.get('focus',f"Explore SAP guide section {info.get('section','country chapter')} for {name}, then test one documented address-mapping decision with synthetic data."),
  focus=info.get('focus',f"Build a traceable {name} source-to-target address experiment and explain the boundary of the guide evidence."),
  refs=['sap-country'],statyear=info.get('localyear','This replication workbook does not define a country tax year; record dates relevant to the employee-data experiment.'),
  assignment='Assess employment, tax, insurance, immigration and data-transfer responsibilities separately; a mapping entry does not decide them.',
  future='Pin future work to the next confirmed guide release and current official instructions. Record uncertain or unpublished parameters as pending.',bands=None,
  themeName='Fresh learning gradient')

def shared_quiz(name,appendix=False,section=''):
 items=[
  (f'What is the evidence boundary for this {name} workbook?', ['A complete certified tax engine','The cited guide scope plus original learning and design exercises','A production approval','A substitute for tenant testing'],1,'Document scope, proposed decisions and observed test results are separate evidence categories.'),
  ('What should happen before a mapping is implemented?',['Copy a neighbouring country','Confirm the documented source, target and actual release','Mark every section complete','Remove the effective dates'],1,'A traceable mapping has a source, a target, a meaning and a release boundary.'),
  ('Which record is appropriate for a learning experiment?',['A real employee bank account','A downloaded production extract','A synthetic employee with controlled test values','An unmasked national ID'],2,'Synthetic records support exploration without exposing personal payroll data.'),
  ('A displayed region label looks correct. What is still needed?',['No further checks','The target code and value-mapping evidence','A payroll total','A screenshot of the logo'],1,'Labels and code values can differ; validate the actual receiving-system value.'),
  ('Which test gives useful boundary evidence?',['One successful sample only','A missing field, a length boundary and an invalid code with predicted results','Reading the table twice','Changing the source after seeing the result'],1,'Positive, boundary and negative cases expose different failure modes.'),
  ('A change has a future valid-from date. What should be checked?',['Only the newest display','The target time slices and retained historical record','Only the employee name','Whether the old evidence can be deleted'],1,'Effective dates and history are part of a reproducible source-to-target result.'),
  ('A technical job completed. What proves the handoff?',['The completion icon alone','Reconciled population, field values and explained exceptions','A renamed file','A saved bookmark'],1,'Execution status and business-data correctness are different checks.'),
  ('What should a retry demonstrate?',['That the button was clicked','That a valid target was not duplicated or overwritten unexpectedly','That all logs were removed','That dates were ignored'],1,'A controlled recovery reconciles the intended target state.'),
  ('How is an uncertain future parameter handled?',['Assume the old value','Keep it pending with an owner and evidence requirement','Average neighbouring rates','Choose the largest value'],1,'Unconfirmed values need an explicit evidence gate before activation.'),
  ('What is a useful learner completion record?',['A certificate proves production readiness','A reviewed section plus a clear decision and test evidence','A copied authority logo','A hidden error'],1,'Self-recorded progress supports learning; it is not a production certification.'),
  ('What belongs in a handover?',['An unexplained screenshot','Source scope, decision, synthetic evidence, owner and next action','A real password','Only the country name'],1,'Another operator should be able to reconstruct and continue the experiment safely.'),
  ('What is the strongest next step after a failed experiment?',['Erase the evidence','Explain the mismatch, revise the hypothesis and rerun a controlled case','Change every parameter','Declare the whole country unsupported'],1,'Curiosity is useful when a changed hypothesis leads to an observable, repeatable test.')]
 return [dict(q=q,options=o,answer=a,why=w) for q,o,a,w in items]

def cards(name,section):
 pairs=[('COUNTRY',name),('SCOPE','The precise boundary of the cited guide and the proposed learning experiment.'),('SOURCE','The originating employee-data record and its effective date.'),('TARGET','The receiving record and its documented business meaning.'),('INFOTYPE','A structured target record whose exact fields must be checked in the guide.'),('ADDRESS','Country-specific employee location data requiring explicit source-to-target decisions.'),('MAPPING','A documented decision connecting source, transformation and target.'),('CODE','A technical value that may differ from its displayed label.'),('REGION','A coded locality decision that needs country-specific evidence.'),('HISTORY','Earlier valid records retained for reproducible corrections.'),('CUTOFF','An owned operational boundary coordinated with source changes.'),('VALIDATION','A check with predicted valid and invalid behaviour.'),('BOUNDARY','A limit case that exposes a length, date or category condition.'),('RETRY','A controlled replay after the failed handoff is understood.'),('RECONCILE','Compare population and selected values; explain every exception.'),('EVIDENCE','A source, decision or observed result with a clear scope and date.'),('OWNER','The person accountable for the next decision or correction.'),('RELEASE','A version boundary that may require the mapping to be reviewed.'),('PRIVACY','Synthetic records and proportionate access keep payroll learning safe.'),('EXCEPTION','A mismatch requiring diagnosis and an owned resolution.'),('APPROVAL','A recorded decision appropriate to the actual implementation stage.'),('PARAMETER','A versioned input requiring operative evidence before activation.'),('BACKUP','A safe export of browser-local learning records.'),('QUESTION','A testable uncertainty that can guide the next experiment.'),('GUIDE',f'SAP 2H 2026, {section}; open the pinned source before using its field definitions.')]
 return [[a,b] for a,b in pairs]

def main_modules(base,p,info):
 mods=[]
 for original in base:
  m={k:copy.deepcopy(v) for k,v in original.items() if k not in ('tables','lab','sources')}
  n=m['n'];m['lab']=f"{LABS[n-1]} Use the {p['name']} case and synthetic employee {p['person']}; explain the evidence boundary."
  m['sources']=['sap-country'];m['evidence']=['Source or decision version and date recorded','Actual employee/employer scope stated','Independent expected result written','Synthetic test evidence retained when executed','Unresolved questions assigned to an owner']
  m['prerequisite']='Country scope, the relevant SAP guide topic and the preceding dependency';m['nextstep']='Explain the observed result, revise one assumption and choose the next experiment.'
  m['tables']=[table('Decision and evidence sheet',['Control','Case decision / evidence','Status'],[['Country / scenario',p['name']+' · '+p['person']+' (fictional)','Learning case'],['Implementation object','Record the actual source field, target or delivered configuration object for this section','Pending tenant evidence'],['Acceptance rule','Write an independently checkable expected result before executing the experiment','Proposed design'],['Owner / next action','Assign the reviewer, dated source and next validation step','Open']])]
  if n==1:m['tables']=[table('Workbook baseline',['Field','Learning baseline'],[['Country',p['name']],['Currency',p['currency']],['Company','OmniVerse Energy · '+p['name']+' learning subsidiary (fictional)'],['Employee',p['person']+' · '+p['city']+' (fictional)'],['Guide coverage','SAP 2H 2026 · chapter '+info['chapter']],['Review date',DATE],['Calculation parameters','Retrieve and approve current authority values separately; numerical rates are not preloaded'],['Production execution','No tenant run or statutory submission is represented as completed']])]
  if n in (8,9,12,14,37):m['tables'].append(table('SAP country topics to investigate',['Document topic','Learning action'],[[t,'Open the country chapter and map one synthetic employee example'] for t in info['topics']]))
  if n==22:
   m.update(what='Design the employment-income withholding process from operative evidence.',why='Employee scope, period, taxable basis and reporting must agree before a deduction is configured.',steps=['Confirm the employee and employer tax scope.','Identify the actual pay period, code or category and governing instructions.','Record approved numeric parameters and effective dates separately.','Reconcile a calculation and its reporting treatment against independent evidence.'])
   m['tables'].append(table('Country tax design focus',['Country instruction','Parameter gate'],[[p['taxnote'],'Current authority source, scope, dates and boundary tests required']]))
  if n==23:m['tables'].append(table('Contribution design focus',['Country instruction','Parameter gate'],[[p['socnote'],'Confirm categories and bases before numeric rates']]))
  if n==24:m['tables'].append(table('Recipient reconciliation',['Country focus','Evidence'],[[p['filing'],'Retain acknowledgement, accepted processing state and reconciled liability']]))
  if n in (2,32,33,45,48):m['tables'].append(table('Version and scope register',['Item','Decision'],[['Local period',p['statyear']],['Country focus',p['focus']],['Next-year evidence',p['future']],['Status','Learning design; no automatic legal feed or completed tenant validation']]))
  mods.append(m)
 return mods

def appendix_modules(p,info):
 mods=[]
 for n,(title,cat,what,why,steps,labtext) in enumerate(APPENDIX,1):
  rows=[['Country',p['name']],['Guide entry',info['section']+' · page '+str(info['page'])],['Source-to-target decision','Record the specific source field, target, optionality and transformation from the linked guide'],['Synthetic case',p['person']+' · employee DEMO-'+str(n).zfill(2)],['Evidence state','Proposed experiment; actual tenant outcome not yet recorded']]
  if n==1:rows.append(['Documentation scope','Appendix: Additional Replication Information. This is not a country statutory calculation specification.'])
  if n in (4,5,8):rows.append(['Target field codes found in the cited entry',', '.join(info['fieldCodes']) or 'Consult the exact country entry'])
  if n==6:rows.append(['Code-mapping decision','Verify whether the specific field needs delivered or customer-defined value mapping; do not infer it from its label'])
  mods.append(dict(n=n,title=title,cat=cat,what=what,why=why,steps=steps,tables=[table('Country experiment register',['Item','Decision / evidence'],rows)],lab=f"For {p['name']}: {labtext}",owner='Employee-data integration learning lead',evidence=['Pinned document section and page','Synthetic input and independently predicted result','Observed target result when actually tested','Explained exception and named owner','One question for the next experiment'],sources=['sap-country'],prerequisite='Pinned guide country entry and a synthetic employee record',nextstep='Explain the result to another learner and refine the next controlled experiment.'))
 return mods

APPENDIX_JS=r"""
function home(){return '<div class="toolbar"><button class="btn primary" data-go="1">Start a country experiment →</button><button class="btn" data-go="evidence">Open guide evidence</button><button class="btn" data-go="lab">Try the mapping lab</button></div><div class="notice"><strong>'+esc(P.name)+' · appendix replication practice</strong>'+M.length+' guided sections connect source data, mapping decisions, validation, reconciliation and handover. The SAP entry documents replication details; statutory tax and contribution calculations require separate evidence.</div><div class="card"><span class="status source">SAP 2H 2026 · '+esc(D.coverage.section)+'</span><h3 style="margin-top:12px">A small experiment. A traceable result.</h3><p>'+esc(P.focus)+'</p><a class="btn" target="_blank" rel="noopener noreferrer" href="'+esc(D.sources[0].url)+'">Read the country entry ↗</a></div><div class="sectiontitle"><h2>Replication learning path</h2></div><div class="sectiongrid">'+M.map(m=>'<button class="sectiontile" data-go="'+m.n+'"><span class="mono">'+String(m.n).padStart(2,'0')+' · '+esc(m.cat)+'</span><strong>'+esc(m.title)+'</strong><span>Predict · test · explain</span>'+(S.progress[m.n]?'<span class="done">✓</span>':'')+'</button>').join('')+'</div><div class="sectiontitle"><h2>Practice, play & reflect</h2></div><div class="tool-grid">'+tools.map(t=>'<button class="btn" data-go="'+t[0]+'"><span>'+icons[t[0]]+'</span><strong>'+t[1]+'</strong><p class="small muted">'+esc(t[2])+'</p></button>').join('')+'</div><div class="notice"><strong>Your learning workspace</strong>Notes, table edits and progress stay in this browser for '+esc(P.name)+'. Export a backup before changing devices. All employee examples are synthetic.</div>'}
function evidence(){return header('Guide evidence',P.name+' · documented replication scope','SAP 2H 2026, '+D.coverage.section+', country entry at page '+D.coverage.page+'.')+'<div class="notice"><strong>Keep the evidence boundary visible</strong>The source is an appendix replication entry. It supplies the country data topics to investigate; it does not prove a delivered statutory payroll localization, complete tax logic, production approval or an executed tenant test.</div><div class="card"><h3>Source register</h3>'+D.sources.map(s=>'<p><a href="'+esc(s.url)+'" target="_blank" rel="noopener noreferrer">'+esc(s.title)+' ↗</a></p>').join('')+'<p class="small muted">Reviewed '+esc(D.date)+'. The activities and experiment records are original SuccessLabs learning material.</p></div><div class="card"><h3>Before accepting a mapping</h3><ol><li>Pin the actual document edition and country entry.</li><li>Check the source field and target definition in that entry.</li><li>Distinguish document constraints from your implementation choices.</li><li>Predict positive, negative and historical cases.</li><li>Run the actual sandbox check and reconcile its result.</li></ol></div>'}
function lab(){return header('Mapping experiment',P.name+' · source-to-target practice','An illustrative contract check using synthetic input. This exercise does not run SAP replication.')+'<div class="notice"><strong>Choose a test contract</strong>Set a proposed maximum length and required-value rule, then compare a synthetic source value with a target value. These are learner-chosen constraints; consult the country guide for the actual field requirements.</div><div class="card"><div class="lab-grid"><div class="field"><label for="map-source">Synthetic source value</label><input id="map-source" value="Learning Street 12"></div><div class="field"><label for="map-target">Observed target value</label><input id="map-target" value="Learning Street 12"></div><div class="field"><label for="map-max">Proposed maximum characters</label><input id="map-max" type="number" min="1" max="250" value="40"></div><div class="field"><label for="map-required">Proposed required-value rule</label><select id="map-required"><option value="yes">Required for this experiment</option><option value="no">Optional for this experiment</option></select></div></div><div class="notice" id="map-result" role="status" aria-live="polite"></div><button class="btn primary" id="map-export">Export this experiment</button><p class="small muted" style="margin-top:15px">Try a blank source, a truncated target and an over-length source. Explain what each case proves about the chosen contract and what it leaves unanswered about the real country mapping.</p></div>'}
function bindLab(){const read=()=>{const a=$('map-source').value,b=$('map-target').value,max=Math.max(1,Number($('map-max').value)||1),required=$('map-required').value==='yes';const errors=[];if(required&&!a.trim())errors.push('Required source is blank.');if(a.length>max)errors.push('Source exceeds the proposed length.');if(a!==b)errors.push('Source and target differ.');$('map-result').textContent=errors.length?errors.join(' '):'This synthetic case meets your chosen contract. It is not proof of an actual SAP replication result.';return {country:P.name,source:a,target:b,proposedMax:max,proposedRequired:required,result:errors.length?errors.join(' '):'Illustrative contract passed',guide:D.sources[0].url}};['map-source','map-target','map-max','map-required'].forEach(id=>$(id).oninput=read);$('map-export').onclick=()=>download(P.name.replace(/ /g,'_')+'_Mapping_Experiment.json','application/json',JSON.stringify(read(),null,2));read()}
"""

def build():
 text=TEMPLATE.read_text();base=json.loads(re.search(r'<script type="application/json" id="workbook-data">(.*?)</script>',text,re.S).group(1));base_js=re.findall(r'<script([^>]*)>(.*?)</script>',text,re.S)[1][1]
 font=base64.b64encode((ROOT/'comfortaa.woff').read_bytes()).decode();logo=base64.b64encode((ROOT/'successlabs-academy-logo.png').read_bytes()).decode()
 entries=[];app=json.loads((ROOT/'appendix-blueprints.json').read_text());specs=[(name,info,False) for name,info in MAIN.items()]+[(r['country'],r,True) for r in app]
 for idx,(name,info,is_app) in enumerate(specs):
  p=profile(name,info,is_app);sec=info.get('section','chapter '+info.get('chapter',''));page=info['page'];p['refs']=['sap-country'];refs=[source('sap-country',f'SAP · {name} · 2H 2026 · {sec} · page {page}',GUIDE+'#page='+str(page))]
  refs += [source(*r) for r in info.get('refs',[])]
  data=dict(profile=p,modules=appendix_modules(p,info) if is_app else main_modules(base['modules'],p,info),quiz=shared_quiz(name,is_app,sec),cards=cards(name,sec),sources=refs,date=DATE,theme=dict(deep='hsl(170 38% 24%)',mid='hsl(200 43% 40%)',accent='hsl(174 44% 29%)',bright='hsl(150 55% 82%)',pale='hsl(165 40% 95%)'),coverage=dict(kind='appendix' if is_app else 'main',section=sec,page=page,guideVersion='2H 2026',guideDate='2026-10-16'))
  count=len(data['modules']);js=base_js.replace("done+' / 48'","done+' / '+M.length").replace('done/48*100','done/M.length*100').replace("'+m.n+' of 48</div>","'+m.n+' of '+M.length+'</div>").replace('m.n<48?','m.n<M.length?')
  js=js.replace('48 detailed sections form a complete country learning journey.','48 learning and design sections connect the country source material to an evidence-based implementation journey.').replace('Published statutory reference','Published guide / authority reference')
  if is_app:
   # These declarations replace the generic overview/evidence/lab functions before route() executes.
   js=js.replace('route();if(!storageOK)',APPENDIX_JS+'\nroute();if(!storageOK)')
   js=js.replace("P.name+' payroll, made tangible.'","P.name+' replication, made tangible.'").replace("P.currency+' · Country-specific design'","'SAP appendix · Replication practice'").replace("['lab','∑','Gross-to-net practice lab']","['lab','∑','Mapping experiment lab']")
  html=re.sub(r'<script type="application/json" id="workbook-data">.*?</script>',lambda m:'<script type="application/json" id="workbook-data">'+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</',r'<\/')+'</script>',text,flags=re.S)
  html=html.replace(base_js,js).replace('United Arab Emirates',name)
  html=html.replace('6 November 2026',DATE)
  html=html.replace('48 configuration sections',str(count)+' guided sections')
  html=html.replace('48 detailed sections',str(count)+' guided sections').replace('>48<','>'+str(count)+'<')
  html=html.replace('Search 48 sections + tools...',f'Search {count} sections + tools...')
  if is_app:
   html=html.replace(name+' Payroll Workbook',name+' Replication Workbook').replace(name+' Payroll ·',name+' Replication ·')
   html=html.replace(name+' ECP Workbook',name+' ECP Replication Workbook').replace('Configuration sections','Guided experiments')
   html=html.replace('Country payroll · living learning workbook','Country replication · living learning workbook')
   html=re.sub(r'<meta name="description" content="[^"]*">',lambda m:'<meta name="description" content="'+name+' replication learning workbook. Twelve guided experiments, six learning tools and pinned SAP 2H 2026 appendix evidence.">',html)
   html=re.sub(r'(<h1 id="hero-title"></h1>)<p>.*?</p>',r'\1<p>Follow a synthetic employee from source fields through mapping, validation and reconciliation. Build confidence with small experiments and clear evidence.</p>',html,count=1,flags=re.S)
  html=re.sub(r'<link href="https://fonts.googleapis.com[^>]+>','',html)
  html=html.replace('</head>',f'<style id="sla-local-font">@font-face{{font-family:Comfortaa;src:url(data:font/woff;base64,{font}) format("woff");font-weight:300 700;font-display:swap}}button,input,select,textarea{{font-family:Comfortaa,sans-serif}}</style></head>')
  # Keep the bundled official logo exactly as supplied; no redrawing or generated substitute.
  html=re.sub(r'(<img[^>]*src=")[^"]+("[^>]*alt="SuccessLabs Academy"[^>]*>)',lambda m:m.group(1)+'data:image/png;base64,'+logo+m.group(2),html)
  # An ISO country marker avoids carrying the template country's flag into a replica.
  codes='MX ZA GB AO BD BY BW KH CR DO SV EE GH GT HN IS IM IL JO KZ KE XK LV LB LT LU MW MT MA MZ MM NA NI MK NG PK PA PR RS SS TZ TN UG VN ZW'.split()
  assert len(codes)==len(specs)
  country_code=codes[idx]
  html=re.sub(r'<img class="mark"[^>]*>',lambda m:'<span class="mark" aria-hidden="true" style="display:grid;place-items:center;font-size:13px;font-weight:700">'+country_code+'</span>',html)
  if 'GPSSA' in html or 'MoHRE' in html or 'No UAE individual income tax' in html:raise AssertionError('Unrelated country content leaked into '+name)
  dest=name.replace(' ','_')+'.html';(OUT/dest).write_text(html)
  for i,(attrs,code) in enumerate(re.findall(r'<script([^>]*)>(.*?)</script>',html,re.S)):
   if 'application/json' in attrs:json.loads(code);continue
   subprocess.run(['node','--check'],input=code,text=True,check=True,capture_output=True)
  raw=(OUT/dest).read_bytes();entries.append(dict(country=name,path=dest,source=dest,kind=data['coverage']['kind'],sections=count,guideSection=sec,guidePage=page,sha256=hashlib.sha256(raw).hexdigest(),gitBlobSha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()))
 (ROOT/'generated-manifest.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2));print(json.dumps({'generated':len(entries),'main':sum(e['kind']=='main' for e in entries),'appendix':sum(e['kind']=='appendix' for e in entries),'javascriptChecks':'passed'}))

if __name__=='__main__':build()
