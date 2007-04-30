set style data lines
set xtics rotate by -45
set xtics ("12am" 0, "1am" 3600, "2am" 7200, "3am" 10800, "4am" 14400, "5am" 18000, "6am" 21600, "7am" 25200, "8am" 28800, "9am" 32400, "10am" 36000, "11am" 39600, "12pm" 43200, "1pm" 46800, "2pm" 50400, "3pm" 54000, "4pm" 57600, "5pm" 61200, "6pm" 64800, "7pm" 68400, "8pm" 72000, "9pm" 75600, "10pm" 79200, "11pm" 82800)
set xrange [0:86400]
set xlabel "Time of day"
set ylabel "Bytes per Second"
plot "bandwidth-processed.txt" using 1:2 title "Bandwidth usage per link"

