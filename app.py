from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pdfs.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Lütfen giriş yapın!'
login_manager.login_message_category = 'info'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class PDF(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    filename = db.Column(db.String(200))  # Optional now
    cover_image = db.Column(db.String(200))
    external_link = db.Column(db.String(500))  # New field for external PDF links
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(200), default="YKS PDF Portalı")
    maintenance_mode = db.Column(db.Boolean, default=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Auth routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Başarıyla giriş yaptınız!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page if next_page else url_for('index'))
        else:
            flash('Kullanıcı adı veya şifre hatalı!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Başarıyla çıkış yaptınız!', 'success')
    return redirect(url_for('index'))

# Main routes
@app.route('/')
def index():
    settings = SiteSettings.query.first()
    if settings and settings.maintenance_mode and not (current_user.is_authenticated and current_user.is_admin):
        return render_template('maintenance.html')
    
    search = request.args.get('search', '')
    pdfs = PDF.query
    if search:
        pdfs = pdfs.filter(PDF.title.contains(search) | PDF.description.contains(search))
    pdfs = pdfs.order_by(PDF.upload_date.desc()).all()
    return render_template('index.html', pdfs=pdfs, search=search, settings=settings)

@app.route('/pdf/<int:id>')
def view_pdf(id):
    pdf = PDF.query.get_or_404(id)
    pdf.views += 1
    db.session.commit()
    if pdf.external_link:
        return redirect(pdf.external_link)
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename))

@app.route('/like/<int:id>')
def like_pdf(id):
    pdf = PDF.query.get_or_404(id)
    pdf.likes += 1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = Feedback(
            name=request.form['name'],
            email=request.form['email'],
            message=request.form['message']
        )
        db.session.add(feedback)
        db.session.commit()
        flash('Mesajınız başarıyla gönderildi!', 'success')
        return redirect(url_for('index'))
    return render_template('feedback.html')

# Admin routes
@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('Bu sayfaya erişim yetkiniz yok!', 'error')
        return redirect(url_for('index'))
    pdfs = PDF.query.all()
    settings = SiteSettings.query.first()
    unread_feedback = Feedback.query.filter_by(is_read=False).count()
    return render_template('admin.html', pdfs=pdfs, settings=settings, unread_feedback=unread_feedback)

@app.route('/admin/pdf/add', methods=['GET', 'POST'])
@login_required
def add_pdf():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        cover_image = request.files['cover']
        cover_filename = None
        
        if cover_image:
            cover_filename = f"cover_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            cover_image.save(os.path.join(app.config['UPLOAD_FOLDER'], cover_filename))
        
        new_pdf = PDF(
            title=request.form['title'],
            description=request.form['description'],
            cover_image=cover_filename,
            external_link=request.form.get('external_link')
        )
        
        if 'pdf' in request.files and request.files['pdf'].filename:
            pdf_file = request.files['pdf']
            pdf_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
            pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename))
            new_pdf.filename = pdf_filename
        
        db.session.add(new_pdf)
        db.session.commit()
        
        flash('PDF başarıyla eklendi!', 'success')
        return redirect(url_for('admin'))
            
    return render_template('add_pdf.html')

@app.route('/admin/pdf/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_pdf(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    pdf = PDF.query.get_or_404(id)
    
    if request.method == 'POST':
        pdf.title = request.form['title']
        pdf.description = request.form['description']
        pdf.external_link = request.form.get('external_link')
        
        cover_image = request.files.get('cover')
        if cover_image and cover_image.filename:
            if pdf.cover_image:
                try:
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], pdf.cover_image))
                except:
                    pass
            cover_filename = f"cover_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            cover_image.save(os.path.join(app.config['UPLOAD_FOLDER'], cover_filename))
            pdf.cover_image = cover_filename
        
        pdf_file = request.files.get('pdf')
        if pdf_file and pdf_file.filename:
            if pdf.filename:
                try:
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename))
                except:
                    pass
            pdf_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
            pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename))
            pdf.filename = pdf_filename
        
        db.session.commit()
        flash('PDF başarıyla güncellendi!', 'success')
        return redirect(url_for('admin'))
    
    return render_template('edit_pdf.html', pdf=pdf)

@app.route('/admin/pdf/delete/<int:id>')
@login_required
def delete_pdf(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    pdf = PDF.query.get_or_404(id)
    if pdf.filename:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename))
        except:
            pass
    if pdf.cover_image:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], pdf.cover_image))
        except:
            pass
    
    db.session.delete(pdf)
    db.session.commit()
    
    flash('PDF başarıyla silindi!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/settings', methods=['POST'])
@login_required
def update_settings():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    settings = SiteSettings.query.first()
    if not settings:
        settings = SiteSettings()
        db.session.add(settings)
    
    settings.site_name = request.form.get('site_name', settings.site_name)
    settings.maintenance_mode = 'maintenance_mode' in request.form
    
    db.session.commit()
    flash('Ayarlar başarıyla güncellendi!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/feedback')
@login_required
def admin_feedback():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    feedbacks = Feedback.query.order_by(Feedback.date.desc()).all()
    return render_template('admin_feedback.html', feedbacks=feedbacks)

@app.route('/admin/feedback/mark-read/<int:id>')
@login_required
def mark_feedback_read(id):
    if not current_user.is_admin:
        return redirect(url_for('index'))
    
    feedback = Feedback.query.get_or_404(id)
    feedback.is_read = True
    db.session.commit()
    return redirect(url_for('admin_feedback'))

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', 
                        password=generate_password_hash('admin123'),
                        is_admin=True)
            db.session.add(admin)
            if not SiteSettings.query.first():
                settings = SiteSettings()
                db.session.add(settings)
            db.session.commit()
    app.run(debug=True)