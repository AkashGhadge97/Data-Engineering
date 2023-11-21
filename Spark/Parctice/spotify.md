**>>> spDf = spark.read.csv("/input/spotify.csv",header=True,inferSchema=True)**
**>>> spDf.printSchema()**                                                      
root
 |-- Artist: string (nullable = true)
 |-- Track: string (nullable = true)
 |-- Album: string (nullable = true)
 |-- Album_type: string (nullable = true)
 |-- Danceability: string (nullable = true)
 |-- Energy: string (nullable = true)
 |-- Loudness: double (nullable = true)
 |-- Speechiness: double (nullable = true)
 |-- Acousticness: double (nullable = true)
 |-- Instrumentalness: double (nullable = true)
 |-- Liveness: double (nullable = true)
 |-- Valence: double (nullable = true)
 |-- Tempo: double (nullable = true)
 |-- Duration_min: double (nullable = true)
 |-- Title: string (nullable = true)
 |-- Channel: string (nullable = true)
 |-- Views: string (nullable = true)
 |-- Likes: string (nullable = true)
 |-- Comments: string (nullable = true)
 |-- Licensed: string (nullable = true)
 |-- official_video: string (nullable = true)
 |-- Stream: string (nullable = true)
 |-- EnergyLiveness: string (nullable = true)
 |-- most_playedon: string (nullable = true)

**>>> spDf.show()**
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+---------+--------+--------+--------------+------------+------------------+-------------+
|              Artist|               Track|               Album|Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|             Channel|       Views|    Likes|Comments|Licensed|official_video|      Stream|    EnergyLiveness|most_playedon|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+---------+--------+--------+--------------+------------+------------------+-------------+
|            Gorillaz|      Feel Good Inc.|          Demon Days|     album|       0.818| 0.705|  -6.679|      0.177|     0.00836|         0.00233|   0.613|  0.772|138.559|3.7106666666666666|Gorillaz - Feel G...|            Gorillaz| 693555221.0|6220896.0|169907.0|    True|          True|1040234854.0|1.1500815660685155|      Spotify|
|            Gorillaz|     Rhinestone Eyes|       Plastic Beach|     album|       0.676| 0.703|  -5.815|     0.0302|      0.0869|         6.87E-4|  0.0463|  0.852| 92.761|3.3362166666666666|Gorillaz - Rhines...|            Gorillaz|  72011645.0|1079128.0| 31003.0|    True|          True| 310083733.0|15.183585313174945|      Spotify|
|            Gorillaz|New Gold (feat. T...|New Gold (feat. T...|    single|       0.695| 0.923|   -3.93|     0.0522|      0.0425|          0.0469|   0.116|  0.551|108.014|3.5858333333333334|Gorillaz - New Go...|            Gorillaz|   8435055.0| 282142.0|  7399.0|    True|          True|  63063467.0| 7.956896551724138|      Spotify|
|            Gorillaz|  On Melancholy Hill|       Plastic Beach|     album|       0.689| 0.739|   -5.81|      0.026|     1.51E-5|           0.509|   0.064|  0.578|120.423|3.8977833333333334|Gorillaz - On Mel...|            Gorillaz| 211754952.0|1788577.0| 55229.0|    True|          True| 434663559.0|         11.546875|      Spotify|
|            Gorillaz|      Clint Eastwood|            Gorillaz|     album|       0.663| 0.694|  -8.627|      0.171|      0.0253|             0.0|  0.0698|  0.525|167.953|             5.682|Gorillaz - Clint ...|            Gorillaz| 618480958.0|6197318.0|155930.0|    True|          True| 617259738.0|  9.94269340974212|      Youtube|
|            Gorillaz|                DARE|          Demon Days|     album|        0.76| 0.891|  -5.852|     0.0372|      0.0229|          0.0869|   0.298|  0.966|120.264| 4.083333333333333|Gorillaz - DARE (...|            Gorillaz| 259021161.0|1844658.0| 72008.0|    True|          True| 323850327.0|2.9899328859060406|      Spotify|
|            Gorillaz|New Gold (feat. T...|New Gold (feat. T...|    single|       0.716| 0.897|  -7.185|     0.0629|       0.012|           0.262|   0.325|  0.358| 127.03|4.5690333333333335|Gorillaz - New Go...|           Dom Dolla|    451996.0|  11686.0|   241.0|   False|          True|  10666154.0|              2.76|      Spotify|
|            Gorillaz|She's My Collar (...|     Humanz (Deluxe)|     album|       0.726| 0.815|  -5.886|     0.0313|     0.00799|           0.081|   0.112|  0.462|140.158|3.4926666666666666|Gorillaz - She's ...|          SalvaMuñox|   1010982.0|  17675.0|   260.0|   False|         False| 159605929.0|7.2767857142857135|      Spotify|
|            Gorillaz|Cracker Island (f...|Cracker Island (f...|    single|       0.741| 0.913|   -3.34|     0.0465|     0.00343|           0.103|   0.325|  0.643|120.012|            3.5625|Gorillaz - Cracke...|            Gorillaz|  24459820.0| 739527.0| 20296.0|    True|          True|  42671901.0| 2.809230769230769|      Spotify|
|            Gorillaz|         Dirty Harry|          Demon Days|     album|       0.625| 0.877|  -7.176|      0.162|      0.0315|          0.0811|   0.672|  0.865|192.296|3.8404333333333334|Gorillaz - Dirty ...|            Gorillaz| 154761056.0|1386920.0| 39240.0|    True|          True| 191074713.0|1.3050595238095237|      Spotify|
|Red Hot Chili Pep...|     Californication|Californication (...|     album|       0.592| 0.767|  -2.788|      0.027|      0.0021|         0.00165|   0.127|  0.328| 96.483|           5.49555|Red Hot Chili Pep...|Red Hot Chili Pep...|1018811259.0|4394471.0|121452.0|    True|          True|1055738398.0| 6.039370078740157|      Spotify|
|Red Hot Chili Pep...|    Under the Bridge|Blood Sugar Sex M...|     album|       0.559| 0.345| -13.496|     0.0459|      0.0576|         1.05E-4|   0.141|  0.458| 84.581| 4.405116666666666|Red Hot Chili Pep...|Red Hot Chili Pep...| 246687714.0|1213572.0| 32761.0|    True|          True|1061750522.0|2.4468085106382977|      Spotify|
|Red Hot Chili Pep...|          Can't Stop|By the Way (Delux...|     album|       0.618| 0.938|  -3.442|     0.0456|      0.0179|             0.0|   0.167|  0.875| 91.455| 4.483333333333333|Red Hot Chili Pep...|Red Hot Chili Pep...| 336635759.0|1740224.0| 32573.0|    True|          True| 866464951.0| 5.616766467065868|      Spotify|
|Red Hot Chili Pep...|         Scar Tissue|Californication (...|     album|       0.595| 0.717|  -4.803|     0.0295|      0.0779|         0.00274|   0.108|  0.547| 88.969|           3.59845|Red Hot Chili Pep...|Red Hot Chili Pep...| 435121530.0|1890900.0| 37069.0|    True|          True| 613838674.0| 6.638888888888888|      Spotify|
|Red Hot Chili Pep...|           Otherside|Californication (...|     album|       0.458| 0.795|  -3.265|     0.0574|     0.00316|         2.02E-4|  0.0756|  0.513|123.229| 4.256216666666667|Red Hot Chili Pep...|Red Hot Chili Pep...| 673528656.0|3140356.0| 60091.0|    True|          True| 732774515.0|10.515873015873016|      Spotify|
|Red Hot Chili Pep...|       Snow (Hey Oh)|    Stadium Arcadium|     album|       0.427|   0.9|  -3.674|     0.0499|       0.116|         1.75E-5|   0.119|  0.599|104.655|5.5777833333333335|Red Hot Chili Pep...|Red Hot Chili Pep...| 320871237.0|1272266.0| 37004.0|    True|          True| 860722316.0| 7.563025210084034|      Spotify|
|Red Hot Chili Pep...|     Dani California|    Stadium Arcadium|     album|       0.556| 0.913|   -2.36|     0.0437|      0.0193|         8.59E-6|   0.346|   0.73| 96.184|4.7026666666666666|Red Hot Chili Pep...|Red Hot Chili Pep...| 324228662.0|1456622.0| 49461.0|    True|          True| 550067391.0|2.6387283236994223|      Spotify|
|Red Hot Chili Pep...|          By the Way|By the Way (Delux...|     album|       0.451|  0.97|  -4.938|      0.107|      0.0264|         0.00355|   0.102|  0.198|122.444|           3.61555|Red Hot Chili Pep...|Red Hot Chili Pep...| 179005296.0| 784717.0| 20084.0|    True|          True| 367485508.0| 9.509803921568627|      Spotify|
|Red Hot Chili Pep...|        Give It Away|Blood Sugar Sex M...|     album|       0.666| 0.936|  -9.919|     0.0476|     0.00244|           0.086|   0.153|  0.776| 91.577| 4.715116666666667|Red Hot Chili Pep...|Red Hot Chili Pep...|  86637926.0| 434837.0| 16029.0|    True|          True| 301947159.0|  6.11764705882353|      Spotify|
|Red Hot Chili Pep...|    Dark Necessities|         The Getaway|     album|         0.7| 0.742|  -6.777|     0.0716|      0.0722|          0.0199|    0.11|  0.197| 91.959| 5.033333333333333|Red Hot Chili Pep...|Red Hot Chili Pep...| 440037964.0|2094182.0| 56516.0|    True|          True| 385677873.0| 6.745454545454545|      Youtube|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+---------+--------+--------+--------------+------------+------------------+-------------+
only showing top 20 rows
