import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/18-Mesajlar.dart';

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

  void mesajParse(){
    String strVeri='{ "mesajlar" : { "mesaj_kod" : 1,"mesaj_icerik" : "başarılı"  } }';
    var jsonVeri=json.decode(strVeri);
    var jsonNesne=jsonVeri["mesajlar"];
    var mesaj= Mesajlar.fromJson(jsonNesne);
    print("mesaj kod: ${mesaj.mesaj_kod}");
    print("mesaj icerik: ${mesaj.mesaj_icerik}");
  }

  @override
  void initState() {
    super.initState();
    mesajParse();
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
