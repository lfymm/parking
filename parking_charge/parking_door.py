class ParkingDoor():
    def __init__(self,door_color = 'striation',door_style = 'column'):
        self.door_color = door_color
        self.door_style = door_style

    # 进入停车场门打开方法
    def into_open_door(self):
        print('欢迎光临，请进入')

    # 出停车场门打开方法
    def out_open_door(self):
        print('小心慢行，欢迎下次光临')

    # 关门方法
    def close_door(self):
        print('停车场门已关')