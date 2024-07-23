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

  String resimAdi="yemekresim.jpeg";

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
            Image.asset("lib/Bolum12/Resimler/$resimAdi"),
            ElevatedButton(
              child: Text("Resim1"),
              onPressed: (){
                setState(() {
                  resimAdi="yemekresim.jpeg";
                });
              },
            ),
            ElevatedButton(
              child: Text("Resim2"),
              onPressed: (){
                setState(() {
                  resimAdi="resim.jpg";
                });
              },
            ),
          ],
        ),
      ),

    );
  }
}
