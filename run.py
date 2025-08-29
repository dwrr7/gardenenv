from flask import Flask, render_template, request, redirect, url_for
from database import get_db, close_db  # fungsi untuk koneksi database

app = Flask(__name__)
app.teardown_appcontext(close_db)  # koneksi db ditutup otomatis setelah request selesai


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_data = None
    flag = False

    if request.method == "POST":  # user klik tombol kirim
        nama = request.form.get("nama")
        email = request.form.get("email")
        pesan = request.form.get("pesan")

        db = get_db()
        db.execute(
            "INSERT INTO CONTACT (nama, email, pesan) VALUES (?, ?, ?)",
            (nama, email, pesan)
        )
        db.commit()  # simpan ke database

        contact_data = {"nama": nama, "email": email, "pesan": pesan}
        flag = True

    return render_template("contact.html", flag=flag, contact=contact_data)



@app.route("/news")
def news():
    db = get_db()
    news = db.execute("SELECT * FROM news").fetchall()   

    return render_template("news.html", news=news)

@app.route("/temperature")
def temperature():
    return "It works!"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1",port=8000)