import sys
import os
import PyPDF2
import pyttsx3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QTextEdit, QMessageBox

class PDFToAudioApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF to Audio Converter")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Select PDF", self)
        self.button.setGeometry(150, 30, 100, 40)
        self.button.clicked.connect(self.select_pdf)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 90, 360, 160)
        self.text_edit.setReadOnly(True)

        self.status_label = QLabel(self)
        self.status_label.setGeometry(20, 270, 360, 20)

        self.show()

    def select_pdf(self):
        file_dialog = QFileDialog()
        pdf_file, _ = file_dialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)")

        if pdf_file:
            self.convert_to_audio(pdf_file)

    def convert_to_audio(self, pdf_file):
        text = self.extract_text_from_pdf(pdf_file)
        self.text_edit.setPlainText(text)

        engine = pyttsx3.init()
        output_file = "output.mp3"
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        self.status_label.setText(f"Audio file saved as: {output_file}")

        output_file_path, _ = QFileDialog.getSaveFileName(self, "Save Audio File", "", "MP3 Files (*.mp3)")

        if output_file_path:
            os.rename(output_file, output_file_path)
            self.status_label.setText(f"Audio file saved at: {output_file_path}")
            QMessageBox.information(self, "Success", "Audio file saved successfully.")
        else:
            os.remove(output_file)
            self.status_label.clear()
            QMessageBox.warning(self, "Error", "Saving operation cancelled.")

    def extract_text_from_pdf(self, pdf_file):
        pdf_text = ""
        with open(pdf_file, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
        return pdf_text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFToAudioApp()
    sys.exit(app.exec_())
