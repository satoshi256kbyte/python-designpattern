
class Student:
    """
    Adapterパターン　生徒クラス
    """

    year: int = 0
    department: str
    cource: str
    num: int = 0

    def __init__(self, year: int, department: str, course: str):
        """コンストラクタ
        Args:
            year (int): 年度
            department (str): 学部
            course (str): 学科
            num (int): 連番
        """
        self.year = year
        self.department = department
        self.course = course

    def code(self) -> str:
        """生徒コードを返す
        Returns:
            str: 生徒コード
        """

        # まだ連番が振られてない場合、年度・学部・学科ごとの連番を自動採番する
        # このソースでは長くなるので省略

        return str(self.year).zfill(2) \
            + self.department \
            + self.course \
            + str(self.num).zfill(4)
