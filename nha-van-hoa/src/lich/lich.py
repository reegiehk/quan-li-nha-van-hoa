"""
Module: lich.py
Chức năng: placeholder quản lý lịch hoạt động của nhà văn hóa
"""

def them_su_kien(data_store, su_kien):
    """Thêm sự kiện (placeholder)."""
    # TODOs:
    # - Validate su_kien (title, start_time, end_time, organizer, resource_ids)
    # - Kiểm tra xung đột lịch (resource/room bị trùng giờ)
    # - Ghi vào data_store và trả về id sự kiện
    # - Viết unit tests cho conflict detection và creation
    raise NotImplementedError

def xoa_su_kien(data_store, su_kien_id):
    """Xóa sự kiện (placeholder)."""
    # TODOs:
    # - Kiểm tra sự kiện có tồn tại không
    # - Chỉ xóa khi chưa bắt đầu hoặc có quyền admin
    # - Xóa khỏi data_store
    # - Cập nhật liên kết với tài nguyên/phòng (nếu có)
    # - Ghi log xóa
    raise NotImplementedError


def cap_nhat_su_kien(data_store, su_kien_id, thong_tin_moi):
    """Cập nhật thông tin sự kiện (placeholder)."""
    #TODOs:
    # - Validate thông_tin_moi (time, title, organizer...)
    # - Kiểm tra không xung đột lịch sau khi cập nhật
    # - Cập nhật vào data_store
    # - Ghi log thay đổi (old_value → new_value)
    raise NotImplementedError


def tim_su_kien_theo_id(data_store, su_kien_id):
    """Tìm sự kiện theo ID (placeholder)."""
    #TODOs:
    # - Truy xuất sự kiện từ data_store
    # - Trả về event hoặc None
    raise NotImplementedError


def tim_su_kien_theo_ngay(data_store, ngay, thang, nam, gio):
    """Lấy danh sách sự kiện theo ngày/tháng/năm/giờ (placeholder)."""
     #TODOs:
    # - Chuẩn hóa input: chuyển ngay/thang/nam/gio về dạng integer
    # - Tạo datetime filter hoặc range filter phù hợp
    # - Lọc data_store theo các trường date/time
    # - Hỗ trợ tìm theo:
        # + chỉ ngày
        # + ngày + tháng
        # + giờ + ngày + tháng + năm 
        # + tháng + năm
        # + chỉ giờ
    # - Thêm unit test cho các dạng filter
    raise NotImplementedError


def kiem_tra_xung_dot(data_store, resource_ids, start_time, end_time):
    """Kiểm tra xem sự kiện có bị xung đột lịch không (placeholder)."""
    #TODOs:
    # - Duyệt tất cả sự kiện trong data_store
    # - Kiểm tra sự kiện nào dùng chung resource_ids
    # - Kiểm tra trùng giờ (time overlap)
    # - Trả về True nếu có xung đột, False nếu không
    # - Viết unit tests cho hàm này
    raise NotImplementedError


def danh_sach_su_kien(data_store, loc=None):
    """Lấy danh sách sự kiện (placeholder)."""
    #TODOs:
    # - Hỗ trợ lọc theo organizer, date, resource
    # - Trả về toàn bộ sự kiện nếu loc=None  
    raise NotImplementedError
