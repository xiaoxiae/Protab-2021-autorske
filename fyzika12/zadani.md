<p>Zkoumáte pohyby vzdálených nebeských těles. Zaujala vás soustava čtyř planet, které okolo sebe obíhají.</p>

<p>Snažíte se odsimulovat jejich pohyb z jejich aktuální <strong>pozice</strong> \((x, y, z)\) a <strong>rychlosti</strong> \((d_x, d_y, d_z)\). Každý krok simulace probíhá ve dvou krocích:</p>

<ul>
	<li><strong>gravitace: </strong>pro každou dvojici měsíců: pokud se liší v pozici \(x\) (nebo \(y, z\)), tak se k jejich \(d_x\) (nebo \(d_y, d_z\)) přičte \(\pm 1\) ve směru „k sobě“</li>
	<li><strong>posun:</strong> každý měsíc se posune o svou rychlost</li>
</ul>

<p>Prvních pár kroků simulace vypadá následně:</p>

<pre>
krok 0:
pozice=<-13, 14, -7>   rychlost=< 0,  0,  0>
pozice=<-18,  9,  0>   rychlost=< 0,  0,  0>
pozice=<  0, -3, -3>   rychlost=< 0,  0,  0>
pozice=<-15,  3,-13>   rychlost=< 0,  0,  0>

krok 1:
pozice=<-14, 11, -6>   rychlost=<-1, -3,  1>
pozice=<-15,  8, -3>   rychlost=< 3, -1, -3>
pozice=< -3,  0, -4>   rychlost=<-3,  3, -1>
pozice=<-14,  4,-10>   rychlost=< 1,  1,  3>

krok 2:
pozice=<-15,  5, -4>   rychlost=<-1, -6,  2>
pozice=< -9,  6, -9>   rychlost=< 6, -2, -6>
pozice=< -9,  6, -6>   rychlost=<-6,  6, -2>
pozice=<-13,  6, -4>   rychlost=< 1,  2,  6>
</pre>

<p>Odsimulujte <strong>10000</strong> kroků. Jaký je součin složek rychlostí všech měsíců (pro krok 2 je to např. \(746496\))?</p>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

