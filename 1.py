import time

start = time.time()  # Время начала эксперимента!)


def sleeping(n):
    # {time.time() - start:.4f} - время от начала работы программы до текущего момента.
    # :.4f - ограничение количества знаков после запятой (4).
    print(f"Начало выполнения длительной операции № {n}: {time.time() - start:.4f}")
    time.sleep(1)  # Имитация операции длительностью в 1 секунду.
    print(f"Длительная операция № {n} завершена")


def main():
    # Запускаю 30 операций.
    all_results = [sleeping(i) for i in range(1, 31)]
    print(f"Выполнено {len(all_results)} операций.")
    print(f"Программа завершена за {time.time() - start:.4f}")

# Запуск главной функции.
main()