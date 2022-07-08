import logging

from airtest.core.api import start_app
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# cmd里面使用adb shell pm list packages 查看包名
# 或者使用代码os.system('adb shell pm list packages')查看
# 记得替换adb文件，airtest自带的40版本的，我们默认41版本的，或者运行代码的时候别启动airtest的IDE
# 以下屏蔽多余日志信息
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
start_app("com.stardust.kissreader")
# start_app是启动,stop_app是停止app,clear_app是清除缓存,其他的可以看文档或者百度或者点进去看
