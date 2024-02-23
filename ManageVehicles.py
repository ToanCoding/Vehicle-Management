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
        self.currentVehicle = 0;
        self.revenue = 0


# Hàm thêm xe
    def add_entry(self):
        ticket_id = input("Nhập ID thẻ gửi xe: ")
        vehicle_type = input("Nhập loại xe (xe đạp(0)/xe máy(1)): ")
        license_plate = input("Nhập biển số xe: ")
        year, month, day, hour, minute = map(int, input("Nhập thời gian gửi xe(năm,tháng,ngày,giờ,phút): ").split(","))
        parking_time = datetime(year, month, day, hour, minute)
        new_vehicle = Vehicle(vehicle_type, license_plate, parking_time, ticket_id)
        self.vehicles.append(new_vehicle)
        self.currentVehicle += 1
        print("Đã thêm mới lượt gửi xe.")

#Hàm lấy xe

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
                    self.currentVehicle -= 1
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
                    self.currentVehicle -= 1
                else:
                    print("Lựa chọn không hợp lệ")
                found = True
        if not found:
            print("Không tìm thấy thông tin xe tương ứng.")

    def count_current_vehicles(self):
        return self.currentVehicle

#Hàm in ra danh sách xe trong nhà xe

    def list_vehicle(self):
        while True:
            print("1. Theo thời gian")
            print("2. Theo loại xe")
            choice = input("Nhập lựa chọn: ")
            if choice == "1":
                while True:
                    print("1. Tăng")
                    print("2. Giảm")
                    print("3. Quay lại")
                    choice2 = input("Nhập lựa chọn: ")
                    if choice2 == "1":
                        sorted_vehicles = sorted(self.vehicles, key=lambda x: x.parking_time)
                        break
                    elif choice2 == "2":
                        sorted_vehicles = sorted(self.vehicles, key=lambda x: x.parking_time, reverse=True)
                        break
                    elif choice2 == "3":
                        break
                    else:
                        print("Lựa chọn không hợp lệ")
                if choice2 == "3":
                    break
                else:
                    print("Danh sách các xe trong nhà xe:")
                    for index, vehicle in enumerate(sorted_vehicles, start=1):
                        print(
                            f"{index}. Biển số xe: {vehicle.license_plate}, Loại xe: {'Xe đạp' if vehicle.vehicle_type == '0' else 'Xe máy'}, Thời gian gửi xe: {vehicle.parking_time}")
            elif choice == "2":
                while True:
                    print("1. Xe đạp")
                    print("2. Xe máy")
                    print("3. Quay lại")
                    choice3 = input("Nhập lựa chọn: ")
                    if choice3 == "1":
                        filtered_vehicles = [vehicle for vehicle in self.vehicles if vehicle.vehicle_type == '0']
                        break
                    elif choice3 == "2":
                        filtered_vehicles = [vehicle for vehicle in self.vehicles if vehicle.vehicle_type == '1']
                        break
                    elif choice3 == "3":
                        break
                    else:
                        print("Lựa chọn không hợp lệ")
                if choice3 == "3":
                    break
                else:
                    print("Danh sách các xe trong nhà xe:")
                    for index, vehicle in enumerate(filtered_vehicles, start=1):
                        print(
                            f"{index}. Biển số xe: {vehicle.license_plate}, Loại xe: {'Xe đạp' if vehicle.vehicle_type == '0' else 'Xe máy'}, Thời gian gửi xe: {vehicle.parking_time}")
            else:
                print("Lựa chọn không hợp lệ")

#Hàm tính doanh thu
    def get_revenue_today(self):
        start_time = datetime.now().replace(hour=8)
        end_time = datetime.now().replace(hour=22)

        total_revenue_motorbike = 0
        total_revenue_bicycle = 0

        for vehicle in self.vehicles:
            if vehicle.checkout_time and start_time <= vehicle.checkout_time <= end_time:
                parking_fee = calculate_price(vehicle)
                if vehicle.vehicle_type == '1':
                    total_revenue_motorbike += parking_fee
                elif vehicle.vehicle_type == '0':
                    total_revenue_bicycle += parking_fee

            print(f"Doanh thu từ xe máy: {total_revenue_motorbike} VND")
        print(f"Doanh thu từ xe đạp: {total_revenue_bicycle} VND")
        print(f"Tổng doanh thu: {total_revenue_motorbike + total_revenue_bicycle} VND")

#Hàm tìm xe bị cảnh bao
    def alert_vehicles(self):
        current_time = datetime.now()

        for vehicle in self.vehicles:
            if vehicle.checkout_time:
                if vehicle.vehicle_type == '0':  # Xe đạp
                    if (current_time - vehicle.parking_time).days >= 3:
                        print(f"Cảnh báo: Xe đạp có biển số {vehicle.license_plate} đã gửi quá 3 ngày.")
                elif vehicle.vehicle_type == '1':  # Xe máy
                    if (current_time - vehicle.parking_time).days >= 5:
                        print(f"Cảnh báo: Xe máy có biển số {vehicle.license_plate} đã gửi quá 5 ngày.")

# Hàm in ra những xe bị mất vé
    def list_lost_tickets(self):
        lost_motorbike_tickets = []
        lost_bicycle_tickets = []

        for vehicle in self.vehicles:
            if not vehicle.paid and not vehicle.checkout_time:
                if vehicle.vehicle_type == '1':
                    lost_motorbike_tickets.append(vehicle)
                elif vehicle.vehicle_type == '0':
                    lost_bicycle_tickets.append(vehicle)

        if lost_motorbike_tickets:
            print("Danh sách xe máy bị mất vé:")
            for index, vehicle in enumerate(lost_motorbike_tickets, start=1):
                print(f"{index}. Biển số xe: {vehicle.license_plate}, ID thẻ gửi xe: {vehicle.ticket_id}")

        if lost_bicycle_tickets:
            print("Danh sách xe đạp bị mất vé:")
            for index, vehicle in enumerate(lost_bicycle_tickets, start=1):
                print(f"{index}. Biển số xe: {vehicle.license_plate}, ID thẻ gửi xe: {vehicle.ticket_id}")
                
# Hàm hiển thị xe có lượt gửi > 2 lần
    def frequent_motorbikes(self):
        motorbike_dict = {}

        for vehicle in self.vehicles:
            if vehicle.vehicle_type == '1':
                motorbike_dict.setdefault(vehicle.license_plate, 0)
                motorbike_dict[vehicle.license_plate] += 1

        frequent_motorbikes = [plate for plate, count in motorbike_dict.items() if count > 2]
        if frequent_motorbikes:
            print("Danh sách xe máy có số lượt gửi lớn hơn 2 lần:")
            for index, plate in enumerate(frequent_motorbikes, start=1):
                print(f"{index}. Biển số xe: {plate}")




