from collections import defaultdict

from ctpbee_converter.helper import convert_ld, convert_lo, convert_d_to_df


class Converter:
    def __init__(self, app=None):
        self.app = None
        if app is not None:
            app.tools['converter'] = self
            self.app = app

        self.main_contract_list = []
        self.main_mapping = {}
        self.contracts = defaultdict(list)

    def init_app(self, app):
        if self.app is None and app is not None:
            self.app = app
            app.tools['converter'] = self

    @property
    def positions_df(self):
        """ 以dataframe的形式返回持仓信息 """
        return convert_ld(self.app.recorder.position_manager.get_all_positions())

    @property
    def position_dict(self):
        """ 以字典的形式返回持仓信息 """
        return

    @property
    def position_list(self):
        """ 以列表形式返回持仓信息 """
        return self.app.recorder.position_manager.get_all_positions()

    @property
    def contract_df(self):
        """ 返回合约信息 """
        return convert_lo(self.app.recorder.get_all_contracts(), index="local_symbol")

    @property
    def active_orders_df(self):
        """ 返回活跃的订单 """
        return convert_lo(self.app.recorder.get_all_active_orders())

    @property
    def all_orders_df(self):
        """ 所有单 """
        return convert_lo(self.app.recorder.get_all_orders())

    @property
    def trade_df(self):
        """ 所有成交单 """
        return convert_lo(self.app.recorder.get_all_trades())

    @property
    def account_df(self):
        """ 以dataframe的形式返回账户信息 """
        return convert_d_to_df(self.app.recorder.get_account()._to_dict())

    @property
    def account_dict(self):
        """ 以字典的形式返回账户信息 """
        return self.app.recorder.get_account()._to_dict()

    def get_avtive_orders_df_by_code(self, local_symbol):
        """ 根据local_symbol拿到活跃订单 """
        return
