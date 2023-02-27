# Gui to get terms for images to download
# Function to get terms for images to download

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import sys

class GetTermsGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Get Terms")
        self.root.geometry("600x400")
        self.root.resizable(0, 0)

        self.search_terms = []
        self.title_term = ""
        self.output_path = ""
        self.number_of_images = 0
        self.make_quilt = tk.BooleanVar(value=False)

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        # Create the widgets
        self.search_terms_label = tk.Label(self.root, text="Search Terms")
        self.search_terms_entry = tk.Entry(self.root, width=50)
        self.search_terms_entry.insert(0, "image of a cat, cat image, photo of a cat, cat photo, cat pictures")
        self.title_term_label = tk.Label(self.root, text="Title Term")
        self.title_term_entry = tk.Entry(self.root, width=50)
        self.title_term_entry.insert(0, "cat_img")
        self.output_path_label = tk.Label(self.root, text="Output Path")
        self.output_path_entry = tk.Entry(self.root, width=50)
        self.output_path_entry.insert(0, "data/cat-images/")
        self.number_of_images_label = tk.Label(self.root, text="Number of Images")
        self.number_of_images_entry = tk.Entry(self.root, width=50)
        self.number_of_images_entry.insert(0, "2000")
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        # checkbox to ask if user wants to combine images into one image
        self.combine_images = tk.Checkbutton(self.root, text="Combine Images into Quilt?", variable=self.make_quilt, onvalue=True, offvalue=False)

        # Place the widgets
        self.search_terms_label.grid(row=0, column=0, pady=5)
        self.search_terms_entry.grid(row=0, column=1, pady=5)
        self.title_term_label.grid(row=1, column=0, pady=5)
        self.title_term_entry.grid(row=1, column=1, pady=5)
        self.output_path_label.grid(row=2, column=0, pady=5)
        self.output_path_entry.grid(row=2, column=1, pady=5)
        self.number_of_images_label.grid(row=3, column=0, pady=5)
        self.number_of_images_entry.grid(row=3, column=1, pady=5)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.combine_images.grid(row=5, column=0, columnspan=2, pady=5)

    def submit(self):
        # Get the search terms
        self.search_terms = self.search_terms_entry.get().split(", ")
        self.search_terms = [term.strip() for term in self.search_terms]

        # Get the title term
        self.title_term = self.title_term_entry.get()

        # Get the output path
        self.output_path = self.output_path_entry.get()

        # Get the number of images
        self.number_of_images = int(self.number_of_images_entry.get())

        # Get the checkbox value
        self.combine_images = self.make_quilt.get()
    

        # Check if the output path exists
        if not os.path.exists(self.output_path):

            # Create the output path
            os.makedirs(self.output_path)

        # Destroy the window
        self.root.destroy()

        

        return self.search_terms, self.title_term, self.output_path, self.number_of_images, self.combine_images



def get_terms():
    # Create the GUI
    gui = GetTermsGui()

    # Return the search terms, title term, output path, and number of images
    return gui.search_terms, gui.title_term, gui.output_path, gui.number_of_images, gui.combine_images
    

