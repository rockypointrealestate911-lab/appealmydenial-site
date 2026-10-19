"""Static site generator for appealmydenial.app.
Run from the repo root: python3 src/build.py && python3 src/build_legal.py
Writes guides/, deadline/, states/, assets/site.css, sitemap.xml, robots.txt and index.html into the site root.
"""
import json, html, re, sys
from pathlib import Path

SRC_DIR = Path(__file__).parent
ROOT = SRC_DIR.parent / "site"
DATA = SRC_DIR.parent / "content"
sys.path.insert(0, str(SRC_DIR))
from articles import ARTICLES, SRC  # noqa: E402

BASE = "https://appealmydenial.app"
REVIEWED_ISO = "2026-10-04"
REVIEWED = "October 4, 2026"
APP_STORE_URL = None        # set to the App Store link at launch
APP_STORE_ID = None         # numeric id, enables the Safari smart banner
ANALYTICS_HEAD = """<!-- Cloudflare Web Analytics --><script defer type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "b8435886b6b7453c97a74d408ab80267"}'></script><!-- End Cloudflare Web Analytics -->"""
OG_IMAGE = f"{BASE}/img/og.png"

esc = html.escape
by_slug = {a["slug"]: a for a in ARTICLES}

CSS = """
:root{--page:#FBF8EE;--paper:#fff;--ink:#1B1F24;--muted:#56606B;--rule:#E2DDD0;--green:#1E7A4A;--green-d:#16603A;--hi:#FFE95C;--soft:#EEF5EF}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--page);color:var(--ink);font:19px/1.6 "IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--green);text-underline-offset:2px}
a:hover{color:var(--green-d)}
.wrap{max-width:720px;margin:0 auto;padding:0 18px}
.top{border-bottom:1px solid var(--rule);background:var(--page)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.brand{display:inline-flex;align-items:center;gap:10px;font-weight:600;font-size:18px;color:var(--ink);text-decoration:none}
.brand img{width:34px;height:34px;border-radius:9px}
nav.main{display:flex;gap:16px;flex-wrap:wrap;font-size:16px}
nav.main a{color:var(--ink);text-decoration:none;font-weight:500}
nav.main a:hover{color:var(--green)}
.crumbs{font-size:15px;color:var(--muted);margin:20px 0 0}
.crumbs a{color:var(--muted)}
h1{font-size:clamp(30px,6.4vw,42px);line-height:1.12;letter-spacing:-.02em;margin:14px 0 8px}
.meta{color:var(--muted);font-size:15px;margin:0 0 20px}
h2{font-size:24px;line-height:1.25;letter-spacing:-.01em;margin:36px 0 10px}
h3{font-size:20px;margin:26px 0 8px}
p,li{margin:0 0 12px}
ul,ol{padding-left:24px}
.answer{background:var(--paper);border:1px solid var(--rule);border-left:6px solid var(--green);padding:16px 20px;margin:0 0 8px}
.answer p{margin:0}
.box{background:var(--paper);border:1px solid var(--rule);padding:18px 20px;margin:28px 0}
.box h2{margin-top:0;font-size:21px}
.next a.card{display:block;padding:12px 14px;border:1px solid var(--rule);border-radius:10px;margin:0 0 10px;text-decoration:none;color:var(--ink);background:var(--page)}
.next a.card:hover{border-color:var(--green)}
.next a.card b{display:block;color:var(--green)}
.cta{background:var(--green);color:#FBF8EE;border-radius:14px;padding:22px 22px;margin:30px 0}
.cta h2{color:#fff;margin:0 0 6px;font-size:23px}
.cta p{margin:0 0 12px}
.cta .btn{display:inline-block;background:var(--hi);color:var(--ink);font-weight:700;text-decoration:none;padding:12px 20px;border-radius:999px}
.cta .soon{display:inline-block;background:rgba(255,255,255,.14);color:#fff;font-weight:600;padding:10px 16px;border-radius:999px}
details{background:var(--paper);border:1px solid var(--rule);border-radius:10px;padding:12px 16px;margin:0 0 10px}
summary{font-weight:600;cursor:pointer}
details p{margin:10px 0 0}
.sources{font-size:15px;color:var(--muted)}
.sources li{margin-bottom:6px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin:12px 0 0}
.grid a{display:block;padding:10px 12px;border:1px solid var(--rule);background:var(--paper);border-radius:10px;text-decoration:none;color:var(--ink);font-weight:500}
.grid a:hover{border-color:var(--green);color:var(--green)}
table.facts{width:100%;border-collapse:collapse;background:var(--paper);border:1px solid var(--rule);font-size:17px}
table.facts th,table.facts td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--rule)}
table.facts th{width:36%;color:var(--muted);font-weight:500}
mark{background:var(--hi);padding:0 3px}
.calc label{display:block;font-weight:600;margin:16px 0 6px}
.calc .hint{font-weight:400;color:var(--muted);font-size:15px}
.calc select,.calc input{width:100%;font:inherit;padding:12px;border:1px solid #CFC8B8;border-radius:10px;background:#fff;color:var(--ink)}
.calc button{margin-top:18px;font:inherit;font-weight:700;background:var(--green);color:#fff;border:0;border-radius:999px;padding:13px 24px;cursor:pointer}
.result{display:none;margin-top:22px}
.result .big{font-size:clamp(28px,6vw,36px);font-weight:700;line-height:1.15;margin:4px 0 6px}
.result .left{font-weight:600}
.warn{background:#FFF6D6;border:1px solid #EBD98A;padding:12px 14px;border-radius:10px}
.hero{padding:34px 0 8px}
.hero img{width:84px;height:84px;border-radius:20px}
.hero h1{font-size:clamp(34px,8vw,48px);margin-top:22px}
.lead{font-size:21px;color:#3d454e}
footer.site{margin:48px 0 0;border-top:1px solid var(--rule);padding:22px 0 40px;font-size:15px;color:var(--muted)}
footer.site a{color:var(--muted)}
@media (max-width:520px){body{font-size:18px}nav.main{gap:12px;font-size:15px}}
"""

TRACK_JS = """<script>
window.amdTrack=window.amdTrack||function(n,p){try{if(window.plausible)plausible(n,{props:p||{}});if(window.gtag)gtag('event',n,p||{});}catch(e){}};
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-track]');if(a)amdTrack(a.getAttribute('data-track'),{page:location.pathname});});
</script>"""

ORG = {"@type": "Organization", "name": "Appeal My Denial", "url": BASE,
       "logo": {"@type": "ImageObject", "url": f"{BASE}/img/appeal-app-icon-1024.png"}}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u}
                                for i, (n, u) in enumerate(items)]}


def crumbs_html(items):
    parts = [f'<a href="{u}">{esc(n)}</a>' for n, u in items[:-1]] + [esc(items[-1][0])]
    return '<p class="crumbs">' + " › ".join(parts) + "</p>"


def page(path, title, desc, body, jsonld=(), og_type="article"):
    url = BASE + path
    smart = f'<meta name="apple-itunes-app" content="app-id={APP_STORE_ID}">' if APP_STORE_ID else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Appeal My Denial">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{smart}
<link rel="icon" href="/img/favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{''.join(ld(j) for j in jsonld)}
{ANALYTICS_HEAD}
{TRACK_JS}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="/"><img src="/img/apple-touch-icon.png" alt="">Appeal My Denial</a>
<nav class="main" aria-label="Main"><a href="/guides/">Guides</a><a href="/deadline/">Deadline calculator</a><a href="/states/">By state</a></nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site"><div class="wrap">
<p><strong>Appeal My Denial</strong> reads your health insurance denial letter, explains it in plain words, and drafts your appeal for you to review and send.</p>
<p>This site gives general information, not legal or medical advice. Rules change and every plan is different; check your own letter and plan documents. Free help: your state insurance department's consumer line, or for Medicare, your <a href="https://www.shiphelp.org/">State Health Insurance Assistance Program</a>.</p>
<p><a href="/guides/">Guides</a> · <a href="/deadline/">Deadline calculator</a> · <a href="/states/">External review by state</a> · <a href="/privacy">Privacy</a> · <a href="/terms">Terms</a></p>
<p>© 2026 Virtual Marketing Consultants, Inc.</p>
</div></footer>
</body></html>
"""


def cta(where):
    if APP_STORE_URL:
        btn = f'<a class="btn" href="{APP_STORE_URL}" data-track="app_store_click" data-where="{where}">Get the app — free to start</a>'
    else:
        btn = '<span class="soon">Coming soon to the App Store</span>'
    return f"""<section class="cta"><h2>Let the app write it for you</h2>
<p>Snap a photo of your denial letter. Appeal My Denial tells you why you were denied, your exact deadline, and drafts the appeal letter, plus the note for your doctor.</p>
{btn}</section>"""


def next_box(rel_slugs):
    cards = "".join(
        f'<a class="card" href="/guides/{s}/" data-track="next_guide"><b>{esc(by_slug[s]["h1"])}</b>{esc(by_slug[s]["desc"][:110].rsplit(" ",1)[0])}…</a>'
        for s in rel_slugs)
    return f"""<section class="box next"><h2>Your next question</h2>{cards}
<a class="card" href="/deadline/" data-track="calc_link"><b>Check your appeal deadline</b>Pick your plan type and the date on your letter. Free, and nothing is sent anywhere.</a></section>"""


def faq_html(faq):
    return '<h2>Common questions</h2>' + "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)


def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def article_ld(title, desc, path, iso=REVIEWED_ISO):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title[:110], "description": desc,
            "datePublished": iso, "dateModified": iso, "mainEntityOfPage": BASE + path,
            "image": OG_IMAGE, "author": ORG, "publisher": ORG, "inLanguage": "en-US"}


def sources_html(keys):
    lis = "".join(f'<li><a href="{SRC[k][1]}" rel="noopener">{esc(SRC[k][0])}</a></li>' for k in keys)
    return f'<h2>Sources</h2><ul class="sources">{lis}</ul>'


def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return rel


urls = []  # (path, priority)


# ---------------- guides ----------------
for a in ARTICLES:
    path = f"/guides/{a['slug']}/"
    trail = [("Home", "/"), ("Guides", "/guides/"), (a["h1"], path)]
    body = (crumbs_html(trail) + f"<article><h1>{esc(a['h1'])}</h1>"
            f'<p class="meta">Reviewed {a.get("reviewed", (REVIEWED_ISO, REVIEWED))[1]} · {a["minutes"]} min read</p>'
            f'<div class="answer">{a["short"]}</div>{a["body"]}'
            + next_box(a["related"]) + faq_html(a["faq"]) + cta(a["slug"]) + sources_html(a["sources"]) + "</article>")
    write(f"guides/{a['slug']}/index.html",
          page(path, a["title"], a["desc"], body,
               [article_ld(a["title"], a["desc"], path, a.get("reviewed", (REVIEWED_ISO, REVIEWED))[0]), crumbs_ld(trail), faq_ld(a["faq"])]))
    urls.append((path, "0.8", a.get("reviewed", (REVIEWED_ISO, REVIEWED))[0]))


# ---------------- guides hub ----------------
def links(tag_prefix):
    out = []
    for a in ARTICLES:
        if any(t.startswith(tag_prefix) for t in a["tags"]):
            out.append(f'<a href="/guides/{a["slug"]}/">{esc(a["h1"])}</a>')
    return "".join(out)

hub_trail = [("Home", "/"), ("Guides", "/guides/")]
hub_body = (crumbs_html(hub_trail) +
            "<h1>Health insurance denial guides</h1>"
            "<p class=\"lead\">Plain-English answers for the moment you get a denial letter: what it means, your deadline, and how to fight it.</p>"
            "<h2>Start here</h2><div class=\"grid\">" + links("start") + '<a href="/deadline/">Appeal deadline calculator</a></div>'
            "<h2>By your type of plan</h2><div class=\"grid\">" + links("plan:") + "</div>"
            "<h2>By the reason you were denied</h2><div class=\"grid\">" + links("reason:") + "</div>"
            "<h2>By state</h2><p>Every state's independent external review program: who to contact, the deadline, and fees. <a href=\"/states/\">See all 50 states and DC</a>.</p>"
            + cta("guides_hub"))
hub_desc = "Free, plain-English guides to appealing a health insurance denial: deadlines by plan type, what each denial reason means, and how to win."
write("guides/index.html", page("/guides/", "Health Insurance Denial Guides | Appeal My Denial", hub_desc, hub_body,
      [crumbs_ld(hub_trail), {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Health insurance denial guides",
                              "description": hub_desc, "url": BASE + "/guides/"}], og_type="website"))
urls.append(("/guides/", "0.9"))


# ---------------- deadline calculator ----------------
plans = json.loads((DATA / "plan_deadlines.json").read_text())["plan_types"]
calc_trail = [("Home", "/"), ("Deadline calculator", "/deadline/")]
guide_for = {"aca_marketplace": "aca-marketplace-appeal", "employer": "employer-plan-appeal",
             "medicare_advantage": "medicare-advantage-appeal", "original_medicare": "original-medicare-appeal",
             "medicaid_managed_care": "medicaid-appeal"}
rules = {p["id"]: {"label": p["label"], "days": p["appeal_deadline_days"], "guide": guide_for[p["id"]],
                   "src": p["source_url"]} for p in plans}
calc_body = crumbs_html(calc_trail) + """
<h1>Health insurance appeal deadline calculator</h1>
<p class="lead">Pick your type of plan and enter the date printed on your denial letter. We'll show your deadline and the rule behind it.</p>
<p class="meta">Free. Runs in your browser; nothing you enter is sent anywhere. Rules reviewed """ + REVIEWED + """.</p>
<div class="box calc">
<label for="plan">Type of plan</label>
<select id="plan">
<option value="">Choose one…</option>
<option value="medicare_advantage">Medicare Advantage (Part C)</option>
<option value="original_medicare">Original Medicare (Medicare Summary Notice)</option>
<option value="aca_marketplace">Marketplace / ACA plan (HealthCare.gov or state)</option>
<option value="employer">Plan through my job</option>
<option value="medicaid_managed_care">Medicaid health plan</option>
</select>
<label for="notice">Date on the denial letter <span class="hint">(the notice date, or the date on your Medicare Summary Notice)</span></label>
<input id="notice" type="date">
<div id="arrivalWrap" style="display:none">
<label for="arrival">When did the letter arrive? <span class="hint">Optional. Leave blank if you're not sure, and we'll use the safer date.</span></label>
<input id="arrival" type="date">
</div>
<label for="stated">Does your letter give its own deadline? <span class="hint">Optional. If it does, enter it and we'll use whichever date is earlier.</span></label>
<input id="stated" type="date">
<button id="go" type="button" data-track="calc_run">Show my deadline</button>
<div class="result" id="result" aria-live="polite"></div>
</div>
<h2>How the deadlines work</h2>
<ul>
<li><strong>Medicare Advantage:</strong> 65 days from the date of the notice. <a href="/guides/medicare-advantage-appeal/">Guide</a></li>
<li><strong>Original Medicare:</strong> 120 days from receiving the Medicare Summary Notice, presumed to be 5 days after its date. <a href="/guides/original-medicare-appeal/">Guide</a></li>
<li><strong>Marketplace and job-based plans:</strong> 180 days from receiving the denial. <a href="/guides/aca-marketplace-appeal/">Marketplace guide</a> · <a href="/guides/employer-plan-appeal/">Job-based guide</a></li>
<li><strong>Medicaid health plans:</strong> 60 days from the date on the notice. To keep a service you already get during the appeal, file within 10 days of when the notice was sent or by the date the change takes effect, whichever is later. <a href="/guides/medicaid-appeal/">Guide</a></li>
</ul>
<p>If waiting could seriously harm your health, don't wait for the deadline: call your plan today and ask for an expedited (72-hour) appeal. On Medicare and being discharged from the hospital, or your skilled nursing, home health or rehab care is ending? Call the Quality Improvement Organization (QIO) on your notice right away, before you leave the hospital.</p>
""" + cta("calculator") + """
<script>
(function(){
var R=""" + json.dumps(rules) + """;
var plan=document.getElementById('plan'),notice=document.getElementById('notice'),arrival=document.getElementById('arrival'),stated=document.getElementById('stated'),out=document.getElementById('result'),aw=document.getElementById('arrivalWrap');
function P(v){if(!v)return null;var a=v.split('-');return new Date(Date.UTC(+a[0],+a[1]-1,+a[2]));}
function add(d,n){return new Date(d.getTime()+n*864e5);}
function F(d){return d.toLocaleDateString('en-US',{timeZone:'UTC',weekday:'long',year:'numeric',month:'long',day:'numeric'});}
function today(){var t=new Date();return new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate()));}
plan.addEventListener('change',function(){var on=(plan.value==='aca_marketplace'||plan.value==='employer'||plan.value==='original_medicare');aw.style.display=on?'block':'none';if(!on)arrival.value='';});
document.getElementById('go').addEventListener('click',function(){
 var p=plan.value,n=P(notice.value);
 if(!p||!n){out.style.display='block';out.innerHTML='<p class="warn">Choose your type of plan and enter the date on your letter.</p>';return;}
 var r=R[p],a=P(arrival.value),s=P(stated.value),start,rule,note='';
 if(p==='aca_marketplace'||p==='employer'){
   if(a&&a>=n){var cap=add(n,10);if(a>cap){a=cap;note='We counted from no more than 10 days after the notice date, to stay on the safe side. ';}
     start=a;rule='180 days from when you received the denial ('+F(a)+').';}
   else{start=n;rule='180 days, counted from the notice date. Your letter counts from the day you received it, so you may have a few extra days; we\\'re using the safer date.';}
 }else if(p==='original_medicare'){
   if(a&&a>=n&&a<add(n,5)){start=a;rule='120 days from when you received your Medicare Summary Notice ('+F(a)+').';}
   else{start=add(n,5);rule='120 days from receipt of your Medicare Summary Notice, which Medicare presumes is 5 days after its date.';}
 }else{start=n;rule=r.days+' days from the date of the notice.';}
 var due=(p==='original_medicare')?add(start,120):add(start,r.days),used='calculated';
 if(s&&s<due){due=s;used='stated';}
 var left=Math.round((due-today())/864e5),lt;
 if(left<0)lt='<p class="warn"><strong>This date has passed.</strong> Contact your plan right away: some plans accept late appeals for good cause, and you may still have other options.</p>';
 else if(left<=14)lt='<p class="warn"><strong>'+left+' day'+(left===1?'':'s')+' left.</strong> Send your appeal as soon as you can, and keep proof of the date you sent it.</p>';
 else lt='<p class="left">'+left+' days from today.</p>';
 out.style.display='block';
 out.innerHTML='<p>Send your appeal by</p><p class="big">'+F(due)+'</p>'+lt+
  '<p><strong>Rule used:</strong> '+(used==='stated'?'the deadline printed on your letter, which is earlier than the standard rule. ':'')+rule+' '+note+'</p>'+
  (p==='medicaid_managed_care'?'<p class="warn"><strong>Is the plan cutting or stopping a service you get now?</strong> To keep it during the appeal, file by '+F(add(n,10))+' or by the date the change takes effect on your notice, whichever is later.</p>':'')+
  (p==='medicare_advantage'?'<p>Prescription (Part D) drug denials follow different steps. <a href="/guides/medicare-advantage-appeal/">See the guide</a>.</p>':'')+
  '<p>Always check the deadline printed on your letter. If the two differ, go by the earlier date.</p>'+
  '<p><a href="/guides/'+r.guide+'/">How to appeal a '+r.label.replace(' / ACA plan','')+' denial →</a></p>';
 if(window.amdTrack)amdTrack('calc_result',{plan:p});
});
})();
</script>
<noscript><p class="warn">The calculator needs JavaScript. Use the rules above: count the days from the date on your letter.</p></noscript>
"""
calc_desc = "Free appeal deadline calculator for Medicare Advantage, Original Medicare, Marketplace, job-based and Medicaid plans. Nothing leaves your browser."
calc_faq = [("How many days do I have to appeal a health insurance denial?",
             "65 days for Medicare Advantage, 120 days from receipt for Original Medicare, 180 days from receipt for Marketplace and job-based plans, and 60 days for Medicaid managed care plans.")]
write("deadline/index.html", page("/deadline/", "Health Insurance Appeal Deadline Calculator (Free)", calc_desc, calc_body,
      [crumbs_ld(calc_trail), faq_ld(calc_faq),
       {"@context": "https://schema.org", "@type": "WebApplication", "name": "Appeal deadline calculator",
        "url": BASE + "/deadline/", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": calc_desc}], og_type="website"))
urls.append(("/deadline/", "0.9"))


# ---------------- states ----------------
states = json.loads((DATA / "external_review_states.json").read_text())
fed = states["meta"]["federal_process"]
TO_INSURER = set("AZ CO DE IN KY LA MT OH OR RI SC TN TX WA WI WY".split())


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def clean_phone(s):
    return s if s else "Not listed on the state's page. Use the contact page linked below."


def deadline_text(r):
    st = r["state"]
    if st == "SC":
        return ("60 days under South Carolina law. Federal rules may give more time, but file within 60 days to be safe, "
                "and confirm with the SC Department of Insurance.")
    if st in ("MO", "WA"):
        return "State law doesn't set a deadline. Check your denial letter, and file within 4 months to be safe."
    if st == "TX":
        return "4 months (federal rule). Texas rules set no separate deadline for health-plan reviews."
    if st == "CO":
        return "4 months from the final denial (60 days if you used the plan's voluntary second-level appeal)."
    if st == "ME":
        return "12 months after the plan's final decision."
    return r["deadline"]


def fee_text(r):
    return r["fee"] if r["fee"] else "No fee listed. Most states charge nothing."


state_links = []
for r in sorted(states["states"], key=lambda x: x["state_name"]):
    name = r["state_name"]
    slug = slugify(name)
    path = f"/states/{slug}/"
    state_links.append((name, path))
    trail = [("Home", "/"), ("External review by state", "/states/"), (name, path)]
    federal = r["program"] == "federal_hhs"
    to_insurer = r["state"] in TO_INSURER
    if federal:
        how = (f"{name} uses the federal external review process for many plans. Your insurer's final denial letter tells you "
               "whether to file with the federal process (run by MAXIMUS Federal Services) or with an independent review organization it names.")
        if r["state"] in ("TX", "WI"):
            how += f" {name} also runs its own review process for plans the state regulates; the letter says which applies."
    elif to_insurer:
        how = f"In {name}, you send the request to your insurance company, which passes it to the state's review process."
    else:
        how = f"In {name}, you send the request to the state agency below."
    title = f"External Review in {name}: Deadline & How to File"
    desc = f"How to get an independent review of a health insurance denial in {name}: who to contact, the deadline, fees and fast reviews."
    rows = [("Who runs it", esc(r["administering_body"])),
            ("Deadline to request", esc(deadline_text(r))),
            ("Where to start", f'<a href="{esc(r["request_url"])}" rel="noopener">Official request page or form</a>'),
            ("Phone", esc(clean_phone(r["phone"]))),
            ("Fee", esc(fee_text(r))),
            ("Fast (expedited) review", "Available when waiting could seriously harm your health. Ask for it when you file." if r["expedited_available"] else "Ask the agency.")]
    table = '<table class="facts">' + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows) + "</table>"
    fed_box = ""
    if federal:
        fed_box = (f'<h2>The federal process</h2><p>File online at the <a href="{fed["portal"]}" rel="noopener">federal external review portal</a> '
                   f'or call {fed["phone"]}. There is no fee. Decisions take up to 45 days, or 72 hours when expedited.</p>')
    sfaq = [(f"How long do I have to request external review in {name}?", deadline_text(r)),
            (f"Who handles health insurance external review in {name}?", r["administering_body"])]
    body = (crumbs_html(trail) + f"<article><h1>External review in {esc(name)}</h1>"
            f'<p class="meta">Checked against official sources {REVIEWED}</p>'
            f'<div class="answer"><p><strong>Short answer:</strong> If your health plan upheld its denial after your internal appeal, '
            f'you can ask an independent reviewer to decide. {esc(how)}</p></div>'
            f"<h2>At a glance</h2>{table}"
            "<h2>Before you file</h2><ul>"
            "<li><strong>Finish the plan's internal appeal first,</strong> unless your situation is urgent. <a href=\"/guides/how-to-appeal-a-health-insurance-denial/\">How to appeal</a></li>"
            "<li><strong>Check which rules apply.</strong> State programs cover plans the state regulates. Self-funded employer plans usually use an independent reviewer the plan hires under federal rules, and Medicare and Medicaid have their own appeals. Your final denial letter says which.</li>"
            "<li><strong>Send everything:</strong> the final denial, your internal appeal, and your doctor's letter.</li></ul>"
            + fed_box +
            f'<p class="meta">Details change. Confirm with the agency before you file, and go by your denial letter if it gives a different deadline.</p>'
            + next_box(["external-review", "not-medically-necessary-denial", "aca-marketplace-appeal"])
            + faq_html(sfaq) + cta(f"state_{r['state']}")
            + '<h2>Sources</h2><ul class="sources">'
            + "".join(f'<li><a href="{esc(u)}" rel="noopener">{esc(re.sub(r"^https?://(www\\.)?", "", u)[:80])}</a></li>' for u in r["source_urls"])
            + "</ul></article>")
    write(f"states/{slug}/index.html", page(path, title, desc, body,
          [article_ld(title, desc, path), crumbs_ld(trail), faq_ld(sfaq)]))
    urls.append((path, "0.6"))

st_trail = [("Home", "/"), ("External review by state", "/states/")]
st_body = (crumbs_html(st_trail) + "<h1>Health insurance external review by state</h1>"
           "<p class=\"lead\">After your insurer's final no, an independent reviewer can overturn it. Pick your state to see who runs the program, the deadline, and how to file.</p>"
           "<div class=\"grid\">" + "".join(f'<a href="{p}">{esc(n)}</a>' for n, p in state_links) + "</div>"
           "<h2>Not sure it applies to you?</h2><p>State programs cover plans the state regulates. Self-funded employer plans usually use an independent reviewer the plan hires under federal rules, and Medicare and Medicaid have their own appeals. "
           "<a href=\"/guides/external-review/\">Read how external review works</a>.</p>" + cta("states_hub"))
st_desc = "Independent external review of health insurance denials in all 50 states and DC: who to contact, deadlines, fees and fast reviews."
write("states/index.html", page("/states/", "Health Insurance External Review by State (All 50 + DC)", st_desc, st_body,
      [crumbs_ld(st_trail)], og_type="website"))
urls.append(("/states/", "0.8"))


# ---------------- home ----------------
home_body = """<section class="hero"><img src="/img/appeal-app-icon-1024.png" alt="Appeal My Denial app icon">
<h1>Denied? Let's appeal it.</h1>
<p class="lead">Appeal My Denial reads your health insurance denial letter, tells you in plain words why you were denied and your exact deadline, and writes the appeal for you to send.</p></section>
<div class="answer"><p><strong>Most people never appeal.</strong> In 2024, HealthCare.gov consumers appealed fewer than 1% of denied claims. In Medicare Advantage, 80.7% of appealed prior authorization denials were fully or partly overturned. <a href="/guides/how-to-appeal-a-health-insurance-denial/">How to appeal</a></p></div>
""" + cta("home") + """
<h2>Free tools and guides</h2>
<div class="grid">
<a href="/deadline/" data-track="calc_link">Appeal deadline calculator</a>
<a href="/guides/how-to-appeal-a-health-insurance-denial/">How to appeal a denial</a>
<a href="/guides/how-to-read-a-denial-letter/">How to read a denial letter</a>
<a href="/guides/medicare-advantage-appeal/">Medicare Advantage appeals</a>
<a href="/guides/not-medically-necessary-denial/">"Not medically necessary"</a>
<a href="/guides/prior-authorization-denial/">No prior authorization</a>
<a href="/states/">External review by state</a>
<a href="/guides/">All guides</a>
</div>
<p class="meta" style="margin-top:28px">Not legal advice. We write the letter; you review and send it.</p>
"""
home_desc = "Appeal My Denial reads your health insurance denial letter, tells you why you were denied and your exact deadline, and writes the appeal for you."
home_html = page("/", "Appeal My Denial: Appeal a Health Insurance Denial", home_desc, home_body,
                 [{"@context": "https://schema.org", "@type": "WebSite", "name": "Appeal My Denial", "url": BASE + "/"}, dict(ORG, **{"@context": "https://schema.org"})],
                 og_type="website")
# keep the share card title the homepage already uses
home_html = home_html.replace('<meta property="og:title" content="Appeal My Denial: Appeal a Health Insurance Denial">',
                              '<meta property="og:title" content="Insurance said no? Appeal it.">')
write("index.html", home_html)
urls.insert(0, ("/", "1.0"))
urls += [("/privacy", "0.2"), ("/terms", "0.2")]

# ---------------- css, sitemap, robots ----------------
write("assets/site.css", CSS.strip() + "\n")
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"<url><loc>{BASE}{u[0]}</loc><lastmod>{u[2] if len(u) > 2 else REVIEWED_ISO}</lastmod><priority>{u[1]}</priority></url>" for u in urls]
sm.append("</urlset>")
write("sitemap.xml", "\n".join(sm) + "\n")
write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /data/\nDisallow: /samples/\n\nSitemap: {BASE}/sitemap.xml\n")
print(f"built {len(urls)} urls")
