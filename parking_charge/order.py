from parking_record import ParkingRecord
class Order():
    def __init__(self):
        pass
    
    # 订单方法
    def print_order(self,car_number):
        print('车牌号：'+car_number)
        enter_time = ParkingRecord.car_record_list[0]
        out_time = ParkingRecord.car_record_list[3]
        print('停车费每小时5元')
        park_time = out_time - enter_time
        hour = park_time // 3600
        mm = (park_time - 3600 * hour) // 60
        ss = str(park_time - 3600 * hour -mm * 60)[0:3]
        remainder = park_time % 3600
        if remainder == 0:
            park_money = hour * 5
        else:
            park_money = hour * 5 + 5
        print('您本次停车'+str(hour)+'小时'+str(mm)+'分钟'+ss+'秒，请交停车费'+str(park_money)+'元')
