📚 Flask PDF Portal

Bu proje, kullanıcıların PDF dosyalarını yükleyip indirebileceği, beğeni ve geri bildirim bırakabileceği basit bir Flask tabanlı PDF yönetim sistemidir.

🚀 Özellikler
--Kullanıcı girişi ve yönetimi (Admin desteği)
--PDF dosyası yükleme, indirme ve dış link desteği
--PDF beğeni ve görüntüleme sayacı
--Geri bildirim (feedback) formu
--Site bakım modu
--Yönetici paneli üzerinden içerik yönetimi

📂 Dizin Yapısı
├── 📁 static/uploads      # PDF ve kapak resimleri burada saklanır
├── 📁 templates           # HTML şablon dosyaları
│   ├── index.html        # Ana sayfa
│   ├── login.html        # Giriş sayfası
│   ├── admin.html        # Admin paneli
│   ├── base.html         # base
│   ├── feedback.html     # Geri bildirim formu
│   ├── maintenance.html  # Bakım modu ekranı
│   ├── add_pdf.html      # PDF ekleme sayfası
│   ├── edit_pdf.html     # PDF düzenleme sayfası
│   ├── admin_feedback.html # Admin geri bildirim paneli
├── app.py                # Ana uygulama dosyası
├── requirements.txt      # Bağımlılık dosyası
├── README.md             # Proje dokümantasyonu

🔧 Kurulum
-pip install -r requirements.txt
-python app.py

🔑 Varsayılan Admin Girişi
-Kullanıcı Adı: admin
-Şifre: admin123
Güvenlik Uyarısı: İlk girişten sonra şifreyi değiştirmeniz önerilir!

📌 Kullanılan Kütüphaneler
-Flask
-Flask-SQLAlchemy
-Flask-Login
-Werkzeug
-Pillow

📞 İletişim
Herhangi bir sorun yaşarsanız lütfen proje üzerindeki Issues bölümünden bildirin. 🛠️

