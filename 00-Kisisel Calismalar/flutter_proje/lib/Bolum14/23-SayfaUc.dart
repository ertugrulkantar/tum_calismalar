import 'package:flutter/material.dart';

class SayfaUc extends StatefulWidget {
  const SayfaUc({super.key});

  @override
  State<SayfaUc> createState() => _SayfaUcState();
}

class _SayfaUcState extends State<SayfaUc> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text("Sayfa Uc",style: TextStyle(color: Colors.black54,fontSize: 30),),
    );
  }
}
