import pandas as pd
#
lipa = pd.read_excel("lab_pi_101.xlsx")
CEst = lipa.shape[0]
CEst1 = lipa['Группа'].str.contains('ПИ101').sum()
#CEst = 0
#for index, row in lipa.iterrows():
    #if any(map(str.isdigit, str(row['Сокращенная оценка']))):
        #CEst += 1
#CEst1 = len(lipa[(lipa['Сокращенная оценка'].astype(str).str.isnumeric()) & (lipa['Группа'] == 'ПИ101')])
#print(CEst)
#print('Общее кол-во оценок:', CEst, 'Кол-во оценок группы ПИ101:', CEst1)
UN = lipa[lipa['Группа'] == "ПИ101"]
N = len(UN['Личный номер студента'].unique())
U = lipa.loc[lipa["Группа"] == "ПИ101", "Личный номер студента"].unique()
#
SC = lipa['Уровень контроля'].unique()
#
date = lipa['Год'].unique()
#
print('Общее кол-во оценок:', CEst, '.Кол-во оценок группы ПИ101:', CEst1)
print("В датасете находятся оценки студентов ПИ101 с следующими личными номерами:", U)
print("Используемые формы контроля:" , SC)
print("Данные представлены по следующим учебным годам:", date)