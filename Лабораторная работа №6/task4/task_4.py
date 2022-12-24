import json

INPUT_FILE = "output.csv"
# Файл взят из предыдущего задания


def csv_to_list_dict(csv_text_name, delimiter=',', new_line='\n') -> list[dict]:
    with open(csv_text_name, 'r') as csv_text:
        json_text = []
        for ind, value in enumerate(csv_text):
            cell = value.strip(new_line).split(delimiter)
            if ind == 0:
                column_head = cell
                continue

            json_text.append({})

            for i, _ in enumerate(column_head):
                json_text[-1][column_head[i]] = cell[i]

    return json_text


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
