from src.mascs import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(data_string: str) -> str:
    """
    Принимает строку с типом и номером карты или счета.
    Возвращает строку с замаскированным номером.
    """
    # Разделяет строку по пробелам
    parts = data_string.split()

    # Последний элемент - это всегда номер
    number = parts[-1]

    # Все остальное (кроме последнего элемента) - это название/тип
    # Соединяем обратно через пробел
    prefix = " ".join(parts[:-1])

    # Проверяем, является ли это счетом (по слову "Счет" или "Счёт")
    if "Счёт" in prefix or "Счет" in prefix:
        # Если счет - используем маскироку для счетов
        masked_number = get_mask_account(number)
    else:
        # Во всех остальных случаях (Visa, Maestro, MasterCard и т.д.)
        masked_number = get_mask_card_number(number)

    # Возвращаем склееную строку
    return f"{prefix} {masked_number}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счёт 72654108430136874305"))


def get_date(date_string: str) -> str:
    """
        Принимаем строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")
    """

    # Преобразуем строку в объект datetime
    dt = datetime.fromisoformat(date_string)

    # Форматируем дату в нужный вид
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":
    test_date = "2024-03-11T02:26:18.671407"
    print(get_date(test_date))
