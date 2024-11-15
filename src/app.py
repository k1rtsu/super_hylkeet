from flask import render_template, jsonify, request
from db_helper import reset_db
from config import app, test_env
from repositories.citation_repository import add_citation


@app.route("/")
def index():
    citations = get_citations()
    return render_template("index.html", listed_citations=citations)


@app.route("/add_citation", methods=["POST"])
def add_citation_route():
    citation = request.form
    """
    DATA VERIFICATION STILL IN PROGRESS
    errors = validate_citations(citation)
    if errors:
        return render_template("index.html", errors=errors)
    """
    add_citation(citation)
    success = "Citation added successfully"
    return render_template("index.html", success=success)


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})
