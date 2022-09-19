import datetime
import hashlib

data1 = {
    1: '5084972163',
    2: '9801567243',
    3: '7286059143',
    4: '1850394726',
    5: '1462578093',
    6: '5042936178',
    7: '0145937682',
    8: '0964238571',
    9: '3497651802',
    10: '9125780643',
    11: '8634972150',
    12: '5924673801',
    13: '8274053169',
    14: '5841792063',
    15: '2469385701',
    16: '8205349671',
    17: '7429516038',
    18: '3769458021',
    19: '5862370914',
    20: '8529364170',
    21: '7936082154',
    22: '5786241930',
    23: '0728643951',
    24: '9418360257',
    25: '5093287146',
    26: '5647830192',
    27: '3986145207',
    28: '0942587136',
    29: '4357069128',
    30: '0956723814',
    31: '1502796384'
}

class Password:
    def get_passwd(passwd, day=datetime.date.today().day, salt=1):
        passwdbyte = [ord(n) for n in passwd]
        ps_len = len(passwd)
        passwd_token = list(range(0, ps_len))
        date_token = Password.get_date_token(day, salt)
        index1 = 0 
        index2 = 0
        for i in range(0, ps_len):
            index1 += 1 & 255
            index1 %= 256
            index2 += date_token[index1] & 255
            index2 %= 256
            temp = date_token[index1]
            date_token[index1] = date_token[index2]
            date_token[index2] = temp
            index = date_token[index1] + date_token[index2] & 255
            index %= 256
            passwd_token[i] = 256 + date_token[index] ^ passwdbyte[i]
            passwd_token[i] %= 256

        m2 = hashlib.md5()
        m2.update(bytes(passwd_token))
        return m2.hexdigest()[8:24]

    def get_date_token(day, salt):
        word = data1.get(day)    
        word_len = len(word)
        wordbyte = [int(w) for w in word]
        token = [n if n < 128 else n-256 for n in range(0, 256)]
        index = 0
        for i in range(0, 256):
            index += token[i] + ((wordbyte[i % word_len]) & (255))
            index %= 256
            temp = token[i]
            token[i] = token[index]
            token[index] = temp
        return token

def show_passwd(passwd):
    for i in range(1,32):
        print(i,"=",Password.get_passwd(passwd, i, 1), sep='')

if __name__ == '__main__':
    ps = '改成你的密码'
    show_passwd(ps)
