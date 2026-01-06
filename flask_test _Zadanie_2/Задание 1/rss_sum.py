def get_summary_rss(file_path: str) -> str:
    total_kib = 0
    with open(file_path, "r") as output_file:
        lines = output_file.readlines()[1:]  # пропускаем заголовок

        for line in lines:
            columns = line.split()
            if len(columns) > 5:
                total_kib += int(columns[5])
    total_bytes = total_kib * 1024
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    size = total_bytes
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"
if __name__ == "__main__":
    file_path = "output_file.text"
    print(get_summary_rss(file_path))
