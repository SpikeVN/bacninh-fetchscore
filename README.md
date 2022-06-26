# bacninh-fetchscore
Fetches score using reverse engineered API

## doc
```py
class Result()
    parameter   identifier        str

    property    id                str
    property    name              str
    property    birth_date        datetime
    property    school_name       str
    property    kk_score          float
    property    ngu_van           float
    property    tieng_anh         float
    property    toan_tluan        float
    property    toan_tngiem       float
    property    toan_tong         float
    property    mon_chuyen        float
    property    tong_chuyen       float
    property    tong_daitra       float

    method      to_dict()   ->    dict
    method      to_json()   ->    str
    method      to_csv()    ->    str
```
### dict structure
```py
{
    "sbd":           str,
    "ten":           str,
    "ngaysinh":      str,
    "truong":        str,
    "diemkk":        float,
    "nguvan":        float,
    "tienganh":      float,
    "toantluan":     float,
    "toantngiem":    float,
    "toantong":      float,
    "chuyen":        float,
    "tongchuyen":    float,
    "tongdaitra":    float
}
```

## example
```py
import hacklib

someone = hacklib.Result("012345")
someone.to_dict()  # -> {"sbd": ..., "ten": ..., ...}
print(someone.name) # -> JONATHAN GALINDO
```
