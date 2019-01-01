class Car():
    def __init__(self,license_number,color,model):
        self.license_number = license_number            # 车牌号
        self.color = color                              # 车颜色
        self.model = model                              # 车的型号

    # 车启动方法
    def car_started(self):
        print('车已启动')


    # 车停方法
    def car_stopping(self):
        print('车已停')
