import re
import datetime
from pathlib import Path
import zipfile

import pandas as pd


def get_station_data(path):
    station_df = pd.read_csv(path, sep=';', decimal=',',
                             encoding='ISO-8859-1',
                             nrows=7, index_col=0, header=None).T

    station_df.columns = ['REGIAO', 'UF', 'ESTACAO', 'CODIGO', 'LATITUDE',
                          'LONGITUDE', 'ALTITUDE']

    for field in ['LATITUDE', 'LONGITUDE', 'ALTITUDE']:
        try:
            station_df[field] = station_df[field] \
                .apply(lambda x: float(x.replace(',', '.')))
        except Exception as e:
            station_df[field] = 0

    return station_df['CODIGO'].values[0], station_df

def convert_data(value, input_format, output_format):
    return datetime.datetime.strptime(value, input_format).strftime(output_format)

def convert_hora(value):
    value = re.sub("[^0-9]", "", value)
    value = value[:2].ljust(4, '0')
    return value


def get_climate_data(path):
    climate_df = pd.read_csv(path, sep=';', decimal=',',
                             encoding='ISO-8859-1',
                             header=8)

    climate_df = climate_df[climate_df.columns[:19]]
    if 'Data' in climate_df.columns:
        climate_df['Data'] = climate_df['Data']\
            .apply(lambda x: convert_data(x, '%Y/%m/%d', '%Y-%m-%d'))

    climate_df.columns = [
        'DATA (YYYY-MM-DD)',
        'HORA (UTC)',
        'PRECIPITACAO TOTAL HORARIO (mm)',
        'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)',
        'PRESSAO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)',
        'PRESSAO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)',
        'RADIACAO GLOBAL (W/m2)',
        'TEMPERATURA DO AR - BULBO SECO, HORARIA (C)',
        'TEMPERATURA DO PONTO DE ORVALHO (C)',
        'TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C)',
        'TEMPERATURA MINIMA NA HORA ANT. (AUT) (C)',
        'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (C)',
        'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (C)',
        'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)',
        'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)',
        'UMIDADE RELATIVA DO AR, HORARIA (%)',
        'VENTO, DIRECAO HORARIA (gr)',
        'VENTO, RAJADA MAXIMA (m/s)',
        'VENTO, VELOCIDADE HORARIA (m/s)'
    ]

    climate_df['HORA (UTC)'] = climate_df['HORA (UTC)']\
            .apply(lambda x: convert_hora(x))

    return climate_df

stations = {}
climate_data_all = []

all_zipped_files = [i for i in Path('.').rglob('*.zip')]
for zipped_file in all_zipped_files:
    print(zipped_file)
    with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
        zip_ref.extractall(".")

        all_files = [i for i in Path(str(zipped_file).replace('.zip','')).rglob('*.CSV')]

        for file in all_files:
            try:
                station_code, station_df = get_station_data(file)

                if not station_code in stations:
                    stations[station_code] = station_df

                climate_data = get_climate_data(file)

                climate_data.insert(0, 'ESTACAO', station_code)

                climate_data_all.append(climate_data)

            except Exception as e:
                print('Error in {}!'.format(file))

stations_csv = pd.concat(stations.values())
climate_csv = pd.concat(climate_data_all)

stations_csv.to_csv('automatic_stations_codes.csv',
                    sep=';',
                    index=False,
                    encoding='utf-8')

climate_csv.to_csv('automatic_weather_stations_inmet_brazil_2000_2019.csv',
                   sep=';',
                   index=False,
                   encoding='utf-8')
