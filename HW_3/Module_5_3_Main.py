
import argparse
from Module_5_3_func import parse_arguments, load_logs, parse_log_line, filter_logs_by_level, count_logs_by_level, display_log_counts
from collections import defaultdict, Counter



def main():
    args = parse_arguments()                                                                            # Ініціалізація cmd команд

    prep_list = load_logs(args.file_path)                                                               # Розпаковка файла
    filtered_data = filter_logs_by_level(logs=prep_list, level=args.log_level)                          # Вибірка потрібних логів
    display_log_counts(counts=count_logs_by_level(filter_logs_by_level(prep_list,False)))         # Побудова таблички
    print()

    # Заключна частина виводу
    if args.log_level and filtered_data:
        print(f"Деталі логів для рівня '{args.log_level.upper()}':")
        for i in filtered_data:
            print(f"{i['date']} {i['time']} - {i['log_message']}")
    elif not filtered_data:
        print(f"Деталі логів для рівня '{args.log_level.upper()}' не було знайдено\nПеревірте правильність введення рівня логування")
    else:
        for i in filtered_data:
            print(f"{i['date']} {i['time']} {i['log_level']} - {i['log_message']}")


if __name__ == "__main__":
    main()
