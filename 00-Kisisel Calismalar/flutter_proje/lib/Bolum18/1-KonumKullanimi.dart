import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:permission_handler/permission_handler.dart';

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
  void initState() {
    // TODO: implement initState
    super.initState();
    konumIzinKontrol();
  }
  double enlem=0.0;
  double boylam=0.0;

  Future<void> konumIzinKontrol() async {
    var status = await Permission.location.status;

    if (status != PermissionStatus.granted) {
      await Permission.location.request();
      // İzin istendi ve kullanıcı onayladı veya reddetti.
      // İzin durumunu tekrar kontrol edebilir ve gerekli işlemleri yapabilirsiniz.
    }
  }

  Future<void> konumBilgisiAl() async{
    var konum=await Geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.high);
    setState(() {
      enlem=konum.latitude;
      boylam=konum.longitude;
    });
  }

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
            Text("Enlem: $enlem",style: TextStyle(fontSize: 30),),
            Text("Boylam: $boylam",style: TextStyle(fontSize: 30),),
            ElevatedButton(
              child: Text("Boylam Bilgisi Al"),
              onPressed: (){
                konumBilgisiAl();
              },
            ),
          ],
        ),
      ),

    );
  }
}
