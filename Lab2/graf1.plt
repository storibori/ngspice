set encoding utf8
set termoption noenhanced
set title "* simulación de un diodo zener en ngspice"
set xlabel "s"
set ylabel "V"
set grid
unset logscale x 
set xrange [0.000000e+00:5.000000e-03]
unset logscale y 
set yrange [4.832869e+00:5.007959e+00]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot 'graf1.data' using 1:2 with lines lw 1 title "v(vk)",\
'graf1.data' using 3:4 with lines lw 1 title "v(vin)"
