from flask import Flask, request
from app.controller import MahasiswaController

app = Flask("Aplikasi Mahasiswa Bodong")

@app.route("/latihan", methods=["GET","POST"])

def mahasiswa():
    controller = MahasiswaController()

    if request.method == "POST":
        controller.set_nama(request.form["nama"])
        controller.set_nim(request.form["nim"])

    return controller.updateView()

if __name__ == "__main__":
    app.run()