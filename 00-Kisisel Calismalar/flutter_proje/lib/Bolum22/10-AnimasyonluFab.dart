import 'dart:math';

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

class _MyHomePageState extends State<MyHomePage> with TickerProviderStateMixin{

  late AnimationController animasyonkontrol;
  late Animation<double> scaleAnimasyonDegerleri;
  late Animation<double> rotateAnimasyonDegerleri;
  bool fabDurum=false;

  @override
  void initState() {
    super.initState();
    animasyonkontrol=AnimationController(duration: Duration(milliseconds: 250),vsync: this);

    scaleAnimasyonDegerleri=Tween(begin: 0.0,end: 1.0).animate(animasyonkontrol)..addListener(() {
      setState(() {

      });
    });
    rotateAnimasyonDegerleri=Tween(begin: 0.0,end: pi/4).animate(animasyonkontrol)..addListener(() {
      setState(() {

      });
    });
  }

  @override
  void dispose() {
    super.dispose();
    animasyonkontrol.dispose();
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

          ],
        ),
      ),
    floatingActionButton:
    Column(
      mainAxisAlignment: MainAxisAlignment.end,
      children: [
        Transform.scale(scale: scaleAnimasyonDegerleri.value,
          child: FloatingActionButton(
            onPressed: (){
              print("Fab1 Tiklandi");
            },
            tooltip: "Fab 1",
            child: Icon(Icons.alarm),
            backgroundColor: Colors.orange,
          ),
        ),
        Transform.scale(scale: scaleAnimasyonDegerleri.value,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: FloatingActionButton(
              onPressed: (){
                print("Fab2 Tiklandi");
              },
              tooltip: "Fab 2",
              child: Icon(Icons.photo_camera),
              backgroundColor: Colors.yellow,
            ),
          ),
        ),
        Transform.rotate(angle: rotateAnimasyonDegerleri.value,
          child: FloatingActionButton(
            onPressed: (){
              print("Fab3 Tiklandi");
              if(fabDurum){
                animasyonkontrol.reverse();
                fabDurum=false;
              }
              else{
                animasyonkontrol.forward();
                fabDurum=true;
              }
            },
            tooltip: "Fab 3",
            child: Icon(Icons.add),
            backgroundColor: Colors.red,
          ),
        ),
      ],
    ),
    );
  }
}
