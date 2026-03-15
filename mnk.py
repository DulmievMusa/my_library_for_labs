import math

def linear_regression(x, y):
    """
    Выполняет линейную регрессию методом наименьших квадратов.
    
    Параметры:
    x, y - списки с координатами точек (должны быть одинаковой длины)
    
    Возвращает:
    k, b, dk, db - коэффициент наклона, смещение и их погрешности
    """
    
    # Проверка входных данных
    if len(x) != len(y):
        raise ValueError("Списки x и y должны иметь одинаковую длину")
    
    n = len(x)
    if n < 2:
        raise ValueError("Необходимо хотя бы 2 точки для регрессии")
    
    # Вычисляем необходимые суммы
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi * xi for xi in x)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    
    # Вычисляем коэффициенты k и b
    denominator = n * sum_x2 - sum_x * sum_x
    if abs(denominator) < 1e-15:
        raise ValueError("Точки лежат на вертикальной прямой или все x одинаковы")
    
    k = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y * sum_x2 - sum_x * sum_xy) / denominator
    
    # Вычисляем погрешности
    # 1. Вычисляем остатки (разности между фактическими и предсказанными значениями)
    residuals = [y[i] - (k * x[i] + b) for i in range(n)]
    
    # 2. Среднеквадратичная ошибка (стандартное отклонение остатков)
    if n > 2:
        s2 = sum(r * r for r in residuals) / (n - 2)
        s = math.sqrt(s2)
    else:
        s = 0.0
    
    # 3. Погрешности коэффициентов
    mean_x = sum_x / n
    var_x = sum((xi - mean_x) ** 2 for xi in x)
    
    if var_x > 0:
        dk = s / math.sqrt(var_x)
        db = s * math.sqrt(sum_x2 / (n * var_x))
    else:
        dk = 0.0
        db = 0.0
    
    return k, b, dk, db

def calculate_r_squared(x, y, k, b):
    """
    Вычисляет коэффициент детерминации R²
    
    Параметры:
    x, y - исходные данные
    k, b - коэффициенты регрессии
    
    Возвращает:
    R² - коэффициент детерминации (от 0 до 1)
    """
    n = len(x)
    
    # Среднее значение y
    y_mean = sum(y) / n
    
    # Общая сумма квадратов
    total_ss = sum((yi - y_mean) ** 2 for yi in y)
    
    # Остаточная сумма квадратов
    residual_ss = sum((y[i] - (k * x[i] + b)) ** 2 for i in range(n))
    
    # Коэффициент детерминации
    if total_ss > 0:
        r2 = 1 - residual_ss / total_ss
    else:
        r2 = 1.0
    
    return r2

def predict(x_val, k, b, dk=None, db=None):
    """
    Предсказывает значение y для заданного x
    
    Параметры:
    x_val - значение x для предсказания
    k, b - коэффициенты регрессии
    dk, db - погрешности коэффициентов (опционально)
    
    Возвращает:
    y_pred - предсказанное значение y
    dy_pred - погрешность предсказания (если переданы dk, db)
    """
    y_pred = k * x_val + b
    
    if dk is not None and db is not None:
        # Погрешность предсказания по формуле распространения ошибок
        dy_pred = math.sqrt((x_val * dk) ** 2 + db ** 2)
        return y_pred, dy_pred
    
    return y_pred

# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    x_data = [1, 2, 3, 4, 5]
    y_data = [2.1, 3.9, 6.2, 8.1, 9.8]
    
    try:
        # Выполняем регрессию
        k, b, dk, db = linear_regression(x_data, y_data)
        
        # Вычисляем R²
        r2 = calculate_r_squared(x_data, y_data, k, b)
        
        print("Результаты линейной регрессии:")
        print(f"Уравнение прямой: y = ({k:.4f} ± {dk:.4f}) * x + ({b:.4f} ± {db:.4f})")
        print(f"Коэффициент детерминации R² = {r2:.4f}")
        print(f"k = {k:.4f} ± {dk:.4f}")
        print(f"b = {b:.4f} ± {db:.4f}")
        
        # Пример предсказания
        x_new = 6
        y_pred, dy_pred = predict(x_new, k, b, dk, db)
        print(f"\nПредсказание для x = {x_new}:")
        print(f"y = {y_pred:.4f} ± {dy_pred:.4f}")
        
        # Вычисление остатков
        residuals = [y_data[i] - (k * x_data[i] + b) for i in range(len(x_data))]
        print(f"\nОстатки: {[f'{r:.4f}' for r in residuals]}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")










def linear_fit(x, y):
    """Минималистичная версия: только k, b и их погрешности"""
    n = len(x)
    Sx = Sy = Sxx = Sxy = 0
    
    for i in range(n):
        Sx += x[i]
        Sy += y[i]
        Sxx += x[i] * x[i]
        Sxy += x[i] * y[i]
    
    D = n * Sxx - Sx * Sx
    k = (n * Sxy - Sx * Sy) / D
    b = (Sy - k * Sx) / n
    
    # Погрешности
    sigma_y = 0
    for i in range(n):
        sigma_y += (y[i] - (k * x[i] + b)) ** 2
    
    sigma_y = math.sqrt(sigma_y / (n - 2)) if n > 2 else 0
    x_mean = Sx / n
    
    S = 0
    for xi in x:
        S += (xi - x_mean) ** 2
    
    sigma_k = sigma_y / math.sqrt(S) if S > 0 else 0
    sigma_b = sigma_y * math.sqrt(Sxx / (n * S)) if S > 0 else 0
    
    return k, b, sigma_k, sigma_b





    