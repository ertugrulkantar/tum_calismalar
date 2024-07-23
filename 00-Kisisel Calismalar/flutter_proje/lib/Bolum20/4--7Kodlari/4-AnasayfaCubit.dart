import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_proje/Bolum20/4--7Kodlari/7-MatematikRepo.dart';

class AnasayfaCubit extends Cubit<int>{
  AnasayfaCubit() : super(0);

  var mrepo=MatematikRepository();

  void toplamaYap(String alinanSayi1,String alinanSayi2){
    emit(mrepo.topla(alinanSayi1, alinanSayi2));
  }

  void carpmaYap(String alinanSayi1,String alinanSayi2){
    emit(mrepo.carp(alinanSayi1, alinanSayi2));

  }
}