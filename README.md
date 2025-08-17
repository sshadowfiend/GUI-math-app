# 📡 Анализатор сигналов электрической цепи

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)
![Flet](https://img.shields.io/badge/Flet-GUI%20Framework-success?style=flat-square)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Программный комплекс для анализа сигналов на выходе электрической цепи с графическим интерфейсом. Разработан в рамках курсовой работы по дисциплине "Программирование".

## 🌟 Основные функции

- 📊 Построение графиков входного и выходного сигналов
- ⚡ Расчет длительности импульса сигнала
- 🔍 Анализ сигналов с заданной погрешностью
- 🖥️ Удобный графический интерфейс
- 📈 Автоматическая генерация отчетов в виде изображений

## 🛠 Технологический стек

- **Python 3.8+**
- **Flet** - фреймворк для создания кроссплатформенных GUI-приложений
- **Matplotlib** - библиотека для построения графиков
- **NumPy** - математические вычисления
- **OS/glob** - работа с файловой системой

## 📚 Теоретическая часть

### Постановка задачи
Анализ сигналов с передаточной характеристикой:
Uвых = aUвх²
где:
- Uвх(t) = { U(1-e^(-at)) при t∈[tнач, t1]
            { U(1-e^(-at1))·e^(-b(t-t1)) при t∈(t1, tкон]
- Параметры: tнач=0, tкон=40, t1=20, a=0.25, b=0.75, U=75В

## 📊 Примеры работы
<img width="726" height="585" alt="image" src="https://github.com/user-attachments/assets/cf48431b-8e33-454e-ad6a-9b5d9f55ac71" />
<img width="724" height="583" alt="image" src="https://github.com/user-attachments/assets/0d7ef778-5290-4c62-8333-704ef7df24e6" />
<img width="721" height="585" alt="image" src="https://github.com/user-attachments/assets/333cd812-761c-4c20-8402-c188c16a3bf3" />
