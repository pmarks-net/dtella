fi = file("pings.txt", "r")
fo = file("pings-processed.txt", "w")

locations = []

for line in fi:
    loc, time = line.rsplit(None, 1)

    try:
        ind = locations.index(loc)
    except ValueError:
        locations.append(loc)
        ind = len(locations)-1

    fo.write("%d %f\n" % (ind, float(time)))

fi.close()
fo.close()

print "set xtics (" + ', '.join(['"%s" %d' % (loc, i) for i, loc in enumerate(locations)]) + ")"
