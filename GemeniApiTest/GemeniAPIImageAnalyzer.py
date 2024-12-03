import google.generativeai as genai
import json
import PIL.Image
import tkinter as tk
from tkinter import filedialog

# Load config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Fetch the API key from config.json
api_key = config.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in config.json.")

# Passes the API key to the genai library enabling authenticated access to Gemeni services.
genai.configure(api_key=api_key)

#Sets up tkinter for creating a file selection dialog 
root = tk.Tk()
root.withdraw()  

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
)

if not file_path:
    print("No file selected. Exiting.")
else:
    image = PIL.Image.open(file_path) #Prepares the image for processing.
    print(f"Selected image: {file_path}")

    #Initializes genAI model
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response = model.generate_content(["Tell me about this image", image])
    print(response.text)
