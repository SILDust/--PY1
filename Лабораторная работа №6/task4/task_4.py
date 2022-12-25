import json

INPUT_FILE = "output.csv"
# Файл взят из предыдущего задания


def csv_to_list_dict(csv_text_name, delimiter=',', new_line='\n') -> list[dict]:
    with open(csv_text_name, 'r') as csv_text:
        column_head = csv_text.readline().strip(new_line).split(delimiter)
        return [dict(zip(column_head, stroka.strip(new_line).split(delimiter))) for stroka in csv_text]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
