#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:36:28 2020

@author: ted
"""
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def graph_japan_data(japancsvfile,prefecture,profile_report_html):
    allprefectures = pd.read_csv(japancsvfile)
    oneprefecturedata = allprefectures.loc[allprefectures['Prefecture'] == prefecture]
    print(oneprefecturedata.describe())
    oneprefecturedata.plot(x='Date', y='Positive', color='blue')
    plt.suptitle(prefecture)
    plt.title('New Cases 3/18/2020-4/08/2020')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.20)
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.show()
    if profile_report_html is not None:
        #import pandas_profiling here to avoid making the matplotlib.pyplot axes disappear
        import pandas_profiling
        profile = oneprefecturedata.profile_report()
        profile.to_file(output_file=profile_report_html)

def main():
    parser = argparse.ArgumentParser(description='graph one japan prefecture covid data')
    parser.add_argument('japancsvfile', help='japan csv file path name')
    parser.add_argument('prefecture', help='prefecture name (capitalize 1st letter)')
    parser.add_argument('--profile_report_html', help='path name of generated html profile report')
    args = parser.parse_args()
    graph_japan_data(args.japancsvfile,args.prefecture,args.profile_report_html)

if __name__ == "__main__":
    main()
