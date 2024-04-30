from app.models import ModelMahasiswa
from app.view import Display

class MahasiswaController:
    def __init__(self):
        self.model = ModelMahasiswa('ratu', 10123215)
        self.view = Display()

    def set_nama(self, nama):
        self.model.nama = nama
    
    def set_nim(self, nim):
        self.model.nim = nim

    def updateView(self):
        return self.view.show(self.model)
    

    