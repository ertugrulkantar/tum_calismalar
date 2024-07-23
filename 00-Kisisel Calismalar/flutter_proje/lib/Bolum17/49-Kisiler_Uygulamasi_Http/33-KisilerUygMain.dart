import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/49-Kisiler_Uygulamasi_Http/33-KisiDetaySayfa.dart';
import 'package:flutter_proje/Bolum17/49-Kisiler_Uygulamasi_Http/33-KisiKayitSayfa.dart';
import 'package:flutter_proje/Bolum17/49-Kisiler_Uygulamasi_Http/33-Kisiler.dart';
import 'package:flutter_proje/Bolum17/49-Kisiler_Uygulamasi_Http/KisilerCevap.dart';

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

  bool aramaYapiliyorMu=false;
  String aramaKelimesi="";

  List<Kisiler> parseKisilerCevap(String cevap){
    return KisilerCevap.fromJson(json.decode(cevap)).kisilerListesi;
  }

  Future<List<Kisiler>> tumKisileriGoster() async{
    var url=Uri.parse("http://kasimadalan.pe.hu/kisiler/tum_kisiler.php");
    var cevap=await http.get(url);
    return parseKisilerCevap(cevap.body);
  }

  Future<List<Kisiler>> aramaYap(String aramaKelimesi) async{
    var url=Uri.parse("http://kasimadalan.pe.hu/kisiler/tum_kisiler_arama.php");
    var veri={"kisi_ad":aramaKelimesi};
    var cevap=await http.post(url,body: veri);
    return parseKisilerCevap(cevap.body);
  }

  Future<void> sil(int kisi_id) async{
    var url=Uri.parse("http://kasimadalan.pe.hu/kisiler/delete_kisiler.php");
    var veri={"kisi_id":kisi_id.toString()};
    var cevap=await http.post(url,body: veri);
    print("Silme Cevap:${cevap.body}");
    setState(() {
    });
  }

  Future<bool> uygulamayiKapat() async{
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
        title: aramaYapiliyorMu ?
            TextField(
              decoration: InputDecoration(hintText: "Arama icin bir sey yazin."),
              onChanged: (aramaSonucu){
                print("Arama sonucu : $aramaSonucu");
                setState(() {
                  aramaKelimesi=aramaSonucu;
                });
              },
            )
            : Text("Kisiler Uygulamasi"),
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
      body: WillPopScope(
        onWillPop: uygulamayiKapat,
        child: FutureBuilder<List<Kisiler>>(
          future: aramaYapiliyorMu? aramaYap(aramaKelimesi) : tumKisileriGoster(),
          builder: (context,snapshot) {
            if(snapshot.hasData){
              var kisilerListesi=snapshot.data;
              return ListView.builder(
                itemCount: kisilerListesi!.length,
                itemBuilder: (context,indeks){
                  var kisi=kisilerListesi[indeks];
                  return GestureDetector(
                    onTap: (){
                      Navigator.push(context,MaterialPageRoute(builder: (context)=>KisiDetaySayfa(kisi: kisi,)));
                    },
                    child: Card(
                      child: SizedBox(height: 50,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Text(kisi.kisi_ad,style: TextStyle(fontWeight: FontWeight.bold),),
                            Text(kisi.kisi_tel),
                            IconButton(
                              icon: Icon(Icons.delete,color: Colors.black54,),
                              onPressed: (){
                                sil(int.parse(kisi.kisi_id));
                              },
                            ),
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
          Navigator.push(context,MaterialPageRoute(builder: (context)=>KisiKayitSayfa()));
        },
        tooltip: "Kisi Ekle",
        child: Icon(Icons.add),
      ),
    );
  }
}
