import 'package:flutter/material.dart';

class SayfaA_9 extends StatefulWidget {
  const SayfaA_9({super.key});

  @override
  State<SayfaA_9> createState() => _SayfaA_9State();
}

class _SayfaA_9State extends State<SayfaA_9> {

  @override
  void deactivate() {
    super.deactivate();
    print("Sayfa A: deactive() çalıştı.");
  }

@override
  void dispose() {
    super.dispose();
    print("Sayfa A: dispose() çalıştı.");
}
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Sayfa A"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [

          ],
        ),
      ),

    );
  }
}
