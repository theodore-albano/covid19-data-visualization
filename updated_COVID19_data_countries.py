#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from gooey import Gooey

def graph_country_data(country,additional_country,statistic,profile_report_html):
    allcountries = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
    onecountrydata = allcountries.loc[allcountries['location'] == country]
    if len(onecountrydata) > 0:
        try:
            ax = onecountrydata.plot(x='date',y=statistic,color='blue',label=country)
        except KeyError:
            print("\nNo data for statistic {}".format(statistic))
            return
        print("\n\n---{}---\n".format(country))
        print(onecountrydata.describe())
        if additional_country is not None:
            for name in additional_country:
                secondcountrydata = allcountries.loc[allcountries['location'] == name]
                if len(secondcountrydata) > 0:
                    print("\n\n---{}---\n".format(name))
                    print(secondcountrydata.describe())
                    secondcountrydata.plot(x='date',y=statistic,label=name,ax=ax)
                else:
                    print("\nNo data for country {}".format(name))
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
    else:
        print("\nNo data for country {}".format(country))
@Gooey    
def main():
    parser = argparse.ArgumentParser(description='graph world COVID-19 data')
    parser.add_argument('statistic', help='choose one of the following: new_cases, new_deaths, total_cases, total_deaths')
    parser.add_argument('country', help='country name (capitalize 1st letter)')
    parser.add_argument('--additional_country', nargs='*', help='add country name(s), space separated - (if country is more than one word, enclose with single quotes)')
    parser.add_argument('-p','--profile_report_html', help='path name of generated html profile report')
    args = parser.parse_args()
    graph_country_data(args.country,args.additional_country,args.statistic,args.profile_report_html)

if __name__ == "__main__":
    main()
