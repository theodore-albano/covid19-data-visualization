#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:52:13 2020

@author: ted
"""
import argparse
import pandas as pd

def graph_country_data(worldcovid19csvfile,country):
    allcountries = pd.read_csv(worldcovid19csvfile)
    onecountrydata = allcountries.loc[allcountries['location'] == country]
    import matplotlib.pyplot as plt
    onecountrydata.plot(x='date',y='new_cases',color='red')
    plt.show()
    
def main():
    parser = argparse.ArgumentParser(description='graph one country covid data')
    parser.add_argument('worldcovid19csvfile', help='world covid19 csv file path name')
    parser.add_argument('country', help='country name (capitalize 1st letter)')
    args = parser.parse_args()
    graph_country_data(args.worldcovid19csvfile, args.country)

if __name__ == "__main__":
    main()    
