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
          children: [
            PopupMenuButton(
              child: Icon(Icons.open_in_new),
              itemBuilder: (context)=> [
                PopupMenuItem(
                  value: 1,
                  child: Text("Sil", style: TextStyle(color: Colors.red),),
                ),
                PopupMenuItem(
                  value: 2,
                  child: Text("Güncelle", style: TextStyle(color: Colors.indigo),),
                ),
              ] ,
              onCanceled: (){
                print("Secim yapilmadi");
              } ,
              onSelected: (menuItemValue){
                if(menuItemValue==1){
                  print("Sil secildi");
                }
                if(menuItemValue==2){
                  print("Güncelle seçildi");
                }
              } ,
            ),
          ],
        ),
      ),

    );
  }
}
