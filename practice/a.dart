import 'dart:io';
import 'dart:collection';

class A {
  void speck() {
    print("Speak");
  }
}

class B {}

class C {}

class D implements A, B, C {
  
  @override
  void speck() {
    // TODO: implement speck
    print("object B");
  }
}

void main(List<String> args) {
  var d = D();
  d.speck();
}
