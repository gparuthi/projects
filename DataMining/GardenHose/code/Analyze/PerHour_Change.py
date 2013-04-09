from ujson import loads
from dateutil.parser import parse
import csv

f = open('./DataMining/uncompressed/all_locations/all_locs_reduced.json1')
json = loads(f.read())

def write_items_to_file(items, selfpath):
    writer = csv.writer(open(selfpath, 'wb'))
    new_items = [(a.encode('utf-8'),b,c,d,e) for a,b,c,d,e in items]
    for item in new_items:
        writer.writerow(item)
        
### generate the final output for each loc
items =[]
time_in = parse('2012-11-7 4:0:0')
items.append(('location', 'per change', 'abs change','avg', 'standard dev'))
for loc in locs_dict:
    abs_change,per_change,avg,std = get_per_change(time_in,locs_dict[loc])
    t = (loc, per_change, abs_change,avg, std)
    items.append(t)

write_items_to_file(items, "./DataMining/uncompressed/all_locations/stats/locs.csv")
    
    