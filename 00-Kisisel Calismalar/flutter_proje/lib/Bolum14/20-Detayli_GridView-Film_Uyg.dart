import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum14/Resimler/20-DetaySayfa.dart';

import '20-Filmler.dart';

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

  Future<List<Filmler>> filmleriGetir() async {
    var filmlerListesi=<Filmler>[];

    var f1=Filmler(1, "Anadoluda", "anadoluda.png", 15.99);
    var f2=Filmler(2, "Django", "django.png", 9.99);
    var f3=Filmler(3, "Inception", "inception.png", 7.99);
    var f4=Filmler(4, "Interstellar", "interstellar.png", 21.99);
    var f5=Filmler(5, "The Hateful Eight", "thehatefuleight.png", 5.99);
    var f6=Filmler(6, "The Pianist", "thepianist.png", 17.99);

    filmlerListesi.add(f1);
    filmlerListesi.add(f2);
    filmlerListesi.add(f3);
    filmlerListesi.add(f4);
    filmlerListesi.add(f5);
    filmlerListesi.add(f6);

    return filmlerListesi;
}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.deepPurple,
        title: Text("Filmler"),
      ),
      body: FutureBuilder<List<Filmler>>(
        future: filmleriGetir(),
        builder: (context,snapshot){
          if(snapshot.hasData){
            var filmlerListesi=snapshot.data;

            return GridView.builder(
              itemCount: filmlerListesi!.length,
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 2/3.5,
              ),
              itemBuilder: (context,indeks){
                var film=filmlerListesi[indeks];
                return GestureDetector(
                  onTap: (){
                    Navigator.push(context,MaterialPageRoute(builder: (context)=>DetaySayfa(film)));
                  },
                  child: Card(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly ,
                      children: [
                        Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: Image.asset("lib/Bolum14/Resimler/${film.film_resim_adi}"),
                        ),
                        Text(film.film_adi,style: TextStyle(fontSize: 16,fontWeight: FontWeight.bold),),
                        Text("${film.film_fiyat} \u{20BA}",style: TextStyle(fontSize: 16,)),
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
