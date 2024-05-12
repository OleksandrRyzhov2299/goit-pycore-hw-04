from statistics import mean

file_path = "files/data.txt"


def total_salary(path):
    try:
        with open(path) as file_handler:
            employees_list = [
                element.strip().split(",") for element in file_handler.readlines()
            ]
            salaries = [int(employee[1]) for employee in employees_list]
            return tuple([sum(salaries), mean(salaries)])
    except:
        print("An exception occurred")


if __name__ == "__main__":
    total, average = total_salary(file_path)
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
