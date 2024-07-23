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

  int? radioDeger=0;

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
            RadioListTile(
              title: Text("Galatasaray"),
              value: 1,
              groupValue: radioDeger,
              activeColor: Colors.red,
              onChanged: (int? veri){
                setState(() {
                  radioDeger=veri;
                });
                print("Galatasaray secildi");
              },
            ),
            RadioListTile(
              title: Text("Fenerbahce"),
              value: 2,
              groupValue: radioDeger,
              activeColor: Colors.indigo,
              onChanged: (int? veri){
                setState(() {
                  radioDeger=veri;
                });
                print("Fenerbahce secildi");
              },
            ),
            ElevatedButton(
              child: Text("Goster"),
              onPressed: (){
                if(radioDeger==1){
                  print("Button:: Galatasaray secildi");
                }
                if(radioDeger==2){
                  print("Button:: Fenerbahce secildi");
                }
              },
            ),
          ],
        ),
      ),

    );
  }
}
