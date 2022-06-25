from time import time
import requests
import time
import json

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

ONE = """<div class="cont-dataset-detail"><h2 class="title-exam">Tra cứu điểm thi tuyển sinh lớp 10 năm 2022</h2>  <div id="search-type1015" class="search-type"> <b>Tìm theo:</b> <span>Số báo danh, Họ và tên</span>
</div> <div style="margin-top: 13px; display: none"> <div class="showSearch-box" style="color:#ff6633;"><i class="fa fa-search" aria-hidden="true" style="margin-right: 5px;"></i> <a href="javascript:;" id="showSearch" style="color:#ff6633;">Tìm kiếm nâng cao</a></div> <div class="hideSearch-box" style="color:#ff6633;"><i class="fa fa-search" aria-hidden="true" style="margin-right: 5px;"></i> <a href="javascript:;" id="hideSearch" style="color:#ff6633;">Tìm kiếm rút gọn</a></div> </div> <div id="box-search-dataset" class="box-search" style="margin-top: 30px;color: #ff6633;display: none"> <form method="post"> <div class="row" style="width: 85%;"> <div class="col-md-3"> <select id="changeListType1015" class="form-control" name="certificateId" onchange="VHV.App.modules[1015].filters.certificateId = this.value.trim(); VHV.App.modules[1015].pageNo = 1; VHV.App.modules[1015].reload();"> <option selected="selected" value="">Tất cả</option>
<option  value="1">Bằng tốt nghiệp Trung học cơ sở</option>
<option  value="2">Bằng tốt nghiệp Trung học phổ thông</option>
<option  value="3">Bằng tốt nghiệp đại học</option>
<option  value="4">Bằng thạc sĩ</option>
<option  value="5">Bằng tiến sĩ</option>
</select> </div> <div class="col-md-3"> <div class="input-search"> <input type="text" class="form-control" onchange="VHV.App.modules[1015].filters.code = this.value.trim(); VHV.App.modules[1015].pageNo = 1; VHV.App.modules[1015].reload();" value="" placeholder="Số hiệu bằng" /> </div> </div> <div class="col-md-3"> <div class="input-search"> <input type="text" class="form-control" onchange="VHV.App.modules[1015].filters.cardId = this.value.trim(); VHV.App.modules[1015].pageNo = 1; VHV.App.modules[1015].reload();" value="" placeholder="Số CMND" /> </div> </div> <div class="col-md-3"> <div class="input-search"> <input type="text" class="form-control" onchange="VHV.App.modules[1015].filters.dateRange = this.value.trim(); VHV.App.modules[1015].pageNo = 1; VHV.App.modules[1015].reload();" value="" placeholder="Năm cấp"/> </div> </div> </div> <input type="hidden" name="securityToken" value=\""""

TWO = """<input type="hidden" name="submitFormId" value="1015"><input type="hidden" name="moduleId" value="1015"></form> </div><div id="pagination1015" class="default-pagination text-center"></div><em>1 bản ghi</em><div class="table-responsive" >
<table class="table table-bordered table-hover"> <thead>  <tr>  <th scope="col" class="text-center" style=""  >Số báo danh</th>
 <th scope="col" class="text-center" style=""  >Họ và tên</th>
 <th scope="col" class="text-center" style=""  >Ngày sinh</th>
 <th scope="col" class="text-center" style=""  >Trường</th>
 <th scope="col" class="text-center" style=""  >Điểm Khuyến khích</th>
 <th scope="col" class="text-center" style=""  >Ngữ Văn</th>
 <th scope="col" class="text-center" style=""  >Tiếng Anh</th>
 <th scope="col" class="text-center" style=""  >Toán Tự Luận</th>
 <th scope="col" class="text-center" style=""  >Toán Trắc Nghiệm</th>
 <th scope="col" class="text-center" style=""  >Tổng toán</th>
 <th scope="col" class="text-center" style=""  >Môn Chuyên</th>
 <th scope="col" class="text-center" style=""  >Tổng Chuyên</th>
 <th scope="col" class="text-center" style=""  >Tổng đại trà</th>"""

FOUR = """)),{"module":"Content.Listing","page":"","id":"1015","modulePosition":"0","moduleParentId":"-1"}),{ totalItems: 1, filters: [], itemsPerPage: 1000, pageNo: 1, orderBy: "", unRegex: ''}, function(){
if(this.gridModuleParentId) { var that = this; VHV.ExecQueue.add(function(){ VHV.App.modules[that.gridModuleParentId].dataSetModule = that; }, function(){
return VHV.App.modules[that.gridModuleParentId]; });
}
});
$('#keyword15').parents('.search-key').show().next().addClass('col-md-9');$('#keyword15').show().attr('placeholder', $('#search-type1015').text());</script>"""


def _analyze(data: str) -> str:
    ndata = data
    ndata = ndata.replace(ONE, " ")
    ndata = ndata.replace(TWO, " ")
    ndata = ndata.replace(""".hideSearch-box, #box-search-dataset{ display:none; }
</style><script type="text/javascript">;""", " ")
    ndata = ndata.replace("""$('#showSearch').click(function(){ $('#box-search-dataset').show(); $('.showSearch-box').css("display", "none"); $('.hideSearch-box').css("display", "block");});
$('#hideSearch').click(function(){ $('#box-search-dataset').hide(); $('.showSearch-box').css("display", "block"); $('.hideSearch-box').css("display", "none");});""", " ")
    ndata = ndata.replace("""$('.BDC_CaptchaDiv').parents('td:first').hide();$('.BDC_CaptchaDiv').next('.capcha-text').attr('disabled', 'disabled');VHV.using ($.extend(""", " ")
    ndata = ndata.replace(FOUR, " ")

    ndatas = ndata.split("\n")
    del ndatas[-1]
    del ndatas[-1]
    del ndatas[-1]
    del ndatas[-1]
    del ndatas[0]
    
    ndata = "".join(ndatas)

    ndata  = ndata.replace("""</td> </tr> </tbody> </table></div></div><div id="pagination1015" class="default-pagination mb-20"></div><style> .input-search{ margin-bottom: 12px; }""", " ")
    ndata = ndata.replace("""</tr> </thead> <tbody>  <tr>  <td  >""", " ")
    ndata = ndata.replace("</td>  <td  >", " ")
    ndata = ndata[1:-1]
    return ndata


class Result:
    def __init__(self, identifier: str):
        """
        Finds a result entry with matching name or identification number

        
        :param identifier str: the identifier. Number must be converted into strings since they have leading zero.
        """
        self.kw = None
        if isinstance(identifier, int):
            self.kw = str(identifier)
        else:
            self.kw = identifier

        self.body = BODY
        self.body["keyword"] = self.kw
        r = requests.post(URL, data=BODY)
        c = _analyze(r.text).split("  ")
        self.content = {
            "sbd": c[0],
            "ten": c[1],
            "ngaysinh": c[2],
            "truong": c[3],
            "diemkk": float(c[4]),
            "nguvan": float(c[5]),
            "tienganh": float(c[6]),
            "toantluan": float(c[7]),
            "toantngiem": float(c[8]),
            "toantong": float(c[9]),
            "chuyen": float(c[10]),
            "tongchuyen": float(c[11]),
            "tongdaitra": float(c[12]),
        }

    def to_json(self) -> str:
        return json.dumps(self.content, ensure_ascii=False)

    def to_dict(self) -> dict:
        return self.content

    def to_csv(self) -> str:
        return "".join([str(i) + "," for i in self.content.values()])
