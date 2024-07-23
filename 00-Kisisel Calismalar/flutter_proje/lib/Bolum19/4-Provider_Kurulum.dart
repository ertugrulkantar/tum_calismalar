import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum19/4-IkinciSayfa.dart';
import 'package:flutter_proje/Bolum19/5-SayacModel.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp();

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context)=>SayacModel()),
      ],
      child: MaterialApp(
        title: 'Flutter Demo',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
          useMaterial3: true,
        ),
        home:  Anasayfa(),
      ),
    );
  }
}


class Anasayfa extends StatelessWidget {

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
            Consumer<SayacModel>
              (builder: (context,sayacModelNesne,child){
              return Text("${sayacModelNesne.sayaciOku()}",style: TextStyle(fontSize: 36),);
            },
            ),
            ElevatedButton(
              child: Text("Gecis Yap"),
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context)=>IkinciSayfa()));
              },
            ),
          ],
        ),
      ),

    );
  }
}
