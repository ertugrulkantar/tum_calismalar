import 'package:flutter/material.dart';

class SonucEkrani extends StatefulWidget {
  int dogruSayisi;

  SonucEkrani({required this.dogruSayisi});



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
            Text("${widget.dogruSayisi} DOGRU ${5-widget.dogruSayisi} YANLIS",style: TextStyle(fontSize: 30),),
            Text("%${(widget.dogruSayisi*100)~/5} BASARI",style: TextStyle(fontSize: 30,color: Colors.pink),),
            SizedBox( width: 250, height: 50,
              child: ElevatedButton(
                child: Text("TEKRAR DENE"),
                onPressed: (){
                  Navigator.pop(context);
                },
              ),
            ),
          ],

        ),
      ),

    );
  }
}
