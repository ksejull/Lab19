# Імпортуємо бібліотеку
import pandas as pd

# Перевіряємо на помилки
try:
    # Зчитуємо дані з файла mas.txt 
    with open('mas.txt', 'r', encoding='utf-8') as file:
        # Розділяємо строку на числа використовуючи пробіл як розділювач
        data = [int(num) for line in file for num in line.split()]
           
    # Записуємо дані в одновимірний масив Series
    series_data = pd.Series(data, name='Data')
    print('Зчитано з файлу: ')
    print(series_data)

    # Видаляємо повтори чисел
    unique_series = series_data.drop_duplicates()
    print('Масив після видалення повторів')
    print(unique_series)

    # Зберігаємо утворений масив у фал JSON
    unique_series.to_json('result.json', orient='values')

    print('Утворений масив збережено уфайл result.json.')
except FileNotFoundError:
    print('Файл mas.txt не знайдено.')
except Exception as e:
    print(f"Сталася помилка : {e}")        
        