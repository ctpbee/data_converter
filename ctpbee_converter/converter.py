from ctpbee_converter.helper import covert_positionholding


class Converter:
    def __init__(self, app=None):
        if app is not None:
            app.tools['converter'] = self
            self.app = app

    def init_app(self, app):
        self.app = app
        app.tools['converter'] = self

    @property
    def positions_df(self):
        """ 以dataframe的形式返回持仓信息 """
        return covert_positionholding(self.app.recorder.position_manager.values())

    def get_positions_cross_dataframe(self):
        pass


if __name__ == '__main__':
    converter  = Converter()
    converter.positions_df