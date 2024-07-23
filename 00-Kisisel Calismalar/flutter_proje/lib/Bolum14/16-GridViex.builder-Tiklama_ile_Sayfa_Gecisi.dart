import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum14/16-DetaySayfa.dart';

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
      home:  MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {


  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  var ulkeler= ["Türkiye","Almanya","İtalya","Rusya","Çin"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Baslik"),
      ),
      body: GridView.builder(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 2/1,
        ),
        itemCount: ulkeler.length,
        itemBuilder: (context,indeks){
          return GestureDetector(
            onTap: (){
              //print("${ulkeler[indeks]} secildi.");
              Navigator.push(context,MaterialPageRoute(builder: (context)=>DetaySayfa(ulkeAdi: ulkeler[indeks],)));
            },
            child: Card(
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    GestureDetector(
                        onTap: () {
                          print("Text ile ${ulkeler[indeks]} secildi.");
                        },
                        child: Text(ulkeler[indeks])),
                    Spacer(),
                    TextButton(
                      child: Text("Ulke Sec"),
                      style: TextButton.styleFrom(
                        foregroundColor: Colors.red,
                      ),
                      onPressed: (){
                        print("Buton ile ${ulkeler[indeks]} secildi.");
                      },
                    ),
                  ],
                ),
              ),
            ),
          );
        },
      ),

    );
  }
}
