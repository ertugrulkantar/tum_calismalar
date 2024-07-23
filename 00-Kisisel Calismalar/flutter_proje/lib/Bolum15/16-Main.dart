import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/13-Kisiler.dart';
import 'package:flutter_proje/Bolum15/16-Kisilerdao.dart';

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

  Future<void> kisileriGoster() async{
    var kdao=Kisilerdao();
    var liste=await kdao.tumKisiler();

    for(Kisiler k in liste){
      print("****************");
      print("Kisi ad: ${k.kisi_ad}");
      print("Kisi id: ${k.kisi_id}");
      print("Kisi yas: ${k.kisi_yas}");

    }
  }

  Future<void> ekle() async{
    await Kisilerdao().kisiEkle("Ece", 57);
  }

  Future<void> sil() async{
    await Kisilerdao().kisiSil(3);
  }

  Future<void> guncelle() async{
    await Kisilerdao().kisiGuncelle(4, "Yeni isim", 99);
  }

  Future<void> kayitKontrol() async{
    int sonuc=await Kisilerdao().kayitKontrol("Yeni isim");
    print("Veritabanindaki Yeni isim sayisi:$sonuc");
  }

  Future<void> getir() async{ //21-Bir tane kayit getirme
    var kisi=await Kisilerdao().kisiGetir(4);


      print("****************");
      print("Kisi ad: ${kisi.kisi_ad}");
      print("Kisi id: ${kisi.kisi_id}");
      print("Kisi yas: ${kisi.kisi_yas}");
  }

  Future<void> aramaYap() async{  //22-Arama islemi
    var liste=await Kisilerdao().kisiArama("zeynep");

    for(Kisiler k in liste){
      print("****************");
      print("Kisi ad: ${k.kisi_ad}");
      print("Kisi id: ${k.kisi_id}");
      print("Kisi yas: ${k.kisi_yas}");
    }
  }

  Future<void> rastgele() async{  //23-Rastgele ve sinirli
    var liste=await Kisilerdao().rastgele2kisiGetir();

    for(Kisiler k in liste){
      print("****************");
      print("Kisi ad: ${k.kisi_ad}");
      print("Kisi id: ${k.kisi_id}");
      print("Kisi yas: ${k.kisi_yas}");
    }
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    //ekle();
    //sil();
    //guncelle();
    //kayitKontrol();
    //getir();
    //aramaYap();
    rastgele();
    //kisileriGoster();
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
