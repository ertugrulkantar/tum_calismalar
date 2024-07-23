import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

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

  int sayac=0;

  Future<void> sayacKontrol() async {
    var sp=await SharedPreferences.getInstance();
    sayac=sp.getInt("sayac") ?? 0;

    setState(() {
      sayac++;
    });

    sp.setInt("sayac", sayac);
  }
@override
  void initState() {
    // TODO: implement initState
    super.initState();
    sayacKontrol();
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
            Text("Acilis sayisi: $sayac",style: TextStyle(fontSize: 50),),
          ],
        ),
      ),

    );
  }
}
