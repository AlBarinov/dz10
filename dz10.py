import pandas as pd
import random

# Генерация DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

# Создаем кросс-таблицу
cross_tab = pd.crosstab(index=data['whoAmI'], columns='count')

# Объединяем с исходным DataFrame
data_one_hot = pd.concat([data, pd.get_dummies(data['whoAmI'], prefix='whoAmI')], axis=1)

# Удаляем избыточный столбец
data_one_hot.drop(columns='whoAmI', inplace=True)

# Выводим результат
data_one_hot.head()