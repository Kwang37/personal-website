#!/usr/bin/env python3
"""Generate a one-page English resume for the portfolio's download link."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

OUT = "assets/Kaibo_Wang_Resume.pdf"
doc = SimpleDocTemplate(OUT, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=29, bottomMargin=29, title="Kaibo Wang - Resume")
ink = colors.HexColor("#18242a")
muted = colors.HexColor("#465c63")
accent = colors.HexColor("#316e76")
style = {
  "name":ParagraphStyle("Name",fontName="Helvetica-Bold",fontSize=18,leading=20,textColor=ink,alignment=TA_CENTER,spaceAfter=4),
  "contact":ParagraphStyle("Contact",fontName="Helvetica",fontSize=8.4,leading=11,textColor=muted,alignment=TA_CENTER,spaceAfter=2),
  "focus":ParagraphStyle("Focus",fontName="Helvetica",fontSize=8.9,leading=12,textColor=accent,alignment=TA_CENTER,spaceAfter=5),
  "section":ParagraphStyle("Section",fontName="Helvetica-Bold",fontSize=9.1,leading=12,textColor=accent,spaceBefore=8,spaceAfter=3),
  "heading":ParagraphStyle("Heading",fontName="Helvetica-Bold",fontSize=8.7,leading=11.3,textColor=ink,spaceBefore=2,spaceAfter=2),
  "bullet":ParagraphStyle("Bullet",fontName="Helvetica",fontSize=8.15,leading=10.4,leftIndent=12,firstLineIndent=-10,spaceAfter=2.3,textColor=ink),
  "body":ParagraphStyle("Body",fontName="Helvetica",fontSize=8.1,leading=10.3,textColor=ink,spaceAfter=2.5),
}
flow=[]
def p(text,key="body"):flow.append(Paragraph(text,style[key]))
def section(name):p(name.upper(),"section")
def heading(name):p(name,"heading")
def bullet(text):p("&#8226; "+text,"bullet")

p("Kaibo Wang","name")
p("Seattle, WA  |  kaibowang0201@gmail.com  |  (206) 306-3257  |  linkedin.com/in/kaibo-wang-uw","contact")
p("Product Management  |  AI Product Development  |  UX Research &amp; Design","focus")
p("<b>Technical:</b> Python, SQL, JavaScript, React, HTML/CSS, R, Figma, Tableau, Pandas, Excel, Git, LLM APIs","body")

section("Education")
p("<b>M.S. Information Management</b> | University of Washington, Seattle | Expected June 2028")
p("<b>B.S. Informatics</b> | University of Washington, Seattle | December 2025 | GPA 3.90/4.00; Dean's List 2023-2025")

section("Relevant Experience")
heading("Co-Founder, Client Services &amp; Application Operations | QuotaQuest | Seattle / Shanghai | Jan 2025-Present")
bullet("Co-founded a career-services venture; drafted service agreements, clarified scope, revised CVs and cover letters, and supported job applications.")
bullet("Reviewed a client's ~300 applications, discovering that roughly 20% targeted employers excluding international students; prioritized eligibility and role fit.")
bullet("Coordinated application tracking for 10+ paying clients; team reported $70K+ revenue and job offers for 8 of 10 clients.")

heading("Researcher, Designer &amp; Mentor | Wordplay, UW Information School | Sep 2023-Present")
bullet("Translated UI and educational materials from English to Chinese; maintained locale resources and checked in-context rendering and screen-reader accessibility.")
bullet("Participated in localization reviews and pull requests, improving terminology consistency and Chinese learning experiences.")

heading("Institutional Sales Intern | Harvest Fund Management | Shanghai | Apr-Jun 2026")
bullet("Produced 10+ market-outlook and product-positioning materials for institutional client meetings at a major asset-management firm.")
bullet("Tracked fund NAV, AUM, and performance information to support institutional inquiries and cross-functional reporting.")

section("Selected Projects")
heading("Healthcare Email Defense Agent | UW Information School | Sep-Dec 2025")
bullet("Designed the HTML demonstration interface and connected it to AWS-backed services for AI email screening with quarantine-first decisions and human IT review.")
bullet("Team-reported evaluation: 654 synthetic emails across 17 days, with 4.56-second average processing time.")

heading("GreenTail - Sustainable Pet Food Platform | UW INFO 442 | Sep-Dec 2025")
bullet("Led React page architecture and workflows for onboarding quiz, search/comparison, location maps, and embedded video.")
bullet("Advocated for optional login and browser-local preferences; integrated, tested, and debugged core user flows.")

section("Leadership")
p("Hua Classmates - Project Lead (2024-2025)  |  UW Utopia - Publicity Director (2023-2024)")
doc.build(flow)
print(f"Generated {OUT}")
