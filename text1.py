import customtkinter

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x200')  # Set the size of the window

        # Create an entry widget for username input
        self.username_entry = customtkinter.CTkEntry(master=root, placeholder_text="Enter Username")
        self.username_entry.pack(pady=20)

        # Create a button that when clicked will call the self.print_username function
        submit_button = customtkinter.CTkButton(master=root, text="Submit", command=self.print_username)
        submit_button.pack()

    def print_username(self):
        # Retrieve the text currently entered in the username_entry
        username = self.username_entry.get()
        print(f"Username entered: {username}")

if __name__ == "__main__":
    root = customtkinter.CTk()  # Create the main window
    app = SimpleApp(root)  # Create an instance of our application
    root.mainloop()  # Start the main event loop
