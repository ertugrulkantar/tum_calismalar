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

    var ekranBilgisi=MediaQuery.of(context);
    final double ekranYuksekligi=ekranBilgisi.size.height;
    final double ekranGenisligi=ekranBilgisi.size.width;

    return Scaffold(
      backgroundColor: Colors.deepPurple,
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Padding(
                padding: EdgeInsets.only(bottom: ekranYuksekligi/20),
                child: SizedBox(
                    width: ekranGenisligi/4,
                    height: ekranYuksekligi/6,
                    child: Image.asset("lib/Bolum10/Resimler/logo.png")
                ),
              ),
              Padding(
                padding:  EdgeInsets.all(ekranYuksekligi/30),
                child: TextField(
                  decoration: InputDecoration(
                    hintText: "Kullanıcı Adı",
                    filled: true,
                    fillColor: Colors.white,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(10.0)),
                    ),
                  ),
                ),
              ),
              Padding(
                padding:  EdgeInsets.all(ekranYuksekligi/30),
                child: TextField(
                  obscureText: true,
                  decoration: InputDecoration(
                    hintText: "Şifre",
                    filled: true,
                    fillColor: Colors.white,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(10.0)),
                    ),
                  ),
                ),
              ),
              Padding(
                padding:  EdgeInsets.all(ekranYuksekligi/30),
                child: SizedBox(
                  width: ekranGenisligi/1.2,
                  height: ekranYuksekligi/12,
                  child: ElevatedButton(
                    child: Text("GİRİŞ YAP",style: TextStyle(fontSize: ekranGenisligi/25),),
                    onPressed: (){
                      print("Giriş yapıldı");
                    },
                      style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.pink,
                          foregroundColor: Colors.white)
                  ),
                ),
              ),
              GestureDetector(
                onTap: (){
                  print("Yardim Secildi!");
                },
                child: Text("Yardim?",style: TextStyle(
                  color: Colors.pink,
                  fontWeight: FontWeight.bold,
                  fontSize: ekranGenisligi/30,
                ),),
              ),
            ],
          ),
        ),
      ),

    );
  }
}
