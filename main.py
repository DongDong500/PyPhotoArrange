import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hello Tkinter")
    
    label = tk.Label(root, text="Hello, Tkinter!", padx=20, pady=20)
    label.pack()
    
    button = tk.Button(root, text="Click me!", command=lambda: print("Button clicked!"))
    button.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()