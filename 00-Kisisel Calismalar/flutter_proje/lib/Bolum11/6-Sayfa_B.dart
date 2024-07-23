import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum11/6-SayfaAna.dart';

class SayfaB_6 extends StatefulWidget {
  const SayfaB_6({super.key});

  @override
  State<SayfaB_6> createState() => _SayfaB_6State();
}

class _SayfaB_6State extends State<SayfaB_6> {

  Future<bool> geriDonusTusu(BuildContext context) async{
    print("Geri tuşu tıklandı.");
    Navigator.of(context).popUntil((route) => route.isFirst); //Bunu silebilirsin de.
    return false;   //True yaparsan geri tusu calisir.
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("SayfaB"),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
            onPressed: (){
              print("Appbar geri tuşu tıklandı.");
            },
        ),
      ),
      body: WillPopScope(
        onWillPop: () => geriDonusTusu(context),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(
                child: Text("Geldiği Sayfaya Dön"),
                onPressed: (){
                  Navigator.pop(context);
                },
              ),
              ElevatedButton(
                child: Text("Anasayfa'ya Dön"),
                onPressed: (){
                  Navigator.of(context).popUntil((route) => route.isFirst);
                },
              ),
              ElevatedButton(
                child: Text("Anasayfa'ya Geçiş Yap"),
                onPressed: (){
                  Navigator.push(context, MaterialPageRoute(builder: (context) => AnaSayfa_6()));
                },
              ),
            ],
          ),
        ),
      ),

    );
  }
}
