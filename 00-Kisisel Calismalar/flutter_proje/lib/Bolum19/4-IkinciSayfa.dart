import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum19/5-SayacModel.dart';
import 'package:provider/provider.dart';

class IkinciSayfa extends StatelessWidget {
  const IkinciSayfa({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Ikinci Sayfa"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Consumer<SayacModel>
              (builder: (context,sayacModelNesne,child){
              return Text("${sayacModelNesne.sayaciOku()}",style: TextStyle(fontSize: 36),);
            },
            ),
            Consumer<SayacModel>
              (builder: (context,sayacModelNesne,child){
              return ElevatedButton(
                child: Text("Sayac Azalt"),
                onPressed: (){
                  sayacModelNesne.sayaciArttir();
                },
              );
            },
            ),
            Consumer<SayacModel>
              (builder: (context,sayacModelNesne,child){
              return ElevatedButton(
                child: Text("Sayac Arttir"),
                onPressed: (){
                  sayacModelNesne.sayaciAzalt(2);
                },
              );
            },
            ),


          ],
        ),
      ),

    );
  }
}
