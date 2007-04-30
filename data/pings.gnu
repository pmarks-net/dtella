set style data points
set xtics rotate by -45
set logscale y
set xlabel "Location"
set ylabel "Ping time (ms)"
#set style line 1 pt 2
plot "pings-processed.txt" using 1:2

