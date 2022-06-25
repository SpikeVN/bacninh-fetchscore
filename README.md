# bacninh-fetchscore
Fetches score using reverse engineered API

## doc
```py
class    Result(identifier: str)
- method    to_dict()   ->   dict
- method    to_json()   ->   str
- method    to_csv()    ->   str
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
```
