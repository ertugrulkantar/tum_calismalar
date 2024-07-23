import 'package:flutter/material.dart';

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

  var ulkelerListe=<String>[];
  String secilenUlke="Türkiye";

  @override
  void initState() {
    super.initState();
    ulkelerListe.add("Türkiye");
    ulkelerListe.add("İtalya");
    ulkelerListe.add("Almanya");
    ulkelerListe.add("Rusya");
    ulkelerListe.add("Çin");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Baslik"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            DropdownButton<String>(
              value: secilenUlke,
              items: ulkelerListe.map<DropdownMenuItem<String>>((String value){
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text("Ülke: $value",style: TextStyle(color: Colors.deepPurple,fontSize: 20),),
                );
              }).toList(),
              icon: Icon(Icons.arrow_drop_down),
              onChanged: (String? secilenVeri){
                setState(() {
                  secilenUlke=secilenVeri!;
                });
              },
            ),
            Text("Secilen Ulke: $secilenUlke"),
            ElevatedButton(
                onPressed:(){
                  print("En son secilen ulke: $secilenUlke");
                },
                child: Text("Goster")),
          ],
        ),
      ),

    );
  }
}
