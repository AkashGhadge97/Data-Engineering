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

**>>> spDf.select("Artist","Views","Likes","Comments").show()**

+--------------------+------------+---------+--------+
|              Artist|       Views|    Likes|Comments|
+--------------------+------------+---------+--------+
|            Gorillaz| 693555221.0|6220896.0|169907.0|
|            Gorillaz|  72011645.0|1079128.0| 31003.0|
|            Gorillaz|   8435055.0| 282142.0|  7399.0|
|            Gorillaz| 211754952.0|1788577.0| 55229.0|
|            Gorillaz| 618480958.0|6197318.0|155930.0|
|            Gorillaz| 259021161.0|1844658.0| 72008.0|
|            Gorillaz|    451996.0|  11686.0|   241.0|
|            Gorillaz|   1010982.0|  17675.0|   260.0|
|            Gorillaz|  24459820.0| 739527.0| 20296.0|
|            Gorillaz| 154761056.0|1386920.0| 39240.0|
|Red Hot Chili Pep...|1018811259.0|4394471.0|121452.0|
|Red Hot Chili Pep...| 246687714.0|1213572.0| 32761.0|
|Red Hot Chili Pep...| 336635759.0|1740224.0| 32573.0|
|Red Hot Chili Pep...| 435121530.0|1890900.0| 37069.0|
|Red Hot Chili Pep...| 673528656.0|3140356.0| 60091.0|
|Red Hot Chili Pep...| 320871237.0|1272266.0| 37004.0|
|Red Hot Chili Pep...| 324228662.0|1456622.0| 49461.0|
|Red Hot Chili Pep...| 179005296.0| 784717.0| 20084.0|
|Red Hot Chili Pep...|  86637926.0| 434837.0| 16029.0|
|Red Hot Chili Pep...| 440037964.0|2094182.0| 56516.0|
+--------------------+------------+---------+--------+
only showing top 20 rows

**>>> spDf.select(col("Artist").alias("Asrtist_Name"),col("Views").alias("Total_Views"),col("Likes").alias("Total_Likes"),col("Comments").alias("Total_Comments")).show()**

+--------------------+------------+-----------+--------------+
|        Asrtist_Name| Total_Views|Total_Likes|Total_Comments|
+--------------------+------------+-----------+--------------+
|            Gorillaz| 693555221.0|  6220896.0|      169907.0|
|            Gorillaz|  72011645.0|  1079128.0|       31003.0|
|            Gorillaz|   8435055.0|   282142.0|        7399.0|
|            Gorillaz| 211754952.0|  1788577.0|       55229.0|
|            Gorillaz| 618480958.0|  6197318.0|      155930.0|
|            Gorillaz| 259021161.0|  1844658.0|       72008.0|
|            Gorillaz|    451996.0|    11686.0|         241.0|
|            Gorillaz|   1010982.0|    17675.0|         260.0|
|            Gorillaz|  24459820.0|   739527.0|       20296.0|
|            Gorillaz| 154761056.0|  1386920.0|       39240.0|
|Red Hot Chili Pep...|1018811259.0|  4394471.0|      121452.0|
|Red Hot Chili Pep...| 246687714.0|  1213572.0|       32761.0|
|Red Hot Chili Pep...| 336635759.0|  1740224.0|       32573.0|
|Red Hot Chili Pep...| 435121530.0|  1890900.0|       37069.0|
|Red Hot Chili Pep...| 673528656.0|  3140356.0|       60091.0|
|Red Hot Chili Pep...| 320871237.0|  1272266.0|       37004.0|
|Red Hot Chili Pep...| 324228662.0|  1456622.0|       49461.0|
|Red Hot Chili Pep...| 179005296.0|   784717.0|       20084.0|
|Red Hot Chili Pep...|  86637926.0|   434837.0|       16029.0|
|Red Hot Chili Pep...| 440037964.0|  2094182.0|       56516.0|
+--------------------+------------+-----------+--------------+
only showing top 20 rows

**>>> spdf.count()**
20594

**>>> spdf.select("*").show()**

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

**>>> spdf.filter(col("Likes") > 100000).show()**

+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+----------+--------+--------+--------------+------------+------------------+-------------+
|              Artist|               Track|               Album|Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|             Channel|       Views|     Likes|Comments|Licensed|official_video|      Stream|    EnergyLiveness|most_playedon|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+----------+--------+--------+--------------+------------+------------------+-------------+
|            Gorillaz|      Feel Good Inc.|          Demon Days|     album|       0.818| 0.705|  -6.679|      0.177|     0.00836|         0.00233|   0.613|  0.772|138.559|3.7106666666666666|Gorillaz - Feel G...|            Gorillaz| 693555221.0| 6220896.0|169907.0|    True|          True|1040234854.0|1.1500815660685155|      Spotify|
|            Gorillaz|     Rhinestone Eyes|       Plastic Beach|     album|       0.676| 0.703|  -5.815|     0.0302|      0.0869|         6.87E-4|  0.0463|  0.852| 92.761|3.3362166666666666|Gorillaz - Rhines...|            Gorillaz|  72011645.0| 1079128.0| 31003.0|    True|          True| 310083733.0|15.183585313174945|      Spotify|
|            Gorillaz|New Gold (feat. T...|New Gold (feat. T...|    single|       0.695| 0.923|   -3.93|     0.0522|      0.0425|          0.0469|   0.116|  0.551|108.014|3.5858333333333334|Gorillaz - New Go...|            Gorillaz|   8435055.0|  282142.0|  7399.0|    True|          True|  63063467.0| 7.956896551724138|      Spotify|
|            Gorillaz|  On Melancholy Hill|       Plastic Beach|     album|       0.689| 0.739|   -5.81|      0.026|     1.51E-5|           0.509|   0.064|  0.578|120.423|3.8977833333333334|Gorillaz - On Mel...|            Gorillaz| 211754952.0| 1788577.0| 55229.0|    True|          True| 434663559.0|         11.546875|      Spotify|
|            Gorillaz|      Clint Eastwood|            Gorillaz|     album|       0.663| 0.694|  -8.627|      0.171|      0.0253|             0.0|  0.0698|  0.525|167.953|             5.682|Gorillaz - Clint ...|            Gorillaz| 618480958.0| 6197318.0|155930.0|    True|          True| 617259738.0|  9.94269340974212|      Youtube|
|            Gorillaz|                DARE|          Demon Days|     album|        0.76| 0.891|  -5.852|     0.0372|      0.0229|          0.0869|   0.298|  0.966|120.264| 4.083333333333333|Gorillaz - DARE (...|            Gorillaz| 259021161.0| 1844658.0| 72008.0|    True|          True| 323850327.0|2.9899328859060406|      Spotify|
|            Gorillaz|Cracker Island (f...|Cracker Island (f...|    single|       0.741| 0.913|   -3.34|     0.0465|     0.00343|           0.103|   0.325|  0.643|120.012|            3.5625|Gorillaz - Cracke...|            Gorillaz|  24459820.0|  739527.0| 20296.0|    True|          True|  42671901.0| 2.809230769230769|      Spotify|
|            Gorillaz|         Dirty Harry|          Demon Days|     album|       0.625| 0.877|  -7.176|      0.162|      0.0315|          0.0811|   0.672|  0.865|192.296|3.8404333333333334|Gorillaz - Dirty ...|            Gorillaz| 154761056.0| 1386920.0| 39240.0|    True|          True| 191074713.0|1.3050595238095237|      Spotify|
|Red Hot Chili Pep...|     Californication|Californication (...|     album|       0.592| 0.767|  -2.788|      0.027|      0.0021|         0.00165|   0.127|  0.328| 96.483|           5.49555|Red Hot Chili Pep...|Red Hot Chili Pep...|1018811259.0| 4394471.0|121452.0|    True|          True|1055738398.0| 6.039370078740157|      Spotify|
|Red Hot Chili Pep...|    Under the Bridge|Blood Sugar Sex M...|     album|       0.559| 0.345| -13.496|     0.0459|      0.0576|         1.05E-4|   0.141|  0.458| 84.581| 4.405116666666666|Red Hot Chili Pep...|Red Hot Chili Pep...| 246687714.0| 1213572.0| 32761.0|    True|          True|1061750522.0|2.4468085106382977|      Spotify|
|Red Hot Chili Pep...|          Can't Stop|By the Way (Delux...|     album|       0.618| 0.938|  -3.442|     0.0456|      0.0179|             0.0|   0.167|  0.875| 91.455| 4.483333333333333|Red Hot Chili Pep...|Red Hot Chili Pep...| 336635759.0| 1740224.0| 32573.0|    True|          True| 866464951.0| 5.616766467065868|      Spotify|
|Red Hot Chili Pep...|         Scar Tissue|Californication (...|     album|       0.595| 0.717|  -4.803|     0.0295|      0.0779|         0.00274|   0.108|  0.547| 88.969|           3.59845|Red Hot Chili Pep...|Red Hot Chili Pep...| 435121530.0| 1890900.0| 37069.0|    True|          True| 613838674.0| 6.638888888888888|      Spotify|
|Red Hot Chili Pep...|           Otherside|Californication (...|     album|       0.458| 0.795|  -3.265|     0.0574|     0.00316|         2.02E-4|  0.0756|  0.513|123.229| 4.256216666666667|Red Hot Chili Pep...|Red Hot Chili Pep...| 673528656.0| 3140356.0| 60091.0|    True|          True| 732774515.0|10.515873015873016|      Spotify|
|Red Hot Chili Pep...|       Snow (Hey Oh)|    Stadium Arcadium|     album|       0.427|   0.9|  -3.674|     0.0499|       0.116|         1.75E-5|   0.119|  0.599|104.655|5.5777833333333335|Red Hot Chili Pep...|Red Hot Chili Pep...| 320871237.0| 1272266.0| 37004.0|    True|          True| 860722316.0| 7.563025210084034|      Spotify|
|Red Hot Chili Pep...|     Dani California|    Stadium Arcadium|     album|       0.556| 0.913|   -2.36|     0.0437|      0.0193|         8.59E-6|   0.346|   0.73| 96.184|4.7026666666666666|Red Hot Chili Pep...|Red Hot Chili Pep...| 324228662.0| 1456622.0| 49461.0|    True|          True| 550067391.0|2.6387283236994223|      Spotify|
|Red Hot Chili Pep...|          By the Way|By the Way (Delux...|     album|       0.451|  0.97|  -4.938|      0.107|      0.0264|         0.00355|   0.102|  0.198|122.444|           3.61555|Red Hot Chili Pep...|Red Hot Chili Pep...| 179005296.0|  784717.0| 20084.0|    True|          True| 367485508.0| 9.509803921568627|      Spotify|
|Red Hot Chili Pep...|        Give It Away|Blood Sugar Sex M...|     album|       0.666| 0.936|  -9.919|     0.0476|     0.00244|           0.086|   0.153|  0.776| 91.577| 4.715116666666667|Red Hot Chili Pep...|Red Hot Chili Pep...|  86637926.0|  434837.0| 16029.0|    True|          True| 301947159.0|  6.11764705882353|      Spotify|
|Red Hot Chili Pep...|    Dark Necessities|         The Getaway|     album|         0.7| 0.742|  -6.777|     0.0716|      0.0722|          0.0199|    0.11|  0.197| 91.959| 5.033333333333333|Red Hot Chili Pep...|Red Hot Chili Pep...| 440037964.0| 2094182.0| 56516.0|    True|          True| 385677873.0| 6.745454545454545|      Youtube|
|             50 Cent|          In Da Club|Get Rich Or Die T...|     album|       0.902|  0.72|  -2.776|      0.347|        0.26|             0.0|  0.0749|  0.805| 90.059|           3.22445|50 Cent - In Da C...|          50CentVEVO|1682616458.0|10481678.0|296745.0|    True|          True|1041736808.0| 9.612817089452603|      Youtube|
|             50 Cent|          Candy Shop|        The Massacre|     album|       0.614| 0.574|  -7.961|      0.466|      0.0253|          3.2E-5|    0.38|  0.755|125.173| 3.485116666666667|50 Cent - Candy S...|          50CentVEVO| 838974650.0| 5014527.0|113251.0|    True|          True| 701248893.0|1.5105263157894735|      Youtube|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+----------+--------+--------+--------------+------------+------------------+-------------+
only showing top 20 rows

**>>> spdf.filter((col("Likes") > 100000) & (col("Comments") > 100000)).show()**

+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+----------+--------+--------+--------------+------------+------------------+-------------+
|              Artist|               Track|               Album|Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|             Channel|       Views|     Likes|Comments|Licensed|official_video|      Stream|    EnergyLiveness|most_playedon|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+----------+--------+--------+--------------+------------+------------------+-------------+
|            Gorillaz|      Feel Good Inc.|          Demon Days|     album|       0.818| 0.705|  -6.679|      0.177|     0.00836|         0.00233|   0.613|  0.772|138.559|3.7106666666666666|Gorillaz - Feel G...|            Gorillaz| 693555221.0| 6220896.0|169907.0|    True|          True|1040234854.0|1.1500815660685155|      Spotify|
|            Gorillaz|      Clint Eastwood|            Gorillaz|     album|       0.663| 0.694|  -8.627|      0.171|      0.0253|             0.0|  0.0698|  0.525|167.953|             5.682|Gorillaz - Clint ...|            Gorillaz| 618480958.0| 6197318.0|155930.0|    True|          True| 617259738.0|  9.94269340974212|      Youtube|
|Red Hot Chili Pep...|     Californication|Californication (...|     album|       0.592| 0.767|  -2.788|      0.027|      0.0021|         0.00165|   0.127|  0.328| 96.483|           5.49555|Red Hot Chili Pep...|Red Hot Chili Pep...|1018811259.0| 4394471.0|121452.0|    True|          True|1055738398.0| 6.039370078740157|      Spotify|
|             50 Cent|          In Da Club|Get Rich Or Die T...|     album|       0.902|  0.72|  -2.776|      0.347|        0.26|             0.0|  0.0749|  0.805| 90.059|           3.22445|50 Cent - In Da C...|          50CentVEVO|1682616458.0|10481678.0|296745.0|    True|          True|1041736808.0| 9.612817089452603|      Youtube|
|             50 Cent|          Candy Shop|        The Massacre|     album|       0.614| 0.574|  -7.961|      0.466|      0.0253|          3.2E-5|    0.38|  0.755|125.173| 3.485116666666667|50 Cent - Candy S...|          50CentVEVO| 838974650.0| 5014527.0|113251.0|    True|          True| 701248893.0|1.5105263157894735|      Youtube|
|           Metallica|Nothing Else Matt...|Metallica (Remast...|     album|       0.547| 0.394|  -9.793|     0.0262|      0.0522|          6.4E-6|  0.0795|   0.17| 142.37| 6.478883333333333|Metallica: Nothin...|           Metallica|1209806093.0| 5127599.0|135946.0|    True|          True|         0.0| 4.955974842767295|      Youtube|
|            Coldplay|              Yellow|          Parachutes|     album|       0.429| 0.661|  -7.227|     0.0281|     0.00239|         1.21E-4|   0.234|  0.285|173.372|4.4462166666666665|Coldplay - Yellow...|            Coldplay| 832532409.0| 4600933.0|118296.0|    True|          True|1483622308.0| 2.824786324786325|      Spotify|
|            Coldplay|        Viva La Vida|Viva La Vida or D...|     album|       0.486| 0.617|  -7.115|     0.0287|      0.0954|         3.23E-6|   0.109|  0.417|138.015|           4.03955|Coldplay - Viva L...|            Coldplay| 789581468.0| 4370461.0|261790.0|    True|          True|1325575712.0| 5.660550458715596|      Spotify|
|            Coldplay|Something Just Li...|Memories...Do Not...|     album|       0.617| 0.635|  -6.769|     0.0317|      0.0498|         1.44E-5|   0.164|  0.446|103.019|4.1193333333333335|The Chainsmokers ...|    ChainsmokersVEVO|2118018686.0|10282499.0|270444.0|    True|          True|2030825694.0|3.8719512195121952|      Youtube|
|            Coldplay|       The Scientist|A Rush of Blood t...|     album|       0.557| 0.442|  -7.224|     0.0243|       0.731|         1.46E-5|    0.11|  0.213|146.277|              5.16|Coldplay - The Sc...|            Coldplay|1082588109.0| 5532787.0|124357.0|    True|          True|1465980600.0|4.0181818181818185|      Spotify|
|            Coldplay|            Paradise|         Mylo Xyloto|     album|       0.449| 0.585|  -6.761|     0.0268|      0.0509|         8.75E-5|  0.0833|  0.212|139.631| 4.645316666666667|Coldplay - Paradi...|            Coldplay|1665814269.0| 8497224.0|343020.0|    True|          True| 927288329.0| 7.022809123649459|      Youtube|
|            Coldplay|Hymn for the Weekend|A Head Full of Dr...|     album|       0.491| 0.693|  -6.487|     0.0377|       0.211|         6.92E-6|   0.325|  0.412| 90.027|           4.30445|Coldplay - Hymn F...|            Coldplay|1828242112.0|13515772.0|377666.0|    True|          True|1049654852.0| 2.132307692307692|      Youtube|
|            Coldplay|         My Universe|Music Of The Spheres|     album|       0.573| 0.711|  -6.268|     0.0406|      0.0114|             0.0|   0.328|   0.47|105.006|3.7699666666666665|Coldplay X BTS - ...|            Coldplay| 254655970.0| 8867547.0|432726.0|    True|          True| 883224238.0| 2.167682926829268|      Spotify|
|            Coldplay|             Fix You|                 X&Y|     album|       0.209| 0.417|   -8.74|     0.0338|       0.164|         0.00196|   0.113|  0.124|138.178|           4.92555|Coldplay - Fix Yo...|            Coldplay| 566239229.0| 2962029.0|114460.0|    True|          True|1115171056.0|3.6902654867256635|      Spotify|
|           Daft Punk|       One More Time|           Discovery|     album|       0.613| 0.697|  -8.618|      0.133|      0.0194|             0.0|   0.332|  0.476|122.746| 5.339283333333333|Daft Punk - One M...|           Daft Punk| 432177586.0| 2707992.0|110189.0|    True|          True| 471747761.0|2.0993975903614457|      Spotify|
|         Linkin Park|          In the End|Hybrid Theory (Bo...|     album|       0.556| 0.864|   -5.87|     0.0584|     0.00958|             0.0|   0.209|    0.4|105.143|3.6146666666666665|In The End [Offic...|         Linkin Park|1487186392.0|10183387.0|409471.0|    True|          True|1444841705.0| 4.133971291866029|      Youtube|
|         Linkin Park|                Numb|             Meteora|     album|       0.496| 0.863|  -4.153|     0.0381|      0.0046|             0.0|   0.639|  0.243|110.018|3.0931166666666665|Numb [Official Mu...|         Linkin Park|1928733776.0|12341722.0|550921.0|    True|          True|1195213410.0| 1.350547730829421|      Youtube|
|         Linkin Park|      What I've Done| Minutes to Midnight|     album|       0.623|  0.93|  -5.285|     0.0324|      0.0141|         1.64E-6|   0.138|  0.287|120.119|3.4268833333333335|What I've Done [O...|         Linkin Park| 587927093.0| 3370635.0|148741.0|    True|          True| 589294152.0| 6.739130434782608|      Spotify|
|         Linkin Park|        BURN IT DOWN|       LIVING THINGS|     album|       0.585| 0.972|   -4.45|     0.0534|      0.0143|             0.0|  0.0707|  0.585|110.006|           3.83755|BURN IT DOWN [Off...|         Linkin Park| 353135986.0| 2534190.0|113567.0|    True|          True| 368132993.0|13.748231966053748|      Spotify|
|           Radiohead|               Creep|         Pablo Honey|     album|       0.515|  0.43|  -9.935|     0.0372|      0.0097|         1.33E-4|   0.129|  0.104| 91.844| 3.977333333333333|   Radiohead - Creep|           Radiohead| 763497849.0| 4777393.0|147276.0|    True|          True|1101854725.0| 3.333333333333333|      Spotify|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+------------+----------+--------+--------+--------------+------------+------------------+-------------+
only showing top 20 rows

>>> **spdf.distinct().show()**

+--------------------+--------------------+--------------------+-----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----------+---------+--------+--------+--------------+-----------+------------------+-------------+
|              Artist|               Track|               Album| Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|             Channel|      Views|    Likes|Comments|Licensed|official_video|     Stream|    EnergyLiveness|most_playedon|
+--------------------+--------------------+--------------------+-----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----------+---------+--------+--------+--------------+-----------+------------------+-------------+
|     Michael Jackson|Rock with You - S...|        Off the Wall|      album|       0.808| 0.535| -12.521|     0.0353|       0.179|         9.91E-5|   0.158|  0.848|114.031|3.6771166666666666|Michael Jackson -...|  michaeljacksonVEVO|301845823.0|2269865.0| 87490.0|    True|          True|346137424.0| 3.386075949367089|      Spotify|
|       Frank Sinatra|Santa Claus Is Co...|Christmas Songs b...|      album|       0.646| 0.204| -11.957|     0.0565|       0.826|             0.0|   0.312|  0.688|140.281|2.5773333333333333|Santa Claus is Co...|          Sands-show|  1679701.0|  23726.0|   533.0|   False|         False| 88041370.0|0.6538461538461539|      Spotify|
|         Hans Zimmer|                Time|Inception (Music ...|      album|       0.286|0.0968| -16.806|     0.0323|       0.178|           0.696|  0.0861| 0.0395| 62.881|            4.5926|Hans Zimmer - Tim...|    WaterTower Music|  2253213.0|  32073.0|   982.0|    True|          True|274717861.0| 1.124274099883856|      Spotify|
|            Bee Gees|       Stayin' Alive|Staying Alive (Or...|compilation|       0.707| 0.535| -19.793|     0.0436|       0.113|         0.00615|  0.0884|  0.641|103.644|1.5477833333333333|Bee Gees - Stayin...|         BeeGeesVEVO|281066254.0|2720170.0| 71642.0|    True|          True|134009247.0| 6.052036199095022|      Youtube|
|       The Offspring|  Staring At The Sun|           Americana|      album|       0.403| 0.952|  -3.925|      0.202|       0.259|             0.0|   0.123|  0.729| 87.833|           2.22645|  Staring At The Sun|The Offspring - T...|  4605524.0|  45728.0|    99.0|    True|          True| 53918632.0| 7.739837398373983|      Spotify|
|            Ice Cube|Gangsta Rap Made ...|         Raw Footage|      album|        0.81| 0.745|  -5.431|      0.097|     0.00712|          2.1E-5|   0.321|  0.388| 87.019| 4.694216666666667|Ice Cube - Gangst...|Ice Cube / Cubevi...|  3462419.0|  62675.0|  1861.0|   False|         False| 52324827.0|2.3208722741433023|      Spotify|
|         Céline Dion|"My Heart Will Go...|Let's Talk About ...|      album|       0.428| 0.276| -11.729|     0.0312|       0.732|         5.33E-6|   0.117| 0.0382| 99.195| 4.666666666666667|CELINE DION: My h...|      TommySuper2011|  6895026.0|  71541.0|  2827.0|   False|         False|430022654.0| 2.358974358974359|      Spotify|
|         Gabry Ponte|Call Me (with R3H...|Call Me (with R3H...|     single|       0.398| 0.956|  -4.429|      0.329|     0.00935|          0.0038|   0.142|  0.269|106.581|2.9718333333333335|Gabry Ponte, R3HA...|         Gabry Ponte|  2755997.0|  33037.0|   342.0|    True|          True| 48546790.0| 6.732394366197183|      Spotify|
|       George Strait|I Cross My Heart ...|        Pure Country|      album|       0.526| 0.442| -10.133|     0.0259|       0.267|         5.49E-5|   0.106|  0.284|131.055| 3.533333333333333|George Strait - I...|    GeorgeStraitVEVO| 51666154.0| 318707.0| 15094.0|    True|          True| 69432226.0| 4.169811320754717|      Spotify|
|    Shekhar Ravjiani|   Jhoome Jo Pathaan|             Pathaan|     single|       0.817| 0.738|  -7.639|     0.0748|      0.0964|             0.0|   0.331|  0.616|104.964|            3.4694|Jhoome Jo Pathaan...|                 YRF|195454813.0|3334223.0|185883.0|    True|          True| 22899885.0| 2.229607250755287|      Youtube|
|        Van Morrison|Into the Mystic -...|           Moondance|      album|       0.608| 0.524| -10.266|     0.0309|       0.367|         0.00254|   0.115|  0.797| 86.204|3.4268833333333335|Van Morrison - In...|               RHINO|  4302880.0|  38657.0|  1371.0|    True|          True|259257572.0| 4.556521739130435|      Spotify|
|Dimitri Vegas & L...|         Say My Name|         Say My Name|     single|       0.729| 0.788|  -4.832|     0.0908|      0.0703|             0.0|   0.115|  0.857|118.039| 2.658933333333333|Dimitri Vegas & L...|Dimitri Vegas & L...|  3877674.0|  50981.0|  1627.0|   False|          True|146207284.0| 6.852173913043479|      Spotify|
|Dimitri Vegas & L...|      Sweet Caroline|      Sweet Caroline|     single|       0.302|   0.8|  -4.032|     0.0376|     0.00596|         5.16E-5|   0.142|  0.328|149.939| 3.574866666666667|Dimitri Vegas & L...|Dimitri Vegas & L...|  3877674.0|  50981.0|  1627.0|   False|          True|  4096818.0| 5.633802816901409|      Spotify|
|        Cyndi Lauper|     Time After Time|    She's So Unusual|      album|       0.726| 0.449|  -9.206|     0.0286|       0.487|         1.34E-6|  0.0824|  0.294|130.388| 4.022216666666667|Cyndi Lauper - Ti...|     CyndiLauperVEVO|473942502.0|2118208.0| 68822.0|    True|          True|552756900.0| 5.449029126213592|      Spotify|
|     Cristian Castro|           Resistiré|           Resistiré|     single|        0.45| 0.878|  -4.592|     0.0827|      0.0071|             0.0|  0.0908|  0.744|199.844|4.2073833333333335|Resistiré México ...| Warner Music México| 15922754.0| 260404.0| 14941.0|    True|          True| 48533462.0| 9.669603524229075|      Spotify|
|        Rocío Dúrcal|La Gata Bajo la L...|Lo Mejor De Lo Mejor|      album|       0.499| 0.652|  -5.784|     0.0341|        0.73|             0.0|   0.643|  0.484| 88.321|           3.58155|Rocío Dúrcal - La...|        Rocío Dúrcal|  3572594.0|  33610.0|   846.0|   False|          True|145145018.0|1.0139968895800933|      Spotify|
| Gustavo Santaolalla|All Gone (No Escape)|      The Last of Us|      album|        0.14|0.0739| -22.458|     0.0437|       0.916|           0.947|  0.0961| 0.0313|141.524|           2.90555|Gustavo Santaolal...| SonySoundtracksVEVO|    46931.0|   1038.0|    29.0|    True|          True| 11028195.0|0.7689906347554629|      Spotify|
|Los Cadetes De Li...|  Cruzando el Puente| 4 Decadas de Exitos|      album|       0.803| 0.745|  -6.155|      0.039|       0.179|         0.00687|  0.0417|  0.964|111.417|2.6842166666666665|Cruzando el Puent...|      irodriguez2062|   100482.0|   1188.0|    21.0|   False|         False| 14658092.0| 17.86570743405276|      Spotify|
|    Sukhwinder Singh|"Chaiyya Chaiyya ...|Bollywood's Music...|      album|       0.786| 0.579| -14.913|      0.142|       0.186|             0.0|   0.118|  0.481| 90.012|           6.94355|Chal Chaiya Chaiy...|  90s bollywood love| 28042161.0| 193772.0|  3540.0|   False|         False| 35796226.0| 4.906779661016949|      Spotify|
|      Sadhana Sargam|      Manmadhane Nee|Manmadhan (Origin...|      album|       0.667| 0.772|  -6.661|     0.0498|       0.349|         1.06E-4|   0.355|  0.429| 89.986|            4.5356|Manmadhan | Manma...|   Think Music India| 11842836.0| 129755.0|  3403.0|   False|         False| 12833849.0| 2.174647887323944|      Spotify|
+--------------------+--------------------+--------------------+-----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----------+---------+--------+--------+--------------+-----------+------------------+-------------+
only showing top 20 rows

>>> **spdf.distinct().select("Artist").show()**

+--------------------+
|              Artist|
+--------------------+
|     Michael Jackson|
|       Frank Sinatra|
|         Hans Zimmer|
|            Bee Gees|
|       The Offspring|
|            Ice Cube|
|         Céline Dion|
|         Gabry Ponte|
|       George Strait|
|    Shekhar Ravjiani|
|        Van Morrison|
|Dimitri Vegas & L...|
|Dimitri Vegas & L...|
|        Cyndi Lauper|
|     Cristian Castro|
|        Rocío Dúrcal|
| Gustavo Santaolalla|
|Los Cadetes De Li...|
|    Sukhwinder Singh|
|      Sadhana Sargam|
+--------------------+
only showing top 20 rows

**>>>  spdf.dropDuplicates(["Artist"]).count()**

2074

**>>> spdf.select(count("Track").alias("Total Tracks")).show()**

+------------+
|Total Tracks|
+------------+
|       20594|
+------------+

**>>> spdf2=spdf.withColumn("Likes",col("Likes").cast("integer")).withColumn("Comments",col("Comments").cast("integer")).withColumn("Views",col("Views").cast("integer"))**
**>>> spdf2.printSchema()**

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
 |-- Views: integer (nullable = true)
 |-- Likes: integer (nullable = true)
 |-- Comments: integer (nullable = true)
 |-- Licensed: string (nullable = true)
 |-- official_video: string (nullable = true)
 |-- Stream: string (nullable = true)
 |-- EnergyLiveness: string (nullable = true)
 |-- most_playedon: string (nullable = true)

**>>> spdf.select(max("Likes")).show()**

+----------+
|max(Likes)|
+----------+
| 607523565|
+----------+

**>>> spdf.select(max("Views")).show()**

+----------+
|max(Views)|
+----------+
|2133459242|
+----------+

**>>> spdf.select(max("Comments")).show()**

+-------------+
|max(Comments)|
+-------------+
|    190851352|
+-------------+

**>>> spdf.orderBy("Likes").show(10)**
+------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----+-----+--------+-----------------+--------------+---------+--------------+-------------+
|      Artist|               Track|               Album|Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|             Channel|Views|Likes|Comments|         Licensed|official_video|   Stream|EnergyLiveness|most_playedon|
+------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----+-----+--------+-----------------+--------------+---------+--------------+-------------+
|  Miky Woodz|       Suave (Remix)|           El Hombre|     album|       0.875| 0.909|  -3.558|      0.076|        0.14|         0.00185|  0.0616|  0.524|119.999|            5.0921|"El Alfa El Jefe ...|        Bryant Myers| null| null|    null|   ElAlfaElJefeTV|   262630290.0|1697154.0|       42215.0|         True|
|  MC Ryan SP|              Sereia|           Vida Cara|     album|       0.651| 0.661|   -5.08|      0.147|       0.276|             0.0|   0.105|  0.505|114.528| 4.906983333333334|"Orochi ""SEREIA ...|                Xamã| null| null|    null|       66708497.0|      717032.0|   9305.0|          True|         True|
| Jay Wheeler|La Curiosidad (fe...|La Curiosidad (Bl...|    single|       0.841| 0.674|   -5.35|     0.0962|       0.104|             0.0|   0.131|  0.761| 90.007| 6.375916666666667|"Jay Wheeler - La...|              JHAYCO| null| null|    null|      Jay Wheeler|    94815197.0| 698005.0|       26567.0|        False|
|   Neo Beats|              Sereia|           Vida Cara|     album|       0.651| 0.661|   -5.08|      0.147|       0.276|             0.0|   0.105|  0.505|114.528| 4.906983333333334|"Orochi ""SEREIA ...|                Xamã| null| null|    null|       66706686.0|      717021.0|   9305.0|          True|         True|
|      Orochi|              Sereia|           Vida Cara|     album|       0.651| 0.661|   -5.08|      0.147|       0.276|             0.0|   0.105|  0.505|114.528| 4.906983333333334|"Orochi ""SEREIA ...|                Xamã| null| null|    null|       66706686.0|      717025.0|   9305.0|          True|         True|
|      Orochi|             Balão 2|           Vida Cara|     album|       0.612| 0.724|  -5.423|     0.0477|       0.186|             0.0|   0.109|  0.268|137.877|            4.2029|"Orochi ""BALÃO 2...|               Kizzy| null| null| 4024007|         183194.0|        6030.0|     True|          True|    3251577.0|
|Bryant Myers|       Suave (Remix)|           El Hombre|     album|       0.875| 0.909|  -3.558|      0.076|        0.14|         0.00185|  0.0616|  0.524|119.999|            5.0921|"El Alfa El Jefe ...|        Bryant Myers| null| null|    null|   ElAlfaElJefeTV|   262630494.0|1697155.0|       42215.0|         True|
|      Noriel|       Suave (Remix)|           El Hombre|     album|       0.875| 0.909|  -3.558|      0.076|        0.14|         0.00185|  0.0616|  0.524|119.999|            5.0921|"El Alfa El Jefe ...|        Bryant Myers| null| null|    null|   ElAlfaElJefeTV|   262630494.0|1697156.0|       42215.0|         True|
|  Stray Kids|TASTE (Lee Know, ...|            MAXIDENT|     album|       0.626| 0.623|  -5.718|     0.0653|      0.0559|             0.0|   0.199|  0.123|140.209|             3.602|"Stray Kids ?MAXI...|                  ??| null| null|    null|JYP Entertainment|     2024369.0| 305000.0|        8467.0|         True|
|  Stray Kids|Red Lights (Bang ...|              NOEASY|     album|       0.707|  0.74|  -4.311|     0.0509|       0.179|             0.0|   0.612|  0.336|127.974|3.1651166666666666|"Stray Kids ""?? (??| ??)(Red Lights (...| null| null|70239296|        2534046.0|       95743.0|     True|          True|   83113843.0|
+------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----+-----+--------+-----------------+--------------+---------+--------------+-------------+
only showing top 10 rows

**>>> spdf.orderBy(col("Views").asc()).show(10)**
+-------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----+--------+--------+--------------+--------------+------------+------------------+-----------------+
|       Artist|               Track|               Album|Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|             Channel|Views|   Likes|Comments|      Licensed|official_video|      Stream|    EnergyLiveness|    most_playedon|
+-------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----+--------+--------+--------------+--------------+------------+------------------+-----------------+
|      Becky G|             Mayores|          MALA SANTA|     album|       0.745| 0.836|  -4.336|     0.0444|       0.145|         0.00314|   0.116|  0.874| 96.993|           3.38645|Becky G, Bad Bunn...|          BeckyGVEVO| null| 7856227|  319541|          True|          True| 612105921.0| 7.206896551724137|          Youtube|
| Shawn Mendes|    Treat You Better|          Illuminate|     album|       0.444| 0.819|  -4.078|      0.341|       0.106|             0.0|   0.107|  0.747| 82.695|3.1328833333333335|Shawn Mendes - Tr...|     ShawnMendesVEVO| null|11040774|  273330|          True|          True|1697308263.0| 7.654205607476635|          Youtube|
|      G Herbo|         Cry No More|                  25|     album|        0.74| 0.611|  -7.312|      0.155|       0.227|             0.0|  0.0991|  0.534|129.947|3.6969333333333334|"G Herbo ""Cry No...| Lil Tjay (Music ...| null|  136928|    2680|          41.0|         False|       False|        40105548.0|6.165489404641776|
| Clean Bandit|Rockabye (feat. S...|What Is Love? (De...|     album|       0.717|  0.73|  -4.729|     0.0568|       0.383|             0.0|   0.398|  0.792|102.002| 4.186216666666667|Clean Bandit - Ro...|        Clean Bandit| null|13333328|  301384|          True|          True|1312649614.0|1.8341708542713566|          Youtube|
|           MØ|             Lean On|Peace Is The Miss...|     album|       0.723| 0.809|  -3.081|     0.0625|     0.00346|         0.00123|   0.565|  0.274| 98.007|2.9426833333333335|Major Lazer & DJ ...|Major Lazer Official| null|16211083|  450170|         False|         False|1713070715.0|1.4318584070796463|          Youtube|
| Ankit Tiwari|Valentine's Mashu...|Valentine's Mashu...|    single|       0.595|  0.61|  -6.887|     0.0499|       0.332|         2.14E-6|  0.0628|  0.314| 97.974|3.5420333333333334|"Valentine's Mash...|Sd Style"")By Amr...| null|    7489|     190|           0.0|         False|       False|        55399812.0|9.713375796178344|
|   Miky Woodz|       Suave (Remix)|           El Hombre|     album|       0.875| 0.909|  -3.558|      0.076|        0.14|         0.00185|  0.0616|  0.524|119.999|            5.0921|"El Alfa El Jefe ...|        Bryant Myers| null|    null|    null|ElAlfaElJefeTV|   262630290.0|   1697154.0|           42215.0|             True|
|  Jay Wheeler|La Curiosidad (fe...|La Curiosidad (Bl...|    single|       0.841| 0.674|   -5.35|     0.0962|       0.104|             0.0|   0.131|  0.761| 90.007| 6.375916666666667|"Jay Wheeler - La...|              JHAYCO| null|    null|    null|   Jay Wheeler|    94815197.0|    698005.0|           26567.0|            False|
|Fifth Harmony|            Worth It|            Worth It|    single|       0.858|  0.78|  -3.739|     0.0738|      0.0478|         5.72E-5|   0.133|  0.602| 99.984|3.0876166666666665|Fifth Harmony - W...|    FifthHarmonyVEVO| null|11228568|  337695|          True|          True|  18298540.0| 5.864661654135338|          Youtube|
|Fifth Harmony|Work from Home (f...|       7/27 (Deluxe)|     album|       0.803| 0.585|  -5.861|     0.0432|       0.103|         3.94E-6|  0.0644|  0.593|105.017| 3.574666666666667|Fifth Harmony - W...|    FifthHarmonyVEVO| null|11869546|  471291|          True|          True|1270912565.0| 9.083850931677018|          Youtube|
+-------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+-----+--------+--------+--------------+--------------+------------+------------------+-----------------+
only showing top 10 rows

**>>> spdf.orderBy(col("Views").desc()).show(10)**
+----------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+-----------------+----------+--------+--------+--------+--------------+------------+------------------+-------------+
|          Artist|               Track|               Album|Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|          Channel|     Views|   Likes|Comments|Licensed|official_video|      Stream|    EnergyLiveness|most_playedon|
+----------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+-----------------+----------+--------+--------+--------+--------------+------------+------------------+-------------+
|       Nicky Jam|                   X|              Intimo|     album|       0.594| 0.749|  -5.298|      0.056|      0.0338|         0.00106|     0.3|  0.694|179.968|            2.8809|Nicky Jam x J. Ba...|       NickyJamTV|2133459242| 9883068|  262847|    True|          True| 865695837.0|2.4966666666666666|      Youtube|
|The Chainsmokers|Something Just Li...|Memories...Do Not...|     album|       0.617| 0.635|  -6.769|     0.0317|      0.0498|         1.44E-5|   0.164|  0.446|103.019|4.1193333333333335|The Chainsmokers ...| ChainsmokersVEVO|2118024518|10282557|  270446|    True|          True|2030825694.0|3.8719512195121952|      Youtube|
|        Coldplay|Something Just Li...|Memories...Do Not...|     album|       0.617| 0.635|  -6.769|     0.0317|      0.0498|         1.44E-5|   0.164|  0.446|103.019|4.1193333333333335|The Chainsmokers ...| ChainsmokersVEVO|2118018686|10282499|  270444|    True|          True|2030825694.0|3.8719512195121952|      Youtube|
|      Bruno Mars|  That's What I Like|           24K Magic|     album|       0.853|  0.56|  -4.961|     0.0406|       0.013|             0.0|  0.0944|   0.86|134.066|3.4448833333333333|Bruno Mars - That...|       Bruno Mars|2102232829|12567365|  378834|    True|          True|1562466168.0|5.9322033898305095|      Youtube|
|         Becky G|          Sin Pijama|          MALA SANTA|     album|       0.788| 0.745|  -4.417|     0.0448|       0.352|         4.56E-5|  0.0973|   0.79| 94.002|3.1693333333333333|Becky G, Natti Na...|       BeckyGVEVO|2086480901| 8624891|  366369|    True|          True| 710166109.0| 7.656731757451182|      Youtube|
|   Natti Natasha|          Sin Pijama|          MALA SANTA|     album|       0.788| 0.745|  -4.417|     0.0448|       0.352|         4.56E-5|  0.0973|   0.79| 94.002|3.1693333333333333|Becky G, Natti Na...|       BeckyGVEVO|2086480719| 8624889|  366369|    True|          True| 710166109.0| 7.656731757451182|      Youtube|
|  Jennifer Lopez|On The Floor - Ra...|        On The Floor|    single|       0.758| 0.686|  -6.346|     0.0792|      0.0848|         0.00127|   0.142|  0.444|130.007|           3.84845|Jennifer Lopez - ...|JenniferLopezVEVO|2062108307| 8740440|  440974|    True|          True| 370761679.0| 4.830985915492959|      Youtube|
|  Jennifer Lopez|        On The Floor|               Love?|     album|        0.73| 0.777|  -5.194|     0.0496|       0.105|         4.78E-4|  0.0691|  0.575|  130.0|4.7477833333333335|Jennifer Lopez - ...|JenniferLopezVEVO|2062108307| 8740440|  440974|    True|          True| 360804163.0|11.244573082489147|      Youtube|
|          Kimbra|Somebody That I U...|      Making Mirrors|     album|       0.864| 0.495|  -7.036|      0.037|       0.591|         1.33E-4|  0.0992|   0.72|129.062| 4.082883333333333|Gotye - Somebody ...|       gotyemusic|2057216266|14580703|  792989|    True|          True|1318267448.0|  4.98991935483871|      Youtube|
|           Gotye|Somebody That I U...|      Making Mirrors|     album|       0.864| 0.495|  -7.036|      0.037|       0.591|         1.33E-4|  0.0992|   0.72|129.062| 4.082883333333333|Gotye - Somebody ...|       gotyemusic|2057215604|14580661|  792986|    True|          True|1318267448.0|  4.98991935483871|      Youtube|
+----------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+-----------------+----------+--------+--------+--------+--------------+------------+------------------+-------------+
only showing top 10 rows

**>>> spdf.groupBy("Artist").sum("Likes").show()**

+--------------------+----------+
|              Artist|sum(Likes)|
+--------------------+----------+
|          Snoop Dogg|  16674468|
|      The Black Keys|   2564135|
|            Chinmayi|   1942656|
|          Eurythmics|  13980491|
|              *NSYNC|   4233423|
|      Jarabe De Palo|   2602323|
|     Johannes Brahms|    669558|
|              Pesado|    930529|
|        Elvis Crespo|   2366112|
|         Exaltasamba|   1102493|
|        Yann Tiersen|    757185|
|     Little Big Town|   2269364|
|    Parokya Ni Edgar|    265398|
|                 Guè|    182150|
|  Fabrizio Paterlini|     25098|
|              Grimes|   3622744|
|     Luther Vandross|   2058174|
|Mi Banda El Mexicano|    211941|
|Daryl Hall & John...|   6964996|
|Huey Lewis & The ...|   1001710|
+--------------------+----------+
only showing top 20 rows

**>>> spdf.groupBy("Artist").agg(sum("Likes").alias("Total Likes"),max("Likes").alias("Max Likes"),min("Likes").alias("Min Likes"),avg("Likes").alias("Average Likes")).show()**

+--------------------+-----------+---------+---------+-----------------+
|              Artist|Total Likes|Max Likes|Min Likes|    Average Likes|
+--------------------+-----------+---------+---------+-----------------+
|          Snoop Dogg|   16674468|  5635352|      373|        1667446.8|
|      The Black Keys|    2564135|   979766|    22736|         256413.5|
|            Chinmayi|    1942656|   651827|        0|         194265.6|
|          Eurythmics|   13980491|  6430665|       46|        1398049.1|
|              *NSYNC|    4233423|  1426156|     1089|         423342.3|
|      Jarabe De Palo|    2602323|  1008777|     5792|         260232.3|
|     Johannes Brahms|     669558|   324416|        0|          66955.8|
|              Pesado|     930529|   297218|      330|          93052.9|
|        Elvis Crespo|    2366112|  1411317|     1472|         236611.2|
|         Exaltasamba|    1102493|   318385|     6942|         110249.3|
|        Yann Tiersen|     757185|   510078|     1477|          75718.5|
|     Little Big Town|    2269364|   997028|      297|         226936.4|
|    Parokya Ni Edgar|     265398|    78865|      478|          26539.8|
|                 Guè|     182150|    90174|     7299|20238.88888888889|
|  Fabrizio Paterlini|      25098|    17172|       88|           2509.8|
|              Grimes|    3622744|   894306|    74638|         362274.4|
|     Luther Vandross|    2058174|   708493|    27620|         205817.4|
|Mi Banda El Mexicano|     211941|    60749|      144|          21194.1|
|Daryl Hall & John...|    6964996|  3482498|        0|         696499.6|
|Huey Lewis & The ...|    1001710|   100171|   100171|         100171.0|
+--------------------+-----------+---------+---------+-----------------+

**>>> spdf.groupBy("channel").agg(sum("Likes").alias("Total Likes"),max("Likes").alias("Max Likes"),min("Likes").alias("Min Likes"),avg("Likes").alias("Average Likes")).show()**

+--------------------+-----------+---------+---------+------------------+
|             channel|Total Likes|Max Likes|Min Likes|     Average Likes|
+--------------------+-----------+---------+---------+------------------+
|      ChannelCoverTV|      42620|    42620|    42620|           42620.0|
|      The Black Keys|    2541399|   979766|    27353| 282377.6666666667|
|   AndreaBocelliVEVO|    6528780|  1167184|    22126|          652878.0|
|            wilsalsa|        602|      301|      301|             301.0|
|            jalos012|     304203|   304203|   304203|          304203.0|
|    EUROPA Hörspiele|        605|       32|       12| 22.40740740740741|
|          changeting|      93730|    93730|    93730|           93730.0|
|        TURB0lovesTP|       7019|     7019|     7019|            7019.0|
|    LeonardCohenVEVO|    2404230|  1125139|    21658|         300528.75|
|    Pink & Grey Subs|       1004|     1004|     1004|            1004.0|
|     Alessandro R. C|      35158|    35158|    35158|           35158.0|
|          Hell 2Rock|       2846|     2846|     2846|            2846.0|
|Academy Of Ancien...|        543|      543|      543|             543.0|
| 1968) on The Ed ...|    2599566|  2599566|  2599566|         2599566.0|
|               TRIBL|     157066|   113964|    43102|           78533.0|
|     Buzz Darkmatter|        644|      644|      644|             644.0|
|    Madagascar2Music|      70434|    70434|    70434|           70434.0|
|         MYSTIC PIMP|      56162|    30315|      589|18720.666666666668|
|Damas Gratis - Topic|      30798|    30798|    30798|           30798.0|
|        Marco Santos|       2206|     2206|     2206|            2206.0|
+--------------------+-----------+---------+---------+------------------+


**>>> spdf.createOrReplaceTempView("spotify")**

**>>> spark.sql("select * from spotify").show()**

+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+----------+-------+--------+--------+--------------+------------+------------------+-------------+
|              Artist|               Track|               Album|Album_type|Danceability|Energy|Loudness|Speechiness|Acousticness|Instrumentalness|Liveness|Valence|  Tempo|      Duration_min|               Title|             Channel|     Views|  Likes|Comments|Licensed|official_video|      Stream|    EnergyLiveness|most_playedon|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+----------+-------+--------+--------+--------------+------------+------------------+-------------+
|            Gorillaz|      Feel Good Inc.|          Demon Days|     album|       0.818| 0.705|  -6.679|      0.177|     0.00836|         0.00233|   0.613|  0.772|138.559|3.7106666666666666|Gorillaz - Feel G...|            Gorillaz| 693555221|6220896|  169907|    True|          True|1040234854.0|1.1500815660685155|      Spotify|
|            Gorillaz|     Rhinestone Eyes|       Plastic Beach|     album|       0.676| 0.703|  -5.815|     0.0302|      0.0869|         6.87E-4|  0.0463|  0.852| 92.761|3.3362166666666666|Gorillaz - Rhines...|            Gorillaz|  72011645|1079128|   31003|    True|          True| 310083733.0|15.183585313174945|      Spotify|
|            Gorillaz|New Gold (feat. T...|New Gold (feat. T...|    single|       0.695| 0.923|   -3.93|     0.0522|      0.0425|          0.0469|   0.116|  0.551|108.014|3.5858333333333334|Gorillaz - New Go...|            Gorillaz|   8435055| 282142|    7399|    True|          True|  63063467.0| 7.956896551724138|      Spotify|
|            Gorillaz|  On Melancholy Hill|       Plastic Beach|     album|       0.689| 0.739|   -5.81|      0.026|     1.51E-5|           0.509|   0.064|  0.578|120.423|3.8977833333333334|Gorillaz - On Mel...|            Gorillaz| 211754952|1788577|   55229|    True|          True| 434663559.0|         11.546875|      Spotify|
|            Gorillaz|      Clint Eastwood|            Gorillaz|     album|       0.663| 0.694|  -8.627|      0.171|      0.0253|             0.0|  0.0698|  0.525|167.953|             5.682|Gorillaz - Clint ...|            Gorillaz| 618480958|6197318|  155930|    True|          True| 617259738.0|  9.94269340974212|      Youtube|
|            Gorillaz|                DARE|          Demon Days|     album|        0.76| 0.891|  -5.852|     0.0372|      0.0229|          0.0869|   0.298|  0.966|120.264| 4.083333333333333|Gorillaz - DARE (...|            Gorillaz| 259021161|1844658|   72008|    True|          True| 323850327.0|2.9899328859060406|      Spotify|
|            Gorillaz|New Gold (feat. T...|New Gold (feat. T...|    single|       0.716| 0.897|  -7.185|     0.0629|       0.012|           0.262|   0.325|  0.358| 127.03|4.5690333333333335|Gorillaz - New Go...|           Dom Dolla|    451996|  11686|     241|   False|          True|  10666154.0|              2.76|      Spotify|
|            Gorillaz|She's My Collar (...|     Humanz (Deluxe)|     album|       0.726| 0.815|  -5.886|     0.0313|     0.00799|           0.081|   0.112|  0.462|140.158|3.4926666666666666|Gorillaz - She's ...|          SalvaMuñox|   1010982|  17675|     260|   False|         False| 159605929.0|7.2767857142857135|      Spotify|
|            Gorillaz|Cracker Island (f...|Cracker Island (f...|    single|       0.741| 0.913|   -3.34|     0.0465|     0.00343|           0.103|   0.325|  0.643|120.012|            3.5625|Gorillaz - Cracke...|            Gorillaz|  24459820| 739527|   20296|    True|          True|  42671901.0| 2.809230769230769|      Spotify|
|            Gorillaz|         Dirty Harry|          Demon Days|     album|       0.625| 0.877|  -7.176|      0.162|      0.0315|          0.0811|   0.672|  0.865|192.296|3.8404333333333334|Gorillaz - Dirty ...|            Gorillaz| 154761056|1386920|   39240|    True|          True| 191074713.0|1.3050595238095237|      Spotify|
|Red Hot Chili Pep...|     Californication|Californication (...|     album|       0.592| 0.767|  -2.788|      0.027|      0.0021|         0.00165|   0.127|  0.328| 96.483|           5.49555|Red Hot Chili Pep...|Red Hot Chili Pep...|1018811259|4394471|  121452|    True|          True|1055738398.0| 6.039370078740157|      Spotify|
|Red Hot Chili Pep...|    Under the Bridge|Blood Sugar Sex M...|     album|       0.559| 0.345| -13.496|     0.0459|      0.0576|         1.05E-4|   0.141|  0.458| 84.581| 4.405116666666666|Red Hot Chili Pep...|Red Hot Chili Pep...| 246687714|1213572|   32761|    True|          True|1061750522.0|2.4468085106382977|      Spotify|
|Red Hot Chili Pep...|          Can't Stop|By the Way (Delux...|     album|       0.618| 0.938|  -3.442|     0.0456|      0.0179|             0.0|   0.167|  0.875| 91.455| 4.483333333333333|Red Hot Chili Pep...|Red Hot Chili Pep...| 336635759|1740224|   32573|    True|          True| 866464951.0| 5.616766467065868|      Spotify|
|Red Hot Chili Pep...|         Scar Tissue|Californication (...|     album|       0.595| 0.717|  -4.803|     0.0295|      0.0779|         0.00274|   0.108|  0.547| 88.969|           3.59845|Red Hot Chili Pep...|Red Hot Chili Pep...| 435121530|1890900|   37069|    True|          True| 613838674.0| 6.638888888888888|      Spotify|
|Red Hot Chili Pep...|           Otherside|Californication (...|     album|       0.458| 0.795|  -3.265|     0.0574|     0.00316|         2.02E-4|  0.0756|  0.513|123.229| 4.256216666666667|Red Hot Chili Pep...|Red Hot Chili Pep...| 673528656|3140356|   60091|    True|          True| 732774515.0|10.515873015873016|      Spotify|
|Red Hot Chili Pep...|       Snow (Hey Oh)|    Stadium Arcadium|     album|       0.427|   0.9|  -3.674|     0.0499|       0.116|         1.75E-5|   0.119|  0.599|104.655|5.5777833333333335|Red Hot Chili Pep...|Red Hot Chili Pep...| 320871237|1272266|   37004|    True|          True| 860722316.0| 7.563025210084034|      Spotify|
|Red Hot Chili Pep...|     Dani California|    Stadium Arcadium|     album|       0.556| 0.913|   -2.36|     0.0437|      0.0193|         8.59E-6|   0.346|   0.73| 96.184|4.7026666666666666|Red Hot Chili Pep...|Red Hot Chili Pep...| 324228662|1456622|   49461|    True|          True| 550067391.0|2.6387283236994223|      Spotify|
|Red Hot Chili Pep...|          By the Way|By the Way (Delux...|     album|       0.451|  0.97|  -4.938|      0.107|      0.0264|         0.00355|   0.102|  0.198|122.444|           3.61555|Red Hot Chili Pep...|Red Hot Chili Pep...| 179005296| 784717|   20084|    True|          True| 367485508.0| 9.509803921568627|      Spotify|
|Red Hot Chili Pep...|        Give It Away|Blood Sugar Sex M...|     album|       0.666| 0.936|  -9.919|     0.0476|     0.00244|           0.086|   0.153|  0.776| 91.577| 4.715116666666667|Red Hot Chili Pep...|Red Hot Chili Pep...|  86637926| 434837|   16029|    True|          True| 301947159.0|  6.11764705882353|      Spotify|
|Red Hot Chili Pep...|    Dark Necessities|         The Getaway|     album|         0.7| 0.742|  -6.777|     0.0716|      0.0722|          0.0199|    0.11|  0.197| 91.959| 5.033333333333333|Red Hot Chili Pep...|Red Hot Chili Pep...| 440037964|2094182|   56516|    True|          True| 385677873.0| 6.745454545454545|      Youtube|
+--------------------+--------------------+--------------------+----------+------------+------+--------+-----------+------------+----------------+--------+-------+-------+------------------+--------------------+--------------------+----------+-------+--------+--------+--------------+------------+------------------+-------------+
only showing top 20 rows


**>>> spark.sql("select artist, sum(Likes) from spotify group by artist").show()**

+--------------------+----------+
|              artist|sum(Likes)|
+--------------------+----------+
|          Snoop Dogg|  16674468|
|      The Black Keys|   2564135|
|            Chinmayi|   1942656|
|          Eurythmics|  13980491|
|              *NSYNC|   4233423|
|      Jarabe De Palo|   2602323|
|     Johannes Brahms|    669558|
|              Pesado|    930529|
|        Elvis Crespo|   2366112|
|         Exaltasamba|   1102493|
|        Yann Tiersen|    757185|
|     Little Big Town|   2269364|
|    Parokya Ni Edgar|    265398|
|                 Guè|    182150|
|  Fabrizio Paterlini|     25098|
|              Grimes|   3622744|
|     Luther Vandross|   2058174|
|Mi Banda El Mexicano|    211941|
|Daryl Hall & John...|   6964996|
|Huey Lewis & The ...|   1001710|
+--------------------+----------+
only showing top 20 rows

**>>> spdf.write.mode("overwrite").save("/output/")**

**>>> spdf.getNumPartitions()**

**>>> spdf.rdd.getNumPartitions()**

2

**>>> spDF = spdf.repartition(1)**

**>>> spDF.write.mode("overwrite").save("/output/new/")**
