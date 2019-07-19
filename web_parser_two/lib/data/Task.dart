class Task {
  int id;
  String url;
  bool active;
  String email;
  String date;
  int user;

//  final String data;

  Task({this.id, this.url, this.active, this.email, this.date, this.user});

  factory Task.fromJson(Map<String, dynamic> json) {
    return Task(
        id: json['id'],
        url: json['url'],
        active: json['active'],
        email: json['email'],
        user: json['user'],
        date: json['date']);
  }
}
