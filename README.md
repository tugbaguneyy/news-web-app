# Django Haber Sitesi (News Website)  
Modern, temiz mimariye sahip, NewsAPI destekli Django haber sitesi uygulaması.

---

## 🏗️ Genel Proje Yapısı (Project Structure)

```

news-web-app/
├── .env                          # Ortam değişkenleri (API anahtarları, gizli bilgiler)
├── requirements.txt              # Python bağımlılıkları listesi
├── manage.py                     # Django yönetim komutları için ana script
├── db.sqlite3                    # SQLite veritabanı dosyası
├── news\_site/                    # Ana Django projesi klasörü
│   ├── **init**.py
│   ├── settings.py               # Proje ayarları
│   ├── urls.py                   # URL yönlendirmeleri
│   ├── wsgi.py                   # WSGI yapılandırması
│   └── asgi.py                   # ASGI yapılandırması
└── news/                         # Haber uygulaması
├── **init**.py
├── admin.py                  # Admin panel ayarları
├── apps.py                   # Uygulama konfigürasyonu
├── models.py                 # Veritabanı modelleri (şimdilik kullanılmıyor)
├── views.py                  # HTTP istek/yanıt işlemleri
├── urls.py                   # Uygulama URL yönlendirmeleri
├── tests.py                  # Unit testler
├── services/                 # İş mantığı katmanı
│   ├── **init**.py
│   └── news\_service.py       # NewsAPI entegrasyonu
├── serializers/              # Veri dönüşüm katmanı
│   ├── **init**.py
│   └── news\_serializer.py    # API verilerini frontend’e uygun hale getirme
├── utils/                    # Yardımcı fonksiyonlar
│   ├── **init**.py
│   └── constants.py          # Sabitler ve yapılandırmalar
└── templates/                # HTML şablonları
└── news/
├── base.html         # Ana template
└── index.html        # Haber listesi template’i

````

---

### Ana Proje Dosyaları (news\_site/)

* **`settings.py`**
  Django projesinin temel ayarları (veritabanı, uygulamalar, API anahtarları, cache, loglama vb.)

* **`urls.py`**
  Projenin ana URL yönlendirmeleri, app URL’lerinin dahil edilmesi.

### Haber Uygulaması (news/)

* **`views.py`**
  HTTP istek ve yanıt işlemleri, sayfa görüntüleme, API endpoint’leri.
  (Class-based view kullanımı ve paginasyon destekli)

* **`urls.py`**
  Haber uygulamasına ait URL yönlendirmeleri.

### İş Mantığı Katmanı (services/)

* **`news_service.py`**
  NewsAPI ile iletişim kurar, veri çeker, önbellekleme yapar.

### Veri Dönüşüm Katmanı (serializers/)

* **`news_serializer.py`**
  API’den gelen ham veriyi, frontend için uygun yapıya dönüştürür.

### Yardımcı Fonksiyonlar (utils/)

* **`constants.py`**
  Uygulamada kullanılan sabitler ve kategori isimleri gibi genel veriler.

### Şablonlar (templates/)

* **`base.html`**
  Ortak sayfa yapısı, navbar, footer, stil ve script dosyaları içerir.

* **`index.html`**
  Ana sayfadaki haber kartlarını listeler.

---

## 🎯 Clean Code ve Mimari Prensipler (Best Practices)

* **Separation of Concerns:** View'lar sadece HTTP işlemleri yapar, servisler iş mantığını yönetir.
* **Single Responsibility:** Her modül sadece kendi sorumluluğuna odaklanır.
* **DRY:** Tekrarlardan kaçınılır, sabitler constants.py’de toplanır.
* **Hata Yönetimi:** API çağrılarında hata ve istisna yakalama.
* **Caching:** Haber verileri 15 dakika önbelleğe alınır, böylece API yükü azaltılır.
* **Güvenlik:** API anahtarları `.env` içinde gizli tutulur, CSRF ve SQL injection’a karşı önlemler alınır.

---

## 🚀 Projeyi Çalıştırma (Setup & Run)

1. Sanal ortam oluştur ve aktif et:

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

2. Bağımlılıkları yükle:

```bash
pip install -r requirements.txt
```

3. Veritabanı migrasyonlarını uygula:

```bash
python manage.py migrate
```

4. Geliştirme sunucusunu başlat:

```bash
python manage.py runserver
```

---
