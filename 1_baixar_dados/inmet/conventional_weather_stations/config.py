STATIONS_CODES = "data/conventional_stations_codes.csv"

STATIONS_DATA_HTML = "data/conventional_stations_html"

STATIONS_DATA_CSV = "data/conventional_stations_csv"

WIND_DIRECTIONS_CODES = "data/wind_directions_codes.csv"

LOGIN_URL = "http://www.inmet.gov.br/projetos/rede/pesquisa/inicio.php"

URL_TEMPLATES = {
    'HOUR': {
        'URL': 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt'
               '.php?&mRelEstacao={code}'
               '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={'
               'end_date}&mAtributos=1,1,,,1,1,,1,1,,,1,,,,,'
    },
    'DAY': {
        'URL': 'http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt'
               '.php?&mRelEstacao={code}'
               '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={'
               'end_date}&mAtributos=,,1,1,,,,,,1,1,,1,1,1,1,'
    },
    'DAYFULL': {
        'URL': 'http://www.inmet.gov.br/projetos/rede/pesquisa'
               '/gera_serie_txt.php?&mRelEstacao={code}'
               '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={end_date}'
               '&mAtributos=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'
    },
    'MONTH': {
        'URL': 'http://www.inmet.gov.br/projetos/rede/pesquisa'
               '/gera_serie_txt_mensal.php?&mRelEstacao={code}'
               '&btnProcesso=serie&mRelDtInicio={start_date}&mRelDtFim={end_date}'
               '&mAtributos=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'
    },
}
