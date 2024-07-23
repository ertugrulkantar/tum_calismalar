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
      backgroundColor: Colors.deepPurple,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Icon(Icons.wb_cloudy,color: Colors.white,size: 128,),
            Text("Hava Durumu",style: TextStyle(color: Colors.white,fontSize: 36),),
            SizedBox(width: 250,height: 50,
              child: ElevatedButton(
                child: Text("BASLA",style: TextStyle(color: Colors.white,fontSize: 18),),
                style: ElevatedButton.styleFrom(backgroundColor:Colors.orange ),
                onPressed: (){

                },
              ),
            ),
          ],
        ),
      ),

    );
  }
}
