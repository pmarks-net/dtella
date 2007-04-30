fi = file("bandwidth.24h.txt", "r")
fo = file("bandwidth-processed.txt", "w")

history=[]

for line in fi:
    time, send, recv, nnbs, nnodes = line.split()

    send = float(send) / float(nnbs)
    recv = float(recv) / float(nnbs)
    nnodes = int(nnodes)

    history.append(send+recv)

    if len(history) >= 6*5:
        bw = sum(history) / (60.0 * 5)
        del history[:]

        h, m, s = time.split(':')
        sec = int(h) * 3600 + int(m) * 60 + int(s)

        fo.write("%d %f %d\n" % (sec, bw, nnodes))

fi.close()
fo.close()
