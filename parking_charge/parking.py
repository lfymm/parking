import time
from car import Car
from owner import Owner
from parking_door import ParkingDoor
from parking_space import ParkingSpace
from parking_record import ParkingRecord
from order import Order
class Parking():
    def __init__(self,free_space = 100,parking_name = 'it_park',park_address = 'muddy_south_area'):
        self.free_space = free_space
        self.parking_name = parking_name
        self.park_address = park_address
        self.car_list = []
    owner_car = dict()
    door = ParkingDoor()
    space = ParkingSpace()
    order = Order()
    # 停车方法
    def stop_car(self):
        if self.free_space > 0:
            car_number = input('请输入车牌号')
            owner_inform = input('请输入车主姓名')
            owner_tele = input('请输入车主联系方式')
            car_color = input('请输入车的颜色')
            car_model = input('请输入车的型号')
            owner = Owner(owner_inform,owner_tele)
            car = Car(car_number,car_color,car_model)
            self.owner_car['owner'] = 'car'
            self.car_list.append(car_number)
            self.free_space -= 1
            self.door.into_open_door()
            owner.drive(car)
            enter_time = time.time()
            ParkingRecord.car_record_list.append(enter_time)
            self.door.close_door()
            print('请将车停在'+str(self.space.space_number)+'号车位')
            self.space.static = 'full'
            ParkingSpace(self.space.space_number,self.space.static)
            enter_storage_time = time.time()
            ParkingRecord.car_record_list.append(enter_storage_time) 
            owner.stop(car)
            print('您已成功进入停车库')
        else:
            print('本停车场已满')

    # 出停车库方法
    def out_car(self):
        car_number = input('请输入车牌号')
        for car_num in self.car_list:
            if car_num == car_number:
                out_storage_time = time.time()
                ParkingRecord.car_record_list.append(out_storage_time)
                out_time = time.time()
                ParkingRecord.car_record_list.append(out_time)
                self.order.print_order(car_number)
                self.door.out_open_door()
                self.door.close_door()
            else:
                print('车牌号有误，不能进入')
                    
                    