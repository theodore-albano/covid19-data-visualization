#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
#from gooey import Gooey

class COVID19DataGrapher:
    def __init__(self,country,additional_country,statistic,profile_report_html):
        self._country = country
        self._additional_country = additional_country
        self._statistic = statistic
        self._profile_report_html = profile_report_html

    def graph_country_data(self):
        allcountries = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
        onecountrydata = allcountries.loc[allcountries['location'] == self._country]
        if len(onecountrydata) > 0:
            try:
                ax = onecountrydata.plot(x='date',y=self._statistic,color='blue',label=self._country)
            except KeyError:
                print("\nNo data for statistic {}".format(self._statistic))
                return
            print("\n\n---{}---\n".format(self._country))
            print(onecountrydata.describe())
            if self._additional_country is not None:
                for name in self._additional_country:
                    secondcountrydata = allcountries.loc[allcountries['location'] == name]
                    if len(secondcountrydata) > 0:
                        print("\n\n---{}---\n".format(name))
                        print(secondcountrydata.describe())
                        secondcountrydata.plot(x='date',y=self._statistic,label=name,ax=ax)
                    else:
                        print("\nNo data for country {}".format(name))
            plt.title(self._statistic)
            plt.xticks(rotation=45)
            plt.subplots_adjust(bottom=0.20)
            plt.xlabel('Date')
            plt.ylabel(self._statistic)
            plt.show()
            if self._profile_report_html is not None:
                #import pandas_profiling here to avoid making the matplotlib.pyplot axes disappear
                import pandas_profiling
                profile = onecountrydata.profile_report()
                profile.to_file(output_file=self._profile_report_html)
        else:
            print("\nNo data for country {}".format(self._country))
#@Gooey    
def main():
    parser = argparse.ArgumentParser(description='graph world COVID-19 data')
    parser.add_argument('statistic', help='choose one of the following: new_cases, new_deaths, total_cases, total_deaths')
    parser.add_argument('country', help='country name (capitalize 1st letter)')
    parser.add_argument('--additional_country', nargs='*', help='add country name(s), space separated - (if country is more than one word, enclose with single quotes)')
    parser.add_argument('-p','--profile_report_html', help='path name of generated html profile report')
    args = parser.parse_args()
    grapher = COVID19DataGrapher(args.country,args.additional_country,args.statistic,args.profile_report_html)
    grapher.graph_country_data()

if __name__ == "__main__":
    main()
