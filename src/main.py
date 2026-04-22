from src.data_io.xls_reader import read_parts, read_profiles
from src.core_al.nesting import nesting_parts
from src.models.Parts import Part
import pandas as pd

excel_path = r"C:\Users\evillarreal\Documents\Personales\Programacion\python\projects\profile_nesting\pruebas.xlsx"
parts_data = read_parts(excel_path)
profiles_data = read_profiles(excel_path)

final_data = nesting_parts(parts_data, profiles_data)

data_rows = []

for profile, data in final_data.items():
    profile_length = data["profile_length"]

    for i, bar in enumerate(data["nestings"], 1):
        used = sum(bar)
        waste = profile_length - used

        data_rows.append({
            "profile": profile,
            "bar": i,
            "pieces": ", ".join(str(x) for x in bar),
            "used": used,
            "waste": waste
        })

data_frame = pd.DataFrame(data_rows)

with pd.ExcelWriter(excel_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
    data_frame.to_excel(writer, sheet_name="Nesting_Result", index=False)

