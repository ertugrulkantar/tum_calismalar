import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/services.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

class VeritabaniYardimcisi{
  static final String veritabaniAdi="rehber.sqlite";

  static Future<Database> veritabaniErisim() async{
    String veritabaniYolu=join(await getDatabasesPath(),veritabaniAdi);

    if(await databaseExists(veritabaniYolu)){
      print("Veritabani zaten var, kopyalamaya gerek yok.");
    }
    else{
      ByteData data=await rootBundle.load("lib/Bolum21/3-SQLite/sqlite/$veritabaniAdi");
      List<int> bytes=data.buffer.asUint8List(data.offsetInBytes,data.lengthInBytes);
      await File(veritabaniYolu).writeAsBytes(bytes,flush:true);
      print("Veritabani kopyalandi");
    }
    return openDatabase(veritabaniYolu);
  }
}