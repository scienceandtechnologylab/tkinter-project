import cv2
import numpy as np
import qrcode
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from barcode import Code128
from barcode.writer import ImageWriter

class QRBarcodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR & Barcode Scanner and Generator")
        self.root.geometry("600x500")

        # Title
        tk.Label(root, text="QR & Barcode Scanner & Generator", font=("Arial", 16, "bold")).pack()

        # Webcam preview
        self.canvas = tk.Label(root)
        self.canvas.pack()

        # Result display
        self.result_label = tk.Label(root, text="Scanned Data: ", font=("Arial", 12))
        self.result_label.pack()

        # Button to start scanning
        self.scan_button = tk.Button(root, text="Start Scanning", command=self.start_scanning)
        self.scan_button.pack()

        # Entry for QR/barcode generation
        self.input_text = tk.Entry(root, font=("Arial", 12))
        self.input_text.pack()

        # Buttons for generating QR and Barcode
        tk.Button(root, text="Generate QR Code", command=self.generate_qr).pack()
        tk.Button(root, text="Generate Barcode", command=self.generate_barcode).pack()

        self.video_capture = None

    def start_scanning(self):
        self.video_capture = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if not ret:
            return
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qr_codes = decode(frame)

        for qr in qr_codes:
            data = qr.data.decode("utf-8")
            self.result_label.config(text=f"Scanned Data: {data}")

            # Draw rectangle around the QR/Barcode
            pts = [(p.x, p.y) for p in qr.polygon]
            if len(pts) == 4:
                cv2.polylines(frame, [np.array(pts, np.int32)], isClosed=True, color=(0, 255, 0), thickness=3)

        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        self.canvas.imgtk = imgtk
        self.canvas.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def generate_qr(self):
        data = self.input_text.get()
        if not data:
            messagebox.showerror("Error", "Enter text to generate QR Code")
            return

        qr = qrcode.make(data)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if file_path:
            qr.save(file_path)
            messagebox.showinfo("Success", "QR Code saved successfully!")

    def generate_barcode(self):
        data = self.input_text.get()
        if not data:
            messagebox.showerror("Error", "Enter text to generate Barcode")
            return

        barcode = Code128(data, writer=ImageWriter())
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if file_path:
            barcode.save(file_path)
            messagebox.showinfo("Success", "Barcode saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRBarcodeApp(root)
    root.mainloop()
