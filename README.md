GitHub'da düzgün görünmesi için README dosyanı Markdown formatına tam uygun hale getirdim. Aşağıdaki gibi düzenleyip tekrar deneyebilirsin:

md
Kopyala
Düzenle
# 📚 Flask PDF Portal

Bu proje, kullanıcıların PDF dosyalarını yükleyip indirebileceği, beğeni ve geri bildirim bırakabileceği basit bir Flask tabanlı PDF yönetim sistemidir.

## 🚀 Özellikler
- **Kullanıcı girişi ve yönetimi** (Admin desteği)
- **PDF dosyası yükleme, indirme ve dış link desteği**
- **PDF beğeni ve görüntüleme sayacı**
- **Geri bildirim (feedback) formu**
- **Site bakım modu**
- **Yönetici paneli üzerinden içerik yönetimi**

## 📂 Dizin Yapısı
📂 project-root/ ├── 📁 static/uploads # PDF ve kapak resimleri burada saklanır ├── 📁 templates # HTML şablon dosyaları │ ├── index.html # Ana sayfa │ ├── login.html # Giriş sayfası │ ├── admin.html # Admin paneli │ ├── base.html # Genel şablon │ ├── feedback.html # Geri bildirim formu │ ├── maintenance.html # Bakım modu ekranı │ ├── add_pdf.html # PDF ekleme sayfası │ ├── edit_pdf.html # PDF düzenleme sayfası │ ├── admin_feedback.html # Admin geri bildirim paneli ├── app.py # Ana uygulama dosyası ├── requirements.txt # Bağımlılık dosyası ├── README.md # Proje dokümantasyonu

perl
Kopyala
Düzenle

## 🔧 Kurulum
```sh
pip install -r requirements.txt
python app.py
🔑 Varsayılan Admin Girişi
Kullanıcı Adı: admin
Şifre: admin123
⚠️ Güvenlik Uyarısı: İlk girişten sonra şifrenizi değiştirmeniz önerilir!

📌 Kullanılan Kütüphaneler
Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug
Pillow
📞 İletişim
Herhangi bir sorun yaşarsanız lütfen proje üzerindeki Issues bölümünden bildirin. 🛠️

vbnet
Kopyala
Düzenle

Bunu kopyalayıp README.md içine yapıştırırsan GitHub'da düzenli ve düzgün görünür. Kod bloklarını, başlıkları ve madde işaretlerini tam Markdown uyumlu hale getirdim. Bi' dene bakalım, oldu mu? 😎






