import pandas as pd
from src.models.Parts import Part
from src.models.Profiles import Profile

parts_sheet = "Sheet1"
profiles_sheet = "Sheet2"
    
def read_parts(file_path, sheet = parts_sheet):

    new_file = pd.read_excel(
        file_path, 
        sheet_name=sheet, 
        usecols=["item", "length", "qty", "profile"],
        dtype={"item": int, "length": float, "qty": int, "profile": str},
        na_values=["-", "NA"]
        )

    new_file = new_file.dropna(subset = ["item", "length", "qty", "profile"] )

    new_file["item"] = new_file["item"].astype(int)
    new_file["length"] = new_file["length"].astype(float)
    new_file["qty"] = new_file["qty"].astype(int)
    new_file["profile"] = new_file["profile"].astype(str)

    parts = [Part.from_row(row) for _, row in new_file.iterrows()]

    return parts

def read_profiles(file_path, sheet = profiles_sheet):

    temporal_nm = pd.read_excel(
        file_path, 
        sheet_name=sheet, 
        usecols=["name", "length"],
        dtype={"name": str, "length": float},
        na_values=["-", "NA"]
        )

    temporal_nm = temporal_nm.dropna(subset = ["name", "length"] )

    temporal_nm["name"] = temporal_nm["name"].astype(str)
    temporal_nm["length"] = temporal_nm["length"].astype(float)

    profiles = [Profile.from_row(row) for _, row in temporal_nm.iterrows()]

    return profiles