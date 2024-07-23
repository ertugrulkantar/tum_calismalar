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
        backgroundColor: Colors.red,
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("Baslik", style: TextStyle(color: Colors.white, fontSize:16.0 ),),
            Text("Alt Baslik", style: TextStyle(color: Colors.white, fontSize:12.0 ),),
          ],
        ),
        centerTitle: false,
        leading: IconButton(
          tooltip: "Menu Icon",
          icon: Icon(Icons.dehaze),
          onPressed: (){
            print("Menu Icon Tiklandi");
          },
        ),
        actions: [
          TextButton(
            child: Text("CIKIS", style: TextStyle(color: Colors.white),),
            onPressed: () {
              print("Cikis Tiklandi");
            },
          ),
          IconButton(
            tooltip: "Bilgi",
            icon: Icon(Icons.info_outline),
            onPressed: (){
              print("Bilgi Tiklandi");
            },
          ),
          PopupMenuButton(
            child: Icon(Icons.more_vert),
            itemBuilder: (context) => [
              PopupMenuItem(
                value: 1,
                child: Text("Sil"),
              ),
              PopupMenuItem(
                value: 2,
                child: Text("Guncelle"),
              ),
            ],
            onSelected: (menuItemValue) {
              if(menuItemValue==1){
                print("Sil Tiklandi");
              }
              if(menuItemValue==2){
                print("Guncelle Tiklandi");
              }
            },
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [

          ],
        ),
      ),

    );
  }
}
