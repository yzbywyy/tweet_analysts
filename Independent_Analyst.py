import pandas as pd
import os
from tweet2analysts.move import move
from tweet2analysts.emo_paddle import anal

result_dir = "Outputs"
list_dir = os.listdir(result_dir)
list_dir.sort(key=lambda fn: os.path.getmtime(result_dir + '\\' + fn))
save_dir_name = os.path.join(result_dir, list_dir[-1])

df_outputs = pd.DataFrame()
for filenames in os.walk(save_dir_name):
    for filename in filenames:
        if isinstance(filename, list):
            for h in filename:
                path_name = [save_dir_name, h]
                path = "\\".join(path_name)
                df_temp = anal(path, save_dir_name)
                if isinstance(df_temp, int):
                    pass
                else:
                    df_outputs = pd.concat([df_outputs, df_temp], axis=1)

df_outputs.to_csv("Outputs.csv")
df_outputs.to_excel("Outputs.xlsx")
move("Outputs.csv", save_dir_name)
move("Outputs.xlsx", save_dir_name)

print("All assignments have been done!")
