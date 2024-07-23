import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/3-SharedPrefs_Login_Ornek.dart';
import 'package:shared_preferences/shared_preferences.dart';

class AnaSayfa extends StatefulWidget {
  const AnaSayfa({super.key});

  @override
  State<AnaSayfa> createState() => _AnaSayfaState();
}

class _AnaSayfaState extends State<AnaSayfa> {

  late String spKullaniciAdi;
  late String spSifre;

  Future<void> oturumBilgisiOku() async{
    var sp=await SharedPreferences.getInstance();
    
    setState(() {
      spKullaniciAdi=sp.getString("kullaniciAdi") ?? "kullanici adi yok";
      spSifre=sp.getString("sifre") ?? "sifre yok";
    });
  }

  Future<void> cikisYap() async{
    var sp=await SharedPreferences.getInstance();
    sp.remove("kullaniciAdi");
    sp.remove("sifre");
    Navigator.pushReplacement(context,MaterialPageRoute(builder: (context)=>LoginEkrani()));
  }
@override
  void initState() {
    // TODO: implement initState
    super.initState();
    oturumBilgisiOku();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("AnaSayfa"),
        actions: [
          IconButton(
            icon: Icon(Icons.exit_to_app),
            onPressed: (){
              cikisYap();
            },
          ),
        ],
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Kullaci Adi: $spKullaniciAdi",style: TextStyle(fontSize: 30),),
              Text("Sifre: $spSifre",style: TextStyle(fontSize: 30),),
            ],
          ),
        ),
      ),

    );
  }
}
