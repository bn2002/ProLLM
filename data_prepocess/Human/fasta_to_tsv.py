def convert_fasta_to_tsv(fasta_file_path, tsv_file_path):
    """
    Chuyển đổi file FASTA từ UniProt thành file TSV hai cột (ID, Sequence)
    theo yêu cầu của script generate_embedding.py.

    Args:
        fasta_file_path (str): Đường dẫn đến file .fasta đã tải về.
        tsv_file_path (str): Đường dẫn đến file .tsv đầu ra.
    """
    protein_dict = {}
    current_id = None

    try:
        with open(fasta_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('>'):
                    # Dòng header, trích xuất ID từ nó
                    # Ví dụ: >sp|P12345|... -> P12345
                    current_id = line.split('|')[1]
                    protein_dict[current_id] = ""
                elif current_id:
                    # Dòng sequence, nối vào protein hiện tại
                    protein_dict[current_id] += line

        with open(tsv_file_path, 'w') as out_f:
            for protein_id, sequence in protein_dict.items():
                out_f.write(f"{protein_id}\t{sequence}\n")

        print(f"Hoàn thành! Đã chuyển đổi {len(protein_dict)} protein.")
        print(f"File kết quả đã được lưu tại: {tsv_file_path}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại '{fasta_file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# --- Bắt đầu thực thi ---
if __name__ == "__main__":
    # Thay đổi tên file này thành tên file FASTA bạn đã tải về
    input_fasta = "idmapping_2025_06_30.fasta"

    # Tên file đầu ra mà script generate_embedding.py sẽ sử dụng
    output_tsv = "human_multiclass_protein_dictionary.tsv"

    convert_fasta_to_tsv(input_fasta, output_tsv)