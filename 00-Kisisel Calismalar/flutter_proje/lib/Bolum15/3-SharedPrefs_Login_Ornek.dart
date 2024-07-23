import 'package:flutter/material.dart';
import 'package:flutter_proje/Bolum15/3-AnaSayfa.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp();

  Future<bool> oturumKontrol() async{
    var sp=await SharedPreferences.getInstance();

      String spKullaniciAdi=sp.getString("kullaniciAdi") ?? "kullanici adi yok";
      String spSifre=sp.getString("sifre") ?? "sifre yok";

      if(spKullaniciAdi=="admin" && spSifre=="123"){
        return true;
      }
      else{
        return false;
      }
  }
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home:  FutureBuilder<bool>(
        future: oturumKontrol(),
        builder: (context,snapshot){
          if(snapshot.hasData){
            bool? gecisIzni=snapshot.data;
            return gecisIzni ?? false ? AnaSayfa() : LoginEkrani();
          }
          else{
            return Container();
          }
        },
      ),
    );
  }
}

class LoginEkrani extends StatefulWidget {


  @override
  State<LoginEkrani> createState() => _LoginEkraniState();
}

class _LoginEkraniState extends State<LoginEkrani> {

  var tfKullaniciAdi=TextEditingController();
  var tfSifre=TextEditingController();


  Future<void> girisKontrol() async{
    var ka=tfKullaniciAdi.text;
    var s=tfSifre.text;

    if(ka=="admin" && s=="123"){
      var sp=await SharedPreferences.getInstance();

      sp.setString("kullaniciAdi", ka);
      sp.setString("sifre", s);
      Navigator.pushReplacement(context,MaterialPageRoute(builder: (context)=>AnaSayfa()));
    }
    else{
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: Text("Giris Hatali"),
      duration: Duration(seconds: 3),));
      print("Girdi");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Login Ekrani"),
      ),
      body: Builder(
        builder: (context) {
          return Center(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  TextField(
                    controller: tfKullaniciAdi,
                    decoration: InputDecoration(
                      hintText: "Kullanici Adi",
                    ),
                  ),
                  TextField(
                    obscureText: true,
                    controller: tfSifre,
                    decoration: InputDecoration(
                      hintText: "Sifre",
                    ),
                  ),
                  ElevatedButton(
                    child: Text("Giris Yap"),
                    onPressed: (){
                      girisKontrol();
                    },
                  ),
                ],
              ),
            ),
          );
        }
      ),

    );
  }
}
