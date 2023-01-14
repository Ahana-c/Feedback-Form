from flask import Flask, request, render_template

app = Flask(__name__)

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
        return "Name:"+name,"Room No:"+room, "Hostel:"+hostel, "Mess:"+mess, "Quality:"+ quality, 
    "Quantity:"+quantity, "Service"+service, "Variety:"+variety, "Friendliness:"+friendliness, "Sanitation:"+sanitation, 
    "Comments:"+comments
    return render_template("feedbackformfinal.html")

if __name__=='__main__':
    app.run()
