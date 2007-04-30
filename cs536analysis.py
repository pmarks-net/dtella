import time
from twisted.internet import reactor

class Analyzer(object):

    def __init__(self, main):
        self.main = main
        self.statsfile = file("data/pings.txt", "w")

        self.statsfile_bw = file("data/bandwidth.txt", "w")

        self.bw_recv = 0
        self.bw_send = 0
        reactor.callLater(0, self.logBandwidth)

        
    def pingEveryone(self):

        osm = self.main.osm

        self.willping = set([n.ipp for n in osm.nodes])

        def cb():
            try:
                ipp = self.willping.pop()
            except KeyError:
                return

            try:
                n = osm.lookup_ipp[ipp]
            except KeyError:
                pass
            else:
                self.sendAPing(n)

            reactor.callLater(0.1, cb)

        reactor.callLater(0, cb)


    def sendAPing(self, n):

        osm = self.main.osm

        ack_key = n.getPMAckKey()

        packet = ['CP']
        packet.append(osm.me.ipp)
        packet.append(ack_key)
        packet.append('\x00\x00\x00\x00')   # bad hash, should get rejected
        packet.append('\x00\x00\x00\x00')
        packet = ''.join(packet)

        send_time = time.time()

        def fail_cb(reason):
            if not n.location:
                print "!!!"
                return
            
            print "%s %f" % (n.location, (time.time()-send_time)*1000.0)

            self.statsfile.write("%s %f\n" % (
                n.location, (time.time()-send_time)*1000.0))

        n.sendPrivateMessage(self.main.ph, ack_key, packet, fail_cb)


    def logRecv(self, nbytes):
        self.bw_recv += nbytes

    def logSend(self, nbytes):
        self.bw_send += nbytes

    def logBandwidth(self):
        osm = self.main.osm
        if osm:
            nnbs = len(osm.pgm.inbound | osm.pgm.outbound)
            
            import time
            tm = time.strftime("%H:%M:%S")
            
            self.statsfile_bw.write("%s %d %d %d %d\n" % (
                tm, self.bw_send, self.bw_recv, nnbs, len(osm.nodes)))
            self.statsfile_bw.flush()
            
            self.bw_send = 0
            self.bw_recv = 0

        reactor.callLater(10.0, self.logBandwidth)
