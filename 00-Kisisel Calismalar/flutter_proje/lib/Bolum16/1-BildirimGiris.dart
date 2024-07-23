import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

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
      home:  Anasayfa(),
    );
  }
}

class Anasayfa extends StatefulWidget {
  const Anasayfa({super.key});

  @override
  State<Anasayfa> createState() => _AnasayfaState();
}

class _AnasayfaState extends State<Anasayfa> {

  var flp= FlutterLocalNotificationsPlugin();

  Future<void> kurulum() async{
    var androidAyari= const AndroidInitializationSettings("@mipmap/ic_launcher");
    var iosAyari= const DarwinInitializationSettings();
    var kurulumAyari=InitializationSettings(android: androidAyari,iOS: iosAyari);
    await flp.initialize(kurulumAyari,onDidReceiveBackgroundNotificationResponse: bildirimSecilme);
  }

  Future<void> bildirimSecilme(NotificationResponse notificationResponse) async{
    var payload=notificationResponse.payload;
    if(payload!=null){
      print("Bildirim Secildi : $payload");
    }
  }

  @override
  void initState() {
    super.initState();
    kurulum();
  }

  Future<void> bildirimGoster() async {
    var androidBildirimDetay=const AndroidNotificationDetails(
        "kanal_id",
        "kanal_baslik",
        channelDescription: "kanal aciklama",
        priority: Priority.high,
        importance: Importance.max, );
    var iosBildirimDetay=const DarwinNotificationDetails();
    var bildirimDetay=NotificationDetails(android: androidBildirimDetay,iOS: iosBildirimDetay);
    await flp.show(3, "Baslik", "Icerik", bildirimDetay,payload: "Payload icerik");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Bildirim Kullanimi"),),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            ElevatedButton(onPressed: (){
              bildirimGoster();
            }, child: const Text("Bildirim Olustur")),
            ElevatedButton(onPressed: (){

            }, child: const Text("Bildirim Olustur (Gecikmeli)")),
          ],
        ),
      ),
    );
  }
}
