# Скрипт собирает информацию с виртуальных машин.
####  Под информацией подразумевается: данные о системе, сведения об установленных программах, состояние локальных дисков.
0. [Входные параметры](#Входные-параметры)
1. [Структура шаблона bat файла](#Структура-шаблона-bat-файла)
2. [Консольные команды windows (cmd)](#Консольные-команды-windows-(cmd))
3. [Сортировка и слияние](#Сортировка-и-слияние)
### Входные параметры
**run.py** является иницилизирующим скриптов, так-же в данном скрипте необходимо указать параметры учётки и имя вируталок.
**Переменная пути директории.**
Указывем в переменную местоположение папки, по данному пути будут сохранены таблицы.
Перед запуском убедиться, что указанной директорию не существует.
```Python
# При необходимости указать внешнию директорию, два бэк-слэша "\\" в конце обязательны.
directory = f"{os.getcwd()}\\info_about_machines\\"
```
**Переменная в виде списка машин.**
Иницализация списка машин, где будет осуществлён сбор информации.
```Python
nodes = ["v01", "v02", "v03", "v04"]
```
**Переменные полномочий (семья,логин,пароль).**
Подключение к виртуалкам осуществляется через аккаунты обладающим соотвествующими привелегиями доступа.
```Python
family = "family"
user = "name_user"
password = "password_user"
```
___
### Структура шаблона bat файла
***Неотьемлемой*** частью программы, является шаблон - "main.bat".
На основе данного шаблона программа иницилизирует [cmd](https://ab57.ru/cmdlist.html) скрипты 
подставляя в ключевые слова переменные: directory, nodes, family, user, password.
### Команды:
-Служебная команда, отключает выводы служебной информации .
```cmd
@echo 
```
-Инициализирует выводы в кодировке utf-8
```cmd
chcp 65001
```
___
#### Следующие запросы сохраняют файлы в формате *.csv
-Команда: "wmic product get name,version,description,installdate,installlocation" 
возвращает установленные программы.

```cmd
wmic /USER:{FAMILY}\{USER} /PASSWORD:{PASSWORD} /NODE:"{NODE}" /OUTPUT:"{DIRECTORY}{NODE}_product.csv" product get name,version,description,installdate,installlocation /FORMAT:CSV
```

|   |Node     |Description	                                |InstallDate	 |InstallLocation  |Name	                                   |Version   |
|---|--------:|--------------------------------------------:|------------|-----------------|-------------------------------------------|----------|
|0	|v01 |Python 3.7.1 Standard Library (32-bit)       |2019-11-15  |		           |Python 3.7.1 Standard Library (32-bit)	   |3.7.2250.0|
|1	|v02 |Python 3.7.1 Development Libraries (32-bit)  |2019-11-16	 |	               |Python 3.7.1 Development Libraries (32-bit)|3.7.2250.0|
|2	|v03 |Python 3.7.1 pip Bootstrap (32-bit)	        |2019-11-11	 |	               |Python 3.7.1 pip Bootstrap (32-bit)        |3.7.2250.0| 
|.|.|.|.|.|.|.|  
  
 В столбце "InstallLocation" редко содержаться информация об установочной папке. 

-Команда "wmic logicaldisk where drivetype=3 get freespace,deviceid,size" возвращает текущие состояние локальных дисков.
```cmd
wmic /USER:{FAMILY}\{USER} /PASSWORD:{PASSWORD} /NODE:"{NODE}" /OUTPUT:"{DIRECTORY}{NODE}_logicaldisk.csv" logicaldisk where drivetype=3 get freespace,deviceid,size /FORMAT:CSV
```
|	|Node	|DeviceID	|FreeSpace|	Size|
|:---|:---|:---|:------|:---|
|0	|v01	|C:|	100.23128128|	149.9003868|
|1	|v02	|C:|	86.11068726|	149.9003868|
|2	|v03	|C:|	71.60224915|	149.9003868| 
  
  
 FreeSpace,Size указывают значение в гигабайтах.

-Команда "systeminfo" возвращает полные сведения о главных компонентах системы. От железа до операционной системы. 
```cmd
systeminfo /S {NODE} /U {FAMILY}\{USER} /P {PASSWORD} /fo csv > {DIRECTORY}{NODE}_systeminfo.csv
```
|     | Host Name |               OS Name              |             OS Version             |    OS Manufacturer    |  OS Configuration  |    OS Build Type    | Registered Owner | Registered   Organization |        Product ID       | Original Install   Date |   System Boot Time  | System   Manufacturer |   System Model  |  System Type |                                          Processor(s)                                         |                 BIOS Version                | Windows Directory |   System Directory  |       Boot Device       | System Locale |          Input Locale         |                   Time Zone                   | Total Physical   Memory | Available   Physical Memory | Virtual Memory:   Max Size | Virtual Memory:   Available | Virtual Memory:   In Use | Page File   Location(s) |   Domain   |  Logon Server  |
|-----|:---------:|:----------------------------------:|:----------------------------------:|:---------------------:|:------------------:|:-------------------:|:----------------:|:-------------------------:|:-----------------------:|:-----------------------:|:-------------------:|:---------------------:|:---------------:|:------------:|:---------------------------------------------------------------------------------------------:|:-------------------------------------------:|:-----------------:|:-------------------:|:-----------------------:|:-------------:|:-----------------------------:|:---------------------------------------------:|:-----------------------:|:---------------------------:|:--------------------------:|:---------------------------:|:------------------------:|:-----------------------:|:----------:|:----|
|  0  | v01  | Microsoft Windows 7  | 1.1.531 Service Pack 1 Build 7611 | Microsoft Corporation | Workstation | Multiprocessor Free | temp             |                           | 10343-111-512341-15333 | 10/18/2019, 10:58:58    | 1/28/2020, 12:43:21 | Microsoft Corporation | Virtual Machine | x64-based PC | 1 Processor(s) Installed.,[01]: AMD64 Family 6 Model 63 Stepping 2   GenuineIntel ~2297 Mhz | ASUS Inc. 090006 , 5/23/2012 | C:\Windows        | C:\Windows\system32 | \Device\HarddiskVolume1 | ru;Russian    | en-us;English (United States) | (UTC+03:00) Omsk            | 5,120 MB                | 2,643 MB                    | 10,237 MB                  | 7,264 MB                    | 2,973 MB                 | C:\pagefile.sys         | Name.local | \\server001 |
|  1  | v02  | Microsoft Windows 7  | 1.1.531 Service Pack 1 Build 7611 | Microsoft Corporation | Workstation | Multiprocessor Free | temp2            |                           | 10332-112-521341-15243 | 10/18/2019, 11:32:01    | 1/28/2020, 18:58:02  | Microsoft Corporation | Virtual Machine | x64-based PC | 1 Processor(s) Installed.,[01]: AMD64 Family 6 Model 63 Stepping 2   GenuineIntel ~2297 Mhz | ASUS Inc. 090006 , 5/23/2012 | C:\Windows        | C:\Windows\system32 | \Device\HarddiskVolume1 | ru;Russian    | en-us;English (United States) | (UTC+03:00) Volgograd | 4,096 MB                | 2,671 MB                    | 8,189 MB                   | 5,191 MB                    | 2,998 MB                 | C:\pagefile.sys         | Name.local | \\server001 |
|...|...|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|..|

 Столбцы с параметрами сети и виртулиации в текущей таблице не демонстрируется т.к 
длинные и сильно вытягивают в высоту таблицу. 

Подробнее об используемых командах:
Команда [WMIC](https://ab57.ru/cmdlist/wmic.html) (Windows Management Instrumentation Command) 
используется для получения сведений об оборудовании и системе, управления процессами и их компонентами.

Команда [systeminfo](https://ab57.ru/cmdlist/systeminfo.html) отображает сведения о конфигурации операционной системы на локальном или удаленном компьютере, включая уровни пакета обновления.

Ключевые слова: {FAMILY},{USER}, {PASSWORD} ,{NODE}, {DIRECTORY}. 
Переменные к ним: directory, nodes, family, user, password. 
### Сортировка и слияние.
***Вызов*** сортирующий ***функции*** полученных файлов по каталогам: logicaldisk, product, systeminfo
```Python
sort_files.sorf_files(directory)
```
***Функция*** объеденяет таблицы с полученных разных машин в одну единную.
```Python
join_files.join_files(directory)
```
Результатом работы является три excel файла содержащие данные о системе, сведения об установленных программах, 
состояние локальных дисков. Для удобства, рекомендуется при работе в excel установить на первой строке фильтр.
