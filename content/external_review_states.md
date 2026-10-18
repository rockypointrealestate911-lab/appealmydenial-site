# External Review by State — notes (verified 2026-10-04)

Companion to `external_review_states.json`. Built from the CMS state list (table dated 2024-07-09, AZ moved to "parallel" 2025-01-01), healthcare.gov, and each state's insurance-department page or statute. Official .gov sources were preferred; where a .gov site blocked fetching, statutes/regulations or another official page were used instead and the row's note says so. Gap-closing pass 2026-10-04 closed 9 of the 10 open rows; only SC remains `fully_verified: false`.

## What external review does NOT cover (route these users elsewhere)

- **Self-funded (ERISA) employer plans** — the state process does not apply. These plans use the **federal external review** route: either the HHS-administered process (MAXIMUS, 1-888-866-6205, https://externalappeal.cms.gov/ferpportal) or a private accredited IRO the employer contracted with; the final denial letter says which. Deadline 4 months, no fee, expedited 72 hours. Self-funded church plans and non-federal governmental plans also use the federal route.
- **Medicare Advantage / Part D** — not external review. Denials upheld by the plan are auto-forwarded to the **Independent Review Entity** (Maximus/C2C); the member calls 1-800-MEDICARE.
- **Original Medicare** — redetermination (MAC) then reconsideration (QIC), not external review.
- **Medicaid / CHIP managed care** — plan appeal, then a **state fair hearing** with the state Medicaid agency (some states also offer external medical review); not the insurance department.
- **FEHB (federal employees)** — OPM disputed-claims review, not state external review.
- **TRICARE, VA** — their own appeal systems.
- **Excepted benefits** (stand-alone dental/vision, fixed indemnity, short-term plans) — generally no ACA external review right; RI is an exception that lets them in for a higher fee.
- **Denials that are not about medical judgment or rescission** (e.g., you were never enrolled, premium not paid, benefit explicitly excluded by contract) — most states will reject the request as ineligible; a few (AZ, KY, OH, MD) route contractual/coverage denials to the insurance department itself instead of an IRO.

## Program type summary

- **46 states + DC run their own program** (CMS "NAIC-parallel" list).
- **5 states use the HHS-administered / IRO process:** **AL, FL, GA, TX, WI.** In these states the insurer picks either the MAXIMUS federal process or a private accredited IRO; the final denial letter tells the consumer which. Caveats: Texas (TDI form LHL009) and Wisconsin (OCI Independent Review) still run state IRO processes for state-regulated plans — show both routes.
- Territories: PR runs its own; AS, GU, MP, VI use the federal process (not in the JSON).

## Routing quirks worth encoding in the app

**Who the consumer sends the request to**
- Direct to the state agency: AK, AR, CA, CT, HI (via plan forms), ID, IL, IA, KS, ME (Bureau of Insurance), MD (as a complaint), MA (OPP), MI, MN (Commerce, or Health for MDH-regulated plans), MS, MO, NE, NV (OCHA), NH, NJ (Maximus), NM, NY, NC, ND (either), OK, PA, SD, UT, VT, VA, WV, DC (Ombudsman).
- To the INSURER, which forwards / assigns the IRO: AZ, CO, DE, IN, KY, LA, MT, OH, OR, RI, SC, TN, TX, WA, WI, WY.

**Agency is not the insurance department**
- CA: DMHC Help Center (CDI for CDI-regulated policies).
- DC: Office of Health Care Ombudsman and Bill of Rights.
- MA: Health Policy Commission, Office of Patient Protection.
- NV: Office for Consumer Health Assistance (Aging & Disability Services Division).
- NJ: Maximus Federal under contract to DOBI.
- RI: Office of the Health Insurance Commissioner (separate from DBR).

**Deadlines that differ from the 4-month ACA floor**
- Shorter/odd: SC 60 days (S.C. Code 38-71-1970, still 60 days in the 2025 code; expedited must be requested within 15 days, 38-71-1980). This conflicts with CMS listing SC as NAIC-parallel, since 45 CFR 147.136(c)(2)(vi) requires parallel states to allow at least 4 months; SCDOI Bulletin 2011-04 probably reconciles it but doi.sc.gov could not be fetched. Show 60 days to be safe. CT/ID/IN/KS/MT/NC/VA/WY 120 days, MI 127 days, HI 130 days.
- Longer: AK/NH/OH/OR/UT/WV 180 days, CA/MN/TN 6 months, ME 12 months (24-A M.R.S. 4312(1)).
- No state deadline (confirmed by reading the law): MO (RSMo 376.1385-376.1389, 20 CSR 100-5.020; DCI form 1073: "no time limitation under Missouri law") and WA (RCW 48.43.535, WAC 284-43A-140/-150, WAC 284-43-3110, OIC guide). `deadline_days` is null by design. In the UI, tell users to file within 4 months (the federal floor) and follow any deadline in the denial letter.
- TX: TDI rules (28 TAC 19.1711/19.1717, form LHL009) set no enrollee deadline for health plans; the 4 months comes from the federal rule for HHS-process states (45 CFR 147.136(d)(2)(i)).

**Consumer fees (everyone else: none or not stated)**
- HI $15 (refundable); WY $15 (waivable); KY $25 billed by IRE unless you win; MA $25 ($75/yr, waivable, refundable); NY up to $25 ($75/yr, waivable); ND up to $25 (insurer's option, refundable); RI up to $25 ($75/yr; $100 for excepted benefits); VT $25 (waivable).

**Expedited**
- Available in every state where the page addressed it (72 hours is typical; NJ 48 h, NC ~4 business days, OR 3 days, SC 3 business days, TX 3 days for life-threatening cases; ME/MN/DE 72 hours confirmed from statute/regulation 2026-10-04; VT not stated). Several states require a physician certification form (ID, NC, UT, NV, CO, PA) and some let you skip the internal appeal in emergencies (AK, KS, OK, VA cancer cases, IL combined process).

## Rows with nulls / lower confidence

Updated 2026-10-04 after the gap-closing pass.

| State | Null fields | Status / why |
|---|---|---|
| SC | fee (no cost: carrier pays, 38-71-2040) | **fully_verified: false.** 60-day statute vs. CMS NAIC-parallel listing (implies at least 4 months) unresolved; SCDOI Bulletin 2011-04 unreadable (doi.sc.gov blocks fetches). Phone 803-737-6160 and expedited (15 days to ask, 3 business days to decide) confirmed. |
| MO | deadline_days, fee | Verified. No state deadline exists (citations above); no cost per DCI form 1073 (TPA-hosted copy). |
| WA | deadline_days, fee | Verified. No state deadline exists (citations above); no cost per WAC 284-43A-140(4)(b). |
| AZ | fee | Verified from A.R.S. 20-2537 and DIFI agency directory. Phone now 602-364-2399 (DIFI Healthcare Appeals). "No fee" comes only from carrier-hosted copies of the DIFI packet (the statute is silent); difi.az.gov PDFs return 403. |
| NH | fee | Verified from RSA 420-J:5-a/5-c/5-e and CMS (phone). Expedited fax 603-271-1406 is from a mirrored NHID guide only (insurance.nh.gov returns 403). |
| DE, ME, MN, PA, TX | fee | Verified. Expedited confirmed for DE/ME/MN (72 h); PA phone 877-881-6388 added; TX deadline explained above. |

Fee is `null` wherever there is no consumer fee or the official page did not state one; most of those states charge nothing (insurer pays the IRO). Where the law says the carrier pays, the row's note says so.

## Key federal sources
- CMS state list: https://www.cms.gov/cciio/resources/files/external_appeals
- HHS-administered process: https://www.cms.gov/cciio/programs-and-initiatives/consumer-support-and-information/csg-ext-appeals-facts
- healthcare.gov external review: https://www.healthcare.gov/appeal-insurance-company-decision/external-review/
- HHS FERP deadline-extension notice: https://www.cms.gov/files/document/hhs-administered-ferp-deadline-extension-07-31-26.pdf
- Status re-checked 2026-10-04: the FERP was temporarily unavailable in July 2026 and reopened 2026-07-31. People whose deadline fell 7/1–8/3/2026 had until 2026-10-02, which has now passed. Requests filed before 7/1/2026 did not need resubmitting. https://externalappeal.cms.gov/ferpportal still works and redirects (302) to the live MAXIMUS portal https://maximusferp.my.site.com/FERP/s/. healthcare.gov still lists 1-888-866-6205, fax 1-888-866-6190, ferp@maximus.com and the Pittsford, NY address. The CMS facts page (last modified 2024-09-10) does not mention the 2026 pause.
