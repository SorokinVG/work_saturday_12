import re
import os


# функция из задачи 2
def extract_names(filename):
    names_list = []
    try:
        # Создаем папку data, если ее еще нет
        os.makedirs("data", exist_ok=True)
        os.chdir("data")
        # Открываем файл с поддержкой разных языков (кодировка utf-8)
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                # Заменяем цифры и знаки препинания на пробел
                cleaned_line = re.sub(r"[\d\W_]+", " ", line)
                cleaned_line = cleaned_line.strip()
                if cleaned_line:
                    names_list.append(cleaned_line)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
        return []

    return names_list


# задача 3
def separate_names(names_list):
    """Разделяет список на русские и английские имена."""
    russian_names = []
    english_names = []
    for name in names_list:
        # Проверяем наличие кириллицы (русский)
        if re.search(r"[А-Яа-яЁё]", name):
            russian_names.append(name)
        # Проверяем наличие латиницы (английский)
        elif re.search(r"[A-Za-z]", name):
            english_names.append(name)

    return russian_names, english_names


def save_sorted_to_file(names, filename):
    """Сортирует имена и сохраняет их в файл в папке data/."""
    # Создаем папку data, если ее еще нет
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, "data")

    # Сортируем по алфавиту (без учета регистра)
    sorted_names = sorted(names, key=str.lower)

    filepath = os.path.join(data_dir, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        for name in sorted_names:
            file.write(f"{name}\n")
    print(f"Файл сохранен: {filepath}")


# ---Основная программа ---
if __name__ == "__main__":
    source_file = "names.txt"

    # 1.Получаем очищенные имена
    all_names = extract_names(source_file)

    # 2 Разделяем их на две группы
    ru_names, en_names = separate_names(all_names)

    # 3 Сортируем и сохраняем в папку data/
    save_sorted_to_file(ru_names, "russian_names.txt")
    save_sorted_to_file(en_names, "english_names.txt")
