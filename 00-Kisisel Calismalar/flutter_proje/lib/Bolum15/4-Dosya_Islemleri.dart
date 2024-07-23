import 'dart:io';

import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';

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

  var tfgirdi=TextEditingController();

  Future<void> veriYaz() async{
    var ad=await getApplicationDocumentsDirectory();

    var uygulamaDosyalamaYolu=await ad.path;

    var dosya=File("$uygulamaDosyalamaYolu/dosyam.txt");
    dosya.writeAsString(tfgirdi.text);
    tfgirdi.text="";
  }
  Future<void> veriOku() async{
    try{
      var ad=await getApplicationDocumentsDirectory();

      var uygulamaDosyalamaYolu=await ad.path;

      var dosya=File("$uygulamaDosyalamaYolu/dosyam.txt");

      String okunanVeri=await dosya.readAsStringSync();
      tfgirdi.text=okunanVeri;
    }
    catch(e){
      e.toString();
    }
  }

  Future<void> veriSil() async{
    var ad=await getApplicationDocumentsDirectory();

    var uygulamaDosyalamaYolu=await ad.path;

    var dosya=File("$uygulamaDosyalamaYolu/dosyam.txt");

    if(dosya.existsSync()){
      dosya.delete();
    }
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
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: tfgirdi,
                decoration: InputDecoration(
                  hintText: "Veri Giriniz"
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(
                  child: Text("Yaz"),
                  onPressed: (){
                    veriYaz();
                  },
                ),
                ElevatedButton(
                  child: Text("Oku"),
                  onPressed: (){
                    veriOku();
                  },
                ),
                ElevatedButton(
                  child: Text("Sil"),
                  onPressed: (){
                    veriSil();
                  },
                ),
              ],
            ),
          ],
        ),
      ),

    );
  }
}
