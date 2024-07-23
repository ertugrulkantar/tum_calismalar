import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_proje/Bolum21/6-Firebase/cubit/AnasayfaCubit.dart';
import 'package:flutter_proje/Bolum21/6-Firebase/cubit/KisiDetayCubit.dart';
import 'package:flutter_proje/Bolum21/6-Firebase/cubit/KisiKayitCubit.dart';
import 'package:flutter_proje/Bolum21/6-Firebase/views/Anasayfa.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp();

  @override
  Widget build(BuildContext context) {
    return MultiBlocProvider(
      providers: [
        BlocProvider(create: (context)=>KisiKayitCubit()),
        BlocProvider(create: (context)=>KisiDetayCubit()),
        BlocProvider(create: (context)=>AnasayfaCubit()),
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

