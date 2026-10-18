"""Guide content for appealmydenial.app/guides/.
Every fact here must trace to a source listed on the same article. Reviewed 2026-10-04.
"""

SRC = {
    "kff_aca": ("KFF: Claims Denials and Appeals in ACA Marketplace Plans in 2024 (Mar 2026)",
                "https://www.kff.org/patient-consumer-protections/claims-denials-and-appeals-in-aca-marketplace-plans-in-2024/"),
    "kff_ma": ("KFF: Medicare Advantage Insurers Made Nearly 53 Million Prior Authorization Determinations in 2024 (Jan 2026)",
               "https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/"),
    "cms_partc": ("CMS: Reconsideration by the Medicare Advantage (Part C) Health Plan",
                  "https://www.cms.gov/medicare/appeals-grievances/managed-care/reconsideration-advantage-health-plan-part-c"),
    "medicare_appeals": ("Medicare.gov: Appeals in Original Medicare",
                         "https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/original-medicare"),
    "cfr_405942": ("42 CFR 405.942 (time frame for filing a redetermination)",
                   "https://www.law.cornell.edu/cfr/text/42/405.942"),
    "cms_redet": ("CMS: Original Medicare (Fee-for-Service) Appeals — Redetermination",
                  "https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor"),
    "erisa": ("29 CFR 2560.503-1 (claims procedure for employer and ACA plans)",
              "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XXV/part-2560/section-2560.503-1"),
    "hcgov_internal": ("HealthCare.gov: Internal appeals",
                       "https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/"),
    "hcgov_external": ("HealthCare.gov: External review",
                       "https://www.healthcare.gov/appeal-insurance-company-decision/external-review/"),
    "cms_ext": ("CMS: External appeals — state programs and the federal process",
                "https://www.cms.gov/cciio/resources/files/external_appeals"),
    "cfr_438402": ("42 CFR 438.402 (Medicaid managed care appeals)",
                   "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.402"),
    "cfr_438408": ("42 CFR 438.408 (plan decision times and state fair hearing)",
                   "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.408"),
    "cfr_438420": ("42 CFR 438.420 (keeping benefits during an appeal)",
                   "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.420"),
    "cfr_147138": ("45 CFR 147.138 (patient protections, including emergency services without prior authorization)",
                   "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-147/section-147.138"),
    "nsa": ("CMS: No Surprises Act — know your rights",
            "https://www.cms.gov/medical-bill-rights/know-your-rights"),
    "nsa_helpdesk": ("CMS: Medical bill rights help — No Surprises Help Desk",
                     "https://www.cms.gov/medical-bill-rights/help/submit-a-complaint"),
    "x12": ("X12: Claim Adjustment Reason Codes",
            "https://x12.org/codes/claim-adjustment-reason-codes"),
    "ship": ("SHIP: State Health Insurance Assistance Programs (free Medicare counseling)",
             "https://www.shiphelp.org/"),
}

# hub tags: plan:<id> or reason:<id> or start
ARTICLES = [
# ---------------------------------------------------------------------------
{
"slug": "how-to-appeal-a-health-insurance-denial",
"tags": ["start"],
"title": "How to Appeal a Health Insurance Denial: 6 Steps That Work",
"h1": "How to appeal a health insurance denial",
"desc": "Your claim was denied. Here are the six steps to appeal it: find your deadline, learn the real reason, get the right papers, and send a letter that answers it.",
"minutes": 6,
"short": "<p><strong>Short answer:</strong> Find the date on your denial letter and work out your deadline first. Then find the exact reason for the denial, gather what answers it (usually a letter from your doctor), and send a written appeal to the address on the letter before the deadline. Most people never appeal, and many who do win.</p>",
"body": """
<h2>Why it's worth appealing</h2>
<p>Denials are common, and appeals are rare. In 2024, insurers on HealthCare.gov denied about 19% of in-network claims, but consumers appealed fewer than 1% of those denials. Insurers upheld 66% of the denials that were appealed, which means about a third were not upheld on that first appeal.</p>
<p>In Medicare Advantage, insurers fully or partly denied 7.7% of prior authorization requests in 2024. Only 11.5% of those denials were appealed, and 80.7% of the appealed denials were fully or partly overturned.</p>
<p>You can't win an appeal you don't file.</p>

<h2>Step 1: Find your deadline</h2>
<p>Your deadline depends on the type of plan you have, and it usually counts from the date printed on the denial letter:</p>
<ul>
<li><strong>Medicare Advantage:</strong> 65 days from the date of the notice.</li>
<li><strong>Original Medicare:</strong> 120 days from when you receive the Medicare Summary Notice.</li>
<li><strong>Marketplace (ACA) or job-based plan:</strong> 180 days from when you receive the denial.</li>
<li><strong>Medicaid managed care:</strong> 60 days from the date on the notice.</li>
</ul>
<p>If your letter states its own deadline, use whichever date comes first. Our <a href="/deadline/">free deadline calculator</a> does the math for you.</p>

<h2>Step 2: Find the real reason</h2>
<p>Every appeal has to answer the reason the plan gave. Look for the sentence that starts "We denied this because…" and for any code like CO-197 or CO-50. Most denials fall into one of these groups:</p>
<ul>
<li><a href="/guides/not-medically-necessary-denial/">Not medically necessary</a></li>
<li><a href="/guides/prior-authorization-denial/">No prior authorization</a></li>
<li><a href="/guides/not-covered-denial/">Not a covered benefit</a></li>
<li><a href="/guides/out-of-network-denial/">Out of network</a></li>
<li>Missing or wrong information, which the provider's billing office can often fix with a corrected claim</li>
</ul>
<p>Not sure what your letter says? Read <a href="/guides/how-to-read-a-denial-letter/">how to read a denial letter</a>.</p>

<h2>Step 3: Decide if it's urgent</h2>
<p>If waiting could seriously harm your health, for example during ongoing treatment, call your plan today and ask for an <strong>expedited (fast) appeal</strong>. Plans generally have to decide those within 72 hours.</p>
<p class="answer"><strong>On Medicare and being discharged?</strong> If you're being discharged from the hospital, or your skilled nursing, home health or rehab care is ending, don't call your plan. Call the Quality Improvement Organization (QIO) listed on your notice right away. For a hospital discharge, call before you leave the hospital.</p>

<h2>Step 4: Gather what answers the reason</h2>
<ul>
<li>A copy of the denial letter.</li>
<li>For medical necessity denials: a <strong>letter of medical necessity</strong> from your doctor that answers the plan's reason point by point, plus office notes and test results.</li>
<li>For coverage denials: the page of your plan documents that covers the service.</li>
<li>You can ask the plan for free copies of the documents and the clinical criteria it used to deny you.</li>
</ul>

<h2>Step 5: Write and send the appeal</h2>
<p>Keep it short and specific. Name the claim, quote the reason, answer it, list what you enclosed, and ask the plan to overturn the denial. Send it to the appeals address on the denial letter, and keep a copy and proof of the date you sent it.</p>

<h2>Step 6: If the plan says no again</h2>
<p>Most plans have a next level. For Marketplace and many job-based plans, that's an <a href="/guides/external-review/">independent external review</a>, where reviewers outside your insurance company decide. In Medicare Advantage, a denial of a medical service that the plan upholds is sent on to an independent reviewer automatically. For prescription drugs, you have to request it yourself. <a href="/states/">Find your state's program</a>.</p>
""",
"faq": [
("How long do I have to appeal a health insurance denial?",
 "It depends on your plan: 65 days for Medicare Advantage, 120 days for Original Medicare, 180 days for Marketplace and most job-based plans, and 60 days for Medicaid managed care. If your letter states a different deadline, use the earlier date."),
("Do I need a lawyer to appeal?",
 "No. Most appeals are filed by patients or family members with a letter and supporting records. For complicated cases, free help is available from your state insurance department's consumer line or, for Medicare, your State Health Insurance Assistance Program (SHIP)."),
("What are my chances of winning?",
 "There is no single number. In KFF's 2024 data, insurers upheld 66% of appealed Marketplace denials, so about a third were not upheld on that appeal. In Medicare Advantage, 80.7% of appealed prior authorization denials were fully or partly overturned."),
],
"related": ["how-to-read-a-denial-letter", "not-medically-necessary-denial", "external-review"],
"sources": ["kff_aca", "kff_ma", "cms_partc", "cfr_405942", "erisa", "cfr_438402", "hcgov_internal"],
},
# ---------------------------------------------------------------------------
{
"slug": "how-to-read-a-denial-letter",
"tags": ["start"],
"title": "How to Read a Health Insurance Denial Letter (Line by Line)",
"h1": "How to read a health insurance denial letter",
"desc": "Where to find the five things that matter on a denial letter: the date, the reason, the codes, the deadline and the appeals address.",
"minutes": 5,
"short": "<p><strong>Short answer:</strong> Find five things: the <strong>date of the notice</strong>, the <strong>reason</strong> for the denial, any <strong>codes</strong> (like CO-197), the <strong>deadline</strong> to appeal, and the <strong>address</strong> where appeals go. Those five tell you what to argue and when it's due.</p>",
"body": """
<h2>1. The date of the notice</h2>
<p>Usually near the top, labeled "Notice date," "Date of this notice," or just a date under the letterhead. Your appeal deadline almost always counts from this date or from the day you received the letter. Write down both.</p>

<h2>2. The reason</h2>
<p>Look for a section called "Why we denied your request," "Reason for denial," or "Explanation." Copy the exact words. Your appeal has to answer this sentence, not the denial in general.</p>

<h2>3. The codes</h2>
<p>Some Explanation of Benefits forms, and most provider billing statements, show a code made of two letters and a number, such as <strong>CO-197</strong>. Your plan's own letter may use its own codes instead. The letters are a "group code." CO means the provider's contract with the plan applies, and PR means the amount is patient responsibility. The number is a standard Claim Adjustment Reason Code. A few common ones:</p>
<ul>
<li><strong>197:</strong> prior authorization was missing. <a href="/guides/prior-authorization-denial/">What to do</a></li>
<li><strong>50:</strong> the plan says the service wasn't medically necessary. <a href="/guides/not-medically-necessary-denial/">What to do</a></li>
<li><strong>96:</strong> non-covered charge. <a href="/guides/not-covered-denial/">What to do</a></li>
<li><strong>16:</strong> the claim is missing information or has a billing error, which the provider's billing office can often fix.</li>
<li><strong>29:</strong> the claim was filed after the plan's time limit. That's usually the provider's problem to fix, not yours.</li>
</ul>

<h2>4. The deadline</h2>
<p>Look in "Your appeal rights" or "If you disagree." It will say something like "within 65 days of the date of this notice" or "within 180 days of receiving this notice." If it counts from when you <em>received</em> the letter, note the day it arrived, or count from the notice date to be safe. <a href="/deadline/">Check your deadline here</a>.</p>

<h2>5. The appeals address</h2>
<p>The letter tells you where to send an appeal, and sometimes a fax number or online portal. Send it there, not to the general customer service address.</p>

<h2>Also worth noting</h2>
<ul>
<li><strong>Plan type.</strong> "Medicare Advantage," "Marketplace," "employer plan," or "Medicaid" changes your deadline and your next steps.</li>
<li><strong>Who decided.</strong> Some letters say a physician reviewer made the decision. That helps you ask for a reviewer in the same specialty on appeal.</li>
<li><strong>Urgent language.</strong> If you're in ongoing treatment, ask for an expedited (72-hour) appeal.</li>
</ul>
""",
"faq": [
("What does CO mean on a denial?",
 "CO is a group code meaning 'contractual obligation': the adjustment is governed by the provider's contract with the plan. PR means 'patient responsibility.' The number after it is the standard reason code."),
("Is an Explanation of Benefits (EOB) the same as a denial letter?",
 "Not exactly. An EOB explains how a claim was processed and may show a denial and its codes. A formal denial notice also explains your appeal rights and deadline. If you only have an EOB, call the plan and ask for the written denial notice."),
],
"related": ["how-to-appeal-a-health-insurance-denial", "prior-authorization-denial", "not-medically-necessary-denial"],
"sources": ["x12", "erisa", "cms_partc"],
},
# ---------------------------------------------------------------------------
{
"slug": "medicare-advantage-appeal",
"tags": ["plan:medicare_advantage"],
"title": "Medicare Advantage Denial Appeal: 65-Day Deadline & Steps",
"h1": "How to appeal a Medicare Advantage denial",
"desc": "Medicare Advantage gives you 65 days to ask for a reconsideration. Here's how to file, how fast the plan must answer, and what happens if it says no again.",
"minutes": 6,
"short": "<p><strong>Short answer:</strong> Ask your plan for a <strong>reconsideration</strong> within <strong>65 days</strong> of the date on the denial notice. If it's urgent, ask for a fast decision within 72 hours. If the plan still says no, it must send your case to an independent reviewer automatically.</p>",
"body": """
<h2>The odds are on your side</h2>
<p>In 2024, Medicare Advantage insurers fully or partly denied 4.1 million prior authorization requests (7.7%). Only 11.5% of those denials were appealed, but <strong>80.7% of the appealed denials were fully or partly overturned</strong>.</p>

<h2>Your deadline: 65 days</h2>
<p>You have 65 days from the date of the notice to request a reconsideration. If you miss it, you can ask for more time if you have a good reason. Don't count on that; file on time. <a href="/deadline/">Calculate your date</a>.</p>

<h2>How fast the plan must decide</h2>
<ul>
<li><strong>Expedited (urgent):</strong> 72 hours. If your doctor says waiting could seriously harm your health, the plan must speed it up.</li>
<li><strong>Service you haven't received yet:</strong> 30 days (the plan can extend up to 14 days in some cases).</li>
<li><strong>Part B drug:</strong> 7 days.</li>
<li><strong>Payment for care you already got:</strong> 60 days.</li>
</ul>

<h2>How to file</h2>
<ol>
<li>Follow the instructions on the denial notice. Most plans accept a written request by mail or fax, and some take requests by phone or online.</li>
<li>Write a short letter that names the service, quotes the plan's reason, and answers it.</li>
<li>Include a letter from your doctor and the records that support it. For a "not medically necessary" denial, this is the most important piece. <a href="/guides/not-medically-necessary-denial/">See how to answer it</a>.</li>
<li>Keep a copy and proof of the date you sent it.</li>
</ol>
<p>Your doctor can also request the reconsideration for you on a request for a service.</p>

<h2>If the plan says no again</h2>
<p>If the plan upholds its denial, fully or partly, it must automatically forward your case to an <strong>Independent Review Entity</strong>, an outside reviewer Medicare contracts with. You don't need to file anything for this step. Further levels exist after that, including a hearing before an administrative law judge for cases above a set dollar amount.</p>
<p class="answer"><strong>Prescription drug denials work differently.</strong> Everything on this page applies to medical services and Part B drugs. If your plan denied a <strong>prescription (Part D) drug</strong>, the steps and timelines are different, and if the plan says no again you must request the independent review yourself, within 65 days of the plan's decision.</p>

<h2>Free help</h2>
<p>Your State Health Insurance Assistance Program (SHIP) gives free, unbiased Medicare counseling and can help with appeals.</p>
""",
"faq": [
("How long does Medicare Advantage have to answer an appeal?",
 "72 hours for an expedited appeal, 30 days for a service you haven't received, 7 days for a Part B drug, and 60 days for a payment request."),
("Is a Medicare Advantage appeal the same as an Original Medicare appeal?",
 "No. Medicare Advantage starts with a reconsideration by your plan (65 days to file). Original Medicare starts with a redetermination by a Medicare contractor (120 days from receiving your Medicare Summary Notice)."),
("What happens if my Medicare Advantage plan denies my appeal?",
 "For medical services and Part B drugs, the plan must automatically send your case to an Independent Review Entity. For prescription (Part D) drug denials, you must request that review yourself within 65 days."),
],
"related": ["not-medically-necessary-denial", "prior-authorization-denial", "original-medicare-appeal"],
"sources": ["cms_partc", "kff_ma", "ship"],
},
# ---------------------------------------------------------------------------
{
"slug": "original-medicare-appeal",
"tags": ["plan:original_medicare"],
"title": "Original Medicare Appeal: How to Request a Redetermination",
"h1": "How to appeal an Original Medicare denial",
"desc": "In Original Medicare, the first appeal is a redetermination, due 120 days after you get your Medicare Summary Notice. Here's how to file and what comes next.",
"minutes": 5,
"short": "<p><strong>Short answer:</strong> Ask for a <strong>redetermination</strong> within <strong>120 days</strong> of receiving your Medicare Summary Notice. Medicare assumes you got it 5 days after its date, so count 125 days from the date printed on it. The contractor usually decides within 60 days.</p>",
"body": """
<h2>Where the denial shows up</h2>
<p>Original Medicare tells you about denied claims on your <strong>Medicare Summary Notice (MSN)</strong>, which comes every few months, or sooner on Medicare.gov. Find the claim, the reason, and the date of the notice.</p>

<h2>Your deadline: 120 days from receipt</h2>
<p>You have 120 days from the day you receive the MSN. Unless you can show otherwise, Medicare presumes you received it 5 days after the date on it. Counting 125 days from the printed date keeps you safe. <a href="/deadline/">Calculate it here</a>.</p>

<h2>How to file a redetermination</h2>
<ol>
<li>Circle the denied item on your MSN, write why you disagree, sign it, and send a copy to the contractor address on the MSN. Or use form CMS-20027, or a letter.</li>
<li>Include your name, Medicare number, the item or service, the dates of service, and why you think it should be paid.</li>
<li>Add any records that support you, such as a letter from your doctor.</li>
<li>Keep copies of everything.</li>
</ol>

<h2>What happens next</h2>
<ul>
<li><strong>Level 1, redetermination:</strong> the Medicare Administrative Contractor usually decides within 60 days.</li>
<li><strong>Level 2, reconsideration:</strong> if you disagree, ask a Qualified Independent Contractor within 180 days of the redetermination decision.</li>
<li>Further levels include an administrative law judge hearing for cases above a set dollar amount.</li>
</ul>

<h2>Free help</h2>
<p>Your State Health Insurance Assistance Program (SHIP) offers free, one-on-one Medicare counseling.</p>
""",
"faq": [
("How long do I have to appeal an Original Medicare claim?",
 "120 days from the day you receive the Medicare Summary Notice. Medicare presumes you received it 5 days after its date."),
("What is a redetermination?",
 "It's the first level of appeal in Original Medicare: a new look at your claim by the Medicare Administrative Contractor that processed it."),
],
"related": ["medicare-advantage-appeal", "how-to-appeal-a-health-insurance-denial", "how-to-read-a-denial-letter"],
"sources": ["cfr_405942", "medicare_appeals", "cms_redet", "ship"],
},
# ---------------------------------------------------------------------------
{
"slug": "aca-marketplace-appeal",
"tags": ["plan:aca_marketplace"],
"title": "Marketplace (ACA) Plan Denial Appeal: 180 Days & Next Steps",
"h1": "How to appeal a Marketplace (ACA) plan denial",
"desc": "If your HealthCare.gov or state Marketplace plan denied a claim, you have 180 days for an internal appeal, then the right to an independent external review.",
"minutes": 6,
"short": "<p><strong>Short answer:</strong> File an <strong>internal appeal</strong> with your insurer within <strong>180 days</strong> of receiving the denial. If the insurer says no again, you can ask for an <strong>independent external review</strong>, and that decision is binding on the insurer.</p>",
"body": """
<h2>Why appeal</h2>
<p>In 2024, Marketplace insurers on HealthCare.gov denied about 19% of in-network claims, yet consumers appealed fewer than 1% of the denials. Insurers upheld 66% of appealed denials, so about a third were not upheld at that first step. External review is a separate chance after that.</p>

<h2>Step 1: Internal appeal, within 180 days</h2>
<p>You have 180 days from receiving the denial notice to ask your insurer to reconsider. <a href="/deadline/">Check your date</a>. The insurer must decide:</p>
<ul>
<li><strong>Urgent care:</strong> within 72 hours.</li>
<li><strong>Service not yet received:</strong> within 30 days.</li>
<li><strong>Service already received:</strong> within 60 days.</li>
</ul>
<p>You have the right to see your claim file and the documents the insurer relied on, free of charge, and to submit your own evidence.</p>

<h2>Step 2: External review</h2>
<p>If the internal appeal fails, you can ask for an <a href="/guides/external-review/">external review</a> by an independent reviewer. Depending on your state, it's run by the state or by the federal process. You generally have 4 months from the final denial, though some states allow longer. <a href="/states/">Find your state</a>.</p>
<p>If your situation is urgent, you can ask for an expedited external review at the same time as an urgent internal appeal.</p>

<h2>What to send</h2>
<ul>
<li>A short letter naming the claim, quoting the reason, and answering it.</li>
<li>Your doctor's letter and records for medical necessity denials. <a href="/guides/not-medically-necessary-denial/">How to answer that reason</a>.</li>
<li>A copy of the denial and of your insurance card.</li>
</ul>
""",
"faq": [
("How long do I have to appeal a Marketplace plan denial?",
 "180 days from receiving the denial notice for the internal appeal. After a final denial, you generally have 4 months to request external review, longer in some states."),
("Is the external review decision final?",
 "If the external reviewer overturns the denial, the insurer must accept it and pay or cover the service."),
],
"related": ["external-review", "employer-plan-appeal", "not-medically-necessary-denial"],
"sources": ["kff_aca", "erisa", "hcgov_internal", "hcgov_external", "cms_ext"],
},
# ---------------------------------------------------------------------------
{
"slug": "employer-plan-appeal",
"tags": ["plan:employer"],
"title": "Employer Health Plan Denial: How to Appeal (180 Days)",
"h1": "How to appeal a denial from a health plan through your job",
"desc": "Job-based health plans must give you 180 days to appeal a denied claim. Here's how the process works, including external review for self-funded plans.",
"minutes": 6,
"short": "<p><strong>Short answer:</strong> You have <strong>180 days</strong> from receiving the denial to file an appeal with the plan. If it still says no, most plans then offer an <strong>independent external review</strong>. Your denial letter says which review process applies.</p>",
"body": """
<h2>Step 1: The plan's internal appeal</h2>
<p>Federal rules give you at least 180 days after you receive a denial to appeal. <a href="/deadline/">Check your date</a>. The plan must decide:</p>
<ul>
<li><strong>Urgent care:</strong> within 72 hours.</li>
<li><strong>Service not yet received:</strong> within 30 days (15 days per level if the plan has two levels).</li>
<li><strong>Service already received:</strong> within 60 days (30 days per level if two levels).</li>
</ul>
<p>You're entitled to free copies of the documents and records relevant to your claim, including the plan provisions and any clinical criteria used.</p>

<h2>Step 2: External review, and which kind</h2>
<p>Which external review you get depends on how the plan is funded:</p>
<ul>
<li><strong>Fully insured plans</strong> (the employer buys coverage from an insurance company) usually use your <a href="/states/">state's external review program</a>.</li>
<li><strong>Self-funded plans</strong> (common at large employers) usually use an accredited independent reviewer that the plan hires under federal rules. Plans run by government employers may use the federal HHS process instead.</li>
</ul>
<p>Your final denial letter must explain the external review option and deadline. If you aren't sure, ask your HR or benefits office whether the plan is "fully insured" or "self-funded."</p>
<p>Plans that were in place before March 23, 2010 and haven't changed much ("grandfathered" plans) may not have to offer external review.</p>

<h2>What to send</h2>
<ul>
<li>A short letter that quotes the reason and answers it.</li>
<li>For coverage disputes, the page of the Summary Plan Description (SPD) that supports you. <a href="/guides/not-covered-denial/">How to answer a "not covered" denial</a>.</li>
<li>For medical necessity, your doctor's letter and records.</li>
</ul>
""",
"faq": [
("How long do I have to appeal an employer health plan denial?",
 "At least 180 days from receiving the denial. Check your letter, and use the earlier date if it states a shorter one."),
("What's the difference between fully insured and self-funded?",
 "A fully insured plan is bought from an insurance company and is regulated by your state. A self-funded plan pays claims from the employer's own funds and follows federal rules; its external review is usually done by an independent reviewer the plan hires."),
],
"related": ["external-review", "not-covered-denial", "aca-marketplace-appeal"],
"sources": ["erisa", "hcgov_external", "cms_ext"],
},
# ---------------------------------------------------------------------------
{
"slug": "medicaid-appeal",
"tags": ["plan:medicaid"],
"title": "Medicaid Plan Denial Appeal: 60 Days, Then a Fair Hearing",
"h1": "How to appeal a Medicaid managed care denial",
"desc": "If your Medicaid plan denies or cuts a service, you have 60 days to appeal, then a state fair hearing. Act within 10 days to keep services.",
"minutes": 5,
"short": "<p><strong>Short answer:</strong> Appeal to your Medicaid plan within <strong>60 days</strong> of the date on the notice. If the plan is stopping or reducing a service you already get, appeal <strong>within 10 days</strong> and ask to keep your benefits while you appeal. If the plan says no again, ask for a <strong>state fair hearing</strong>.</p>",
"body": """
<h2>Your deadline: 60 days</h2>
<p>Medicaid managed care plans must give you 60 days from the date on the notice to file an appeal. <a href="/deadline/">Calculate your date</a>.</p>

<h2>Keeping your services during the appeal</h2>
<p>If the plan is ending, cutting, or suspending a service you're already receiving, you can usually keep getting it while you appeal. You need to file the appeal and ask to continue benefits on time, within 10 days of when the notice was sent or by the date the change takes effect, whichever is later. Your notice gives the exact date.</p>
<p>If you lose the appeal, the plan may be allowed to recover the cost of services you received while the appeal was pending. Ask the plan or a legal aid office about this before you decide.</p>

<h2>How fast the plan must decide</h2>
<ul>
<li><strong>Standard appeal:</strong> no more than 30 days (the plan can extend up to 14 days if you ask or it shows the delay is in your interest).</li>
<li><strong>Expedited appeal</strong> (when waiting could seriously harm your health): 72 hours.</li>
</ul>

<h2>Next: the state fair hearing</h2>
<p>If the plan upholds its decision, you can ask your state Medicaid agency for a <strong>state fair hearing</strong>. States set the deadline, between 90 and 120 days from the plan's decision, and your notice will say which. Some states also offer an external medical review.</p>
<p>To keep receiving a service through the fair hearing, you must request the hearing and ask to continue benefits within 10 days of the plan's appeal decision.</p>

<h2>Free help</h2>
<p>Your state's Medicaid ombudsman or legal aid office can often help for free. The number is usually on your plan's notice.</p>
""",
"faq": [
("How long do I have to appeal a Medicaid denial?",
 "60 days from the date on the notice for an appeal to your managed care plan. To keep an existing service during the appeal, file much sooner, generally within 10 days."),
("What is a state fair hearing?",
 "A hearing run by your state Medicaid agency, not the plan, where an impartial hearing officer decides. You can request it after the plan upholds its denial."),
],
"related": ["how-to-appeal-a-health-insurance-denial", "how-to-read-a-denial-letter", "not-medically-necessary-denial"],
"sources": ["cfr_438402", "cfr_438408", "cfr_438420"],
},
# ---------------------------------------------------------------------------
{
"slug": "prior-authorization-denial",
"tags": ["reason:prior_auth"],
"title": "Denied for No Prior Authorization (CO-197)? How to Appeal",
"h1": "Denied because prior authorization wasn't obtained",
"desc": "A CO-197 'no prior authorization' denial is often winnable. Emergency care generally needs no prior authorization, and the provider often owns the mistake.",
"minutes": 5,
"short": "<p><strong>Short answer:</strong> If it was an <strong>emergency</strong>, say so. Most plans can't require prior authorization for emergency care. If it was scheduled care, ask the plan to review it for <strong>retroactive authorization</strong> on its medical merits, and get the provider who ordered it involved, since getting approval was usually their job.</p>",
"body": """
<h2>What the codes mean</h2>
<p>These Claim Adjustment Reason Codes usually mean an approval was missing or didn't match:</p>
<ul>
<li><strong>197:</strong> precertification, authorization, or notification absent.</li>
<li><strong>15:</strong> authorization number missing, invalid, or doesn't apply.</li>
<li><strong>198:</strong> precertification or authorization exceeded.</li>
</ul>

<h2>If it was emergency care</h2>
<p>Under federal rules, Marketplace and most job-based plans can't require prior authorization for emergency services, whether or not the hospital is in network. Your appeal should say plainly: this was emergency care, here's what was happening, and emergency services don't require prior authorization. Ask the plan to process it as emergency care. The standard is whether a reasonable person with average health knowledge would have believed it was an emergency, not the final diagnosis.</p>

<h2>If it was scheduled care</h2>
<ul>
<li><strong>Ask for retroactive review.</strong> Ask the plan to review the service on its medical merits as if authorization had been requested.</li>
<li><strong>Point to who was responsible.</strong> Getting approval is usually the ordering provider's job. If the provider is in network, its contract with the plan often bars it from billing you for its own missed authorization. Ask the provider's billing office directly.</li>
<li><strong>If the provider did ask,</strong> get the date of their request. A plan that didn't answer a timely request has a problem of its own.</li>
</ul>

<h2>Medicare Advantage</h2>
<p>In Medicare Advantage, appeals of prior authorization denials succeed often. In 2024, 80.7% of appealed prior authorization denials were fully or partly overturned. <a href="/guides/medicare-advantage-appeal/">How to appeal in Medicare Advantage</a>.</p>
""",
"faq": [
("What does denial code CO-197 mean?",
 "CO-197 means precertification, authorization, or notification was absent: the plan says no approval was on file before the service. CO means the provider's contract with the plan governs the adjustment."),
("Can I be billed if my in-network provider didn't get prior authorization?",
 "Often not. Many network contracts bar providers from billing patients when they failed to get a required authorization. Ask the provider's billing office and your plan before paying."),
("Does emergency care need prior authorization?",
 "Generally no. Federal rules bar Marketplace and most job-based plans from requiring prior authorization for emergency services."),
],
"related": ["medicare-advantage-appeal", "out-of-network-denial", "how-to-read-a-denial-letter"],
"sources": ["x12", "cfr_147138", "kff_ma", "erisa"],
},
# ---------------------------------------------------------------------------
{
"slug": "not-medically-necessary-denial",
"tags": ["reason:medical_necessity"],
"title": "Denied as Not Medically Necessary? How to Win the Appeal",
"h1": "Denied as “not medically necessary”",
"desc": "A 'not medically necessary' (CO-50) denial is a judgment call, and those get reversed. The key: a doctor's letter that answers the plan's criteria.",
"minutes": 6,
"short": "<p><strong>Short answer:</strong> Get a <strong>letter of medical necessity</strong> from your doctor that answers the plan's stated reason point by point, attach the records that prove it, and ask for the <strong>clinical criteria</strong> the plan used. Ask for a reviewer in the same specialty, and ask your doctor to request a <strong>peer-to-peer</strong> call with the plan's reviewer.</p>",
"body": """
<h2>What the plan is really saying</h2>
<p>"Not medically necessary" means a reviewer decided your records didn't meet the plan's rules for that service. Often the denial names exactly what was missing, for example "at least six weeks of conservative treatment before advanced imaging." Common codes:</p>
<ul>
<li><strong>50:</strong> not deemed a medical necessity by the payer.</li>
<li><strong>56:</strong> not deemed proven to be effective by the payer.</li>
</ul>

<h2>The four things that win these</h2>
<ol>
<li><strong>A letter of medical necessity</strong> from the doctor who ordered the service. It should quote the plan's reason and answer it directly: what you've already tried, for how long, what happened, and why this service is needed now.</li>
<li><strong>The records that prove it:</strong> office notes, test results, and a list of earlier treatments with dates.</li>
<li><strong>The plan's own criteria.</strong> Ask for a free copy of the clinical policy used to deny you, then show how you meet it.</li>
<li><strong>The right reviewer.</strong> Ask that the appeal be decided by a physician in the same or a similar specialty who wasn't part of the first decision, and ask your doctor to request a peer-to-peer review.</li>
</ol>

<h2>Give your doctor's office what it needs</h2>
<p>Doctors' offices handle many of these. Make it easy: give them the denial letter, the exact reason quoted, your deadline, and the date you need their letter by, about two weeks before the deadline.</p>

<h2>If it's urgent</h2>
<p>If waiting could seriously harm your health, ask for an expedited appeal. Plans generally decide those within 72 hours.</p>

<h2>If the plan says no again</h2>
<p>Medical necessity denials are exactly what <a href="/guides/external-review/">independent external review</a> is for. In Medicare Advantage, the plan sends upheld denials of medical services to an independent reviewer automatically.</p>
""",
"faq": [
("What is a letter of medical necessity?",
 "A letter from your doctor explaining why a service is needed for your condition, ideally answering the plan's specific reason for the denial and pointing to your records."),
("What is a peer-to-peer review?",
 "A phone call between your doctor and the plan's medical reviewer to discuss the case. Many plans offer it, and it can resolve a denial quickly."),
("What does denial code CO-50 mean?",
 "CO-50 means the payer did not deem the service a medical necessity. CO means the provider's contract with the plan governs the adjustment."),
],
"related": ["external-review", "medicare-advantage-appeal", "prior-authorization-denial"],
"sources": ["x12", "erisa", "cms_partc", "hcgov_external"],
},
# ---------------------------------------------------------------------------
{
"slug": "not-covered-denial",
"tags": ["reason:not_covered"],
"title": "Denied as Not Covered (CO-96)? How to Appeal an Exclusion",
"h1": "Denied as “not a covered benefit”",
"desc": "A 'not covered' (CO-96) denial is a fight over the plan's own words. How to use your plan documents, and what to do about 'experimental' denials.",
"minutes": 5,
"short": "<p><strong>Short answer:</strong> Ask the plan which <strong>exact provision</strong> it relied on, then read that section of your plan documents. Appeal by showing the service fits a covered category, or that the exclusion doesn't apply to your situation. For “experimental” denials, your doctor's evidence matters most.</p>",
"body": """
<h2>What the codes mean</h2>
<ul>
<li><strong>96:</strong> non-covered charge.</li>
<li><strong>204:</strong> not covered under the patient's current benefit plan.</li>
<li><strong>119:</strong> benefit maximum for this period has been reached.</li>
<li><strong>55:</strong> procedure deemed experimental or investigational by the payer.</li>
</ul>

<h2>Get the plan's words</h2>
<p>Ask for the specific plan provision the denial relies on. You're entitled to free copies of the documents relevant to your claim. Then read your <strong>Summary of Benefits and Coverage</strong>, and for job-based plans the <strong>Summary Plan Description</strong>, around that section.</p>

<h2>Ways these get overturned</h2>
<ul>
<li><strong>Wrong category.</strong> The service may be covered under a different benefit. For example, a device may be excluded under one heading but covered as part of treatment under another.</li>
<li><strong>Exception language.</strong> Many exclusions carry exceptions, such as "except when medically necessary for…" Quote them.</li>
<li><strong>Limit miscounted.</strong> For "maximum reached," ask for the count of visits or units the plan applied and check it against your records.</li>
<li><strong>"Experimental" that isn't.</strong> If the treatment is FDA-approved for your condition or is standard care under medical guidelines, your doctor's letter should say so and cite the evidence.</li>
</ul>

<h2>Be realistic</h2>
<p>Some exclusions are clear and hold up, for example a plan that plainly excludes hearing aids for adults. Even then, a short appeal costs little and creates a record. And some states now require certain plans to cover services that the plan document excludes, so check with your state insurance department.</p>

<h2>Next steps</h2>
<p>External review generally covers denials based on medical judgment, including "experimental" denials. Pure contract disputes may be handled differently depending on your state. <a href="/states/">Check your state</a>.</p>
""",
"faq": [
("What does denial code CO-96 mean?",
 "CO-96 means non-covered charge: the plan says the service isn't a covered benefit. CO means the provider's contract with the plan governs the adjustment."),
("Can I appeal an exclusion in my plan?",
 "Yes. You can argue the service fits a covered category or that the exclusion doesn't apply. Ask the plan for the exact provision it used first."),
],
"related": ["employer-plan-appeal", "external-review", "how-to-read-a-denial-letter"],
"sources": ["x12", "erisa", "hcgov_external"],
},
# ---------------------------------------------------------------------------
{
"slug": "out-of-network-denial",
"tags": ["reason:out_of_network"],
"title": "Out-of-Network Denial or Surprise Bill? Know Your Rights",
"h1": "Denied or billed because a provider was out of network",
"desc": "The No Surprises Act limits surprise out-of-network bills for emergencies, many services at in-network hospitals, and air ambulances. How to use it.",
"minutes": 5,
"short": "<p><strong>Short answer:</strong> For <strong>emergency care</strong>, and for many out-of-network clinicians at an <strong>in-network hospital or facility</strong>, federal law limits you to in-network cost sharing and bars balance billing. Appeal to your plan to reprocess the claim, and contact the No Surprises Help Desk at <strong>1-800-985-3059</strong> if you're billed anyway.</p>",
"body": """
<h2>When you're protected</h2>
<p>Since January 1, 2022, the federal No Surprises Act protects people in most private health plans from surprise bills for:</p>
<ul>
<li><strong>Emergency services,</strong> even at an out-of-network hospital or from out-of-network doctors there.</li>
<li><strong>Non-emergency services from out-of-network providers at an in-network hospital or surgery center,</strong> Some providers can ask you to sign away this protection in advance, but never for emergency medicine, anesthesiology, pathology, radiology, neonatology, assistant surgeons, hospitalists, intensivists, or diagnostic services such as lab work, and never when no in-network provider was available.</li>
<li><strong>Air ambulance</strong> services from out-of-network providers.</li>
</ul>
<p>In these cases you pay no more than your in-network cost sharing, and the provider can't bill you the difference.</p>

<h2>What to do</h2>
<ol>
<li><strong>Appeal to your plan</strong> and ask it to reprocess the claim at in-network cost sharing under the No Surprises Act.</li>
<li><strong>Tell the provider</strong> in writing that the bill is covered by the No Surprises Act, and don't pay the balance-billed amount while it's sorted out.</li>
<li><strong>File a complaint</strong> with the No Surprises Help Desk (1-800-985-3059) if you're balance billed.</li>
<li><strong>If the plan won't fix it,</strong> disputes over whether the plan followed the No Surprises Act can go to <a href="/guides/external-review/">independent external review</a>.</li>
</ol>

<h2>When there was no in-network option</h2>
<p>If you used an out-of-network provider because no in-network provider was reasonably available, ask your plan for a <strong>network adequacy exception</strong>, meaning coverage at in-network rates. Describe how far you'd have had to travel or how long you'd have had to wait.</p>

<h2>Codes you may see</h2>
<ul>
<li><strong>242:</strong> services not provided by network/primary care providers.</li>
<li><strong>243:</strong> services not authorized by network/primary care providers.</li>
</ul>
""",
"faq": [
("Does the No Surprises Act cover ground ambulances?",
 "No. The federal protections cover air ambulances, not ground ambulances, though some states have their own ground ambulance protections."),
("What number do I call about a surprise medical bill?",
 "The federal No Surprises Help Desk: 1-800-985-3059."),
],
"related": ["prior-authorization-denial", "aca-marketplace-appeal", "employer-plan-appeal"],
"sources": ["nsa", "nsa_helpdesk", "x12"],
},
# ---------------------------------------------------------------------------
{
"slug": "external-review",
"tags": ["start"],
"title": "External Review of a Health Insurance Denial: How It Works",
"h1": "How to request an independent external review",
"desc": "After your insurer's final no, an independent reviewer can overturn it, and the insurer must follow the decision. Who qualifies, deadlines, how to file.",
"minutes": 6,
"short": "<p><strong>Short answer:</strong> After your insurer denies your internal appeal, you can ask an <strong>independent reviewer</strong> to decide. You usually have <strong>4 months</strong> from the final denial (longer in some states). If the reviewer sides with you, the insurer must pay or cover the service.</p>",
"body": """
<h2>Who can use it</h2>
<p>External review applies to Marketplace plans and most job-based plans, for denials based on medical judgment (such as medical necessity, appropriateness, level of care, or "experimental" treatment) for rescissions of coverage, and for disputes about whether the plan followed the No Surprises Act. Some older "grandfathered" plans are exempt.</p>
<p>It doesn't apply to Medicare or Medicaid, which have their own processes. In Medicare Advantage, upheld denials of medical services go to an independent reviewer automatically; for prescription drugs you request it yourself. <a href="/guides/medicare-advantage-appeal/">See how</a>.</p>

<h2>State program or federal process</h2>
<p>Most states run their own external review program for plans they regulate. Five states, Alabama, Florida, Georgia, Texas and Wisconsin, use the federal process for many plans, and self-funded employer plans in every state generally use an accredited independent reviewer the plan hires under federal rules. Your final denial letter should tell you which applies. <a href="/states/">Find your state's program</a>.</p>

<h2>Deadlines and timing</h2>
<ul>
<li><strong>To file:</strong> generally 4 months from the final internal denial. Some states allow more, such as 6 months or 12 months, and a few allow less. Check your state's page.</li>
<li><strong>Standard decision:</strong> usually within 45 days.</li>
<li><strong>Expedited decision:</strong> within 72 hours when waiting could seriously jeopardize your health. You can request it at the same time as an urgent internal appeal.</li>
</ul>

<h2>The federal process</h2>
<p>The HHS-administered federal process is run by MAXIMUS Federal Services. You can file online through the federal external review portal, or call 1-888-866-6205. There's no fee.</p>

<h2>What to send</h2>
<ul>
<li>The final denial letter.</li>
<li>Your internal appeal and everything you sent with it.</li>
<li>Your doctor's letter of medical necessity, if you have one. New evidence can help.</li>
</ul>
""",
"faq": [
("Is external review free?",
 "In most states, and in the federal process, yes. A few states charge a small fee, generally $25 or less, that may be waived or refunded."),
("Does the insurer have to follow the external review decision?",
 "Yes. If the independent reviewer overturns the denial, the insurer must provide coverage or payment."),
("How long do I have to request external review?",
 "Generally 4 months after your insurer's final internal denial. Some states allow longer; check your state's page."),
],
"related": ["aca-marketplace-appeal", "employer-plan-appeal", "not-medically-necessary-denial"],
"sources": ["hcgov_external", "cms_ext", "erisa"],
},
]
