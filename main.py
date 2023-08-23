import tkinter as tk
from PIL import ImageTk, Image
import io

import requests
import responses

def clear_previous_result():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget != label:
            widget.destroy()

def display_cocktail_details(cocktail):
    detail_window = tk.Toplevel(root)
    detail_window.title(cocktail.name)
    detail_window.minsize(400, 100)
    detail_window.maxsize(400, 1000)

    response = requests.get(cocktail.image)
    image_data = io.BytesIO(response.content)
    image = Image.open(image_data)
    resized_image = image.resize((300,205))
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(detail_window, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)

    name_label = tk.Label(detail_window, text=cocktail.name, font=("Arial", 16))
    name_label.pack(pady=10)

    alcoholic_label = tk.Label(detail_window, text=f"{cocktail.isAlcoholic}")
    alcoholic_label.pack(pady=5)

    ingredients_label = tk.Label(detail_window, text="Ingredients:")
    ingredients_label.pack(pady=5)

    for ingredient, measure in cocktail.ingredients:
        ing_label = tk.Label(detail_window, text=f"{ingredient} - {measure}")
        ing_label.pack()

    instructions_label = tk.Label(detail_window, text=f"Instructions: {cocktail.instructions}", wraplength=400-20)
    instructions_label.pack(pady=10)

def on_label_click(event, cocktail):
    display_cocktail_details(cocktail)

def on_search_click():
    clear_previous_result()
    cocktails = responses.searchByName(entry.get())
    
    if not cocktails:
        error_label = tk.Label(root, text="No cocktails found.")
        error_label.pack()
        return
    for cocktail in cocktails:
        cocktail_label = tk.Label(root, text=f"{cocktail.name}", cursor="hand2", foreground="blue")
        cocktail_label.bind("<Button-1>", lambda event, c=cocktail: on_label_click(event, c))
        cocktail_label.pack()

### Create the main window ###
root = tk.Tk()
root.title("Cocktail Getter")
root.geometry("200x500")

# Create a label widget
label = tk.Label(root, text="Search cocktail:")
label.pack()

# Create an entry widget (text input)
entry = tk.Entry(root)
entry.pack()

# Create a button widget
button = tk.Button(root, text="Search", command=on_search_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()
