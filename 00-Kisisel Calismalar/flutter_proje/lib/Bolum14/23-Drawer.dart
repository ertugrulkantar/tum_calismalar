import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum14/23-SayfaBir.dart';
import 'package:flutter_proje/Bolum14/23-SayfaIki.dart';
import 'package:flutter_proje/Bolum14/23-SayfaUc.dart';

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

  var sayfaListe=[SayfaBir(),SayfaIki(),SayfaUc()];
  int secilenIndeks=0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.deepPurple,
        title: Text("Baslik"),
      ),
      body: sayfaListe[secilenIndeks],
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,  //Yukarisi tam oturur.
          children: [
            DrawerHeader(
              child: Text("Baslik Tasarimi",style: TextStyle(color: Colors.white,fontSize: 30),),
              decoration: BoxDecoration(
                color: Colors.deepPurple,
              ),
            ),
            ListTile(
              title: Text("Sayfa Bir"),
              onTap: (){
                setState(() {
                  secilenIndeks=0;
                });
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: Text("Sayfa Iki",style: TextStyle(color:Colors.pink ),),
              onTap: (){
                setState(() {
                  secilenIndeks=1;
                });
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: Text("Sayfa Uc"),
              leading: Icon(Icons.looks_3,color: Colors.orange,),
              onTap: (){
                setState(() {
                  secilenIndeks=2;
                });
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),

    );
  }
}
