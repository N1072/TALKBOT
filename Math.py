class math:
    def __init__(self) -> None:
        pass

    def __poland(self, target, ind, ope):
        """2つの数字の計算式をいれかえて逆ポーランド記法に変換する"""
        dest = 2# 入れ替え先
        bracket = 0# 括弧の数

        # もしもindの次の値にopeで指定した演算子があるなら
        if target[ind+1] == ope:
            #その次の値が括弧だった場合、その括弧の終わりまで移動
            while True:

                # 括弧の始まりを見つけたら括弧カウントを1増やす
                if target[ind+dest] == "(":
                    bracket += 1

                # 括弧の終わりを見つけたら括弧カウントを1減らす
                if target[ind+dest] == ")":
                    bracket -= 1
                
                dest += 1
                # 括弧カウントが0なら終了
                if bracket == 0:
                    break
            
            target.insert(ind+dest, ope+"!") # 移動先に演算子(入れ替え済みの印付き)を挿入
            target.insert(ind+dest+1, ")")# その次に閉じ括弧を挿入
            target.pop(ind+1)# 元々あった演算子を削除

            dest = 0
            #indの値が閉じ括弧だった場合、その括弧の始まりまで移動
            if target[ind] == ")":
                while True:
                    # 括弧の終わりを見つけたら括弧カウントを1増やす
                    if target[ind+dest] == ")":
                        bracket += 1
                    
                    # 括弧の始まりを見つけたら括弧カウントを1減らす
                    if target[ind+dest-1] == "(":
                        bracket -= 1
                    
                    dest -= 1
                    # 括弧カウントが0なら終了
                    if bracket == 0:
                        break
            # 移動先に括弧を挿入
            target.insert(ind+dest, "(")
            # 括弧を挿入するのは入れ替え済みの部分を孤立させて誤って入れ替えないようにするため

    def __Separat(self, target):
        """文字列に含まれている数値とそれ以外を分離して計算式を作る"""
        # 使う変数の初期化
        result = []# 返り値となる配列
        val = ""# 見つけた数字のカウンター(文字列、配列に入れる際に数値に変換)
        mode = False# カウントのモード(False = 数値をカウント, True = 文字列をカウント)
        # １文字ずつ探索
        for i in target:
            try:
                # 整数に変換できるか確かめる
                int(i)

            # 整数に変換できない場合＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
            except ValueError:
                # 数値モードならーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
                if mode == False:

                    # valの中身がある場合
                    if val:
                        # 探索した文字が小数点ならvalに追加
                        if i == ".":
                            val += i

                        # 一つ上の条件に当てはまらない場合
                        else:
                            # カウントしたものを配列に入れる
                            if "." in val:
                                # 小数点が含まれているなら小数型に
                                result.append(float(val))
                            else:
                                # 小数点が含まれていないなら整数型に
                                result.append(int(val))
                            val = ""
                            mode = True# 文字列モードに切り替え
                    # valの中身がない場合
                    else:
                        mode = True# 文字列モードに切り替え

                # 文字列モードならーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
                if mode == True:

                    # 式で使う文字列なら
                    if i in "+-*/%().=":
                        val += i# valの末尾にその文字を追加

                    # 探索した文字がマイナスなら特殊な処理
                    if i == "-":
                        # valの文字数が1より大きい場合
                        if len(val) > 1:
                            # valから最後の一文字(マイナス)をとったものを配列に入れる
                            result.append(val[0:-1])
                            # valを"-"にして数値モードに切り替え
                            val = "-"
                            mode = False

                    # かっこだった場合の特殊処理
                    if i in "()":
                        # valが2文字以上なら、最後の一文字(かっこ)をとったものを配列に入れる
                        if len(val) >= 2:
                            result.append(val[0:-1])
                        # かっこそのものを分けて配列に入れる
                        result.append(i)

                        val = ""
            # 整数に変換できる場合＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
            else:
                if mode == True:# 文字列モードならーーーーーーーーーーーーーーーーーーーーーーーー
                    # カウントしたものを配列に入れる
                    if val:
                        result.append(val)
                    val = ""
                    mode = False# 数値モードに切り替え

                if mode == False:# 数値モードならーーーーーーーーーーーーーーーーーーーーーーーーー
                    # valの末尾にその数値を追加
                    val += i


        # valに残っているものを配列に入れる
        if mode == False:# 数値モードなら
            if "." in val:
                # 小数点が含まれているなら小数型に
                result.append(float(val))
            else:
                # 小数点が含まれていないなら整数型に
                result.append(int(val))

        if mode == True:# 文字列モードなら
            if val != "":
                result.append(val)

            
        return result


    # ーーーーーー-ここまでプライベートメソッド定義-ーーーーーー
    def clac(self, formula):
        import copy
        """逆ポーランド記法の式を作り、計算する"""
        # 式の最後にイコールをつける
        if formula[-1] != "=":  
            formula += "="

        # 式を演算子や括弧と数値で分離して、式と関係ない文字を排除
        formula = self.__Separat(formula)
        # 式が空っぽの場合エラーを返す
        if formula[0] == "=":
            return "error"

        # 式を逆ポーランド記法に変換
        while 1:
            # iを1つずつ足していって"="にたどり着くまで繰り返す
            i = 0
            pre_formula = copy.copy(formula)
            while formula[i] != "=":
                try:
                    # "*", "/", "**", "//, "%"が一つもないなら"+", "-"を入れ替える
                    if "*" in formula or "/" in formula or "//" in formula or "%" in formula or "**" in formula:
                        self.__poland(formula, i, "*")
                        self.__poland(formula, i, "/")
                        self.__poland(formula, i, "**")
                        self.__poland(formula, i, "//")
                        self.__poland(formula, i, "%")
                    # "*", "/", "**", "//, "%"が一つでもあるならそれらを入れ替える
                    else:
                        self.__poland(formula, i, "+")
                        self.__poland(formula, i, "-")
                except IndexError:
                    break

                i += 1
            # もし上のループで式の内容が何も変わらなければ終了
            if formula == pre_formula:
                break


        # できた式の仕上げをする(括弧をけす、入れ替えの印を外すなど)
        while "(" in formula:
            formula.remove("(")
            formula.remove(")")
        try:
            for i in range(len(formula)):
                if type(formula[i]) is str:
                    if formula[i][-1] == "!":
                        formula[i] = formula[i][:-1:]
        except IndexError:
            return "error"


        # 実際に計算する
        while 1:
            # iを1つずつ足していって"="にたどり着くまで繰り返す
            i = 0
            pre_formula = copy.copy(formula)
            while formula[i] != "=":
                try:
                    # 足し算
                    if formula[i+2] == "+":
                        formula[i] = formula[i] + formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                    # 引き算
                    if formula[i+2] == "-":
                        formula[i] = formula[i] - formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                    # 掛け算
                    if formula[i+2] == "*":
                        formula[i] = formula[i] * formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                    # 割り算
                    if formula[i+2] == "/":
                        formula[i] = formula[i] / formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                    # 累乗
                    if formula[i+2] == "**":
                        formula[i] = formula[i] ** formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                    # 商の整数値
                    if formula[i+2] == "//":
                        formula[i] = formula[i] // formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                    # 累乗
                    if formula[i+2] == "**":
                        formula[i] = formula[i] ** formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                    # 商のあまり
                    if formula[i+2] == "%":
                        formula[i] = formula[i] % formula[i+1]
                        formula.pop(i+2)
                        formula.pop(i+1)
                except TypeError:
                    # 計算の対象に演算子が含まれている場合
                    pass
                except IndexError:
                    # 演算子のチェック時に式の配列をはみ出した場合
                    break
                except ZeroDivisionError:
                    # 0で割った場合
                    return "div0"
                i += 1

            # もし上のループで何も変わらなければ終了
            if formula == pre_formula:
                break

        # 計算結果を返す
        return formula[0]

# テスト用
if __name__ == "__main__":
    a=math()
    while 1:
        formula = input("計算式:")
        print(a.clac(formula))

        if input("もう１回？(y/n)：") == "n":
            
            break
        
