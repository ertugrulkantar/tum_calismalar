import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_proje/Bolum19/14-SayacCubit.dart';

class IkinciSayfa extends StatelessWidget {
  const IkinciSayfa({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("IkinciSayfa"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            BlocBuilder<SayacCubit,int>(
              builder: (context,sayacDegeri){
                return Text("$sayacDegeri",style: TextStyle(fontSize: 36),);
              },
            ),

            ElevatedButton(
              child: Text("Sayac Arttir"),
              onPressed: (){
                context.read<SayacCubit>().sayaciArttir();
              },
            ),
            ElevatedButton(
              child: Text("Sayac Azalt"),
              onPressed: (){
                context.read<SayacCubit>().sayaciAzalt(2);
              },
            ),
          ],
        ),
      ),

    );
  }
}
