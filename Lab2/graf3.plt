set encoding utf8
set termoption noenhanced
set title "* circuito de protección de sobretensión con diodo zener 1smb5929b"
set xlabel "Hz"
set ylabel "V"
set grid
set logscale x
set xrange [1e+00:1e+03]
set mxtics 10
set grid mxtics
unset logscale y 
set yrange [-1.100000e+00:1.100000e+00]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot 'graf3.data' using 1:2 with lines lw 1 title "v(vk)"
