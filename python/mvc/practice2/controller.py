from flask import Flask, request

class MahasiswaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def set_nama(self,nama):
        self.model.nama = nama
    def set_nim(self,nim):
        self.model.nim = nim
    def update_view(self):
        return self.view.show(self.model)

