import random

class Phone:
    def __init__(self, number):
        self.number = number

    def call(self):
        phrases = [
            f"Дзвонимо з номера {self.number}...",
            f"Набираємо абонента з {self.number}...",
            f"Лінія зайнята, але {self.number} намагається дозвонитися."
        ]
        return random.choice(phrases)


class SmartPhone(Phone):
    def __init__(self, number, brand, megapixels):
        super().__init__(number)
        self.brand = brand
        self.megapixels = megapixels

    def take_photo(self):
        photo_types = ["ий пейзаж", "е селфі", "ий портрет", "е фото закату"]
        chosen_style = random.choice(photo_types)
        return f"Телефон {self.brand} засняв крут{chosen_style} на {self.megapixels} Мега Пікселів!"


numbers = ["+380991112233", "+380674445566", "+380637778899"]
brands = ["Samsung", "iPhone", "Xiaomi", "Pixel", "Sigma Mobile"]
camera_res = [48, 50, 64, 108]

my_phone = SmartPhone(
    number=random.choice(numbers),
    brand=random.choice(brands),
    megapixels=random.choice(camera_res)
)

print(my_phone.call())
print(my_phone.take_photo())