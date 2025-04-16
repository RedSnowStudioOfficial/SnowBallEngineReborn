import tkinter as tk
import time

class FPSMonitor:
    def __init__(self, root):
        self.root = root
        self.last_time = None
        self.frame_count = 0
        self.fps = 0
        
        # Элементы GUI
        self.label = tk.Label(root, text="FPS: 0\nInterval: 0 ms", font=('Arial', 12))
        self.label.pack(pady=20)
        
        self.btn_start = tk.Button(root, text="Start", command=self.start_updates)
        self.btn_start.pack()

    def start_updates(self):
        self.btn_start.config(state=tk.DISABLED)
        self.last_time = time.perf_counter()
        self.root.after(1, self.update)  # Планируем первый вызов

    def update(self):
        # Измеряем время между вызовами
        current_time = time.perf_counter()
        delta_time = current_time - self.last_time
        self.last_time = current_time
        
        # Рассчитываем FPS и интервал
        self.fps = 1 / delta_time if delta_time != 0 else 0
        interval_ms = delta_time * 1000
        
        # Обновляем статистику каждые 10 кадров
        self.frame_count += 1
        if self.frame_count % 10 == 0:
            self.label.config(
                text=f"FPS: {self.fps:.1f}\nInterval: {interval_ms:.2f} ms"
            )
        
        # Планируем следующий вызов
        self.root.after(1, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("FPS Monitor")
    app = FPSMonitor(root)
    root.mainloop()