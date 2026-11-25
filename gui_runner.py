import tkinter as tk
from tkinter import messagebox, ttk
from main import evaluate_product, export_to_csv


class ProductAgentGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("AI E-Commerce Product Research & Listing Agent")
        self.root.geometry("620x420")
        self.listings = []

        frame = ttk.Frame(root, padding="15")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Product Research & Margin Validator", font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 12))

        fields = [("SKU Code:", "BD-2026-101"), ("Product Title:", "Vitamin C Glow Serum"), ("Category:", "Health & Beauty"), ("Unit Cost:", "450"), ("Selling Price:", "1215"), ("Est. Conversion (%):", "2.6")]
        self.entries = {}
        for idx, (label, default) in enumerate(fields, start=1):
            ttk.Label(frame, text=label).grid(row=idx, column=0, sticky=tk.W, pady=4)
            ent = ttk.Entry(frame, width=38)
            ent.insert(0, default)
            ent.grid(row=idx, column=1, sticky=tk.W, pady=4)
            self.entries[label] = ent

        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=12)
        ttk.Button(btn_frame, text="Evaluate Product", command=self.run_evaluation).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Export CSV", command=self.save_csv).pack(side=tk.LEFT, padx=5)

        self.output = tk.Text(frame, height=6, width=70)
        self.output.grid(row=8, column=0, columnspan=2, pady=6)

    def run_evaluation(self):
        try:
            item = {
                "sku": self.entries["SKU Code:"].get(),
                "title": self.entries["Product Title:"].get(),
                "category": self.entries["Category:"].get(),
                "cost_price": float(self.entries["Unit Cost:"].get()),
                "selling_price": float(self.entries["Selling Price:"].get()),
                "conversion_rate": float(self.entries["Est. Conversion (%):"].get()),
            }
            res = evaluate_product(item)
            self.listings.append(res)
            self.output.insert(tk.END, f"{res.sku} -> {res.status} | Net Profit: {res.net_profit} | ROI: {res.roi_percent}%\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for prices and conversion rate.")

    def save_csv(self):
        if not self.listings:
            messagebox.showwarning("No Data", "Evaluate at least one product first.")
            return
        file_path = export_to_csv(self.listings)
        messagebox.showinfo("Exported", f"Saved qualified listings to {file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductAgentGUI(root)
    root.mainloop()
