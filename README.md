# covid19-data-visualization
Graph COVID-19 statistics against date using csv files. Visualize COVID-19 statistics over time in order to see trends in growth and decline. Compare data from multiple countries in one graph. Available statistics include new cases, total cases, new deaths, and total deaths.

### Prerequisites

pip3 install pandas

pip3 install matplotlib

pip3 install Gooey

pip3 install pandas-profiling

## Graph World COVID-19 data

Enter statistic

Enter country name


Optional:

  Enter additional country name(s)

  Enter a name for the path of your new html profile report

COVID-19 data source: ourworldindata.org - https://covid.ourworldindata.org/data/ecdc/full_data.csv

## Graph Japan COVID-19 data

Get Japan data set from kaggle: https://www.kaggle.com/lisphilar/covid19-dataset-in-japan#covid_jpn_total.csv

Unzip and use covid_jpn_prefecture.csv

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

