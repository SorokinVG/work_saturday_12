def get_mask_card_number(card_number: str) -> str:
    """
    Функция, которая принимает на вход номер карты и возвращает его маску
    :param card_number: строка
    """
    clean_number = card_number.replace(" ", "")
    length = len(clean_number)
    result = ""
    char_count = 0  # Счетчик для добавления пробелов

    for i in range(length):
        # Проверяем, нужно ли скрыть символ
        if i < 6 or i >= length - 4:
            result += clean_number[i]
        else:
            result += "*"
        char_count += 1
        # Добавляем пробел после каждого 4-го элемента
        if char_count == 4 and i != length - 1:
            result += " "
            char_count = 0
    return result


def get_mask_account(account_number: str) -> str:
    """
    Функция, которая принимает на вход номер счета и возвращает его маску
    :param account_number: строка
    """
    clean_number = account_number.replace(" ", "")
    return f"**{clean_number[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
