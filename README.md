# fastapi-app

* Микросервис, который выводит список файлов и директорий с датой их создания, находящихся в указанной директории. Директория устанавливается в файле ```config.py```

```
WORK_DIR = <директория>
```
* Перед запуском примонтируйте рабочую директорию, указав её в ```docker-compose.yml``` в volumes
* Для запуска выполните команду ```docker-compose up```