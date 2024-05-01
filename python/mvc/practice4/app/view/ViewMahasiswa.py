from flask import Flask, render_template

class ViewMahasiswa:
    def show(self, mahasiswa):
        return render_template("mahasiswa.html", mahasiswa=mahasiswa)