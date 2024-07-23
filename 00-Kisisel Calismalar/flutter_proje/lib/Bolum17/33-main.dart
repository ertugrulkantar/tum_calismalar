import 'dart:collection';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/33-Kisiler.dart';

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
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var refKisiler = FirebaseDatabase.instance.ref().child("kisiler_tablo");

  Future<void> kisiEkle() async{
    var bilgi=HashMap<String,dynamic>();
    bilgi["kisi_ad"]="Zeynep";
    bilgi["kisi_yas"]=10;
    refKisiler.push().set(bilgi);
  }

  Future<void> kisiSil() async{   //34
    refKisiler.child("-NlcM2sGVlGc1hVcOGax").remove();
  }

  Future<void> kisiGuncelle() async{
    var guncelbilgi=HashMap<String,dynamic>();
    guncelbilgi["kisi_ad"]="ert";
    guncelbilgi["kisi_yas"]=10;
    refKisiler.child("-NlcMHlE3Ta5gdv5o8AQ").update(guncelbilgi);
  }

  Future<void> tumKisiler() async{  //37
    refKisiler.onValue.listen((event) {
      var gelenDegerler=event.snapshot.value as dynamic;
      if(gelenDegerler!=null){
        gelenDegerler.forEach((key,nesne){
          var gelenKisi=Kisiler.fromJson(nesne);
          print("***********");
          print("Kisi key : $key");
          print("Kisi ad : ${gelenKisi.kisi_ad}");
          print("Kisi yas : ${gelenKisi.kisi_yas}");
        });
      }
    });
  }

  Future<void> tumKisilerOnce() async{  //38
    refKisiler.once().then((value) {
      var gelenDegerler=value.snapshot.value as dynamic;
      if(gelenDegerler!=null){
        gelenDegerler.forEach((key,nesne){
          var gelenKisi=Kisiler.fromJson(nesne);
          print("***********");
          print("Kisi key : $key");
          print("Kisi ad : ${gelenKisi.kisi_ad}");
          print("Kisi yas : ${gelenKisi.kisi_yas}");
        });
      }
    });
  }

  Future<void> esitlikArama() async{  //39

    var sorgu=refKisiler.orderByChild("kisi_ad").equalTo("Ece");

    sorgu.onValue.listen((event) {
      var gelenDegerler=event.snapshot.value as dynamic;
      if(gelenDegerler!=null){
        gelenDegerler.forEach((key,nesne){
          var gelenKisi=Kisiler.fromJson(nesne);
          print("***********");
          print("Kisi key : $key");
          print("Kisi ad : ${gelenKisi.kisi_ad}");
          print("Kisi yas : ${gelenKisi.kisi_yas}");
        });
      }
    });
  }

  Future<void> limitliVeri() async{  //39

    var sorgu=refKisiler.limitToFirst(2);
    //var sorgu=refKisiler.limitToLast(2);

    sorgu.onValue.listen((event) {
      var gelenDegerler=event.snapshot.value as dynamic;
      if(gelenDegerler!=null){
        gelenDegerler.forEach((key,nesne){
          var gelenKisi=Kisiler.fromJson(nesne);
          print("***********");
          print("Kisi key : $key");
          print("Kisi ad : ${gelenKisi.kisi_ad}");
          print("Kisi yas : ${gelenKisi.kisi_yas}");
        });
      }
    });
  }

  Future<void> degerAraligi() async{  //39

    var sorgu=refKisiler.orderByChild("kisi_yas").startAt(1).endAt(100);
    //var sorgu=refKisiler.limitToLast(2);

    sorgu.onValue.listen((event) {
      var gelenDegerler=event.snapshot.value as dynamic;
      if(gelenDegerler!=null){
        gelenDegerler.forEach((key,nesne){
          var gelenKisi=Kisiler.fromJson(nesne);
          print("***********");
          print("Kisi key : $key");
          print("Kisi ad : ${gelenKisi.kisi_ad}");
          print("Kisi yas : ${gelenKisi.kisi_yas}");
        });
      }
    });
  }

  @override
  void initState() {
    super.initState();
    //kisiEkle();
    //kisiSil();
    //kisiGuncelle();
    //tumKisiler();
    //tumKisilerOnce();
    //esitlikArama();
    //limitliVeri();
    degerAraligi();
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
          children: [],
        ),
      ),
    );
  }
}