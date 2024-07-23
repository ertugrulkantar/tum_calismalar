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

  Future<int> faktoriyelHesapla(int sayi) async{
    int sonuc=1;
    for(var i=1; i<=sayi;i++){
      sonuc*=i;
    }
    return sonuc;
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
            FutureBuilder<int>(
              future: faktoriyelHesapla(5),
              builder: (context,snapshot){
                if(snapshot.hasError){
                  print("Hata sonucu: ${snapshot.error}");
                }
                if(snapshot.hasData){
                  return Text("Sonuc: ${snapshot.data}");
                }
                else{
                  return Text("Gosterilecek veri yok!");
                }
              },
            ),
          ],
        ),
      ),

    );
  }
}
