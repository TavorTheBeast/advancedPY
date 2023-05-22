import tkinter as tk
from PIL import ImageTk, Image

def show_image():
    image_path = "C:\\Users\\tzurt\PycharmProjects\\advancedPY\\venv\\4610948947.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image.show()

window = tk.Tk()

question_label = tk.Label(window, text="What is your favorite Image?")
question_label.pack()

button = tk.Button(window, text="Show Answer", command=show_image)
button.pack()

window.mainloop()
