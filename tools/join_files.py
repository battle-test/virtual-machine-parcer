import pandas as pd
from pathlib import Path
import os

def join_files(directory):
    os.chdir(directory)
    logicaldisk_dir = Path(f"{directory}\\logicaldisk")
    df_logicaldisk = pd.concat([pd.read_csv(f, sep=",",skiprows=1, encoding="utf_16_le") for f in logicaldisk_dir.glob("*.csv")], ignore_index=True)
    df_logicaldisk["FreeSpace"] = df_logicaldisk["FreeSpace"]/1073741824
    df_logicaldisk["Size"] = df_logicaldisk["Size"]/1073741824
    df_logicaldisk.to_excel("DiskInfo.xlsx")

    systeminfo_dir = Path(f"{directory}\\systeminfo")
    df_systeminfo = pd.concat([pd.read_csv(f, sep=",", encoding="utf_8") for f in systeminfo_dir.glob("*.csv")], ignore_index=True)
    del df_systeminfo['Hotfix(s)']
    df_systeminfo.to_excel("Systeminfo.xlsx")

    product_dir = Path(f"{directory}\\product")
    df_product = pd.concat([pd.read_csv(f, sep=",",skiprows=1, encoding="utf_16_le") for f in product_dir.glob("*.csv")], ignore_index=True)
    x = lambda x: str(x)[0:4]+"-"+str(x)[4:6]+"-"+str(x)[6:8]
    df_product['InstallDate'] = df_product['InstallDate'].apply(x)
    df_product.to_excel("ProductInfo.xlsx")
