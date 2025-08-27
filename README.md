
# 📘 SummarEase – Smart PDF Summarizer  

An **AI-powered PDF Summarizer** that helps you extract insights from lengthy documents in seconds!  
Upload any PDF and receive a **concise, structured summary** powered by **NVIDIA’s LLaMA-based API**.  
Perfect for students, researchers, and professionals who need quick takeaways without reading full reports.  

---

## ✨ Features  

- 📄 **PDF Upload & Extraction** – Supports drag & drop or file browsing.  
- 🧠 **AI-Powered Summarization** – Uses NVIDIA’s LLaMA model for clean, human-like summaries.  
- 📋 **Expandable Raw Text View** – See the extracted text from your PDF.  
- 📥 **Export Summaries** – Download your summarized content as a PDF.  
- 🎨 **Clean UI** – Built with Streamlit for an elegant, distraction-free experience.  

---

## 🛠️ Tech Stack  

- **Frontend / UI**: [Streamlit](https://streamlit.io/)  
- **AI Model**: [NVIDIA API (Meta LLaMA-3.3-70B-Instruct)](https://build.nvidia.com/meta/llama-3_3-70b-instruct)  
- **PDF Processing**: [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)  
- **Export Utility**: [ReportLab](https://www.reportlab.com/)  
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/<your-username>/SummarEase.git
cd SummarEase
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add NVIDIA API Key

Create a `.env` file in the project root and add:

```env
NVIDIA_API_KEY=your_api_key_here
```

### 4️⃣ Run the App

```bash
streamlit run app-pdf.py
```

---
### 📌 Upload & Summary View

![WhatsApp Image 2025-08-27 at 23 04 52_435fb4de](https://github.com/user-attachments/assets/bdd591c0-8fbb-4c85-8361-2abb89768550)


### 📌 chat History & Download Option
![WhatsApp Image 2025-08-27 at 23 05 24_0ab59d54](https://github.com/user-attachments/assets/827b31df-31e2-4cdd-8e63-f18f20eb5ddd)

<img width="1880" height="918" alt="Screenshot 2025-08-27 232150" src="https://github.com/user-attachments/assets/c4165a1a-9d1e-4b20-812f-284f22606566" />




## 🤔 Why SummarEase?

Reading through lengthy reports or research papers can be overwhelming.
SummarEase saves time by:

* Extracting **core ideas quickly**.
* Providing **downloadable summaries** for later use.
* Offering a **student & researcher-friendly tool** for productivity.

