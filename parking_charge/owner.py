class Owner():
    def __init__(self,owner_name,phone_number):
        self.owner_name = owner_name                # 车主姓名
        self.phone_number = phone_number            # 车主联系方式

    # 车主开车方法
    def drive(self,car):
        car.car_started()
    
    # 车主停车方法
    def stop(self,car):
        car.car_stopping()

    # 车主付停车费方法
    def paying(self):
        pass