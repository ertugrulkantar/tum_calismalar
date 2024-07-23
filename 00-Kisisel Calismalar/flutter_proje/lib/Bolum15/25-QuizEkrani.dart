import 'dart:collection';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/25-Bayraklar.dart';
import 'package:flutter_proje/Bolum15/25-Bayraklardao.dart';
import 'package:flutter_proje/Bolum15/25-SonucEkrani.dart';
import 'dart:core';

class QuizEkrani extends StatefulWidget {
  const QuizEkrani({super.key});

  @override
  State<QuizEkrani> createState() => _QuizEkraniState();
}

class _QuizEkraniState extends State<QuizEkrani> {

  var sorular=<Bayraklar>[];
  var yanlisSecenekler=<Bayraklar>[];
  late Bayraklar dogruSoru;
  var tumSecenekler=HashSet<Bayraklar>();

  int soruSayac=0;
  int dogruSayac=0;
  int yanlisSayac=0;

  String bayrakResimAdi="placeholder.png";
  String butonAyazi="";
  String butonByazi="";
  String butonCyazi="";
  String butonDyazi="";

  @override
  void initState() {
    super.initState();
    sorulariAl();
  }

  Future<void> sorulariAl() async{
    sorular=await Bayraklardao().rastgele5Getir();
    soruYukle();
  }

  Future<void> soruYukle() async{
    dogruSoru=sorular[soruSayac];

    bayrakResimAdi=dogruSoru.bayrak_resim;

    yanlisSecenekler=await Bayraklardao().rastgele3YanlisGetir(dogruSoru.bayrak_id);
    tumSecenekler.clear();
    tumSecenekler.add(dogruSoru);
    tumSecenekler.add(yanlisSecenekler[0]);
    tumSecenekler.add(yanlisSecenekler[1]);
    tumSecenekler.add(yanlisSecenekler[2]);

    butonAyazi=tumSecenekler.elementAt(0).bayrak_ad;
    butonByazi=tumSecenekler.elementAt(1).bayrak_ad;
    butonCyazi=tumSecenekler.elementAt(2).bayrak_ad;
    butonDyazi=tumSecenekler.elementAt(3).bayrak_ad;

    setState(() {
    });
  }

  void soruSayacKontrol(){
    soruSayac++;
    if(soruSayac!=5){
      soruYukle();
    }
    else{
      Navigator.pushReplacement(context, MaterialPageRoute(builder: (context)=> SonucEkrani(dogruSayisi: dogruSayac,)));
    }
  }

  void dogruKontrol(String butonYazi){
    if(dogruSoru.bayrak_ad==butonYazi){
      dogruSayac++;
    }
    else{
      yanlisSayac++;
    }

  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Quiz Ekrani"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Text("Dogru : $dogruSayac",style: TextStyle(fontSize: 18),),
                Text("Yanlis : $yanlisSayac",style: TextStyle(fontSize: 18),),
              ],
            ),
            soruSayac!=5 ? Text("${soruSayac+1}. Soru",style: TextStyle(fontSize: 30),) : Text("5. Soru",style: TextStyle(fontSize: 30),) ,
            Image.asset("lib/Bolum15/resimler/$bayrakResimAdi"),
            SizedBox( width: 250, height: 50,
              child: ElevatedButton(
                child: Text(butonAyazi),
                onPressed: (){
                  dogruKontrol(butonAyazi);
                  soruSayacKontrol();
                },
              ),
            ),
            SizedBox( width: 250, height: 50,
              child: ElevatedButton(
                child: Text(butonByazi),
                onPressed: (){
                  dogruKontrol(butonByazi);
                  soruSayacKontrol();
                },
              ),
            ),
            SizedBox( width: 250, height: 50,
              child: ElevatedButton(
                child: Text(butonCyazi),
                onPressed: (){
                  dogruKontrol(butonCyazi);
                  soruSayacKontrol();
                },
              ),
            ),
            SizedBox( width: 250, height: 50,
              child: ElevatedButton(
                child: Text(butonDyazi),
                onPressed: (){
                  dogruKontrol(butonDyazi);
                  soruSayacKontrol();
                },
              ),
            ),
          ],
        ),
      ),

    );
  }
}
