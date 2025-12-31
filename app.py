from flask import Flask, render_template, request

app = Flask(__name__)

career_database = {
    "Finance Manager": [
        "accounting", "balance sheet", "financial analysis",
        "budgeting", "excel", "auditing", "taxation"
    ],
    "Chartered Accountant": [
        "accounting", "taxation", "auditing", "financial reporting"
    ],
    "Data Analyst": [
        "python", "excel", "sql", "data analysis", "visualization"
    ],
    "Data Scientist": [
        "python", "machine learning", "statistics", "data modeling"
    ],
    "AI Engineer": [
        "python", "deep learning", "nlp", "tensorflow"
    ],
    "Marketing Manager": [
        "marketing", "seo", "branding", "content strategy"
    ],
    "HR Manager": [
        "communication", "recruitment", "management"
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        skills = request.form["skills"].lower().split(",")
        skills = [s.strip() for s in skills]

        scores = {}
        for career, req_skills in career_database.items():
            match = len(set(skills).intersection(set(req_skills)))
            if match > 0:
                scores[career] = match

        recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

