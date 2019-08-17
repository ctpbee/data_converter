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


## 简单使用


```
from ctpbee import CtpBee
from ctpbee_converter import Converter

app = Ctpbee("ctpbee", __name__)
app.recorder.from_mapping(info)

converter = DataConverter(app)
# 或者通过
# converter = DataConverter()
# converter.init_app(app)


# 示范用例 
converter.get_positions()

```

## 相关API
> is developing 
