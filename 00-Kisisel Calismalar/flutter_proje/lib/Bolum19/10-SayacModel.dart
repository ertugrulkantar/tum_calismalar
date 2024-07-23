import 'package:mobx/mobx.dart';

part '10-SayacModel.g.dart';

class SayacModel=SayacModelBase with _$SayacModel;

abstract class SayacModelBase with Store{
  @observable
  int sayac=0;

  @action
  void sayacArttir(){
    sayac++;
  }

  @action
  void sayacAzalt(int miktar){
    sayac-=miktar;
  }
}