from flask import Flask, render_template
from forms import PostForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/produce_records", methods=['GET', 'POST'])
def produce_records():
    form = PostForm()
    if form.validate_on_submit():
        post = [form.title.data, form.quantity.data, form.price.data, form.date.data, form.market.data, form.status.data]
        report = ','.join(post)
        with open("records.csv", 'a') as f:
            f.write(report + '\n')
    return render_template("produce_records.html", form=form)


@app.route("/list_items")
def list_items():
    with open('records.csv') as f:
        data = f.readlines()
    details = [item.strip("\n").split(',')for item in data]
    sold_tomatoes = sum([float(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'tomatoes'])
    sold_cucumbers = sum([float(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'cucumbers'])
    sold_long_pepers = sum([float(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'long peppers'])
    sold_red_bell_pepper = sum([float(q[1]) for q in details if q[5] == 'seller' and q[0].lower() == 'red bell peppers'])
    total = [sold_tomatoes, sold_cucumbers, sold_long_pepers, sold_red_bell_pepper]
    return render_template("list_items.html", data=details, total=total)



if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8010)