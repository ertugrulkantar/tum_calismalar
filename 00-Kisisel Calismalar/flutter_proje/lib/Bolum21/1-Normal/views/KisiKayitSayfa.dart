import 'package:flutter/material.dart';

class KisiKayitSayfa extends StatefulWidget {
  const KisiKayitSayfa({super.key});

  @override
  State<KisiKayitSayfa> createState() => _KisiKayitSayfaState();
}

class _KisiKayitSayfaState extends State<KisiKayitSayfa> {

  var tfKisiAd=TextEditingController();
  var tfKisiTel=TextEditingController();

  Future<void> kayit(String kisi_ad,String kisi_tel) async{
    print("Kisi kayit: $kisi_ad - $kisi_tel");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Kisi Kayit"),),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.only(left:50.0,right: 50.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              TextField(controller: tfKisiAd,decoration: const InputDecoration(hintText: "Kisi Ad" ),),
              TextField(controller: tfKisiTel,decoration: const InputDecoration(hintText: "Kisi Tel" ),),
              ElevatedButton(onPressed: (){
                kayit(tfKisiAd.text,tfKisiTel.text);
              }, child: const Text("Kaydet")),
            ],
          ),
        ),
      ),
    );
  }
}
