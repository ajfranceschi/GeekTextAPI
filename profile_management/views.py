from . import profman_bp


@profman_bp.route('/')
def index():
    return "Profile Management route"


@profman_bp.route('/getProf')
def getProfile():
    return {"Route": "Get Profile Management"}