import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF for PDF text extraction
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load environment variables
load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

# Initialize client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

# Streamlit Page Config
st.set_page_config(
    page_title="SummarEase - PDF Summarizer",
    page_icon="📄",
    layout="wide"
)

# Header & Description
st.title("📄 SummarEase - Smart PDF Summarizer")
st.markdown("### Upload your PDF and chat with an AI summarizer. Download the summary as a wrapped PDF!")

# System Prompt
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are SummarEase, an AI assistant specialized in reading and summarizing PDF documents. "
        "Your mission is to extract key insights, condense information, and provide clear, concise summaries. "
        "Make sure the summaries are accurate, professional, and easy to understand."
    )
}

# Function: Extract text from PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function: Get AI summary
def get_summary(text):
    messages = [SYSTEM_PROMPT, {"role": "user", "content": text}]

    completion = client.chat.completions.create(
        model="meta/llama-3.3-70b-instruct",
        messages=messages,
        temperature=0.3,
        top_p=0.7,
        max_tokens=800,
        stream=False
    )
    return completion.choices[0].message.content

# Function: Generate wrapped PDF
def create_pdf(summary_text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("SummarEase - PDF Summary", styles["Title"]))
    story.append(Spacer(1, 20))
    for para in summary_text.split("\n"):
        if para.strip():
            story.append(Paragraph(para, styles["Normal"]))
            story.append(Spacer(1, 10))

    doc.build(story)
    buffer.seek(0)
    return buffer

# Sidebar for file upload
st.sidebar.header("📂 Upload PDF")
pdf_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if pdf_file:
    with st.spinner("Extracting text and summarizing... ⏳"):
        pdf_text = extract_text_from_pdf(pdf_file)
        if pdf_text.strip():
            summary = get_summary(pdf_text[:4000])  # Limit input tokens

            # Add to chat history
            st.session_state["chat_history"].append(
                {"role": "assistant", "content": summary}
            )

            st.subheader("📌 Chat History")
            for i, msg in enumerate(st.session_state["chat_history"]):
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['content']}")
                elif msg["role"] == "assistant":
                    st.markdown(f"**SummarEase:** {msg['content']}")
                st.markdown("---")

            # Download button for summary as wrapped PDF
            pdf_buffer = create_pdf(summary)
            st.download_button(
                label="⬇️ Download Summary as PDF",
                data=pdf_buffer,
                file_name="summary.pdf",
                mime="application/pdf"
            )

            # Expandable section for raw text
            with st.expander("📖 Show Extracted Text"):
                st.text_area("Extracted PDF Text", pdf_text, height=300)
        else:
            st.error("Could not extract text from the PDF. Please try another file.")
else:
    st.info("👆 Upload a PDF from the sidebar to get started!")
