from flaskr import app
from flask import render_template, request, redirect, url_for,Markup
from flaskr import eng
import nltk
from googletrans import Translator

#nltk.download('all')


@app.route('/')
def index():
    book = 10
    return render_template(
        'index.html',
        book=book
    )


@app.route('/register', methods=['POST'])
def register():
    request
    sentence = request.form['sentence']
    check = request.form.get('transAble')
    en_div = nltk.word_tokenize(sentence)
    en_pos = nltk.pos_tag(en_div)
    en_color = []
    en_ruby = []
    paragraph= 1
    p_max=1
    en_text = f'<p>{paragraph}段落</p>'
    en_text_simple= f'<p>{paragraph}段落</p>'
    tr_text= f'<p>{paragraph}段落</p>'
    en_words=f'<tr><th colspan="3"class="th-layout">{paragraph}</th></tr>'
    en_question=f'<tr><th colspan="3"class="th-layout">{paragraph}</th></tr>'

    translator=Translator()
    tr_en=""
    for i in range(len(en_pos)):
        if en_pos[i][1] == ".":
            p_max+=1
    for i in range(len(en_pos)):
        en_color = eng.divide(en_pos[i][1])
        en_ruby = eng.ruby(en_pos[i][1])

        if check != None:
            tr_en = en_pos[i][0]
            tr_ja = translator.translate(tr_en, src="en", dest="ja").text

        if en_pos[i][1] == ".":
            paragraph +=1
            if p_max != paragraph:
                en_text += f'<span style="text-decoration-color:{en_color}"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:{en_color};text-align: center">{en_ruby + " "}</rt></ruby></span><br><br><p>{paragraph}段落</p>'
                en_text_simple += f'<span style="text-decoration-color:#333"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:#333;text-align: center">{en_ruby + " "}</rt></ruby></span><br><br><p>{paragraph}段落</p>'
                if check != None:
                    tr_text += f'<span style="text-decoration-color:#333"><font class="font">{en_pos[i][0] + "/"}</font></span><br><br><p>{paragraph}段落</p>'
            else:
                en_text += f'<span style="text-decoration-color:{en_color}"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:{en_color};text-align: center">{en_ruby + " "}</rt></ruby></span><br><br>'
                en_text_simple += f'<span style="text-decoration-color:#333"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:#333;text-align: center">{en_ruby + " "}</rt></ruby></span><br><br>'
                if check != None:
                    tr_text += f'<span style="text-decoration-color:#333"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:#333;text-align: center">{tr_ja + " "}</rt></ruby></span><br><br>'
        else:
            en_text += f'<span style="text-decoration-color:{en_color}"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:{en_color};text-align: center">{en_ruby + " "}</rt></ruby></span>'
            en_text_simple += f'<span style="text-decoration-color:#333"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:#333;text-align: center">{en_ruby + " "}</rt></ruby></span>'
            if check != None:
                tr_text += f'<span style="text-decoration-color:#333"><ruby style="ruby-position:under"><font class="font">{en_pos[i][0] + "/"}</font><rt style="color:#333;text-align: center">{tr_ja + " "}</rt></ruby></span>'

        if en_pos[i][1] == ".":
            if p_max != paragraph:
                en_question += f'<tr><th colspan="3" class="th-layout">{paragraph}</th></tr>'
        elif en_pos[i][1] == "," or en_pos[i][1] == "``" or en_pos[i][1] == "''":
            pass
        else:
            en_question += f'<tr><th>{en_pos[i][0]}</th><th>{en_ruby}</th><th></th></tr>'


        if check != None:
            if en_pos[i][1] == ".":
                if p_max != paragraph:
                    en_words += f'<tr><th colspan="3" class="th-layout">{paragraph}</th></tr>'
            elif en_pos[i][1] == "," or en_pos[i][1] == "``" or en_pos[i][1] == "''":
                pass
            else:
                en_words += f'<tr><th>{en_pos[i][0]}</th><th>{en_ruby}</th><th>{tr_ja}</th></tr>'

    Mark_text = Markup(en_text)
    Mark_text_simple = Markup(en_text_simple)
    Trans_text= Markup(tr_text)
    return render_template(
        'index.html',
        sentence=sentence,
        en_pos=en_pos,
        Mark_text=Mark_text,
        Mark_text_simple=Mark_text_simple,
        Trans_text=Trans_text,
        en_words=en_words,
        en_question=en_question
    )
