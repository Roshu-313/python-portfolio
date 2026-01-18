# 📄 AI PDF Summarizer (GenAI Project)

## 📌 Overview
This project is a beginner-friendly GenAI application that reads PDF files and generates concise summaries using a Large Language Model (LLM).

It demonstrates how traditional Python processing can be combined with modern Generative AI.

## 🚀 Features
- Reads and extracts text from PDF files
- Cleans and preprocesses text
- Uses a free Hugging Face LLM for summarization
- Saves AI-generated summary to a text file

## 🛠️ Technologies Used
- Python 3
- PyPDF2
- requests
- Hugging Face Inference API (LLM)

## ▶️ How to Run
1. Install dependencies:
   python -m pip install PyPDF2 requests

2. Add your Hugging Face token in the code:
   HF_TOKEN = "your_token_here"

3. Run the script:
   python summarizer.py

## 📂 Output
- summary.txt → AI-generated summary of the PDF

## 🎯 Learning Outcome
- Understanding GenAI pipelines
- Working with LLM APIs
- Prompt-based summarization
- Safe handling of API keys

