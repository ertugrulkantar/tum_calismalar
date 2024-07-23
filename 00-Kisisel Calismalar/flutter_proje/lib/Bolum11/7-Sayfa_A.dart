import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum11/7-Kisiler.dart';
import 'package:flutter_proje/Bolum11/7-Sayfa_B.dart';

class SayfaA_7 extends StatefulWidget {

  //## 1.YOL ##
  //String? isim;
  //int? yas;
  //double? boy;
  //bool? bekarMi;
  //  SayfaA_7({required this.isim,required this.yas,required this.boy,required this.bekarMi});
  //## 1.YOL ##

  //## 2.YOL ##
  Kisiler kisi;
  SayfaA_7({required this.kisi});
  //## 2.YOL ##


  @override
  State<SayfaA_7> createState() => _SayfaA_7State();
}

class _SayfaA_7State extends State<SayfaA_7> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Sayfa A"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text("Sayfa B'ye Git"),
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context) => SayfaB_7()));
              },
            ),
            //Text("İsim: ${widget.isim}"),
            //Text("Yaş: ${widget.yas}"),
            //Text("Boy: ${widget.boy}"),
            //Text("Bekar Mı: ${widget.bekarMi}"),
            Text("İsim: ${widget.kisi.isim}"),
            Text("Yaş: ${widget.kisi.yas}"),
            Text("Boy: ${widget.kisi.boy}"),
            Text("Bekar Mı: ${widget.kisi.bekarMi}"),
          ],
        ),
      ),

    );
  }
}
