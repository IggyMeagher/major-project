import customtkinter
import re

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x200')

        # Setting up a textbox
        self.textbox = customtkinter.CTkEntry(master=root, placeholder_text="Type here...")
        self.textbox.pack(pady=20)

        # Binding the KeyRelease event to the textbox
        self.textbox.bind("<KeyRelease>", self.on_key_release)

        # Label to display results
        self.result_label = customtkinter.CTkLabel(master=root, text="")
        self.result_label.pack()

    def on_key_release(self, event):
        # Get the content of the textbox
        content = self.textbox.get()
        # Check content length for demonstration
        length = len(content)
        # Update the label to show the number of characters
        self.result_label.configure(text=f"Length of input: {length}")

        # Example of checking character types
        if re.search(r'[A-Z]', content):
            self.result_label.configure(text="Contains uppercase letters.")
        elif re.search(r'[a-z]', content):
            self.result_label.configure(text="Contains lowercase letters.")
        elif re.search(r'[0-9]', content):
            self.result_label.configure(text="Contains digits.")
        elif re.search(r'[\W_]', content):
            self.result_label.configure(text="Contains special characters.")

def main():
    root = customtkinter.CTk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
