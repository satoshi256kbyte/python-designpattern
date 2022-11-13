
from student import Student
from seireki_interface import SeirekiInterface


class SeirekiStudent(Student, SeirekiInterface):
    """
    Adapterパターン　生徒(西暦Ver)クラス
    """

    def seireki_cd(self) -> str:
        """生徒コード(西暦版)を取得する
        Returns:
            str: 生徒コード(西暦版)
        """
        code: str = self.code()

        # コードが12桁以上なら西暦＋４桁の番号になってるのでそのまま返却
        if (len(code) >= 12):
            return code

        year: int = int(code[0:2])
        # 令和元年〜10年の場合
        # 令和5年以降は年そのものに西暦が入力されていく予定
        if (year <= 10):
            year = year + 2018

        # 平成元年〜31年の場合
        if (year <= 31):
            year = year + 1988

        return str(year).zfill(2) \
            + self.department \
            + self.course \
            + str(self.num).zfill(4)
        