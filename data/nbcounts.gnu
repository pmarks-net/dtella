set style data boxes
set style fill solid border -1
set boxwidth 0.8
set xlabel "Neighbor Count"
set ylabel "Number of Nodes"
plot "nbcounts-processed.txt" using 1:2
