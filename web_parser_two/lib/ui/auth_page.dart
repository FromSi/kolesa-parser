import 'package:flutter_web/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';
import 'dart:html';
import 'package:web_parser_two/data/Token.dart';
import 'home_page.dart';
import 'package:web_parser_two/link.dart';

class AuthPage extends StatelessWidget {
  const AuthPage({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: _AuthView(),
      ),
    );
  }
}

class _AuthView extends StatefulWidget {
  @override
  State createState() => _AuthViewState();
}

class _AuthViewState extends State<_AuthView> {
  final username = TextEditingController();
  final password = TextEditingController();
  bool _loading = false;

  @override
  void dispose() {
    username.dispose();
    password.dispose();
    super.dispose();
  }

  void _setLoading() {
    this.setState(() {
      _loading = !_loading;
    });
  }

  Future fetchToken(bool auth) async {
    if (username.text.isNotEmpty && password.text.isNotEmpty) {
      final Storage _localStorage = window.localStorage;
      var response;

      if (auth) {
        response = await http.post('http://${link}/api/auth/',
            headers: {"Content-Type": "application/json"},
            body: json.encode(
                {'username': username.text.toLowerCase(), 'password': password.text.toLowerCase()}));
      } else {
        response = await http.post('http://${link}/api/register/',
            headers: {"Content-Type": "application/json"},
            body: json.encode(
                {'username': username.text.toLowerCase(), 'password': password.text.toLowerCase()}));
        if (response.statusCode == 201) {
          response = await http.post('http://${link}/api/auth/',
              headers: {"Content-Type": "application/json"},
              body: json.encode(
                  {'username': username.text.toLowerCase(), 'password': password.text.toLowerCase()}));
        }
      }

      if (response.statusCode == 200) {
        String token = Token.fromJson(json.decode(response.body)).token;
        _localStorage['token'] = token;
        _localStorage['username'] = username.text.toLowerCase();
      } else {
        throw Exception('При запросе произошла ошибка');
      }
    } else {
      throw Exception('Не заполнены поля');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
        child: Container(
      width: 400,
      height: 250,
      padding: EdgeInsets.all(16.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Center(
            child: Text(
              'Авторизация и регистрация',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.w700),
            ),
          ),
          Container(
            margin: EdgeInsets.fromLTRB(32, 8, 32, 0),
            child: TextField(
              controller: username,
              decoration: InputDecoration(labelText: 'Логин'),
            ),
          ),
          Container(
            margin: EdgeInsets.fromLTRB(32, 0, 32, 8),
            child: TextField(
              controller: password,
              decoration: InputDecoration(labelText: 'Пароль'),
            ),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              MaterialButton(
                  child: Text('Авторизация'),
                  onPressed: () {
                    if (!_loading) {
                      _setLoading();

                      fetchToken(true)
                          .then((value) => {
                                _setLoading(),
                                Navigator.pushReplacement(
                                    context,
                                    MaterialPageRoute(
                                        builder: (context) => HomePage()))
                              })
                          .catchError((error) => {
                                _setLoading(),
                                Scaffold.of(context).showSnackBar(
                                    SnackBar(content: Text(error.toString())))
                              });
                    }
                    ;
                  }),
              MaterialButton(
                  child: Text('Регистрация'),
                  onPressed: () {
                    if (!_loading) {
                      _setLoading();

                      fetchToken(false)
                          .then((value) => {
                                _setLoading(),
                                Navigator.pushReplacement(
                                    context,
                                    MaterialPageRoute(
                                        builder: (context) => HomePage()))
                              })
                          .catchError((error) => {
                                _setLoading(),
                                Scaffold.of(context).showSnackBar(
                                    SnackBar(content: Text(error.toString())))
                              });
                    }
                  }),
              Container(
                margin: EdgeInsets.fromLTRB(8, 0, 0, 0),
                width: 24,
                height: 24,
                child: Visibility(
                    child: CircularProgressIndicator(), visible: _loading),
              )
            ],
          )
        ],
      ),
    ));
  }
}
