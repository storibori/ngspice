set encoding utf8
set termoption noenhanced
set title "* simulación de un diodo zener en ngspice"
set xlabel "V"
set ylabel "V"
set grid
unset logscale x 
set xrange [-4.000000e+01:3.990000e+01]
unset logscale y 
set yrange [-4.399500e+01:4.389500e+01]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot 'graf2.data' using 1:2 with lines lw 1 title "v(vk)",\
'graf2.data' using 3:4 with lines lw 1 title "v(vin)"
