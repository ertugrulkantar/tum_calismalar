import 'dart:async';

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

  late Timer zamanlayici;
  int kalanSure=10;

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
            Text("Kalan sure : $kalanSure sn",style: TextStyle(fontSize: 30),),
            ElevatedButton(
              child: Text("Basla"),
              onPressed: (){
                zamanlayici=Timer.periodic(Duration(seconds: 1), (timer) {
                  setState(() {
                    if(kalanSure<1){
                      kalanSure=10;
                      zamanlayici.cancel();
                    }
                    else{
                      kalanSure=kalanSure-1;
                    }
                  });
                });

              },
            ),
          ],
        ),
      ),

    );
  }
}
