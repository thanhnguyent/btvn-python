class Error(Exception):
    '''Base class cho game error'''
    pass


class MaximumPlayerError(Error):
    '''Vượt quá số lượng người chơi cho phép !'''

    message = 'Số lượng người chơi quá đông!\n'

    def __init__(self, message=message):
        self.message = message


class MinimumPlayerError(Error):
    '''Không đủ người chơi '''

    message = 'Đang quá ít người chơi:v\n'

    def __init__(self, message=message):
        self.message = message


class PlayerDoesNotExistsError(Error):
    '''Không tồn tại người chơi này'''

    message = '''Không tồn tại ID người chơi\n'''

    def __init__(self, message=message):
        self.message = message


class PlayingError(Error):
    '''Lỗi thao tác khi game đang chơi'''

    message = 'Tạm dừng một chút, có người chơi ra ngoài \n'

    def __init__(self, message=message):
        self.message = message


class DealtError(Error):
    '''Lỗi chia bài nhiều lần'''

    message = 'Đã chia bài !)\n'

    def __init__(self, message=message):
        self.message = message


class NotDealtError(Error):
    '''Lỗi lật bài khi chưa chia'''

    message = 'Bài chưa được chia\n'

    def __init__(self, message=message):
        self.message = message


class FlippedError(Error):
    '''Lỗi lật bài nhiều lần'''

    message = 'Lật bài rồi\n'

    def __init__(self, message=message):
        self.message = message


class FunctionDoesNotExists(Error):
    '''Lỗi chọn chức năng không tồn tại'''

    message = 'Chức năng không tồn tại\n'

    def __init__(self, message=message):
        self.message = message


class CancelError(Error):
    '''Lỗi khi hủy chức năng, ví dụ hủy xóa người chơi'''

    def __init__(self, message=''):
        self.message = message
