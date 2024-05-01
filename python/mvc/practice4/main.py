from flask import Flask, request
from app.controller import Controller

app = Flask("Aplikasi Sederhana")

# route mahasiswa
@app.route("/mahasiswa", methods=["GET","POST"])
def mahasiswa():
    controller = Controller()

    if request.method == "POST":
        controller.set_nama(request.form["nama"], 'mahasiswa')
        controller.set_nim(request.form["nim"])
        controller.set_prodi(request.form["prodi"])

    return controller.updateView('mahasiswa')

# route dosen
@app.route("/mahasiswa/dosen", methods=["GET","POST"])
def dosen():
    controller = Controller()

    if request.method == "POST":
        controller.set_nama(request.form["nama"], 'dosen')
        controller.set_nip(request.form["nip"])

    return controller.updateView('dosen')

# app run
if __name__ == "__main__":
    app.run()