import sys
import os
import streamlit as st
import matplotlib.pyplot as plt
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.parser import extract_text_from_pdf
from utils.preprocessing import clean_text
from utils.similarity import get_similarity
from utils.skill_match import match_skills
from utils.scoring import calculate_score
from utils.suggesstions import generate_suggestions, ai_chat_response

# -------------------- CONFIG --------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# -------------------- JOB ROLE GENERATOR --------------------
def generate_job_roles(skills):
    roles = []
    skills_text = " ".join(skills).lower()

    if "python" in skills_text:
        roles.append("Python Developer")
    if "machine learning" in skills_text or "ml" in skills_text:
        roles.append("Machine Learning Engineer")
    if "data" in skills_text or "pandas" in skills_text:
        roles.append("Data Analyst")
    if "sql" in skills_text:
        roles.append("Database Developer")
    if "deep learning" in skills_text:
        roles.append("AI Engineer")

    if not roles:
        roles = ["Software Developer"]

    return roles[:3]

# -------------------- CSS --------------------
st.markdown("""
<style>
html, body, .stApp { background-color: white !important; }
h1, h2, h3, h4, h5, h6, label { color: black !important; }
.stCaption, .stMarkdown p, footer { color: black !important; }

/* Fix expander visibility */
details summary {
    color: black !important;
    font-weight: 600;
}
details div {
    color: black !important;
}

/* Fix priority skills visibility */
.priority-text {
    color: black !important;
    font-size: 15px;
}

/* Buttons */
.stButton { position: relative; }
.stButton > button {
    background: linear-gradient(to right, #4facfe, #00c6ff);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}
.stButton > button:hover {
    box-shadow: 0 0 20px rgba(0,191,255,0.9);
    transform: translateY(-2px);
}
.stButton::after {
    content: "🚀";
    position: absolute;
    right: -30px;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0;
}
.stButton:hover::after { opacity: 1; }

/* Cards */
.green-card {
    background-color: #e6ffe6;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid green;
    color: black;
}
.red-card {
    background-color: #ffe6e6;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid red;
    color: black;
}

/* Job cards */
.job-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #f9f9f9;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 4px solid #00c6ff;
}
.job-title { font-weight: bold; color: black; font-size: 14px; }
.job-link { text-decoration: none; color: #0077b6; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

# -------------------- SESSION --------------------
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# -------------------- HEADER --------------------
st.title("📄 AI Resume Analyzer & Job Recommender")
st.caption("AI-powered resume screening, skill gap analysis, and job role recommendations 🚀")

st.divider()

# -------------------- INPUT --------------------
col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

with col2:
    jd_text = st.text_area(
        "Paste Job Description",
        height=200,
        placeholder="Upload resume first...",
        disabled=not resume_file
    )

apply_btn = st.button("Apply Analysis")

st.divider()

# -------------------- ANALYSIS --------------------
if apply_btn and resume_file and jd_text:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(resume_file)
        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(jd_text)

        st.session_state.similarity = get_similarity(resume_clean, jd_clean)
        st.session_state.resume_skills, st.session_state.missing_skills = match_skills(resume_clean, jd_clean)
        st.session_state.score = calculate_score(
            st.session_state.similarity,
            st.session_state.missing_skills
        )

        st.session_state.analyzed = True

# -------------------- RESULTS --------------------
if st.session_state.analyzed:

    similarity = st.session_state.similarity
    resume_skills = st.session_state.resume_skills
    missing_skills = st.session_state.missing_skills
    score = st.session_state.score

    st.subheader("Results")

    c1, c2 = st.columns(2)

    c1.markdown(f"<h4 style='color:black;'>Similarity</h4><h2 style='color:black;'>{similarity:.2f}</h2>", unsafe_allow_html=True)
    c2.markdown(f"<h4 style='color:black;'>Score</h4><h2 style='color:black;'>{score}/100</h2>", unsafe_allow_html=True)

    if score >= 80:
        verdict, color = "✅ Strong Match", "green"
    elif score >= 60:
        verdict, color = "⚠️ Moderate Match", "orange"
    else:
        verdict, color = "❌ Needs Improvement", "red"

    st.markdown(f"<h3 style='color:{color};'>Final Verdict: {verdict}</h3>", unsafe_allow_html=True)

    st.progress(int(score))

    # Graph
    st.subheader("Skill Overview")

    col_left, col_mid, col_right = st.columns([2,2,2])
    with col_mid:
        labels = ["Matching", "Missing"]
        target_values = [len(resume_skills), len(missing_skills)]

        fig, ax = plt.subplots(figsize=(4,3))
        chart = st.pyplot(fig)

        for i in range(30):
            ax.clear()
            progress = i / 29
            values = [target_values[0]*progress, target_values[1]*progress]
            ax.bar(labels, values, color=["green", "red"])
            ax.set_xlabel("Skills Type")
            ax.set_ylabel("Count")
            chart.pyplot(fig)
            time.sleep(0.04)

    # Skills
    st.subheader("Skills")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### Matching")
        st.markdown(f'<div class="green-card">{", ".join(resume_skills) or "None"}</div>', unsafe_allow_html=True)

    with c2:
        st.markdown("### Missing")
        st.markdown(f'<div class="red-card">{", ".join(missing_skills) or "None"}</div>', unsafe_allow_html=True)

    # -------- PRIORITY SKILLS (FIXED FAST VERSION) --------
    st.markdown("<h3 style='color:black;'>🔥 Priority Skills to Learn</h3>", unsafe_allow_html=True)

    priority = missing_skills[:5]

    skill_info = {
        "machine learning": "Machine Learning is about training models to learn patterns from data and make predictions.",
        "deep learning": "Deep Learning uses neural networks with multiple layers to solve complex problems like image and speech recognition.",
        "tensorflow": "TensorFlow is an open-source library by Google used for building and training machine learning models.",
        "python": "Python is a programming language widely used in data science, AI, and backend development.",
        "sql": "SQL is used to manage and query structured databases.",
    }

    if "selected_skill" not in st.session_state:
        st.session_state.selected_skill = None

    if priority:
        for skill in priority:
            if st.button(f"⚡ {skill}", key=f"skill_{skill}"):
                st.session_state.selected_skill = skill

        if st.session_state.selected_skill:
            info = skill_info.get(
                st.session_state.selected_skill.lower(),
                f"{st.session_state.selected_skill} is an important skill for your target role."
            )
            st.markdown(f"<div class='priority-text'>{info}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='priority-text'>No major gaps detected 🎉</div>", unsafe_allow_html=True)

    # Suggestions
    st.subheader("Suggestions")
    for s in generate_suggestions(missing_skills, score):
        st.markdown(f"👉 {s}")

    # Jobs
    st.subheader("Recommended Jobs")

    roles = generate_job_roles(resume_skills)

    platforms = [
        ("LinkedIn", "https://www.linkedin.com/jobs/search/?keywords="),
        ("Internshala", "https://internshala.com/jobs/keywords-"),
        ("Indeed", "https://www.indeed.com/jobs?q="),
        ("Naukri", "https://www.naukri.com/"),
        ("Glassdoor", "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=")
    ]

    for role in roles:
        for name, base_url in platforms:
            link = base_url + role.replace(" ", "+")
            st.markdown(f"""
            <div class="job-card">
                <div class="job-title">
                    💼 {role} Jobs <span style="color:#555;">({name})</span>
                </div>
                <a class="job-link" href="{link}" target="_blank">View →</a>
            </div>
            """, unsafe_allow_html=True)

    # Download
    report = f"""
Similarity: {similarity:.2f}
Score: {score}/100
Matching Skills: {", ".join(resume_skills)}
Missing Skills: {", ".join(missing_skills)}
"""
    st.download_button("📥 Download Report", report, file_name="report.txt")

    # AI Chat
    st.subheader("AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    prompt = st.chat_input("Ask something about your resume...")

    if prompt:
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        reply = ai_chat_response(prompt, resume_skills, missing_skills, score)

        st.chat_message("assistant").write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.expander("📘 How this works"):
        st.markdown("""
        <div style="color:black;">
        - Extracts text from resume (PDF)  
        - Cleans and preprocesses using NLP  
        - Computes similarity with job description  
        - Identifies matching and missing skills  
        - Generates score and suggestions  
        - Recommends job roles dynamically  
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Built with Streamlit 🚀")