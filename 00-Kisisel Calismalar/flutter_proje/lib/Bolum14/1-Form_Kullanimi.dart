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

  var formKey=GlobalKey<FormState>();
  var tfKullaniciAdi=TextEditingController();
  var tfSifre=TextEditingController();

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
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Form(
                key: formKey,
                child: Column(
                  children: [
                    TextFormField(
                      controller: tfKullaniciAdi,
                      decoration: InputDecoration(hintText: "Kullanici Adi"),
                      validator: (tfgirdisi){
                        if(tfgirdisi!.isEmpty){
                          return "Kullanici Adi Giriniz";
                        }
                        return null;
                      },
                    ),
                    TextFormField(
                      controller: tfSifre,
                      obscureText: true,
                      decoration: InputDecoration(hintText: "Sifre"),
                      validator: (tfgirdisi){
                        if(tfgirdisi!.isEmpty){
                          return "Sifre Giriniz";
                        }
                        if(tfgirdisi.length<6){
                          return "Sifreniz en az 6 haneli olmalidir";
                        }
                        return null;
                      },
                    ),
                    ElevatedButton(
                      child: Text("Giris"),
                      onPressed: (){
                        bool kontrolSonucu=formKey.currentState!.validate();

                        if(kontrolSonucu){
                          String ka=tfKullaniciAdi.text;
                          String s=tfSifre.text;
                          print("Kullanici adi: $ka , Sifre: $s");
                        }
                      },
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),

    );
  }
}
