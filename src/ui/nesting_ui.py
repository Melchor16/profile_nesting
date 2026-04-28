import tkinter as tk
from tkinter import filedialog, messagebox

from src.data_io.xls_reader import read_parts, read_profiles
from src.core_al.nesting import nesting_parts

import pandas as pd
import shutil
import os


def run_nesting_pipeline(excel_path: str):
    # Crear nombre de archivo de salida
    output_path = excel_path.replace(".xlsx", "_nesting.xlsx")

    # Leer datos
    parts_data = read_parts(excel_path)
    profiles_data = read_profiles(excel_path)

    # Copiar archivo original
    shutil.copy(excel_path, output_path)

    # Ejecutar algoritmo
    final_data = nesting_parts(parts_data, profiles_data)

    # Preparar datos para Excel
    data_rows = []
    summary_rows = []

    for profile, data in final_data.items():
        stock = data["profile_length"]

        for bar in data["nestings"]:
            used = sum(bar)
            waste = stock - used

            data_rows.append({
                "profile": profile,
                "pieces": " | ".join(f"{x:.2f}" for x in bar),
                "used": round(used, 2),
                "waste": round(waste, 2)
            })

    for profile, data in final_data.items():
        stock = data["profile_length"]
        bars = data["nestings"]

        total_bars = len(bars)
        total_used = sum(sum(bar) for bar in bars)
        total_stock = total_bars * stock
        total_waste = total_stock - total_used

        utilization = (total_used / total_stock) * 100 if total_stock > 0 else 0

        summary_rows.append({
            "profile": profile,
            "total_bars": total_bars,
            "total_used": round(total_used, 2),
            "total_waste": round(total_waste, 2),
            "utilization_%": round(utilization, 2)
        })

    df_detail = pd.DataFrame(data_rows)
    df_summary = pd.DataFrame(summary_rows)

    # Escribir al nuevo Excel
    with pd.ExcelWriter(output_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df_detail.to_excel(writer, sheet_name="Nesting_detail", index=False)
        df_summary.to_excel(writer, sheet_name="Nesting_summary", index=False)

    return output_path


def run_app():
    def select_file():
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx")]
        )
        if file_path:
            entry.delete(0, tk.END)
            entry.insert(0, file_path)

    def execute():
        excel_path = entry.get()

        if not excel_path or not os.path.exists(excel_path):
            messagebox.showerror("Error", "Select a valid excel file")
            return

        try:
            btn_run.config(state="disabled")
            root.update_idletasks()

            output_path = run_nesting_pipeline(excel_path)

            messagebox.showinfo(
                "Success",
                f"Nesting completed\nFile created:\n{output_path}"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:
            btn_run.config(state="normal")

    # 🎨 UI
    root = tk.Tk()
    root.title("Nesting Tool by Melchor16")
    root.geometry("420x180")
    root.resizable(False, False)

    label = tk.Label(root, text="Select Excel file:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    btn_select = tk.Button(root, text="Browse", command=select_file)
    btn_select.pack(pady=5)

    btn_run = tk.Button(root, text="Run Nesting", command=execute)
    btn_run.pack(pady=15)

    root.mainloop()