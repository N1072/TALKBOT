


#モジュールのインポート
import TicTacToe, Number, Math
from hello import say_hello

ttt = TicTacToe.tictactoe()
num = Number.number()
mat = Math.math()

# 使用する変数の初期化
ansed = False# 何かしらの要件にこたえるとTrueになる

# 起動時のあいさつ
say_hello()# 時間帯に合わせた挨拶をする
print("わたしはTALKBOTです。")

while 1:
    
    ansed = False
    #要件を訪ねる
    request=input("要件はなんでしょう？>>")

    print("TALKBOT:")
    # ここから要件に含まれている単語に応じて返事をする

    # 終了(「さよ」「バイ」)＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    for i in ["さよ", "バイ"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            print("さようなら")
            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            ansed = True
            break
    if ansed:# この処理をした場合
        pre_request = request
        break

    # やりなおし(「もういち」「もういっかい」「もう１」「もう1」「いまの」「今の」「さっきの」)=＝
    for i in ["もうい", "いまの", "今の", "さっきの"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            request = pre_request
            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            break

    # ヘルプ(「ができますか」「何が」「できること」「ヘルプ」)＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    for i in ["ができますか", "何が", "できること", "ヘルプ"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            print("・挨拶")
            print("「こんにちは」「おはよう」といった挨拶をしていただくと、こちらも挨拶を返します")
            print("・和暦変換")
            print("「****年を和暦で」「和暦変換がしたい」と言ってくだされば、和暦返還をいたします。")
            print("ただし、明治時代以前の元号には対応しておりません。")
            print("・ゲーム")
            print("「まるばつゲーム」「数あてゲーム」の２つのゲームに対応しております。")
            print("・計算")
            print("式を入力していただくと、その結果を返します。")
            print("・終了")
            print("「さようなら」「バイバイ」と言っていただければ、本プログラムを終了します。")
            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            ansed = True
            break
    if ansed:# この処理をした場合
        pre_request = request
        continue

    # マルバツゲーム(「〇」、「まるばつ」、「マルバツ」)＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    for i in ["〇", "まるばつ", "マルバツ"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            print("まるばつゲームを起動します。")
            ttt.game()
            print("お疲れさまでした。")
            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            ansed = True
            break
    if ansed:# この処理をした場合
        pre_request = request
        continue

    # 計算(「答え」、「+」、「-」、「*」、「/」、「%」、「算」)＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝=
    for i in ["答え", "+", "-", "*", "/", "%", "算"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            formula = ""
            # 要求の中に計算式が含まれている場合、それを取り出す
            for i in request:
                if i in "1234567890+-*/%().":
                    formula += i
            # 含まれていない場合、式を入力させる
            if formula == "":
                formula = input("式を入力してください>>")

            # 計算用のメソッドを呼び、何かしらのエラーが出たら答えを"error"にする
            try:
                ans = mat.clac(formula)
            except BaseException:
                ans = "error"

            # 計算結果を表示(答えが文字列だった場合、エラーメッセージを表示)
            if type(ans) is str:
                if ans == "div0":
                    print("0で割ることはできません")
                else:
                    print("計算できませんでした。")
            else:
                print("{}は{}です。".format(formula, ans))

            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            ansed = True
            break
    if ansed:# この処理をした場合
        pre_request = "算"
        continue

    # 数あてゲーム(「かずあて」、「数あて」、「数当」)＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    for i in ["かずあて", "数あて", "数当"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            print("数あてゲームを起動します。")
            num.game()
            print("お疲れさまでした。")
            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            ansed = True
            break
    if ansed:# この処理をした場合
        pre_request = request
        continue

    # 挨拶する(「おは」、「こん」)＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    for i in ["おは", "こん"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            say_hello()
            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            ansed = True
            break
    if ansed:# この処理をした場合
        pre_request = request
        continue

    # 西暦⇒和暦変換(「和暦」「元号」「何年」)＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    for i in ["和暦", "元号", "何年"]:
        if i in request:
            # 個別の処理ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            # 使う変数の初期化
            year = 0# 変換する西暦
            year_inputed = False# 西暦が入力されたかどうか
            # 元号データ
            era = [
                ("明治" ,1868),
                ("大正" ,1912),
                ("昭和" ,1927),
                ("平成" ,1989),
                ("令和" ,2019),
            ]
            # 文字列から西暦の取り出し(forで1文字ずつ取り出してチェック)
            for j in request:
                # "年","を","は"を見つけたらループを中断
                if j in "年をは":
                    break
                # 例外処理を利用して取り出した1文字が数字かチェック
                try:
                    getint=int(j)
                except ValueError:
                    # intに変換できない(数字でない)なら何もしない
                    pass
                else:
                    # intに変換できた(数字)ならyearに加算
                    year = year * 10 + getint
                    year_inputed = True

            # 西暦が見つからない場合改めて聞く
            if year_inputed == False:
                while True:
                    try:
                        year = int(input("西暦を入力してください>>"))
                    except ValueError:
                        print("整数で入力してください")
                    else:
                        break

            # 和暦に変換 
            preera = ["", 0]# 結果の一つ前の年号(元年のときに表示)
            result = ["", 0]# 結果
            for j in range(len(era)):
                if year >= era[j][1]:
                    preera = [era[j-1][0], year - era[j-1][1] + 1]
                    result = [era[j][0], year - era[j][1] + 1]

            # 明治以前の年が入力された場合
            if year<era[0][1]:
                print("すみません、明治以前には対応していません。")
            else:
                print("{}年は".format(year), end="")
                # 元年(年数が1)の場合の処理
                if result[1] == 1:
                    result[1] = "元"
                    # 一つ前の年数が表示できるなら表示する
                    if preera[1]>0:
                        print("{}{}年、または".format(preera[0], preera[1]), end="")

                print("{}{}年です。".format(result[0], result[1]))
                

            # ここで処理終わりーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            ansed = True
            break
    if ansed:# この処理をした場合
        pre_request = request
        continue

    # 要件がどの機能にも当てはまらない場合
    if request:
        print("ごめんなさい、よくわかりません")# 何か入力されていた場合
    else:
        print("何かしら入力してください")# 何も入力されていない場合
    print("「何ができる？」と聞いていただくと、できることを説明いたします。")

    