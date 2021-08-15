import pandas as pd
import math as mt

df_cell2adm = pd.read_csv('D:/Acronis/test_case/area2district.csv', sep=',')
df_data = pd.read_csv('D:/Acronis/test_case/data.csv', sep=',')

df_cell2adm.head()
df_data.head()

#Соединяем две таблицы по предикату квадрата(areaid)
df_merge_total = df_cell2adm \
    .merge(df_data, how='inner', on='areaid')

# Вычисляем количество живущих людей в районе, округляем до целого в меньшую сторону
df_merge_total['count_living_people_district'] = df_merge_total.percent * df_merge_total.home
df_merge_total['count_living_people_district'] = df_merge_total.count_living_people_district.astype('float').astype('int')

count_people_living_district_total = df_merge_total.groupby('districtid',as_index=False) \
    .agg({'count_living_people_district': 'sum'})

#Запись текущего фрейма в файл
write_file_count_living_people = count_people_living_district_total.to_csv('D:/Acronis/count_people_living.csv')

# Вычисляем количество работающих людей в районе, округляем до целого в меньшую сторону
df_merge_total['count_job_people_district'] = df_merge_total.percent * df_merge_total.job
df_merge_total['count_job_people_district'] = df_merge_total.count_job_people_district.astype('float').astype('int')

count_people_job_district_total = df_merge_total.groupby('districtid',as_index=False) \
    .agg({'count_job_people_district': 'sum'})

#Запись текущего фрейма в файл
write_file_count_job_people = count_people_job_district_total.to_csv('D:/Acronis/count_people_job.csv')
