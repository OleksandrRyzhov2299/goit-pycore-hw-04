def get_cats_info(path):
    try:
        with open(path) as fh:
            cats_info = [element.strip().split(",") for element in fh.readlines()]
            cats = []

            for cat in cats_info:
                cats.append({"id": cat[0], "name": cat[1], "age": cat[2]})

            return cats
    except:
        print("An exception occurred")


if __name__ == "__main__":
    cats_info = get_cats_info("files/cats.txt")
    print(cats_info)
