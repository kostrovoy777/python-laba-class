import json
from keyword import iskeyword


class Advert:
    def __init__(self, jobj):
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
                    setattr(self, k, Advert(v))
                else:
                    setattr(self, k, v)
            except ValueError:
                print("ValueError: must be >= 0")

        if not hasattr(self, "price"):
            setattr(self, "price", 0)


if __name__ == '__main__':
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{
        "title": "python",
        "price": 5,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print(lesson_ad.__dict__)
    print(lesson_ad.location.address)
    print(lesson_ad.location)

