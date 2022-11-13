
from abc import ABCMeta, abstractmethod


class SeirekiInterface(metaclass=ABCMeta):
    """
    Adapterパターン 西暦インターフェース
    """

    @abstractmethod
    def seireki_cd(self) -> str:
        """生徒コード(西暦版)を取得する
        Returns:
            str: 生徒コード(西暦版)
        """
