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
      appBar: AppBar(
        backgroundColor: Colors.red,
        title: Text("İlham Ver"),
      ),
      body: Column(
        children: [
          Padding(
            padding: EdgeInsets.only(top:ekranYuksekligi/100, bottom: ekranYuksekligi/100),
            child: SizedBox(
                width: ekranGenisligi/4,
                child: Image.asset("lib/Bolum10/Resimler/stevejobs@3x.png")
            ),
          ),
          Text("Steve Jobs",
            style: TextStyle(
              color: Colors.redAccent,
              fontWeight: FontWeight.bold,
              fontSize: ekranGenisligi/25
            ),
          ),
          Spacer(),
          Padding(
            padding:  EdgeInsets.only(left: ekranGenisligi/100,right: ekranGenisligi/100),
            child: Text("Dünyayı değiştirecek insanlar, onu değiştirebileceklerini düşünecek kadar çılgın olanlardır.",
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: ekranGenisligi/25
              ),
            ),
          ),
          Spacer(),
          Padding(
            padding:  EdgeInsets.only(bottom: ekranYuksekligi/100),
            child: SizedBox(
              width: ekranGenisligi/2,
              height: ekranYuksekligi/15,
              child: ElevatedButton(
                  child: Text("İLHAM VER",style: TextStyle(fontSize: ekranGenisligi/25),),
                  onPressed: (){
                    print("İlham verildi");
                  },
              style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.redAccent,
                  foregroundColor: Colors.white)
    ),
            ),
          ),
        ],
      ),
    );
  }
}
