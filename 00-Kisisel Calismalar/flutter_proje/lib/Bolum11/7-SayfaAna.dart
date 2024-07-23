import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum11/7-Kisiler.dart';
import 'package:flutter_proje/Bolum11/7-Sayfa_A.dart';

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
      home:  AnaSayfa_7(),
    );
  }
}

class AnaSayfa_7 extends StatefulWidget {


  @override
  State<AnaSayfa_7> createState() => _AnaSayfa_7State();
}

class _AnaSayfa_7State extends State<AnaSayfa_7> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("AnaSayfa"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text("Sayfa A'ya Git"),
              onPressed: (){
                var kisi= Kisiler(isim: "Ahmet",yas: 18,boy: 1.78,bekarMi: true,);
                Navigator.push(context, MaterialPageRoute(builder: (context) => SayfaA_7(kisi : kisi)));
              },
            ),
          ],
        ),
      ),

    );
  }
}
