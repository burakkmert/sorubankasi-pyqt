import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QFontComboBox

class WordProcessor(QtWidgets.QMainWindow):
    def __init__(self):
        super(WordProcessor, self).__init__()
        
        # Load UI file
        uic.loadUi('word_processor.ui', self)
        
        # Initialize UI elements
        self.setup_ui()
        
        # Connect signals to slots
        self.connect_signals()
        
        # Initialize file handling
        self.current_file = None
        self.setWindowTitle("Kelime İşlemci - Yeni Belge")

    def setup_ui(self):
        # Replace the existing combobox with a font combo box
        old_combo = self.fontComboBox
        self.fontComboBox = QFontComboBox(self)
        self.verticalLayout.replaceWidget(old_combo, self.fontComboBox)
        old_combo.deleteLater()
        
        # Setup font size combo box
        font_sizes = ['8', '9', '10', '11', '12', '14', '16', '18', '20', '22', '24', '26', '28', '36', '48', '72']
        self.fontSizeComboBox.addItems(font_sizes)
        self.fontSizeComboBox.setCurrentText('12')
        
        # Setup text edit default font
        font = QtGui.QFont('Arial', 12)
        self.textEdit.setFont(font)
        
        # Setup toolbar icons
        self.actionBold.setIcon(QtGui.QIcon.fromTheme('format-text-bold'))
        self.actionItalic.setIcon(QtGui.QIcon.fromTheme('format-text-italic'))
        self.actionUnderline.setIcon(QtGui.QIcon.fromTheme('format-text-underline'))
        self.actionAlignLeft.setIcon(QtGui.QIcon.fromTheme('format-justify-left'))
        self.actionAlignCenter.setIcon(QtGui.QIcon.fromTheme('format-justify-center'))
        self.actionAlignRight.setIcon(QtGui.QIcon.fromTheme('format-justify-right'))
        self.actionAlignJustify.setIcon(QtGui.QIcon.fromTheme('format-justify-fill'))

    def connect_signals(self):
        # File menu actions
        self.actionYeni.triggered.connect(self.new_file)
        self.actionAc.triggered.connect(self.open_file)
        self.actionKaydet.triggered.connect(self.save_file)
        self.actionFarkliKaydet.triggered.connect(self.save_file_as)
        self.actionCikis.triggered.connect(self.close)
        
        # Edit menu actions
        self.actionKes.triggered.connect(self.textEdit.cut)
        self.actionKopyala.triggered.connect(self.textEdit.copy)
        self.actionYapistir.triggered.connect(self.textEdit.paste)
        
        # Format actions
        self.actionBold.triggered.connect(self.format_bold)
        self.actionItalic.triggered.connect(self.format_italic)
        self.actionUnderline.triggered.connect(self.format_underline)
        self.actionAlignLeft.triggered.connect(self.format_align_left)
        self.actionAlignCenter.triggered.connect(self.format_align_center)
        self.actionAlignRight.triggered.connect(self.format_align_right)
        self.actionAlignJustify.triggered.connect(self.format_align_justify)
        
        # Font and size changes
        self.fontComboBox.currentFontChanged.connect(self.change_font)
        self.fontSizeComboBox.currentTextChanged.connect(self.change_font_size)
        
        # Update format buttons when cursor position changes
        self.textEdit.cursorPositionChanged.connect(self.update_format_buttons)

    def new_file(self):
        if self.maybe_save():
            self.textEdit.clear()
            self.current_file = None
            self.setWindowTitle("Kelime İşlemci - Yeni Belge")

    def open_file(self):
        if self.maybe_save():
            file_name, _ = QFileDialog.getOpenFileName(
                self, "Belge Aç", "", "HTML Belgeleri (*.html *.htm);;Tüm Dosyalar (*)"
            )
            if file_name:
                with open(file_name, 'r', encoding='utf-8') as file:
                    self.textEdit.setHtml(file.read())
                self.current_file = file_name
                self.setWindowTitle(f"Kelime İşlemci - {os.path.basename(file_name)}")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(self.textEdit.toHtml())
            return True
        else:
            return self.save_file_as()

    def save_file_as(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Belgeyi Kaydet", "", "HTML Belgeleri (*.html *.htm);;Tüm Dosyalar (*)"
        )
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.textEdit.toHtml())
            self.current_file = file_name
            self.setWindowTitle(f"Kelime İşlemci - {os.path.basename(file_name)}")
            return True
        return False

    def maybe_save(self):
        if self.textEdit.document().isModified():
            ret = QMessageBox.warning(
                self, "Kelime İşlemci",
                "Belge değiştirildi.\nDeğişiklikleri kaydetmek istiyor musunuz?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )
            if ret == QMessageBox.Save:
                return self.save_file()
            elif ret == QMessageBox.Cancel:
                return False
        return True

    def closeEvent(self, event):
        if self.maybe_save():
            event.accept()
        else:
            event.ignore()

    def format_bold(self):
        if self.actionBold.isChecked():
            self.textEdit.setFontWeight(QtGui.QFont.Bold)
        else:
            self.textEdit.setFontWeight(QtGui.QFont.Normal)

    def format_italic(self):
        self.textEdit.setFontItalic(self.actionItalic.isChecked())

    def format_underline(self):
        self.textEdit.setFontUnderline(self.actionUnderline.isChecked())

    def format_align_left(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignLeft)
        self.update_alignment_buttons(self.actionAlignLeft)

    def format_align_center(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.update_alignment_buttons(self.actionAlignCenter)

    def format_align_right(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignRight)
        self.update_alignment_buttons(self.actionAlignRight)

    def format_align_justify(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignJustify)
        self.update_alignment_buttons(self.actionAlignJustify)

    def update_alignment_buttons(self, active_action):
        self.actionAlignLeft.setChecked(active_action == self.actionAlignLeft)
        self.actionAlignCenter.setChecked(active_action == self.actionAlignCenter)
        self.actionAlignRight.setChecked(active_action == self.actionAlignRight)
        self.actionAlignJustify.setChecked(active_action == self.actionAlignJustify)

    def change_font(self, font):
        self.textEdit.setCurrentFont(font)

    def change_font_size(self, size):
        self.textEdit.setFontPointSize(float(size))

    def update_format_buttons(self):
        # Update the state of formatting buttons based on cursor position
        font = self.textEdit.currentFont()
        self.fontComboBox.setCurrentFont(font)
        self.fontSizeComboBox.setCurrentText(str(int(font.pointSize())))
        
        self.actionBold.setChecked(font.weight() == QtGui.QFont.Bold)
        self.actionItalic.setChecked(font.italic())
        self.actionUnderline.setChecked(font.underline())
        
        # Update alignment buttons
        alignment = self.textEdit.alignment()
        self.actionAlignLeft.setChecked(alignment == QtCore.Qt.AlignLeft)
        self.actionAlignCenter.setChecked(alignment == QtCore.Qt.AlignCenter)
        self.actionAlignRight.setChecked(alignment == QtCore.Qt.AlignRight)
        self.actionAlignJustify.setChecked(alignment == QtCore.Qt.AlignJustify)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WordProcessor()
    window.show()
    sys.exit(app.exec_()) 