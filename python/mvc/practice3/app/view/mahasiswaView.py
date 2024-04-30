from flask import Flask, render_template

class Display:
    def show(self, mahasiswa):
        return render_template("latihan.html", mahasiswa=mahasiswa)