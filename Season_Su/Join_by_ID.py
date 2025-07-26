#!/usr/bin/python3
import pandas as pd

Data_Frame_Centroids = pd.read_csv('../Centroides-Elevacion_QGIS.csv')

Data_Frame_Region_1 = pd.read_csv('Season_Su_Region_1/R1_IDs.csv')
Data_Frame_Region_1['Datos_ranas_x'] = (
    pd.read_csv('Season_Su_Region_1/Season_Su_Region_1_Results/r1E2gs_x.txt', header = None)
    )
Data_Frame_Region_1['Datos_ranas_p'] = (
    pd.read_csv('Season_Su_Region_1/Season_Su_Region_1_Results/r1E2gs_p.txt', header = None)
    )
Data_Frame_Region_1['Datos_ranas_e'] = (
    pd.read_csv('Season_Su_Region_1/Season_Su_Region_1_Results/r1E2gs_e.txt', header = None)
    )

Data_Frame_Region_2 = pd.read_csv('Season_Su_Region_2/R2_IDs.csv')
Data_Frame_Region_2['Datos_ranas_x'] = (
    pd.read_csv('Season_Su_Region_2/Season_Su_Region_2_Results/r2E2gs_x.txt', header = None)
    )
Data_Frame_Region_2['Datos_ranas_p'] = (
    pd.read_csv('Season_Su_Region_2/Season_Su_Region_2_Results/r2E2gs_p.txt', header = None)
    )
Data_Frame_Region_2['Datos_ranas_e'] = (
    pd.read_csv('Season_Su_Region_2/Season_Su_Region_2_Results/r2E2gs_e.txt', header = None)
    )

Data_Frame_Region_3 = pd.read_csv('Season_Su_Region_3/R3_IDs.csv')
Data_Frame_Region_3['Datos_ranas_x'] = (
    pd.read_csv('Season_Su_Region_3/Season_Su_Region_3_Results/r3E2gs_x.txt', header = None)
    )
Data_Frame_Region_3['Datos_ranas_p'] = (
    pd.read_csv('Season_Su_Region_3/Season_Su_Region_3_Results/r3E2gs_p.txt', header = None)
    )
Data_Frame_Region_3['Datos_ranas_e'] = (
    pd.read_csv('Season_Su_Region_3/Season_Su_Region_3_Results/r3E2gs_e.txt', header = None)
    )

Data_Frame_Region_4 = pd.read_csv('Season_Su_Region_4/R4_IDs.csv')
Data_Frame_Region_4['Datos_ranas_x'] = (
    pd.read_csv('Season_Su_Region_4/Season_Su_Region_4_Results/r4E2gs_x.txt', header = None)
    )
Data_Frame_Region_4['Datos_ranas_p'] = (
    pd.read_csv('Season_Su_Region_4/Season_Su_Region_4_Results/r4E2gs_p.txt', header = None)
    )
Data_Frame_Region_4['Datos_ranas_e'] = (
    pd.read_csv('Season_Su_Region_4/Season_Su_Region_4_Results/r4E2gs_e.txt', header = None)
    )


Data_Frame_Region_1_Merged = pd.merge(Data_Frame_Region_1, Data_Frame_Centroids, on = 'ID', how = 'left')
Data_Frame_Region_2_Merged = pd.merge(Data_Frame_Region_2, Data_Frame_Centroids, on = 'ID', how = 'left')
Data_Frame_Region_3_Merged = pd.merge(Data_Frame_Region_3, Data_Frame_Centroids, on = 'ID', how = 'left')
Data_Frame_Region_4_Merged = pd.merge(Data_Frame_Region_4, Data_Frame_Centroids, on = 'ID', how = 'left')

Data_Frame_Full = pd.concat([Data_Frame_Region_1_Merged,Data_Frame_Region_2_Merged,Data_Frame_Region_3_Merged,Data_Frame_Region_4_Merged])

Data_Frame_Full.to_csv('Data_Frame_Full_Su.csv')
