import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/45-Notlar_Uygulamasi_Http/29-Notlar.dart';
import 'package:flutter_proje/Bolum17/45-Notlar_Uygulamasi_Http/29-NotlarUygMain.dart';

import 'package:http/http.dart' as http;

class NotDetaySayfa extends StatefulWidget {
  Notlar not;
  @override
  State<NotDetaySayfa> createState() => _NotDetaySayfaState();

  NotDetaySayfa({required this.not});
}

class _NotDetaySayfaState extends State<NotDetaySayfa> {

  var tfDersAdi=TextEditingController();
  var tfnot1=TextEditingController();
  var tfnot2=TextEditingController();

  Future<void> sil(int not_id) async {
    var url=Uri.parse("http://kasimadalan.pe.hu/notlar/delete_not.php");
    var veri={"not_id":not_id.toString()};
    var cevap=await http.post(url,body: veri);
    print("Not sil cevap: ${cevap.body}");
    Navigator.push(context, MaterialPageRoute(builder: (context)=> Anasayfa()));
  }

  Future<void> guncelle(int not_id,String ders_adi, int not1, int not2 ) async {
    var url=Uri.parse("http://kasimadalan.pe.hu/notlar/update_not.php");
    var veri={"not_id":not_id.toString(),"ders_adi":ders_adi,"not1":not1.toString(),"not2":not2.toString()};
    var cevap=await http.post(url,body: veri);
    print("Not guncelle cevap: ${cevap.body}");
    Navigator.push(context, MaterialPageRoute(builder: (context) => Anasayfa()));
  }

  @override
  void initState() {
    super.initState();
    tfDersAdi.text=widget.not.ders_adi;
    tfnot1.text=widget.not.not1.toString();
    tfnot2.text=widget.not.not2.toString();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Notlar Detay"),
        actions: [
          TextButton(
            child: Text("Sil",style: TextStyle(color: Colors.white),),
            onPressed: (){
              sil(int.parse(widget.not.not_id));
            },
          ),
          TextButton(
            child: Text("Guncelle",style: TextStyle(color: Colors.white),),
            onPressed: (){
              guncelle(int.parse(widget.not.not_id), tfDersAdi.text, int.parse(tfnot1.text), int.parse(tfnot2.text));
            },
          ),
        ],
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.only(left: 50.0,right: 50.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              TextField(
                controller: tfDersAdi,
                decoration: InputDecoration(hintText: "Ders Adi"),
              ),
              TextField(
                controller: tfnot1,
                decoration: InputDecoration(hintText: "1. Not"),
              ),
              TextField(
                controller: tfnot2,
                decoration: InputDecoration(hintText: "2. Not"),
              ),
            ],
          ),
        ),
      ),

    );
  }
}
