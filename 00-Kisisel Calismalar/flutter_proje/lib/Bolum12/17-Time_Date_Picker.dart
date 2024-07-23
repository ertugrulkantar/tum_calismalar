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

  var tfTarih=TextEditingController();
  var tfSaat=TextEditingController();

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
            TextField(
              controller: tfSaat,
              decoration: InputDecoration(
                hintText: "Saat giriniz"
              ),
              onTap: (){
                showTimePicker(
                  context: context,
                  initialTime: TimeOfDay.fromDateTime(DateTime.now()),
                ).then((alinanSaat){
                  setState(() {
                    tfSaat.text="${alinanSaat!.hour}:${alinanSaat.minute}";
                  });
                });
              },
            ),
            TextField(
              controller: tfTarih,
              decoration: InputDecoration(
                  hintText: "Tarih giriniz"
              ),
              onTap: (){
                showDatePicker(
                  context: context,
                  initialDate: DateTime.now(),
                  firstDate: DateTime(2000),
                  lastDate: DateTime(2050),
                ).then((alinanTarih){
                  setState(() {
                    tfTarih.text="${alinanTarih!.day}/${alinanTarih.month}/${alinanTarih.year}";
                  });
                });
              },
            ),
          ],
        ),
      ),

    );
  }
}
