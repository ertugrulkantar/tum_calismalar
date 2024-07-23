import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/31-FilmlerSayfa.dart';
import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/31-Kategoriler.dart';
import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/KategorilerCevap.dart';

import 'package:http/http.dart' as http;
import 'dart:convert';

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
      home:  Anasayfa(),
    );
  }
}

class Anasayfa extends StatefulWidget {


  @override
  State<Anasayfa> createState() => _AnasayfaState();
}

class _AnasayfaState extends State<Anasayfa> {

  List<Kategoriler> parseKategorilerCevap(String cevap){
    return KategorilerCevap.fromJson(json.decode(cevap)).kategorilerNesnesi;
  }

  Future<List<Kategoriler>> tumKategorileriGoster() async{
    var url=Uri.parse("http://kasimadalan.pe.hu/filmler/tum_kategoriler.php");
    var cevap= await http.get(url);
    return parseKategorilerCevap(cevap.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Kategoriler"),
      ),
      body: FutureBuilder<List<Kategoriler>>(
        future: tumKategorileriGoster(),
        builder: (context,snapshot){
          if(snapshot.hasData){
            var kategoriListesi=snapshot.data;
            return ListView.builder(
              itemCount: kategoriListesi!.length,
              itemBuilder: (context,indeks){
                var kategori=kategoriListesi[indeks];
                return GestureDetector(
                  onTap: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>FilmlerSayfa(kategori: kategori,)));
                  },
                  child: Card(
                    child: SizedBox( height: 50,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(kategori.kategori_ad),
                        ],
                      ),
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
