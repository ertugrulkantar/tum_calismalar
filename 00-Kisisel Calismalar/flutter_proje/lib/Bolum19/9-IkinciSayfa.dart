import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_proje/Bolum19/10-SayacModel.dart';

class IkinciSayfa extends StatelessWidget {

  var sayacModelNesne=SayacModel();

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
            Observer(
                builder: (_){
                  return Text("${sayacModelNesne.sayac}",style: TextStyle(fontSize: 30),);
                }),
            ElevatedButton(
              child: Text("Sayac Arttir"),
              onPressed: (){
                sayacModelNesne.sayacArttir();
              },
            ),
            ElevatedButton(
              child: Text("Sayac Azalt"),
              onPressed: (){
                sayacModelNesne.sayacAzalt(2);
              },
            ),
          ],
        ),
      ),

    );
  }
}
