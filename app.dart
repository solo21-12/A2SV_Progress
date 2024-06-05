import 'dart:io';

Future<void> longRunningOperation() async {
  for (int i = 0; i < 5; i++) {
    await Future.delayed(Duration(seconds: 3));
    print("index: $i");
  }
}

Future<String> fetachData() async {
  await Future.delayed(Duration(seconds: 1));
  return "Data fetched";
}

main() async {
  print("start of long running operation");
  longRunningOperation();

  print("continuing main body");
  for (int i = 10; i < 15; i++) {
    sleep(Duration(seconds: 3));
    print("index from main: $i");
  }
  print("end of main");

  // var data = fetachData();
  // (data.then((value) => print(value)));
  // print("Taske completed");
}


// start of long running operation
// index 0 1 2 3 4
// continuing main body

// index from main
// end of main

class a{}
class c{}
class b implements a, c{}