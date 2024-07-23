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
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                controller: tfController,

                obscureText: true, //Sifre girermis gibi
                keyboardType: TextInputType.datetime,
                textAlign: TextAlign.center,
                maxLength: 4,
                style: TextStyle(color: Colors.white),
                decoration: InputDecoration(
                  hintText: "Yaziniz",
                  hintStyle: TextStyle(
                    color: Colors.yellow,
                    fontSize: 20,
                  ),
                  labelText: "Email",
                  labelStyle: TextStyle(
                    color: Colors.red,
                    fontSize: 30,
                  ),
                  filled: true,
                  fillColor: Colors.green,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(10.0)),
                  ),
                  prefixIcon: Icon(Icons.print),
                ),
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
