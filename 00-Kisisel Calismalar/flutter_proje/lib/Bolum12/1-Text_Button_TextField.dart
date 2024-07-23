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

  //###BU IKI DEGISKENI EKLEMELISIN KI
  //###BIRBIRLERIYLE BAGLAYABILESIN
  var tfController=TextEditingController();
  String alinanVeri ="";

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
            TextField(
              controller: tfController,
              decoration: InputDecoration(
                hintText: "Yaziniz"
              ),
            ),
            ElevatedButton(
              child: Text("Veriyi AL"),
              onPressed: () {
                setState(() {
                  alinanVeri=tfController.text;
                });
              } ,
            ),
            Text("Gelen Veri: $alinanVeri"),
          ],
        ),
      ),

    );
  }
}
