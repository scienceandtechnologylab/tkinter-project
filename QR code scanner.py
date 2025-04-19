import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from PIL import Image, ImageTk

class QRCodeScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Scanner")

        self.video_capture = cv2.VideoCapture(0)  # Open webcam

        self.canvas = tk.Label(root)
        self.canvas.pack()

        self.result_label = tk.Label(root, text="Scan a QR Code...", font=("Arial", 14))
        self.result_label.pack()

        self.update_frame()  # Start scanning

    def update_frame(self):
        _, frame = self.video_capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        qr_codes = decode(frame)
        for qr in qr_codes:
            data = qr.data.decode("utf-8")
            self.result_label.config(text=f"Scanned Data: {data}")

            # Draw a rectangle around the QR code
            points = qr.polygon
            if len(points) == 4:
                pts = [(p.x, p.y) for p in points]
                cv2.polylines(frame, [np.array(pts, np.int32)], isClosed=True, color=(0, 255, 0), thickness=3)

        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        self.canvas.imgtk = imgtk
        self.canvas.configure(image=imgtk)
        self.root.after(10, self.update_frame)  # Refresh every 10ms

    def __del__(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    scanner = QRCodeScanner(root)
    root.mainloop()
