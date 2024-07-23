import 'package:flutter/material.dart';

class SonucEkrani extends StatefulWidget {

  bool sonuc;

  SonucEkrani({required this.sonuc});

  @override
  State<SonucEkrani> createState() => _SonucEkraniState();
}

class _SonucEkraniState extends State<SonucEkrani> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Sonuc Ekrani"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            widget.sonuc ? Image.asset("lib/Bolum12/Resimler/mutlu_resim.png") : Image.asset("lib/Bolum12/Resimler/uzgun_resim.png") ,
            Text(widget.sonuc ? "Kazandiniz" : "Kaybettiniz",style: TextStyle(color: Colors.black54,fontSize: 36),),
            SizedBox(
              width: 200,
              height: 50,
              child: ElevatedButton(
                child: Text("Tekrar Dene"),
                style: ElevatedButton.styleFrom(backgroundColor: Colors.blue,foregroundColor: Colors.white),
                onPressed: (){
                  Navigator.pop(context);
                },
              ),
            ),
          ],
        ),
      ),

    );;
  }
}
