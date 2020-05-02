#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt

def graph_country_data(country,next_country,statistic,profile_report_html):
    allcountries = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
    onecountrydata = allcountries.loc[allcountries['location'] == country]
    ax = onecountrydata.plot(x='date',y=statistic,color='blue',label=country)
    print(onecountrydata.describe())
    for name in next_country:
        secondcountrydata = allcountries.loc[allcountries['location'] == name]
        print(secondcountrydata.describe())
        secondcountrydata.plot(x='date',y=statistic,label=name,ax=ax)
    plt.title(statistic)
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.20)
    plt.xlabel('Date')
    plt.ylabel(statistic)
    plt.show()
    if profile_report_html is not None:
        #import pandas_profiling here to avoid making the matplotlib.pyplot axes disappear
        import pandas_profiling
        profile = onecountrydata.profile_report()
        profile.to_file(output_file=profile_report_html)
    
def main():
    parser = argparse.ArgumentParser(description='graph one country COVID-19 data')
    parser.add_argument('statistic', help='one of the following: new_cases new_deaths total_cases total_deaths')
    parser.add_argument('country', help='country name (capitalize 1st letter)')
    parser.add_argument('next_country', nargs='*', help='next country name(s)')
    parser.add_argument('-p','--profile_report_html', help='path name of generated html profile report')
    args = parser.parse_args()
    graph_country_data(args.country,args.next_country,args.statistic,args.profile_report_html)

if __name__ == "__main__":
    main()
