# INMET

Atenção: A partir de setembro de 2020, o instituto Nacional de Meteorologia (INMET) entrou em processo de migração para o seu novo portal (https://portal.inmet.gov.br/). 
A partir desta data, seu antigo portal (http://www.inmet
.gov.br) poderá deixar de existir e conseguentemente esse conjunto de scripts
 irão parar de funcionar.
 
 
### Dados baixados de 1961 à 2019
Para obter facilmente os dados de todas as estações meteorológicas
 convencionais gerenciadas pelo INMET baixados para o período de 1961 à 2019
 , acesse [Brazil Weather, Conventional Stations
  (1961-2019)](https://www.kaggle.com/saraivaufc/conventional-weather-stations-brazil)

### Parâmetros

* __Dados Horários__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_horario.php))
    * Dados de 3x ao dia
    * Temp Bulbo Seco(ºC)
	* Temp Bulbo Úmido(ºC)
	* Umidade Relativa(%)
	* Pressão Atm nível Estação(mbar)
	* Direção do Vento - ([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_de_codigos.html))
	* Velocidade do Vento(m/s)
	* Nebulosidade
	* 1,1,,,1,1,,1,1,,,1,,,,,

* __Dados Diários__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_c_diario.php))
    * Dados de 3x ao dia contendo a media diaria e mais algumas medidas calculadas
    * Precipitação (mm)
	* Temp Máxima (ºC)
	* Temp Mínima (ºC)
	* Insolação(horas)
	* Evaporação do Piche (mm)
	* Temperatura Compensada Média(ºC)
	* Umidade Relativa Média (%)
	* Velocidade Vento Média (mps)
	* ,,1,1,,,,,,1,1,,1,1,1,1,

* __Dados Diários Completo__
    * Dados de 3x ao dia contendo a media diaria e mais algumas medidas calculadas
    * Precipitacao - Precipitação (mm)
	* TempBulboSeco (ºC)
	* TempBulboUmido (ºC)
	* TempMaxima - Temp Máxima (ºC)
	* TempMinima - Temp Mínima (ºC)
	* UmidadeRelativa - Umidade Relativa (%)
	* PressaoAtmEstacao - Pressão Atm da Estação (mbar)
	* PressaoAtmMar - Pressão Atm nível Mar Média (mbar)
	* DirecaoVento - Diração do Vento ([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_de_codigos.html))
	* VelocidadeVento (m/s)
	* Insolacao (hs)
	* Nebulosidade - Nebulosidade (décimos) ([tabela](https://pt.wikipedia.org/wiki/Nebulosidade#/media/Ficheiro:Cloud_cover_in_oktas_ptbr.svg))
	* Evaporacao Piche - Evaporação do Piche (mm)
	* Temp Comp Media - Temp Compensada Média(ºC)
	* Umidade Relativa Media - Umidade Relativa Media (%)
	* Velocidade do Vento Media - Velocidade do Vento Média (mps)
	* 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1


* __Dados Mensais__ ([link](http://www.inmet.gov.br/projetos/rede/pesquisa/form_mapas_mensal.ph)p)
    * Dados de 1x ao mes, com a media mensal
    * DirecaoVento - Direção do Vento Predominante ([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_de_codigos.html))
	* VelocidadeVentoMedia - Velocidade do Vento Média (mps)
	* VelocidadeVentoMaximaMedia - Velocidade do Vento Máxima Média (mps)
	* EvaporacaoPiche - Evaporação do Piche (mm)
	* EvapoBHPotencial - Evapotranspiração Potencial BH (mm)
	* EvapoBHReal - Evapotranspiração Real BH (mm)
	* InsolacaoTotal - Insolação Total (hs)
	* NebulosidadeMedia - Nebulosidade Média (décimos) ([tabela](https://pt.wikipedia.org/wiki/Nebulosidade#/media/Ficheiro:Cloud_cover_in_oktas_ptbr.svg))
	* NumDiasPrecipitacao - Número de Dias com Precipitação (qtd)
	* PrecipitacaoTotal - Precipitação Total (mm)
	* PressaoNivelMarMedia - Pressão Atm nível Mar Média (mbar)
	* PressaoMedia - Pressão Atm Média (mbar)
	* TempMaximaMedia - Temp Máxima Média(ºC)
	* TempCompensadaMedia - Temp Compensada Média(ºC)
	* TempMinimaMedia - Temp Mínima Média(ºC)
	* UmidadeRelativaMedia - Umidade Relativa Média (%)
	* VisibilidadeMedia - Visibilidade Média (%)([tabela](http://www.inmet.gov.br/projetos/rede/pesquisa/tabela_visibilidade.html))
	* 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

* Informações sobre os parametros:
    * [Bulbo Umido](https://pt.wikipedia.org/wiki/Temperatura_de_bulbo_%C3%BAmido)
    * [Bulbo Seco](https://es.wikipedia.org/wiki/Temperatura_de_bulbo_seco)
    * Nebulosidade (0/10 de céu coberto)
    	* 0-3 Pouca nebulosidade
    	* 4-6 Parcialmente nublado
    	* 7-10 Muita nebulosidade