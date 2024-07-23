import 'dart:math';

import 'package:flutter/material.dart';

import '20-Sonuc_Ekrani.dart';

class TahminEkrani extends StatefulWidget {
  const TahminEkrani({super.key});

  @override
  State<TahminEkrani> createState() => _TahminEkraniState();
}

class _TahminEkraniState extends State<TahminEkrani> {

  var tfTahmin=TextEditingController();
  int rastgeleSayi=0;
  int kalanHak=5;
  String yonlendirme="";

  @override
  void initState() {
    super.initState();
    rastgeleSayi=Random().nextInt(101);
    print("Rastgele Sayi: $rastgeleSayi");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Tahmin Ekrani"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Text("Kalan Hak:$kalanHak",style: TextStyle(color: Colors.pink,fontSize: 30),),
            Text("Yardim: $yonlendirme",style: TextStyle(color: Colors.black54,fontSize: 24),),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: tfTahmin,
                keyboardType: TextInputType.number,
                textAlign: TextAlign.center,
                decoration: InputDecoration(
                  labelText: "Tahmin",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(10.0)),
                  ),
                ),
              ),
            ),
            SizedBox(
              width: 200,
              height: 50,
              child: ElevatedButton(
                child: Text("Tahmin Et"),
                style: ElevatedButton.styleFrom(backgroundColor: Colors.pink,foregroundColor: Colors.white),
                onPressed: (){
                  setState(() {
                    kalanHak-=1;
                  });
                  int tahmin=int.parse(tfTahmin.text);
                  if(tahmin==rastgeleSayi){
                    Navigator.pushReplacement(context, MaterialPageRoute(builder: (context)=> SonucEkrani(sonuc: true,)));
                    return;
                  }
                  if(tahmin>rastgeleSayi){
                    setState(() {
                      yonlendirme="Tahmini Azalt";
                    });
                  }
                  if(tahmin<rastgeleSayi){
                    setState(() {
                      yonlendirme="Tahmini Arttir";
                    });
                  }
                  if(kalanHak==0){
                    Navigator.pushReplacement(context, MaterialPageRoute(builder: (context)=> SonucEkrani(sonuc: false,)));
                  }
                    tfTahmin.text="";
                },
              ),
            ),
          ],
        ),
      ),

    );;
  }
}
