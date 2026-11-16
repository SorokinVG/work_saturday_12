import re

def extract_names (filename):
    names_list = []
    try:
        #Открываем файл с поддержкой разных языков (кодировка utf-8)
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = re.sub(r'[\d\W_]+', ' ', line)
                cleaned_line = cleaned_line.strip()
                if cleaned_line:
                    names_list.append(cleaned_line)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
        return []

    return names_list


print (extract_names("names.txt"))