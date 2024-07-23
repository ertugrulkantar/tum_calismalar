import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/45-Notlar_Uygulamasi_Http/29-NotDetaySayfa.dart';
import 'package:flutter_proje/Bolum17/45-Notlar_Uygulamasi_Http/29-NotKayitSayfa.dart';
import 'package:flutter_proje/Bolum17/45-Notlar_Uygulamasi_Http/29-Notlar.dart';
import 'package:flutter_proje/Bolum17/45-Notlar_Uygulamasi_Http/NotlarCevap.dart';

import 'dart:convert';
import 'package:http/http.dart' as http;

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

  List<Notlar> parseNotlarCevap(String cevap){
    print("XXX ${NotlarCevap.fromJson(json.decode(cevap)).notlarListesi}");
    return NotlarCevap.fromJson(json.decode(cevap)).notlarListesi;
  }

  Future<List<Notlar>> tumNotlariGoster() async {
    var url=Uri.parse("http://kasimadalan.pe.hu/notlar/tum_notlar.php");
    var cevap=await http.get(url);
    return parseNotlarCevap(cevap.body);
  }

  Future<bool> uygulamayiKapat() async {
    await exit(0);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: (){
            uygulamayiKapat();
          },
        ),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("Notlar Uygulamasi",style: TextStyle(color: Colors.white,fontSize: 16),),
            FutureBuilder(
              future: tumNotlariGoster(),
              builder: (context,snapshot){
                if(snapshot.hasData){
                  var notlarListesi=snapshot.data;
                  double ortalama=0.0;
                  if(!notlarListesi!.isEmpty){
                    double toplam=0.0;

                    for(var n in notlarListesi){
                      toplam=toplam+(int.parse(n.not1)+int.parse(n.not2))/2;
                    }
                    ortalama=toplam/notlarListesi.length;
                  }

                  return Text("Ortalama : ${ortalama.toInt()}",style: TextStyle(color: Colors.white,fontSize: 14,));
                }
                else{
                  return Text("Ortalama : 0",style: TextStyle(color: Colors.white,fontSize: 14,));
                }
              },
            ),
          ],
        ),
      ),
      body: WillPopScope(
        onWillPop: uygulamayiKapat,
        child: FutureBuilder<List<Notlar>>(
          future: tumNotlariGoster(),
          builder: (context,snapshot){
            if(snapshot.hasData){
              var notlarListesi=snapshot.data;
              return ListView.builder(
                itemCount: notlarListesi!.length,
                itemBuilder: (context,indeks){
                  var not=notlarListesi[indeks];
                  return GestureDetector(
                    onTap: (){
                      Navigator.push(context, MaterialPageRoute(builder: (context)=> NotDetaySayfa(not: not,)));
                    },
                    child: Card(
                      child: SizedBox( height: 50,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Text(not.ders_adi,style: TextStyle(fontWeight: FontWeight.bold),),
                            Text(not.not1.toString()),
                            Text(not.not2.toString()),
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
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: (){
          Navigator.push(context, MaterialPageRoute(builder: (context)=> NotKayitSayfa()));
        } ,
        tooltip: "Not Ekle",
        child: Icon(Icons.add),
      ),
    );
  }
}
