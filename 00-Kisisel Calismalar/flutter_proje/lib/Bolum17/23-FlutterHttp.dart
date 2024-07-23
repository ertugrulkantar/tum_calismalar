import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/19-Kisiler.dart';
import 'package:flutter_proje/Bolum17/20-KisilerCevap.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home:  MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {


  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  List<Kisiler> parseKisilerCevap(String cevap){
    /*var jsonVeri=json.decode(cevap);
    var kisilerCevap=KisilerCevap.fromJson(jsonVeri);  //Bunu asagidaki sekilde tek satira dusurdu.
    List<Kisiler> kisilerListesi=kisilerCevap.kisilerListesi;
    return kisilerListesi;*/
    var kisilerCevap=KisilerCevap.fromJson(json.decode(cevap));
    return kisilerCevap.kisilerListesi;
  }

  Future<List<Kisiler>> tumKisiler() async{ //24
    //var url = Uri.parse("http://ertugrulkantar.000.pe/test/tum_kisiler.php");  //CALISMIYOR
    var url = Uri.parse("http://kasimadalan.pe.hu/kisiler/tum_kisiler.php");
    var cevap=await http.get(url);
    return parseKisilerCevap(cevap.body);
  }

  Future<List<Kisiler>> kisilerAra(String aramaKelimesi) async{  //25
    var url = Uri.parse("http://kasimadalan.pe.hu/kisiler/tum_kisiler_arama.php");
    var veri={"kisi_ad":aramaKelimesi};
    var cevap=await http.post(url,body: veri);
    return parseKisilerCevap(cevap.body);
  }

  Future<void> kisilerSil(int kisi_id) async{  //26
    var url = Uri.parse("http://kasimadalan.pe.hu/kisiler/delete_kisiler.php");
    var veri={"kisi_id":kisi_id.toString()};
    var cevap=await http.post(url,body: veri);
    print("Silme Cevao: ${cevap.body}");
  }

  Future<void> kisiEkle(String kisi_ad,String kisi_tel) async{  //27
    var url = Uri.parse("http://kasimadalan.pe.hu/kisiler/insert_kisiler.php");
    var veri={"kisi_ad":kisi_ad,"kisi_tel":kisi_tel};
    var cevap=await http.post(url,body: veri);
    print("Ekleme Cevao: ${cevap.body}");
  }

  Future<void> kisiGuncelle(int kisi_id,String kisi_ad,String kisi_tel) async{  //27
    var url = Uri.parse("http://kasimadalan.pe.hu/kisiler/update_kisiler.php");
    var veri={"kisi_id":kisi_id.toString(),"kisi_ad":kisi_ad,"kisi_tel":kisi_tel};
    var cevap=await http.post(url,body: veri);
    print("Guncelleme Cevao: ${cevap.body}");
  }

  Future<void> kisileriGoster() async{
    var liste=await tumKisiler();  //24 icin bunu ac.
    //var liste=await kisilerAra("ECE"); //25
    //kisilerSil(16453); //26
    //kisiEkle("Kasim Hocam", "Sizi Seviyoruz!"); //27
    kisiGuncelle(16468, "Ertugrul", "33333");

    for(var k in liste){
      print("***********");
      print("Kisi id: ${k.kisi_id}");
      print("Kisi ad: ${k.kisi_ad}");
      print("Kisi tel: ${k.kisi_tel}");
    }
  }

  @override
  void initState() {
    super.initState();
    kisileriGoster();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Baslik"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [

          ],
        ),
      ),

    );
  }
}
