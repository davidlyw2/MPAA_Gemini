# -*- coding: utf-8 -*-

TR_LIST = {'CSPAT00600':'현물정상주문', 'ChartIndex':'차트지표데이터조회', 'CHARTINDEX':'차트지표데이터조회', 'CSPAQ12300':'현물계좌 잔고내역 조회', 'CSPAQ22200':'현물계좌 예수금/주문가능금액/총평가 조회',
           'CSPAT00800':'현물취소주문', 'CSPAT00700':'현물정정주문', 'CSPAQ13700':'현물계좌 주문체결내역 조회', 't0425':'주식체결/미체결', 't8410':'주식차트(일주월년)', 't8411':'주식차트(틱/n틱)',
           't8412':'주식차트(N분분)', 't8430':'주식종목 조회', 't8451':'주식종목 조회', 't1444':'시가총액상위', 't8424':'업종전체조회', 't1441':'등락율 상위', 't1866':'서버저장조건리스트 조회', 't1857':'e종목검색 조회',
           't1901': 'ETF 현재가(시세) 조회', 't1903': 'ETF 일별 추이', 't1101':'주식 현재가 호가 조회', 't1102':'주식 현재가 조회', 't1486':'시간대별 예상 체결가', 't8407':'주식멀티현재가조회', 't1637':'종목별프로그램매매추이', 't1716':'외인기관종목별동향', 't1764':'거래원리스트', 't1771':'거래원별누적', 't1752':'종목별상위회원사', 't8436':'주식클릭종목조회',
           't1702':'외인기관종목별동향', 't1717':'외인기관별종목별동향', 't8425':'전체테마', 't8424':'업종전체조회', 't1532':'종목별 테마', 't1531':'섹터별 종목'
        }

# 현물계좌 잔고내역 조회 : CSPAQ12300
CSPAQ12300_IN_BLOCK_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'BalCreTp', 'CmsnAppTpCode', 'D2balBaseQryTp', 'UprcTpCode']
CSPAQ12300_IN_BLOCK_NAME = ['레코드갯수', '계좌번호', '비밀번호', '잔고생성구분', '수수료적용구분', 'D2잔고기준조회구분', '단가구분']
CSPAQ12300_OUT_BLOCK_1_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'BalCreTp', 'CmsnAppTpCode', 'D2balBaseQryTp', 'UprcTpCode']
CSPAQ12300_OUT_BLOCK_1_NAME = ['레코드갯수', '계좌번호', '비밀번호', '잔고생성구분', '수수료적용구분', 'D2잔고기준조회구분', '단가구분']
CSPAQ12300_OUT_BLOCK_2_CODE = ['RecCnt', 'BrnNm', 'AcntNm', 'MnyOrdAbleAmt', 'MnyoutAbleAmt', 'SeOrdAbleAmt', 'KdqOrdAbleAmt', 'HtsOrdAbleAmt', 'MgnRat100pctOrdAbleAmt', 'BalEvalAmt', 'PchsAmt', 'RcvblAmt', 'PnlRat', 'InvstOrgAmt', 'InvstPlAmt', 'CrdtPldgOrdAmt', 'Dps', 'D1Dps', 'D2Dps', 'OrdDt', 'MnyMgn', 'SubstMgn', 'SubstAmt', 'PrdayBuyExecAmt', 'PrdaySellExecAmt', 'CrdayBuyExecAmt', 'CrdaySellExecAmt', 'EvalPnlSum', 'DpsastTotamt', 'Evrprc', 'RuseAmt', 'EtclndAmt', 'PrcAdjstAmt', 'D1CmsnAmt', 'D2CmsnAmt', 'D1EvrTax', 'D2EvrTax', 'D1SettPrergAmt', 'D2SettPrergAmt', 'PrdayKseMnyMgn', 'PrdayKseSubstMgn', 'PrdayKseCrdtMnyMgn', 'PrdayKseCrdtSubstMgn', 'CrdayKseMnyMgn', 'CrdayKseSubstMgn', 'CrdayKseCrdtMnyMgn', 'CrdayKseCrdtSubstMgn', 'PrdayKdqMnyMgn', 'PrdayKdqSubstMgn', 'PrdayKdqCrdtMnyMgn', 'PrdayKdqCrdtSubstMgn', 'CrdayKdqMnyMgn', 'CrdayKdqSubstMgn', 'CrdayKdqCrdtMnyMgn', 'CrdayKdqCrdtSubstMgn', 'PrdayFrbrdMnyMgn', 'PrdayFrbrdSubstMgn', 'CrdayFrbrdMnyMgn', 'CrdayFrbrdSubstMgn', 'PrdayCrbmkMnyMgn', 'PrdayCrbmkSubstMgn', 'CrdayCrbmkMnyMgn', 'CrdayCrbmkSubstMgn', 'DpspdgQty', 'BuyAdjstAmtD2', 'SellAdjstAmtD2', 'RepayRqrdAmtD1', 'RepayRqrdAmtD2', 'LoanAmt']
CSPAQ12300_OUT_BLOCK_2_NAME = ['레코드갯수', '지점명', '계좌명', '현금주문가능금액', '출금가능금액', '거래소금액', '코스닥금액', 'HTS주문가능금액', '증거금률100퍼센트주문가능금액', '잔고평가금액', '매입금액', '미수금액', '손익율', '투자원금', '투자손익금액', '신용담보주문금액', '예수금', 'D1예수금', 'D2예수금', '주문일', '현금증거금액', '대용증거금액', '대용금액', '전일매수체결금액', '전일매도체결금액', '금일매수체결금액', '금일매도체결금액', '평가손익합계', '예탁자산총액', '제비용', '재사용금액', '기타대여금액', '가정산금액', 'D1수수료', 'D2수수료', 'D1제세금', 'D2제세금', 'D1결제예정금액', 'D2결제예정금액', '전일KSE현금증거금', '전일KSE대용증거금', '전일KSE신용현금증거금', '전일KSE신용대용증거금', '금일KSE현금증거금', '금일KSE대용증거금', '금일KSE신용현금증거금', '금일KSE신용대용증거금', '전일코스닥현금증거금', '전일코스닥대용증거금', '전일코스닥신용현금증거금', '전일코스닥신용대용증거금', '금일코스닥현금증거금', '금일코스닥대용증거금', '금일코스닥신용현금증거금', '금일코스닥신용대용증거금', '전일프리보드현금증거금', '전일프리보드대용증거금', '금일프리보드현금증거금', '금일프리보드대용증거금', '전일장외현금증거금', '전일장외대용증거금', '금일장외현금증거금', '금일장외대용증거금', '예탁담보수량', '매수정산금(D+2)', '매도정산금(D+2)', '변제소요금(D+1)', '변제소요금(D+2)', '대출금액']
CSPAQ12300_OUT_BLOCK_3_CODE = ['IsuNo', 'IsuNm', 'SecBalPtnCode', 'SecBalPtnNm', 'BalQty', 'BnsBaseBalQty', 'CrdayBuyExecQty', 'CrdaySellExecQty', 'SellPrc', 'BuyPrc', 'SellPnlAmt', 'PnlRat', 'NowPrc', 'CrdtAmt', 'DueDt', 'PrdaySellExecPrc', 'PrdaySellQty', 'PrdayBuyExecPrc', 'PrdayBuyQty', 'LoanDt', 'AvrUprc', 'SellAbleQty', 'SellOrdQty', 'CrdayBuyExecAmt', 'CrdaySellExecAmt', 'PrdayBuyExecAmt', 'PrdaySellExecAmt', 'BalEvalAmt', 'EvalPnl', 'MnyOrdAbleAmt', 'OrdAbleAmt', 'SellUnercQty', 'SellUnsttQty', 'BuyUnercQty', 'BuyUnsttQty', 'UnsttQty', 'UnercQty', 'PrdayCprc', 'PchsAmt', 'RegMktCode', 'LoanDtlClssCode', 'DpspdgLoanQty']
CSPAQ12300_OUT_BLOCK_3_NAME = ['종목번호', '종목명', '유가증권잔고유형코드', '유가증권잔고유형명', '잔고수량', '매매기준잔고수량', '금일매수체결수량', '금일매도체결수량', '매도가', '매수가', '매도손익금액', '손익율', '현재가', '신용금액', '만기일', '전일매도체결가', '전일매도수량', '전일매수체결가', '전일매수수량', '대출일', '평균단가', '매도가능수량', '매도주문수량', '금일매수체결금액', '금일매도체결금액', '전일매수체결금액', '전일매도체결금액', '잔고평가금액', '평가손익', '현금주문가능금액', '주문가능금액', '매도미체결수량', '매도미결제수량', '매수미체결수량', '매수미결제수량', '미결제수량', '미체결수량', '전일종가', '매입금액', '등록시장코드', '대출상세분류코드', '예탁담보대출수량']

# 현물계좌 예수금/주문가능금액/총평가 조회 2: CSPAQ22200
CSPAQ22200_IN_BLOCK_CODE = ['RecCnt', 'MgmtBrnNo', 'AcntNo', 'Pwd', 'BalCreTp']
CSPAQ22200_IN_BLOCK_NAME = ['레코드갯수', '관리지점번호', '계좌번호', '비밀번호', '잔고생성구분']
CSPAQ22200_OUT_BLOCK_1_CODE = ['RecCnt', 'MgmtBrnNo', 'AcntNo', 'Pwd', 'BalCreTp']
CSPAQ22200_OUT_BLOCK_1_NAME = ['레코드갯수', '관리지점번호', '계좌번호', '비밀번호', '잔고생성구분']
CSPAQ22200_OUT_BLOCK_2_CODE = ['RecCnt', 'BrnNm', 'AcntNm', 'MnyOrdAbleAmt', 'SubstOrdAbleAmt', 'SeOrdAbleAmt', 'KdqOrdAbleAmt', 'CrdtPldgOrdAmt', 'MgnRat100pctOrdAbleAmt', 'MgnRat35ordAbleAmt', 'MgnRat50ordAbleAmt', 'CrdtOrdAbleAmt', 'Dps', 'SubstAmt', 'MgnMny', 'MgnSubst', 'D1Dps', 'D2Dps', 'RcvblAmt', 'D1ovdRepayRqrdAmt', 'D2ovdRepayRqrdAmt', 'MloanAmt', 'ChgAfPldgRat', 'RqrdPldgAmt', 'PdlckAmt', 'OrgPldgSumAmt', 'SubPldgSumAmt', 'CrdtPldgAmtMny', 'CrdtPldgSubstAmt', 'Imreq', 'CrdtPldgRuseAmt', 'DpslRestrcAmt', 'PrdaySellAdjstAmt', 'PrdayBuyAdjstAmt', 'CrdaySellAdjstAmt', 'CrdayBuyAdjstAmt', 'CslLoanAmtdt1']
CSPAQ22200_OUT_BLOCK_2_NAME = ['레코드갯수', '지점명', '계좌명', '현금주문가능금액', '대용주문가능금액', '거래소금액', '코스닥금액', '신용담보주문금액', '증거금률100퍼센트주문가능금액', '증거금률35%주문가능금액', '증거금률50%주문가능금액', '신용주문가능금액', '예수금', '대용금액', '증거금현금', '증거금대용', 'D1예수금', 'D2예수금', '미수금액', 'D1연체변제소요금액', 'D2연체변제소요금액', '융자금액', '변경후담보비율', '소요담보금액', '담보부족금액', '원담보합계금액', '부담보합계금액', '신용담보금현금', '신용담보대용금액', '신용설정보증금', '신용담보재사용금액', '처분제한금액', '전일매도정산금액', '전일매수정산금액', '금일매도정산금액', '금일매수정산금액', '매도대금담보대출금액']

# 현물정상주문: CSPAT00600
CSPAT00600_IN_BLOCK_1_CODE = ['AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdPrc', 'BnsTpCode', 'OrdprcPtnCode', 'MgntrnCode', 'LoanDt', 'OrdCndiTpCode', 'MbrNo']
CSPAT00600_IN_BLOCK_1_NAME = ['계좌번호', '입력비밀번호', '종목번호', '주문수량', '주문가', '매매구분', '호가유형코드', '신용거래코드', '대출일', '주문조건구분', '회원사번호']
CSPAT00600_OUT_BLOCK_1_CODE = ['RecCnt', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdPrc', 'BnsTpCode', 'OrdprcPtnCode', 'PrgmOrdprcPtnCode', 'StslAbleYn', 'StslOrdprcTpCode', 'CommdaCode', 'MgntrnCode', 'LoanDt', 'MbrNo', 'OrdCndiTpCode', 'StrtgCode', 'GrpId', 'OrdSeqNo', 'PtflNo', 'BskNo', 'TrchNo', 'ItemNo', 'OpDrtnNo', 'LpYn', 'CvrgTpCode']
CSPAT00600_OUT_BLOCK_1_NAME = ['레코드갯수', '계좌번호', '입력비밀번호', '종목번호', '주문수량', '주문가', '매매구분', '호가유형코드', '프로그램호가유형코드', '공매도가능여부', '공매도호가구분', '통신매체코드', '신용거래코드', '대출일', '회원번호', '주문조건구분', '전략코드', '그룹ID', '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호', '운용지시번호', '유동성공급자여부', '반대매매구분']
CSPAT00600_OUT_BLOCK_2_CODE = ['RecCnt', 'OrdNo', 'OrdTime', 'OrdMktCode', 'OrdPtnCode', 'ShtnIsuNo', 'MgempNo', 'OrdAmt', 'SpareOrdNo', 'CvrgSeqno', 'RsvOrdNo', 'SpotOrdQty', 'RuseOrdQty', 'MnyOrdAmt', 'SubstOrdAmt', 'RuseOrdAmt', 'AcntNm', 'IsuNm']
CSPAT00600_OUT_BLOCK_2_NAME = ['레코드갯수', '주문번호', '주문시각', '주문시장코드', '주문유형코드', '단축종목번호', '관리사원번호', '주문금액', '예비주문번호', '반대매매일련번호', '예약주문번호', '실물주문수량', '재사용주문수량', '현금주문금액', '대용주문금액', '재사용주문금액', '계좌명', '종목명']

# 현물취소주문: CSPAT00800
CSPAT00800_IN_BLOCK_1_CODE = ['OrgOrdNo', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty']
CSPAT00800_IN_BLOCK_1_NAME = ['원주문번호', '계좌번호', '입력비밀번호', '종목번호', '주문수량']
CSPAT00800_OUT_BLOCK_1_CODE = ['RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'CommdaCode', 'GrpId', 'StrtgCode', 'OrdSeqNo', 'PtflNo', 'BskNo', 'TrchNo', 'ItemNo']
CSPAT00800_OUT_BLOCK_1_NAME = ['레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '종목번호', '주문수량', '통신매체코드', '그룹ID', '전략코드', '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호']
CSPAT00800_OUT_BLOCK_2_CODE = ['RecCnt', 'OrdNo', 'PrntOrdNo', 'OrdTime', 'OrdMktCode', 'OrdPtnCode', 'ShtnIsuNo', 'PrgmOrdprcPtnCode', 'StslOrdprcTpCode', 'StslAbleYn', 'MgntrnCode', 'LoanDt', 'CvrgOrdTp', 'LpYn', 'MgempNo', 'BnsTpCode', 'SpareOrdNo', 'CvrgSeqno', 'RsvOrdNo', 'AcntNm', 'IsuNm']
CSPAT00800_OUT_BLOCK_2_NAME = ['레코드갯수', '주문번호', '모주문번호', '주문시각', '주문시장코드', '주문유형코드', '단축종목번호', '프로그램호가유형코드', '공매도호가구분', '공매도가능여부', '신용거래코드', '대출일', '반대매매주문구분', '유동성공급자여부', '관리사원번호', '매매구분', '예비주문번호', '반대매매일련번호', '예약주문번호', '계좌명', '종목명']

# 현물정정주문 : CSPAT00700
CSPAT00700_IN_BLOCK_1_CODE = ['OrgOrdNo', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdprcPtnCode', 'OrdCndiTpCode', 'OrdPrc']
CSPAT00700_IN_BLOCK_1_NAME = ['원주문번호', '계좌번호', '입력비밀번호', '종목번호', '주문수량', '호가유형코드', '주문조건구분', '주문가']
CSPAT00700_OUT_BLOCK_1_CODE = ['RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdprcPtnCode', 'OrdCndiTpCode', 'OrdPrc', 'CommdaCode', 'StrtgCode', 'GrpId', 'OrdSeqNo', 'PtflNo', 'BskNo', 'TrchNo', 'ItemNo']
CSPAT00700_OUT_BLOCK_1_NAME = ['레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '종목번호', '주문수량', '호가유형코드', '주문조건구분', '주문가', '통신매체코드', '전략코드', '그룹ID', '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호']
CSPAT00700_OUT_BLOCK_2_CODE = ['RecCnt', 'OrdNo', 'PrntOrdNo', 'OrdTime', 'OrdMktCode', 'OrdPtnCode', 'ShtnIsuNo', 'PrgmOrdprcPtnCode', 'StslOrdprcTpCode', 'StslAbleYn', 'MgntrnCode', 'LoanDt', 'CvrgOrdTp', 'LpYn', 'MgempNo', 'OrdAmt', 'BnsTpCode', 'SpareOrdNo', 'CvrgSeqno', 'RsvOrdNo', 'MnyOrdAmt', 'SubstOrdAmt', 'RuseOrdAmt', 'AcntNm', 'IsuNm']
CSPAT00700_OUT_BLOCK_2_NAME = ['레코드갯수', '주문번호', '모주문번호', '주문시각', '주문시장코드', '주문유형코드', '단축종목번호', '프로그램호가유형코드', '공매도호가구분', '공매도가능여부', '신용거래코드', '대출일', '반대매매주문구분', '유동성공급자여부', '관리사원번호', '주문금액', '매매구분', '예비주문번호', '반대매매일련번호', '예약주문번호', '현금주문금액', '대용주문금액', '재사용주문금액', '계좌명', '종목명']

# 주식잔고2 : t0424
T0424_IN_BLOCK_CODE = ['accno', 'passwd', 'prcgb', 'chegb', 'dangb', 'charge', 'cts_expcode']
T0424_IN_BLOCK_NAME = ['계좌번호', '비밀번호', '단가구분', '체결구분', '단가구분', '제비용구분', 'CTS_종목번호']
T0424_OUT_BLOCK_CODE = ['sunikrt', 'tsunik', 'tappamt', 'tvalamt', 'tjanqty']
T0424_OUT_BLOCK_NAME = ['총수익률', '총평가손익', '총매입금액', '총평가금액', '총잔고수량']
T0424_OUT_BLOCK_1_CODE = ['expcode', 'jangb', 'janqty', 'mdposqt', 'pamt', 'mamt', 'sinamt', 'sunikrt', 'daysunik', 'dtsunik', 'sunik', 'evalamt', 'parprice', 'stat', 'medosu', 'jocd', 'hname']
T0424_OUT_BLOCK_1_NAME = ['종목번호', '잔고구분', '잔고수량', '매도가능수량', '평균단가', '매입금액', '대출금액', '수익률', '당일매도손익', '당일매매손익', '평가손익', '평가금액', '현재가', '종목상태', '매입매도구분', '종목구분', '종목명']

# 현물계좌 주문체결내역 조회 : t0425
T0425_IN_BLOCK_CODE = ['accno', 'passwd', 'expcode', 'chegb', 'medosu', 'sortgb', 'cts_ordno']
T0425_IN_BLOCK_NAME = ['계좌번호', '비밀번호', '종목번호', '체결구분', '매매구분', '정렬순서', '주문번호']
T0425_OUT_BLOCK_CODE = ['tqty', 'tcheqty', 'tordrem', 'cmss', 'tamt', 'tmdamt', 'tmsamt', 'tax', 'cts_ordno']
T0425_OUT_BLOCK_NAME = ['총주문수량', '총체결수량', '총미체결수량', '추정수수료', '총주문금액', '총매도체결금액', '총매수체결금액', '추정제세금', '주문번호']
T0425_OUT_BLOCK_1_CODE = ['ordno', 'expcode', 'medosu', 'qty', 'price', 'cheqty', 'cheprice', 'ordrem', 'cfmqty', 'status', 'orgordno', 'ordgb', 'ordtime', 'ordermtd', 'sysprocseq', 'hogagb', 'price1', 'orggb', 'singb', 'loandt']
T0425_OUT_BLOCK_1_NAME = ['주문번호', '종목번호', '구분', '주문수량', '주문가격', '체결수량', '체결가격', '미체결잔량', '확인수량', '상태', '원주문번호', '유형', '주문시간', '주문매체', '처리순번', '호가유형', '현재가', '주문구분', '신용구분', '대출일자']

# 현물계좌 주문체결내역 조회 : CSPAQ13700
CSPAQ13700_IN_BLOCK_CODE = ['RecCnt', 'AcntNo', 'InptPwd', 'OrdMktCode', 'BnsTpCode', 'IsuNo', 'ExecYn', 'OrdDt', 'SrtOrdNo2', 'BkseqTpCode', 'OrdPtnCode']
CSPAQ13700_IN_BLOCK_NAME = ['레코드갯수', '계좌번호', '입력비밀번호', '주문시장코드', '매매구분', '종목번호', '체결여부', '주문일', '시작주문번호2', '역순구분', '주문유형코드']
CSPAQ13700_OUT_BLOCK_1_CODE = ['RecCnt', 'AcntNo', 'InptPwd', 'OrdMktCode', 'BnsTpCode', 'IsuNo', 'ExecYn', 'OrdDt', 'SrtOrdNo2', 'BkseqTpCode', 'OrdPtnCode']
CSPAQ13700_OUT_BLOCK_1_NAME = ['레코드갯수', '계좌번호', '입력비밀번호', '주문시장코드', '매매구분', '종목번호', '체결여부', '주문일', '시작주문번호2', '역순구분', '주문유형코드']
CSPAQ13700_OUT_BLOCK_2_CODE = ['RecCnt', 'SellExecAmt', 'BuyExecAmt', 'SellExecQty', 'BuyExecQty', 'SellOrdQty', 'BuyOrdQty']
CSPAQ13700_OUT_BLOCK_2_NAME = ['레코드갯수', '매도체결금액', '매수체결금액', '매도체결수량', '매수체결수량', '매도주문수량', '매수주문수량']
CSPAQ13700_OUT_BLOCK_3_CODE = ['OrdDt', 'MgmtBrnNo', 'OrdMktCode', 'OrdNo', 'OrgOrdNo', 'IsuNo', 'IsuNm', 'BnsTpCode', 'BnsTpNm', 'OrdPtnCode', 'OrdPtnNm', 'OrdTrxPtnCode', 'OrdTrxPtnNm', 'MrcTpCode', 'MrcTpNm', 'MrcQty', 'MrcAbleQty', 'OrdQty', 'OrdPrc', 'ExecQty', 'ExecPrc', 'ExecTrxTime', 'LastExecTime', 'OrdprcPtnCode', 'OrdprcPtnNm', 'OrdCndiTpCode', 'AllExecQty', 'RegCommdaCode', 'CommdaNm', 'MbrNo', 'RsvOrdYn', 'LoanDt', 'OrdTime', 'OpDrtnNo', 'OdrrId']
CSPAQ13700_OUT_BLOCK_3_NAME = ['주문일', '관리지점번호', '주문시장코드', '주문번호', '원주문번호', '종목번호', '종목명', '매매구분', '매매구분', '주문유형코드', '주문유형명', '주문처리유형코드', '주문처리유형명', '정정취소구분', '정정취소구분명', '정정취소수량', '정정취소가능수량', '주문수량', '주문가격', '체결수량', '체결가', '체결처리시각', '최종체결시각', '호가유형코드', '호가유형명', '주문조건구분', '전체체결수량', '통신매체코드', '통신매체명', '회원번호', '예약주문여부', '대출일', '주문시각', '운용지시번호', '주문자ID']

# 주식차트(일주월년) : t8410
T8410_IN_BLOCK_CODE = ['shcode', 'gubun', 'qrycnt', 'sdate', 'edate', 'cts_date', 'comp_yn', 'sujung']
T8410_IN_BLOCK_NAME = ['단축코드', '주기구분(2:일3:주4:월5:년)', '요청건수(최대-압축:2000비압축:500)', '시작일자', '종료일자', '연속일자', '압축여부(Y:압축N:비압축)', '수정주가여부(Y:적용N:비적용)']
T8410_OUT_BLOCK_CODE = ['shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose', 'highend', 'lowend', 'cts_date', 's_time', 'e_time', 'dshmin', 'rec_count', 'svi_uplmtprice', 'svi_dnlmtprice']
T8410_OUT_BLOCK_NAME = ['단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가', '상한가', '하한가', '연속일자', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트', '정적VI상한가', '정적VI하한가']
T8410_OUT_BLOCK_1_CODE = ['date', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value', 'jongchk', 'rate', 'pricechk', 'ratevalue', 'sign']
T8410_OUT_BLOCK_1_NAME = ['날짜', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율', '수정주가반영항목', '수정비율반영거래대금', '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)']

# 주식차트(틱/n틱) : t8411
T8411_IN_BLOCK_CODE = ['shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time', 'comp_yn']
T8411_IN_BLOCK_NAME = ['단축코드', '단위(n틱)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간', '압축여부(Y:압축N:비압축)']
T8411_OUT_BLOCK_CODE = ['shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose', 'highend', 'lowend', 'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count']
T8411_OUT_BLOCK_NAME = ['단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가', '상한가', '하한가', '연속일자', '연속시간', '장시작시간(HHMMSS)', '장 종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트']
T8411_OUT_BLOCK_1_CODE = ['date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'jongchk', 'rate', 'pricechk']
T8411_OUT_BLOCK_1_NAME = ['날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '수정구분', '수정비율', '수정주가반영항목']

# 주식차트(N분분) : t8412
T8412_IN_BLOCK_CODE = ['shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time', 'comp_yn']
T8412_IN_BLOCK_NAME = ['단축코드', '단위(n분)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간', '압축여부(Y:압축N:비압축)']
T8412_OUT_BLOCK_CODE = ['shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose', 'highend', 'lowend', 'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count']
T8412_OUT_BLOCK_NAME = ['단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가', '상한가', '하한가', '연속일자', '연속시간', '장시작시간(HHMMSS)', '장 종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트']
T8412_OUT_BLOCK_1_CODE = ['date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value', 'jongchk', 'rate', 'sign']
T8412_OUT_BLOCK_1_NAME = ['날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율', '종가등락구분(1:상한2:상승3:보합4:하한5:하락)']

# 주식마스터조회 : t9945
T9945_IN_BLOCK_CODE = ['gubun']
T9945_IN_BLOCK_NAME = ['구분(1:코스피2:코스닥)']
T9945_OUT_BLOCK_CODE = ['hname', 'shcode', 'expcode', 'etfgubun', 'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun']
T9945_OUT_BLOCK_NAME = ['종목명', '단축코드', '확장코드', 'ETF구분(1:ETF)', '상한가', '하한가', '전일가', '주문수량단위', '기준가', '구분']

# 주식종목 조회 : t8430
T8430_IN_BLOCK_CODE = ['gubun']
T8430_IN_BLOCK_NAME = ['구분(0:전체1:코스피2:코스닥)']
T8430_OUT_BLOCK_CODE = ['hname', 'shcode', 'expcode', 'etfgubun', 'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun']
T8430_OUT_BLOCK_NAME = ['종목명', '단축코드', '확장코드', 'ETF구분(1:ETF)', '상한가', '하한가', '전일가', '주문수량단위', '기준가', '구분(1:코스피2:코스닥)']

# 주식종목 조회 : t8451
T8451_IN_BLOCK_CODE = ['shcode', 'gubun', 'qrycnt', 'sdate', 'edate', 'cts_date', 'comp_yn', 'sujung', 'exchgubun']
T8451_IN_BLOCK_NAME = ['단축코드', '주기구분(2:일3:주4:월5:년)', '요청건수(최대-압축:2000비압축:500)', '시작일자', '종료일자', '연속일자', '압축여부(Y:압축N:비압축)', '수정주가여부(Y:적용N:비적용)', '거래소 구분코드']
T8451_OUT_BLOCK_CODE = ['shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose', 'highend', 'lowend', 'cts_date', 's_time', 'e_time', 'dshmin', 'rec_count', 'svi_uplmtprice', 'svi_dnlmtprice', 'nxt_fm_s_time', 'nxt_fm_e_time', 'nxt_fm_dshmin', 'nxt_am_s_time', 'nxt_am_e_time', 'nxt_am_dshmin']
T8451_OUT_BLOCK_NAME = ['단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가', '상한가', '하한가', '연속일자', '장시작시간(HHMMSS)', '장종료 시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트', '정적VI상한가', '정적VI하한가', 'NXT프리마켓장시작시간(HHMMSS)', 'NXT프리마켓장종료시간(HHMMSS)', 'NXT프리마켓동시호가처리시간(MM:분)', 'NXT에프터마켓장시작시간(HHMMSS)', 'NXT에프터마켓장종료시간(HHMMSS)', 'NXT에프터마켓동시호가처리시간(MM:분)']
T8451_OUT_BLOCK_1_CODE = ['date', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value', 'jongchk', 'rate', 'pricechk', 'ratevalue', 'sign']
T8451_OUT_BLOCK_1_NAME = ['날짜', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율', '수정주가반영항목', '수정비율반영거래대금', '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)']

# 시가총액상위 : t1444
T1444_IN_BLOCK_CODE = ['upcode', 'idx']
T1444_IN_BLOCK_NAME = ['업종코드', 'IDX']
T1444_OUT_BLOCK_CODE = ['idx']
T1444_OUT_BLOCK_NAME = ['IDX']
T1444_OUT_BLOCK_1_CODE = ['shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'vol_rate', 'total', 'rate', 'for_rate']
T1444_OUT_BLOCK_1_NAME = ['종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '거래비중', '시가총액', '비중', '외인비중']


# 업종전체조회 : t8424
T8424_IN_BLOCK_CODE = ['gubun1']
T8424_IN_BLOCK_NAME = ['구분1']
T8424_OUT_BLOCK_CODE = ['hname', 'upcode']
T8424_OUT_BLOCK_NAME = ['업종명', '업종코드']

# 주식멀티현재가조회 : t8407
T8407_IN_BLOCK_CODE = ['nrec', 'shcode']
T8407_IN_BLOCK_NAME = ['건수', '종목코드']
T8407_OUT_BLOCK_1_CODE = ['shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'offerho', 'bidho', 'cvolume', 'chdegree', 'open', 'high', 'low', 'value', 'offerrem', 'bidrem', 'totofferrem', 'totbidrem', 'jnilclose', 'uplmtprice', 'dnlmtprice']
T8407_OUT_BLOCK_1_NAME = ['종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '매도호가', '매수호가', '체결수량', '체결강도', '시가', '고가', '저가', '거래대금(백만)', '우선매도잔량', '우선매수잔량', '총매도잔량', '총매수잔량', '전일종가', '상한가', '하한가']

# 등락율 상위 : t1441
T1441_IN_BLOCK_CODE = ['gubun1', 'gubun2', 'gubun3', 'jc_num', 'sprice', 'eprice', 'volume', 'idx', 'jc_num2']
T1441_IN_BLOCK_NAME = ['구분', '상승하락', '당일전일', '대상제외', '시작가격', '종료가격', '거래량', 'IDX', '대상제외2']
T1441_OUT_BLOCK_CODE = ['idx']
T1441_OUT_BLOCK_NAME = ['IDX']
T1441_OUT_BLOCK_1_CODE = ['hname', 'price', 'sign', 'change', 'diff', 'volume', 'offerrem1', 'offerho1', 'bidho1', 'bidrem1', 'updaycnt', 'jnildiff', 'shcode', 'open', 'high', 'low', 'voldiff', 'value', 'total']
T1441_OUT_BLOCK_1_NAME = ['한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '매도잔량', '매도호가', '매수호가', '매수잔량', '연속', '전일등락율', '종목코드', '시가', '고가', '저가', '거래량대비율', '거래대금', '시가총액']

# 종목별프로그램매매추이 : t1637
T1637_IN_BLOCK_CODE = ['gubun1', 'gubun2', 'shcode', 'date', 'time', 'cts_idx', 'exchgubun']
T1637_IN_BLOCK_NAME = ['수량금액구분', '시간일별구분', '종목코드', '일자', '시간', 'IDXCTS', '거래소구분코드']
T1637_OUT_BLOCK_CODE = ['cts_idx']
T1637_OUT_BLOCK_NAME = ['IDXCTS']
T1637_OUT_BLOCK_1_CODE = ['date', 'time', 'price', 'sign', 'change', 'diff', 'volume', 'svalue', 'offervalue', 'stksvalue', 'svolume', 'offervolume', 'stksvolume', 'shcode', 'ex_shcode']
T1637_OUT_BLOCK_1_NAME = ['일자', '시간', '현재가', '대비구분', '대비', '등락율', '거래량', '순매수금액', '매도금액', '매수금액', '순매수수량', '매도수량', '매수수량', '종목코드', '거래소별단축코드']

# 외인/기관 종목별동향 : t1716
T1716_IN_BLOCK_CODE = ['shcode', 'gubun', 'fromdt', 'todt', 'prapp', 'prgubun', 'orggubun', 'frggubun', 'exchgubun']
T1716_IN_BLOCK_NAME = ['종목코드', '구분', '시작일자', '종료일자', 'PR감산적용율', 'PR적용구분', '기관적용', '외인적용', '거래소구분코드']
T1716_OUT_BLOCK_CODE = ['date', 'close', 'sign', 'change', 'diff', 'volume', 'krx_0008', 'krx_0018', 'krx_0009', 'pgmvol', 'fsc_listing', 'fsc_sjrate', 'fsc_0009', 'gm_volume', 'gm_value']
T1716_OUT_BLOCK_NAME = ['일자', '종가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래소_개인', '거래소_기관', '거래소_외국인', '프로그램', '금감원_외인보유주식수', '금감원_소진율', '금감원_외국인', '공매도수량', '공매도대금']

# 거래원리스트 : t1764
T1764_IN_BLOCK_CODE = ['shcode', 'gubun1']
T1764_IN_BLOCK_NAME = ['종목코드', '구분1']
T1764_OUT_BLOCK_CODE = ['rank', 'tradno', 'tradname']
T1764_OUT_BLOCK_NAME = ['순위', '거래원번호', '거래원명']

# 주식 현재가 조회 : t1102
T1102_IN_BLOCK_CODE = ['shcode']
T1102_IN_BLOCK_NAME = ['종목코드']
T1102_OUT_BLOCK_CODE = ['hname', 'price', 'sign', 'change', 'diff', 'volume', 'total', 'abscnt', 'listing', 'listdate', 'jnilclose', 'open', 'high', 'low']
T1102_OUT_BLOCK_NAME = ['한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '시가총액', '유동주식수', '상장주식수', '상장일', '전일종가', '시가', '고가', '저가']

# 거래원별누적 : t1771
T1771_IN_BLOCK_CODE = ['shcode', 'tradno', 'gubun1', 'traddate1', 'traddate2', 'cts_idx', 'cnt', 'exchgubun']
T1771_IN_BLOCK_NAME = ['종목코드', '거래원코드', '구분1', '거래일자1', '거래일자2', 'CTSIDX', '요청건수', '거래소구분']
T1771_OUT_BLOCK_CODE = ['cts_idx']
T1771_OUT_BLOCK_NAME = ['CTSIDX']
T1771_OUT_BLOCK2_CODE = ['traddate', 'price', 'tradmdcha', 'tradmsscha', 'tradavg', 'tradmttavg']
T1771_OUT_BLOCK2_NAME = ['거래일자', '종가', '순매수', '누적순매수', '평균단가', '누적평균단가']




# 통합 체결 실시간 데이터 : UH1, US2, US3
UH1_IN_BLOCK_CODE = ['ex_shcode']
UH1_IN_BLOCK_NAME = ['거래소별단축코드']
UH1_OUT_BLOCK_CODE = ['hotime', 'offerho1', 'bidho1', 'krx_offerrem1', 'nxt_offerrem1', 'unt_offerrem1', 'krx_bidrem1', 'nxt_bidrem1', 'unt_bidrem1', 'offerho2', 'bidho2', 'krx_offerrem2', 'nxt_offerrem2', 'unt_offerrem2', 'krx_bidrem2', 'nxt_bidrem2', 'unt_bidrem2', 'offerho3', 'bidho3', 'krx_offerrem3', 'nxt_offerrem3', 'unt_offerrem3', 'krx_bidrem3', 'nxt_bidrem3', 'unt_bidrem3', 'offerho4', 'bidho4', 'krx_offerrem4', 'nxt_offerrem4', 'unt_offerrem4', 'krx_bidrem4', 'nxt_bidrem4', 'unt_bidrem4', 'offerho5', 'bidho5', 'krx_offerrem5', 'nxt_offerrem5', 'unt_offerrem5', 'krx_bidrem5', 'nxt_bidrem5', 'unt_bidrem5', 'offerho6', 'bidho6', 'krx_offerrem6', 'nxt_offerrem6', 'unt_offerrem6', 'krx_bidrem6', 'nxt_bidrem6', 'unt_bidrem6', 'offerho7', 'bidho7', 'krx_offerrem7', 'nxt_offerrem7', 'unt_offerrem7', 'krx_bidrem7', 'nxt_bidrem7', 'unt_bidrem7', 'offerho8', 'bidho8', 'krx_offerrem8', 'nxt_offerrem8', 'unt_offerrem8', 'krx_bidrem8', 'nxt_bidrem8', 'unt_bidrem8', 'offerho9', 'bidho9', 'krx_offerrem9', 'nxt_offerrem9', 'unt_offerrem9', 'krx_bidrem9', 'nxt_bidrem9', 'unt_bidrem9', 'offerho10', 'bidho10', 'krx_offerrem10', 'nxt_offerrem10', 'unt_offerrem10', 'krx_bidrem10', 'nxt_bidrem10', 'unt_bidrem10', 'krx_totofferrem', 'nxt_totofferrem', 'unt_totofferrem', 'krx_totbidrem', 'nxt_totbidrem', 'unt_totbidrem', 'krx_donsigubun', 'nxt_donsigubun', 'shcode', 'alloc_gubun', 'volume', 'krx_midprice', 'krx_offermidsumrem', 'krx_bidmidsumrem', 'nxt_midprice', 'nxt_offermidsumrem', 'nxt_bidmidsumrem', 'krx_midsumrem', 'krx_midsumremgubun', 'nxt_midsumrem', 'nxt_midsumremgubun', 'ex_shcode']
UH1_OUT_BLOCK_NAME = ['호가시간', '매도호가1', '매수호가1', 'KRX매도호가잔량1', 'NXT매도호가잔량1', '통합매도호가잔량1', 'KRX매수호가잔량1', 'NXT매수호가잔량1', '통합매수호가잔량1', '매도호가2', '매수호가2', 'KRX매도호가잔량2', 'NXT매도호가잔량2', '통합 매도호가잔량2', 'KRX매수호가잔량2', 'NXT매수호가잔량2', '통합매수호가잔량2', '매도호가3', '매수호가3', 'KRX매도호가잔량3', 'NXT매도호가잔량3', '통합매도호가잔량3', 'KRX매수호가잔량3', 'NXT매수호가잔량3', '통합매수호가잔량3', '매도호가4', '매수호가4', 'KRX매도호가잔량4', 'NXT매도호가잔량4', '통합매도호가잔량4', 'KRX매수호가잔량4', 'NXT매수호가잔량4', '통합매수호가잔량4', '매도호가5', '매수호가5', 'KRX매도호가잔량5', 'NXT매도호가잔량5', '통합매도호가잔량5', 'KRX 매수호가잔량5', 'NXT매수호가잔량5', '통합매수호가잔량5', '매도호가6', '매수호가6', 'KRX매도호가잔량6', 'NXT매도호가잔량6', '통합매도호가잔량6', 'KRX매수호가잔량6', 'NXT매수호가잔량6', '통합매수호가잔량6', '매도호가7', '매수호가7', 'KRX매도호가잔량7', 'NXT매도호가잔량7', '통합매도호가잔량7', 'KRX매수호가잔량7', 'NXT매수호가잔량7', '통합매수호가잔량7', '매도호가8', '매수호가8', 'KRX매도호가잔량8', 'NXT매도호가잔량8', '통합매도호가잔량8', 'KRX매수호가잔량8', 'NXT매수호가잔량8', '통합매수호가잔량8', '매도호가9', '매수호가9', 'KRX매도호가잔량9', 'NXT매도호가잔량9', '통합매도호가잔량9', 'KRX매수호가잔량9', 'NXT매수호가잔량9', '통합매수호가잔량9', '매도호가10', '매수호가10', 'KRX매도호가잔량10', 'NXT매도호가잔량10', '통합매도호가잔량10', 'KRX매수호가잔량10', 'NXT매수호가잔량10', '통합매수호가잔량10', 'KRX총매도호가잔량', 'NXT총매도호가잔량', '통합총매도호가잔량', 'KRX총매수호가잔량', 'NXT총매수호가잔량', '통합총매수호가잔량', 'KRX동시호가구분', 'NXT동시호가구분', '단축코드', '배분적용구분', '누적거래량', 'KRX중간가격', 'KRX매도중간가잔량합계수량', 'KRX매수중간가잔량합계수량', 'NXT중간가격', 'NXT매도중간가잔량합계수량', 'NXT매수중간가잔량합계수량', 'KRX중간가잔량합계수량', "KRX중간가잔량구분(''없음'1'매도'2'매수)", 'NXT중간가잔량합계수량', "NXT중간가잔량구분(''없음'1'매도'2'매수)", '거래소별단축코드']

US2_IN_BLOCK_CODE = ['ex_shcode']
US2_IN_BLOCK_NAME = ['거래소별단축코드']
US2_OUT_BLOCK_CODE = ['offerho', 'bidho', 'shcode', 'ex_shcode']
US2_OUT_BLOCK_NAME = ['매도호가', '매수호가', '단축코드', '거래소별단축코드']

US3_IN_BLOCK_CODE = ['ex_shcode']
US3_IN_BLOCK_NAME = ['거래소별단축코드']
US3_OUT_BLOCK_CODE = ['chetime', 'sign', 'change', 'drate', 'price', 'opentime', 'open', 'hightime', 'high', 'lowtime', 'low', 'cgubun', 'cvolume', 'volume', 'value', 'mdvolume', 'mdchecnt', 'msvolume', 'mschecnt', 'cpower', 'w_avrg', 'offerho', 'bidho', 'status', 'jnilvolume', 'shcode', 'exchname', 'ex_shcode']
US3_OUT_BLOCK_NAME = ['체결시간', '전일대비구분', '전일대비', '등락율', '현재가', '시가시간', '시가', '고가시간', '고가', '저가시간', '저가', '체결구분', '체결량', '누적거래량', '누적거래대금', '매도누적체결량', '매도누적체결건수', '매수누적체결량', '매 수누적체결건수', '체결강도', '가중평균가', '매도호가', '매수호가', '장정보', '전일동시간대거래량', '단축코드', '거래소명', '거래소별단축코드']

# KOSPI 체결 실시간 데이터 : S3_
S3__IN_BLOCK_CODE = ['shcode']
S3__IN_BLOCK_NAME = ['단축코드']
S3__OUT_BLOCK_CODE = ['chetime', 'sign', 'change', 'drate', 'price', 'opentime', 'open', 'hightime', 'high', 'lowtime', 'low', 'cgubun', 'cvolume', 'volume', 'value', 'mdvolume', 'mdchecnt', 'msvolume', 'mschecnt', 'cpower', 'w_avrg', 'offerho', 'bidho', 'status', 'jnilvolume', 'shcode']
S3__OUT_BLOCK_NAME = ['체결시간', '전일대비구분', '전일대비', '등락율', '현재가', '시가시간', '시가', '고가시간', '고가', '저가시간', '저가', '체결구분', '체결량', '누적거래량', '누적거래대금', '매도누적체결량', '매도누적체결건수', '매수누적체결량', '매수누적체결건수', '체결강도', '가중평균가', '매도호가', '매수호가', '장정보', '전일동시간대거래량', '단축코드']

# KOSPI 호가잔량 : H1_
H1__IN_BLOCK_CODE = ['shcode']
H1__IN_BLOCK_NAME = ['단축코드']
H1__OUT_BLOCK_CODE = ['hotime', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'offerho3', 'bidho3', 'offerrem3', 'bidrem3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'offerho5', 'bidho5', 'offerrem5', 'bidrem5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'offerho8', 'bidho8', 'offerrem8', 'bidrem8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'offerho10', 'bidho10', 'offerrem10', 'bidrem10', 'totofferrem', 'totbidrem', 'donsigubun', 'shcode', 'alloc_gubun', 'volume']
H1__OUT_BLOCK_NAME = ['호가시간', '매도호가1', '매수호가1', '매도호가잔량1', '매수호가잔량1', '매도호가2', '매수호가2', '매도호가잔량2', '매수호가잔량2', '매도호가3', '매수호가3', '매도호가잔량3', '매수호가잔량3', '매도호가4', '매수호가4', '매도호가잔량4', '매수호가잔량4', '매도호가5', '매 수호가5', '매도호가잔량5', '매수호가잔량5', '매도호가6', '매수호가6', '매도호가잔량6', '매수호가잔량6', '매도호가7', '매수호가7', '매도호가잔량7', '매수호가잔량7', '매도호가8', '매수호가8', '매도호가잔량8', '매수호가잔량8', '매도호가9', '매수호가9', '매도호가잔량9', '매수호가잔량9', '매도호가10', '매수호가10', '매도호가잔량10', '매수호가잔량10', '총매도호가잔량', '총매수호가잔량', '동시호가구분', '단축코드', '배분적용구분', '누적거래량']

# KOSDAQ 호가잔량 : HA_
HA__IN_BLOCK_CODE = ['shcode']
HA__IN_BLOCK_NAME = ['단축코드']
HA__OUT_BLOCK_CODE = ['hotime', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'offerho3', 'bidho3', 'offerrem3', 'bidrem3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'offerho5', 'bidho5', 'offerrem5', 'bidrem5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'offerho8', 'bidho8', 'offerrem8', 'bidrem8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'offerho10', 'bidho10', 'offerrem10', 'bidrem10', 'totofferrem', 'totbidrem', 'donsigubun', 'shcode', 'alloc_gubun', 'volume']
HA__OUT_BLOCK_NAME = ['호가시간', '매도호가1', '매수호가1', '매도호가잔량1', '매수호가잔량1', '매도호가2', '매수호가2', '매도호가잔량2', '매수호가잔량2', '매도호가3', '매수호가3', '매도호가잔량3', '매수호가잔량3', '매도호가4', '매수호가4', '매도호가잔량4', '매수호가잔량4', '매도호가5', '매 수호가5', '매도호가잔량5', '매수호가잔량5', '매도호가6', '매수호가6', '매도호가잔량6', '매수호가잔량6', '매도호가7', '매수호가7', '매도호가잔량7', '매수호가잔량7', '매도호가8', '매수호가8', '매도호가잔량8', '매수호가잔량8', '매도호가9', '매수호가9', '매도호가잔량9', '매수호가잔량9', '매도호가10', '매수호가10', '매도호가잔량10', '매수호가잔량10', '총매도호가잔량', '총매수호가잔량', '동시호가구분', '단축코드', '배분적용구분', '누적거래량']

# 주식주문 접수 : SC0
SC0_IN_BLOCK_CODE = []
SC0_IN_BLOCK_NAME = []
SC0_OUT_BLOCK_CODE = ['lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid', 'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno', 'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey', 'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'ordchegb', 'marketgb', 'ordgb', 'orgordno', 'accno1', 'accno2', 'passwd', 'expcode', 'shtcode', 'hname', 'ordqty', 'ordprice', 'hogagb', 'etfhogagb', 'pgmtype', 'gmhogagb', 'gmhogayn', 'singb', 'loandt', 'cvrgordtp', 'strtgcode', 'groupid', 'ordseqno', 'prtno', 'basketno', 'trchno', 'itemno', 'brwmgmyn', 'mbrno', 'procgb', 'admbrchno', 'futaccno', 'futmarketgb', 'tongsingb', 'lpgb', 'dummy', 'ordno', 'ordtm', 'prntordno', 'mgempno', 'orgordundrqty', 'orgordmdfyqty', 'ordordcancelqty', 'nmcpysndno', 'ordamt', 'bnstp', 'spareordno', 'cvrgseqno', 'rsvordno', 'mtordseqno', 'spareordqty', 'orduserid', 'spotordqty', 'ordruseqty', 'mnyordamt', 'ordsubstamt', 'ruseordamt', 'ordcmsnamt', 'crdtuseamt', 'secbalqty', 'spotordableqty', 'ordableruseqty', 'flctqty', 'secbalqtyd2', 'sellableqty', 'unercsellordqty', 'avrpchsprc', 'pchsamt', 'deposit', 'substamt', 'csgnmnymgn', 'csgnsubstmgn', 'crdtpldgruseamt', 'ordablemny', 'ordablesubstamt', 'ruseableamt']
SC0_OUT_BLOCK_NAME = ['라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호', '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호', '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값', '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결구분', '시장구분', '주문구분', ' 원주문번호', '계좌번호', '계좌번호', '비밀번호', '종목번호', '단축종목번호', '종목명', '주문수량', '주문가격', '주문조건', '호가유형코드', '프로그램호가구분', '공매도호가구분', '공매도가능여부', '신용구분', '대출일', '반대매매주문구분', '전략코드', '그룹ID', '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아아템번호', '차입구분', '회원사번호', '처리구분', '관리지점번호', '선물계좌번호', '선물상품구분', '통신매체구분', '유동성공급자구분', 'DUMMY', '주문번호', '주문시각', '모주문번호', '관리사원번호', '원주문미체결수량', '원 주문정정수량', '원주문취소수량', '비회원사송신번호', '주문금액', '매매구분', '예비주문번호', '반대매매일련번호', '예약주문번호', '복수주문일련번호', '예비주문수량', '주문사원번호', '실물주문수량', '재사용주문수량', '현금주문금액', '주문대용금액', '재사용주문금액', '수수료주문금액', '사용신용담보재사용금', '잔고수량', '실물가능수량', '재사용가능수량(매도)', '변동수량', '잔고수량(D2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액', '예수금', '대용금', '위탁증거금현금', '위탁증거금대용', '신용담보재사용금', '주문가능현금', '주문가능대용', '재사용가능금액']
# 주식주문 체결/정정/취소/거부. : SC1, SC2, SC3
SCN_IN_BLOCK_CODE = []
SCN_IN_BLOCK_NAME = []
SCN_OUT_BLOCK_CODE = ['lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid', 'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno', 'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey', 'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'ordxctptncode', 'ordmktcode', 'ordptncode', 'mgmtbrnno', 'accno1', 'accno2', 'acntnm', 'Isuno', 'Isunm', 'ordno', 'orgordno', 'execno', 'ordqty', 'ordprc', 'execqty', 'execprc', 'mdfycnfqty', 'mdfycnfprc', 'canccnfqty', 'rjtqty', 'ordtrxptncode', 'mtiordseqno', 'ordcndi', 'ordprcptncode', 'nsavtrdqty', 'shtnIsuno', 'opdrtnno', 'cvrgordtp', 'unercqty', 'orgordunercqty', 'orgordmdfyqty', 'orgordcancqty', 'ordavrexecprc', 'ordamt', 'stdIsuno', 'bfstdIsuno', 'bnstp', 'ordtrdptncode', 'mgntrncode', 'adduptp', 'commdacode', 'Loandt', 'mbrnmbrno', 'ordacntno', 'agrgbrnno', 'mgempno', 'futsLnkbrnno', 'futsLnkacntno', 'futsmkttp', 'regmktcode', 'mnymgnrat', 'substmgnrat', 'mnyexecamt', 'ubstexecamt', 'cmsnamtexecamt', 'crdtpldgexecamt', 'crdtexecamt', 'prdayruseexecval', 'crdayruseexecval', 'spotexecqty', 'stslexecqty', 'strtgcode', 'grpId', 'ordseqno', 'ptflno', 'bskno', 'trchno', 'itemno', 'orduserId', 'brwmgmtYn', 'frgrunqno', 'trtzxLevytp', 'lptp', 'exectime', 'rcptexectime', 'rmndLoanamt', 'secbalqty', 'spotordableqty', 'ordableruseqty', 'flctqty', 'secbalqtyd2', 'sellableqty', 'unercsellordqty', 'avrpchsprc', 'pchsant', 'deposit', 'substamt', 'csgnmnymgn', 'csgnsubstmgn', 'crdtpldgruseamt', 'ordablemny', 'ordablesubstamt', 'ruseableamt']
SCN_OUT_BLOCK_NAME = ['라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호', '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호', '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값', '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드', '관리지점번호', '계좌번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '주문수량', '주문가격', '체결수량', '체결가격', '정정확인수량', '정정확인가격', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건', '호가유형코드', '비저축체결수량', '단축종목번호', '운용지시번호', '반대매매주문구분', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가격', '주문금액', '표준종목번호', '전표준종목번호', '매매구분', '주문거래유형코드', '신용거래코드', '수수료합산코드', '통신매체코드', '대출일', '회원/비회원사번호', '주문계좌번호', '집계지점번호', '관리사원번호', '선물연계지점번호', '선물연계계좌번호', '선물시장구분', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액', '대용체결금액', '수수료체결금액', '신용담보체결금액', '신용체결금액', '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹Id', '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호', '주문자Id', '차입관리여부', '외국인고유번호', '거래세징수구분', '유동성공급자구분', '체결시각', '거래소수신체결시각', '잔여대출금액', '잔고수량', '실물가능수량', '재사용가능수량(매도)', '변동수량', '잔고수량(d2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액', '예수금', '대용금', '위탁증거금현금', '위탁증거금대용', '신용담보재사용금', '주문가능현금', '주문가능대용', '재사용가능금액']

# 통합 예상체결
UYS_IN_BLOCK_CODE = ['ex_shcode']
UYS_IN_BLOCK_NAME = ['거래소별단축코드']
UYS_OUT_BLOCK_CODE = ['hotime', 'yeprice', 'yevolume', 'jnilysign', 'jnilchange', 'jnilydrate', 'yofferho0', 'ybidho0', 'yofferrem0', 'ybidrem0', 'shcode', 'exchname', 'ex_shcode']
UYS_OUT_BLOCK_NAME = ['호가시간', '예상체결가격', '예상체결수량', '예상체결가전일종가대비구분', '예상체결가전일종가대비', '예상체결가전일종가등락율', '예상매도호가', '예상매수호가', '예상매도호가수량', '예상매수호가수량', '단축코드', '거래소명', '거래소별단축코드']

# 서버저장조건리스트 조회 : t1866
T1866_IN_BLOCK_CODE = ['user_id', 'gb', 'group_name', 'cont', 'cont_key']
T1866_IN_BLOCK_NAME = ['로그인ID', '조회구분', '그룹명', '연속여부', '연속키']
T1866_OUT_BLOCK_CODE = ['result_count', 'cont', 'cont_key']
T1866_OUT_BLOCK_NAME = ['저장조건수', '연속여부', '연속키']
T1866_OUT_BLOCK_1_CODE = ['query_index', 'group_name', 'query_name']
T1866_OUT_BLOCK_1_NAME = ['서버저장인덱스', '그룹명', '조건저장명']

# e종목검색 : t1857
T1857_IN_BLOCK_CODE = ['sRealFlag', 'sSearchFlag', 'query_index']
T1857_IN_BLOCK_NAME = ['실시간구분(0:조회1:실시간)', '종목검색구분(F:파일S:서버)', '종목검색입력값']
T1857_OUT_BLOCK_CODE = ['result_count', 'result_time', 'AlertNum']
T1857_OUT_BLOCK_NAME = ['검색종목수', '포착시간', '실시간키']
T1857_OUT_BLOCK_1_CODE = ['shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'JobFlag']
T1857_OUT_BLOCK_1_NAME = ['종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '종목상태(N:진입R:재진입O:이탈)']

# Chart 정보 조회 : ChartIndex
CHARTINDEX_IN_BLOCK_CODE = ['indexid', 'indexname', 'indexparam', 'market', 'period', 'shcode', 'qrycnt', 'ncnt', 'sdate', 'edate', 'Isamend', 'Isgab', 'IsReal']
CHARTINDEX_IN_BLOCK_NAME = ['지표ID', '지표명', '지표조건설정', '시장구분', '주기구분', '단축코드', '요청건수(최대500개)', '단위(n틱/n분)', '시작일자', '종료일자', '수정주가반영여부', '갭보정여부', '실시간데이터수신자동등록여부']
CHARTINDEX_OUT_BLOCK_CODE = ['indexid', 'rec_cnt', 'validdata_cnt']
CHARTINDEX_OUT_BLOCK_NAME = ['지표ID', '레코드갯수', '유효데이터컬럼갯수']
CHARTINDEX_OUT_BLOCK_1_CODE = ['date', 'time', 'open', 'high', 'low', 'close', 'volume', 'value1', 'value2', 'value3', 'value4', 'value5', 'pos']
CHARTINDEX_OUT_BLOCK_1_NAME = ['일자', '시간', '시가', '고가', '저가', '종가', '거래량', '지표값1', '지표값2', '지표값3', '지표값4', '지표값5', '위치']

# ETF 관련.
# t1901 : ETF 현재가(시세) 조회.
T1901_IN_BLOCK_CODE = ['shcode']
T1901_IN_BLOCK_NAME = ['단축코드']
T1901_OUT_BLOCK_CODE = ['hname', 'price', 'sign', 'change', 'diff', 'volume', 'recprice', 'avg', 'uplmtprice', 'dnlmtprice', 'jnilvolume', 'volumediff', 'open', 'opentime', 'high', 'hightime', 'low', 'lowtime', 'high52w', 'high52wdate', 'low52w', 'low52wdate', 'exhratio', 'flmtvol', 'per', 'listing', 'jkrate', 'vol', 'shcode', 'value', 'highyear', 'highyeardate', 'lowyear', 'lowyeardate', 'upname', 'upcode', 'upprice', 'upsign', 'upchange', 'updiff', 'futname', 'futcode', 'futprice', 'futsign', 'futchange', 'futdiff', 'nav', 'navsign', 'navchange', 'navdiff', 'cocrate', 'kasis', 'subprice', 'offerno1', 'bidno1', 'dvol1', 'svol1', 'dcha1', 'scha1', 'ddiff1', 'sdiff1', 'offerno2', 'bidno2', 'dvol2', 'svol2', 'dcha2', 'scha2', 'ddiff2', 'sdiff2', 'offerno3', 'bidno3', 'dvol3', 'svol3', 'dcha3', 'scha3', 'ddiff3', 'sdiff3', 'offerno4', 'bidno4', 'dvol4', 'svol4', 'dcha4', 'scha4', 'ddiff4', 'sdiff4', 'offerno5', 'bidno5', 'dvol5', 'svol5', 'dcha5', 'scha5', 'ddiff5', 'sdiff5', 'fwdvl', 'ftradmdcha', 'ftradmddiff', 'fwsvl', 'ftradmscha', 'ftradmsdiff', 'upname2', 'upcode2', 'upprice2', 'jnilnav', 'jnilnavsign', 'jnilnavchange', 'jnilnavdiff', 'etftotcap', 'spread', 'leverage', 'taxgubun', 'opcom_nmk', 'lp_nm1', 'lp_nm2', 'lp_nm3', 'lp_nm4', 'lp_nm5', 'etf_cp', 'etf_kind', 'vi_gubun', 'etn_kind_cd', 'lastymd', 'payday', 'lastdate', 'issuernmk', 'last_sdate', 'last_edate', 'lp_holdvol', 'listdate', 'etp_gb', 'etn_elback_yn', 'settletype', 'idx_asset_class1', 'ty_text', 'leverage2']
T1901_OUT_BLOCK_NAME = ['한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '기준가', '가중평균', '상한가', '하한가', '전일거래량', '거래량차', '시가', '시가시간', '고가', '고가시간', '저가', '저가시간', '52최고가', '52최고가일', '52최저가', '52최 저가일', '소진율', '외국인보유수량', 'PER', '상장주식수(천)', '증거금율', '회전율', '단축코드', '누적거래대금', '연중최고가', '연중최고일자', '연중최저가', '연중최저일자', '업종명', '업종코드', '업종현재가', '업종전일비구분', '업종전일대비', '업종등락율', '선물최근월물명', '선물최근월물코드', '선물현재가', '선물전일비구분', '선물전일대비', '선물등락율', 'NAV', 'NAV전일대비구분', 'NAV전일대비', 'NAV등락율', '추적오차율', '괴리율', '대용가', '매도증권사코드1', '매수증권사코드1', '총매도 수량1', '총매수수량1', '매도증감1', '매수증감1', '매도비율1', '매수비율1', '매도증권사코드2', '매수증권사코드2', '총매도수량2', '총매수수량2', '매도증감2', '매수증감2', '매도비율2', '매수비율2', '매도증권사코드3', '매수증권사코드3', '총매도수량3', '총매수수량3', '매도증감3', '매수증감3', '매도비율3', '매수비율3', '매도증권사코드4', '매수증권사코드4', '총매도수량4', '총매수수량4', '매도증감4', '매수증감4', '매도비율4', '매수비율4', '매도증권사코드5', '매수증권사코드5', '총매도수량5', ' 총매수수량5', '매도증감5', '매수증감5', '매도비율5', '매수비율5', '외국계매도합계수량', '외국계매도직전대비', '외국계매도비율', '외국계매수합계수량', '외국계매수직전대비', '외국계매수비율', '참고지수명', '참고지수코드', '참고지수현재가', '전일NAV', '전일NAV전일대비구분', '전일NAV전일대비', '전일NAV등락율', '순자산총액(억원)', '스프레드', '레버리지', '과세구분', '운용사', 'LP1', 'LP2', 'LP3', 'LP4', 'LP5', '복제방법', '상품유형(Filler)', 'VI발동해제', 'ETN상품분류', 'ETN만기일', 'ETN지 급일', 'ETN최종거래일', 'ETN발행시장참가자', 'ETN만기상환가격결정시작일', 'ETN만기상환가격결정종료일', 'ETNLP보유수량', '상장일', 'ETP상품구분코드', 'ETN조기상환가능여부', '최종결제', '지수자산분류코드(대분류)', 'ETF/ETN투자유의', '추적수익률배 수']

# t1903 : ETF 일별 추이
T1903_IN_BLOCK_CODE = ['shcode', 'date']
T1903_IN_BLOCK_NAME = ['단축코드', '일자']
T1903_OUT_BLOCK_CODE = ['date', 'hname', 'upname']
T1903_OUT_BLOCK_NAME = ['일자', '종목명', '업종지수명']
T1903_OUT_BLOCK_1_CODE = ['date', 'price', 'sign', 'change', 'volume', 'navdiff', 'nav', 'navchange', 'crate', 'grate', 'jisu', 'jichange', 'jirate']
T1903_OUT_BLOCK_1_NAME = ['일자', '현재가', '전일대비구분', '전일대비', '누적거래량', 'NAV대비', 'NAV', '전일대비', '추적오차', '괴리', '지수', '전일대비', '전일대비율']

# t1904 : ETF 구성종목조회
T1904_IN_BLOCK_CODE = ['shcode', 'date', 'sgb']
T1904_IN_BLOCK_NAME = ['ETF단축코드', 'PDF적용일자', '정렬기준(1:평가금액2:증권수)']
T1904_OUT_BLOCK_CODE = ['chk_tday', 'date', 'price', 'sign', 'change', 'diff', 'volume', 'nav', 'navsign', 'navchange', 'navdiff', 'jnilnav', 'jnilnavsign', 'jnilnavchange', 'jnilnavdiff', 'upname', 'upcode', 'upprice', 'upsign', 'upchange', 'updiff', 'futname', 'futcode', 'futprice', 'futsign', 'futchange', 'futdiff', 'upname2', 'upcode2', 'upprice2', 'etftotcap', 'etfnum', 'etfcunum', 'cash', 'opcom_nmk', 'tot_pval', 'tot_sigatval']
T1904_OUT_BLOCK_NAME = ['당일구분', 'PDF적용일자', 'ETF현재가', 'ETF전일대비구분', 'ETF전일대비', 'ETF등락율', 'ETF누적거래량', 'NAV', 'NAV전일대비구분', 'NAV전일대비', 'NAV등락율', '전일NAV', '전일NAV전일대비구분', '전일NAV전일대비', '전일NAV등락율', '업종명', '업종 코드', '업종현재가', '업종전일비구분', '업종전일대비', '업종등락율', '선물최근월물명', '선물최근월물코드', '선물현재가', '선물전일비구분', '선물전일대비', '선물등락율', '참고지수명', '참고지수코드', '참고지수현재가', '순자산총액(단위:억)', '구성종목수', 'CU주식수', '현금', '운용사명', '전종목평가금액합', '전종목구성시가총액합']
T1904_OUT_BLOCK_1_CODE = ['shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'value', 'icux', 'parprice', 'pvalue', 'sigatvalue', 'profitdate', 'weight', 'diff2']
T1904_OUT_BLOCK_1_NAME = ['단축코드', '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래대금(백만)', '단위증권수(계약수/원화현금/USD현금/창고증권)', '액면금액/설정현금액', '평가금액', '구성시가총액', 'PDF적용일자', '비중(평가금액)', 'ETF종목과등락차']

# t1906 : ETF LP 호가
T1906_IN_BLOCK_CODE = ['shcode']
T1906_IN_BLOCK_NAME = ['단축코드']
T1906_OUT_BLOCK_CODE = ['hname', 'price', 'sign', 'change', 'diff', 'volume', 'lp_offerrem1', 'lp_bidrem1', 'lp_offerrem2', 'lp_bidrem2', 'lp_offerrem3', 'lp_bidrem3', 'lp_offerrem4', 'lp_bidrem4', 'lp_offerrem5', 'lp_bidrem5', 'lp_offerrem6', 'lp_bidrem6', 'lp_offerrem7', 'lp_bidrem7', 'lp_offerrem8', 'lp_bidrem8', 'lp_offerrem9', 'lp_bidrem9', 'lp_offerrem10', 'lp_bidrem10', 'jnilclose', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'preoffercha1', 'prebidcha1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'preoffercha2', 'prebidcha2', 'offerho3', 'bidho3', 'offerrem3', 'bidrem3', 'preoffercha3', 'prebidcha3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'preoffercha4', 'prebidcha4', 'offerho5', 'bidho5', 'offerrem5', 'bidrem5', 'preoffercha5', 'prebidcha5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'preoffercha6', 'prebidcha6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'preoffercha7', 'prebidcha7', 'offerho8', 'bidho8', 'offerrem8', 'bidrem8', 'preoffercha8', 'prebidcha8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'preoffercha9', 'prebidcha9', 'offerho10', 'bidho10', 'offerrem10', 'bidrem10', 'preoffercha10', 'prebidcha10', 'offer', 'bid', 'preoffercha', 'prebidcha', 'hotime', 'yeprice', 'yevolume', 'yesign', 'yechange', 'yediff', 'tmoffer', 'tmbid', 'ho_status', 'shcode', 'uplmtprice', 'dnlmtprice', 'open', 'high', 'low']
T1906_OUT_BLOCK_NAME = ['한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', 'LP매도호가수량1', 'LP매수호가수량1', 'LP매도호가수량2', 'LP매수호가수량2', 'LP매도호가수량3', 'LP매수호가수량3', 'LP매도호가수량4', 'LP매수호가수량4', 'LP매도호가수량5', 'LP매수호가수량5', 'LP매도호가수량6', 'LP매수호가수량6', 'LP매도호가수량7', 'LP매수호가수량7', 'LP매도호가수량8', 'LP매수호가수량8', 'LP매도호가수량9', 'LP매수호가수량9', 'LP매도호가수량10', 'LP매수호가수량10', '전일종가', '매도호가1', '매수호가1', '매도호가수량1', '매수호가수량1', '직전매도대비수량1', '직전매수대비수량1', '매도호가2', '매수호가2', '매도호가수량2', '매수호가수량2', '직전매도대비수량2', '직전매수대비수량2', '매도호가3', '매수호가3', '매도호가수량3', '매수호가수량3', '직 전매도대비수량3', '직전매수대비수량3', '매도호가4', '매수호가4', '매도호가수량4', '매수호가수량4', '직전매도대비수량4', '직전매수대비수량4', '매도호가5', '매수호가5', '매도호가수량5', '매수호가수량5', '직전매도대비수량5', '직전매수대비수량5', ' 매도호가6', '매수호가6', '매도호가수량6', '매수호가수량6', '직전매도대비수량6', '직전매수대비수량6', '매도호가7', '매수호가7', '매도호가수량7', '매수호가수량7', '직전매도대비수량7', '직전매수대비수량7', '매도호가8', '매수호가8', '매도호가수량8', '매수호가수량8', '직전매도대비수량8', '직전매수대비수량8', '매도호가9', '매수호가9', '매도호가수량9', '매수호가수량9', '직전매도대비수량9', '직전매수대비수량9', '매도호가10', '매수호가10', '매도호가수량10', '매수호가수량10', '직전매도대비수량10', '직전매수대비수량10', '매도호가수량합', '매수호가수량합', '직전매도대비수량합', '직전매수대비수량합', '수신시간', '예상체결가격', '예상체결수량', '예상체결전일구분', '예상체결전일대비', '예상체결등락율', '시간외매도잔량', '시간외매수잔량', ' 동시구분', '단축코드', '상한가', '하한가', '시가', '고가', '저가']


# I5_ : 코스피 ETF 종목 실시간 NAV. 실제 ETF를 매수(매도?) 하려고 할 때, 이 값을 기준으로 매매하면 된다. 그래서, 이 값을 계속 추적해야 한다.
I5__IN_BLOCK_CODE = ['shcode']
I5__IN_BLOCK_NAME = ['단축코드']
I5__OUT_BLOCK_CODE = ['time', 'price', 'sign', 'change', 'volume', 'navdiff', 'nav', 'navchange', 'crate', 'grate', 'jisu', 'jichange', 'jirate', 'shcode']
I5__OUT_BLOCK_NAME = ['시간', '현재가', '전일대비구분', '전일대비', '누적거래량', 'NAV대비', 'NAV', '전일대비', '추적오차', '괴리', '지수', '전일대비', '전일대비율', '단축코드']

# VI_ : VI 발동/해제
VI__IN_BLOCK_CODE = ['shcode']
VI__IN_BLOCK_NAME = ['단축코드(KEY)']
VI__OUT_BLOCK_CODE = ['vi_gubun', 'svi_recprice', 'dvi_recprice', 'vi_trgprice', 'shcode', 'ref_shcode', 'time']
VI__OUT_BLOCK_NAME = ['구분(0:해제1:정적발동2:동적발동3:정적&동적)', '정적VI발동기준가격', '동적VI발동기준가격', 'VI발동가격', '단축코드(KEY)', '참조코드', '시간']

# t1101 : 주식 현재가 호가 조회
T1101_IN_BLOCK_CODE = ['shcode']
T1101_IN_BLOCK_NAME = ['단축코드']
T1101_OUT_BLOCK_CODE = ['hname', 'price', 'sign', 'change', 'diff', 'volume', 'jnilclose', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'preoffercha1', 'prebidcha1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'preoffercha2', 'prebidcha2', 'offerho3', 'bidho3', 'offerrem3', 'bidrem3', 'preoffercha3', 'prebidcha3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'preoffercha4', 'prebidcha4', 'offerho5', 'bidho5', 'offerrem5', 'bidrem5', 'preoffercha5', 'prebidcha5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'preoffercha6', 'prebidcha6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'preoffercha7', 'prebidcha7', 'offerho8', 'bidho8', 'offerrem8', 'bidrem8', 'preoffercha8', 'prebidcha8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'preoffercha9', 'prebidcha9', 'offerho10', 'bidho10', 'offerrem10', 'bidrem10', 'preoffercha10', 'prebidcha10', 'offer', 'bid', 'preoffercha', 'prebidcha', 'hotime', 'yeprice', 'yevolume', 'yesign', 'yechange', 'yediff', 'tmoffer', 'tmbid', 'ho_status', 'shcode', 'uplmtprice', 'dnlmtprice', 'open', 'high', 'low', 'krx_midprice', 'krx_offermidsumrem', 'krx_bidmidsumrem', 'krx_midsumrem', 'krx_midsumremgubun']
T1101_OUT_BLOCK_NAME = ['한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '전일종가(기준가)', '매도호가1', '매수호가1', '매도호가수량1', '매수호가수량1', '직전매도대비수량1', '직전매수대비수량1', '매도호가2', '매수호가2', '매도호가수량2', '매수호가수량2', '직전매도대비수량2', '직전매수대비수량2', '매도호가3', '매수호가3', '매도호가수량3', '매수호가수량3', '직전매도대비수량3', '직전매수대비수량3', '매도호가4', '매수호가4', '매도호가수량4', '매수호가수량4', '직전 매도대비수량4', '직전매수대비수량4', '매도호가5', '매수호가5', '매도호가수량5', '매수호가수량5', '직전매도대비수량5', '직전매수대비수량5', '매도호가6', '매수호가6', '매도호가수량6', '매수호가수량6', '직전매도대비수량6', '직전매수대비수량6', '매도호가7', '매수호가7', '매도호가수량7', '매수호가수량7', '직전매도대비수량7', '직전매수대비수량7', '매도호가8', '매수호가8', '매도호가수량8', '매수호가수량8', '직전매도대비수량8', '직전매수대비수량8', '매도호가9', '매수호가9', '매도호가수량9', '매수호가수량9', '직전매도대비수량9', '직전매수대비수량9', '매도호가10', '매수호가10', '매도호가수량10', '매수호가수량10', '직전매도대비수량10', '직전매수대비수량10', '매도호가수량합', '매수호가수량합', '직전매도대비수량합', '직전매수대비수량합', '수신시간', '예상체결가격', '예상체결수량', '예상체결전일구분', '예상체결전일대비', '예상체결등락율', '시간외매도잔량', '시간외매수잔량', '동시구분', '단축코드', '상한가', '하한가', '시가', '고가', '저가', 'KRX중간가격', 'KRX매도중간가잔량합계수량', 'KRX매수중간가잔량합계수량', 'KRX중간가잔량합계수량', "KRX중간가잔량구분(''없음'1'매도'2'매"]

# t1486 : 시간대별 예상 체결가
T1486_IN_BLOCK_CODE = ['shcode', 'cts_time', 'cnt', 'exchgubun']
T1486_IN_BLOCK_NAME = ['단축코드', '시간CTS', '조회건수', '거래소구분코드']
T1486_OUT_BLOCK_CODE = ['cts_time', 'ex_shcode']
T1486_OUT_BLOCK_NAME = ['시간CTS', '거래소별단축코드']
T1486_OUT_BLOCK_1_CODE = ['chetime', 'price', 'sign', 'change', 'diff', 'cvolume', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'exchname']
T1486_OUT_BLOCK_1_NAME = ['시간', '예상체결가', '전일대비구분', '전일대비', '등락율', '예상체결량', '매도호가', '매수호가', '매도잔량', '매수잔량', '거래소명']


# 주식클릭종목조회 (관심종목) : t8436
T8436_IN_BLOCK_CODE = ['gubun']
T8436_IN_BLOCK_NAME = ['구분(0:전체1:코스피2:코스닥)']
T8436_OUT_BLOCK_CODE = ['hname', 'shcode', 'expcode', 'etfgubun', 'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun', 'bu12gubun', 'spac_gubun', 'filler']
T8436_OUT_BLOCK_NAME = ['종목명', '단축코드', '확장코드', 'ETF구분(1:ETF2:ETN)', '상한가', '하한가', '전일가', '주문수량단위', '기준가', '구분(1:코스피2:코스닥)', '증권그룹', '기업인수목적회사여부(Y/N)', 'filler(미사용)']

# 종목별상위회원사 (Period Aggregation) : t1752
T1752_IN_BLOCK_CODE = ['shcode', 'traddate1', 'traddate2', 'fwgubun1', 'cts_idx', 'exchgubun']
T1752_IN_BLOCK_NAME = ['종목코드', '조회날짜1', '조회날짜2', '외국계구분', 'CTSIDX', '거래소구분코드']
T1752_OUT_BLOCK_CODE = ['fwdvl', 'fwsvl', 'cts_idx']
T1752_OUT_BLOCK_NAME = ['외국계매도', '외국계매수', 'CTSIDX']
T1752_OUT_BLOCK_1_CODE = ['tradname', 'tradmdvol', 'tradmsvol', 'tradmssvol', 'wintrd', 'winrat', 'tradno', 'wgubun', 'swinrat']
T1752_OUT_BLOCK_1_NAME = ['회원사', '매도수량', '매수수량', '순매수', '창구거래', '비중', '회원사코드', '외국계여부', '순비중']


# 외인기관 종목별동향 : t1702
T1702_IN_BLOCK_CODE = ['shcode', 'fromdt', 'todt', 'volvalgb', 'msmdgb', 'gubun', 'exchgubun']
T1702_IN_BLOCK_NAME = ['종목코드', '시작일자', '종료일자', '금액수량구분(0:금액1:수량2:단가)', '매수매도구분(0:순매수1:매수2:매도)', '누적구분(0:일간1:누적)', '거래소구분코드']
T1702_OUT_BLOCK_1_CODE = ['date', 'close', 'sign', 'change', 'diff', 'volume', 'tjj0000', 'tjj0001', 'tjj0002', 'tjj0003', 'tjj0004', 'tjj0005', 'tjj0006', 'tjj0007', 'tjj0008', 'tjj0009', 'tjj0010', 'tjj0011', 'tjj0018', 'tjj0016', 'tjj0017', 'value']
T1702_OUT_BLOCK_1_NAME = ['일자', '종가', '전일대비구분', '전일대비', '등락율', '누적거래량', '사모펀드', '증권', '보험', '투신', '은행', '종금', '기금', '기타법인', '개인', '등록외국인', '미등록외국인', '국가외', '기관', '외인계(등록+미등록)', '기타계(기타+국가)', '거래대금']

# 외인기관별 종목별동향 : t1717
T1717_IN_BLOCK_CODE = ['shcode', 'gubun', 'fromdt', 'todt', 'dan_gb']
T1717_IN_BLOCK_NAME = ['종목코드', '구분(0:일간순매수1:기간누적순매수)', '시작일자(일간조회일경우는space)', '종료일자', '단가구분(0:전체1:매수혹은매도단가)']
T1717_OUT_BLOCK_CODE = ['date', 'close', 'sign', 'change', 'diff', 'volume', 'tjj0000_vol', 'tjj0001_vol', 'tjj0002_vol', 'tjj0003_vol', 'tjj0004_vol', 'tjj0005_vol', 'tjj0006_vol', 'tjj0007_vol', 'tjj0008_vol', 'tjj0009_vol', 'tjj0010_vol', 'tjj0011_vol', 'tjj0018_vol', 'tjj0016_vol', 'tjj0017_vol', 'tjj0000_dan', 'tjj0001_dan', 'tjj0002_dan', 'tjj0003_dan', 'tjj0004_dan', 'tjj0005_dan', 'tjj0006_dan', 'tjj0007_dan', 'tjj0008_dan', 'tjj0009_dan', 'tjj0010_dan', 'tjj0011_dan', 'tjj0018_dan', 'tjj0016_dan', 'tjj0017_dan']
T1717_OUT_BLOCK_NAME = ['일자', '종가', '전일대비구분', '전일대비', '등락율', '누적거래량', '사모펀드(순매수량)', '증권(순매수량)', '보험(순매수량)', '투신(순매수량)', '은행(순매수량)', '종금(순매수량)', '기금(순매수량)', '기타법인(순매수량)', '개인(순매수량)', '등록외국인(순매수량)', '미등록외국인(순매수량)', '국가외(순매수량)', '기관(순매수량)', '외인계(순매수량)(등록+미등록)', '기타계(순매수량)(기타+국가)', '사모펀드(단가)', '증권(단가)', '보험(단가)', '투신(단가)', '은행(단가)', '종금(단가)', '기금(단가)', '기타법인(단가)', '개인(단가)', '등록외국인(단가)', '미등록외국인(단가)', '국가외(단가)', '기관(단가)', '외인계(단가)(등록+미등록)', '기타계(단가)(기타+국가)']

# 종목별프로그램매매추이 : t1637
T1637_IN_BLOCK_CODE = ['gubun1', 'gubun2', 'shcode', 'date', 'time', 'cts_idx', 'exchgubun']
T1637_IN_BLOCK_NAME = ['수량금액구분(0:수량1:금액)', '시간일별구분(0:시간1:일자)', '종목코드', '일자', '시간', 'IDXCTS(9999:차트)', '거래소구분코드']
T1637_OUT_BLOCK_CODE = ['cts_idx']
T1637_OUT_BLOCK_NAME = ['IDXCTS']
T1637_OUT_BLOCK_1_CODE = ['date', 'time', 'price', 'sign', 'change', 'diff', 'volume', 'svalue', 'offervalue', 'stksvalue', 'svolume', 'offervolume', 'stksvolume', 'shcode', 'ex_shcode']
T1637_OUT_BLOCK_1_NAME = ['일자', '시간', '현재가', '대비구분', '대비', '등락율', '거래량', '순매수금액', '매도금액', '매수금액', '순매수수량', '매도수량', '매수수량', '종목코드', '거래소별단축코드']

# 전체테마 : t8425
T8425_IN_BLOCK_CODE = ['dummy']
T8425_IN_BLOCK_NAME = ['Dummy']
T8425_OUT_BLOCK_CODE = ['tmname', 'tmcode']
T8425_OUT_BLOCK_NAME = ['테마명', '테마코드']

# 거래원별 종목별동향 : t1771
T1771_IN_BLOCK_CODE = ['shcode', 'tradno', 'gubun1', 'traddate1', 'traddate2', 'cts_idx', 'cnt', 'exchgubun']
T1771_IN_BLOCK_NAME = ['종목코드', '거래원코드', '구분1', '거래원날짜1', '거래원날짜2', 'CTSIDX', '요청건수', '거래소구분']
T1771_OUT_BLOCK_CODE = ['cts_idx']
T1771_OUT_BLOCK_NAME = ['CTSIDX']
T1771_OUT_BLOCK_2_CODE = ['traddate', 'tradtime', 'price', 'sign', 'change', 'diff', 'volume', 'tradmdcha', 'tradmscha', 'tradmdval', 'tradmsval', 'tradmsscha', 'tradmttvolume', 'tradavg', 'tradmttavg', 'exchname', 'ex_shcode']
T1771_OUT_BLOCK_2_NAME = ['날짜', '시간', '현재가', '대비구분', '대비', '등락율', '거래량', '매도', '매수', '매도대금', '매수대금', '순매수', '누적순매수', '평균단가', '누적평균단가', '거래소명', '거래소별단축코드']

# 종목별 테마 : t1532
T1532_IN_BLOCK_CODE = ['shcode']
T1532_IN_BLOCK_NAME = ['종목코드']
T1532_OUT_BLOCK_CODE = ['tmname', 'avgdiff', 'tmcode']
T1532_OUT_BLOCK_NAME = ['테마명', '평균등락율', '테마코드']

# 섹터별 종목 : t1531
T1531_IN_BLOCK_CODE = ['tmname', 'tmcode']
T1531_IN_BLOCK_NAME = ['테마명', '테마코드']
T1531_OUT_BLOCK_CODE = ['tmname', 'avgdiff', 'tmcode']
T1531_OUT_BLOCK_NAME = ['테마명', '평균등락율', '테마코드']



def menu_var_name(tr_code=""):
    in_block = []
    out_block = []
    """
    # IN 블록 가져오기
    # var_name = f"{tr_code.upper()}_IN_BLOCK_CODE"
    # in_block_code = globals()[var_name]
    # in_block.append(in_block_code)        
    # var_name = f"{tr_code.upper()}_IN_BLOCK_NAME"
    # in_block_name = globals()[var_name]    
    # in_block.append(in_block_name)        
    # print(in_block_name)
    """
    for block in ['IN_BLOCK_CODE', 'IN_BLOCK_NAME', 'IN_BLOCK_1_CODE', 'IN_BLOCK_1_NAME']:
        var_name = f"{tr_code.upper()}_{block}"
        if var_name in globals():
            in_block.append(globals()[var_name])

    # OUT 블록 가져오기 (존재하는 변수만 추가)
    for block in ['OUT_BLOCK_CODE', 'OUT_BLOCK_NAME', 
                  'OUT_BLOCK_1_CODE', 'OUT_BLOCK_1_NAME',
                  'OUT_BLOCK_2_CODE', 'OUT_BLOCK_2_NAME',
                  'OUT_BLOCK_3_CODE', 'OUT_BLOCK_3_NAME']:
        var_name = f"{tr_code.upper()}_{block}"
        if var_name in globals():
            out_block.append(globals()[var_name])            # print(globals()[var_name])    

    if in_block != "":
        return in_block, out_block
    else:
        return out_block



