import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home:  MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {


  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    
    var ekranBilgisi=MediaQuery.of(context);
    final double ekranYuksekligi=ekranBilgisi.size.height;
    final double ekranGenisligi=ekranBilgisi.size.width;
    
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.orange,
        title: Text("Yemek Tarifi"),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            SizedBox(
                width: ekranGenisligi,
                child: Image.asset("lib/Bolum10/Resimler/yemekresim.jpeg")),
            Row(
              children: [
                Expanded(
                  child: SizedBox(
                    height: ekranGenisligi/8,
                    child: TextButton(child: Yazi("Begen", ekranGenisligi/25)
                      ,onPressed: (){
                        print("Begenildi");
                      },
                    style: TextButton.styleFrom(
                      backgroundColor: Colors.orange,
                      foregroundColor: Colors.black,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(0),
                        )
                    ),),
                  ),
                ),
                Expanded(
                  child: SizedBox(
                    height: ekranGenisligi/8,
                    child: TextButton(child: Yazi("Yorum Yap", ekranGenisligi/25)
                      ,onPressed: (){
                        print("Yorum Yapildi");
                      },
                      style: TextButton.styleFrom(
                        backgroundColor: Colors.deepOrangeAccent,
                        foregroundColor: Colors.black,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(0),
                        )
                      ),),
                  ),
                ),
              ],
            ),
            Padding(
              padding:  EdgeInsets.all(ekranYuksekligi/100),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Köfte", style: TextStyle(
                    color: Colors.deepOrangeAccent,
                    fontWeight: FontWeight.bold,
                    fontSize: ekranGenisligi/20,
                  ),
                  ),
                  Row(
                    children: [
                      Yazi("Izgara Üzerinde Pişirime Uygun", ekranGenisligi/25),
                      Spacer(),
                      Yazi("8 Ağustos", ekranGenisligi/25)
                    ],
                  ),
                ],
              ),
            ),
            Padding(
              padding:  EdgeInsets.all(ekranYuksekligi/100),
              child: Yazi("Köfte harcını hazırlamak için, soğanları rendeleyin"
                  " ve maydanozları ince ince kıyın. İsterseniz,"
                  " bir diş sarımsak da ekleyebilirsiniz. Kıymaya"
                  " soğanı ekleyin. Köfte harcının üzerini streç"
                  " filmle kapatarak yarım saat buzdolabında dinlendirin."
                  "Ardından harçtan ceviz büyüklüğünde parçalar koparıp yuvarlayın."
                  "1 cm olacak şekilde üzerine basarak yassılaştırın.", ekranGenisligi/25),
            )
          ],
        ),
      ),

    );
  }
}

class  Yazi extends StatelessWidget {
  String icerik;
  double yaziBoyut;

  Yazi(this.icerik, this.yaziBoyut);

  @override
  Widget build(BuildContext context) {
    return Text(icerik, style: TextStyle(fontSize:yaziBoyut ),);
  }
}
