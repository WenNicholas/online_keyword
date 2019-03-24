from flask import Flask,render_template,request
import jieba
import keywords

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/getResult",methods=["POST"])
def getResult():
    source = request.form.get("source")
    # words = jieba.cut(source)
    # seg_list = keywords.seg_to_list(source)
    # filter_list = keywords.word_filter(seg_list, pos)
    keyword = keywords.textrank_extract(source)
    word = [str(words)for words in keyword]
        # print(words)
    return " ".join(word)



if __name__ == '__main__':
    app.run()
