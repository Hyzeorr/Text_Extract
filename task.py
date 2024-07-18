import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image
import pytesseract
import os

# Tesseract OCR의 경로 설정 (Windows 사용자에게 필요함)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\Spyder\\Desktop\\Code Stuff\\Tesseract_OCR\\tesseract.exe'


class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Extractor")

        self.label = tk.Label(root, text="Select an image file to extract text:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=5)

        self.text_area = Text(root, wrap='word', width=50, height=15)
        self.text_area.pack(pady=10)

    def select_image(self):
        # 기본 경로 설정 (예: 바탕화면/Code Stuff)
        default_path = os.path.join(os.path.expanduser('~'), '바탕화면', 'Code Stuff')
        file_path = filedialog.askopenfilename(
            initialdir=default_path,
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )
        if file_path:
            self.extract_text(file_path)

    def extract_text(self, image_path):
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)
        except Exception as e:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
