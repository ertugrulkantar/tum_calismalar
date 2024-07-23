import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/27-DetaySayfa.dart';
import 'package:flutter_proje/Bolum15/27-Kelimeler.dart';

import '27-Kelimelerdao.dart';

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

  bool aramaYapiliyorMu=false;
  String aramaKelimesi="";

  Future<List<Kelimeler>> tumKelimelerGoster() async{
    var kelimelerListesi=await Kelimelerdao().tumKelimeler();
    return kelimelerListesi;
  }

  Future<List<Kelimeler>> aramaYap(String aramaKelimesi) async{
    var kelimelerListesi=await Kelimelerdao().kelimelerAra(aramaKelimesi);
    return kelimelerListesi;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: aramaYapiliyorMu ?
            TextField(
              decoration: InputDecoration(hintText: "Arama icin bir sey yazin"),
              onChanged: (aramaSonucu){
                print("Arama sonucu : $aramaSonucu");
                setState(() {
                  aramaKelimesi=aramaSonucu;
                });
              },
            )
            : Text("Sozluk Uygulamasi"),
        actions: [
          aramaYapiliyorMu ?
          IconButton(
          icon: Icon(Icons.cancel),
          onPressed: (){
            setState(() {
              aramaYapiliyorMu=false;
              aramaKelimesi="";
            });
          },
        )
          : IconButton(
            icon: Icon(Icons.search),
            onPressed: (){
              setState(() {
                aramaYapiliyorMu=true;
              });
            },
          ),
        ],
      ),
      body: FutureBuilder<List<Kelimeler>>(
        future: aramaYapiliyorMu ? aramaYap(aramaKelimesi) :  tumKelimelerGoster(),
        builder: (context,snapshot) {
          if(snapshot.hasData){
            var kelimelerListesi=snapshot.data;
            return ListView.builder(
              itemCount: kelimelerListesi!.length,
              itemBuilder: (context,indeks){
                var kelime=kelimelerListesi[indeks];
                return GestureDetector(
                  onTap: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>DetaySayfa(kelime: kelime,)));
                  },
                  child: SizedBox(height: 50,
                    child: Card(
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          Text(kelime.ingilizce,style: TextStyle(fontWeight: FontWeight.bold),),
                          Text(kelime.turkce),
                        ],
                      ),
                    ),
                  ),
                );
              } ,
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
