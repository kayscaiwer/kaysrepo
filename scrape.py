import pandas as pd
import numpy as np


URL = "https://www.soccerstats.com/latest.asp?league=argentina"
leagues = {
    'EPL':'TXT/EPL_2324_text.txt',
    'ESP':'TXT/LaLiga_2324_text.txt',
    'ITA':'TXT/SerieA_2324_text.txt',
    'FRA':'TXT/Ligue1_2423_text.txt',
    'MEX':'TXT/Liga-MX_23-4_text.txt',
    'ARG':'TXT/ArgentinaLP_23-4_text.txt',
    'BEL':'TXT/BelgiumPro_2324_text.txt',
    'GER':'TXT/Bundesliga_2324_text.txt',
    'BRA':'TXT/BRA_2324.txt',
    'GRC':'TXT/GRC_2324.txt',
    'POL':'TXT/POL_2324.txt',
    'TUR':'TXT/TUR_2324.txt',
    'PTG':'TXT/PTG_2324.txt',
    'AUS':'TXT/AUS_2324.txt',
    'KSV':'TXT/KSV_2324.txt',
    'HGK':'TXT/HGK_2324.txt',
    'GUA':'TXT/GUA_2324.txt',
    'VAM':'TXT/VAM_2324.txt',
    'ISR':'TXT/ISR_2324.txt',
    'WAL':'TXT/WAL_2324.txt',
    'SCO':'TXT/SCO_2324.txt',
    'AML':'TXT/AML_2324.txt'
}
augtxt = 'Rk  Squad  '

def txt2csv(filename):
    with open(filename,'r') as file_ob:
        df_lol = []
        line0 = file_ob.readline()
        df_fields = (augtxt + line0).split()[:10]
        df_fields[2] = 'MP'
        df_lol.append(df_fields)
        # print(df_fields)
        for i in range(200):
            line = file_ob.readline()
            if line == "":
                break
            elif (i % 2) == 0:
                raw = line.split()
                s = raw[1:-8]
                if len(s) > 1:
                    t = s[0]
                    for i in s[1:]:
                        t = t + " " + i
                else:
                    t = s[0]
                raw = [raw[0]] + [t] + raw[-8:]
                df_lol.append(raw)
                # print(raw)
    df = pd.DataFrame(df_lol[1:], columns= df_lol[0])
    print(df.set_index('Rk'))
    return df



def make_csvs(txtfiles_dict):
    for key,value in txtfiles_dict.items():
        df = txt2csv(txtfiles_dict.get(key))
        df.to_csv(f"CSV/{key}_2324.csv", index=False)
    print("All done!")



make_csvs(leagues)


