from flask import Flask, request
from model import ModelMahasiswa
from view import  Display
from controller import MahasiswaController


def mahasiswa(nama,nim):
    mahasiswa = ModelMahasiswa(nama,nim)
    view = Display()
    controller = MahasiswaController(mahasiswa,view)

    if request.method == "POST":
        controller.set_nama(request.form["nama"])
        controller.set_nim(request.form["nim"])

    return controller.update_view()

app = Flask("Aplikasi Awal")

@app.route("/", methods=["GET","POST"])

if __name__ == "__main__":
    app.run()