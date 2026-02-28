import argparse
import sys
from collections import defaultdict, Counter


# Парсер аргументів з CMD
def parse_arguments():
    try:
        parser = argparse.ArgumentParser(description="Обробка файлів логів.")
        parser.add_argument('file_path', type=str, help="Шлях до файлу логів")                # cmd аргумент ( ОБОВЯЗКОВИЙ )
        parser.add_argument('log_level', type=str, help="Рівень логування", nargs='?')        # cmd аргумент ( ОПЦІЙНИЙ )
        return parser.parse_args()
    except SystemExit as e:
        print(f"Script was interrupted due to the following errors: --- {e}")
        return None

# Розпаковка файла
def load_logs(file_path : str) -> list:
    try:
        content = []
        with open(file_path) as file:
            for line in file:
                if line.strip():
                    parsed_line = parse_log_line(line)
                    content.append(parsed_line)
        return content
    except FileNotFoundError as e:
        print(f"Script was interrupted due to the following errors: --- {e}")
        return []

# Лінійний парсер line, використовується в  [ def load_logs ]
def parse_log_line(line : str) -> dict:
    parsed_info = defaultdict(str)                             # Використовуємо str для збереження значень
    info = line.split(" ")
    try:
        parsed_info["date"] = info[0]                              # Дата
        parsed_info["time"] = info[1]                              # Час
        parsed_info["log_level"] = info[2]                         # Рівень логування
        parsed_info["log_message"] = " ".join(info[3:]).strip()    # Повідомлення
        return parsed_info
    except IndexError as e:
        print(f"Script was interrupted due to the following errors: --- {e}\nVerify the log file!")
        return sys.exit()

# Можливість вибірки інформації згідно з рівнем логування
def filter_logs_by_level(logs: list, level: str) -> list:
    if level:
        filtered_logs = [log for log in logs if log["log_level"] == level.upper()]
        return filtered_logs
    else:
        return logs

# Рахує кількість повідомлень для кожного рівня логування
def count_logs_by_level(logs: list) -> dict:
    counts = Counter(log["log_level"] for log in logs)
    return counts

# Побудова таблички
def display_log_counts(counts: dict):
    header_1 = "Рівень логування"
    header_2 = "Кількість"
    header = header_1 + " | " + header_2
    dividing_line = (len(header_1) + len(header_2) + 3) * "-"
    dividing_line_additional = round(((len(header_1) + len(header_2) + 3) / 2)) * "- "
    if counts:

        print()
        print(header, dividing_line, sep="\n")

        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        for key, value in sorted_counts.items():
            indent_1 = len(header_1) - len(key)
            indent_2 = len(header_2) - len(str(value))
            line_1 = key + indent_1 * " "
            line_2 = str(value) + indent_2 * " "

            print(line_1, line_2, sep=" | ")
            print(dividing_line_additional)








