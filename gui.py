import tkinter as tk
import requests

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self, text="URL:")
        self.url_label.pack(side="top")

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(side="top")

        self.query_label = tk.Label(self, text="Query:")
        self.query_label.pack(side="top")

        self.query_entry = tk.Entry(self, width=50)
        self.query_entry.pack(side="top")

        self.submit_button = tk.Button(self)
        self.submit_button["text"] = "Submit"
        self.submit_button["command"] = self.submit_query
        self.submit_button.pack(side="top")

        self.response_text = tk.Text(self, height=10, width=50)
        self.response_text.pack(side="top")

    def submit_query(self):
        url = self.url_entry.get()
        query = self.query_entry.get()
        response = requests.get("http://127.0.0.1:5000/", params={"url":url,"query": query})
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response.text)

root = tk.Tk()
app = Application(master=root)
app.mainloop()