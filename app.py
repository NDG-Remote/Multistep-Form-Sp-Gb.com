from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    """ content = db.Column(db.String(200), nullable=False) """
    """ completed = db.Column(db.Integer, default=0) """
    """ TO DO: I have to add all the nullable=False to the required fields like in the example above """
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    im_strasse = db.Column(db.String(200), default='0')
    im_plz = db.Column(db.String(200), default='0')
    im_ortschaft = db.Column(db.String(200), default='0')
    im_eigentuemer = db.Column(db.String(200), default='0')
    im_bemerkungen = db.Column(db.String(500), default='0')
    best_vorname = db.Column(db.String(200), default='0')
    best_nachname = db.Column(db.String(200), default='0')
    best_email = db.Column(db.String(200), default='0')
    best_tel = db.Column(db.String(200), default='0')
    best_ausweis = db.Column(db.String(200), default='0')
    best_bemerkungen = db.Column(db.String(500), default='0')
    bez_produkt_gbauszug = db.Column(db.String(200), default='0')
    bez_produkt_kataster = db.Column(db.String(200), default='0')
    bez_produkt_inhaltslegende = db.Column(db.String(200), default='0')
    bez_produkt_englisch = db.Column(db.String(200), default='0')
    bez_zahlungsart_kreditkarte = db.Column(db.String(200), default='0')
    bez_zahlungsart_paypal = db.Column(db.String(200), default='0')
    bez_agb = db.Column(db.String(200), default='0')   
    
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        """ task_content = request.form['content']
        new_task = Order(content=task_content) """
        content_im_strasse = request.form['Strasse']
        new_im_strasse = Order(im_strasse=content_im_strasse)
        content_im_plz = request.form['Postleitzahl']
        new_im_plz = Order(im_plz=content_im_plz)
        content_im_ortschaft = request.form['Ortschaft']
        new_im_ortschaft = Order(im_ortschaft=content_im_ortschaft)
        content_im_eigentuemer = request.form['Eigentuemer']
        new_im_eigentuemer = Order(im_eigentueme=content_im_eigentuemer)
        content_im_bemerkungen = request.form['Bemerkungen']
        new_im_bemerkungen = Order(im_bemerkungen=content_im_bemerkungen)
        content_best_vorname = request.form['Vorname']
        new_best_vorname = Order(best_vorname=content_best_vorname)
        content_best_nachname = request.form['Nachname']
        new_best_nachname = Order(best_nachname=content_best_nachname)
        content_best_email = request.form['E-mail']
        new_best_email = Order(best_email=content_best_email)
        content_best_tel = request.form['Telefonnummer']
        new_best_tel = Order(best_tel=content_best_tel)
        content_best_ausweis = request.form['Ausweisnummer']
        new_best_ausweis = Order(best_ausweis=content_best_ausweis)
        content_best_bemerkungen = request.form['Rechnungsvermerke']
        new_best_bemerkungen = Order(best_bemerkungen=content_best_bemerkungen)
        content_bez_produkt_gbauszug = request.form['Check-Grundbuchauszug']
        new_bez_produkt_gbauszug = Order(bez_produkt_gbauszug=content_bez_produkt_gbauszug)
        content_bez_produkt_kataster = request.form['Check-Katasterplan']
        new_bez_produkt_kataster = Order(bez_produkt_kataster=content_bez_produkt_kataster)
        content_bez_produkt_inhaltslegende = request.form['Check-Inhaltslegende-DE']
        new_bez_produkt_inhaltslegende = Order(bez_produkt_inhaltslegende=content_bez_produkt_inhaltslegende)
        content_bez_produkt_englisch = request.form['Check-Uebersetzung-EN']
        new_bez_produkt_englisch = Order(bez_produkt_englisch=content_bez_produkt_englisch)
        content_bez_zahlungsart_kreditkarte = request.form['Zahlungsart-Kreditkarte']
        new_bez_zahlungsart_kreditkarte = Order(bez_zahlungsart_kreditkarte=content_bez_zahlungsart_kreditkarte)
        content_bez_zahlungsart_paypal = request.form['Zahlungsart-Paypal']
        new_bez_zahlungsart_paypal = Order(bez_zahlungsart_paypal=content_bez_zahlungsart_paypal)
        content_bez_agb = request.form['AGB-Datenschutz-Akzeptiert']
        new_bez_agb = Order(bez_agb=content_bez_agb)
        
        try:
            """ db.session.add(new_task) """
            db.session.add(new_im_strasse)
            db.session.add(new_im_plz)
            db.session.add(new_im_ortschaft)
            db.session.add(new_im_eigentuemer)
            db.session.add(new_im_bemerkungen)
            db.session.add(new_best_vorname)
            db.session.add(new_best_nachname)
            db.session.add(new_best_email)
            db.session.add(new_best_tel)
            db.session.add(new_best_ausweis)
            db.session.add(new_best_bemerkungen)
            db.session.add(new_bez_produkt_gbauszug)
            db.session.add(new_bez_produkt_kataster)
            db.session.add(new_bez_produkt_inhaltslegende)
            db.session.add(new_bez_produkt_englisch)
            db.session.add(new_bez_zahlungsart_kreditkarte)
            db.session.add(new_bez_zahlungsart_paypal)
            db.session.add(new_bez_agb)
            db.session.commit()
            return render_template('/success')
        except:
            return 'There was an issue, adding your order'
        
    else:
        tasks = Order.query.order_by(Order.data_created).all
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
