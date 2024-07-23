import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum12/20-Tahmin_Ekrani.dart';

void main() {
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Anasayfa"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Text("Tahmin Oyunu",style: TextStyle(color: Colors.black54,fontSize: 36),),
            Image.asset("lib/Bolum12/Resimler/zar_resim.png"),
            SizedBox(
              width: 200,
              height: 50,
              child: ElevatedButton(
                child: Text("Oyun Basla"),
                style: ElevatedButton.styleFrom(backgroundColor: Colors.blue,foregroundColor: Colors.white),
                onPressed: (){
                  Navigator.push(context, MaterialPageRoute(builder: (context)=> TahminEkrani()));
                },
              ),
            ),
          ],
        ),
      ),

    );
  }
}
