from src.data_io.xls_reader import read_parts, read_profiles
from src.core_al.nesting import nesting_parts
from src.models.Parts import Part
import pandas as pd
import shutil

excel_path = r"C:\Users\evillarreal\Documents\Personales\Programacion\python\projects\profile_nesting\pruebas.xlsx"
output_path = excel_path.replace(".xlsx", "_nesting.xlsx") # path of the copy of the original excel file
parts_data = read_parts(excel_path)
profiles_data = read_profiles(excel_path)

shutil.copy(excel_path, output_path) # create a copy of the original excel file

final_data = nesting_parts(parts_data, profiles_data)

data_rows = [] # table shown on "Nesting_detail"
summary_rows = [] # table shown on "Nesting_summary"

for profile, data in final_data.items(): #create table for "Nesting_detail" for excel file
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

for profile, data in final_data.items(): #create table for "Nesting_summary" for the excel file
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
        "total_used": total_used,
        "total_waste": total_waste,
        "utilization_%": round(utilization, 2)
    })

df_detail = pd.DataFrame(data_rows) # data frame for "Nesting_details"
df_summary = pd.DataFrame(summary_rows) # data frame for "Nesting_summary"

# Create edit the new excel file with the new sheets
with pd.ExcelWriter(output_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
    df_detail.to_excel(writer, sheet_name="Nesting_detail", index=False)
    df_summary.to_excel(writer, sheet_name="Nesting_summary", index=False)


print("-----Nesting completed-----")
