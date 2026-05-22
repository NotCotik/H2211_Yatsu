import colorama

print("Найважливіші функції colorama")
print("")

print("Функція init:")
print(type(colorama.init))
print("Пояснення: Вмикає кольоровий текст, щоб він працював у консолі.")
print("")

print("Функція Fore:")
print(type(colorama.Fore))
print("Атрибути всередині:")
print(dir(colorama.Fore))
print("Пояснення: Відповідає за колір самих літер (наприклад, RED, GREEN).")
print("")

print("Функція Style:")
print(type(colorama.Style))
print("Атрибути всередині:")
print(dir(colorama.Style))
print("Пояснення: Робить текст яскравим і скидає кольори назад до звичайних (RESET_ALL).")