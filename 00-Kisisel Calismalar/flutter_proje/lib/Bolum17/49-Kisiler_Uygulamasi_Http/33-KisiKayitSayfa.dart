import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/49-Kisiler_Uygulamasi_Http/33-KisilerUygMain.dart';
import 'package:http/http.dart' as http;

class KisiKayitSayfa extends StatefulWidget {
  const KisiKayitSayfa({super.key});

  @override
  State<KisiKayitSayfa> createState() => _KisiKayitSayfaState();
}

class _KisiKayitSayfaState extends State<KisiKayitSayfa> {

  var tfKisiAdi=TextEditingController();
  var tfKisiTel=TextEditingController();

  Future<void> kayit(String kisi_ad, String kisi_tel) async{
    var url=Uri.parse("http://kasimadalan.pe.hu/kisiler/insert_kisiler.php");
    var veri={"kisi_ad":kisi_ad,"kisi_tel":kisi_tel};
    var cevap=await http.post(url,body: veri);
    print("Ekle Cevap:${cevap.body}");
    Navigator.push(context,MaterialPageRoute(builder: (context)=>Anasayfa()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Kisiler Kayit"),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.only(left: 50,right: 50),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              TextField(
                controller: tfKisiAdi,
                decoration: InputDecoration(hintText: "Kisi Ad"),
              ),
              TextField(
                controller: tfKisiTel,
                decoration: InputDecoration(hintText: "Kisi Tel"),
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: (){
          kayit(tfKisiAdi.text, tfKisiTel.text);
        },
        tooltip: "Kisi Ekle",
        icon: Icon(Icons.save),
        label: Text("Kaydet"),
      ),
    );
  }
}
