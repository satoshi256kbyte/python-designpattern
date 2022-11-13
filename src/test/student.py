
class Student:
    '''
    Adapterパターン　生徒クラス
    '''

    year: int = 0
    num: int = 0

    def __init__(self, year: int, num: int):
        self.year = year
        self.num = num

    def code(self) -> str:
        '''
        生徒番号を取得する
        '''
        return self.year + self.num.zfill(4)
