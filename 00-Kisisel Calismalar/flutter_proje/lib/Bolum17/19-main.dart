import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/19-Kisiler.dart';

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

  void kisilerParse(){
    String strVeri = '{"kisiler":[{"kisi_id":"1","kisi_ad":"Ahmet","kisi_tel":"12312312"}'
        ',{"kisi_id":"2","kisi_ad":"Mehmet","kisi_tel":"912318212"}]}';
  var jsonVeri=json.decode(strVeri);
  var jsonArray=jsonVeri["kisiler"] as List;
  List<Kisiler> kisilerListesi=jsonArray.map((jsonArrayNesnesi) => Kisiler.fromJson(jsonArrayNesnesi)).toList();
  for(var k in kisilerListesi){
    print("****************");
    print("Kisi id: ${k.kisi_id}");
    print("Kisi ad: ${k.kisi_ad}");
    print("Kisi tel: ${k.kisi_tel}");
  }
  }

  @override
  void initState() {
    super.initState();
    kisilerParse();
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
