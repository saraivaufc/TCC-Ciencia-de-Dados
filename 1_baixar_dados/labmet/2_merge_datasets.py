import hashlib
from os import listdir
from os.path import isfile, join

import pandas as pd

folder = '.'
files = [f for f in listdir(folder) if
         isfile(join(folder, f)) and f.find('.xls') != -1]

months = {
    'Janeiro': 1,
    'Fevereiro': 2,
    'Março': 3,
    'Abril': 4,
    'Maio': 5,
    'Junho': 6,
    'Julho': 7,
    'Agosto': 8,
    'Setembro': 9,
    'Outubro': 10,
    'Novembro': 11,
    'Dezembro': 12
}

variables = [
    'vento maxima 10m',
    'umidade minima',
    'umidade maxima',
    'umidade',
    'temperatura minima',
    'temperatura maxima',
    'temperatura',
    'rad. solar global',
    'evap. de referencia',
    'chuva diaria'
]

dataframes_variables = {

}

dataframe_stations = pd.DataFrame(columns=['Estacao', 'Detalhes'])


def get_variable(filename, variables):
    for v in variables:
        if filename.find(v) != -1:
            return v


for file in files:
    current_variable = get_variable(file, variables)

    print("File:", file)

    xl = pd.ExcelFile(file)
    station_info = next(iter(xl.parse(header=0, nrows=1).to_dict().keys()))
    station_code = hashlib.md5(station_info.encode()).hexdigest()

    if len(dataframe_stations[
               dataframe_stations.Estacao == station_code]) == 0:
        dataframe_stations = dataframe_stations.append({
            'Estacao': station_code,
            'Detalhes': station_info
        }, ignore_index=True)

    for sheet_name in xl.sheet_names:
        print("Sheet name: ", sheet_name)
        year = int(sheet_name)
        df = xl.parse(sheet_name, header=5)
        if 'Ano' in df.columns:
            del df['Ano']
        df['Dia'] = pd.to_numeric(df['Dia'], errors='coerce')

        df = df[df.Dia.notnull()]

        df['Dia'] = df['Dia'].astype('int')
        df = df.melt(id_vars=["Dia"], var_name="Mes",
                     value_name=current_variable)

        df = df[df[current_variable].notnull()]

        df['Estacao'] = station_code
        df['Ano'] = year
        df['Mes'].replace(months, inplace=True)

        df['Data'] = pd.to_datetime(
            dict(year=df.Ano, month=df.Mes, day=df.Dia), errors='coerce')
        df = df[df.Data.notnull()]

        del df['Dia']
        del df['Mes']
        del df['Ano']

        current_dataframe = dataframes_variables.get(current_variable)
        if current_dataframe is None:
            dataframes_variables[current_variable] = df
        else:
            dataframes_variables[current_variable] = pd.concat(
                [current_dataframe, df])

dataframes_variables_keys = list(dataframes_variables.keys())

final_df = dataframes_variables.get(dataframes_variables_keys[0])

for variable in dataframes_variables_keys[1:]:
    final_df = pd.merge(final_df, dataframes_variables[variable], how='outer',
                        on=['Estacao', 'Data'])

start_date = final_df['Data'].min().strftime('%Y-%m-%d')
end_date = final_df['Data'].max().strftime('%Y-%m-%d')

dataframe_stations.to_csv('labmet_automatic_stations_codes.csv', index=False)
final_df.to_csv(
    'labmet_automatic_stations_{}_{}.csv'.format(start_date, end_date),
    index=False)
