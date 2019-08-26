from collections import defaultdict

from ctpbee_converter.helper import covert_positionholding, remove_digit


class Converter:
    def __init__(self, app=None):
        if app is not None:
            app.tools['converter'] = self
            self.app = app
        self.main_contract_list = []
        self.main_mapping = {}
        self.contracts = defaultdict(list)
        self.cal_main()

    def cal_main(self):
        """ 计算主力合约  可以被主动调用 """
        for contract in self.app.recorder.get_all_contracts():
            self.contracts[remove_digit(contract.symbol)].append(contract)
        for x, v in self.contracts.items():
            # 根据成交量 来进行计算主力合约
            vol_contract = sorted(v, key=lambda x: x.min_volume, reverse=True)[0]
            self.main_mapping[x.upper()] = vol_contract
            self.main_contract_list.append(vol_contract.local_symbol)

    def init_app(self, app):
        if app is None:
            self.app = app
            app.tools['converter'] = self

    @property
    def positions_df(self):
        """ 以dataframe的形式返回持仓信息 """
        return covert_positionholding(self.app.recorder.position_manager.values())

    @property
    def main_contracts(self) -> list:
        """ 所有主力合约数据 [local_symbol, local_symbol... ] """
        return self.main_contract_list

    def get_main_contract_by_code(self, code: str) -> object:
        """
            通过英文code来获取相应的主力合约数据
            假定输入 ap 返回 --- > ContractData(local_symbol=ap1910)

        """
        return self.main_mapping.get(code.upper())
