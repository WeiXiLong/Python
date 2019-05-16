class Car():
    """一次模拟描述汽车的属性"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_nmae =  str(self.year) + " " + self.make.title() + " " + self.model.title()
        return long_nmae

    def read_odometer(self):
         """打印一条信息，指出汽车的里程"""
         print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程数往回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,milse):
        """将里程表读数增加指定的量"""
        self.odometer_reading += milse



