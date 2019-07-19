import 'package:flutter_web/material.dart';
import 'ui/auth_page.dart';
import 'ui/home_page.dart';
import 'dart:html';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {

  Widget getMainWidget(){
    if (window.localStorage['token'] != null){
      return HomePage();
    } else {
      return AuthPage();
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(primarySwatch: Colors.blue),
      home: getMainWidget(),
    );
  }
}