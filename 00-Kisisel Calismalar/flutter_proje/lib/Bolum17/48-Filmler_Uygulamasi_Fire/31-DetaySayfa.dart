import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/48-Filmler_Uygulamasi_Fire/31-Filmler.dart';

class DetaySayfa extends StatefulWidget {

  Filmler film;

  DetaySayfa({required this.film});

  @override
  State<DetaySayfa> createState() => _DetaySayfaState();
}

class _DetaySayfaState extends State<DetaySayfa> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.film.film_ad),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Image.network("http://kasimadalan.pe.hu/filmler/resimler/${widget.film.film_resim}"),
            Text(widget.film.film_yil.toString(),style: TextStyle(fontSize: 30),),
            Text(widget.film.yonetmen_ad.toString(),style: TextStyle(fontSize: 30),),
          ],
        ),
      ),

    );
  }
}
