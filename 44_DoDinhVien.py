# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    new_student = {
        'name': name,
        'year_of_birth': year_of_birth,
        'address': address
    }
    student_list.append(new_student)
    print(f"Đã thêm sinh viên {name} thành công.")

def print_student_list():
    if not student_list:
        print("Danh sách trống.")
        return  
    for student in student_list:
        print(f"Tên: {student['name']}, Năm sinh: {student['year_of_birth']}, Địa chỉ: {student['address']}")

def search_student_by_name(name):
    found_students = [student for student in student_list if student['name'].lower() == name.lower()]
    if not found_students:
        print(f"Không tìm thấy sinh viên với tên: {name}")
    else:
        for student in found_students:
            print(f"Tên: {student['name']}, Năm sinh: {student['year_of_birth']}, Địa chỉ: {student['address']}")

if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ---")
    
    # Yêu cầu 1: Thêm sinh viên
    print("\n1. Thêm sinh viên:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    # Yêu cầu 2: In danh sách
    print("\n2. In danh sách sinh viên:")
    print_student_list()

    # Yêu cầu 3: Tìm kiếm
    print("\n3. Tìm kiếm sinh viên theo tên 'an':")
    search_student_by_name("an")
    
    print("\nTìm kiếm sinh viên theo tên 'Dung':")
    search_student_by_name("Dung")
# DoDinhVien.py