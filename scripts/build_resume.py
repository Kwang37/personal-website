#!/usr/bin/env python3
"""Generate a one-page ATS-readable PM/APM resume for the portfolio."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether

OUT=Path("assets/Kaibo_Wang_Resume.pdf")
OUT.parent.mkdir(parents=True,exist_ok=True)
NAVY=colors.HexColor("#1D3038")
TEAL=colors.HexColor("#1D676B")
DARK=colors.HexColor("#233037")
MUTED=colors.HexColor("#4D5C61")
LINE=colors.HexColor("#B9CFCD")
styles={
"name":ParagraphStyle("name",fontName="Helvetica-Bold",fontSize=21.3,leading=25,textColor=NAVY,alignment=TA_CENTER,spaceAfter=2),
"contact":ParagraphStyle("contact",fontName="Helvetica",fontSize=9,leading=12.2,textColor=MUTED,alignment=TA_CENTER,spaceAfter=.5),
"subtitle":ParagraphStyle("subtitle",fontName="Helvetica-Bold",fontSize=9.2,leading=12.4,textColor=TEAL,alignment=TA_CENTER,spaceBefore=4,spaceAfter=6),
"section":ParagraphStyle("section",fontName="Helvetica-Bold",fontSize=9.7,leading=12.6,textColor=TEAL),
"role":ParagraphStyle("role",fontName="Helvetica-Bold",fontSize=9.35,leading=12.2,textColor=NAVY),
"date":ParagraphStyle("date",fontName="Helvetica",fontSize=8.8,leading=11.8,textColor=MUTED,alignment=2),
"org":ParagraphStyle("org",fontName="Helvetica-Oblique",fontSize=8.75,leading=10.7,textColor=MUTED),
"bullet":ParagraphStyle("bullet",fontName="Helvetica",fontSize=8.95,leading=12.15,textColor=DARK,leftIndent=11,firstLineIndent=-8,spaceAfter=2.45),
"body":ParagraphStyle("body",fontName="Helvetica",fontSize=9,leading=12.5,textColor=DARK,spaceAfter=2.3)
}
experience=[
("Co-Founder | Client Services & Application Operations","QuotaQuest  |  Seattle, WA / Shanghai, China","Jan 2025 - Present",[
"Co-founded a career-services venture and managed client delivery: drafted service agreements, tailored CVs/cover letters, screened roles, and coordinated applications and updates.",
"Audited ~300 job applications and found ~20% targeted employers explicitly excluding international students; shifted targeting toward eligibility and role fit.",
"Supported 10+ paying clients; the referral-driven venture generated $70K+ in revenue, with 8 of 10 clients receiving job offers."]),
("Institutional Sales Intern","Harvest Fund Management  |  Shanghai, China","Apr - Jun 2026",[
"Produced 10+ market-outlook and fund-positioning materials per quarter for institutional client roadshows and portfolio discussions.",
"Maintained NAV, AUM, and performance-attribution trackers to support same-day institutional client inquiries and team reporting."]),
("Researcher, Designer & Mentor | Chinese Localization","Wordplay, University of Washington Information School  |  Seattle, WA","Sep 2023 - Present",[
"Localized 20+ pages of UI and learning content from English into Mandarin Chinese; maintained locale files and verified layout and screen-reader compatibility.",
"Reviewed localization changes with cross-functional contributors, improving terminology consistency and tutorial clarity for Chinese-speaking learners."])
]
projects=[
("AI Defender | AI Product Lead & Demo Developer","University of Washington  |  Four-person team","Sep - Dec 2025",[
"Led product discovery through 8 clinician/IT stakeholder interviews; designed the HTML demo and connected it to AWS-backed classification and quarantine workflows with human IT review.",
"Team evaluation using synthetic email: 654 messages in 17 days, 4.56-second average processing time, 7.5% quarantine rate, and zero reported system errors."]),
("GreenTail | Product Design & React Development","University of Washington, INFO 442  |  React / JavaScript","Sep - Dec 2025",[
"Led architecture and integration of React flows for a five-step onboarding quiz, product search/comparison, ZIP-code store maps, and embedded educational video.",
"Advocated optional sign-in and localStorage-based saved preferences to minimize unnecessary server-side collection; tested and debugged core journeys."])
]
doc=SimpleDocTemplate(str(OUT),pagesize=letter,leftMargin=42,rightMargin=42,topMargin=28,bottomMargin=27,
                      title="Kaibo Wang | Product Management Resume",author="Kaibo Wang",subject="Product Management / APM resume")
story=[]
def p(text,key="body"):return Paragraph(text,styles[key])
def section(label):
    story.append(Spacer(1,6.5))
    story.append(p(label.upper(),"section"))
    story.append(HRFlowable(width="100%",thickness=.65,color=LINE,spaceBefore=2,spaceAfter=5))
def entry(e):
    role,org,date,bullets=e
    width=letter[0]-84
    t=Table([[p(role,"role"),p(date,"date")]],colWidths=[width-139,139])
    t.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    group=[t,p(org,"org"),Spacer(1,2)]
    group.extend(p("&#8226; "+escape(b),"bullet") for b in bullets)
    story.append(KeepTogether(group))
    story.append(Spacer(1,3))
story.append(p("Kaibo Wang","name"))
story.append(p("Seattle, WA  |  (206) 306-3257  |  <link href='mailto:kaibowang0201@gmail.com' color='#4D5C61'>kaibowang0201@gmail.com</link>","contact"))
story.append(p("<link href='https://www.linkedin.com/in/kaibo-wang-uw' color='#1D676B'>linkedin.com/in/kaibo-wang-uw</link>  |  <link href='https://kwang37.github.io/personal-website/' color='#1D676B'>kwang37.github.io/personal-website</link>","contact"))
story.append(p("PRODUCT MANAGEMENT  |  AI PRODUCTS  |  TECHNICAL PRODUCT DESIGN","subtitle"))
section("Professional Experience")
for e in experience:entry(e)
section("Selected Projects")
for e in projects:entry(e)
section("Education")
story.append(p("<b>M.S., Information Management</b>  |  University of Washington, Seattle  |  Expected Jun 2028"))
story.append(p("<b>B.S., Informatics</b>  |  University of Washington, Seattle  |  Dec 2025  |  GPA 3.90/4.00; Dean's List (2023-2025)"))
section("Skills & Leadership")
story.append(p("<b>Product &amp; Research:</b> Product discovery, requirements, stakeholder interviews, user flows, UX testing, cross-functional coordination"))
story.append(p("<b>Technical &amp; Analytics:</b> React, JavaScript, HTML/CSS, Python, SQL, AWS integration, Figma, Excel, Pandas, Tableau, Git, LLM APIs"))
story.append(p("<b>Leadership &amp; Languages:</b> Project Lead, Hua Classmates; Publicity Director, UW Utopia | Mandarin (native), English (fluent)"))
doc.build(story)
print(f"Generated {OUT} ({OUT.stat().st_size:,} bytes)")
