import json
from keyword import iskeyword


class ColorizeMixin:
    repr_color_code = 32  # green

    def coloring(self):
        print("\033[1;" + str(self.repr_color_code) + ";40m")


class Advert(ColorizeMixin):
    repr_color_code = 33

    def __init__(self, jobj: dict, recur=0):
        for k, v in jobj.items():
            assert k.isidentifier(), "Некорректный идентификатор"
            assert not iskeyword(k), "Ключевое слово используется в качестве идентификатора"
            # if k == "price" and v < 0:
            #     print("ValueError: must be >= 0")
            #     exit(1)
            # if k == "price":
            #     assert (v >= 0), "ValueError: must be >= 0"
            try:
                # если цена отрицательная, то будет исключение, и поле инициализируется нулем после цикла
                if k == "price" and v < 0:
                    raise ValueError

                if isinstance(v, dict):
                    setattr(self, k, Advert(v, 1))
                else:
                    setattr(self, k, v)
            except ValueError:
                print("ValueError: must be >= 0")
        # проверяем что это не вложенный словарь
        if not recur:
            if not hasattr(self, "title"):
                print("Отсутствует поле title")
                exit(1)

            if not hasattr(self, "price"):
                setattr(self, "price", 0)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{
        "title": "python",
        "price": 5,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            },
        "borch": 10
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    # print(lesson_ad.__dict__)
    # print(lesson_ad.location)
    print(lesson_ad.title)
    print(lesson_ad.location.address)

    iphone_ad = Advert({"title": "Iphone", "price": 100})
    iphone_ad.coloring()
    print(iphone_ad)
