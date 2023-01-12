import webview
import tkinter as tk

def save_input():
    global input_text
    input_text = input_box.get()
    print("Input saved as:", input_text)
    root.destroy()
    
# Create the main window
root = tk.Tk()
photo = tk.PhotoImage(file = 'icon.png')
root.wm_iconphoto(False, photo)
root.title("YouTubeWindow")

# Create a label to prompt the user for input
tk.Label(root, text="Enter YouTube link:").pack()

# Create a text box for the user to input
input_box = tk.Entry(root)
input_box.pack()

# Create a button to save the user's input
save_button = tk.Button(root, text="Play", command=save_input)
save_button.pack()

# Start the main loop
root.mainloop()

webview.create_window("YouTube", input_text, width=800, height=600)
webview.start()