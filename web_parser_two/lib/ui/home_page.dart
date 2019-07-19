import 'package:flutter_web/material.dart';
import 'package:web_parser_two/data/Task.dart';
import 'dart:js' as js;
import 'package:http/http.dart' as http;
import 'package:web_parser_two/ui/auth_page.dart';
import 'dart:convert';
import 'dart:html';
import 'dart:async';
import 'package:web_parser_two/link.dart';
import 'package:intl/intl.dart';

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return HomePage();
  }
}

class HomePage extends StatefulWidget {
  @override
  State createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final url = TextEditingController();
  final email = TextEditingController();
  List<Task> task_list = [];
  final exit = TextEditingController();
  bool _loading = false;

  Future _exitProfile() async {
    final Storage _localStorage = window.localStorage;
    _localStorage.remove('username');
    _localStorage.remove('token');
  }

  Future deleteTask(id, position) async {
    final response = await http.delete('http://${link}/api/task/${id}/',
        headers: {'Authorization': 'token ${window.localStorage['token']}'});

    if (response.statusCode > 204) {
      throw Exception('При запросе произошла ошибка');
    } else {
      this.setState(() {
        this.task_list.removeAt(position);
      });
    }
  }

  Future<Task> setTask(id, {email, url}) async {
    var obj = {};

    obj['id'] = id;

    if (email != null) {
      obj['email'] = email;
    }

    if (url != null) {
      obj['url'] = url;
    }

    final response = await http.put('http://${link}/api/task/',
        headers: {
          "Content-Type": "application/json",
          'Authorization': 'token ${window.localStorage['token']}'
        },
        body: json.encode(obj));

    if (response.statusCode > 204) {
      throw Exception('При запросе произошла ошибка');
    } else {
      return Task.fromJson(json.decode(response.body));
    }
  }

  Future<Task> setTaskActive(active, task_id) async {
    var obj = {};

    obj['active'] = active;
    obj['id'] = task_id;

    final response = await http.put('http://${link}/api/task/',
        headers: {
          "Content-Type": "application/json",
          'Authorization': 'token ${window.localStorage['token']}'
        },
        body: json.encode(obj));

    if (response.statusCode > 204) {
      throw Exception('При запросе произошла ошибка');
    } else {
      return Task.fromJson(json.decode(response.body));
    }
  }

  Future<Task> addTask() async {
    var obj = {};

    obj['email'] = this.email.text.toLowerCase();
    obj['url'] = this.url.text.toLowerCase();

    this.email.clear();
    this.url.clear();

    final response = await http.post('http://${link}/api/task/',
        headers: {
          "Content-Type": "application/json",
          'Authorization': 'token ${window.localStorage['token']}'
        },
        body: json.encode(obj));

    if (response.statusCode > 204) {
      throw Exception('При запросе произошла ошибка');
    } else {
      return Task.fromJson(json.decode(response.body));
    }
  }

  List<Task> parseTask(String responseBody) {
    final parsed = json.decode(responseBody).cast<Map<String, dynamic>>();

    return parsed.map<Task>((json) => Task.fromJson(json)).toList();
  }

  Future<List<Task>> fetchTask() async {
    final response = await http.get('http://${link}/api/task/',
        headers: {'Authorization': 'token ${window.localStorage["token"]}'});

    return compute(parseTask, response.body);
  }

  @override
  void initState() {
    super.initState();
    fetchTask().then((tasks) => {
          this.setState(() {
            task_list.addAll(tasks);
          })
        });
  }

  void _setLoading() {
    this.setState(() {
      _loading = !_loading;
    });
  }

  @override
  void dispose() {
    url.dispose();
    email.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Card(
            child: Container(
          padding: EdgeInsets.all(8),
          child: Column(
            children: <Widget>[
              Row(
                children: <Widget>[
                  Expanded(
                      child: Align(
                    alignment: Alignment.centerLeft,
                    child: Text(
                      'Логин: ${window.localStorage['username']}',
                      style:
                          TextStyle(fontWeight: FontWeight.w500, fontSize: 18),
                    ),
                  )),
                  Expanded(
                      child: Align(
                    alignment: Alignment.centerRight,
                    child: MaterialButton(
                        child: Text('Выход'),
                        onPressed: () {
                          if (!_loading) {
                            _exitProfile().then((value) => {
                                  _setLoading(),
                                  Navigator.pushReplacement(
                                      context,
                                      MaterialPageRoute(
                                          builder: (context) => AuthPage()))
                                });
                          }
                          ;
                        }),
                  ))
                ],
              ),
            ],
          ),
        )),
        Card(
            child: Container(
          padding: EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Center(
                child: Text(
                  'Создание задач',
                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.w700),
                ),
              ),
              Container(
                margin: EdgeInsets.fromLTRB(32, 8, 32, 0),
                child: TextField(
                  controller: url,
                  decoration: InputDecoration(labelText: 'Ссылка на kolesa.kz'),
                ),
              ),
              Container(
                margin: EdgeInsets.fromLTRB(32, 0, 32, 8),
                child: TextField(
                  controller: email,
                  decoration: InputDecoration(labelText: 'Электронная почта'),
                ),
              ),
              SizedBox(
                  width: double.infinity,
                  child: MaterialButton(
                      child: Text('Добавить задачу'),
                      onPressed: () {
                        addTask().then((task) => {
                              this.setState(() {
                                task_list.add(task);
                              })
                            });
                      }))
            ],
          ),
        )),
        Expanded(
            child: Card(
                child: Container(
          padding: EdgeInsets.all(16.0),
          child: Column(
            children: <Widget>[
              Center(
                child: Text(
                  'Список задач',
                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.w700),
                ),
              ),
              Expanded(
                  child: ListView.builder(
                      itemCount: task_list.length,
                      padding: const EdgeInsets.all(15.0),
                      itemBuilder: (context, position) {
                        return Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: <Widget>[
                            Divider(height: 5.0),
                            ListTile(
                              title: Text(
                                  '${task_list[position].email} ⋯ ${DateFormat('yyyy-MM-dd').format(DateTime.parse(task_list[position].date))}'),
                              subtitle: Text(task_list[position].url),
                              trailing: Switch(
                                  value: task_list[position].active,
                                  onChanged: (active) {
                                    setTaskActive(
                                            active, task_list[position].id)
                                        .then((v) => {
                                              this.setState(() {
                                                task_list[position].active =
                                                    !task_list[position].active;
                                              })
                                            });
                                  }),
                              onTap: () {
                                final url_local = TextEditingController(
                                    text: task_list[position].url);
                                final email_local = TextEditingController(
                                    text: task_list[position].email);

                                showDialog(
                                  context: context,
                                  builder: (BuildContext context) {
                                    // return object of type Dialog
                                    return AlertDialog(
                                      title: Text("Редактирование задачи"),
                                      content: SizedBox(
                                        child: Column(
                                          mainAxisSize: MainAxisSize.min,
                                          children: <Widget>[
                                            Container(
                                              margin: EdgeInsets.fromLTRB(
                                                  8, 8, 8, 0),
                                              child: TextField(
                                                controller: url_local,
                                                decoration: InputDecoration(
                                                    labelText:
                                                        'Ссылка на kolesa.kz'),
                                              ),
                                            ),
                                            Container(
                                              margin: EdgeInsets.all(8),
                                              child: TextField(
                                                controller: email_local,
                                                decoration: InputDecoration(
                                                    labelText:
                                                        'Электронная почта'),
                                              ),
                                            )
                                          ],
                                        ),
                                      ),
                                      actions: <Widget>[
                                        // usually buttons at the bottom of the dialog
                                        FlatButton(
                                          child: Text("Изменить"),
                                          onPressed: () {
                                            setTask(task_list[position].id,
                                                    email: email_local.text,
                                                    url:url_local.text)
                                                .then((task) => {
                                                      this.setState((){task_list[position] = task;})
                                                    });
                                            Navigator.of(context).pop();
                                          },
                                        ),
                                        FlatButton(
                                          child: Text("Удалить"),
                                          onPressed: () {
                                            deleteTask(task_list[position].id,
                                                position);
                                            Navigator.of(context).pop();
                                          },
                                          textColor: Colors.red,
                                        ),
                                        FlatButton(
                                          child: Text("Отменить"),
                                          onPressed: () {
                                            Navigator.of(context).pop();
                                          },
                                          textColor: Colors.black54,
                                        ),
                                      ],
                                    );
                                  },
                                );
                              },
                            ),
                          ],
                        );
                      }))
            ],
          ),
        )))
      ],
    );
  }
}
