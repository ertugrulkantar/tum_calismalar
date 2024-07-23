import 'dart:collection';

import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/46-Notlar_Uygulamasi_Fire/29-NotlarUygMain.dart';

class NotKayitSayfa extends StatefulWidget {
  const NotKayitSayfa({super.key});

  @override
  State<NotKayitSayfa> createState() => _NotKayitSayfaState();
}

class _NotKayitSayfaState extends State<NotKayitSayfa> {

  var tfDersAdi=TextEditingController();
  var tfnot1=TextEditingController();
  var tfnot2=TextEditingController();

  var refNotlar= FirebaseDatabase.instance.ref().child("notlar");

  Future<void> kayit(String ders_adi, int not1, int not2 ) async {
    var bilgi=HashMap<String,dynamic>();
    bilgi["not_id"]="";
    bilgi["ders_adi"]=ders_adi;
    bilgi["not1"]=not1;
    bilgi["not2"]=not2;
    refNotlar.push().set(bilgi);
    Navigator.push(context, MaterialPageRoute(builder: (context)=> Anasayfa()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Notlar Kayit"),
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
      floatingActionButton: FloatingActionButton.extended(
        onPressed: (){
          kayit(tfDersAdi.text, int.parse(tfnot1.text), int.parse(tfnot2.text));
        } ,
        tooltip: "Not Kayit",
        icon: Icon(Icons.save),
        label: Text("Kaydet"),
      ),
    );
  }
}
