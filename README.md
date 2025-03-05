Flask PDF Portal - README

Proje Hakkında

Bu proje, kullanıcıların PDF dosyalarını yükleyip paylaşabileceği bir web uygulamasıdır. Kullanıcılar hesap oluşturabilir, giriş yapabilir, PDF'leri görüntüleyebilir, beğenebilir ve geri bildirimde bulunabilir. Adminler ise PDF yönetimi, site ayarları ve geri bildirimleri kontrol edebilir.

Kullanılan Teknolojiler

Flask

Flask-SQLAlchemy

Flask-Login

SQLite

HTML, CSS, Bootstrap

Werkzeug

Pillow

Kurulum

1. Depoyu Klonlayın

git clone https://github.com/kullaniciadi/projeadi.git
cd projeadi

2. Sanal Ortamı Oluşturun ve Aktifleştirin

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\\Scripts\\activate

3. Gerekli Paketleri Yükleyin

pip install -r requirements.txt

4. Veritabanını Başlatın

python app.py

Uygulama ilk kez çalıştırıldığında pdfs.db veritabanı otomatik olarak oluşturulacaktır.

Dizin Yapısı

projeadi/
│── static/
│   ├── uploads/          # PDF ve kapak resimlerinin saklandığı klasör
│   ├── css/              # Stil dosyaları
│   ├── js/               # JavaScript dosyaları
│
│── templates/
│   ├── index.html        # Ana sayfa
│   ├── login.html        # Giriş sayfası
│   ├── admin.html        # Admin paneli
│   ├── add_pdf.html      # PDF ekleme sayfası
│   ├── edit_pdf.html     # PDF düzenleme sayfası
│   ├── feedback.html     # Geri bildirim formu
│   ├── admin_feedback.html  # Admin geri bildirim yönetimi
│   ├── maintenance.html  # Bakım modu sayfası
│
│── app.py                # Flask uygulamasının ana dosyası
│── requirements.txt       # Bağımlılıkları içeren dosya
│── README.md              # Bu dosya
│── config.py              # Uygulama yapılandırma ayarları (geliştirme, prod vs.)

Kullanıcı İşlevleri

Kullanıcı kaydı ve girişi

PDF arama ve görüntüleme

Beğenme ve indirme

Geri bildirim gönderme

Admin İşlevleri

PDF ekleme, düzenleme ve silme

Site ayarlarını değiştirme

Kullanıcı geri bildirimlerini yönetme

Varsayılan Admin Girişi

Kullanıcı Adı: admin
Şifre: admin123

İlk çalıştırmada otomatik olarak admin hesabı oluşturulacaktır. Daha sonra app.py içinde generate_password_hash() fonksiyonu kullanılarak admin şifresi değiştirilebilir.

Çalıştırma

python app.py

Uygulama varsayılan olarak http://127.0.0.1:5000/ adresinde çalışacaktır.

Sorunsuz bir şekilde kullanabilmen için her şeyi ayarladım. İyi kodlamalar! 🚀
