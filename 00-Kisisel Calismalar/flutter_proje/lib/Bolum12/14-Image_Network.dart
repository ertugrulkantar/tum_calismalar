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

  String resimAdi="django.png";

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
            Image.network("http://kasimadalan.pe.hu/filmler/resimler/$resimAdi"),
            ElevatedButton(
              child: Text("Resim1"),
              onPressed: (){
                setState(() {
                  resimAdi="inception.png";
                });
              },
            ),
            ElevatedButton(
              child: Text("Resim2"),
              onPressed: (){
                setState(() {
                  resimAdi="django.png";
                });
              },
            ),
          ],
        ),
      ),

    );
  }
}
