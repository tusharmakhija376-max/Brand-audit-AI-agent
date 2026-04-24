import streamlit as st
from gemini_agents import run_brand_audit_pipeline

st.set_page_config(
    page_title="Brand Audit AI Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
    }

    .hero-container {
        text-align: center;
        padding: 3rem 2rem 2rem 2rem;
        background: linear-gradient(135deg, rgba(102,126,234,0.15), rgba(118,75,162,0.15));
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }

    .hero-badge {
        display: inline-block;
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 6px 18px;
        border-radius: 20px;
        margin-bottom: 1.2rem;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #ffffff, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1.2;
    }

    .hero-subtitle {
        color: rgba(255,255,255,0.6);
        font-size: 1.1rem;
        margin-top: 0.8rem;
        font-weight: 300;
    }

    .agent-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 1.2rem;
        margin-bottom: 0.8rem;
        transition: all 0.3s ease;
    }

    .agent-card:hover {
        background: rgba(255,255,255,0.08);
        border-color: rgba(102,126,234,0.5);
        transform: translateX(4px);
    }

    .agent-number {
        display: inline-block;
        width: 28px;
        height: 28px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 50%;
        text-align: center;
        line-height: 28px;
        font-size: 0.75rem;
        font-weight: 700;
        color: white;
        margin-right: 8px;
    }

    .agent-name {
        font-weight: 600;
        color: #a78bfa;
        font-size: 0.9rem;
    }

    .agent-desc {
        color: rgba(255,255,255,0.5);
        font-size: 0.8rem;
        margin-top: 4px;
        padding-left: 36px;
    }

    .tech-pill {
        display: inline-block;
        background: rgba(102,126,234,0.2);
        border: 1px solid rgba(102,126,234,0.4);
        color: #a78bfa;
        font-size: 0.72rem;
        font-weight: 500;
        padding: 4px 12px;
        border-radius: 20px;
        margin: 3px;
    }

    .input-section {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }

    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.08) !important;
        border: 2px solid rgba(102,126,234,0.4) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 0.8rem 1.2rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102,126,234,0.2) !important;
        background: rgba(255,255,255,0.12) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.3) !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.8rem 2rem !important;
        transition: all 0.3s ease !important;
        letter-spacing: 0.5px !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(102,126,234,0.4) !important;
    }

    .result-header {
        background: linear-gradient(135deg, rgba(102,126,234,0.2), rgba(118,75,162,0.2));
        border: 1px solid rgba(102,126,234,0.3);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1.5rem 0;
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .pipeline-step {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-left: 3px solid #667eea;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.5rem;
        margin-bottom: 0.5rem;
    }

    .score-card {
        background: linear-gradient(135deg, rgba(102,126,234,0.15), rgba(118,75,162,0.15));
        border: 1px solid rgba(102,126,234,0.3);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
    }

    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255,255,255,0.04) !important;
        border-radius: 12px !important;
        padding: 4px !important;
        gap: 4px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px !important;
        color: rgba(255,255,255,0.5) !important;
        font-weight: 500 !important;
        padding: 8px 16px !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
    }

    .stMarkdown, .stMarkdown p, .stMarkdown li {
        color: rgba(255,255,255,0.85) !important;
    }

    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #a78bfa !important;
    }

    .stExpander {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
    }

    .stSuccess {
        background: rgba(16,185,129,0.15) !important;
        border: 1px solid rgba(16,185,129,0.3) !important;
        border-radius: 12px !important;
        color: #6ee7b7 !important;
    }

    .stSpinner > div {
        border-top-color: #667eea !important;
    }

    .sidebar-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #a78bfa;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .stat-box {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .stat-number {
        font-size: 1.8rem;
        font-weight: 700;
        color: #a78bfa;
    }

    .stat-label {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    div[data-testid="stDownloadButton"] button {
        background: rgba(16,185,129,0.2) !important;
        border: 1px solid rgba(16,185,129,0.4) !important;
        color: #6ee7b7 !important;
        border-radius: 10px !important;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-title">🔍 Brand Audit Agent</div>', unsafe_allow_html=True)

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown('<div class="stat-box"><div class="stat-number">4</div><div class="stat-label">Agents</div></div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown('<div class="stat-box"><div class="stat-number">3</div><div class="stat-label">Tools</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Agent Pipeline**", unsafe_allow_html=True)

    agents = [
        ("Perception Researcher", "Searches web via Tavily"),
        ("Sentiment Analyst", "Scores public emotion"),
        ("Report Writer", "Structures audit report"),
        ("LLM-as-Judge", "Scores report quality"),
    ]
    for i, (name, desc) in enumerate(agents, 1):
        st.markdown(f"""
        <div class="agent-card">
            <span class="agent-number">{i}</span>
            <span class="agent-name">{name}</span>
            <div class="agent-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Tech Stack**", unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-top:8px">
        <span class="tech-pill">🤖 Gemini 2.0 Flash</span>
        <span class="tech-pill">🔍 Tavily Search</span>
        <span class="tech-pill">🎈 Streamlit</span>
        <span class="tech-pill">🐍 Python 3.13</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="color:rgba(255,255,255,0.3);font-size:0.75rem;text-align:center">Sem IV ECE — Agentic AI Project</div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero-container">
    <div class="hero-badge">✦ Multi-Agent AI System</div>
    <h1 class="hero-title">Brand Audit AI Agent</h1>
    <p class="hero-subtitle">
        Enter any brand name and get a complete AI-powered audit in under 60 seconds.<br>
        Powered by live web search + 4 specialized AI agents.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="input-section">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown('<p style="color:rgba(255,255,255,0.7);font-weight:500;margin-bottom:8px">Enter Brand Name</p>', unsafe_allow_html=True)
    brand_name = st.text_input(
        "",
        placeholder="e.g., Nike, Tesla, Zomato, Apple, Swiggy...",
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    run_button = st.button(
        "🚀  Generate Brand Audit Report",
        type="primary",
        use_container_width=True,
        disabled=(brand_name.strip() == "")
    )
    st.markdown('<p style="color:rgba(255,255,255,0.3);font-size:0.8rem;text-align:center;margin-top:8px">Searches live web data · Runs 4 AI agents · Takes ~30-60 seconds</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if run_button and brand_name.strip():
    brand = brand_name.strip()
    with st.spinner(f"Running 4-agent pipeline for {brand}..."):
        try:
            results = run_brand_audit_pipeline(brand)
            st.session_state["results"] = results
            st.session_state["last_brand"] = brand
        except Exception as e:
            st.error(f"Pipeline error: {str(e)}")
            st.stop()
    st.success(f"✅ Brand audit for **{brand}** complete! Scroll down to explore all 5 tabs.")

if "results" in st.session_state:
    results = st.session_state["results"]
    brand = st.session_state["last_brand"]

    st.markdown(f"""
    <div class="result-header">
        <div style="font-size:2rem">📊</div>
        <div>
            <div style="font-size:1.3rem;font-weight:700;color:white">Results for <span style="color:#a78bfa">{brand}</span></div>
            <div style="color:rgba(255,255,255,0.4);font-size:0.85rem">4 agents completed · Live web data · AI-generated report</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🔍  Raw Search Data",
        "👁️  Perception Research",
        "📊  Sentiment Analysis",
        "📋  Audit Report",
        "⚖️  Quality Score"
    ])

    with tab1:
        st.markdown("### Raw Data from Tavily Search")
        st.markdown('<p style="color:rgba(255,255,255,0.4)">Live web data collected by the Tavily Search tool across 3 query types</p>', unsafe_allow_html=True)
        search_data = results["search_data"]
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            with st.expander("📝 Customer Reviews", expanded=True):
                st.text(search_data["reviews"][:2000])
        with col_b:
            with st.expander("📰 News Coverage", expanded=True):
                st.text(search_data["news"][:2000])
        with col_c:
            with st.expander("💬 Social Mentions", expanded=True):
                st.text(search_data["social"][:2000])

    with tab2:
        st.markdown(f"### Perception Research — {brand}")
        st.markdown('<div class="pipeline-step"><b style="color:#a78bfa">Agent 1 — Perception Researcher</b><br><span style="color:rgba(255,255,255,0.5);font-size:0.85rem">Extracted key themes from raw Tavily search data</span></div>', unsafe_allow_html=True)
        st.markdown(results["perception"])

    with tab3:
        st.markdown(f"### Sentiment Analysis — {brand}")
        st.markdown('<div class="pipeline-step"><b style="color:#a78bfa">Agent 2 — Sentiment Analyst</b><br><span style="color:rgba(255,255,255,0.5);font-size:0.85rem">Quantified emotional tone across 5 dimensions with scores</span></div>', unsafe_allow_html=True)
        st.markdown(results["sentiment"])

    with tab4:
        st.markdown(f"### Brand Audit Report — {brand}")
        st.markdown('<div class="pipeline-step"><b style="color:#a78bfa">Agent 3 — Audit Report Writer</b><br><span style="color:rgba(255,255,255,0.5);font-size:0.85rem">Synthesized all data into a structured professional report</span></div>', unsafe_allow_html=True)
        st.markdown(results["audit_report"])
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="⬇️  Download Full Report as .txt",
            data=results["audit_report"],
            file_name=f"brand_audit_{brand.lower().replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True
        )

    with tab5:
        st.markdown("### Report Quality Evaluation")
        st.markdown('<div class="pipeline-step"><b style="color:#a78bfa">Agent 4 — LLM-as-Judge</b><br><span style="color:rgba(255,255,255,0.5);font-size:0.85rem">Independently scored report quality using a 5-criterion rubric</span></div>', unsafe_allow_html=True)
        st.markdown(results["judge_evaluation"])

else:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;color:rgba(255,255,255,0.3)">Try these brands to get started</p>', unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    for col, brand_ex in zip([col1,col2,col3,col4,col5], ["Nike","Tesla","Zomato","Apple","Swiggy"]):
        with col:
            st.markdown(f'<div style="text-align:center;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:10px;padding:10px;color:rgba(255,255,255,0.6);font-size:0.9rem">{brand_ex}</div>', unsafe_allow_html=True)
