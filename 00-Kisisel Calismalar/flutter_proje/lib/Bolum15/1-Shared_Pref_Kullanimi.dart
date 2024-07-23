import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/1-SayfaA.dart';
import 'package:shared_preferences/shared_preferences.dart';

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

  Future<void> veriKaydi() async{
    var sp=await SharedPreferences.getInstance();

    sp.setString("ad", "ahmet");
    sp.setInt("yas", 18);
    sp.setDouble("boy", 1.78);
    sp.setBool("bekarMi", true);

    var arkadasListe=<String>[];
    arkadasListe.add("Ece");
    arkadasListe.add("Ali");
    sp.setStringList("arkadasListe", arkadasListe);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Anasayfa"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text("Gecis Yap"),
              onPressed: (){
                veriKaydi();
                Navigator.push(context,MaterialPageRoute(builder: (context)=>SayfaA()));
              },
            ),
          ],
        ),
      ),

    );
  }
}
