# ⚡ Neon Wave Studio - Streamlit Müzik Stüdyosu

Bu proje, kodlama veya müzik prodüksiyonu hakkında **hiçbir şey bilmeseniz dahi** kendi bilgisayarınızda kolayca çalıştırabileceğiniz ve internete tamamen ücretsiz yükleyebileceğiniz basitleştirilmiş bir **çevrimiçi ritim ve melodi stüdyosudur**.

Saniyeler içinde kendi ritimlerinizi tasarlayabilir, piyano çalarak melodiler ekleyebilir ve yaptığınız müziğin ses dalgalarını ekranınızda canlı olarak görebilirsiniz!

---

## 🛠️ Bölüm 1: Bilgisayarınızda Çalıştırma Rehberi (Adım Adım)

Hiç kodlama bilmiyorsanız endişelenmeyin! Aşağıdaki adımları sırayla takip etmeniz yeterlidir.

### Adım 1: Python'ı Bilgisayarınıza Yükleyin
Uygulamanın çalışması için bilgisayarınızda **Python** programlama dilinin yüklü olması gerekir.
1. [Python Resmi Web Sitesi'ne](https://www.python.org/downloads/) gidin.
2. Sarı renkli **"Download Python 3.x.x"** butonuna tıklayarak kurulum dosyasını indirin.
3. İndirdiğiniz dosyayı çalıştırın.
4. **ÇOK ÖNEMLİ:** Kurulum penceresinin en altında bulunan **"Add python.exe to PATH"** seçeneğinin yanındaki kutucuğu mutlaka işaretleyin!
5. **"Install Now"** butonuna tıklayarak kurulumu tamamlayın.

### Adım 2: Proje Klasörünü Açın
1. Bilgisayarınızda `C:\Users\pc\.gemini\antigravity\scratch\streamlit-music-studio` klasörüne gidin (Uygulamanın tüm dosyaları buradadır).

### Adım 3: Terminali (Komut İstemini) Açın
1. Klasörün boş bir yerinde `Shift` tuşuna basılı tutarak sağ tıklayın ve **"PowerShell Penceresini Buradan Açın"** veya **"Komut İstemini Buradan Açın"** deyin.
2. Veya Windows arama çubuğuna `cmd` yazıp Enter tuşuna basarak siyah terminali açın, ardından şu komutu yazıp klasöre gidin:
   ```bash
   cd C:\Users\pc\.gemini\antigravity\scratch\streamlit-music-studio
   ```

### Adım 4: Gerekli Kütüphaneyi (Streamlit) Yükleyin
Terminal ekranına aşağıdaki komutu kopyalayıp yapıştırın ve `Enter` tuşuna basın (İnternet bağlantınız olmalıdır):
```bash
pip install streamlit
```
*Bu komut, uygulamanın çalışması için gereken Streamlit altyapısını otomatik olarak bilgisayarınıza kuracaktır.*

### Adım 5: Uygulamayı Başlatın!
Kurulum bittikten sonra terminale şu komutu yazın ve `Enter` tuşuna basın:
```bash
streamlit run app.py
```
**Tebrikler!** Tarayıcınızda (Chrome, Edge vb.) müzik stüdyonuz otomatik olarak açılacaktır. Eğer açılmazsa terminal ekranında yazan `http://localhost:8501` adresini tarayıcınıza kopyalayabilirsiniz.

---

## 🚀 Bölüm 2: Web Sitenizi İnternette Ücretsiz Yayınlayın (Canlıya Alın)

Web sitenizi tüm arkadaşlarınızın ve internetteki herkesin girip çalabileceği bir canlı web sitesi yapmak ister misiniz? Üstelik tamamen ücretsiz!

### Adım 1: GitHub Hesabı Açın ve Dosyaları Yükleyin
1. [GitHub](https://github.com/) adresine gidip ücretsiz bir hesap oluşturun.
2. Sağ üstteki **"+"** işaretine tıklayıp **"New repository"** (Yeni Depo) deyin.
3. Deponuza bir isim verin (Örn: `neon-wave-studio`) ve alttaki **"Create repository"** butonuna tıklayın.
4. Çıkan ekrandaki yükleme yönergelerini kullanarak veya dosyaları doğrudan tarayıcınızdan sürükleyip bırakarak (uploading an existing file) klasörünüzdeki şu 4 dosyayı yükleyin:
   - `app.py`
   - `studio.html`
   - `requirements.txt`
   - `README.md`
5. Sayfanın altındaki yeşil **"Commit changes"** butonuna basın.

### Adım 2: Streamlit Share'e Bağlayın
1. [Streamlit Community Cloud](https://share.streamlit.io/) sitesine gidin.
2. **"Sign in with GitHub"** butonuna basarak GitHub hesabınızla giriş yapın.
3. Giriş yaptıktan sonra **"Create app"** veya **"New app"** butonuna tıklayın.
4. **Repository** alanında az önce GitHub'da oluşturduğunuz depoyu seçin (Örn: `neon-wave-studio`).
5. **Main file path** kısmına `app.py` yazılı olduğundan emin olun.
6. Alt taraftaki **"Deploy!"** butonuna tıklayın.

**İşte bu kadar!** Yaklaşık 1 dakika içinde uygulamanız kurulacak ve size `https://neon-wave-studio.streamlit.app` gibi benzersiz bir canlı web sitesi linki verilecektir. Bu linki dilediğiniz kişiyle paylaşabilirsiniz!

---

## 🎵 Eğlenceye Başlayın!
- **Ritim Kareleri:** Karelere tıklayarak kendi ritimlerinizi tasarlayın, tempo kaydırıcısıyla hızlandırın.
- **Piyano:** Klavyenizdeki **A, S, D, F, G, H, J, K** tuşlarını birer piyano tuşu gibi kullanıp canlı sololar çalın!
- **Görsel Şölen:** Yaptığınız müzikle senkronize bir şekilde parıldayan neon ses dalgalarının keyfini çıkarın.
