from flask import Flask, render_template

class ViewDosen:
    def show(self, dosen):
        return render_template("dosen.html", dosen=dosen)