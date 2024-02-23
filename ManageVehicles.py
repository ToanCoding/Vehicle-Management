from datetime import datetime


class Vehicle:
    def __init__(self, vehicle_type, license_plate, parking_time, ticket_id):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.parking_time = parking_time
        self.ticket_id = ticket_id
        self.checkout_time = None
        self.paid = False


def calculate_price(vehicle):
    parking_fee = 0
    if vehicle.checkout_time.day == vehicle.parking_time.day:
        if vehicle.vehicle_type == '0':
            parking_fee = 2000 if vehicle.checkout_time.hour <= 18 else 4000
        elif vehicle.vehicle_type == '1':
            parking_fee = 3000 if vehicle.checkout_time.hour <= 18 else 6000
    elif vehicle.checkout_time.day > vehicle.parking_time.day:
        nights = vehicle.checkout_time.day - vehicle.parking_time.day
        if vehicle.vehicle_type == '0':
            parking_fee = 2000 + 15000 * nights if vehicle.checkout_time.hour <= 18 else 4000 + 15000 * nights
        elif vehicle.vehicle_type == '1':
            parking_fee = 3000 + 30000 * nights if vehicle.checkout_time.hour <= 18 else 6000 + 30000 * nights
    else:
        print("Ngày lấy xe không hợp lệ")
    return parking_fee


class ManageVehicles:
    def __init__(self):
        self.vehicles = []
        self.revenue = 0

    def add_entry(self):
        ticket_id = input("Nhập ID thẻ gửi xe: ")
        vehicle_type = input("Nhập loại xe (xe đạp(0)/xe máy(1)): ")
        license_plate = input("Nhập biển số xe: ")
        year, month, day, hour, minute = map(int, input("Nhập thời gian gửi xe(năm,tháng,ngày,giờ,phút): ").split(","))
        parking_time = datetime(year, month, day, hour, minute)
        new_vehicle = Vehicle(vehicle_type, license_plate, parking_time, ticket_id)
        self.vehicles.append(new_vehicle)
        print("Đã thêm mới lượt gửi xe.")

    def checkout(self):
        ticket_id = input("Nhập ID thẻ gửi xe: ")
        vehicle_type = input("Nhập loại xe (xe đạp(0)/xe máy(1)): ")
        license_plate = input("Nhập biển số xe: ")

        found = False
        for vehicle in self.vehicles:
            if vehicle.ticket_id == ticket_id and vehicle.vehicle_type == vehicle_type and vehicle.license_plate == license_plate:
                year, month, day, hour, minute = map(int, input(
                    "Nhập thời gian trả xe(year,month,day,hour,minute): ").split(","))
                vehicle.checkout_time = datetime(year, month, day, hour, minute)
                vehicle.paid = True
                parking_fee = calculate_price(vehicle)
                print(f"Phí gửi xe của xe {vehicle.license_plate} là: {parking_fee} VND")

                print("1. Đã thanh toán")
                print("2. Chưa thanh toán")
                print("3. Mất vé xe")

                choice = input("Nhập lựa chọn (1-3): ")
                if choice == "1":
                    self.revenue += parking_fee
                    print("Xe được phép ra")
                elif choice == "2":
                    print("Chưa thanh toán, chưa được phép ra")
                elif choice == "3":
                    if vehicle_type == "1":
                        parking_fee = 60000
                    elif vehicle_type == "2":
                        parking_fee = 30000
                    print(f"Phí phạt mất xe là {parking_fee}")
                    self.revenue += parking_fee
                else:
                    print("Lựa chọn không hợp lệ")
                found = True
        if not found:
            print("Không tìm thấy thông tin xe tương ứng.")

    def count_current_vehicles(self):
        return len(self.vehicles)

    def get_revenue(self):
        return self.revenue
