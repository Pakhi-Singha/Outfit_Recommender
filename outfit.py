from flask import Flask, render_template, request

app = Flask(__name__)

class Closet:
    def __init__(self):
        self.items = []

    def add_item(self, name, category, image_url):
        self.items.append({"name": name, "category": category, "image": image_url})

    def recommend_outfit(self, dress_code):
        dress_code_map = {
            "cocktail": ["sequin dress", "pumps"],
            "corporate": ["hosiery", "pumps", "button down", "pencil skirt"]
        }
        required = dress_code_map.get(dress_code.lower(), [])
        return [
            item for item in self.items if item["name"].lower() in required
        ]

closet = Closet()
closet.add_item("Sequin Dress", "dress", "/static/sequin_dress.jpg")
closet.add_item("Hosiery", "accessory", "/static/hosiery.jpg")
closet.add_item("Pumps", "shoes", "/static/pumps.jpg")
closet.add_item("Button Down", "top", "/static/button_down.jpg")
closet.add_item("Pencil Skirt", "bottom", "/static/pencil_skirt.jpg")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected = request.form["dress_code"]
        outfit = closet.recommend_outfit(selected)
        return render_template("result.html", dress_code=selected, outfit=outfit)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
