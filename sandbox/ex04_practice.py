from csv import DictReader


file_handle = open("../../data/nc_durham_2015_march_21_to_27.csv", "r", encoding="utf8")
csv_reader = str(file_handle)


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    for line in csv_file:
        print(line[0])
        #rows.append(line)
    print(rows)
    return rows


read_csv_rows(csv_reader)