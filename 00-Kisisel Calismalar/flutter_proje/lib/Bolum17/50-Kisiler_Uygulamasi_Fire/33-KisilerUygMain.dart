import 'dart:io';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/50-Kisiler_Uygulamasi_Fire/33-KisiDetaySayfa.dart';
import 'package:flutter_proje/Bolum17/50-Kisiler_Uygulamasi_Fire/33-KisiKayitSayfa.dart';
import 'package:flutter_proje/Bolum17/50-Kisiler_Uygulamasi_Fire/33-Kisiler.dart';


Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
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

  var refKisiler=FirebaseDatabase.instance.ref().child("kisiler");

  Future<void> sil(String kisi_id) async{
    refKisiler.child(kisi_id).remove();
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
        child: StreamBuilder<DatabaseEvent>(
          stream: refKisiler.onValue,
          builder: (context,event) {
            if(event.hasData){
              var kisilerListesi=<Kisiler>[];
              var gelenDegerler=event.data!.snapshot.value as dynamic;
              if(gelenDegerler!=null){
                gelenDegerler.forEach((key,nesne){
                  var gelenKisi=Kisiler.fromJson(key, nesne);
                  if(aramaYapiliyorMu){
                    if(gelenKisi.kisi_ad.contains(aramaKelimesi)){
                      kisilerListesi.add(gelenKisi);
                    }
                  }
                  else{
                    kisilerListesi.add(gelenKisi);

                  }
                });
              }
              return ListView.builder(
                itemCount: kisilerListesi.length,
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
                                sil(kisi.kisi_id);
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
