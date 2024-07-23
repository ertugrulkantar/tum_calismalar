import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum14/19-DetaySayfa.dart';

import 'Resimler/19-Yemekler.dart';

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

  Future<List<Yemekler>> yemekleriGetir() async{
    var yemekListesi=<Yemekler>[];
    var y1=Yemekler(1, "Köfte", "kofte.png", 15.99);
    var y2=Yemekler(2, "Ayran", "ayran.png", 2.0);
    var y3=Yemekler(3, "Fanta", "fanta.png", 3.0);
    var y4=Yemekler(4, "Makarna", "makarna.png", 14.99);
    var y5=Yemekler(5, "Kadayıf", "kadayif.png", 8.50);
    var y6=Yemekler(6, "Baklava", "baklava.png", 15.99);

    yemekListesi.add(y1);
    yemekListesi.add(y2);
    yemekListesi.add(y3);
    yemekListesi.add(y4);
    yemekListesi.add(y5);
    yemekListesi.add(y6);

    return yemekListesi;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.orange,
        title: Text("Yemek"),
      ),
      body: FutureBuilder<List<Yemekler>>(
        future: yemekleriGetir(),
        builder: (context,snapshot){
          if(snapshot.hasData){
            var yemekListesi=snapshot.data;

            return ListView.builder(
              itemCount: yemekListesi!.length,
              itemBuilder: (context,indeks){
                var yemek=yemekListesi[indeks];
                
                return GestureDetector(
                  onTap: (){
                    Navigator.push(context,MaterialPageRoute(builder:(context)=>DetaySayfa(yemek: yemek,)));
                  },
                  child: Card(
                    child: Row(
                      children: [
                        SizedBox(width: 150,height: 150, child: Image.asset("lib/Bolum14/Resimler/${yemek.yemek_resim_adi}")),
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(yemek.yemek_adi,style: TextStyle(fontSize: 25),),
                            SizedBox(height: 50,),
                            Text("${yemek.yemek_fiyat} \u{20BA}",style: TextStyle(fontSize: 20,color: Colors.blue),),
                          ],
                        ),
                        Spacer(),
                        Icon(Icons.keyboard_arrow_right),
                      ],
                    ),
                  ),
                );
              },
            );
          }
          else{
            return Center();
          }
        },
      ),

    );
  }
}
