import 'package:flutter/material.dart';

class SayfaIki extends StatefulWidget {
  const SayfaIki({super.key});

  @override
  State<SayfaIki> createState() => _SayfaIkiState();
}

class _SayfaIkiState extends State<SayfaIki> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text("Sayfa Iki",style: TextStyle(color: Colors.black54,fontSize: 30),),
    );
  }
}
