'''
Created on Dec 11, 2012

@author: gparuthi
'''
import os
import csv

def analyze_sel(sel):
    items = []
    items.append(['date']+sel[sel.keys()[0]].keys())
    for k in sel:
        name = os.path.basename(k)
        item = [name]
        for c in sel[k]:
            item.append(sel[k][c])
        items.append(item)
    write_items_to_file(items,'sel_items.csv')
    
def analyze_diff(diff_items):
    items = []
    items.append(('change','perc_change','total','location'))
    items += diff_items
    write_items_to_file(items, 'diff_stats.csv')
        

def write_items_to_file(items, selfpath):
    writer = csv.writer(open(selfpath, 'wb'))
    new_items = [(a,b,c,d.encode('utf-8')) for a,b,c,d in items]
    for item in new_items:
        writer.writerow(item)

if __name__ == '__main__':
    pass