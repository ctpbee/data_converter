# data_converter
ctpbee提供的快速数据转换器


> 旨在提供快速数据转换功能, 减少你的数据处理时间

## 安装
```bash 
# 代码安装
git clone https://github.com/ctpbee/data_converter && cd data_converter && python setup.py install 

# pip 安装
pip install ctpbee_converter

```


## 简单使用 推荐使用工厂模式 

##### ext.py  中间文件
```
from ctpbee_converter import Converter
converter = Converter()
```
##### strategy.py 策略文件
 
```python
from ext import converter
from ctpbee import CtpbeeApi

class Strategy(CtpbeeApi):
    pass

# code in here 

```
#####  app.py
```
from ctpbee import CtpBee
from ext import converter
from strategy import Strategy

def create_app():
    app = Ctpbee("ctpbee", __name__)
    app.recorder.from_mapping(info)
    converter.init_app(app)
    # 策略载入 方式多种多样 
    # pass
    return app
```

#### manager.py
```
from app import create_app 
app = create_app()
app.start()

```
# 示范用例 
`converter.positions_df`



## 相关API
> is developing 
