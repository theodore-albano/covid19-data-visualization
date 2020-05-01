# covid19-data-visualization
Graph new cases against date for COVID-19 csv files. Visualize new COVID-19 cases over time in order to see trends in growth and decline.
## Getting Started
### Prerequisites

'''pip3 install pandas
pip3 install matplotlib
pip3 install pandas-profiling'''

Get world data set from ourworldindata.org: https://covid.ourworldindata.org/data/who/full_data.csv

Get Japan data set from kaggle: https://www.kaggle.com/lisphilar/covid19-dataset-in-japan#covid_jpn_total.csv

Unzip and use covid_jpn_prefecture.csv

usage: visualizecovid19country.py worldcovid19csvfile country [--profile_report_html PROFILE_REPORT_HTML]

  e.g. ./visualizecovid19country.py full_data.csv Egypt

usage: visualizecovid19japan.py japancsvfile prefecture [--profile_report_html PROFILE_REPORT_HTML]

  e.g. ./visualizecovid19japan.py covid_jpn_prefecture.csv Osaka 

Optional-generate a profile report with pandas-profiling

optional arguments:

  --profile_report_html PROFILE_REPORT_HTML
                        path name of generated html profile report

  e.g. ./visualizecovid19japan.py covid_jpn_prefecture.csv Osaka --profile_report_html osaka_profile_report.html

List of prefectures in Japan:

Hokkaido
Aomori
Iwate
Miyagi
Akita
Yamagata
Fukushima
Ibaraki
Tochigi
Gunma
Saitama
Chiba
Tokyo
Kanagawa
Niigata
Toyama
Ishikawa
Fukui
Yamanashi
Nagano
Gifu
Shizuoka
Aichi
Mie
Shiga
Kyoto
Osaka
Hyogo
Nara
Wakayama
Tottori
Shimane
Okayama
Hiroshima
Yamaguchi
Tokushima
Kagawa
Ehime
Kouchi
Fukuoka
Saga
Nagasaki
Kumamoto
Oita
Miyazaki
Kagoshima
Okinawa

