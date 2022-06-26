import time
import requests

URL = "http://bacninh.edu.vn/?module=Content.Listing&moduleId=1015&cmd=redraw&site=45610&url_mode=rewrite&submitFormId=1015&moduleId=1015&page=&site=45610"

BODY = {
    "layout": "Decl.DataSet.Detail.default",
    "itemsPerPage": 1000,
    "pageNo": 1,
    "service": "Content.Decl.DataSet.Grouping.select",
    "itemId": "62afcd34dc1a96b675037542",
    "gridModuleParentId": 15,
    "type": "Decl.DataSet",
    "page": "",
    "modulePosition": 0,
    "moduleParentId": -1,
    "orderBy": "",
    "unRegex": "",
    "keyword": "",
    "_t": time.time()
}

STRIP_TARGET = """ </td> </tr> </tbody> </table></div></div><div id="pagination1015" class="default-pagination mb-20"></div><style> .input-search{ margin-bottom: 12px; }"""

def _analyze(data: str) -> str:
    return data.split("\n")[21][36:].replace(STRIP_TARGET, " ").replace("</td>  <td  >", " ").strip().split("  ")



def make_rq(keyword: str) -> str:
    a = BODY.copy()
    a["keyword"] = keyword
    r = requests.post(URL, data=a)
    return r.text
