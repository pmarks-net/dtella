set style data boxes
set style fill solid border -1
set boxwidth 0.8
set xlabel "Hop count of incoming packet"
set ylabel "Packet count"
set xrange [0:14]
plot "hopcounts-processed.txt" using 1:2

