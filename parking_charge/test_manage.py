from parking import Parking
class TestManage():
    park = Parking()
    while True:
        # 请车主选择停车还是出车
        choice = input(
        '''
        —————————————————————————
        |***欢迎进入车辆管理系统***|
        —————————————————————————  
        请选择功能：
                1.停车
                2.出车
                3.退出系统   
        '''
        )
        if choice == '1':
            park.stop_car()
        elif choice == '2':
            park.out_car()
        elif choice == '3':
            print('你已退出系统')
            break
        else:
            print('您输入的选项不在范围内，将为您返回主页')
            break