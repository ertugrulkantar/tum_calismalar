import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum11/6-Sayfa_A.dart';

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
      home:  AnaSayfa_6(),
    );
  }
}

class AnaSayfa_6 extends StatefulWidget {


  @override
  State<AnaSayfa_6> createState() => _AnaSayfa_6State();
}

class _AnaSayfa_6State extends State<AnaSayfa_6> {

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
                Navigator.push(context, MaterialPageRoute(builder: (context) => SayfaA_6()));
              },
            ),
          ],
        ),
      ),

    );
  }
}
