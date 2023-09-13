import pandas as pd
#
maindata = pd.read_excel("lab_pi_101.xlsx")
CEst = maindata.shape[0]
CEst1 = maindata['Группа'].str.contains('ПИ101').sum()
#CEst = 0
#for index, row in maindata.iterrows():
    #if any(map(str.isdigit, str(row['Сокращенная оценка']))):
        #CEst += 1
#CEst1 = len(maindata[(lipa['Сокращенная оценка'].astype(str).str.isnumeric()) & (maindata['Группа'] == 'ПИ101')])
#print(CEst)
#print('Общее кол-во оценок:', CEst, 'Кол-во оценок группы ПИ101:', CEst1)
UN = maindata[lipa['Группа'] == "ПИ101"]
N = len(UN['Личный номер студента'].unique())
U = maindata.loc[maindata["Группа"] == "ПИ101", "Личный номер студента"].unique()
#
SC = maindata['Уровень контроля'].unique()
#
date = maindata['Год'].unique()
#
print('Общее кол-во оценок:', CEst, '.Кол-во оценок группы ПИ101:', CEst1)
print("В датасете находятся оценки студентов ПИ101 с следующими личными номерами:", U)
print("Используемые формы контроля:" , SC)
print("Данные представлены по следующим учебным годам:", date)