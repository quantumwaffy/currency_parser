from time import sleep

import requests
from bs4 import BeautifulSoup, NavigableString

SOURCE = "https://myfin.by/currency/"

CITIES = {
    1: ("minsk", "Минск"),
    2: ("brest", "Брест"),
    3: ("vitebsk", "Витебск"),
    4: ("gomel", "Гомель"),
    5: ("grodno", "Гродно"),
    6: ("mogilev", "Могилев"),
}

PROPOSAL = (
    ("usd_buy", "best_usd_buy"),
    ("usd_sell", "best_usd_sell"),
    ("euro_buy", "best_euro_buy"),
    ("euro_sell", "best_euro_sell"),
    ("rub_buy", "best_rub_buy"),
    ("rub_sell", "best_rub_sell"),
    ("usd_buy_from euro", "best_usd_buy_from euro"),
    ("usd_sell_from euro", "best_usd_sell_from euro"),
)


def choice_city():
    city = ""
    checker = True
    while checker:
        try:
            print("Выберите город:")
            for key, value in CITIES.items():
                print(str(key) + ") " + value[1])
            choice = input()
            choice_dict = CITIES.get(int(choice))
            if not choice_dict:
                print("Такого города не существует. Повторите выбор...")
            else:
                checker = False
                city = CITIES[int(choice)][0]
        except ValueError:
            print("Введите корректное значение!")
    return city


def make_soup():
    city = choice_city()
    if city:
        file = "temporary_" + city + ".html"
        url = SOURCE + city
        response = requests.get(url, headers={"User-agent": "your bot 0.1"})
        with open(file, "w") as f:
            f.write(str(BeautifulSoup(response.text, "lxml")))
            print(url)
        return file


def parsing_soup():
    file = make_soup()
    dict_currency = {}
    dict_best_currency = {}

    with open(file) as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")
    table_currnecy = soup.find("tbody", {"id": "currency_tbody"})
    banks = table_currnecy.findAll("tr")
    bank_name = ""
    for bank in banks:
        if bank.has_attr("data-bank_id"):
            for td in bank:
                if not isinstance(td, NavigableString):
                    if td.find("span"):
                        bank_name = td.find("span").get_text()
                        dict_currency[bank_name] = {}
                        dict_best_currency[bank_name] = {}
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[0][0]):
                        dict_currency[bank_name].update({PROPOSAL[0][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[0][1]: td.get_text()})
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[1][0]):
                        dict_currency[bank_name].update({PROPOSAL[1][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[1][1]: td.get_text()})
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[2][0]):
                        dict_currency[bank_name].update({PROPOSAL[2][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[2][1]: td.get_text()})
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[3][0]):
                        dict_currency[bank_name].update({PROPOSAL[3][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[3][1]: td.get_text()})
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[4][0]):
                        dict_currency[bank_name].update({PROPOSAL[4][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[4][1]: td.get_text()})
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[5][0]):
                        dict_currency[bank_name].update({PROPOSAL[5][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[5][1]: td.get_text()})
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[6][0]):
                        dict_currency[bank_name].update({PROPOSAL[6][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[6][1]: td.get_text()})
                        continue
                    if not dict_currency[bank_name].get(PROPOSAL[7][0]):
                        dict_currency[bank_name].update({PROPOSAL[7][0]: td.get_text()})
                        if td.has_attr("class") and td.attrs["class"][0] == "best":
                            dict_best_currency[bank_name].update({PROPOSAL[7][1]: td.get_text()})
                        continue

    dict_best_currency = {bank: currencies for bank, currencies in dict_best_currency.items() if currencies}

    return [dict_currency, dict_best_currency]


def print_banks(dict_currency, chosen_currency=None):
    dynamic_dict = {}
    if chosen_currency == PROPOSAL[0][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[0][1]
        }
    elif chosen_currency == PROPOSAL[1][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[1][1]
        }
    elif chosen_currency == PROPOSAL[2][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[2][1]
        }
    elif chosen_currency == PROPOSAL[3][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[3][1]
        }
    elif chosen_currency == PROPOSAL[4][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[4][1]
        }
    elif chosen_currency == PROPOSAL[5][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[5][1]
        }
    elif chosen_currency == PROPOSAL[6][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[6][1]
        }
    elif chosen_currency == PROPOSAL[7][1]:
        dynamic_dict = {
            bank: {kind: value}
            for bank, currencies in dict_currency.items()
            for kind, value in currencies.items()
            if kind == PROPOSAL[7][1]
        }
    elif not chosen_currency:
        dynamic_dict = dict_currency
    for bank, currencies in dynamic_dict.items():
        print("\n" + bank + ":")
        for kind, value in currencies.items():
            print(kind + ": " + value)


def user_input():
    list_soup = parsing_soup()

    def option_choose():
        print(
            "1) Узнать все курсы валют\n"
            "2) Узнать банки с лучшим курсом валют\n"
            "3) Узнать лучший курс покупки $\n"
            "4) Узнать лучший курс продажи $\n"
            "5) Узнать лучший курс покупки €\n"
            "6) Узнать лучший курс продажи €\n"
            "7) Узнать лучший курс покупки ₽\n"
            "8) Узнать лучший курс продажи ₽\n"
            "9) Узнать лучший курс покупки $ c €\n"
            "10) Узнать лучший курс продажи $ c €\n"
        )

        choice = input("Выберите пункт меню:")
        if choice == "1":
            print_banks(list_soup[0])
        elif choice == "2":
            print_banks(list_soup[1])
        elif choice == "3":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[0][1])
        elif choice == "4":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[1][1])
        elif choice == "5":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[2][1])
        elif choice == "6":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[3][1])
        elif choice == "7":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[4][1])
        elif choice == "8":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[5][1])
        elif choice == "9":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[6][1])
        elif choice == "10":
            print_banks(list_soup[1], chosen_currency=PROPOSAL[7][1])
        else:
            print("Вы ввели неверное значение. Введите корректное...")
            sleep(1)
            return option_choose()

    option_choose()

    def continue_work():
        print(
            "\n\nЖелаете продолжить?\n"
            "1) Смотреть курс валют в текущем городе\n"
            "2) Выбрать другой город\n"
            "3) Выход"
        )
        continue_choice = input("Выберите пункт меню:")
        if continue_choice == "1":
            option_choose()
        elif continue_choice == "2":
            user_input()
        elif continue_choice == "3":
            exit()
        else:
            print("Вы ввели неверное значение. Введите корректное...")
        return continue_choice

    while continue_work() != "3":
        continue_work()


def main():
    user_input()


if __name__ == "__main__":
    main()
