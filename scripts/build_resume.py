#!/usr/bin/env python3
"""Build the current one-page portfolio resume from the approved final CV content.

The generated PDF is published at assets/Kaibo_Wang_Resume.pdf and linked from
both the English and Chinese portfolio homepages.
"""
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle,
    KeepTogether,
)

OUT = Path("assets/Kaibo_Wang_Resume.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

INK = colors.HexColor("#202124")
MUTED = colors.HexColor("#4B4F54")
RULE = colors.HexColor("#9A9A9A")
LINK = colors.HexColor("#1769AA")

styles = {
    "name": ParagraphStyle(
        "name", fontName="Helvetica-Bold", fontSize=19.5, leading=22.5,
        textColor=INK, alignment=TA_CENTER, spaceAfter=2,
    ),
    "contact": ParagraphStyle(
        "contact", fontName="Helvetica", fontSize=8.45, leading=10.2,
        textColor=MUTED, alignment=TA_CENTER, spaceAfter=0.5,
    ),
    "summary": ParagraphStyle(
        "summary", fontName="Helvetica", fontSize=8.45, leading=10.5,
        textColor=INK, spaceBefore=4, spaceAfter=2,
    ),
    "section": ParagraphStyle(
        "section", fontName="Helvetica-Bold", fontSize=9.35, leading=11.2,
        textColor=INK, spaceBefore=4.5, spaceAfter=1.2,
    ),
    "entry": ParagraphStyle(
        "entry", fontName="Helvetica-Bold", fontSize=8.35, leading=9.9,
        textColor=INK,
    ),
    "date": ParagraphStyle(
        "date", fontName="Helvetica", fontSize=8.15, leading=9.9,
        textColor=MUTED, alignment=TA_RIGHT,
    ),
    "bullet": ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=8.15, leading=9.75,
        textColor=INK, leftIndent=9, firstLineIndent=-7,
        spaceBefore=0, spaceAfter=1.1,
    ),
    "skill": ParagraphStyle(
        "skill", fontName="Helvetica", fontSize=8.15, leading=9.8,
        textColor=INK, spaceAfter=0.8,
    ),
    "body": ParagraphStyle(
        "body", fontName="Helvetica", fontSize=8.25, leading=10,
        textColor=INK,
    ),
}

def para(text, style):
    return Paragraph(text, styles[style])

def section(title, story):
    story.append(Spacer(1, 3.2))
    story.append(para(escape(title), "section"))
    story.append(HRFlowable(
        width="100%", thickness=0.65, color=RULE,
        spaceBefore=0.5, spaceAfter=2.4,
    ))

def entry(title, date, bullets, story):
    width = letter[0] - 76
    date_width = 86
    row = Table(
        [[para(escape(title), "entry"), para(escape(date), "date")]],
        colWidths=[width - date_width, date_width],
        hAlign="LEFT",
    )
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    block = [row]
    for item in bullets:
        block.append(para("&#8226; " + escape(item), "bullet"))
    story.append(KeepTogether(block))
    story.append(Spacer(1, 1.2))

doc = SimpleDocTemplate(
    str(OUT), pagesize=letter,
    leftMargin=38, rightMargin=38, topMargin=28, bottomMargin=27,
    title="Kaibo Wang | Resume",
    author="Kaibo Wang",
    subject="AI, Technical & Product Operations",
)

story = []
story.append(para("KAIBO WANG", "name"))
story.append(para(
    "Shanghai, China  |  +86 166 2870 9261  |  "
    "kaibowang0201@gmail.com",
    "contact",
))
story.append(para(
    'Portfolio: <link href="https://kwang37.github.io/personal-website/" '
    'color="#1769AA">kwang37.github.io/personal-website</link>  |  '
    '<link href="https://www.linkedin.com/in/kaibo-wang-uw" '
    'color="#1769AA">LinkedIn</link>',
    "contact",
))
story.append(para(
    "UW MSIM candidate with a B.S. in Informatics and experience turning "
    "user and operational needs into practical web interfaces, AI-workflow "
    "concepts, and cross-functional project delivery. Uses Cursor to "
    "decompose requirements, select relevant standards for accessibility, "
    "performance, and compatibility, and validate implementations through "
    "hands-on iteration.",
    "summary",
))

section("EDUCATION", story)
entry(
    "University of Washington, Seattle  |  M.S. Information Management",
    "Expected June 2028", [], story,
)
entry(
    "University of Washington, Seattle  |  B.S. Informatics  |  "
    "GPA: 3.90/4.00; Dean’s List",
    "December 2025", [], story,
)

section("AI, TECHNICAL & PRODUCT PROJECTS", story)
entry(
    "AI Defender — Healthcare Email Safety  |  HTML Demo & AWS Integration  |  UW INFO 492",
    "2025",
    [
        "Designed HTML/JavaScript demo screens for staff and IT review, translating the team’s quarantine-first, human-in-the-loop email-defense approach into clear role-specific interactions.",
        "Connected demo interface flows to AWS-backed services and collaborated with teammates on testing; used synthetic email scenarios rather than real patient data.",
    ],
    story,
)
entry(
    "GreenTail — Sustainable Pet Food Discovery  |  Product Design & Front-end Implementation  |  UW INFO 442",
    "2025",
    [
        "Used team personas and stakeholder needs to shape guided onboarding for first-time pet owners and transparent comparison for experienced owners; advocated optional sign-in and browser-local preferences.",
        "Implemented major React experiences including the five-step quiz, search and comparison flows, ZIP-based React-Leaflet store map, embedded educational video, and product-data/page transitions.",
        "Built and refined front-end pages with HTML/JSX and CSS/Tailwind, using Cursor as a coding assistant; decomposed UI needs into prompts, debugged cross-page issues, and integrated teammate code.",
        "Manually reviewed responsive layouts, content overflow, visual consistency, navigation, and mouse/touch interactions across desktop and mobile; iterated on issues with AI assistance.",
    ],
    story,
)
entry(
    "CSE 163 — Applied Python & Data Analysis  |  UW Coursework",
    "",
    [
        "Analyzed YouTube video engagement and top-1,000 creator data with Python; modeled views against likes, dislikes, and comments and compared reach with a custom view-to-subscriber conversion metric.",
        "Applied scikit-learn for classification and clustering, GeoPandas spatial joins on shapefile/GeoJSON data, advanced visualizations, and test scripts for data-processing logic.",
    ],
    story,
)
entry(
    "Wordplay — Accessible Programming Platform  |  Localization & Accessibility",
    "2023–2025",
    [
        "Localized 20+ pages of programming tutorials and interface content into Simplified Chinese; maintained structured language files, consistent terminology, and readable in-product layouts.",
        "Contributed to user research, usability feedback, and screen-reader evaluation; submitted GitHub pull requests/issues, incorporated maintainer feedback, and tested revisions.",
    ],
    story,
)

section("PROFESSIONAL EXPERIENCE", story)
entry(
    "Institutional Sales Intern  |  Harvest Fund Management, Shanghai",
    "Apr–Jun 2026",
    [
        "Analyzed institutional holdings, fund NAV, AUM, and performance data to support client inquiries and recurring sales reporting.",
        "Prepared 10+ market-outlook and fund-positioning materials in one quarter, translating financial information into clear client-facing presentations.",
    ],
    story,
)
entry(
    "Marketing Intern  |  Go Big",
    "Sep–Dec 2024",
    [
        "Planned WeChat and Instagram content calendars; wrote articles and captions, created promotional visuals/videos, managed publishing, and reviewed engagement metrics to refine content.",
        "Supported app engagement through in-app campaigns, community outreach, founder interviews, campus promotion, and cross-team coordination; relayed user feedback and UX suggestions.",
    ],
    story,
)
entry(
    "Career Mentor  |  QuotaQuest",
    "Jan 2025–Present",
    [
        "Researched role requirements and advised clients on resumes, cover letters, application fit, and submission tracking; coordinated follow-ups and service documentation.",
    ],
    story,
)

section("LEADERSHIP & PROJECT OPERATIONS", story)
entry(
    "Publicity Director  |  UW Utopia",
    "2023–2024",
    [
        "Led a 15-member publicity team by assigning writing/design tasks, setting content calendars and deadlines, mentoring new members, and reviewing publication quality.",
        "Coordinated a new-student welcome event from early planning through promotion; aligned campus partners and content contributors while resolving deadline and creative issues.",
    ],
    story,
)
entry(
    "Project Lead & Informatics Mentor  |  Hua Classmates",
    "2024–2025",
    [
        "Helped organize a mentorship workshop connecting 12 mentors and 20 students; coordinated mentor recruitment and advised Informatics students.",
    ],
    story,
)

section("SKILLS", story)
story.append(para(
    "<b>AI &amp; Workflow:</b> AI-assisted development (Cursor), prompt decomposition, "
    "context-aware guideline selection, AI-workflow concepts, human-in-the-loop design",
    "skill",
))
story.append(para(
    "<b>Programming &amp; Tools:</b> Python (scikit-learn, GeoPandas), HTML/CSS, "
    "JavaScript, React, AWS, Git, SQL (foundational)",
    "skill",
))
story.append(para(
    "<b>Product &amp; Operations:</b> Project coordination, event operations, "
    "stakeholder communication, UX, accessibility, content operations",
    "skill",
))
story.append(para(
    "<b>Languages:</b> Mandarin Chinese, English",
    "skill",
))

doc.build(story)
print(f"Generated {OUT} ({OUT.stat().st_size:,} bytes)")
