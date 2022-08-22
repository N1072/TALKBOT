

def say_hello():
    """時間帯に合わせた挨拶をする"""
    import datetime
    time = datetime.datetime.now()

    if(time.hour<11):
        # 10:59まで(11時まで)の挨拶
        print("おはようございます")
    elif(time.hour<18):
        # 17:59まで(18時まで)の挨拶
        print("こんにちは")
    else:
        # 18:00以降の挨拶
        print("こんばんは")