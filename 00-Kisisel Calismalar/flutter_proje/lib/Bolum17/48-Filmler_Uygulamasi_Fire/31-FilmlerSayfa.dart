import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/48-Filmler_Uygulamasi_Fire/31-DetaySayfa.dart';
import 'package:flutter_proje/Bolum17/48-Filmler_Uygulamasi_Fire/31-Filmler.dart';
import 'package:flutter_proje/Bolum17/48-Filmler_Uygulamasi_Fire/31-Kategoriler.dart';


class FilmlerSayfa extends StatefulWidget {



  Kategoriler kategori;

  FilmlerSayfa({required this.kategori});

  @override
  State<FilmlerSayfa> createState() => _FilmlerSayfaState();
}

class _FilmlerSayfaState extends State<FilmlerSayfa> {

  var refFilmler=FirebaseDatabase.instance.ref().child("filmler");

  Future<List<Filmler>> filmleriGoster() async{
    return <Filmler>[];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Filmler : ${widget.kategori.kategori_ad}"),
      ),
      body: StreamBuilder<DatabaseEvent>(
        stream: refFilmler.orderByChild("kategori_ad").equalTo(widget.kategori.kategori_ad).onValue,
        builder: (context,event){
          if(event.hasData){
            var filmlerListesi=<Filmler>[];
            var gelendegerler=event.data!.snapshot.value as dynamic;
            if(gelendegerler!=null){
              gelendegerler.forEach((key,nesne){
                var gelenFilm=Filmler.fromJson(key, nesne);
                filmlerListesi.add(gelenFilm);
              });
            }
            return GridView.builder(
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 2/3.5,
              ),
              itemCount: filmlerListesi.length,
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
