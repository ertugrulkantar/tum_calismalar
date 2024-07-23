import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum14/Resimler/19-Yemekler.dart';

class DetaySayfa extends StatefulWidget {
  Yemekler  yemek;

  DetaySayfa({required this.yemek});

  @override
  State<DetaySayfa> createState() => _DetaySayfaState();
}

class _DetaySayfaState extends State<DetaySayfa> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.orange,
        title: Text(widget.yemek.yemek_adi),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Image.asset("lib/Bolum14/Resimler/${widget.yemek.yemek_resim_adi}"),
            Text("${widget.yemek.yemek_fiyat} \u{20BA}",style: TextStyle(fontSize: 48,color: Colors.blue),),
            SizedBox(width: 200,height: 50,
              child: ElevatedButton(
                child: Text("Siparis Ver"),
                style: ElevatedButton.styleFrom(foregroundColor:Colors.white, backgroundColor: Colors.orange ),
                onPressed: (){
                  print("${widget.yemek.yemek_adi} siparis edildi.");
                },
              ),
            ),
          ],
        ),
      ),

    );
  }
}
