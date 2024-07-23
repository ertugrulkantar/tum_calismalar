import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum11/6-Sayfa_B.dart';

class SayfaA_6 extends StatefulWidget {
  const SayfaA_6({super.key});

  @override
  State<SayfaA_6> createState() => _SayfaA_6State();
}

class _SayfaA_6State extends State<SayfaA_6> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Sayfa A"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text("Sayfa B'ye Git"),
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context) => SayfaB_6()));
              },
            ),
          ],
        ),
      ),

    );
  }
}
