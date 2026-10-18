# Appeal — letter templates (v1)

Rules for every template:
- `{{field}}` = filled from the extracted letter or the context screen. `[YOUR …]` = a placeholder the user must fill; it stays visible and highlighted until they do. Never invent clinical facts, dates, or history.
- Tone: plain, firm, polite. No accusations, no "illegal," no "fraud," no threats. "I am requesting" and "I ask that you" — never "I demand."
- Every letter ends with: the enclosures list, "Please send your written decision to the address above," and the signature block. The app adds the copy line ("cc: {{provider_name}}") when the provider should see it.
- Footer (in-app only, not printed): "Appeal My Denial drafts this letter for you to review and send. It is not legal advice. Free help: your State Health Insurance Assistance Program (Medicare) or your state insurance department's consumer line."

---

## Shared header (all letters)

```
{{patient_name_or_[YOUR NAME]}}
[YOUR ADDRESS]
[YOUR PHONE]

{{today}}

{{insurer_name}}
{{appeals_address_from_letter_or_[APPEALS ADDRESS — on your denial letter]}}

Re: Request for {{appeal_level_label}}
Member: {{member_name}}    Member ID: {{member_id}}
Claim / reference number: {{claim_number}}
Service: {{service_description}}    Date of service: {{service_date}}
Provider: {{provider_name}}
Date of denial notice: {{notice_date}}
```

`appeal_level_label`: "internal appeal" (ACA/employer) · "reconsideration" (Medicare Advantage) · "redetermination" (Original Medicare) · "appeal" (Medicaid) · "expedited appeal" when urgent.

---

## 1. letter_administrative — missing or wrong information

```
I am writing about the denial of the claim above. Your notice dated {{notice_date}} gives the reason as "{{denial_reason_quoted}}."

This appears to be an information or processing issue rather than a coverage decision. {{#if missing_item}}The item you asked for, {{missing_item}}, is enclosed.{{else}}I have asked {{provider_name}} to send a corrected claim. [YOUR NOTE — what you were told is wrong, e.g., "the wrong member ID was used."]{{/if}}

I ask that you reprocess this claim with the enclosed information. If you treat this as a formal {{appeal_level_label}}, please consider this letter my timely request.
```

Enclosures: copy of the denial notice; {{missing_item}} if any; copy of insurance card (front and back).

---

## 2. letter_timely_filing — claim filed late

```
Your notice dated {{notice_date}} denies this claim because it was not filed within your time limit.

I received this service from {{provider_name}} on {{service_date}} and gave them my insurance information at the time. Filing the claim was the provider's responsibility. {{#if in_network}}Because {{provider_name}} is in your network, I understand their contract does not allow them to bill me for a claim they filed late, and I ask you to confirm that in your decision.{{/if}}

I ask that you reconsider the denial. If the provider has proof that the claim was submitted on time, I have asked them to send it to you directly.
```

Enclosures: copy of the denial notice. cc: {{provider_name}} (always).

---

## 3. letter_prior_auth — approval not obtained

Variant A, emergency care (`service_setting = emergency`):

```
Your notice dated {{notice_date}} denies this claim because prior authorization was not obtained.

This was emergency care. On {{service_date}} I went to {{provider_name}} for [YOUR WORDS — what was happening, e.g., "chest pain"]. Emergency services do not require prior authorization, and I ask that you process this claim as emergency care under my plan and under federal law.
```

Variant B, scheduled care:

```
Your notice dated {{notice_date}} denies this claim because prior authorization was not obtained.

{{#if provider_requested}}{{provider_name}} requested authorization on [DATE — ask your provider] and did not receive a timely decision.{{else}}Obtaining authorization was the responsibility of {{provider_name}}, who ordered the service. I was not told it was required.{{/if}}

I ask that you review this service for retroactive authorization on its merits. {{provider_name}} can provide the records showing why it was needed.
```

Enclosures: copy of the denial notice; {{#if emergency}}the emergency room record if available{{/if}}. cc: {{provider_name}}.

---

## 4. letter_not_covered — excluded or over a limit

```
Your notice dated {{notice_date}} denies this service as "{{denial_reason_quoted}}."

I ask that you reconsider. [YOUR PLAN'S WORDS — the section of your plan document or Summary of Benefits that covers this service, with page number. If you don't have it, write: "Please send me the specific plan provision you relied on, as I am entitled to request."]

{{#if experimental}}This treatment is [YOUR DOCTOR'S STATEMENT — that it is FDA-approved for this use, or standard of care]. A letter from {{provider_name}} is enclosed.{{/if}}

I also request copies of all documents, records, and plan provisions relevant to this decision, free of charge.
```

Enclosures: copy of the denial notice; relevant plan pages; doctor's letter if experimental.

---

## 5. letter_medical_necessity — not medically necessary

```
Your notice dated {{notice_date}} denies {{service_description}} as not medically necessary{{#if criteria_quoted}}, stating "{{criteria_quoted}}"{{/if}}.

My doctor, {{provider_name}}, ordered this service because [YOUR DOCTOR'S REASON — from their letter; leave for them to fill if you don't know]. A letter of medical necessity from my doctor and the related records are enclosed. They address the reason you gave.

I ask that you:
1. Overturn the denial and approve {{service_description}}.
2. Have this {{appeal_level_label}} reviewed by a physician in the same or a similar specialty who was not involved in the original decision.
3. Offer my doctor a peer-to-peer review with your medical reviewer.
4. Send me copies of the clinical criteria or policy you used to make this decision.

{{#if urgent}}Because delay could seriously harm my health, I request an expedited decision within 72 hours.{{/if}}
```

Enclosures: copy of the denial notice; letter of medical necessity from {{provider_name}}; [RECORDS — office notes, test results, prior treatments tried].

---

## 6. letter_out_of_network — out of network or balance bill

Variant A, emergency or in-network facility (No Surprises Act applies):

```
Your notice dated {{notice_date}} processed this claim as out of network.

{{#if emergency}}This was emergency care on {{service_date}}. Under the federal No Surprises Act, emergency services must be covered at in-network cost sharing regardless of the provider's network status.{{else}}I received this service at {{facility_name}}, an in-network facility. Under the federal No Surprises Act, ancillary services from out-of-network clinicians at an in-network facility must be covered at in-network cost sharing.{{/if}}

I ask that you reprocess this claim at in-network cost sharing and confirm that I cannot be balance billed for the difference.
```

Variant B, no in-network option (network adequacy):

```
Your notice dated {{notice_date}} processed this claim as out of network.

I used an out-of-network provider because no in-network provider was available [YOUR SITUATION — e.g., "within 50 miles" or "within 6 weeks"]. I ask that you cover this service at in-network cost sharing as a network-adequacy exception.
```

Enclosures: copy of the denial notice; any itemized bill from the provider.

---

## Doctor request (medical necessity, and experimental)

A half page the patient hands to the doctor's office. Printed separately; never sent to the insurer.

```
To: {{provider_name}} — billing and clinical staff
From: {{patient_name}}, date of birth [YOUR DATE OF BIRTH]
Re: Insurance denial — request for letter of medical necessity

My insurance, {{insurer_name}}, denied {{service_description}} on {{notice_date}} as not medically necessary. The reason they gave:
"{{denial_reason_quoted}}"
{{#if criteria_quoted}}Criteria they cited: "{{criteria_quoted}}"{{/if}}

I am appealing. My deadline is {{deadline_date}}. To give the appeal its best chance, please send me (or the plan directly, at {{appeals_address}}) by {{deadline_minus_14}}:
1. A letter of medical necessity that answers the reason above point by point.
2. The office notes, test results, and records of earlier treatments that support it.
3. If possible, a request for a peer-to-peer review with the plan's medical reviewer.

Claim number: {{claim_number}}    Member ID: {{member_id}}
Thank you.
```

---

## External review request (cover letter)

Used when the user marks a prior appeal as upheld. Routing from external_review_states.json (state process vs federal HHS process vs Medicare Advantage IRE, which is automatic).

```
I am requesting an external review of {{insurer_name}}'s final decision dated {{final_denial_date}}, which upheld the denial of {{service_description}}.

I completed the plan's internal appeal. My request is within the {{external_deadline_label}} allowed. {{#if urgent}}I request an expedited external review because delay could seriously jeopardize my health.{{/if}}

Enclosed are the final denial, my internal appeal and its enclosures, and {{#if doctor_letter}}my doctor's letter of medical necessity{{/if}}.
```
