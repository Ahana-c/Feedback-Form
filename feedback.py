from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

data={}

@app.route('/', methods =["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        room = request.form.get("room")
        hostel = request.form.get("hostel")
        mess = request.form.get("mess")
        quality = request.form.get("quality")
        quantity = request.form.get("quantity")
        service = request.form.get("service")
        variety = request.form.get("variety")
        friendliness = request.form.get("friendliness")
        sanitation = request.form.get("sanitation")
        comments = request.form.get("comments")
        
        data['name']=name
        data['room']=room
        data['hostel']=hostel
        data['mess']=mess
        data['quality']=quality
        data['quantity']=quantity
        data['service']=service
        data['variety']=variety
        data['friendliness']=friendliness
        data['sanitation']=sanitation
        data['comments']=comments
        return redirect(url_for('input'))
    else:
        return render_template("feedbackformfinal.html")
    
@app.route('/input')
def input():
    return render_template('input.html',
    name = data['name'],
    room = data['room'],
    hostel = data['hostel'],
    mess = data['mess'],
    quality = data['quality'],
    quantity = data['quantity'],
    service = data['service'],
    variety = data['variety'],
    friendliness = data['friendliness'],
    sanitation = data['sanitation'],
    comments = data['comments'])

if __name__=='__main__':
    app.run()
