import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum14/22-SayfaBir.dart';
import 'package:flutter_proje/Bolum14/22-SayfaIki.dart';
import 'package:flutter_proje/Bolum14/22-SayfaUc.dart';

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

  var sayfaListesi=[Sayfa1(),Sayfa2(),Sayfa3()];
  int secilenIndeks=0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.deepPurple,
        title: Text("Baslik"),
      ),
      body:sayfaListesi[secilenIndeks],
      bottomNavigationBar: BottomNavigationBar(
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.looks_one),
            label: "Bir",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.looks_two),
            label: "Iki",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.looks_3),
            label: "Uc",
          ),
        ],
        backgroundColor: Colors.deepPurple,
        selectedItemColor: Colors.orange,
        unselectedItemColor: Colors.white,
        currentIndex: secilenIndeks,
        onTap: (indeks){
          setState(() {
            secilenIndeks=indeks;
          });
        },
      ),

    );
  }
}
