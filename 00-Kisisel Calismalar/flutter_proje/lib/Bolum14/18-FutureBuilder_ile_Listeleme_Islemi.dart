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

  Future<List<String>> verileriGetir() async{
    var ulkeListesi=["Türkiye","Almanya","İtalya","Rusya","Çin"];
    return ulkeListesi;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Baslik"),
      ),
      body: FutureBuilder<List<String>>(
        future: verileriGetir(),
        builder: (context,snapshot) {
          if (snapshot.hasData) {
            var ulkeListesi = snapshot.data;
            return ListView.builder(
              itemCount: ulkeListesi!.length,
              itemBuilder: (context, indeks) {
                return Card(
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: SizedBox(
                      height: 50,
                      child: Row(
                        children: [
                          Text(ulkeListesi[indeks]),
                        ],
                      ),
                    ),
                  ),
                );
              },
            );
          }

          else {
            return Center();
          }
        },
      ),

    );
  }
}
