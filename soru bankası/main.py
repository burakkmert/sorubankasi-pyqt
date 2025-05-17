import sys
import json
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class SoruBankasi(QtWidgets.QMainWindow):
    def __init__(self):
        super(SoruBankasi, self).__init__()
        # UI dosyasını yükle
        uic.loadUi('soru_bankasi.ui', self)
        
        # Soru listesi
        self.sorular = []
        
        # Dosya yolu
        self.veri_dosyasi = "sorular.json"
        
        # Verileri yükle
        self.verileri_yukle()
        
        # Buton bağlantıları
        self.btn_soru_ekle.clicked.connect(self.soru_ekle)
        self.btn_soru_sil.clicked.connect(self.soru_sil)
        self.btn_soru_goster.clicked.connect(self.soru_goster)
        
        # Tabloyu güncelle
        self.tabloya_yukle()
    
    def verileri_yukle(self):
        """Soruları JSON dosyasından yükler"""
        if os.path.exists(self.veri_dosyasi):
            try:
                with open(self.veri_dosyasi, 'r', encoding='utf-8') as f:
                    self.sorular = json.load(f)
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Veriler yüklenirken hata: {str(e)}")
    
    def verileri_kaydet(self):
        """Soruları JSON dosyasına kaydeder"""
        try:
            with open(self.veri_dosyasi, 'w', encoding='utf-8') as f:
                json.dump(self.sorular, f, ensure_ascii=False, indent=4)
        except Exception as e:
            QMessageBox.warning(self, "Hata", f"Veriler kaydedilirken hata: {str(e)}")
    
    def soru_ekle(self):
        """Yeni soru ekler"""
        soru_metni = self.txt_soru.toPlainText().strip()
        dogru_cevap = self.txt_dogru_cevap.text().strip()
        a_sikki = self.txt_a_sikki.text().strip()
        b_sikki = self.txt_b_sikki.text().strip()
        c_sikki = self.txt_c_sikki.text().strip()
        d_sikki = self.txt_d_sikki.text().strip()
        
        if not soru_metni or not dogru_cevap:
            QMessageBox.warning(self, "Uyarı", "Soru metni ve doğru cevap girilmelidir.")
            return
        
        # Doğru cevabı seçme
        dogru_sik = ""
        if self.radio_a.isChecked():
            dogru_sik = "A"
        elif self.radio_b.isChecked():
            dogru_sik = "B"
        elif self.radio_c.isChecked():
            dogru_sik = "C"
        elif self.radio_d.isChecked():
            dogru_sik = "D"
        else:
            QMessageBox.warning(self, "Uyarı", "Doğru şık seçilmelidir.")
            return
        
        # Yeni soru oluştur
        yeni_soru = {
            "soru": soru_metni,
            "a_sikki": a_sikki,
            "b_sikki": b_sikki,
            "c_sikki": c_sikki,
            "d_sikki": d_sikki,
            "dogru_sik": dogru_sik,
            "dogru_cevap": dogru_cevap
        }
        
        # Soruyu listeye ekle
        self.sorular.append(yeni_soru)
        
        # Verileri kaydet
        self.verileri_kaydet()
        
        # Tabloyu güncelle
        self.tabloya_yukle()
        
        # Alanları temizle
        self.formu_temizle()
        
        QMessageBox.information(self, "Bilgi", "Soru başarıyla eklendi.")
    
    def soru_sil(self):
        """Seçili soruyu siler"""
        secili_satirlar = self.tablo_sorular.selectedItems()
        
        if not secili_satirlar:
            QMessageBox.warning(self, "Uyarı", "Lütfen silinecek bir soru seçin.")
            return
        
        secili_satir = secili_satirlar[0].row()
        
        # Onay mesajı
        cevap = QMessageBox.question(self, "Onay", 
                                    "Seçili soruyu silmek istediğinize emin misiniz?",
                                    QMessageBox.Yes | QMessageBox.No)
        
        if cevap == QMessageBox.Yes:
            # Soruyu sil
            del self.sorular[secili_satir]
            
            # Verileri kaydet
            self.verileri_kaydet()
            
            # Tabloyu güncelle
            self.tabloya_yukle()
            
            QMessageBox.information(self, "Bilgi", "Soru başarıyla silindi.")
    
    def soru_goster(self):
        """Seçili soruyu gösterir"""
        secili_satirlar = self.tablo_sorular.selectedItems()
        
        if not secili_satirlar:
            QMessageBox.warning(self, "Uyarı", "Lütfen görüntülenecek bir soru seçin.")
            return
        
        secili_satir = secili_satirlar[0].row()
        secili_soru = self.sorular[secili_satir]
        
        # Formu doldur
        self.txt_soru.setPlainText(secili_soru["soru"])
        self.txt_dogru_cevap.setText(secili_soru["dogru_cevap"])
        self.txt_a_sikki.setText(secili_soru["a_sikki"])
        self.txt_b_sikki.setText(secili_soru["b_sikki"])
        self.txt_c_sikki.setText(secili_soru["c_sikki"])
        self.txt_d_sikki.setText(secili_soru["d_sikki"])
        
        # Doğru şıkkı işaretle
        if secili_soru["dogru_sik"] == "A":
            self.radio_a.setChecked(True)
        elif secili_soru["dogru_sik"] == "B":
            self.radio_b.setChecked(True)
        elif secili_soru["dogru_sik"] == "C":
            self.radio_c.setChecked(True)
        elif secili_soru["dogru_sik"] == "D":
            self.radio_d.setChecked(True)
    
    def tabloya_yukle(self):
        """Soruları tabloya yükler"""
        # Tablo ayarları
        self.tablo_sorular.setRowCount(len(self.sorular))
        self.tablo_sorular.setColumnCount(3)
        self.tablo_sorular.setHorizontalHeaderLabels(["Soru", "Doğru Cevap", "Doğru Şık"])
        
        # Soruları tabloya ekle
        for i, soru in enumerate(self.sorular):
            self.tablo_sorular.setItem(i, 0, QTableWidgetItem(soru["soru"][:50] + "..."))
            self.tablo_sorular.setItem(i, 1, QTableWidgetItem(soru["dogru_cevap"]))
            self.tablo_sorular.setItem(i, 2, QTableWidgetItem(soru["dogru_sik"]))
        
        # Sütun genişliklerini ayarla
        self.tablo_sorular.setColumnWidth(0, 300)
        self.tablo_sorular.setColumnWidth(1, 150)
        self.tablo_sorular.setColumnWidth(2, 100)
    
    def formu_temizle(self):
        """Form alanlarını temizler"""
        self.txt_soru.clear()
        self.txt_dogru_cevap.clear()
        self.txt_a_sikki.clear()
        self.txt_b_sikki.clear()
        self.txt_c_sikki.clear()
        self.txt_d_sikki.clear()
        self.radio_a.setChecked(False)
        self.radio_b.setChecked(False)
        self.radio_c.setChecked(False)
        self.radio_d.setChecked(False)

# Ana uygulama
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SoruBankasi()
    window.show()
    sys.exit(app.exec_()) 