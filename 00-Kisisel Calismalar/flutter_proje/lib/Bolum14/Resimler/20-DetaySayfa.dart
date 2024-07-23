import 'package:flutter/material.dart';
import '../20-Filmler.dart';

class DetaySayfa extends StatefulWidget {
  Filmler film;

  DetaySayfa(this.film);

  @override
  State<DetaySayfa> createState() => _DetaySayfaState();
}

class _DetaySayfaState extends State<DetaySayfa> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.deepPurple,
        title: Text(widget.film.film_adi),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Image.asset("lib/Bolum14/Resimler/${widget.film.film_resim_adi}"),
            Text("${widget.film.film_fiyat} \u{20BA}",style: TextStyle(fontSize: 48,color: Colors.blue)),
            SizedBox(
              width: 200,
              height: 50,
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(backgroundColor: Colors.red,foregroundColor: Colors.white),
                child: Text("Kirala"),
                onPressed: (){
                  print("${widget.film.film_adi} Kiralandi");
                },
              ),
            ),
          ],
        ),
      ),
    );;
  }
}
