import datetime
import json

from .engine import make_rq, _analyze


class Result:
    def __init__(self, identifier: str):
        """
        Finds a result entry with matching name or identification number

        :param identifier str: the identifier. Number must be converted into strings since they have leading zero.
        """
        self.__kw = str(identifier)
        rq = make_rq(self.__kw)
        c = _analyze(make_rq(self.__kw))
        self.exist = True
        try:
            self.__content = {
                "id": c[0],
                "name": c[1],
                "birth_date": c[2],
                "school_name": c[3],
                "kk_score": float(c[4]),
                "ngu_van": float(c[5]),
                "tieng_anh": float(c[6]),
                "toan_tluan": float(c[7]),
                "toan_tngiem": float(c[8]),
                "toan_tong": float(c[9]),
                "mon_chuyen": float(c[10]),
                "tong_chuyen": float(c[11]),
                "tong_daitra": float(c[12]),
            }
            date_sep = c[2].split("/")
            self.id = c[0]
            self.name = c[1]
            self.birth_date = datetime.date(*[int(i) for i in date_sep[::-1]])
            self.school_name = c[3]
            self.kk_score = float(c[4])
            self.ngu_van = float(c[5])
            self.tieng_anh = float(c[6])
            self.toan_tluan = float(c[7])
            self.toan_tngiem = float(c[8])
            self.toan_tong = float(c[9])
            self.mon_chuyen = float(c[10])
            self.tong_chuyen = float(c[11])
            self.tong_daitra = float(c[12])
        except ValueError:
            self.__content = {}
            self.exist = False
            self.id = identifier
            self.name = None
            self.birth_date = None
            self.school_name = None
            self.kk_score = None
            self.ngu_van = None
            self.tieng_anh = None
            self.toan_tluan = None
            self.toan_tngiem = None
            self.toan_tong = None
            self.mon_chuyen = None
            self.tong_chuyen = None
            self.tong_daitra = None

    def to_json(self) -> str:
        return json.dumps(self.__content, ensure_ascii=False)

    def to_dict(self) -> dict:
        return self.__content

    def to_csv(self) -> str:
        return "".join([str(i) + "," for i in self.__content.values()])[:-1]
