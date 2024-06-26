from flask import Flask, request
from controller import MahasiswaController

app = Flask("Aplikasi Awal")

@app.route("/coba", methods=["GET","POST"])

def mahasiswa():
    controller = MahasiswaController()

    if request.method == "POST":
        controller.set_nama(request.form["nama"])
        controller.set_nim(request.form["nim"])

    return controller.update_view()

if __name__ == "__main__":
    app.run()