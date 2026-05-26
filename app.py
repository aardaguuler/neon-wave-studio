import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Neon Wave Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background-color: #070913;
        color: #f8fafc;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #0a0d1e !important;
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }

    section[data-testid="stSidebar"] * {
        color: #94a3b8 !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] strong {
        color: #e2e8f0 !important;
    }

    .stAlert {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 8px !important;
        color: #64748b !important;
    }

    hr {
        border-top: 1px solid rgba(255, 255, 255, 0.06) !important;
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: #070913; }
    ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 16px 0; border-bottom: 1px solid rgba(255,255,255,0.06); margin-bottom: 16px;">
        <div style="font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #475569; margin-bottom: 4px;">Studio</div>
        <div style="font-size: 18px; font-weight: 800; color: #f1f5f9; letter-spacing: -0.5px;">Neon Wave</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Drum Sequencer**")
    st.markdown("""
Karelere tıklayarak ritim oluşturun. Mavi kareler o adımda çalar. Her satır ayrı bir enstrüman kanalıdır.

Satır başındaki sürgü ses seviyesini, **M** butonu ise o kanalı sessize alır.
    """)

    st.write("")
    st.markdown("**Synthesizer**")
    st.markdown("""
Piyano tuşlarına mouse ile veya klavyedeki **A S D F G H J K** tuşlarıyla çalın. Dalga formu, decay ve filtre ayarlarını sağ panelden değiştirin.

Delay sürgüsü notaların yankısını kontrol eder.
    """)

    st.write("")
    st.markdown("**BPM**")
    st.markdown("Üst paneldeki sürgü ritim hızını belirler. 60–180 BPM arası ayarlanabilir.")

    st.write("")
    st.markdown("---")
    st.markdown(
        "<div style='font-size: 10px; color: #334155; text-align: center; padding-top: 4px;'>Neon Wave Studio &mdash; Web Audio API</div>",
        unsafe_allow_html=True
    )

st.markdown("""
<div style="padding: 8px 0 16px 0; border-bottom: 1px solid rgba(255,255,255,0.05); margin-bottom: 4px;">
    <div style="font-size: 22px; font-weight: 800; color: #f1f5f9; letter-spacing: -0.5px; font-family: 'Inter', sans-serif;">
        Neon Wave Studio
    </div>
    <div style="font-size: 12px; color: #475569; margin-top: 3px; font-weight: 500;">
        16-Step Sequencer · Synthesizer · Delay FX
    </div>
</div>
""", unsafe_allow_html=True)

html_file_path = os.path.join(os.path.dirname(__file__), "studio.html")

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        studio_html = f.read()
    components.html(studio_html, height=950, scrolling=False)
except FileNotFoundError:
    st.error("studio.html not found.")
