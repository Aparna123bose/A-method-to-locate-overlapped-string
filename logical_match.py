from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def serach():
    text=request.form['text']
    pattern=request.form['pattern']
    logic_matrix=[]
    for i in range(len(pattern)):
        index_list=[pattern[i]]
        for j in range(len(text)):
            if(text[j]==pattern[i]):
                index_list.append(j+1)
        logic_matrix.append(index_list)


    col=len(logic_matrix[0])
    match_list=[]
    for i in range(1,col):
        item=logic_matrix[0][i]
        item_list=[item]
        for j in range(1,len(pattern)):
            for k in range(1,len(logic_matrix[j])):
                if(item+1 == logic_matrix[j][k]):
                    item_list.append(item+1)
            item=item+1
        if(len(item_list)==len(pattern)):
            match_list.append(item_list)
    return render_template('output.html',data=match_list,text=text,pattern=pattern)
        

if __name__=='__main__':
    app.run(debug=True)
