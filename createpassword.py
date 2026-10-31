import secrets
import string
import tkinter as tk
from tkinter import messagebox


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("520x560")
        self.root.minsize(480, 520)
        self.root.configure(bg="#101827")
        self.bg, self.panel = "#101827", "#1b2638"
        self.text, self.muted, self.accent = "#f4f7fb", "#aab7c8", "#67e8c2"
        self.length_var = tk.IntVar(value=16)
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Password Generator", font=("Segoe UI", 22, "bold"), bg=self.bg, fg=self.text).pack(pady=(24, 4))
        tk.Label(self.root, text="Create a strong random password", font=("Segoe UI", 10), bg=self.bg, fg=self.muted).pack(pady=(0, 18))
        panel = tk.Frame(self.root, bg=self.panel, padx=22, pady=20)
        panel.pack(fill="both", expand=True, padx=24, pady=(0, 22))
        tk.Label(panel, text="PASSWORD LENGTH", font=("Segoe UI", 9, "bold"), bg=self.panel, fg=self.muted).pack(anchor="w")
        length_row = tk.Frame(panel, bg=self.panel)
        length_row.pack(fill="x", pady=(8, 18))
        tk.Scale(length_row, from_=8, to=64, orient="horizontal", variable=self.length_var, showvalue=False, length=300, bg=self.panel, fg=self.text, troughcolor="#34445c", highlightthickness=0, activebackground=self.accent, command=self.update_length_label).pack(side="left", fill="x", expand=True)
        self.length_label = tk.Label(length_row, text="16", width=4, font=("Segoe UI", 12, "bold"), bg=self.panel, fg=self.accent)
        self.length_label.pack(side="right", padx=(12, 0))
        tk.Label(panel, text="INCLUDE CHARACTERS", font=("Segoe UI", 9, "bold"), bg=self.panel, fg=self.muted).pack(anchor="w", pady=(0, 8))
        for label, variable in [("Lowercase letters (a-z)", self.lower_var), ("Uppercase letters (A-Z)", self.upper_var), ("Numbers (0-9)", self.digits_var), ("Symbols (!@#$...)", self.symbols_var)]:
            tk.Checkbutton(panel, text=label, variable=variable, anchor="w", font=("Segoe UI", 10), bg=self.panel, fg=self.text, selectcolor=self.bg, activebackground=self.panel, activeforeground=self.text, highlightthickness=0).pack(fill="x", pady=2)
        self.password_entry = tk.Entry(panel, font=("Consolas", 13), justify="center", bg="#0b1220", fg=self.text, insertbackground=self.text, relief="flat")
        self.password_entry.pack(fill="x", ipady=11, pady=(20, 12))
        buttons = tk.Frame(panel, bg=self.panel)
        buttons.pack(fill="x")
        tk.Button(buttons, text="Generate Password", command=self.generate_password, font=("Segoe UI", 10, "bold"), bg=self.accent, fg="#09221b", activebackground="#4dd8ae", relief="flat", cursor="hand2", pady=10).pack(fill="x", pady=(0, 8))
        tk.Button(buttons, text="Copy to Clipboard", command=self.copy_password, font=("Segoe UI", 10, "bold"), bg="#34445c", fg=self.text, activebackground="#405573", relief="flat", cursor="hand2", pady=9).pack(fill="x")
        self.status_label = tk.Label(panel, text="Choose your options and generate a password.", font=("Segoe UI", 9), bg=self.panel, fg=self.muted, wraplength=400)
        self.status_label.pack(pady=(12, 0))
        self.generate_password()

    def update_length_label(self, _value=None):
        self.length_label.config(text=str(self.length_var.get()))

    def generate_password(self):
        pools = []
        if self.lower_var.get(): pools.append(string.ascii_lowercase)
        if self.upper_var.get(): pools.append(string.ascii_uppercase)
        if self.digits_var.get(): pools.append(string.digits)
        if self.symbols_var.get(): pools.append("!@#$%^&*()-_=+[]{};:,.?/")
        if not pools:
            messagebox.showwarning("Choose at least one option", "Please select at least one character type.")
            return
        length = self.length_var.get()
        chars = [secrets.choice(pool) for pool in pools]
        all_chars = "".join(pools)
        chars.extend(secrets.choice(all_chars) for _ in range(length - len(chars)))
        secrets.SystemRandom().shuffle(chars)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, "".join(chars))
        self.status_label.config(text="Password generated. Keep it private and store it securely.", fg=self.accent)

    def copy_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showinfo("No password", "Generate a password first.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()
        self.status_label.config(text="Copied to clipboard.", fg=self.accent)


def main():
    root = tk.Tk()
    PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
