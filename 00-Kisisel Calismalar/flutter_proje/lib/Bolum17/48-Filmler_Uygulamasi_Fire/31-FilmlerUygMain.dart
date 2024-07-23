import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/48-Filmler_Uygulamasi_Fire/31-FilmlerSayfa.dart';
import 'package:flutter_proje/Bolum17/48-Filmler_Uygulamasi_Fire/31-Kategoriler.dart';


Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
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
      home:  Anasayfa(),
    );
  }
}

class Anasayfa extends StatefulWidget {


  @override
  State<Anasayfa> createState() => _AnasayfaState();
}

class _AnasayfaState extends State<Anasayfa> {

  var refKategoriler=FirebaseDatabase.instance.ref().child("kategoriler");

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Kategoriler"),
      ),
      body: StreamBuilder<DatabaseEvent>(
        stream: refKategoriler.onValue,
        builder: (context,event){
          if(event.hasData){
            var kategoriListesi=<Kategoriler>[];
            var gelendegerler=event.data!.snapshot.value as dynamic;
            if(gelendegerler!=null){
              gelendegerler.forEach((key,nesne){
                var gelenKategori=Kategoriler.fromJson(key, nesne);
                kategoriListesi.add(gelenKategori);
              });
            }

            return ListView.builder(
              itemCount: kategoriListesi.length,
              itemBuilder: (context,indeks){
                var kategori=kategoriListesi[indeks];
                return GestureDetector(
                  onTap: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>FilmlerSayfa(kategori: kategori,)));
                  },
                  child: Card(
                    child: SizedBox( height: 50,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(kategori.kategori_ad),
                        ],
                      ),
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
