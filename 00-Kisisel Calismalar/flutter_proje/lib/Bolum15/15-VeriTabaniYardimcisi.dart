import 'dart:io';
import 'package:flutter/services.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

class VeritabaniYardimcisi{

  static  final String veriTabaniAdi="rehber.sqlite";

  static Future<Database> veritabaniErisim() async{
    String veritabaniYolu=join(await getDatabasesPath(),veriTabaniAdi);

    if(await databaseExists(veritabaniYolu)){
      print("Veritabanı zaten var. Kopyalamaya gerek yok.");
    }
    else{
      ByteData data=await rootBundle.load("lib/Bolum15/veritabani/$veriTabaniAdi");
      List<int> bytes=data.buffer.asUint8List(data.offsetInBytes,data.lengthInBytes);
      await File(veritabaniYolu).writeAsBytes(bytes,flush: true);
      print("Veritabani kopyalandi");
    }
    return openDatabase(veritabaniYolu);
  }

}