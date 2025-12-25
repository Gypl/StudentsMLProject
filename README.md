# Student Grades API
REST-сервис на FastAPI для загрузки CSV-файлов с успеваемостью студентов, сохранения данных в PostgreSQL и выполнения аналитических запросов.

## API эндпоинты
### POST /upload-grades
Загрузка CSV-файла.

Response
```
{
  "status": "ok",
  "records_loaded": 2000,
  "students": 40
}
```


### GET /students/more-than-3-twos

Студенты, у которых оценка 2 встречается больше 3 раз

Response
```
[
  {
    "full_name": "Иванов Иван",
    "count_twos": 5
  }
]
```


### GET /students/less-than-5-twos
Студенты, у которых оценка 2 встречается меньше 5 раз


Response
```
[
  {
    "full_name": "Петров Пётр",
    "count_twos": 2
  }
]
```

# Запуск проекта (Docker)
Клонировать репозиторий 
Для успешного запуска контейнера должны быть свободны порты 5432 для postgreSQL и 8000 для api.
```
git clone https://github.com/Gypl/StudentsMLProject.git
cd StudentsMLProject
docker-compose up --build
```

# Проверка через Postman
POST /upload-grades

Method: POST

URL: http://localhost:8000/upload-grades

Body → form-data

| Key  | Type | Value               |
| ---- | ---- | ------------------- |
| file | File | students_grades.csv |
