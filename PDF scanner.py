import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger

# Set Tesseract Path (Change this based on your OS)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows Path

class PDFScannerCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Scanner & Creator")
        self.root.geometry("600x500")

        tk.Label(root, text="PDF Scanner & Creator", font=("Arial", 16, "bold")).pack()

        # Buttons for scanning and creating PDFs
        tk.Button(root, text="Scan Image for Text (OCR)", command=self.scan_image).pack(pady=5)
        tk.Button(root, text="Create PDF from Text", command=self.create_text_pdf).pack(pady=5)
        tk.Button(root, text="Create PDF from Images", command=self.create_image_pdf).pack(pady=5)
        tk.Button(root, text="Merge Multiple PDFs", command=self.merge_pdfs).pack(pady=5)

        # Text area for OCR output
        self.text_area = tk.Text(root, height=10, width=60)
        self.text_area.pack()

    def scan_image(self):
        """Scans an image and extracts text using OCR"""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return
        
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)

        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, text)
        messagebox.showinfo("OCR Result", "Text extracted successfully!")

    def create_text_pdf(self):
        """Creates a PDF from the extracted text"""
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "No text to convert to PDF!")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            pdf = canvas.Canvas(file_path)
            pdf.drawString(100, 750, text)
            pdf.save()
            messagebox.showinfo("Success", "PDF created successfully!")

    def create_image_pdf(self):
        """Creates a PDF from selected images"""
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not file_paths:
            return
        
        images = [Image.open(fp).convert("RGB") for fp in file_paths]
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            images[0].save(file_path, save_all=True, append_images=images[1:])
            messagebox.showinfo("Success", "PDF created from images successfully!")

    def merge_pdfs(self):
        """Merges multiple PDFs into one"""
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if not file_paths:
            return
        
        merger = PdfMerger()
        for pdf in file_paths:
            merger.append(pdf)

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            merger.write(file_path)
            merger.close()
            messagebox.showinfo("Success", "PDFs merged successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFScannerCreator(root)
    root.mainloop()
