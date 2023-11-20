# きのみの基礎エナジー -> https://wikiwiki.jp/poke_sleep/%E3%81%8D%E3%81%AE%E3%81%BF%E3%81%AE%E4%B8%80%E8%A6%A7
# きのみの獲得エナジー -> https://wikiwiki.jp/poke_sleep/%E3%81%8D%E3%81%AE%E3%81%BF

def get_energy_point(pkmn_level:int, pkmn_type:str, help_time:float, kinomi_amount:int, is_suit:bool) -> float:
    '''
    きのみのエナジー効率を計算する

    :param pkmn_level:      ポケモンのレベル(Ex: 19)
    :param pkmn_type:       ポケモンのタイプ(Ex: "でんき")
    :param help_time:       おてつだい時間(Ex: 35)
    :param kinomi_amount:   持ってくるきのみの数(Ex: 2)
    :param is_suit:         カビゴンの好みかどうか(Ex: False)
    :return:                のみのエナジー効率(Ex: 2.00)
    '''
    kiso_energy_dic = {
        "ひこう":24,
        "むし":24,
        "でんき":25,
        "エスパー":26,
        "ゴースト":26,
        "フェアリー":26,
        "ほのお":27,
        "かくとう":27,
        "ノーマル":28,
        "じめん":29,
        "くさ":30,
        "いわ":30,
        "みず":31,
        "あく":31,
        "こおり":32,
        "どく":32,
        "はがね":33,
        "ドラゴン":35,
    }
    kiso_energy = kiso_energy_dic[pkmn_type]
    energy_value = max(kiso_energy+pkmn_level-1, kiso_energy*1.025**(pkmn_level-1))
    point = 1 / help_time * energy_value * kinomi_amount * (2 if is_suit else 1)
    return point

# テスト用
def main():
    print("サンダース",get_energy_point(19, "でんき", 35, 2, False))
    print("グレイシア",get_energy_point(20, "こおり", 51, 1, True))

if __name__ == "__main__":
    main()