import 'package:flutter/material.dart';

class Sayfa1 extends StatelessWidget {
  const Sayfa1({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Stateless Sayfa"),
      ),
      body: Center(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Merhaba"),
            ],
          ),
        ),
      ),

    );
  }
}