# Імпортуємо бібліотеки
import numpy as np
import pandas as pd

# Створюємо двовимірний масив
# І заповнюємо перший стовпчик масиву випадковими числами у діапазоні [1, 20]
data = np.random.randint(1, 21, size=(10, 1))
df = pd.DataFrame(data, columns=['Column1'])

# Замінюємо повтори в першому стовпчику на випадкові числа в діапазоні [-10, -1]
df['Column1'] = np.where(df.duplicated('Column1'), np.random.randint(-10, 0), df['Column1'])

# Заповнюємо 2, 3 і 4 стовпчики відповідно 2, 3 і 4 степенями значень, які містяться в 1 стовпчику
df['Column2'] = df['Column1']**2
df['Column3'] = df['Column1']**3
df['Column4'] = df['Column1']**4

print(df)

# Зберігаємо утворений масив у файл array.csv
df.to_csv('array.csv', index=False)