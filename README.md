## Проект API автотестов на тестовый магазин shop.bugred
![This is an image](resources/images/shop.png)

<h3> Список реализованных проверок:</h3>

* Создание товара
* Получение информации по созданному товару с помощью ID
* Обновление информации по созданному товару с помощью ID
* Поиск карточек товара
* Удаление созданного товар с помощью ID
  
----
### Используется:
<p  align="center">
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="resources/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="resources/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="resources/logo/tg.png"></code>
</p>

----
### Локальный запуск

> Для локального запуска необходимо выполнить команду в СLI:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/
```

> Получение Allure отчета
```bash
allure serve allure-results/
```

----
### <img width="5%" title="Jenkins" src="resources/logo/jenkins.png"> Запуск проекта в Jenkins

### [Jenkins](https://jenkins.autotests.cloud/job/python_project_okko.tv/)

#### При нажатии на "Build with Parameters" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide
![This is an image](resources/images/jenkins.png)

<!-- Allure report -->

### <img width="5%" title="Allure Report" src="resources/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/python_project_okko.tv/18/allure/)
#### Результаты тестов в Allure отчете
![This is an image](resources/images/results.png)

#### Список тест кейсов
![This is an image](resources/images/test.png)

#### Пример отчета о прохождении api-теста
![This is an image](resources/images/test_example.png)

