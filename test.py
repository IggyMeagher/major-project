import pandas as pd
import customtkinter as ctk
from tkinter import ttk

class TableApp:
    def __init__(self, root):
        self.root = root
        self.df = pd.read_csv('user_data.csv')
        
        # Create a CTkFrame for the Treeview
        self.tree_frame = ctk.CTkFrame(self.root)
        self.tree_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Create the Treeview
        self.tree = ttk.Treeview(self.tree_frame, columns=("Username", "AverageScore", "PreviousAverage", "PercentageIncrease"), show="headings")
        
        # Define the headings
        self.tree.heading("Username", text="Username")
        self.tree.heading("AverageScore", text="Average Score")
        self.tree.heading("PreviousAverage", text="Previous Average")
        self.tree.heading("PercentageIncrease", text="Percentage Increase")
        
        # Define the column widths
        self.tree.column("Username", width=150)
        self.tree.column("AverageScore", width=100)
        self.tree.column("PreviousAverage", width=100)
        self.tree.column("PercentageIncrease", width=150)
        
        # Create a scrollbar
        self.scrollbar = ctk.CTkScrollbar(self.tree_frame, orientation="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack the Treeview and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Load data into the table
        self.load_user_data()

    def load_user_data(self):
        # Check if 'PreviousAverage' column exists
        if 'PreviousAverage' not in self.df.columns:
            self.df['PreviousAverage'] = [0] * len(self.df)  # Initialize with zeros if it doesn't exist

        for i in range(len(self.df)):
            score = self.df.iloc[i]['AverageScore']
            previous_score = self.df.iloc[i]['PreviousAverage']
            if pd.notna(score):
                score = float(score)
            else:
                score = 0
            
            if pd.notna(previous_score):
                previous_score = float(previous_score)
            else:
                previous_score = 0
            
            if previous_score != 0:
                percentage_increase = ((score - previous_score) / previous_score) * 100
            else:
                percentage_increase = 0  # Handle division by zero
            
            self.tree.insert("", "end", values=(
                self.df.iloc[i]['Username'],
                score,
                previous_score,
                f"{percentage_increase:.2f}%"
            ))

if __name__ == "__main__":
    root = ctk.CTk()  # Use customtkinter CTk as the root window
    app = TableApp(root)
    root.mainloop()
