import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_proje/Bolum19/13-IkinciSayfa.dart';
import 'package:flutter_proje/Bolum19/14-SayacCubit.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp();

  @override
  Widget build(BuildContext context) {
    return MultiBlocProvider(
      providers: [
        BlocProvider(create: (context)=>SayacCubit()),
      ],
      child: MaterialApp(
        title: 'Flutter Demo',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
          useMaterial3: true,
        ),
        home:  Anasayfa(),
      ),
    );
  }
}


class Anasayfa extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Anasayfa"),
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
              child: Text("Gecis Yap"),
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context)=>IkinciSayfa()));
              },
            ),
          ],
        ),
      ),

    );
  }
}
