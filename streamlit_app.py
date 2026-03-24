import streamlit as st
import os

# ==========================================
# MFE5150 Final Project: Multi-Asset Risk Analytics (Group Submission)
# ==========================================
#
# HOW TO RUN THIS PROJECT:
# 1. Open your terminal or command prompt.
# 2. Make sure you have Streamlit installed (`pip install streamlit`).
# 3. Navigate to this directory and execute the following command:
#    streamlit run app.py
#
# ------------------------------------------
# ARCHITECTURE NOTE:
# We decided to use Streamlit as our deployment shell because of its ease of hosting.
# However, all of our core econometric modelling (GARCH/EGARCH/Nelder-Mead MLE) 
# and VaR Backtesting logic is implemented PURELY within our custom HTML file.

# 1. Default Page Configuration
st.set_page_config(
    page_title="MFE5150 · Multi-Asset Portfolio Risk Analytics", 
    layout="wide", 
    initial_sidebar_state="collapsed",
    page_icon="📈"
)

# 2. UI Customization
# We inject custom CSS into the Streamlit container to completely hide the default UI chrome (headers, 
# footers, menus, and whitespace). We want our embedded HTML dashboard to take up 100% of the screen.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

/* Force Zero Margins and Padding to let our custom HTML breathe */
.appview-container .main .block-container {
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    padding-bottom: 0rem !important;
    max-width: 100% !important;
}

/* Hide Default Streamlit Menus so it looks like a professional standalone web app */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
[data-testid="collapsedControl"] {display: none;}
footer {visibility: hidden;}

/* Iframe Height Fixes to prevent ugly double scrollbars when our HTML component renders */
iframe {
    border: none !important;
    height: 100vh !important;
    width: 100vw !important;
}
</style>
""", unsafe_allow_html=True)

# 3. Load & Render the Client-Side Engine
# This block loads our 'GroupProject.html' file which handles all the time-series math, VaR backtesting, and Plotly charts.
html_file_path = os.path.join(os.path.dirname(__file__), "GroupProject.html")

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Render the exact HTML client-side inside the Streamlit iframe wrapper.
    # We allocate 9000px height so there's enough room for all our dynamic charts and diagnostics to render safely.
    st.components.v1.html(html_code, height=9000, scrolling=True)

except FileNotFoundError:
    st.error(f"Error: Could not locate our main HTML engine at `{html_file_path}`")
