from app import goodplace


@goodplace.route("/")
@goodplace.route("/index")
def index():
    return "BEM VINDO AO GOODPLACE, ESTAMOS EM MANUNTENÇÃO NO MOMENTO"
