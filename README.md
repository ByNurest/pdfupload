# 📚 Flask PDF Portal

Bu proje, kullanıcıların PDF dosyalarını yükleyip indirebileceği, beğeni ve geri bildirim bırakabileceği basit ama güçlü bir Flask tabanlı PDF yönetim sistemidir. Hem kullanıcı dostu hem de yönetici odaklı özelliklerle dolu! 😎

---

## 🌟 Özellikler

- **Kullanıcı Girişi ve Yönetimi**: Admin ve normal kullanıcı desteği.  
- **PDF Yükleme & İndirme**: Dosyaları kolayca yükle, indir veya dış link ekle.  
- **Beğeni ve Görüntüleme Sayacı**: PDF’lerin popülerliğini ölç!  
- **Geri Bildirim Formu**: Kullanıcılar düşüncelerini paylaşabilir.  
- **Site Bakım Modu**: Güncellemeler için siteyi geçici olarak kapat.  
- **Yönetici Paneli**: İçerik ve kullanıcı yönetimi için güçlü bir arayüz.  

---

## 📦 Kurulum

Projenin çalışması için aşağıdaki adımları takip edin. Her şey adım adım açıklanmıştır! 🚀

### 1. Depoyu Klonlama
Öncelikle projeyi klonlayın:

```sh
git clone https://github.com/kullanici_adin/proje_adin.git
cd proje_adin

2. Sanal Ortam Oluşturma (Önerilir)
Sanal ortam oluşturmak için aşağıdaki komutları çalıştırın:
sh

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Bağımlılıkları Yükleme
Gerekli kütüphaneleri yüklemek için:
sh

pip install -r requirements.txt

4. Uygulamayı Başlatma
Uygulamayı çalıştırmak için aşağıdaki komutu kullanın:
sh

python app.py

 Varsayılan Admin Girişi
Uygulamayı ilk çalıştırdığınızda aşağıdaki bilgileri kullanarak yönetici paneline erişebilirsiniz:
plaintext

Kullanıcı Adı: admin
Şifre: admin123

 Güvenlik Uyarısı: İlk girişten sonra şifrenizi mutlaka değiştirin!
 Kullanılan Kütüphaneler
Bu projede kullanılan temel kütüphaneler:
Flask: Web framework  

Flask-SQLAlchemy: Veritabanı yönetimi  

Flask-Login: Kullanıcı oturum yönetimi  

Werkzeug: Güvenlik ve yardımcı araçlar  

Pillow: Görsel işlemleri

 İletişim ve Katkı
Herhangi bir sorunla karşılaşırsanız veya katkıda bulunmak isterseniz:  
Sorun Bildirme: Issues  

Katkıda Bulunma: Pull Request’ler her zaman açıktır! 

