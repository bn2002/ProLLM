import os

def extract_unique_protein_ids(input_file_path, output_file_path):
    """
    Đọc file dữ liệu tương tác protein, trích xuất tất cả các ID protein duy nhất
    và lưu chúng vào một file đầu ra.

    Args:
        input_file_path (str): Đường dẫn đến file đầu vào (ví dụ: 'Human_PPI.tsv').
        output_file_path (str): Đường dẫn đến file đầu ra để lưu danh sách ID duy nhất.
    """
    protein_ids = set()

    try:
        with open(input_file_path, 'r') as f:
            # Bỏ qua dòng tiêu đề
            next(f)
            
            # Đọc từng dòng để trích xuất ID
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    # Thêm ID từ cột đầu tiên và thứ hai vào set
                    # Script gốc thay thế '9606.', ta cũng làm tương tự
                    protein_ids.add(parts[0].replace('9606.', ''))
                    protein_ids.add(parts[1].replace('9606.', ''))

        # Chuyển set thành list và sắp xếp (tùy chọn)
        sorted_ids = sorted(list(protein_ids))

        # Lưu danh sách ID duy nhất vào file đầu ra
        with open(output_file_path, 'w') as out_f:
            for protein_id in sorted_ids:
                out_f.write(protein_id + '\n')
        
        print(f"Hoàn thành! Đã tìm thấy {len(sorted_ids)} ID protein duy nhất.")
        print(f"Danh sách đã được lưu vào file: {output_file_path}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại '{input_file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# --- Bắt đầu thực thi ---
if __name__ == "__main__":
    # Thay đổi đường dẫn này thành đường dẫn thực tế đến file Human_PPI.tsv của bạn
    input_path = 'Human_PPI.tsv' 
    output_path = 'unique_protein_ids.txt'
    
    # Kiểm tra xem file input có tồn tại không trước khi chạy
    if not os.path.exists(input_path):
        print(f"File '{input_path}' không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
        print("Bạn cần đặt file Human_PPI.tsv vào cùng thư mục với script này, hoặc cung cấp đường dẫn đầy đủ.")
    else:
        extract_unique_protein_ids(input_path, output_path)