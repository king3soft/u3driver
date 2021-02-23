from u3driver import AltrunUnityDriver
import os
import argparse
import uiautomator2 as u2
import uautoTest

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help="ip")   # 命令行参数 -i ip地址
    parser.add_argument('-s', help="device serial")   # 命令行参数 -s 设备号

    args = parser.parse_args()
    ip = args.i or None
    device_s = args.s #one plus 7t

    if ip == None:
        try:
            res = os.popen(f"adb -s {device_s} shell ifconfig").read()
            ip = res.split('wlan0')[1].split('inet addr:')[1].split(' ')[0]
        except:
            try:
                res = os.popen(f'adb -s {device_s} shell netcfg').read()
                ip = res.split('wlan0')[1].split('UP')[1].split('/')[0].split()[0]
            except:
                res = os.popen(f'adb -s {device_s} shell netstat').read()
                ip = res.split('udp')[1].split(':bootpc')[0].split(' ')[-1]

    # device_s = 0  # 设备号
    # platform = 0  # 平台
    # ip = 0   # 启动游戏机器的ip地址
    # TCP_PORT = 0  # 端口号
    # timeout = 0  # 超时重试时间
    udriver = AltrunUnityDriver(device_s,"",ip,TCP_PORT=13000,timeout=60)

    # # 录制，目前只支持点击，拖动，文本输入的录制
    # udriver.debug_mode("uautoTest.py")

    # # 回放
    # uautoTest.AutoRun(udriver)

    # # 获取游戏物体
    # udriver.find_object(By.PATH,"//UICamera//Loadout//OpenLeaderboard")

    # # 对游戏对象发起点击事件
    # udriver.find_object(By.PATH, "//UICamera//Loadout//OpenLeaderboard").tap()

    # # 判断物体是否存在且活动
    # udriver.object_exist(By.PATH,"//UICamera//Loadout//OpenLeaderboard")

    # # 获取一个父游戏物体的所有直接子游戏物体的名字
    # udriver.find_child("//UICamera//Leaderboard//Background")

    # # 按名字获取父物体的直接子物体
    # udriver.find_object(By.PATH,"//UICamera//Leaderboard//Background//Display").find("Score")

    # # 按索引获取父物体下的子物体
    # udriver.find_object(By.PATH,"//UICamera//Leaderboard//Background//Display").child_index(1)

    # # 获取游戏对象的text值，该游戏对象必须拥有Text或InputField组件
    # udriver.find_object(By.PATH,"//UICamera//Leaderboard//Background//Display//Score").find("Score").get_text()

    
    # # 得到屏幕宽高
    # width,height = udriver.get_screen()

    # # 对游戏进行截图
    # objects = udriver.get_png_screenshot("pic.jpg")

    # # 寻找所有名字包含value且活动（avtive）的游戏对象，返回的列表中包含所找到的游戏对象
    # objects = udriver.find_object_which_contains("/UI/UI_Main/Panel/MainBtn/BtnAct",By.NAME)

    # # 在指定的路径下寻找名字包含value且活动（active）的直接子游戏对象，返回的列表中包含所有找到的游戏对象
    # objects = udriver.find_object_in_range_where_name_contains("BtnAct","//UI//UI_Main//Panel")

    # # 在父游戏物体的子孙级物体下寻找文本内容包含text且活动（avtive）的游戏物体放回的列表中包含所有找到的游戏物体
    # objects = udriver.find_object_in_range_where_text_contains("value","text")

    # # 获取一个UI矩形的中心的和四个顶点的屏幕坐标
    # ret = udriver.get_object_rect("//UI//UI_Main//Panel//MainBtn//BtnAct")
    # print(ret['Center'])
    # print(ret['BottomLeft'])
    # print(ret['TopLeft'])
    # print(ret['TopRight'])
    # print(ret['BottomRight'])

    # # 获取一个物体下的所有子孙级物体，返回的列表中包含所有找到的游戏对象
    # objects = udriver.find_all_objects("//Canvas")

    # # 获取所有 text 包含对应文本的游戏物体，该游戏物体必须拥有 Text 或 InputField 组件，返回的列表中包含所有找到的游戏对象
    # objects = udriver.find_all_objects_where_text_contains("text")

    # # 给游戏对象的 text 属性设置值，该游戏对象必须拥有 InputField 组件
    # text = udriver.find_object(By.PATH, "//Canvas//Text")
    # str = text.set_text('this is text')

    # # 寻找游戏物体，如果找到且是活动（active）的，对游戏对象发起一次点击事件
    # udriver.find_object_and_tap(By.PATH, "//Canvas//Button")

    # # 对屏幕上指定一点的 UI 触发点击事件
    # udriver.tap_at_coordiates("480", "720")

    # # 获取一个游戏物体中指定的组件上的指定值
    # ret = udriver.get_value_on_component("//Canvas//Image", "Image", "color")

    # # 对 UI 控件触发拖动事件
    # udriver.drag_object("//Canvas//Slider", 400, 200)
    # udriver.drag_object("//Canvas//Slider", 400, 100, 400, 200)

    # storeName = udriver.find_object(By.PATH, "//UI//UI_ShopNew//PnlStory//ToggleTab//List").child_index(3).find("Text").get_text()

    uiauto = u2.connect(udriver.appium_driver)  # uiautomator2初始化

    uiauto.click(500,1205,0.5)  # 点击

    # uiauto.long_click(1000,500,0.5)  # 长按

    # uiauto.drag(1000,1000,1500,500,0.5)   # 拖动

    # uiauto.swipe(500,300,1000,300,0.5)   # 滑动

    udriver.stop()