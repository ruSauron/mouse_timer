# mouse_timer
Windows console timer that auto-resets when the mouse enters a target screen area

# Mouse Auto-Reset Console Timer

A simple Windows console timer that resets when the mouse cursor enters a specified screen area. Designed to track the last interaction with a button or other elements in third-party programs.

## Features

* **Multi-Monitor Support**: Enables Windows DPI awareness (`shcore` / `user32`) for accurate global cursor coordinate tracking.
* **Target Reset Zone**: Automatically resets the timer when the cursor enters a designated region defined by center coordinates and a pixel tolerance.
* **Drift-Free Timing**: Calculates elapsed time using system monotonic timestamps (`time.monotonic()`) to prevent time drift at higher polling frequencies.
* **Adaptive Terminal Rendering**: Safely formats and pads output based on the current terminal width to prevent line wrapping glitches when resizing the window.
* **Window Title Mirroring**: Optional toggle to mirror the active timer status directly into the console window title bar.

## Requirements

* **OS**: Windows (uses native `ctypes` bindings)
* **Python**: 3.10+

## Usage

1. Configure parameters inside `mouse_timer.py`:
```python
TARGET_X = 100          # Target X coordinate
TARGET_Y = 240          # Target Y coordinate
TOLERANCE = 30          # Region tolerance in pixels (±TOLERANCE)
CHECK_INTERVAL_MS = 500 # Polling frequency in milliseconds
ENABLE_WINDOW_TITLE = True  # Duplicate timer to window title bar

```


2. Run the script:
```bash
python mouse_timer.py

```


3. Press `Ctrl+C` to stop the program.

Made in Gemini

---

# Консольный таймер с автосбросом по мыши

Простенький консольный секундомер для Windows, который автоматически сбрасывается при попадании курсора мыши в заданную область экрана. Сделан для отслеживания последнего взаимодействия с кнопкой или другим элементов в сторонних программах

## Особенности

* **Поддержка нескольких мониторов**: Активирует системный DPI Awareness (`shcore` / `user32`) для точного считывания глобальных координат мыши.
* **Зона автосброса**: Сбрасывает отсчет при попадании курсора в целевой квадрат (задается координатами центра и допуском в пикселях).
* **Точность времени**: Считает прошедшее время по разнице системных меток (`time.monotonic()`), исключая рассинхрон при высокой частоте опроса.
* **Адаптивный вывод**: Динамически подрезает и дополняет строку под текущую ширину окна консоли, предотвращая сбои разметки при изменении размера терминала.
* **Заголовок окна**: Настраиваемый флаг для дублирования текущего времени таймера в заголовок окна консоли.

## Требования

* **Операционная система**: Windows (используются вызовы `ctypes`)
* **Python**: 3.10 или выше

## Использование

1. Задайте параметры в начале файла `mouse_timer.py`:
```python
TARGET_X = 100          # Целевая координата X
TARGET_Y = 240          # Целевая координата Y
TOLERANCE = 30          # Допуск в пикселях (±TOLERANCE)
CHECK_INTERVAL_MS = 500  # Частота проверки в миллисекундах
ENABLE_WINDOW_TITLE = True  # Дублировать таймер в заголовок окна

```


2. Запустите скрипт:
```bash
python mouse_timer.py

```


3. Нажмите `Ctrl+C` для завершения работы.

Скрипт сделан Gemini
