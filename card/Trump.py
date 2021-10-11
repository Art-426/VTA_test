import random

class Card:
    SUITS = ['♠️',  '❤️', '♦︎', '♣️']
    SUITS_white = ['♤', '♡', '♢', '♧']
    NUMBERS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  
    # トランプ52枚の生成
    def make_card():
        return [Card.SUITS[s] + Card.NUMBERS[n] for s in range(4) for n in range(13)]
    # トランプ52枚の生成 2
    def make_card_white():
        return [Card.SUITS_white[s] + Card.NUMBERS[n] for s in range(4) for n in range(13)]
    
    def change_num():
        return

    def make_jokcer():
        return 

class DeckAction:
    # シャッフルした山札作成
    def shuffle(card):
        return random.sample(card, len(card))
    # カードを引くかの確認
    def draw_check():
        print('カードを引きますか？ Yes or No')
        draw_flag = False
        while True:
            ans = input('Y or N >>> ')
            if ans == 'y' or ans == 'Y':
                draw_flag = True
                return draw_flag
            elif ans == 'n' or ans == 'N':
                draw_flag = False
                return draw_flag
    # 山札の上から一枚引く
    def draw(deck):
        draw_card = deck.pop(0)
        return draw_card

class Game:
    # ゲームを続けるか確認
    def next_game(chips):
        if chips <= 0:
            game_flag = False
            print('チップがなくなったため終了します')
        else:
            print('続けますか？ Yes or No')
            while True:
                next_game = input('Y or N >>> ')
                if next_game == 'y' or next_game == 'Y':
                    print('次のゲームが始まります')
                    game_flag = True
                    return game_flag
                elif next_game == 'n' or next_game == 'N':
                    print('ゲームを終了します')
                    game_flag = False
                    return game_flag
    # 区切り　エンターで進む
    def pless_enter():
        print('--------------------------')
        input('Please Enter >>> ')
        print('--------------------------')
