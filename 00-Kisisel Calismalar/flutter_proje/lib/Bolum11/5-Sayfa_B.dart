import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum11/5-Sayfa_Ana.dart';

class SayfaB extends StatefulWidget {
  const SayfaB({super.key});

  @override
  State<SayfaB> createState() => _SayfaBState();
}

class _SayfaBState extends State<SayfaB> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("SayfaB"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text("Geldiği Sayfaya Dön"),
              onPressed: (){
                Navigator.pop(context);
              },
            ),
            ElevatedButton(
              child: Text("Anasayfa'ya Dön"),
              onPressed: (){
                Navigator.of(context).popUntil((route) => route.isFirst);
              },
            ),
            ElevatedButton(
              child: Text("Anasayfa'ya Geçiş Yap"),
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context) => AnaSayfa()));
              },
            ),
          ],
        ),
      ),

    );
  }
}
