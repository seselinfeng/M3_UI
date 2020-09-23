import inspect
import json
import minium
import yaml


class BasePage(minium.MiniTest):
    _params = {}  # 参数化的数据

    def __init__(self):
        super(BasePage, self).__init__()

    def find(self, mini, locator, value: str = None):
        """
        查找元素
        :param locator:
        :param value:
        :return:
        """
        element = None
        if isinstance(locator, tuple):
            element = mini.page.get_element(*locator)
        elif isinstance(value, dict):
            element = mini.page.get_element(locator, **value)
        else:
            element = mini.page.get_element(locator, inner_text=value)
        return element

    def finds(self, mini, locator, value: str = None):
        """
        查找多个元素
        :param locator:
        :param value:
        :return:
        """
        elements: list
        if isinstance(locator, tuple):
            elements = mini.page.get_elements(*locator)
        elif isinstance(value, dict):
            element = mini.page.get_elements(locator, **value)
        else:
            element = mini.page.get_elements(locator, inner_text=value)
        return elements

    def step(self, mini, path: str = None):
        """
        操作步骤以及操作步骤的数据驱动
        :param path:
        :return:
        """
        element = None
        with open(path, encoding='utf-8') as f:
            # 获取调用函数的名称
            name = inspect.stack()[1].function
            # 反射原理获取当前函数的yaml数据驱动
            steps = yaml.safe_load(f)[name]
            # 序列化steps为字符串 Serialize ``obj`` to a JSON formatted ``str``.
            raw = json.dumps(steps)
            # 将yaml文件中特殊格式字符串转义为数据 ${name} --> name
            for key, value in self._params.items():
                raw = raw.replace('${' + key + '}', value)
            # 反序列化
            steps = json.loads(raw)
            for step in steps:
                if 'by' in step.keys():
                    if 'by' in step.keys():
                        element = self.find(mini, step.get('by'), step.get('locator'))
                    if 'action' in step.keys():
                        action = step.get('action')
                        if action == 'click':
                            # 点击事件
                            element.click()
                        if action == 'input':
                            # 输入文本
                            element.input(step.get('value'))
                        if action == 'get_text':
                            # 获取文本
                            element = element.text
        return element
