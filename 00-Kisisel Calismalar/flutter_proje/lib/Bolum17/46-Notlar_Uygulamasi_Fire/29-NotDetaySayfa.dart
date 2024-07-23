import 'dart:collection';

import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/46-Notlar_Uygulamasi_Fire/29-Notlar.dart';
import 'package:flutter_proje/Bolum17/46-Notlar_Uygulamasi_Fire/29-NotlarUygMain.dart';


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

  var refNotlar= FirebaseDatabase.instance.ref().child("notlar");

  Future<void> sil(String not_id) async {
    refNotlar.child(not_id).remove();
    Navigator.push(context, MaterialPageRoute(builder: (context)=> Anasayfa()));
  }

  Future<void> guncelle(String not_id,String ders_adi, int not1, int not2 ) async {
    var bilgi=HashMap<String,dynamic>();
    bilgi["ders_adi"]=ders_adi;
    bilgi["not1"]=not1;
    bilgi["not2"]=not2;
    refNotlar.child(not_id).update(bilgi);
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
              sil(widget.not.not_id);
            },
          ),
          TextButton(
            child: Text("Guncelle",style: TextStyle(color: Colors.white),),
            onPressed: (){
              guncelle(widget.not.not_id, tfDersAdi.text, int.parse(tfnot1.text), int.parse(tfnot2.text));
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
