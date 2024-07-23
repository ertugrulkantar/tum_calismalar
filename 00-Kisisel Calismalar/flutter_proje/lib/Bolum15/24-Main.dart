import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/24-Filmler.dart';
import 'package:flutter_proje/Bolum15/24-Flimlerdao.dart';

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

  Future<void> goster() async{
    var liste=await Filmlerdao().tumFilmler();

    for(Filmler f in liste){
      print("*************");
      print("Film id: ${f.film_id}");
      print("Film ad: ${f.film_ad}");
      print("Film resim: ${f.film_resim}");
      print("Film kategori: ${f.kategori.kategori_ad}");
      print("Film yonetmen: ${f.yonetmen.yonetmen_ad}");
    }
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    goster();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Baslik"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [

          ],
        ),
      ),

    );
  }
}
