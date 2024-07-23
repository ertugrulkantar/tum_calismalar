import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/25-QuizEkrani.dart';

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
            Text("QUIZE HOSGELDINIZ",style: TextStyle(fontSize: 30),),
            SizedBox( width: 250, height: 50,
              child: ElevatedButton(
                child: Text("Basla"),
                onPressed: (){
                  Navigator.push(context, MaterialPageRoute(builder: (context)=> QuizEkrani()));
                },
              ),
            )
          ],
        ),
      ),

    );
  }
}
