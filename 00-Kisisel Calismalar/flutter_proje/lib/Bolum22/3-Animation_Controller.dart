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

  late AnimationController animasyonKontrol;
  late Animation<double> alphaAnimasyonDegerleri;
  late Animation<double> scaleAnimasyonDegerleri;
  late Animation<double> rotateAnimasyonDegerleri;
  late Animation<double> translateAnimasyonDegerleri;
  late Animation<double> digerAnimasyonDegerleri;

  @override
  void initState() {
    super.initState();
    animasyonKontrol=AnimationController(duration: Duration(milliseconds: 3000),vsync: this);
    alphaAnimasyonDegerleri=Tween(begin: 1.0,end: 0.0).animate(animasyonKontrol)
      ..addListener(() {
      setState(() {
      });
    });
    scaleAnimasyonDegerleri=Tween(begin: 128.0,end: 50.0).animate(animasyonKontrol)
      ..addListener(() {
      setState(() {
      });
    });
    rotateAnimasyonDegerleri=Tween(begin: 0.0,end: pi/2).animate(animasyonKontrol)
      ..addListener(() {
      setState(() {
      });
    });
    translateAnimasyonDegerleri=Tween(begin: 0.0,end: 50.0).animate(animasyonKontrol)
      ..addListener(() {
      setState(() {
      });
    });
    digerAnimasyonDegerleri=Tween(begin: 0.0,end: 50.0)
        .animate(CurvedAnimation(parent: animasyonKontrol, curve: Curves.easeInOut))
      ..addListener(() {
      setState(() {
      });
    });
  }

  @override
  void dispose() {
    super.dispose();
    animasyonKontrol.dispose();
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.deepPurple,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Opacity(opacity: alphaAnimasyonDegerleri.value,
                child: Icon(Icons.wb_cloudy,color: Colors.white,size: scaleAnimasyonDegerleri.value,)),
            Transform.translate(offset: Offset(digerAnimasyonDegerleri.value,digerAnimasyonDegerleri.value),
              child: Transform.rotate(angle: rotateAnimasyonDegerleri.value,
                  child: Text("Hava Durumu",style: TextStyle(color: Colors.white,fontSize: 36),)),
            ),
            SizedBox(width: 250,height: 50,
              child: ElevatedButton(
                child: Text("BASLA",style: TextStyle(color: Colors.white,fontSize: 18),),
                style: ElevatedButton.styleFrom(backgroundColor:Colors.orange ),
                onPressed: (){
                  //animasyonKontrol.forward(); //4...7
                  animasyonKontrol.repeat(reverse: true);

                },
              ),
            ),
          ],
        ),
      ),

    );
  }
}
