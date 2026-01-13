import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt


class IncubatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Incubator Monitor")
        self.root.geometry("400x300") 
        
        # 1. HEADER
        self.header_label = tk.Label(root, text="Neonatal Monitoring System", 
                                     font=("Arial", 16, "bold"), fg="blue")
        self.header_label.pack(pady=10)

        # 2. STATUS DISPLAY
        self.status_label = tk.Label(root, text="Status: Waiting for Data...", 
                                     font=("Arial", 12), fg="gray")
        self.status_label.pack(pady=20)

        # 3. BUTTONS
        self.btn_load = tk.Button(root, text="Load Patient Log", 
                                  command=self.load_data, bg="lightgray", width=20)
        self.btn_load.pack(pady=5)

        self.btn_graph = tk.Button(root, text="View Temperature Chart", 
                                   command=self.show_graph, state="disabled", width=20)
        self.btn_graph.pack(pady=5)

        
        self.df = None

    
    def load_data(self):
        try:
            self.df = pd.read_csv("incubator_log.csv")
            
            
            max_temp = self.df["Temperature"].max()
        
            if max_temp > 37.5:
                self.status_label.config(text=f"WARNING: Fever Detected ({max_temp}°C)", fg="red")
            else:
                self.status_label.config(text=f"Status: Patient Stable ({max_temp}°C)", fg="green")
            
          
            self.btn_graph.config(state="normal", bg="lightblue")
            messagebox.showinfo("Success", "Patient data loaded successfully.")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "incubator_log.csv not found!")

  
    def show_graph(self):
        if self.df is None:
            return
            
        plt.figure(figsize=(8, 4))
        plt.plot(self.df["TimeID"], self.df["Temperature"], color='blue')
        plt.axhline(y=37.5, color='r', linestyle='--', label="Max Limit")
        plt.title("Patient Temperature History")
        plt.xlabel("Time Reading")
        plt.ylabel("Temp (°C)")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk() 
    app = IncubatorApp(root) 
    root.mainloop() 