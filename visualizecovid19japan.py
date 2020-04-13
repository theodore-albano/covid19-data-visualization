#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:36:28 2020

@author: ted
"""
import argparse
import pandas as pd

def graph_japan_data(japancsvfile,prefecture):
    allprefectures = pd.read_csv(japancsvfile)
    oneprefecturedata = allprefectures.loc[allprefectures['Prefecture'] == prefecture]
    import matplotlib.pyplot as plt
    oneprefecturedata.plot(x='Date',y='Positive',color='red')
    plt.show()
    
def main():
    parser = argparse.ArgumentParser(description='graph one japan prefecture covid data')
    parser.add_argument('japancsvfile', help='japan csv file path name')
    parser.add_argument('prefecture', help='prefecture name (capitalize 1st letter)')
    args = parser.parse_args()
    graph_japan_data(args.japancsvfile,args.prefecture)

if __name__ == "__main__":
    main()