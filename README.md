# 📰 News Article Analyzer with LLaMA 3.2 3B  

## 🚀 Overview  
This AI-powered **News Article Analyzer** enables users to paste a news article URL and interact with it via a chat interface. You can:  
- **Extract and summarize** news articles.  
- **Ask questions** about the content.  
- **Receive precise answers** powered by a **locally hosted LLaMA 3.2 3B model**.  

## 🛠️ Tech Stack  
- **Python**  
- **Streamlit** (Frontend)  
- **LangChain** (LLM Framework)  
- **FAISS** (Vector Database)  
- **BeautifulSoup** (Web Scraping)  
- **Ollama** (Locally Hosted LLM)  

## 🏗️ Project Structure  
📂 news-analyzer-llama3
│── app.py # Streamlit UI
│── main.py # Core functions (QA Summarization, Vector Storage)
│── ollama_llm.py # Wrapper for running LLaMA 3.2 3B locally
│── requirements.txt # Dependencies
│── README.md # Documentation


## 🎯 Features  
- **Extracts content** from news article URLs.  
- **Summarizes** the article concisely.  
- **Allows users to ask questions** and get context-aware responses.  
- **Runs entirely locally** using the lightweight **LLaMA 3.2 3B model**.  

## 🔧 Installation  
1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/ShlokRana/news-analyzer-llama3.git
cd news-analyzer-llama3
```

2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Run Ollama to Serve the Model Locally**
Ensure you have Ollama installed, and check for the model also
```bash
ollama list
```

4️⃣ **Run the Streamlit App**
```bash
streamlit run app.py
```

## 📌 Usage
- **Paste a news article URL into the app.**
- **Click "Extract" to fetch the content.**
- **Click "Get Summary" to receive a concise summary.**
- **Ask any question about the article and get instant responses.**


## 📽️ Demo Video
Click below to watch a demo of the News Article Analyzer in action:  
[![Watch the Demo](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](videos/demo.mp4)  


## 📩 Feedback & Contributions
Feel free to submit PRs or open issues! Let's improve this together. 🚀
