import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Streamlit Sayfa Yapılandırması
st.set_page_config(
    page_title="Neon Wave Studio - İnteraktif Ritim ve Melodi Laboratuvarı",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Özel Streamlit Tasarım Özelleştirmesi (Dark Synthwave Ahengi)
st.markdown("""
<style>
    /* Ana arka plan ve metin renkleri */
    .stApp {
        background-color: #070913;
        color: #f8fafc;
    }
    
    /* Sidebar tasarımı */
    section[data-testid="stSidebar"] {
        background-color: #0d1127 !important;
        border-right: 1px solid rgba(0, 242, 254, 0.15);
    }
    
    /* Sidebar içindeki başlıklar */
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #00f2fe !important;
        font-family: 'Outfit', sans-serif;
    }
    
    /* Bilgi kutuları (Info alerts) */
    .stAlert {
        background-color: rgba(13, 17, 39, 0.8) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(0, 242, 254, 0.15) !important;
        border-radius: 12px !important;
    }
    
    /* Streamlit varsayılan bileşen sınır çizgileri */
    hr {
        border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sol Panel (Sidebar) - Kullanım Kılavuzu ve Bilgiler
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>⚡ NEON WAVE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Yapay Zeka Destekli Hibrit Müzik Stüdyosu</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("### 🎹 Nasıl Kullanılır?")
    st.markdown("""
    1. **Ritim Oluşturucu (Drum Pads):** 
       Izgaradaki karelere tıklayarak ritminizi tasarlayın. **"Döngüyü Başlat"** butonuna basarak ritminizin çalmasını sağlayın.
    2. **Tempo Ayarı (BPM):** 
       Tempo sürgüsünü hareket ettirerek ritminizin hızını (BPM) gerçek zamanlı değiştirin.
    3. **Sanal Synthesizer:** 
       Piyano tuşlarına mouse ile basabilir ya da klavyenizden **A, S, D, F, G, H, J, K** tuşlarını kullanarak canlı melodiler çalabilirsiniz.
    4. **Ses Karakteri:** 
       Piyanonun dalga formunu (Sine, Saw vb.) değiştirerek ses tonunu kalınlaştırıp inceltebilir, Filtre sürgüsü ile yumuşatabilirsiniz.
    """)
    
    st.write("---")
    
    st.markdown("### 🧠 Sistem Nasıl Çalışır?")
    st.info("""
    **Sıfır Gecikme Teknolojisi:** 
    Geleneksel web sitelerinde ses dosyaları sunucudan yüklenirken gecikmeler yaşanır. 
    Bu uygulamada ise sesler **Web Audio API** sayesinde tamamen tarayıcınızın (bilgisayarınızın) kendi ses kartı ve işlemcisi ile **gerçek zamanlı olarak sentezlenir**. Bu sayede hiçbir tuşta basma gecikmesi yaşanmaz!
    """)
    
    st.write("---")
    st.markdown("<p style='font-size:11px; color:#64748b; text-align:center;'>Antigravity tarafından sizin için tasarlandı ♥</p>", unsafe_allow_html=True)

# 4. Ana Panel
st.markdown("<h1 style='font-family: Outfit, sans-serif; color: #f8fafc; margin-bottom: 0;'>⚡ Çevrimiçi Ritim & Melodi Odası</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #94a3b8; margin-top: 5px; font-size: 15px;'>Tamamen tarayıcınızda sentezlenen, gecikmesiz canlı müzik stüdyosu. Ritimlerinizi programlayın ve piyano ile doğaçlama yapın!</p>", unsafe_allow_html=True)

# studio.html dosyasını okuyoruz ve Streamlit bileşeni olarak gömüyoruz
html_file_path = os.path.join(os.path.dirname(__file__), "studio.html")

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        studio_html = f.read()
    
    # HTML bileşenini sayfaya gömme
    components.html(studio_html, height=950, scrolling=False)
except FileNotFoundError:
    st.error("Hata: `studio.html` dosyası bulunamadı! Lütfen aynı dizinde olduğundan emin olun.")


