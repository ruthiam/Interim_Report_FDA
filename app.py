import streamlit as st
import os

# ==========================================
# STREAMLIT CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="MFE5150 · Multi-Asset Portfolio Risk Analytics", 
    layout="wide", 
    initial_sidebar_state="collapsed",
    page_icon="📈"
)

# Hide STREAMLIT's default whitespace, menus, padding, and UI Chrome entirely
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

/* Force Zero Margins and Padding */
.appview-container .main .block-container {
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    padding-bottom: 0rem !important;
    max-width: 100% !important;
}

/* Hide Default Menus */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
[data-testid="collapsedControl"] {display: none;}
footer {visibility: hidden;}

/* Iframe Height Fixes to prevent double scrollbars */
iframe {
    border: none !important;
    height: 100vh !important;
    width: 100vw !important;
}
</style>
""", unsafe_allow_html=True)

# Path to the source HTML file
html_file_path = os.path.join(os.path.dirname(__file__), "GroupProject.html")

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Render the exact perfect HTML client-side
    st.components.v1.html(html_code, height=9000, scrolling=True)

except FileNotFoundError:
    st.error(f"Error: Could not locate exactly 1-to-1 HTML file at `{html_file_path}`")
