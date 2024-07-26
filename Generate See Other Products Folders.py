import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FolderCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Creator")

        self.select_folder_button = tk.Button(root, text="Select Root Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=10)

        self.create_folders_button = tk.Button(root, text="Create Folders", state=tk.DISABLED, command=self.create_folders)
        self.create_folders_button.pack(pady=10)

        self.selected_folder = None

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.create_folders_button['state'] = tk.NORMAL

    def create_folders(self):
        if self.selected_folder:
            for root, dirs, files in os.walk(self.selected_folder, topdown=False):
                folder_name = os.path.basename(root)
                product_id = folder_name.split(' ')[0]
                other_data_folder = os.path.join(root, f"- Other data for product {product_id}")
                if not os.path.exists(other_data_folder):
                    os.makedirs(other_data_folder)
                    print(f"Created folder: {other_data_folder}")

            messagebox.showinfo("Info", "Folders created successfully.")
        else:
            messagebox.showwarning("Warning", "No root folder selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderCreatorApp(root)
    root.mainloop()
