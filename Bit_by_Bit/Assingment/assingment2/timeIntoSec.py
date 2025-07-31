# 1. Convert the time entered in hh,min and sec into seconds.
hh = int(input("Enter time into HH MIN SEC\nHH: "))
min = int(input("MIN: "))
sec = int(input("SEC: "))

total_sec = (hh*3600)+(min*60)+(sec)

print(f'After the convert {hh}:{min}:{sec} (HH:MIN:SEC) into seconds is:{total_sec}sec ')