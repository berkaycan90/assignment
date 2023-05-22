import pandas
import warnings                 
warnings.simplefilter("ignore")

df = pandas.read_excel("./data/raw_data.xlsx")
df = df[[
    "MusteriText",	
    "MusteriID",	
    "Sirket Kodu",	
    "Takvim",	
    "Primary Segment (Belge)",	
    "Teklif kaynagi",	
    "Total CS Revenue EUR"]]

df = df.groupby(["MusteriText", "MusteriID", "Sirket Kodu", "Primary Segment (Belge)",	"Teklif kaynagi", "Takvim"]).sum().reset_index()



df.to_excel("./data/cleaned_data.xlsx", index = False, encoding='utf-8-sig')
