# covid19-data-visualization
graph date against new cases for covid19 csv files

get world data set from ourworldindata.org: https://covid.ourworldindata.org/data/who/full_data.csv

get Japan data set from kaggle: https://www.kaggle.com/lisphilar/covid19-dataset-in-japan#covid_jpn_total.csv
unzip and use covid_jpn_prefecture.csv

install pandas and matplotlib

usage: visualizecovid19country.py worldcovid19csvfile country
e.g. ./visualizecovid19country.py full_data.csv Egypt

usage: visualizecovid19japan.py japancsvfile prefecture
e.g. ./visualizecovid19japan.py covid_jpn_prefecture.csv Osaka
