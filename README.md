3. September 2016

# Dagatal	

Þessi síða er hugsuð sem skóladagatal fyrir framhaldsskóla á Íslandi. Táknmyndirnar tákna viðburði á skólaárinu. Ef músarbendillinn er lagður yfir myndirnar þá birtist stuttur skýringatexti. Litirnir í dagatalinu tákna frí (rauður), kennsludag (grænn), starfsdag (gulur) og svo daga sem ekki tilheyra skólaárinu (hvítur). Dagatalið opnast sjálfkrafa í núverandi mánuði og markar blár rammi daginn í dag. Hægt er að fletta dagatalinu eins og hverri annarri heimasíðu.

## Gerð síðunnar

Síðan er gerð í [Python 2.7](https://www.python.org/) og [Knockout](http://knockoutjs.com/). Notaði Calendar safnið í Python til þess að búa til Json javascript gögn yfir hvern dag í skólaárinu. Nota Knockout til þess að búa til bindingar milli gagnanna og útlits síðunnar skv. MVW mynstri. Notaði útgáfu 3.2.3 af Bootstrap. Allar táknmyndir síðunannar eru úr Glyphicon táknmyndakerfi Bootstrap.


## Hvernig á að nota síðuna.

Til þess að keyra síðuna er í raun nóg að smella á index.html skránna og þá opnast dagatalið í vafra. 

## Ef breyta á dagatalinu

1. Opnið [Bootstrap síðuna](http://getbootstrap.com/components/) til þess að sjá mögulegar táknmyndir. 

2. Opnið python-skrárnar dagatal.py og dagatalGenerator.py. Í skránni datagal.py koma dagsetningarnar fyrir í orðabók (e. dictionary). Hver slík færsla inniheldur tegund dagsetningar (virkur, profadagur, kennsludagur og helgi). Einnig lista sem afmarkast af []. Inni í listanum eru tvíundir (e. tuples). Fyrra hnitið er skýringatexti en seinna hnitið er textastrengur undir táknmynd úr skrefi 1. Til þess að setja viðkomandi táknmynd inn ásamt texta þurfið þið að bæta við tvíund. Þegar öllum breytingum er lokið þá keyrið þið dagatalGenerator.py skránna. Í Windows er gott að nota Idle umhverfið (veljið run) eða <b>cmd</b> skipanalínuna og 

<pre>
python dagatalGenerator.py
</pre>