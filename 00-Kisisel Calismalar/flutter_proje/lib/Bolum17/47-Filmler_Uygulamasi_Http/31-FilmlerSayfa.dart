import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/31-DetaySayfa.dart';
import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/31-Filmler.dart';
import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/31-Kategoriler.dart';
import 'package:flutter_proje/Bolum17/47-Filmler_Uygulamasi_Http/FilmlerCevap.dart';

import 'package:http/http.dart' as http;
import 'dart:convert';

class FilmlerSayfa extends StatefulWidget {

  Kategoriler kategori;

  FilmlerSayfa({required this.kategori});

  @override
  State<FilmlerSayfa> createState() => _FilmlerSayfaState();
}

class _FilmlerSayfaState extends State<FilmlerSayfa> {

  List<Filmler> parseFilmlerCevap(String cevap){
    return FilmlerCevap.fromJson(json.decode(cevap)).filmlerNesnesi;
  }



  Future<List<Filmler>> filmleriGoster(int kategori_id) async{
    var url=Uri.parse("http://kasimadalan.pe.hu/filmler/filmler_by_kategori_id.php");
    var veri={"kategori_id":kategori_id.toString()};
    var cevap= await http.post(url,body: veri);
    return parseFilmlerCevap(cevap.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Filmler : ${widget.kategori.kategori_ad}"),
      ),
      body: FutureBuilder<List<Filmler>>(
        future: filmleriGoster(int.parse(widget.kategori.kategori_id)),
        builder: (context,snapshot){
          if(snapshot.hasData){
            var filmlerListesi=snapshot.data;
            return GridView.builder(
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 2/3.5,
              ),
              itemCount: filmlerListesi!.length,
              itemBuilder: (context,indeks){
                var film=filmlerListesi[indeks];
                return GestureDetector(
                  onTap: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>DetaySayfa(film: film)));
                  },
                  child: Card(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        Padding(
                          padding: const EdgeInsets.all(8.0),
                          child: Image.network("http://kasimadalan.pe.hu/filmler/resimler/${film.film_resim}"),
                        ),
                        Text(film.film_ad,style: TextStyle(fontSize: 16,fontWeight: FontWeight.bold),),
                      ],
                    ),
                  ),
                );
              },
            );
          }
          else{
            return Center();
          }
        },
      ),

    );
  }
}
