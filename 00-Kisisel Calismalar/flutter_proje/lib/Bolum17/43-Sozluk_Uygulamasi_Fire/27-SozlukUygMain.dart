import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum17/43-Sozluk_Uygulamasi_Fire/27-DetaySayfa.dart';
import 'package:flutter_proje/Bolum17/43-Sozluk_Uygulamasi_Fire/27-Kelimeler.dart';

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

  bool aramaYapiliyorMu=false;
  String aramaKelimesi="";

  var refKelimeler=FirebaseDatabase.instance.ref().child("kelimeler");







  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: aramaYapiliyorMu ?
            TextField(
              decoration: InputDecoration(hintText: "Arama icin bir sey yazin"),
              onChanged: (aramaSonucu){
                print("Arama sonucu : $aramaSonucu");
                setState(() {
                  aramaKelimesi=aramaSonucu;
                });
              },
            )
            : Text("Sozluk Uygulamasi"),
        actions: [
          aramaYapiliyorMu ?
          IconButton(
          icon: Icon(Icons.cancel),
          onPressed: (){
            setState(() {
              aramaYapiliyorMu=false;
              aramaKelimesi="";
            });
          },
        )
          : IconButton(
            icon: Icon(Icons.search),
            onPressed: (){
              setState(() {
                aramaYapiliyorMu=true;
              });
            },
          ),
        ],
      ),
      body: StreamBuilder<DatabaseEvent>(
        stream:   refKelimeler.onValue,
        builder: (context,event) {
          if(event.hasData){
            var kelimelerListesi=<Kelimeler>[];

            var gelenDegerler=event.data!.snapshot.value as dynamic;

            if(gelenDegerler!=null){
              gelenDegerler.forEach((key,nesne){
                var gelenKelime=Kelimeler.fromJson(key, nesne);
                if(aramaYapiliyorMu){
                  if(gelenKelime.ingilizce.contains(aramaKelimesi)){
                    kelimelerListesi.add(gelenKelime);
                  }

                }
                else{
                  kelimelerListesi.add(gelenKelime);
                }


                });
            }
            return ListView.builder(
              itemCount: kelimelerListesi.length,
              itemBuilder: (context,indeks){
                var kelime=kelimelerListesi[indeks];
                return GestureDetector(
                  onTap: (){
                    Navigator.push(context, MaterialPageRoute(builder: (context)=>DetaySayfa(kelime: kelime,)));
                  },
                  child: SizedBox(height: 50,
                    child: Card(
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          Text(kelime.ingilizce,style: TextStyle(fontWeight: FontWeight.bold),),
                          Text(kelime.turkce),
                        ],
                      ),
                    ),
                  ),
                );
              } ,
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
