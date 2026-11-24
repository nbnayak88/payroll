# SAP UK Payroll — From First Payslip to Transformation Architect

SuccessLabs Academy · Mission Ananta · HR07 Architecting Payroll Enterprises  
Version 1.0 · Published 24 November 2026 · Statutory baseline: UK tax year 2026–2027

> Every accurate payslip is an experience of trust, designed through evidence.

## Promise and scope

Build the ability to explain, configure, test, operate and architect UK payroll services across SAP HCM Payroll and SAP SuccessFactors Employee Central Payroll. This is an aspirational curriculum blueprint with detailed learning specifications, experiments and assessment evidence. It is not a claim that training videos, tenant configuration or payroll test execution have already been delivered. Learning hours are planning estimates, not a guarantee of mastery or employment.

The UK includes England, Scotland, Wales and Northern Ireland. Ireland and Crown Dependencies require separate scope. Each lesson distinguishes legislation, employer policy, SAP standard, customer configuration and external-provider responsibility. Compare SAP HCM Payroll and ECP using the actual product version, support package, contract, permissions and supported interfaces. EC is a source HR platform, not itself the UK gross-to-net engine.

## Learning architecture

36 modules: 288 hours, plus 72 hours of portfolio challenges = **360 recommended learning hours**. Modules include explanation, guided demonstration, sandbox work or design simulation, independent experimentation, evidence capture and reflection. Learners can demonstrate prior competence to enter a later stage. A completed checkbox is a personal progress record; assessed evidence determines competence.

| Stage | Modules | Hours | Exit capability |
|---|---|---:|---|
| Origin | UK01–UK06 | 12 | Explain payroll purpose, stakeholders and evidence |
| Pre-Foundation | UK07–UK12 | 24 | Navigate the landscape and trace a controlled cycle |
| Foundation | UK13–UK18 | 48 | Configure and diagnose core calculations in a sandbox |
| Essentials | UK19–UK24 | 60 | Design statutory, pension, RTI and year-end controls |
| Advanced | UK25–UK30 | 72 | Integrate, migrate, test and transition a service |
| Ultimate | UK31–UK36 | 72 | Defend architecture and lead evidence-based improvement |
| Portfolio challenges | C1–C3 | 72 | Demonstrate end-to-end professional capability |

Silver/Foundation: self-guided concepts and guided practice. Gold/Essentials: facilitated configuration and reconciliation. Diamond/Advanced: implementation and architecture studios. Ultimate: specialist practice and leadership. These are proposed learning pathways, not new pricing or entitlement commitments.

## Entry diagnostics and role routes

Newcomer: explain a payslip, tax year and five stakeholder roles before UK07. SAP consultant: demonstrate effective dating, wage-type concepts and payroll-log reading before UK13. UK payroll practitioner: pass a SAP landscape and data-lineage exercise before skipping UK07–UK12. Architect: demonstrate a reconciled payroll cycle and statutory reporting lifecycle before entering UK25.

Payroll analyst route: UK01–UK12, UK15–UK24 and UK30. Configuration consultant: UK07–UK30. Integration consultant: UK07–UK12 and UK25–UK29 with statutory context from UK15–UK24. Solution architect: full pathway plus C3. These subsets overlap and do not carry a separate fixed duration; assess gaps individually.

## Flexible delivery formats

**Three-day discovery workshop: 18 hours.** Day 1: purpose and intention 1h, UK institutions and payslip 2h, calendar and master-data journey 2h, reflection 1h. Day 2: tax/NI and wage-type demonstration 2h, time/statutory/pension scenarios 2h, payroll-log and RTI walkthrough 2h. Day 3: integration and reconciliation 2h, incident simulation 2h, architecture showcase and next-step charter 2h. Discovery does not confer configuration mastery.

**Three-week launch bootcamp: 45 hours.** Week 1: 15h of foundations, landscape and master data; week 2: 15h of calculation and statutory scenarios; week 3: 15h of reporting, integration and a reconciled demonstration. This is a curated launch subset; the 360h pathway supplies the subsequent depth.

**Practitioner pathway:** 24 weeks × 15 hours = 360h. Weeks 1–3 cover UK01–UK12 plus the first 9h of C1; weeks 4–6 UK13–UK18; weeks 7–10 UK19–UK24; weeks 11–15 UK25–UK30; weeks 16–20 UK31–UK36; weeks 21–24 complete remaining portfolio work and remediation. Sequence by prerequisites and use weekly capacity flexibly; module boundaries need not equal week boundaries.

**Micro-sprint pattern:** 15m question and recall, 20m concept, 25m demonstration, 40m experiment, 15m evidence and explanation, 5m next hypothesis = 120m. Short videos should focus on one decision; a learner then applies it to an unfamiliar case. Optional peer studios use existing community sessions instead of adding mandatory meetings.

## Sandbox and readiness prerequisites

For configuration evidence, provide an authorised non-production SAP UK payroll system with an identified release/support-package level, relevant country localisation, scoped roles, transport route and synthetic employees. For the ECP lane, confirm EC/ECP licences, provisioning, supported integration, mapping access and monitoring. PCC, SAP Integration Suite, analytics, bank connectivity and pension interfaces require separate applicability and entitlement checks. SAP for Me access may be required for full Notes/KBAs. Use training/test endpoints where available; local mock payloads are sufficient for interface design exercises. Never transmit synthetic submissions to production HMRC or release bank payments during training.

Without a tenant, complete design and calculation simulations and label the evidence **design-only**. Do not award an executed-configuration badge until a reviewer sees system outputs. Record environment, release, execution date, input fixtures, expected/actual results, defects and reviewer for each executed lab.

## Fictional case thread

**OmniWorks Industrial Systems UK Ltd**, an original fictional extension of the Industrials case: 1,200 UK employees; one monthly salaried population and one weekly shift population; HR master in EC, UK payroll in the selected SAP engine, external time capture, FI destination, Treasury bank channel and pension provider. Include all four UK nations. All headcounts and arrangements are teaching assumptions.

Synthetic personas: Maya Shah, UK Payroll Lead; Owen Hughes, HR Operations Manager; Isla Fraser, Finance Controller; Aisha Khan, Integration Architect; Daniel Reed, Treasury Approver; Niamh Clarke, Security Reviewer. Rotate these roles in discovery, incident response and design reviews.

Test workers: TEST-UK-001 monthly starter without P45; TEST-UK-002 Scottish taxpayer with retro salary award; TEST-UK-003 Welsh taxpayer with student and postgraduate loans; TEST-UK-004 weekly shift worker with overtime and sickness; TEST-UK-005 director; TEST-UK-006 maternity then neonatal-care scenario subject to verified eligibility; TEST-UK-007 leaver with termination elements; TEST-UK-008 low-paid worker with pension assessment; TEST-UK-009 worker with ordered deductions; TEST-UK-010 rehire requiring identifier continuity. Do not invent valid national insurance numbers or real bank details. Financial values are learner-defined synthetic inputs, versioned with their tax-year assumptions.

## Detailed module specifications

Each module produces a reusable portfolio artefact. Prerequisites are a default sequence, not a rigid curriculum: a reviewer can accept equivalent evidence. The acceptance criterion is assessed using the shared rubric below.

### UK01 · Payroll purpose and professional identity

**Level:** Origin · **Effort:** 2h · **Entry:** Learning charter.

**Learning scope and outcomes**

- Explain and apply Employee trust.
- Explain and apply payroll as a service.
- Explain and apply gross-to-net.
- Explain and apply employer cost.
- Explain and apply payroll analyst, consultant and architect roles.

**Experiment:** Interview a fictional payroll manager and trace a late salary complaint from symptom to business impact.

**Portfolio evidence:** Personal learning charter and payroll service canvas.

**Acceptance:** Explain employee net pay versus employer total cost and name the accountable process owners.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK02 · UK institutions and jurisdiction

**Level:** Origin · **Effort:** 2h · **Entry:** UK01 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply HMRC, The Pensions Regulator, employment policy, devolved income tax, Northern Ireland distinctions, UK versus Crown Dependencies.

**Experiment:** Build a responsibility map for England, Scotland, Wales and Northern Ireland; keep Ireland and Isle of Man outside the UK scope.

**Portfolio evidence:** Jurisdiction and regulator map with source register.

**Acceptance:** Separate tax jurisdiction, work location, residence and employing entity without assuming they are equivalent.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK03 · Payslip and gross-to-net literacy

**Level:** Origin · **Effort:** 2h · **Entry:** UK02 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Contractual earnings.
- Explain and apply taxable pay.
- Explain and apply NI-able pay.
- Explain and apply pensionable pay.
- Explain and apply deductions.
- Explain and apply year-to-date balances.

**Experiment:** Annotate a synthetic payslip and reconcile each line to a source event.

**Portfolio evidence:** Payslip explanation and arithmetic bridge.

**Acceptance:** Reconcile gross less deductions to net and explain why the calculation bases differ.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK04 · Calendar and service rhythm

**Level:** Origin · **Effort:** 2h · **Entry:** UK03 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Tax year 6 April–5 April.
- Explain and apply tax months.
- Explain and apply weekly, fortnightly, four-weekly and monthly frequencies.
- Explain and apply cut-offs and approvals.

**Experiment:** Design a calendar spanning a bank holiday and tax-year boundary.

**Portfolio evidence:** Payroll calendar and responsibility matrix.

**Acceptance:** Distinguish contractual payday, processing date, bank deadline and reporting deadline.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK05 · Evidence and responsible experimentation

**Level:** Origin · **Effort:** 2h · **Entry:** UK04 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Primary sources.
- Explain and apply tax-year applicability.
- Explain and apply approved employer policy.
- Explain and apply assumptions.
- Explain and apply synthetic data.
- Explain and apply version history.

**Experiment:** Compare an old training slide with current guidance and record a corrected learning hypothesis.

**Portfolio evidence:** Evidence log and uncertainty register.

**Acceptance:** Every statutory claim has a URL, effective date, review date and owner.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK06 · Payroll discovery and experience

**Level:** Origin · **Effort:** 2h · **Entry:** UK05 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Employee journeys.
- Explain and apply HR, Finance, Treasury and payroll handoffs.
- Explain and apply accessibility.
- Explain and apply complaints.
- Explain and apply service outcomes.

**Experiment:** Role-play a joiner, payroll analyst and CFO discovering failure points.

**Portfolio evidence:** Stakeholder interview guide and current-state journey.

**Acceptance:** Show at least five failure points with an owner, control and measurable outcome.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK07 · SAP landscape and product choices

**Level:** Pre-Foundation · **Effort:** 4h · **Entry:** UK06 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply SAP HCM Payroll, SAP HCM for SAP S/4HANA, SuccessFactors Employee Central Payroll.
- Explain and apply EC as HR master.
- Explain and apply backend versus employee experience.

**Experiment:** Compare two target landscapes and identify licences, access, release and responsibility boundaries.

**Portfolio evidence:** Product decision record and environment readiness checklist.

**Acceptance:** No assumption that EC, ECP, PCC or middleware is automatically licensed or activated.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK08 · Organisation and payroll structures

**Level:** Pre-Foundation · **Effort:** 4h · **Entry:** UK07 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Company codes.
- Explain and apply personnel areas/subareas.
- Explain and apply employee groups/subgroups.
- Explain and apply country grouping.
- Explain and apply payroll areas.
- Explain and apply cost centres.

**Experiment:** Design monthly salaried and weekly operational populations for OmniWorks UK.

**Portfolio evidence:** Organisation-to-payroll mapping and configuration workbook.

**Acceptance:** Explain grouping choices, reporting needs and transport dependencies before changing configuration.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK09 · Employee lifecycle and master data

**Level:** Pre-Foundation · **Effort:** 4h · **Entry:** UK08 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Effective dating.
- Explain and apply hiring.
- Explain and apply transfers.
- Explain and apply leavers.
- Explain and apply rehires.
- Explain and apply bank data.
- Explain and apply basic pay.
- Explain and apply recurring and one-time payments.
- Explain and apply UK statutory data.

**Experiment:** Create synthetic joiner and leaver records, then introduce a backdated transfer.

**Portfolio evidence:** Data dictionary, lifecycle timeline and validation rules.

**Acceptance:** Distinguish business-effective date, replication date and payroll impact date.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK10 · Time, absence and valuation

**Level:** Pre-Foundation · **Effort:** 4h · **Entry:** UK09 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Planned working time.
- Explain and apply absence records.
- Explain and apply time evaluation boundaries.
- Explain and apply overtime inputs.
- Explain and apply public holidays.
- Explain and apply approved holiday-pay policy.

**Experiment:** Trace a shift worker's approved time and absence to proposed payroll inputs.

**Portfolio evidence:** Time-to-pay interface map and valuation examples.

**Acceptance:** Identify missing approvals, duplicate hours and policy assumptions without inventing a universal overtime rule.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK11 · Payroll execution and control records

**Level:** Pre-Foundation · **Effort:** 4h · **Entry:** UK10 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Simulation.
- Explain and apply release.
- Explain and apply correction.
- Explain and apply exit.
- Explain and apply payroll logs.
- Explain and apply result inspection.
- Explain and apply employee-level errors.
- Explain and apply controlled reruns.

**Experiment:** Run or storyboard a payroll cycle containing one rejected employee.

**Portfolio evidence:** Cycle runbook and error triage log.

**Acceptance:** Show who can change data at each state and how failed employees are recovered.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK12 · Reading results and reconciliation

**Level:** Pre-Foundation · **Effort:** 4h · **Entry:** UK11 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Earnings, deductions, employer costs, cumulative balances.
- Explain and apply wage-type totals.
- Explain and apply variance analysis.
- Explain and apply result lineage.

**Experiment:** Explain two successive results with a salary change and compare totals.

**Portfolio evidence:** Result walkthrough and first reconciliation pack.

**Acceptance:** Every material variance links to an approved event or a documented defect.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK13 · Wage-type engineering

**Level:** Foundation · **Effort:** 8h · **Entry:** UK12 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Copying suitable model wage types.
- Explain and apply permissibility.
- Explain and apply valuation.
- Explain and apply processing, cumulation and evaluation classes.
- Explain and apply tax/NI/pension treatment.

**Experiment:** Design salary, overtime, bonus, deduction and benefit wage types in a sandbox.

**Portfolio evidence:** Wage-type catalogue and treatment decision table.

**Acceptance:** For each wage type, demonstrate expected bases and posting outcomes with positive and negative tests.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK14 · Schemas and personnel calculation rules

**Level:** Foundation · **Effort:** 8h · **Entry:** UK13 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Schema flow.
- Explain and apply functions and operations.
- Explain and apply PCR branching.
- Explain and apply employee subgroup groupings.
- Explain and apply custom namespace.
- Explain and apply logs and transport discipline.

**Experiment:** Trace a delivered calculation, then prototype one controlled allowance rule.

**Portfolio evidence:** Annotated schema trace, PCR specification and rollback plan.

**Acceptance:** Explain input, decision and output; compare standard behaviour before proposing a custom rule.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK15 · PAYE and tax-code lifecycle

**Level:** Foundation · **Effort:** 8h · **Entry:** UK14 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Cumulative and non-cumulative operation.
- Explain and apply tax-code notices.
- Explain and apply Scottish and Welsh prefixes.
- Explain and apply starter information.
- Explain and apply tax refunds.
- Explain and apply tax-year boundaries.

**Experiment:** Test a starter without P45, a new tax code and an in-year correction.

**Portfolio evidence:** PAYE scenario matrix and independently calculated expected results.

**Acceptance:** Use tax-year-specific guidance and preserve notice/source lineage; avoid treating a sample code as universal.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK16 · National Insurance and directors

**Level:** Foundation · **Effort:** 8h · **Entry:** UK15 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Employee and employer Class 1.
- Explain and apply category selection.
- Explain and apply thresholds.
- Explain and apply directors' methods.
- Explain and apply category changes.
- Explain and apply relief eligibility.

**Experiment:** Compare an ordinary employee, director and apprentice using controlled test inputs.

**Portfolio evidence:** NI decision table and boundary-test pack.

**Acceptance:** Test just below, at and above relevant thresholds and separate employee from employer calculations.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK17 · Loans and ordered deductions

**Level:** Foundation · **Effort:** 8h · **Entry:** UK16 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Student and postgraduate loans.
- Explain and apply start/stop notices.
- Explain and apply simultaneous deductions.
- Explain and apply attachment orders.
- Explain and apply priority.
- Explain and apply protected earnings.
- Explain and apply jurisdiction.

**Experiment:** Simulate a loan plan change and multiple ordered deductions with a low-net-pay case.

**Portfolio evidence:** Deduction priority design and remittance reconciliation.

**Acceptance:** Document the legal basis per order type and prevent unsupported generic priority assumptions.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK18 · Regular, retroactive and exceptional pay

**Level:** Foundation · **Effort:** 8h · **Entry:** UK17 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Retro limits.
- Explain and apply earliest changes.
- Explain and apply splits.
- Explain and apply backdated pay awards.
- Explain and apply off-cycle applicability.
- Explain and apply reversals.
- Explain and apply overpayments.
- Explain and apply negative net.

**Experiment:** Process a backdated salary increase and an emergency payment without duplicating payment or reporting.

**Portfolio evidence:** Retro explanation, exceptional-payment runbook and reconciliation.

**Acceptance:** Tie original and replacement results to net payment, statutory reporting and FI effects.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK19 · Sickness and statutory family pay

**Level:** Essentials · **Effort:** 10h · **Entry:** UK18 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply SSP.
- Explain and apply maternity, paternity, adoption, shared parental, parental bereavement and neonatal care pay.
- Explain and apply eligibility, average earnings, overlaps and recovery.

**Experiment:** Test a sickness case crossing April 2026 and a neonatal-care case alongside another family-pay entitlement.

**Portfolio evidence:** Statutory-pay decision trees, eligibility evidence and effective-date tests.

**Acceptance:** Keep SSP non-recoverable; distinguish parental-pay recovery; test transitional rules and installed SAP legal changes.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK20 · Pensions and automatic enrolment

**Level:** Essentials · **Effort:** 10h · **Entry:** UK19 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Worker assessment.
- Explain and apply eligible jobholders.
- Explain and apply opt-in/joining.
- Explain and apply postponement.
- Explain and apply opt-out/refunds.
- Explain and apply re-enrolment.
- Explain and apply contribution bases.
- Explain and apply net pay versus relief at source.

**Experiment:** Process age and earnings changes, an opt-out and a backdated contribution correction.

**Portfolio evidence:** Assessment timeline, pension interface and contribution reconciliation.

**Acceptance:** Evidence assessment decisions, communications, contribution basis and provider acknowledgement.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK21 · Benefits, expenses and salary sacrifice

**Level:** Essentials · **Effort:** 10h · **Entry:** UK20 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Cash versus benefits in kind.
- Explain and apply payrolling benefits.
- Explain and apply P11D/P11D(b).
- Explain and apply Class 1A.
- Explain and apply salary sacrifice.
- Explain and apply optional remuneration.
- Explain and apply mileage.

**Experiment:** Compare a pension sacrifice, company car and taxable expense using current guidance.

**Portfolio evidence:** Benefit-treatment matrix and year-end responsibility map.

**Acceptance:** Separate current rules from announced future changes and test minimum-wage implications where applicable.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK22 · Minimum wage, holiday and termination

**Level:** Essentials · **Effort:** 10h · **Entry:** UK21 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply National Minimum/Living Wage.
- Explain and apply pay-reference periods.
- Explain and apply deductions.
- Explain and apply holiday pay policy.
- Explain and apply PILON/PENP.
- Explain and apply redundancy and termination awards.

**Experiment:** Investigate a low-paid worker's deduction and a leaver with multiple termination elements.

**Portfolio evidence:** Minimum-wage review and termination treatment specification.

**Acceptance:** Break termination components into their individual treatments rather than applying a blanket exemption.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK23 · RTI and HMRC reconciliation

**Level:** Essentials · **Effort:** 10h · **Entry:** UK22 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply FPS.
- Explain and apply EPS.
- Explain and apply reporting timing.
- Explain and apply identifiers.
- Explain and apply acknowledgements.
- Explain and apply rejected submissions.
- Explain and apply corrections.
- Explain and apply balances and HMRC account reconciliation.

**Experiment:** Create a mock submission, reject an identifier and demonstrate controlled resubmission.

**Portfolio evidence:** RTI field lineage, submission register and correction playbook.

**Acceptance:** Evidence accepted acknowledgement as well as transmission; prevent duplicate reporting; use current SAP RTI documentation.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK24 · Year-end and tax-year transition

**Level:** Essentials · **Effort:** 10h · **Entry:** UK23 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Final reporting.
- Explain and apply P60.
- Explain and apply P45 on leaving.
- Explain and apply benefits reporting.
- Explain and apply opening balances.
- Explain and apply rates and thresholds.
- Explain and apply SAP legal change delivery.

**Experiment:** Rehearse a March/April transition with a leaver and benefit reconciliation.

**Portfolio evidence:** Year-end checklist and tax-year change regression pack.

**Acceptance:** Reconcile year-to-date values, employee outputs and statutory liabilities before sign-off.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK25 · EC-to-payroll replication architecture

**Level:** Advanced · **Effort:** 12h · **Entry:** UK24 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Effective-dated employee data.
- Explain and apply mapping.
- Explain and apply replication monitoring.
- Explain and apply error recovery.
- Explain and apply source ownership.
- Explain and apply identifiers.
- Explain and apply EC Payroll integration options.

**Experiment:** Inject a missing mapping, duplicate event and out-of-order effective date.

**Portfolio evidence:** Field mapping, sequence diagram and recovery evidence.

**Acceptance:** Choose the supported integration pattern for the actual release; do not assume CPI is mandatory for every EC-to-ECP integration.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK26 · Finance, Treasury and payment integration

**Level:** Advanced · **Effort:** 12h · **Entry:** UK25 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Symbolic accounts.
- Explain and apply cost assignment.
- Explain and apply posting runs.
- Explain and apply liabilities.
- Explain and apply balancing.
- Explain and apply bank files.
- Explain and apply Bacs and bank-channel responsibilities.

**Experiment:** Reconcile payroll totals to an FI journal and synthetic payment file; then reject one bank record.

**Portfolio evidence:** Posting specification, bank interface and four-way reconciliation.

**Acceptance:** Reconcile gross-to-net, bank net, FI balances and liabilities; payment format and Faster Payments depend on bank and service design.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK27 · Security, privacy and resilient operations

**Level:** Advanced · **Effort:** 12h · **Entry:** UK26 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Least privilege.
- Explain and apply segregation of duties.
- Explain and apply backend authorisations.
- Explain and apply EC RBP.
- Explain and apply privileged access.
- Explain and apply encryption.
- Explain and apply retention.
- Explain and apply audit.
- Explain and apply recovery.

**Experiment:** Threat-model a bank-account change and rehearse a failed payroll batch.

**Portfolio evidence:** Access matrix, threat model and recovery runbook.

**Acceptance:** Separate HR master-data access, payroll processing, payment release and technical administration.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK28 · Migration, testing and parallel runs

**Level:** Advanced · **Effort:** 12h · **Entry:** UK27 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Data cleansing.
- Explain and apply balances.
- Explain and apply history scope.
- Explain and apply identifiers.
- Explain and apply mock loads.
- Explain and apply unit, integration, regression and UAT.
- Explain and apply parallel reconciliation.

**Experiment:** Migrate a synthetic mid-year population and explain every difference against a controlled baseline.

**Portfolio evidence:** Migration reconciliation, defect log and signed test pack.

**Acceptance:** Zero unexplained critical differences; business-approved rounding tolerances; no balancing totals that conceal employee errors.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK29 · Cutover and operational transition

**Level:** Advanced · **Effort:** 12h · **Entry:** UK28 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply SAP Activate delivery gates.
- Explain and apply run sequence.
- Explain and apply freeze windows.
- Explain and apply go/no-go.
- Explain and apply rollback constraints.
- Explain and apply first live payroll.
- Explain and apply hypercare.

**Experiment:** Run a tabletop cutover with a replication outage near the payment deadline.

**Portfolio evidence:** Timed cutover plan, decision log and support handover.

**Acceptance:** Named owners approve payroll, bank release, RTI and FI; recovery feasibility is assessed after external submission.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK30 · Payroll Control Center and AMS

**Level:** Advanced · **Effort:** 12h · **Entry:** UK29 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply PCC availability and configuration.
- Explain and apply validation rules.
- Explain and apply alerts.
- Explain and apply root-cause analysis.
- Explain and apply SLA.
- Explain and apply incident/problem/change management.

**Experiment:** Design alerts for abnormal net pay and missing tax data; role-play an urgent payroll incident.

**Portfolio evidence:** Control catalogue, incident evidence pack and AMS acceptance criteria.

**Acceptance:** Alert thresholds have owners and false-positive review; distinguish business rule defects from technical outages.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK31 · Enterprise payroll architecture

**Level:** Ultimate · **Effort:** 12h · **Entry:** UK30 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Capabilities.
- Explain and apply value streams.
- Explain and apply service boundaries.
- Explain and apply integration contracts.
- Explain and apply data lineage.
- Explain and apply non-functional requirements.
- Explain and apply deployment options.

**Experiment:** Defend a UK payroll target architecture to a fictional CHRO, CFO and security lead.

**Portfolio evidence:** Architecture dossier with alternatives, constraints and decisions.

**Acceptance:** Explain service ownership, data authority, failure handling, observability and product-specific limits.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK32 · Specialist and sector pathways

**Level:** Ultimate · **Effort:** 12h · **Entry:** UK31 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Public-sector pensions and retro awards.
- Explain and apply utilities shift pay.
- Explain and apply industrial overtime.
- Explain and apply financial-services bonuses.
- Explain and apply expatriates.
- Explain and apply shadow payroll.
- Explain and apply CIS boundary.

**Experiment:** Choose one sector and identify specialist advice and integration dependencies.

**Portfolio evidence:** Sector extension backlog and applicability assessment.

**Acceptance:** Treat CIS subcontractor processing and maritime/expatriate rules as specialist scope requiring verified product support.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK33 · Analytics and service improvement

**Level:** Ultimate · **Effort:** 12h · **Entry:** UK32 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Accuracy.
- Explain and apply timeliness.
- Explain and apply first-time-right.
- Explain and apply cost per payslip.
- Explain and apply exception rate.
- Explain and apply case ageing.
- Explain and apply observability.
- Explain and apply privacy-preserving analytics.

**Experiment:** Build a synthetic KPI dashboard and investigate a rising retro-adjustment rate.

**Portfolio evidence:** Metrics dictionary and improvement experiment.

**Acceptance:** Define numerator, denominator, owner and data lineage; measure effects before and after a controlled change.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK34 · AI-assisted payroll with human control

**Level:** Ultimate · **Effort:** 12h · **Entry:** UK33 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Retrieval over approved guidance.
- Explain and apply source citations.
- Explain and apply policy explanation.
- Explain and apply anomaly triage.
- Explain and apply access controls.
- Explain and apply model evaluation.
- Explain and apply human approvals.

**Experiment:** Prototype a payroll-policy assistant using synthetic questions and test misleading or outdated prompts.

**Portfolio evidence:** Evaluation dataset, failure log and approval workflow.

**Acceptance:** No autonomous changes to pay, bank files or HMRC submissions; demonstrate correct escalation when evidence is missing.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK35 · Legal-change and release engineering

**Level:** Ultimate · **Effort:** 12h · **Entry:** UK34 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply HMRC updates.
- Explain and apply SAP Notes applicability.
- Explain and apply support-package dependencies.
- Explain and apply regression scope.
- Explain and apply effective dates.
- Explain and apply transport and rollback strategy.

**Experiment:** Build a change-impact analysis for a new tax year and a statutory-pay update.

**Portfolio evidence:** Legal-change register and release evidence pack.

**Acceptance:** Every rule change links to authority, applicable SAP delivery, test cases and approval; announced changes remain flagged until effective.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

### UK36 · Practice leadership and professional portfolio

**Level:** Ultimate · **Effort:** 12h · **Entry:** UK35 or demonstrated equivalent.

**Learning scope and outcomes**

- Explain and apply Discovery facilitation.
- Explain and apply estimation.
- Explain and apply presales.
- Explain and apply ethical claims.
- Explain and apply reusable accelerators.
- Explain and apply coaching.
- Explain and apply career narrative.
- Explain and apply continuous learning.

**Experiment:** Present a ten-minute payroll transformation proposal and teach a difficult concept to a peer.

**Portfolio evidence:** Portfolio index, demonstration recording and personal development roadmap.

**Acceptance:** Defend assumptions, show original evidence and explain limitations without claiming SAP certification.

**Stretch:** Change one effective date, employee population or input assumption. Predict the outcome before rerunning the experiment; explain the difference using evidence.

## Portfolio challenges — 72 hours

### C1 · Trustworthy payroll cycle — 18h

Discover and design 3h; prepare fixtures and configuration/simulation 5h; execute and reconcile 6h; explain and peer-review 4h. Cover a starter, a weekly worker, a tax-code change and a leaver. Submit a service map, inputs, calculation basis, gross-to-net bridge, log/error evidence, payslip explanation and reporting timeline. Pass when every material difference is explained and every claim is marked executed or design-only.

### C2 · Statutory and integration recovery studio — 24h

Rule/source review 4h; scenario preparation 4h; testing and recovery 10h; evidence review 6h. Cover SSP change boundaries, parental pay, pension assessment, loan changes, rejected replication and an RTI rejection. Produce a dated decision register, expected/actual comparisons, recovery sequence and payroll/FI/bank/statutory reconciliation. Pass when retries do not duplicate employees, payments or reporting and an independent reviewer can reproduce the result.

### C3 · UK payroll transformation architecture — 30h

Discovery 5h; option and architecture design 7h; migration/test/cutover plan 8h; operational and security design 5h; presentation and defence 5h. Use the fictional OmniWorks case. Deliver a 10-slide decision narrative, context/container/interface views, capability map, requirements traceability, 12 architecture-stream viewpoints, cost assumptions, roadmap, controls, cutover and AMS dossier. Pass when two viable options are compared, ownership is clear, statutory and technical dependencies are evidenced and the board can make an informed go/no-go decision.

## Assessment and mastery

Entry diagnostic: 20 questions plus a five-minute payslip explanation; diagnostic only. Each module: a short retrieval quiz, one lab and a ten-minute teach-back. Each stage: unseen scenario and portfolio review. Suggested rubric: statutory/policy accuracy 25%; configuration or design reasoning 20%; reconciliation/test evidence 25%; security and operational controls 15%; communication and reflection 15%. Pass at 80/100, with remediation allowed. A missing critical control, unexplained payroll difference, fabricated execution evidence or unsafe payment/reporting practice blocks progression regardless of score.

Sample assessment prompts with assessor expectations:

1. Why can taxable, NI-able and pensionable pay differ? Expect distinct treatment bases and evidence for each wage type.
2. A salary award is backdated after payroll exit. What must be investigated? Expect effective dates, retro limits, result differences, employee payment, reporting and FI implications.
3. Is SSP recovery a valid EPS reduction? Expect no, and a distinction from recoverable statutory family payments using current guidance.
4. A file was transmitted to HMRC. Is reporting complete? Expect acknowledgement and acceptance evidence, rejection handling and reconciliation.
5. EC says a worker was updated but payroll is unchanged. Expect source/mapping/effective-date/replication-monitor checks before calculation changes.
6. Net pay matches overall but two employees differ. Can parallel testing pass? Expect employee-level reconciliation and investigation of offsetting errors.
7. Can an AI assistant approve an urgent bank file? Expect a human-controlled approval chain and segregation of duties.
8. What changes when moving from HCM Payroll to ECP? Expect verified product/operating responsibilities, supported integration, access, release and licensing analysis rather than a cosmetic system-name change.

Progress states: explored, practised, evidenced, reviewed, mastered. Learning completion is separate from scroll position and self-checks. Academy badges represent demonstrated academy outcomes; they are not SAP certification or statutory professional accreditation.

## Implementation evidence templates

### Configuration workbook

Object ID | business requirement | standard/model reference | proposed setting | rationale | applicable release | dependency | transport | expected result | actual result | reviewer | rollback. Record country grouping, actual schema, PCR and wage types from the learner's system; do not assume that workbook examples are universal delivered settings. Common SAP GUI tools such as PA20/PA30, PA03, PE01, PE02 and SPRO are orientation examples; availability and permissions must be confirmed for the system. Use approved configuration routes rather than direct table edits.

### Test specification

Test ID | requirement | tax year | employee fixture | source events and dates | preconditions | action | expected earnings/bases/deductions/net/employer cost | expected reporting/posting/payment | actual values | evidence link | defect | retest | approver. Include normal, boundary, negative, retroactive, duplicate, failure/recovery and year-transition tests. Derive expected statutory results independently of the configuration under test.

### Reconciliation pack

1. Population: eligible, processed, rejected, joiners and leavers.
2. Master data and input: source totals, accepted totals and exceptions.
3. Calculation: employee and wage-type totals, current period and year to date.
4. Cash: approved net pay versus payment file and bank response.
5. Finance: expenses, employer costs, employee deductions and liabilities.
6. Statutory: FPS/EPS values, acceptance and HMRC account reconciliation.
7. Pensions/third parties: deductions, employer contributions, remittance and provider response.
8. Sign-off: preparer, independent reviewer, exceptions and release authority.

### Architecture decision record

Context | options | decision drivers | selected option | rejected alternatives and rationale | product/version evidence | security | failure/recovery | service owner | non-functional measures | costs/assumptions | review date. Maintain a requirements-to-design-to-test traceability matrix.

### AMS handover acceptance

Landscape and access confirmed; configuration baseline accepted; interface inventory and monitoring tested; operating calendar agreed; incident severities and escalation defined; known errors recorded; backlog and risks assigned; legal-change owner named; recovery exercised; payroll/FI/Treasury/HMRC responsibilities signed off. Use service-specific SLA targets agreed with the business, not arbitrary universal resolution promises.

## Twelve architecture-stream viewpoints

| Stream | UK payroll portfolio viewpoint |
|---|---|
| Enterprise | Payroll capability, service outcomes and transformation roadmap |
| Business | Hire-to-pay value stream, policies, roles and approvals |
| Data | Effective dates, identifiers, ownership and retention |
| Application | EC, payroll engine, time, finance and employee-facing services |
| Technology | Release, tooling, jobs and approved runtime components |
| AI | Evidence-backed policy assistance with human approval |
| Security | Segregation, least privilege and sensitive-payroll access |
| UI-UX | Understandable payslip, accessible support and exception journeys |
| Infrastructure | Availability, connectivity and shared responsibility |
| Integration | Contracts, mapping, acknowledgements and recovery |
| Domain | UK payroll rules, calendar and reconciled calculations |
| Industry | Industrials shift pay and specialist sector extensions |

## Living learning ecosystem

Use Discover to investigate payroll experiences; Flow to model the service; Design and Build for decisions and controlled configuration; Validate for test evidence; Support and Run for operations; Secure and Govern for access and accountability; Measure, Sustain and Scale for improvement. These are reuse paths through the existing SuperLabs, not separate copies of the same lessons.

Keep an experiment journal: question → prediction → controlled input → observation → evidence → revised explanation. Encourage learners to propose alternative designs and challenge assumptions respectfully. Each month, review one real-world change using public guidance and synthetic data. Each quarter, refresh a portfolio challenge. Share only synthetic artefacts in public repositories. Learners can teach back through a short recording, whiteboard, written walkthrough or live role-play.

## Statutory currency and source boundaries

Reviewed 24 November 2026. Maintain tax-year-specific source fixtures rather than embedding unversioned rate constants in lessons. Before each cohort and tax-year transition, recheck HMRC, TPR, relevant employment guidance and applicable SAP Notes. Record approved law versus proposals and confirmed SAP delivery versus planned availability. Verify specialist Northern Ireland, cross-border, termination and benefit matters separately.

Current correction to the source outline: SSP is not recoverable from HMRC. For 2026–2027, new SSP rules require effective-date and transitional testing; lessons must not reuse the former waiting-day and earnings-limit assumptions as current universal rules. Parental statutory payments have separate recovery provisions. See sources S1–S3. The curriculum intentionally does not reproduce comprehensive rates or full SAP KBA content.

Other clarifications: P45 is a leaving process, not simply an annual form; PCR execution depends on schema flow and grouping logic, not a universal direct assignment to every employee subgroup; CIS is a specialist subcontractor process and should not be presented as ordinary employee payroll; bank-channel capabilities require an actual bank integration design.

## Sources and provenance

- S1 — [HMRC employer rates and thresholds 2026–2027](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027): statutory baseline and review checklist. Consult the source for actual rates.
- S2 — [HMRC SSP manual calculation](https://www.gov.uk/guidance/statutory-sick-pay-manually-calculate-your-employees-payments): current calculation and effective-date learning.
- S3 — [SSP absences crossing 6 April 2026](https://www.gov.uk/guidance/sickness-absences-that-start-before-and-end-on-or-after-6-april-2026): transition scenarios.
- S4 — [HMRC FPS reporting](https://www.gov.uk/running-payroll/reporting-to-hmrc): reporting on/before payday and timing exceptions.
- S5 — [HMRC EPS reporting](https://www.gov.uk/running-payroll/reporting-to-hmrc-eps): reductions and reporting lifecycle.
- S6 — [The Pensions Regulator employer guidance](https://www.thepensionsregulator.gov.uk/employers): assessment and ongoing duties.
- S7 — [SAP KBA 3123610 — PY-GB RTI User Guide](https://userapps.support.sap.com/sap/support/knowledge/en/3123610): public preview reviewed; full content requires SAP sign-in and was not accessed.
- S8 — [Original Notion curriculum](https://app.notion.com/p/148ce6de608980b383cafc776342404d): workshop/bootcamp intent and topic inventory, expanded and corrected here. Private source may require access.

A related user-owned UK ECP AMS checklist in Drive was reviewed for operational topic coverage. Its environment examples and rates were not treated as statutory authority, and its contents or access link are not republished here. All learning structure, fictional cases, experiments, rubrics and architecture outputs are original proposed curriculum design.

## Maintenance and publication

Source of truth for this published edition: CURRICULUM.md plus curriculum.json in this folder. index.html contains a readable, searchable edition. Changes to curriculum scope should update all three together. Keep a dated change log and obtain a payroll subject-matter review before teaching a statutory calculation or using a configuration guide in a real project.

Release v1.0, 24 November 2026: expanded the source workshop/bootcamp into 36 modules, six levels, three capstones, role routes, assessment and operations/architecture evidence. Independent educational material; no affiliation with SAP, HMRC or TPR is implied.
