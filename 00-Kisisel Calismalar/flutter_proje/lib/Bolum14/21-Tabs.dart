import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum14/21-Sayfa1.dart';
import 'package:flutter_proje/Bolum14/21-Sayfa2.dart';
import 'package:flutter_proje/Bolum14/21-Sayfa3.dart';

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

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.deepPurple,
          title: Text("Baslik"),
          bottom: TabBar(
            tabs: [
              Tab(text: "Bir",),
              Tab(icon: Icon(Icons.looks_two,color: Colors.cyanAccent,),),
              Tab(text: "Uc",icon: Icon(Icons.looks_3,),),
            ],
            indicatorColor: Colors.pink,
            labelColor: Colors.orange,
          ),
        ),
        body: TabBarView(
          children: [
            Sayfa1(),
            Sayfa2(),
            Sayfa3(),
          ],
        ),

      ),
    );
  }
}
