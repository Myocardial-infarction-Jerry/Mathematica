# Mathematica 简易学生管理数据库实现

## 项目概述
本项目旨在使用 Wolfram Language 实现一个简易的学生管理数据库。该数据库允许插入学生和课程信息，并提供了一些基本的查询和删除功能。

### 功能列表
- 插入学生信息：`InsertStudent(name, id, courses)`

- 插入课程信息：`InsertCourse(name, code, instructor)`

- 删除学生信息：`DeleteStudent(id)`

- 删除课程信息：`DeleteCourse(code)`

- 查找学生的课程列表：`FindCoursesForStudent(studentID)`

- 查找课程的学生列表：`FindStudentsForCourse(courseCode)`

- 绘制学生和课程的关系图：`DrawGraph`

  <img src="/Users/qiu_nangong/Documents/GitHub/Mathematica/relationship.png"  />

## 代码示例
以下是一些使用示例，展示了如何使用上述功能来操作学生和课程信息：

```mathematica
(* 示例用法 *)
InsertStudent["Alice", 1, {"CS101", "CS102"}] (* 插入学生 *)
InsertStudent["Bob", 2, {"CS101", "CS103"}] (* 插入学生 *)
InsertStudent["Charlie", 3, {"CS102", "CS103"}] (* 插入学生 *)
InsertStudent["David", 4, {"CS101"}] (* 插入学生 *)

InsertCourse["Introduction to Computer Science", "CS101", "Prof. Smith"] (* 插入课程 *)
InsertCourse["Advanced Computer Science", "CS102", "Prof. Johnson"] (* 插入课程 *)
InsertCourse["Data Science", "CS103", "Prof. Brown"] (* 插入课程 *)

FindCoursesForStudent[1] (* 查找学生ID为1的课程列表 *)
FindStudentsForCourse["CS101"] (* 查找课程代码为"CS101"的学生列表 *)

(* 增加更多示例关系 *)
InsertStudent["Eve", 5, {"CS102", "CS103"}] (* 插入学生 *)
InsertStudent["Frank", 6, {"CS101", "CS102", "CS103"}] (* 插入学生 *)
InsertCourse["Machine Learning", "CS104", "Prof. Davis"] (* 插入课程 *)
InsertCourse["Database Management", "CS105", "Prof. Wilson"] (* 插入课程 *)

FindCoursesForStudent[2] (* 查找学生ID为2的课程列表 *)
FindStudentsForCourse["CS103"] (* 查找课程代码为"CS103"的学生列表 *)

(* 绘制学生和课程的关系图 *)
DrawGraph

DeleteStudent[1] (* 删除学生ID为1的学生 *)
DeleteCourse["CS101"] (* 删除课程代码为"CS101"的课程 *)
FindCoursesForStudent[1] (* 再次查找学生ID为1的课程列表，确认学生已被删除 *)
FindStudentsForCourse["CS101"] (* 再次查找课程代码为"CS101"的学生列表，确认课程已被删除 *)
```

## 可扩展性和改进

该项目目前只实现了基本的功能，但可以根据需要进行扩展和改进。以下是一些可能的扩展方向：

- 添加更多的数据字段，如学生的年龄、性别等信息。
- 支持更复杂的查询，如按照课程名称、教师姓名等进行搜索。
- 实现数据的持久化，以便在不同会话中保留数据。
- 添加用户界面，使用户可以通过图形界面进行操作。

通过对项目的扩展和改进，我们可以进一步提升学生管理数据库的功能和易用性。

## 结论

通过本项目，我们成功实现了一个简易的学生管理数据库。该数据库允许插入学生和课程信息，并提供了基本的查询和删除功能。使用这些功能，我们可以方便地管理学生和课程数据。

