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
      body: Row(
        children: [
          Container(
            margin: const EdgeInsets.all(10.0),
            //margin: const EdgeInsets.only(top:10.0,left:5.0),
            width: 200,
            height: 200,
            //color: Colors.red,
            child: Text("Merhaba") ,
            decoration: BoxDecoration(
              color:Colors.yellow,
              border: Border.all(
                color: Colors.blue,
                width: 10.0
              ),
              borderRadius: BorderRadius.all(Radius.circular(20.0))
            ),
          ),
        ],
      ),

    );
  }
}
