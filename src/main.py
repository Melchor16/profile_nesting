from src.data_io.xls_reader import read_parts, read_profiles
from src.core_al.nesting import nesting_parts
from src.models.Parts import Part

excel_path = r"C:\Users\evillarreal\Documents\Personales\Programacion\python\projects\profile_nesting\pruebas.xlsx"
parts_data = read_parts(excel_path)
profiles_data = read_profiles(excel_path)

resultado = nesting_parts(parts_data, profiles_data)

# convertir profiles_data a diccionario para acceso rápido
profiles_dict = {p.name: p for p in profiles_data}

