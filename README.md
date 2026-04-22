# 📄 AI Resume Analyzer & Job Recommender 🚀

An intelligent web application that analyzes resumes against job descriptions, identifies skill gaps, and recommends relevant job roles with direct application links.

---

## 🔥 Features

* 📑 **Resume Parsing** – Extracts text from PDF resumes
* 🧠 **AI-Based Analysis** – Compares resume with job description
* 📊 **Similarity Score** – Calculates how well your resume matches the job
* 🎯 **Skill Gap Detection** – Identifies missing and matching skills
* ⚡ **Priority Skills Flash Cards** – Clickable insights for improvement
* 💼 **Job Recommendations** – Direct links from LinkedIn, Internshala, Indeed, Naukri, Glassdoor
* 🤖 **AI Assistant** – Ask questions about your resume
* 📥 **Downloadable Report** – Export analysis results

---

## 🛠️ Tech Stack

* **Frontend & Backend:** Streamlit
* **Language:** Python
* **Libraries:**

  * matplotlib
  * NLP preprocessing utilities
* **Concepts Used:**

  * Natural Language Processing (NLP)
  * Cosine Similarity
  * Skill Matching Algorithms

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── utils/
│   ├── parser.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── skill_match.py
│   ├── scoring.py
│   └── suggestions.py
│
└── assets/
```

---

## ⚙️ How It Works

1. Upload your resume (PDF)
2. Paste a job description
3. Click **Apply Analysis**
4. The system:

   * Extracts and cleans text
   * Computes similarity score
   * Identifies matching & missing skills
   * Generates recommendations
   * Suggests job roles

---


## 🚀 Installation & Setup

```bash
# Clone repository
git clone https://github.com/your-username/AI-Resume-Analyzer.git

# Navigate to folder
cd AI-Resume-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🔐 Data Security

* No resume data is stored permanently
* All processing happens in-memory
* No third-party sharing of user data
* Session-based handling ensures temporary usage only

---

## ⚠️ Limitations

* No user authentication
* No persistent storage
* Basic skill matching (rule-based)

---

## 🚀 Future Enhancements

* 🔐 User authentication & dashboard
* ☁️ Cloud deployment
* 📈 Advanced AI-based skill detection
* 📊 Resume improvement suggestions using LLMs
* 🎯 ATS optimization scoring

---

## 💡 Key Highlights (For Recruiters)

* Real-world problem solving (Resume screening)
* Clean UI with interactive visualization
* Performance optimized (cached rendering, fast UI interactions)
* Modular and scalable code structure

---

## 👩‍💻 Author

**Shubhangi**

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
