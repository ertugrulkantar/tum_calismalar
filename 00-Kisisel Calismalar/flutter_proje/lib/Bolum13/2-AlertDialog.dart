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
            ElevatedButton(
              child: Text("Basic Alert"),
              onPressed: (){
                showDialog(
                  context: context,
                builder: (BuildContext context){
                    return AlertDialog(
                      title: Text("Baslik"),
                      content: Text("Icerik"),
                      actions: [
                        TextButton(
                          child: Text("Iptal"),
                          onPressed: (){
                            Navigator.pop(context);
                          },
                        ),
                        TextButton(
                          child: Text("Tamam"),
                          onPressed: (){
                            print("Tamam secildi");
                            Navigator.pop(context);
                          },
                        ),
                      ],
                    );
                });
              },
            ),ElevatedButton(
              child: Text("Special Alert"),
              onPressed: (){
                
              },
            ),
          ],
        ),
      ),

    );
  }
}
