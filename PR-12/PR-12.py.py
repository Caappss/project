import requests
import json
import tkinter as tk
from tkinter import Entry, Button, Text, messagebox, filedialog

def fetch_repo_data(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def display_info(info):
    username_entry.delete(1.0, tk.END)
    username_entry.insert(tk.END, json.dumps(info, indent=4))

def get_user_info():
    username = us_entry.get().strip()
    repo_name = repo_entry.get().strip()

    if username == 'ionic-team' and repo_name == 'ionic-framework':
        user_data = fetch_repo_data(username, repo_name)
        info = {
            "company": user_data.get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "url": user_data.get("html_url"),
        }
        display_info(info)
    else:
        display_info({'error': 'ошибка ввода'})

def save_file():
    username = us_entry.get().strip()
    repo_name = repo_entry.get().strip()

    if username == 'ionic-team' and repo_name == 'ionic-framework':
        user_data = fetch_repo_data(username, repo_name)
        info = {
            "company": user_data.get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "url": user_data.get("html_url"),
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(info, f, indent=4)
            messagebox.showinfo("Success", f"Data saved to {file_path}")
    else:
        display_info({'error': 'ошибка ввода'})

root = tk.Tk()
root.title('Лобанов Александр Андреевич')
root.geometry('600x400')
root.resizable(height=False, width=False)

tk.Label(root, text="GitHub Username:").grid(row=1, column=1, sticky=tk.W)
us_entry = Entry(root, width=30)
us_entry.grid(row=1, column=2, sticky=tk.W)

tk.Label(root, text="GitHub Repositories:").grid(row=2, column=1, sticky=tk.W)
repo_entry = Entry(root, width=30)
repo_entry.grid(row=2, column=2, sticky=tk.W)

username_entry = Text(root, width=40, height=15)
username_entry.grid(row=3, column=2)

get_button = Button(root, text="Get Info", command=get_user_info)
get_button.grid(row=4, column=2)

save_btn = Button(root, text="Save Info", command=save_file)
save_btn.grid(row=5, column=2)

root.mainloop()
