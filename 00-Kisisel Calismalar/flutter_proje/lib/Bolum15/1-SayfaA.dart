import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SayfaA extends StatefulWidget {
  const SayfaA({super.key});

  @override
  State<SayfaA> createState() => _SayfaAState();
}

class _SayfaAState extends State<SayfaA> {

  Future<void> veriOku() async{
    var sp=await SharedPreferences.getInstance();

    String ad=sp.getString("ad") ?? "isim yok";
    int yas=sp.getInt("yas") ?? 99;
    double boy=sp.getDouble("boy") ?? 9.99;
    bool bekarMi=sp.getBool("bekarMi") ?? false;

    var arkadasListe=sp.getStringList("arkadasListe") ?? null;

    print("Ad: $ad");
    print("Yas: $yas");
    print("Boy: $boy");
    print("Bekar mi: $bekarMi");

    for(var a in arkadasListe!){
      print("Arkadas: $a");
    }
  }

  Future<void> veriSil() async{
    var sp=await SharedPreferences.getInstance();
    sp.remove("ad");
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    veriSil();
    veriOku();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Sayfa A"),
      ),
      body: Center(),

    );
  }
}
