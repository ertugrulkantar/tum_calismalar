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

  var ulkeler=["Türkiye","Almanya","İtalya","Rusya","Çin"];


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Baslik"),
      ),
      body: SizedBox(
        height: 100,
        child: ListView.builder(
          scrollDirection: Axis.horizontal,
          itemCount: ulkeler.length,
          itemBuilder: (context,indeks) {
            return GestureDetector(
              onTap: (){
                print("${ulkeler[indeks]} secildi.");
              },
              child: Card(
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: SizedBox(
                    width: 100,
                    child: Row(
                      children: [
                        GestureDetector(
                            onTap: (){
                              print("Text ile ${ulkeler[indeks]} secildi");
                            }    ,
                            child: Text(ulkeler[indeks])),
                        Spacer(),
                        PopupMenuButton(
                          child: Icon(Icons.more_vert),
                          itemBuilder: (context) => [
                            PopupMenuItem(value: 1, child: Text("Sil"),),
                            PopupMenuItem(value: 2, child: Text("Guncelle"),),
                          ],
                          onSelected: (menuItemValue){
                            if(menuItemValue==1){
                              print("${ulkeler[indeks]} silindi");
                            }
                            if(menuItemValue==2){
                              print("${ulkeler[indeks]} guncellendi");
                            }
                          },
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}
