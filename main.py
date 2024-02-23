from ManageVehicles import ManageVehicles
def main():
    manager = ManageVehicles()

    while True:
        print("\nQuản lý gửi xe:")
        print("1. Thêm mới lượt gửi xe")
        print("2. Lấy xe")
        print("3. Thống kê số lượng xe hiện tại")
        print("4. Thống kê doanh thu")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            manager.add_entry()

        elif choice == "2":
            manager.checkout()

        elif choice == "3":
            print("Số lượng xe hiện tại:", manager.count_current_vehicles())

        elif choice == "4":
            print("Doanh thu hiện tại:", manager.get_revenue())

        elif choice == "5":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
