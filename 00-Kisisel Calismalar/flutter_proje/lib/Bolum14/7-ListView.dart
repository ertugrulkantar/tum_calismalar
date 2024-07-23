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
      body: ListView(
        children: [
          ListTile(
            leading: Icon(Icons.sunny),
            title: Text("Gunes"),
            subtitle: Text("Gunes alt baslik"),
            trailing: Icon(Icons.arrow_right),
            onTap: (){
              print("Gunes Tiklandi");
            },
          ),
          ListTile(
            leading: Icon(Icons.brightness_2),
            title: Text("Ay"),
            subtitle: Text("Ay alt baslik"),
            trailing: Icon(Icons.arrow_right),
            onTap: (){
              print("Ay Tiklandi");
            },
          ),
          ListTile(
            leading: Icon(Icons.star),
            title: Text("Yıldız"),
            subtitle: Text("Yıldız alt baslik"),
            trailing: Icon(Icons.arrow_right),
            onTap: (){
              print("Yıldız Tiklandi");
            },
          ),
          GestureDetector(
            onTap: (){
              print("Card Tiklandi");
            },
            child: Card(
              child: SizedBox(
                height: 50,
                child: Row(
                  children: [
                    Text("Card Tasarim"),
                    Spacer(),
                    Icon(Icons.more_vert),
                  ],
                ),
              ),
            ),
          ),
          GestureDetector(
            onTap: (){
              print("Container Tiklandi");
            },
            child: Container(
              height: 50,
              color: Colors.red,
              child: Text("Merhaba"),
            ),
          ),
        ],
      ),

    );
  }
}
