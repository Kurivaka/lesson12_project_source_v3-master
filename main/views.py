from flask import Blueprint, render_template, request
import logging
from main.utils import *
from config import POST_PATH
from exceptions import *



main_blueprint = Blueprint("main_bluerprint", __name__ , template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def searh_page():
    s = request.args.get("s", "")
    logging.info("Выполняется поиск")
    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"
    filtered_posts = search_posts_by_uppstring(posts, s)
    return render_template("post_list.html", posts=filtered_posts, s=s)


