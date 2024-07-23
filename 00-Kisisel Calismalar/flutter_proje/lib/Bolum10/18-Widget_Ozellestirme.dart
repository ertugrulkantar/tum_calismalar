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
          children:[
            MaviKare(),
            SizedBox(height: 20,),
            KirmiziKare(),
            Yazi("Merhaba", 30.0)
          ],
        ),
      ),

    );
  }
}
class MaviKare extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(width: 50,height: 50,color: Colors.blue,);
  }
}

class KirmiziKare extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(width: 50,height: 50,color: Colors.red,);
  }
}

class Yazi extends StatelessWidget {

  String ?icerik;
  double ?yaziBoyutu;

  Yazi(this.icerik, this.yaziBoyutu);

  @override
  Widget build(BuildContext context) {
    return Text(icerik!,style: TextStyle(fontSize: yaziBoyutu),);
  }
}
