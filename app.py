import streamlit as st
from streamlit_option_menu import option_menu

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="AgroDSS AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------
# LOAD CUSTOM CSS
# ----------------------------------------------------

try:
    with open("assets/css/style.css", encoding="utf-8") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding-top:10px;">
            <h2 style="color:white; margin-bottom:0;">
                🌾 AgroDSS AI
            </h2>

            <p style="color:#E5E7EB; font-size:14px;">
                AI-Powered Agronomist
                <br>
                Decision Support System
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected = option_menu(
        menu_title=None,

        options=[
            "Home",
            "Farm Input",
            "Analysis Center",
            "Reports",
            "Settings"
        ],

        icons=[
            "house",
            "geo-alt",
            "bar-chart",
            "file-earmark-text",
            "gear"
        ],

        default_index=0,

        styles={
            "container": {
                "padding": "8px",
                "background": "linear-gradient(180deg,#60A5FA,#3B82F6)",
                "border-radius": "15px",
            },

            "icon": {
                "color": "white",
                "font-size": "18px",
            },

            "nav-link": {
                "color": "white",
                "font-size": "16px",
                "font-weight": "600",
                "text-align": "left",
                "margin": "5px 0",
                "padding": "12px",
                "border-radius": "10px",
            },

            "nav-link-selected": {
                "background-color": "#2563EB",
                "color": "white",
            },
        },
    )

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.markdown(
    """
<div class="top-header">

<h2>🌾 AgroDSS AI</h2>

<p>
AI-Powered Agronomist Decision Support System
</p>

</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------
# HOME PAGE
# ----------------------------------------------------

if selected == "Home":

    st.title("Welcome")

    st.write(
        """
Welcome to **AgroDSS AI**.

An enterprise platform that combines:

- Artificial Intelligence
- Google Earth Engine
- GIS
- Remote Sensing
- Weather Intelligence
- Precision Agriculture

to support data-driven agricultural decision making.
"""
    )

# ----------------------------------------------------
# FARM INPUT
# ----------------------------------------------------

elif selected == "Farm Input":

    st.title("Farm Input")

    st.info("Farm Input page will be developed in Sprint 2.")

# ----------------------------------------------------
# ANALYSIS CENTER
# ----------------------------------------------------

elif selected == "Analysis Center":

    st.title("Analysis Center")

    st.info("Analysis Center will be developed in Sprint 3.")

# ----------------------------------------------------
# REPORTS
# ----------------------------------------------------

elif selected == "Reports":

    st.title("Reports")

    st.info("Report Generation module will be developed later.")

# ----------------------------------------------------
# SETTINGS
# ----------------------------------------------------

elif selected == "Settings":

    st.title("Settings")

    st.info("Settings page coming soon.")
