# app.py
import streamlit as st
from main import NewsAnalyzer

st.set_page_config(
    page_title="News Article Analyzer",
    page_icon="📰",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-top: 10px;
    }
    .main {
        padding: 2rem;
    }
    .stTextInput>div>div>input {
        padding: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def get_analyzer():
    return NewsAnalyzer()

def main():
    st.title("📰 News Article Analyzer")
    st.markdown("---")

    analyzer = get_analyzer()
    
    # Initialize session state
    if 'article_text' not in st.session_state:
        st.session_state.article_text = None
    if 'qa_chain' not in st.session_state:
        st.session_state.qa_chain = None
    if 'url' not in st.session_state:
        st.session_state.url = ""

    # URL Input with automatic extraction
    url = st.text_input(
        "Enter News Article URL and press Enter:",
        placeholder="https://example.com/news-article",
        key="url_input"
    )

    # Automatically process URL when it changes
    if url and url != st.session_state.url:
        st.session_state.url = url
        with st.spinner("Extracting article content..."):
            try:
                st.session_state.article_text = analyzer.extract_article_content(url)
                vector_store = analyzer.create_vector_store(st.session_state.article_text)
                st.session_state.qa_chain = analyzer.setup_qa_chain(vector_store)
                st.success("Article extracted successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.article_text = None
                st.session_state.qa_chain = None

    # Only show content if article is extracted
    if st.session_state.article_text:
        # Article Actions
        col1, col2 = st.columns(2)

        # Summary Section
        with col1:
            if st.button("📋 Get Summary"):
                with st.spinner("Generating summary..."):
                    summary = analyzer.get_summary(st.session_state.article_text)
                    st.markdown("### Article Summary")
                    st.write(summary)

        # Question Answering Section
        st.markdown("### ❓ Ask Questions About the Article")
        question = st.text_input(
            "Enter your question:",
            placeholder="What is the main topic of the article?"
        )

        if question:
            if st.button("🔍 Get Answer"):
                with st.spinner("Finding answer..."):
                    answer = analyzer.answer_question(st.session_state.qa_chain, question)
                    st.markdown("### Answer")
                    st.write(answer)

        # Display Article Text
        with st.expander("View Article Text"):
            st.write(st.session_state.article_text)

if __name__ == "__main__":
    main()