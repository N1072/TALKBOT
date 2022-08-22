class tictactoe:
    def __init__(self):
        pass

    def __chkwin(self, list, i):
        """list変数をチェックして勝者を決める"""
        if list[i] == "o":
            return 1
        elif list[i] == "x":
            return -1

    def __cpu(self, list, turn):
        """cpuに置く場所を考えさせる"""
        import random
        # you,me変数を設定
        if turn == 1:
            me = "o"
            you = "x"
        else:
            me = "x"
            you = "o"
        # you = 相手の記号
        # me = 自分の記号

        # 探索モードを一つずつ試す
        
        # cmode = 0:リーチがあるなら完成させる
        # cmode = 1:相手のリーチをつぶす
        for cmode in range(2):
            # 探索方向(chk)を1つずつ試していく

            # chk = 0:横方向
            # chk = 1:縦方向
            # chk = 2:斜め１(左上から右下)
            # chk = 3:斜め２(右上から左下)
            for chk in range(4):

                # chkに応じて次のfor文のループ回数を決める
                if chk <= 1:
                    loop = 3
                else:
                    loop = 1
                
                # 実際に確かめる
                for i in range(loop):

                    # 盤面から１列取得し、chklistに代入
                    if chk == 0:# 横方向
                        chklist = list[i*3 : i*3+3]

                    elif chk == 1:# 縦方向
                        chklist = list[0+i : 7+i : 3]

                    elif chk == 2:# 斜め１
                        chklist = list[0 :: 4]

                    elif chk == 3:# 斜め２
                        chklist = list[2 : 7 : 2]

                    #cmodeごとにおけるかどうかチェック
                    if cmode == 0:
                        # chklistから自分の記号をとった結果１文字だけ残り、その１文字が相手の記号でないならそこに置く
                        chklist2 = chklist.replace(me, "")
                        if len(chklist2) == 1 and chklist2 != you:
                            return chklist2

                    elif cmode == 1:
                        # chklistから相手の記号をとった結果１文字だけ残り、その１文字が自分の記号でないならそこに置く
                        chklist2 = chklist.replace(you, "")
                        if len(chklist2) == 1 and chklist2 != me:
                            return chklist2
                
        # 置く場所が決まらなかった場合、ランダムに記号を置く
        randlist=str(list).replace(you, "").replace(me, "")# 盤面からおける場所だけ残す
        return randlist[random.randint(0, len(randlist)-1)]# 残った場所からランダムに選ぶ

    # 盤面の表示
    def __viewlist(self, list):
        print(list[0], '|', list[1],'|', list[2], sep="")
        print('-+-+-')
        print(list[3], '|', list[4],'|', list[5], sep="")
        print('-+-+-')
        print(list[6], '|', list[7],'|', list[8], sep="")
    # ーーーーーーーここまでプライベートメソッド定義ーーーーーーー 
    def game(self):
        """実際のゲーム部分"""
        #変数の宣言
        self.winner = 0 # 勝者(0 : 決まってない , 1 : 〇の勝ち , -1 : ✕の勝ち , 2 : 引き分け)
        turn = 1 # ターン(1 : 〇のターン , -1 : ✕のターン)
        list = "012345678" #盤面(下のように並べる)
        #                   0|1|2
        #                   -+-+-
        #                   3|4|5
        #                   -+-+-
        #                   6|7|8
        msg = "" #メッセージ前半(自分の記号が入っている)
        msg2 = "" #メッセージ後半

        # モードセレクト
        print("モードを選んでください")
        while 1:
            print("(0=両方人間, 1=oがcpu, 2=xがcpu, 3=両方cpu)")
            try:
                mode=int(input("入力："))
                if mode >= 0 and mode < 4:
                    # 0～3が入力されればゲームスタート(ループを抜ける)
                    break
                else:
                    #範囲外の場合
                    print("0～3の範囲で入力してください")
            except ValueError:
                # ValueErrorが発生した場合(数値に変換できないデータが入力されたとき)
                print("数字で入力してください")

        # ゲームのメイン部分
        while self.winner == 0:
            

            if turn == 1:
                msg = "o"
            elif turn == -1:
                msg = "x"
            msg2 = "の番"
            while mode == 0 or (mode == 1 and turn == -1) or (mode == 2 and turn == 1):
                self.__viewlist(list)# 盤面の表示
                

                print(msg + msg2)
                try:
                    put=input("どこに置きますか？(番号で / 'cpu'でおまかせ):")
                    put=str(int(put))
                except ValueError:
                    if put != "cpu":
                        msg2=":番号を入力してください"
                        continue

                if put!="cpu":

                    # エラー(入力が１文字でなかった場合)
                    if len(put)!=1:
                        msg2=":入力は１文字だけにしてください"
                        continue
                
                    # エラー(盤面にない番号に置こうとした場合)
                    if put not in list :
                        msg2=":そこにはおけません"
                        continue

                    # エラー(何も書かれなかった場合)
                    if put=="":
                        msg2=":何か入力してください"
                        continue

                    break
            
            # cpuがおいた場所の処理
            if (mode==1 and turn==1) or (mode==2 and turn==-1) or mode==3 or put=="cpu":
                put=self.__cpu(list, turn)
                print("{}：{}に置きました".format(msg, put))

            if turn==1:
                list = list.replace(put, "o")
            elif turn==-1:
                list = list.replace(put, "x")
            

            # 勝敗判定
            if list.replace("o", "").replace("x", "")=="":
                self.winner = 2
            
            for i in range(3):
                # 横方向の判定
                if list[i*3 : i*3+3] == msg*3:
                    self.winner = self.__chkwin(list, i*3)
                # 縦方向の判定
                if list[0+i : 7+i : 3] == msg*3:
                    self.winner = self.__chkwin(list, 0+i)
            # 斜め方向の判定
            if list[0 :: 4] == msg*3 or list[2 : 7 : 2] == msg*3:
                self.winner = self.__chkwin(list, 4)

            # 盤面の表示(両方CPUモードのみ)
            if mode == 3:
                self.__viewlist(list)
                input("ENTERで次へ")

            turn *= -1# ターンの切り替え

        #ここから決着後の処理

        self.__viewlist(list)# 盤面の表示

        # 結果の表示
        if self.winner == 1:
            print("oの勝ち")
        elif self.winner == -1:
            print("xの勝ち")
        else:
            print("引き分け")


# テスト用
if __name__ == "__main__":
    a=tictactoe()
    while 1:
        a.game()
        if input("もう１回？(y/n)：") == "n":
            break