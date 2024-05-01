from app.model import Mahasiswa, Dosen
from app.view import ViewDosen, ViewMahasiswa

class Controller:
    def __init__(self,):
        self.modelMahasiswa = Mahasiswa('ratu', 10123215, 'Teknik Informatika')
        self.modelDosen = Dosen('Andri Heryadi', 16378546)
        self.viewMahasiswa = ViewMahasiswa()
        self.viewDosen = ViewDosen()

    def set_nama(self, nama, model):
        if model == 'mahasiswa':
            self.modelMahasiswa.nama = nama
        elif model == 'dosen':
            self.modelDosen.nama = nama

    def set_nim(self, nim):
        self.modelMahasiswa.nim = nim
    
    def set_nip(self, nip):
        self.modelDosen.nip = nip

    def set_prodi(self, prodi):
        self.modelMahasiswa.prodi = prodi

    # def updateView_mhs(self):
    #     return self.viewMahasiswa.show(self.modelMahasiswa)
    
    # def updateView_dsn(self):
    #     return self.viewDosen.show(self.modelDosen)

    def updateView(self, model):
        if model == 'mahasiswa':
            return self.viewMahasiswa.show(self.modelMahasiswa)
        elif model == 'dosen':
            return self.viewDosen.show(self.modelDosen)
        else:
            return 'Jenis model tidak valid'
