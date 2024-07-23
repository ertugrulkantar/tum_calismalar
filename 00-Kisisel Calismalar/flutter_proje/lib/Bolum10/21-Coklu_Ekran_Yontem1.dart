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
      body: LayoutBuilder(
        builder: (BuildContext context,BoxConstraints constraints){
          if(constraints.maxWidth<600){
            return TelefonTasarim();
          }else{
            return TabletTasarim();
          }
        }
      ),

    );
  }
}

class TabletTasarim extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.asset("lib/Bolum10/Resimler/stevejobs@2x.png"),
          Text("Steve Jobs",style: TextStyle(fontSize: 30.0),),
        ],
      ),
    );
  }
}

class TelefonTasarim extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.asset("lib/Bolum10/Resimler/stevejobs@1x.png"),
          Text("Steve Jobs",style: TextStyle(fontSize: 20.0),),
        ],
      ),
    );
  }
}