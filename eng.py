eng = {'CC': '調整接続詞', #品詞分けの辞書
       'CD': '基数',
       'DT': '限定詞',
       'EX': '存在を表すthere',
       'FW': '外国語',
       'IN': '前置詞または従属接続詞',
       'JJ': '形容詞',
       'JJR': '形容詞 (比較級)',
       'JJS': '形容詞 (最上級)',
       'LS': '-',
       'MD': '法',
       'NN': '名詞',
       'NNS': '名詞 (複数形)',
       'NNP': '固有名詞',
       'NNPS': '固有名詞 (複数形)',
       'PDT': '前限定辞',
       'POS': '所有格の終わり',
       'PRP': '人称代名詞',
       'PRP$': '所有代名詞',
       'RB': '副詞',
       'RBR': '副詞 (比較級)',
       'RBS': '副詞 (最上級)',
       'RP': '不変化詞',
       'SYM': '記号',
       'TO': '前置詞 to',
       'UH': '感嘆詞',
       'VB': '動詞 (原形)',
       'VBD': '動詞 (過去形)',
       'VBG': '動詞 (動名詞または現在分詞)',
       'VBN': '動詞 (過去分詞)',
       'VBP': '動詞 (三人称単数以外の現在形)',
       'VBZ': '動詞 (三人称単数の現在形)',
       'WDT': 'Wh 限定詞',
       'WP': 'Wh 代名詞',
       'WP$': '所有 Wh 代名詞',
       'WRB': 'Wh 副詞',
       }

en_color = {'調整接続詞': 'purple', #品詞の色
            '基数': 'cadetblue',
            '限定詞': 'teal',
            '存在を表すthere': 'brown',
            '外国語': 'linen',
            '前置詞または従属接続詞': 'red',
            '形容詞': 'crimson',
            '形容詞 (比較級)': 'gold',
            '形容詞 (最上級)': 'orange',
            '-': 'aliceblue',
            '法': 'silver',
            '名詞': 'blue',
            '名詞 (複数形)': 'mediumblue',
            '固有名詞': 'darkblue',
            '固有名詞 (複数形)': 'navy',
            '前限定辞': 'midnightblue',
            '所有格の終わり': 'darkolivegreen',
            '人称代名詞': 'chartreuse',
            '所有代名詞': 'yellowgreen',
            '副詞': 'green',
            '副詞 (比較級)': 'forestgreen',
            '副詞 (最上級)': 'seagreen',
            '不変化詞': 'darkseagreen',
            '記号': 'gray',
            '前置詞 to': 'tomato',
            '感嘆詞': 'lemonchiffon',
            '動詞 (原形)': 'indigo',
            '動詞 (過去形)': 'blueviolet',
            '動詞 (動名詞または現在分詞)': 'mediumvioletred',
            '動詞 (過去分詞)': 'magenta',
            '動詞 (三人称単数以外の現在形)': 'fuchsia',
            '動詞 (三人称単数の現在形)': 'violet',
            'Wh 限定詞': 'olive',
            'Wh 代名詞': 'darkred',
            '所有 Wh 代名詞': 'maroon',
            'Wh 副詞': 'indianred',
            }

def divide(name): #品仕分け
    if name in eng:
        return en_color[eng[name]]
    else:
        color = 'black'
        return color

def ruby(name): #ルビ振り
    if name in eng:
        return eng[name]
    else:
        ruby = ''
        return  ruby

#inp = input("入力: ")
