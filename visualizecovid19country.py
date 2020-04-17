#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:52:13 2020

@author: ted
"""
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def graph_country_data(worldcovid19csvfile,country,profile_report_html):
    allcountries = pd.read_csv(worldcovid19csvfile)
    onecountrydata = allcountries.loc[allcountries['location'] == country]
    print(onecountrydata.describe())
    onecountrydata.plot(x='date',y='new_cases',color='blue')
    plt.suptitle(country)
    plt.title('New Cases through 3/17/2020')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.20)
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.show()
    if profile_report_html is not None:
        #import pandas_profiling here to avoid making the matplotlib.pyplot axes disappear
        import pandas_profiling
        profile = onecountrydata.profile_report()
        profile.to_file(output_file=profile_report_html)
    
def main():
    parser = argparse.ArgumentParser(description='graph one country covid data')
    parser.add_argument('worldcovid19csvfile', help='world covid19 csv file path name')
    parser.add_argument('country', help='country name (capitalize 1st letter)')
    parser.add_argument('--profile_report_html', help='path name of generated html profile report')
    args = parser.parse_args()
    graph_country_data(args.worldcovid19csvfile,args.country,args.profile_report_html)

if __name__ == "__main__":
    main()
