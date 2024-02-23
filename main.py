from ManageVehicles import ManageVehicles
def main():
    manager = ManageVehicles()

    while True:
        print("\nQuản lý gửi xe:")
        print("1. Thêm mới lượt gửi xe")
        print("2. Lấy xe")
        print("3. Thống kê số lượng xe hiện tại")
        print("4. Danh sách xe trong nhà xe")
        print("5. Thống kê doanh thu ngày")
        print("6. Hiển thị danh sách xe bị cảnh báo")
        print("7. Hiển thị danh sách xe bị mất vé xe")
        print("8. Hiển thị danh sách xe máy gửi trên 2 lần trong ngày")
        print("9. Thoát")

        choice = input("Chọn chức năng (1-9): ")

        if choice == "1":
            manager.add_entry()

        elif choice == "2":
            manager.checkout()

        elif choice == "3":
            print("Số lượng xe hiện tại:", manager.count_current_vehicles())

        elif choice == "4":
            manager.list_vehicle()

        elif choice == "5":
            manager.get_revenue_today()

        elif choice == "6":
            manager.alert_vehicles()

        elif choice == "7":
            manager.list_lost_tickets()

        elif choice == "8":
            manager.frequent_motorbikes()

        elif choice == "9":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
