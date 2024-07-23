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
              child: Text("Varsayilan"),
              onPressed: (){
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text("Merhaba!"),),
                );
              },
            ),ElevatedButton(
              child: Text("Snackbar Action"),
              onPressed: (){
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text("Silmek istiyor musun?"),
                    action: SnackBarAction(
                      label:"Evet",
                      onPressed: (){
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(content: Text("Silindi!!"),),
                        );
                      },
                    ),
                  ),
                );
              },
            ),ElevatedButton(
              child: Text("Snackbar Ozel"),
              onPressed: (){
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text("Internet Baglantisi Yok!",style: TextStyle(color: Colors.indigoAccent) ,),
                    backgroundColor: Colors.white,
                    duration: Duration(seconds: 5),
                    action: SnackBarAction(
                      label:"Tekrar Dene",
                      textColor: Colors.red,
                      onPressed: (){
                        print("Tekrar denendi");
                      },
                    ),
                  ),
                );
              },
            ),
          ],
        ),
      ),

    );
  }
}
