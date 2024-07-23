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
    
    var ekranBilgisi=MediaQuery.of(context);
    final double ekranYuksekligi=ekranBilgisi.size.height;
    final double ekranGenisligi=ekranBilgisi.size.width;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Baslik"),
      ),
      body: Column(
        children: [
          Padding(
            padding: EdgeInsets.only(top:ekranYuksekligi/100),
            child: SizedBox(
                width: ekranGenisligi/2,
                height: ekranYuksekligi/5,
                child: Image.asset("lib/Bolum10/Resimler/resim.jpg")),
          ),
          Container(width: ekranGenisligi,height: ekranYuksekligi/4,color: Colors.red,),
          Text("Merhaba", style: TextStyle(fontSize: ekranGenisligi/10),),
        ],
      ),

    );
  }
}
