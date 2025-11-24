# TechIstPyBootcampProject_Basit_Hava_Durumu_Portali

# 🌤️ Basit Hava Durumu Portalı

Bu proje Flask ile oluşturulmuş basit bir hava durumu uygulamasıdır.

## 🚀 Özellikler
- Kullanıcıdan şehir adı alma
- OpenWeatherMap API ile hava durumu verisi çekme
- JSON çözümleme
- Jinja2 ile sonuçların ekrana basılması
- Hatalı giriş / API hatası yönetimi
- .env ile güvenli API anahtarı

---

## 📦 Kurulum

### 1. Depoyu klonla
git clone https://github.com/kullanici/weather-app.git

### 2. Gerekli paketleri kur
pip install -r requirements.txt

### 3. `.env` oluştur
`.env.example` dosyasını kopyalayarak:
cp .env.example .env

Ve API anahtarını ekleyin:
OPENWEATHER_API_KEY=your_api_key_here


---

## ▶️ Uygulamayı Başlat

```bash
python app.py

Tarayıcıda aç:
http://127.0.0.1:5000

🛡️ Hata Yönetimi

Yanlış şehir adı → Uyarı mesajı

İnternet problemi → Uyarı mesajı

📄 Lisans

MIT

# 🚀 **VS CODE’DA NASIL ÇALIŞTIRIRSIN (adım adım)**

1️⃣ **VS Code aç → File → Open Folder → `weather-app` klasörünü seç**  
2️⃣ Terminal aç → **virtual environment oluştur**

Windows:
```bash
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Gerekli kütüphaneleri yükle
pip install -r requirements.txt

4️⃣ Proje köküne .env oluştur
OPENWEATHER_API_KEY=xxx_senin_api_key_xxx

5️⃣ Çalıştır:
python app.py

6️⃣ Tarayıcıya git:
http://127.0.0.1:5000



