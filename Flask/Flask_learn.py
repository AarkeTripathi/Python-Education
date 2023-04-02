from flask import Flask,render_template
posts=[{'Name':'Aarke Tripathi','Profession':'Student','Age':19},{'Name':'Harsh Sharma','Profession':'Student','Age':20}]
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('Home.html', posts=posts, title='Home Page')       #You can also write a full html code as string in return but that will be very messy, therefore we use seperate html file as template using render_template class of flask module

@app.route("/about")
def about():
    return render_template('About.html')

if __name__=='__main__':
    app.run(debug=True)
