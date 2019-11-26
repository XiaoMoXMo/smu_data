from server_app.grasp.water import get_water


def add_api(app):
    # pass
    @app.route('/water_state')
    def get_water_state():
        water_list = get_water()
        return {'data': {'list': water_list, 'size': len(water_list)}}
