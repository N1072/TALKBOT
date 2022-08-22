# coding: utf-8
class number:
    def __init__(self) -> None:
        pass

    def game(self):
        """ゲームのメイン部分"""
        import random
        # 変数の初期化
        ans = random.randint(0, 99)
        score = 0
        num = -1
        # 説明の表示
        print("0から99までの数をあててください")

        # 正解まで繰り返す
        while num != ans:
            # 入力の受付
            try:
                num = int(input("数を入力:"))
            except:
                print("数字で入力してください")

            # 不正解判定
            if num < ans:
                print("小さすぎます")
            elif num > ans:
                print("大きすぎます")
            
            #回数を1加算
            score += 1

        # 正解の処理
        print("！！！あたり！！！")
        print(score, "回で正解しました", sep="")

# テスト用
if __name__ == "__main__":
    a=number()
    while 1:
        a.game()
        if input("もう１回？(y/n)：") == "n":
            break