fi = file("nbcounts.txt", "r")
fo = file("nbcounts-processed.txt", "w")

values = [0] * 20 

for line in fi:
    try:
        intval = int(line)
    except ValueError:
        continue
    values[intval] += 1

for v in range(20):
    fo.write("%d %d\n" % (v, values[v]))

fi.close()
fo.close()
