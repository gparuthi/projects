
diff_items = []
def af(json):
    for k in json:
        j = json[k]
        diff_items.append((j['count_diff'], j['count_perc'], j['count_7'], k))
