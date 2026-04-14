# -*- coding: utf-8 -*-

TR_LIST = {
           'AS0': '해외주식주문접수(미국)',
           'AS1': '해외주식주문체결(미국)',
           'AS2': '해외주식주문정정(미국)',
           'AS3': '해외주식주문취소(미국)',
           'AS4': '해외주식주문거부(미국)',
           'B7_': 'ETF호가잔량(B7)',
           'BMT': '시간대별투자자매매추이(BMT)',
           'BM_': '업종별투자자별매매현황(BM)',
           'CDPCQ04700': '계좌거래내역',
           'CHARTEXCEL': '챠트엑셀데이터조회',
           'CHARTINDEX': '챠트지표데이터조회',
           'CLNAQ00100': '예탁담보융자가능종목현황조회',
           'COSAQ00102': '해외주식API주문체결조회',
           'COSAQ01400': '예약주문처리결과조회',
           'COSAT00301': '미국시장주문API',
           'COSAT00311': '미국시장정정주문API',
           'COSAT00400': '해외주식예약주문등록및취소',
           'COSMT00300': '해외증권매도상환주문(미국)',
           'COSOQ00201': '해외주식종합잔고평가API',
           'COSOQ02701': '해외주식예수금조회API',
           'CSPAQ00600': '계좌별신용한도조회',
           'CSPAQ12200': '현물계좌예수금주문가능금액총평가조회',
           'CSPAQ12300': 'BEP단가조회',
           'CSPAQ13700': '현물계좌주문체결내역조회',
           'CSPAQ22200': '현물계좌예수금주문가능금액총평가2',
           'CSPAT00600': '현물주문',
           'CSPAT00700': '현물정정주문',
           'CSPAT00800': '현물취소주문',
           'CSPBQ00200': '현물계좌증거금률별주문가능수량조회',
           'CUR': '현물정보USD실시간(CUR)',
           'DH1': 'KOSPI시간외단일가호가잔량(DH1)',
           'DHA': 'KOSDAQ시간외단일가호가잔량(DHA)',
           'DK3': 'KOSDAQ시간외단일가체결(DK3)',
           'DS3': 'KOSPI시간외단일가체결(DS3)',
           'DVI': '시간외단일가VI발동해제(DVI)',
           'FOCCQ33600': '주식계좌기간별수익률상세',
           'GSC': '해외주식체결(GSC)',
           'GSH': '해외주식호가(GSH)',
           'H1_': 'KOSPI호가잔량(H1)',
           'H2_': 'KOSPI장전시간외호가잔량(H2)',
           'HA_': 'KOSDAQ호가잔량(HA)',
           'HB_': 'KOSDAQ장전시간외호가잔량(HB)',
           'I5_': '코스피ETF종목실시간NAV(I5)',
           'IJ_': '지수(IJ)',
           'JIF': '장운영정보(JIF)',
           'K1_': 'KOSPI거래원(K1)',
           'K3_': 'KOSDAQ체결(K3)',
           'KH_': 'KOSDAQ프로그램매매종목별(KH)',
           'KM_': 'KOSDAQ프로그램매매전체집계(KM)',
           'KS_': 'KOSDAQ우선호가(KS)',
           'MK2': 'US지수(MK2)',
           'NBM': 'NXT업종별투자자별매매현황(투자자별매매종합)(NBM)',
           'NBT': 'NXT시간대별투자자매매추이(투자자종합)(NBT)',
           'NH1': 'NXTKOSPI+KOSDAQ호가잔량(NH1)',
           'NK1': 'NXTKOSPI+KOSDAQ거래원(NK1)',
           'NPH': 'NXT프로그램매매종목별(뉴스/검색겸용)(NPH)',
           'NPM': 'NXT프로그램매매전체집계(NPM)',
           'NS2': 'NXTKOSPI+KOSDAQ우선호가(NS2)',
           'NS3': 'NXTKOSPI+KOSDAQ체결(NS3)',
           'NVI': 'NXTVI발동해제(NVI)',
           'NWS': '실시간뉴스제목패킷(NWS)',
           'NYS': 'NXTKOSPI+KOSDQT예상체결(NYS)',
           'OK_': 'KOSDAQ거래원(OK)',
           'PH_': 'KOSPI프로그램매매종목별(PH)',
           'PM_': 'KOSPI프로그램매매전체집계(PM)',
           'S2_': 'KOSPI우선호가(S2)',
           'S3_': 'KOSPI체결(S3)',
           'S4_': 'KOSPI기세(S4)',
           'SC0': '주식주문접수',
           'SC1': '주식주문체결',
           'SC2': '주식주문정정',
           'SC3': '주식주문취소',
           'SC4': '주식주문거부',
           'SHC': '상/하한가근접진입(SHC)',
           'SHD': '상/하한가근접이탈(SHD)',
           'SHI': '상/하한가진입(SHI)',
           'SHO': '상/하한가이탈(SHO)',
           'UBM': 'KRX+NXT업종별투자자별매매현황(투자자별매매종합)',
           'UBT': 'KRX+NXT시간대별투자자매매추이(투자자종합)(UBT)',
           'UH1': 'KRX+NXT통합호가잔량(UH1)',
           'UK1': 'KRX+NXT통합KOSPI+KOSDAQ거래원(UK1)',
           'UPH': 'KRX+NXT통합프로그램매매종목별(뉴스/검색겸용)(UPH)',
           'UPM': 'KRX+NXT통합프로그램매매전체집계(UPM)',
           'US2': 'KRX+NXT통합우선호가(US2)',
           'US3': 'KRX+NXT통합체결(US3)',
           'UVI': 'KRX+NXT통합VI발동/해제',
           'UYS': 'KOSPI+KOSDAQ예상체결(UYS)',
           'VI_': 'VI발동해제(VI_)',
           'YJ_': '예상지수(YJ)',
           'YK3': 'KOSDAQ예상체결(YK3)',
           'YS3': 'KOSPI예상체결(YS3)',
           'g3101': '해외주식API현재가(g3101)',
           'g3102': '해외주식API시간대별(g3102)',
           'g3103': '해외주식API일주월별조회(g3103)',
           'g3104': '해외주식API종목정보조회(g3104)',
           'g3106': '해외주식API현재가호가조회(g3106)',
           'g3190': '해외주식API마스터조회(g3190)',
           'g3202': '해외주식차트NTICK',
           'g3203': '해외주식차트NMIN',
           'g3204': '해외주식차트일주월년별',
           't0150': '주식당일매매일지/수수료(t0150)',
           't0151': '주식당일매매일지/수수료(전일)(t0151)',
           't0167': '서버시간조회(t0167)',
           't0424': '주식잔고2(t0424)',
           't0425': '주식체결/미체결(t0425)',
           't1101': '주식현재가호가조회(t1101)',
           't1102': '주식현재가(시세)조회(t1102)',
           't1104': '주식현재가시세메모(t1104)',
           't1105': '주식피못/디마크조회(t1105)',
           't1109': '시간외체결량(t1109)',
           't1301': '주식시간대별체결조회(t1301)',
           't1302': '주식분별주가조회(t1302)',
           't1305': '기간별주가(t1305)',
           't1308': '주식시간대별체결조회챠트(t1308)',
           't1310': '주식당일전일분틱조회(t1310)',
           't1403': '신규상장종목조회(t1403)',
           't1404': '관리/불성실/투자유의조회(t1404)',
           't1405': '투자경고/매매정지/정리매매조회(t1405)',
           't1410': '초저유동성조회(t1410)',
           't1411': '증거금율별종목조회(t1411)',
           't1422': '상/하한(t1422)',
           't1427': '상/하한가직전(t1427)',
           't1441': '등락율상위(t1441)',
           't1442': '신고/신저가(t1442)',
           't1444': '시가총액상위(t1444)',
           't1449': '가격대별매매비중조회(t1449)',
           't1452': '거래량상위(t1452)',
           't1463': '거래대금상위(t1463)',
           't1466': '전일동시간대비거래급증(t1466)',
           't1471': '시간대별호가잔량추이(t1471)',
           't1475': '체결강도추이(t1475)',
           't1481': '시간외등락율상위(t1481)',
           't1482': '거래량상위(t1482)',
           't1485': '예상지수(t1485)',
           't1486': '시간별예상체결가(t1486)',
           't1488': '예상체결가등락율상위조회(t1488)',
           't1489': '예상체결량상위조회(t1489)',
           't1492': '단일가예상등락율상위(t1492)',
           't1511': '업종현재가(t1511)',
           't1514': '업종기간별추이(t1514)',
           't1516': '업종별종목시세(t1516)',
           't1531': '테마별종목(t1531)',
           't1532': '종목별테마(t1532)',
           't1533': '특이테마(t1533)',
           't1537': '테마종목별시세조회(t1537)',
           't1601': '투자자별종합(t1601)',
           't1602': '시간대별투자자매매추이(t1602)',
           't1603': '시간대별투자자매매추이상세(t1603)',
           't1615': '투자자매매종합1(t1615)',
           't1617': '투자자매매종합2(t1617)',
           't1621': '업종별분별투자자매매동향(챠트용)',
           't1631': '프로그램매매종합조회(t1631)',
           't1632': '시간대별프로그램매매추이(t1632)',
           't1633': '기간별프로그램매매추이(t1633)',
           't1636': '종목별프로그램매매동향(t1636)',
           't1637': '종목별프로그램매매추이(t1637)',
           't1638': '종목별잔량/사전공시(t1638)',
           't1640': '프로그램매매종합조회(미니)(t1640)',
           't1662': '시간대별프로그램매매추이(차트)(t1662)',
           't1664': '투자자매매종합(챠트)',
           't1665': '기간별투자자매매추이(챠트)',
           't1702': '외인기관종목별동향(t1702)',
           't1716': '외인기관종목별동향(t1716)',
           't1717': '외인기관종목별동향(t1717)',
           't1752': '종목별상위회원사(t1752)',
           't1764': '회원사리스트(t1764)',
           't1771': '종목별회원사추이(t1771)',
           't1809': '신호조회(t1809)',
           't1825': '종목Q클릭검색(씽큐스마트)(t1825)',
           't1826': '종목Q클릭검색리스트조회(씽큐스마트)(t1826)',
           't1857': 'e종목검색(신버전API용)',
           't1866': '서버저장조건리스트조회(API)(t1866)',
           't1901': 'ETF현재가(시세)조회(t1901)',
           't1902': 'ETF시간별추이(t1902)',
           't1903': 'ETF일별추이(t1903)',
           't1904': 'ETF구성종목조회(t1904)',
           't1906': 'ETFLP호가(t1906)',
           't1921': '신용거래동향(t1921)',
           't1926': '종목별신용정보(t1926)',
           't1927': '공매도일별추이(t1927)',
           't1941': '종목별대차거래일간추이(t1941)',
           't3102': '뉴스본문(t3102)',
           't3202': '종목별증시일정(t3202)',
           't3320': 'FNG_요약(t3320)',
           't3341': '재무순위종합(t3341)',
           't3401': '투자의견(t3401)',
           't3518': '해외실시간지수(t3518)',
           't3521': '해외지수조회(API용)(t3521)',
           't4203': '업종챠트(종합)(t4203)',
           't8407': 'API용주식멀티현재가조회(t8407)',
           't8410': 'API전용주식챠트(일주월년)(t8410)',
           't8411': '주식챠트(틱/n틱)(t8411)',
           't8412': '주식챠트(N분)(t8412)',
           't8417': '업종차트(틱/n틱)(t8417)',
           't8418': '업종챠트(N분)(t8418)',
           't8419': '업종챠트(일주월)(t8419)',
           't8424': '전체업종(t8424)',
           't8425': '전체테마(t8425)',
           't8428': '증시주변자금추이(t8428)',
           't8430': '주식종목조회(t8430)',
           't8436': '주식종목조회API용(t8436)',
           't8450': '주식현재가호가조회(t8450)',
           't8451': '주식챠트(일주월년)(t8451)',
           't8452': '주식챠트(종합)(t8452)',
           't8453': '주식챠트(틱/n틱)(t8453)',
           't8454': '주식시간대별체결조회2(t8454)',
           't9945': '주식마스터조회API용-종목명40bytes(t9945)'

        }


# AS0
AS0_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'sOrdxctPtnCode', 'sOrdMktCode', 'sOrdPtnCode',
           'sOrgOrdNo', 'sAcntNo', 'sPwd', 'sIsuNo', 'sShtnIsuNo', 'sIsuNm', 'sOrdQty', 'sOrdPrc', 'sOrdCndi', 'sOrdprcPtnCode',
           'sStrtgCode', 'sGrpId', 'sOrdSeqno', 'sCommdaCode', 'sOrdNo', 'sOrdTime', 'sPrntOrdNo', 'sOrgOrdUnercQty', 'sOrgOrdMdfyQty', 'sOrgOrdCancQty',
           'sNmcpySndNo', 'sOrdAmt', 'sBnsTp', 'sMtiordSeqno', 'sOrdUserId', 'sSpotOrdQty', 'sRuseOrdQty', 'sOrdMny', 'sOrdSubstAmt', 'sOrdRuseAmt',
           'sUseCmsnAmt', 'sSecBalQty', 'sSpotOrdAbleQty', 'sOrdAbleRuseQty', 'sFlctQty', 'sSecBalQtyD2', 'sSellAbleQty', 'sUnercSellOrdQty', 'sAvrPchsPrc', 'sPchsAmt',
           'sDeposit', 'sSubstAmt', 'sCsgnMnyMgn', 'sCsgnSubstMgn', 'sOrdAbleMny', 'sOrdAbleSubstAmt', 'sRuseAbleAmt', 'sMgntrnCode']
AS0_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '원주문번호', '계좌번호', '비밀번호', '종목번호', '단축종목번호', '종목명', '주문수량', '주문가', '주문조건', '호가유형코드',
           '전략코드', '그룹ID', '주문회차', '통신매체코드', '주문번호', '주문시각', '모주문번호', '원주문미체결수량', '원주문정정수량', '원주문취소수량',
           '비회원사송신번호', '주문금액', '매매구분', '복수주문일련번호', '주문사원번호', '실물주문수량', '재사용주문수량', '주문현금', '주문대용금액', '주문재사용금액',
           '사용수수료', '잔고수량', '실물주문가능수량', '주문가능재사용수량', '변동수량', '잔고수량(D2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액',
           '예수금', '대용금', '위탁현금증거금액', '위탁대용증거금액', '주문가능현금', '주문가능대용금액', '재사용가능금액', '신용거래코드']

# AS1
AS1_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'sOrdxctPtnCode', 'sOrdMktCode', 'sOrdPtnCode',
           'sMgmtBrnNo', 'sAcntNo', 'sAcntNm', 'sIsuNo', 'sIsuNm', 'sOrdNo', 'sOrgOrdNo', 'sExecNO', 'sAbrdExecId', 'sOrdQty',
           'sOrdPrc', 'sExecQty', 'sExecPrc', 'sMdfyCnfQty', 'sMdfyCnfPrc', 'sCancCnfQty', 'sRjtQty', 'sOrdTrxPtnCode', 'sMtiordSeqno', 'sOrdCndi',
           'sOrdprcPtnCode', 'sShtnIsuNo', 'sOpDrtnNo', 'sUnercQty', 'sOrgOrdUnercQty', 'sOrgOrdMdfyQty', 'sOrgOrdCancQty', 'sOrdAvrExecPrc', 'sOrdAmt', 'sStdIsuNo',
           'sBnsTp', 'sCommdaCode', 'sOrdAcntNo', 'sAgrgtBrnNo', 'sRegMktCode', 'sMnyMgnRat', 'sSubstMgnRat', 'sMnyExecAmt', 'sSubstExecAmt', 'sCmsnAmtExecAmt',
           'sPrdayRuseExecVal', 'sCrdayRuseExecVal', 'sSpotExecQty', 'sStslExecQty', 'sStrtgCode', 'sGrpId', 'sOrdSeqno', 'sOrdUserId', 'sExecTime', 'sRcptExecTime',
           'sRjtRsn', 'sSecBalQty', 'sSpotOrdAbleQty', 'sOrdAbleRuseQty', 'sFlctQty', 'sSecBalQtyD2', 'sSellAbleQty', 'sUnercSellOrdQty', 'sAvrPchsPrc', 'sPchsAmt',
           'sDeposit', 'sSubstAmt', 'sCsgnMnyMgn', 'sCsgnSubstMgn', 'sOrdAbleMny', 'sOrdAbleSubstAmt', 'sRuseAbleAmt', 'sMgntrnCode']
AS1_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '해외체결ID', '주문수량',
           '주문가', '체결수량', '체결가', '정정확인수량', '정정확인가', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '단축종목번호', '운용지시번호', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가', '주문금액', '표준종목번호',
           '매매구분', '통신매체코드', '주문계좌번호', '집계지점번호', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액', '대용체결금액', '수수료체결금액',
           '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹ID', '주문회차', '주문자ID', '체결시각', '거래소수신체결시각',
           '거부사유', '잔고수량', '실물주문가능수량', '주문가능재사용수량', '변동수량', '잔고수량(D2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액',
           '예수금', '대용금', '위탁현금증거금액', '위탁대용증거금액', '주문가능현금', '주문가능대용금액', '재사용가능금액', '신용거래코드']

# AS2
AS2_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'sOrdxctPtnCode', 'sOrdMktCode', 'sOrdPtnCode',
           'sMgmtBrnNo', 'sAcntNo', 'sAcntNm', 'sIsuNo', 'sIsuNm', 'sOrdNo', 'sOrgOrdNo', 'sExecNO', 'sAbrdExecId', 'sOrdQty',
           'sOrdPrc', 'sExecQty', 'sExecPrc', 'sMdfyCnfQty', 'sMdfyCnfPrc', 'sCancCnfQty', 'sRjtQty', 'sOrdTrxPtnCode', 'sMtiordSeqno', 'sOrdCndi',
           'sOrdprcPtnCode', 'sShtnIsuNo', 'sOpDrtnNo', 'sUnercQty', 'sOrgOrdUnercQty', 'sOrgOrdMdfyQty', 'sOrgOrdCancQty', 'sOrdAvrExecPrc', 'sOrdAmt', 'sStdIsuNo',
           'sBnsTp', 'sCommdaCode', 'sOrdAcntNo', 'sAgrgtBrnNo', 'sRegMktCode', 'sMnyMgnRat', 'sSubstMgnRat', 'sMnyExecAmt', 'sSubstExecAmt', 'sCmsnAmtExecAmt',
           'sPrdayRuseExecVal', 'sCrdayRuseExecVal', 'sSpotExecQty', 'sStslExecQty', 'sStrtgCode', 'sGrpId', 'sOrdSeqno', 'sOrdUserId', 'sExecTime', 'sRcptExecTime',
           'sRjtRsn', 'sSecBalQty', 'sSpotOrdAbleQty', 'sOrdAbleRuseQty', 'sFlctQty', 'sSecBalQtyD2', 'sSellAbleQty', 'sUnercSellOrdQty', 'sAvrPchsPrc', 'sPchsAmt',
           'sDeposit', 'sSubstAmt', 'sCsgnMnyMgn', 'sCsgnSubstMgn', 'sOrdAbleMny', 'sOrdAbleSubstAmt', 'sRuseAbleAmt', 'sMgntrnCode']
AS2_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '해외체결ID', '주문수량',
           '주문가', '체결수량', '체결가', '정정확인수량', '정정확인가', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '단축종목번호', '운용지시번호', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가', '주문금액', '표준종목번호',
           '매매구분', '통신매체코드', '주문계좌번호', '집계지점번호', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액', '대용체결금액', '수수료체결금액',
           '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹ID', '주문회차', '주문자ID', '체결시각', '거래소수신체결시각',
           '거부사유', '잔고수량', '실물주문가능수량', '주문가능재사용수량', '변동수량', '잔고수량(D2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액',
           '예수금', '대용금', '위탁현금증거금액', '위탁대용증거금액', '주문가능현금', '주문가능대용금액', '재사용가능금액', '신용거래코드']

# AS3
AS3_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'sOrdxctPtnCode', 'sOrdMktCode', 'sOrdPtnCode',
           'sMgmtBrnNo', 'sAcntNo', 'sAcntNm', 'sIsuNo', 'sIsuNm', 'sOrdNo', 'sOrgOrdNo', 'sExecNO', 'sAbrdExecId', 'sOrdQty',
           'sOrdPrc', 'sExecQty', 'sExecPrc', 'sMdfyCnfQty', 'sMdfyCnfPrc', 'sCancCnfQty', 'sRjtQty', 'sOrdTrxPtnCode', 'sMtiordSeqno', 'sOrdCndi',
           'sOrdprcPtnCode', 'sShtnIsuNo', 'sOpDrtnNo', 'sUnercQty', 'sOrgOrdUnercQty', 'sOrgOrdMdfyQty', 'sOrgOrdCancQty', 'sOrdAvrExecPrc', 'sOrdAmt', 'sStdIsuNo',
           'sBnsTp', 'sCommdaCode', 'sOrdAcntNo', 'sAgrgtBrnNo', 'sRegMktCode', 'sMnyMgnRat', 'sSubstMgnRat', 'sMnyExecAmt', 'sSubstExecAmt', 'sCmsnAmtExecAmt',
           'sPrdayRuseExecVal', 'sCrdayRuseExecVal', 'sSpotExecQty', 'sStslExecQty', 'sStrtgCode', 'sGrpId', 'sOrdSeqno', 'sOrdUserId', 'sExecTime', 'sRcptExecTime',
           'sRjtRsn', 'sSecBalQty', 'sSpotOrdAbleQty', 'sOrdAbleRuseQty', 'sFlctQty', 'sSecBalQtyD2', 'sSellAbleQty', 'sUnercSellOrdQty', 'sAvrPchsPrc', 'sPchsAmt',
           'sDeposit', 'sSubstAmt', 'sCsgnMnyMgn', 'sCsgnSubstMgn', 'sOrdAbleMny', 'sOrdAbleSubstAmt', 'sRuseAbleAmt', 'sMgntrnCode']
AS3_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '해외체결ID', '주문수량',
           '주문가', '체결수량', '체결가', '정정확인수량', '정정확인가', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '단축종목번호', '운용지시번호', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가', '주문금액', '표준종목번호',
           '매매구분', '통신매체코드', '주문계좌번호', '집계지점번호', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액', '대용체결금액', '수수료체결금액',
           '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹ID', '주문회차', '주문자ID', '체결시각', '거래소수신체결시각',
           '거부사유', '잔고수량', '실물주문가능수량', '주문가능재사용수량', '변동수량', '잔고수량(D2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액',
           '예수금', '대용금', '위탁현금증거금액', '위탁대용증거금액', '주문가능현금', '주문가능대용금액', '재사용가능금액', '신용거래코드']

# AS4
AS4_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'sOrdxctPtnCode', 'sOrdMktCode', 'sOrdPtnCode',
           'sMgmtBrnNo', 'sAcntNo', 'sAcntNm', 'sIsuNo', 'sIsuNm', 'sOrdNo', 'sOrgOrdNo', 'sExecNO', 'sAbrdExecId', 'sOrdQty',
           'sOrdPrc', 'sExecQty', 'sExecPrc', 'sMdfyCnfQty', 'sMdfyCnfPrc', 'sCancCnfQty', 'sRjtQty', 'sOrdTrxPtnCode', 'sMtiordSeqno', 'sOrdCndi',
           'sOrdprcPtnCode', 'sShtnIsuNo', 'sOpDrtnNo', 'sUnercQty', 'sOrgOrdUnercQty', 'sOrgOrdMdfyQty', 'sOrgOrdCancQty', 'sOrdAvrExecPrc', 'sOrdAmt', 'sStdIsuNo',
           'sBnsTp', 'sCommdaCode', 'sOrdAcntNo', 'sAgrgtBrnNo', 'sRegMktCode', 'sMnyMgnRat', 'sSubstMgnRat', 'sMnyExecAmt', 'sSubstExecAmt', 'sCmsnAmtExecAmt',
           'sPrdayRuseExecVal', 'sCrdayRuseExecVal', 'sSpotExecQty', 'sStslExecQty', 'sStrtgCode', 'sGrpId', 'sOrdSeqno', 'sOrdUserId', 'sExecTime', 'sRcptExecTime',
           'sRjtRsn', 'sSecBalQty', 'sSpotOrdAbleQty', 'sOrdAbleRuseQty', 'sFlctQty', 'sSecBalQtyD2', 'sSellAbleQty', 'sUnercSellOrdQty', 'sAvrPchsPrc', 'sPchsAmt',
           'sDeposit', 'sSubstAmt', 'sCsgnMnyMgn', 'sCsgnSubstMgn', 'sOrdAbleMny', 'sOrdAbleSubstAmt', 'sRuseAbleAmt', 'sMgntrnCode']
AS4_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '해외체결ID', '주문수량',
           '주문가', '체결수량', '체결가', '정정확인수량', '정정확인가', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '단축종목번호', '운용지시번호', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가', '주문금액', '표준종목번호',
           '매매구분', '통신매체코드', '주문계좌번호', '집계지점번호', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액', '대용체결금액', '수수료체결금액',
           '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹ID', '주문회차', '주문자ID', '체결시각', '거래소수신체결시각',
           '거부사유', '잔고수량', '실물주문가능수량', '주문가능재사용수량', '변동수량', '잔고수량(D2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액',
           '예수금', '대용금', '위탁현금증거금액', '위탁대용증거금액', '주문가능현금', '주문가능대용금액', '재사용가능금액', '신용거래코드']

# B7_
B7__IN_BLOCK_CODE = ['shcode']
B7__IN_BLOCK_NAME = ['단축코드']
B7__OUT_BLOCK_CODE = [
           'hotime', 'lp_offerho1', 'lp_bidho1', 'lp_offerho2', 'lp_bidho2', 'lp_offerho3', 'lp_bidho3', 'lp_offerho4', 'lp_bidho4', 'lp_offerho5',
           'lp_bidho5', 'lp_offerho6', 'lp_bidho6', 'lp_offerho7', 'lp_bidho7', 'lp_offerho8', 'lp_bidho8', 'lp_offerho9', 'lp_bidho9', 'lp_offerho10',
           'lp_bidho10', 'shcode', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2',
           'offerho3', 'bidho3', 'offerrem3', 'bidrem3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'offerho5', 'bidho5',
           'offerrem5', 'bidrem5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7',
           'offerho8', 'bidho8', 'offerrem8', 'bidrem8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'offerho10', 'bidho10',
           'offerrem10', 'bidrem10', 'totofferrem', 'totbidrem', 'donsigubun', 'alloc_gubun', 'midprice', 'offermidsumrem', 'bidmidsumrem']
B7__OUT_BLOCK_NAME = [
           '호가시간', 'LP매도호가수량1', 'LP매수호가수량1', 'LP매도호가수량2', 'LP매수호가수량2', 'LP매도호가수량3', 'LP매수호가수량3', 'LP매도호가수량4', 'LP매수호가수량4', 'LP매도호가수량5',
           'LP매수호가수량5', 'LP매도호가수량6', 'LP매수호가수량6', 'LP매도호가수량7', 'LP매수호가수량7', 'LP매도호가수량8', 'LP매수호가수량8', 'LP매도호가수량9', 'LP매수호가수량9', 'LP매도호가수량10',
           'LP매수호가수량10', '단축코드', '매도호가1', '매수호가1', '매도호가잔량1', '매수호가잔량1', '매도호가2', '매수호가2', '매도호가잔량2', '매수호가잔량2',
           '매도호가3', '매수호가3', '매도호가잔량3', '매수호가잔량3', '매도호가4', '매수호가4', '매도호가잔량4', '매수호가잔량4', '매도호가5', '매수호가5',
           '매도호가잔량5', '매수호가잔량5', '매도호가6', '매수호가6', '매도호가잔량6', '매수호가잔량6', '매도호가7', '매수호가7', '매도호가잔량7', '매수호가잔량7',
           '매도호가8', '매수호가8', '매도호가잔량8', '매수호가잔량8', '매도호가9', '매수호가9', '매도호가잔량9', '매수호가잔량9', '매도호가10', '매수호가10',
           '매도호가잔량10', '매수호가잔량10', '총매도호가잔량', '총매수호가잔량', '동시호가구분', '배분적용구분', '중간가격', '매도중간가잔량합계수량', '매수중간가잔량합계수량']

# BMT
BMT_IN_BLOCK_CODE = ['upcode']
BMT_IN_BLOCK_NAME = ['업종코드']
BMT_OUT_BLOCK_CODE = [
           'tjjtime', 'tjjcode1', 'msvolume1', 'mdvolume1', 'msvol1', 'msvalue1', 'mdvalue1', 'msval1', 'tjjcode2', 'msvolume2',
           'mdvolume2', 'msvol2', 'msvalue2', 'mdvalue2', 'msval2', 'tjjcode3', 'msvolume3', 'mdvolume3', 'msvol3', 'msvalue3',
           'mdvalue3', 'msval3', 'tjjcode4', 'msvolume4', 'mdvolume4', 'msvol4', 'msvalue4', 'mdvalue4', 'msval4', 'tjjcode5',
           'msvolume5', 'mdvolume5', 'msvol5', 'msvalue5', 'mdvalue5', 'msval5', 'tjjcode6', 'msvolume6', 'mdvolume6', 'msvol6',
           'msvalue6', 'mdvalue6', 'msval6', 'tjjcode7', 'msvolume7', 'mdvolume7', 'msvol7', 'msvalue7', 'mdvalue7', 'msval7',
           'tjjcode8', 'msvolume8', 'mdvolume8', 'msvol8', 'msvalue8', 'mdvalue8', 'msval8', 'tjjcode9', 'msvolume9', 'mdvolume9',
           'msvol9', 'msvalue9', 'mdvalue9', 'msval9', 'tjjcode10', 'msvolume10', 'mdvolume10', 'msvol10', 'msvalue10', 'mdvalue10',
           'msval10', 'tjjcode11', 'msvolume11', 'mdvolume11', 'msvol11', 'msvalue11', 'mdvalue11', 'msval11', 'upcode', 'tjjcode0',
           'msvolume0', 'mdvolume0', 'msvol0', 'msvalue0', 'mdvalue0', 'msval0']
BMT_OUT_BLOCK_NAME = [
           '수신시간', '투자자코드1(개인)', '매수거래량1', '매도거래량1', '거래량순매수1', '매수거래대금1', '매도거래대금1', '거래대금순매수1', '투자자코드2(외국인)', '매수거래량2',
           '매도거래량2', '거래량순매수2', '매수거래대금2', '매도거래대금2', '거래대금순매수2', '투자자코드3(기관계)', '매수거래량3', '매도거래량3', '거래량순매수3', '매수거래대금3',
           '매도거래대금3', '거래대금순매수3', '투자자코드4(증권)', '매수거래량4', '매도거래량4', '거래량순매수4', '매수거래대금4', '매도거래대금4', '거래대금순매수4', '투자자코드5(투신)',
           '매수거래량5', '매도거래량5', '거래량순매수5', '매수거래대금5', '매도거래대금5', '거래대금순매수5', '투자자코드6(은행)', '매수거래량6', '매도거래량6', '거래량순매수6',
           '매수거래대금6', '매도거래대금6', '거래대금순매수6', '투자자코드7(보험)', '매수거래량7', '매도거래량7', '거래량순매수7', '매수거래대금7', '매도거래대금7', '거래대금순매수7',
           '투자자코드8(종금)', '매수거래량8', '매도거래량8', '거래량순매수8', '매수거래대금8', '매도거래대금8', '거래대금순매수8', '투자자코드9(기금)', '매수거래량9', '매도거래량9',
           '거래량순매수9', '매수거래대금9', '매도거래대금9', '거래대금순매수9', '투자자코드10(선물업자)', '매수거래량10', '매도거래량10', '거래량순매수10', '매수거래대금10', '매도거래대금10',
           '거래대금순매수10', '투자자코드11(기타)', '매수거래량11', '매도거래량11', '거래량순매수11', '매수거래대금11', '매도거래대금11', '거래대금순매수11', '업종코드', '투자자코드0(사모펀드)',
           '매수거래량0', '매도거래량0', '거래량순매수0', '매수거래대금0', '매도거래대금0', '거래대금순매수0']

# BM_
BM__IN_BLOCK_CODE = ['upcode']
BM__IN_BLOCK_NAME = ['업종코드']
BM__OUT_BLOCK_CODE = [
           'tjjcode', 'tjjtime', 'msvolume', 'mdvolume', 'msvol', 'p_msvol', 'msvalue', 'mdvalue', 'msval', 'p_msval',
           'upcode']
BM__OUT_BLOCK_NAME = [
           '투자자코드', '수신시간', '매수거래량', '매도거래량', '거래량순매수', '거래량순매수직전대비', '매수거래대금', '매도거래대금', '거래대금순매수', '거래대금순매수직전대비',
           '업종코드']

# CDPCQ04700
CDPCQ04700_IN_BLOCK_CODE = [
           'RecCnt', 'AcntNo', 'Pwd', 'QrySrtDt', 'QryEndDt', 'SrtNo', 'PdptnCode', 'IsuLgclssCode', 'IsuNo']
CDPCQ04700_IN_BLOCK_NAME = [
           '레코드갯수', '계좌번호', '비밀번호', '조회시작일', '조회종료일', '시작번호', '상품유형코드', '종목대분류코드', '종목번호']
CDPCQ04700_OUT_BLOCK_1_CODE = [
           'RecCnt', 'AcntNo', 'Pwd', 'QrySrtDt', 'QryEndDt', 'SrtNo', 'PdptnCode', 'IsuLgclssCode', 'IsuNo']
CDPCQ04700_OUT_BLOCK_1_NAME = [
           '레코드갯수', '계좌번호', '비밀번호', '조회시작일', '조회종료일', '시작번호', '상품유형코드', '종목대분류코드', '종목번호']
CDPCQ04700_OUT_BLOCK_2_CODE = ['RecCnt']
CDPCQ04700_OUT_BLOCK_2_NAME = ['레코드갯수']
CDPCQ04700_OUT_BLOCK_3_CODE = [
           'AcntNo', 'TrdDt', 'TrdNo', 'TpCodeNm', 'SmryNo', 'SmryNm', 'CancTpNm', 'TrdQty', 'Trtax', 'FcurrAdjstAmt',
           'AdjstAmt', 'OvdSum', 'DpsBfbalAmt', 'SellPldgRfundAmt', 'DpspdgLoanBfbalAmt', 'TrdmdaNm', 'OrgTrdNo', 'IsuNm', 'TrdUprc', 'CmsnAmt',
           'FcurrCmsnAmt', 'RfundDiffAmt', 'RepayAmtSum', 'SecCrbalQty', 'CslLoanRfundIntrstAmt', 'DpspdgLoanCrbalAmt', 'TrxTime', 'Inouno', 'IsuNo', 'TrdAmt',
           'ChckAmt', 'TaxSumAmt', 'FcurrTaxSumAmt', 'IntrstUtlfee', 'MnyDvdAmt', 'RcvblOcrAmt', 'TrxBrnNo', 'TrxBrnNm', 'DpspdgLoanAmt', 'DpspdgLoanRfundAmt',
           'BasePrc', 'DpsCrbalAmt', 'BoaAmt', 'MnyoutAbleAmt', 'BcrLoanOcrAmt', 'BcrLoanBfbalAmt', 'BnsBasePrc', 'TaxchrBasePrc', 'TrdUnit', 'BalUnit',
           'EvrTax', 'EvalAmt', 'BcrLoanRfundAmt', 'BcrLoanCrbalAmt', 'AddMgnOcrTotamt', 'AddMnyMgnOcrAmt', 'AddMgnDfryTotamt', 'AddMnyMgnDfryAmt', 'BnsplAmt', 'Ictax',
           'Ihtax', 'LoanDt', 'CrcyCode', 'FcurrAmt', 'FcurrTrdAmt', 'FcurrDps', 'FcurrDpsBfbalAmt', 'OppAcntNm', 'OppAcntNo', 'LoanRfundAmt',
           'LoanIntrstAmt', 'AskpsnNm', 'OrdDt', 'TrdXchrat', 'RdctCmsn', 'FcurrStmpTx', 'FcurrElecfnTrtax', 'FcstckTrtax']
CDPCQ04700_OUT_BLOCK_3_NAME = [
           '계좌번호', '거래일자', '거래번호', '구분코드명', '적요번호', '적요명', '취소구분', '거래수량', '거래세', '외화정산금액',
           '정산금액', '연체합', '예수금전잔금액', '매도담보상환금', '예탁담보대출전잔금액', '거래매체명', '원거래번호', '종목명', '거래단가', '수수료',
           '외화수수료금액', '상환차이금액', '변제금합계', '유가증권금잔수량', '매도대금담보대출상환이자금액', '예탁담보대출금잔금액', '처리시각', '출납번호', '종목번호', '거래금액',
           '수표금액', '세금합계금액', '외화세금합계금액', '이자이용료', '배당금액', '미수발생금액', '처리지점번호', '처리지점명', '예탁담보대출금액', '예탁담보대출상환금액',
           '기준가', '예수금금잔금액', '과표', '출금가능금액', '수익증권담보대출발생금', '수익증권담보대출전잔금', '매매기준가', '과세기준가', '거래좌수', '잔고좌수',
           '제세금', '평가금액', '수익증권담보대출상환금', '수익증권담보대출금잔금', '추가증거금발생총액', '추가현금증거금발생금액', '추가증거금납부총액', '추가현금증거금납부금액', '매매손익금액', '소득세',
           '주민세', '대출일', '통화코드', '외화금액', '외화거래금액', '외화예수금', '외화예수금전잔금액', '상대계좌명', '상대계좌번호', '대출상환금액',
           '대출이자금액', '의뢰인명', '주문일자', '거래환율', '감면수수료', '외화인지세', '외화전자금융거래세', '외화증권거래세']
CDPCQ04700_OUT_BLOCK_4_CODE = ['RecCnt', 'CtrctAsm', 'CmsnAmtSumAmt']
CDPCQ04700_OUT_BLOCK_4_NAME = ['레코드갯수', '약정누계', '수수료합계금액']
CDPCQ04700_OUT_BLOCK_5_CODE = [
           'RecCnt', 'SecinAmt', 'MnyoutAmt', 'SecoutAmt', 'DiffAmt', 'DiffAmt0', 'SellQty', 'SellAmt', 'SellCmsn', 'EvrTax',
           'FcurrSellAdjstAmt', 'BuyQty', 'BuyAmt', 'BuyCmsn', 'ExecTax', 'FcurrBuyAdjstAmt']
CDPCQ04700_OUT_BLOCK_5_NAME = [
           '레코드갯수', '입고금액', '출금금액', '출고금액', '차이금액', '차이금액0', '매도수량', '매도금액', '매도수수료', '제세금',
           '외화매도정산금액', '매수수량', '매수금액', '매수수수료', '체결세금', '외화매수정산금액']

# CHARTEXCEL
CHARTEXCEL_IN_BLOCK_CODE = [
           'indexid', 'indexparam', 'indexouttype', 'market', 'period', 'shcode', 'isexcelout', 'excelfilename', 'IsReal']
CHARTEXCEL_IN_BLOCK_NAME = [
           '지표ID', '지표조건설정', '결과데이터구분', '시장구분', '주기구분', '단축코드', '결과지표데이터엑셀표시여부', '엑셀데이터파일명', '실시간데이터수신자동등록여부']
CHARTEXCEL_OUT_BLOCK_CODE = ['indexid', 'rec_cnt', 'validdata_cnt']
CHARTEXCEL_OUT_BLOCK_NAME = ['지표ID', '레코드갯수', '유효데이터컬럼갯수']
CHARTEXCEL_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'volume', 'value1', 'value2', 'value3',
           'value4', 'value5', 'pos']
CHARTEXCEL_OUT_BLOCK_1_NAME = [
           '일자', '시간', '시가', '고가', '저가', '종가', '거래량', '지표값1', '지표값2', '지표값3',
           '지표값4', '지표값5', '위치']

# CHARTINDEX
CHARTINDEX_IN_BLOCK_CODE = [
           'indexid', 'indexparam', 'market', 'period', 'shcode', 'qrycnt', 'ncnt', 'sdate', 'edate', 'Isamend',
           'Isgab', 'IsReal']
CHARTINDEX_IN_BLOCK_NAME = [
           '지표ID', '지표조건설정', '시장구분', '주기구분', '단축코드', '요청건수(최대500개)', '단위(n틱/n분)', '시작일자', '종료일자', '수정주가반영여부',
           '갭보정여부', '실시간데이터수신자동등록여부']
CHARTINDEX_OUT_BLOCK_CODE = ['indexid', 'rec_cnt', 'validdata_cnt']
CHARTINDEX_OUT_BLOCK_NAME = ['지표ID', '레코드갯수', '유효데이터컬럼갯수']
CHARTINDEX_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'volume', 'value1', 'value2', 'value3',
           'value4', 'value5', 'pos']
CHARTINDEX_OUT_BLOCK_1_NAME = [
           '일자', '시간', '시가', '고가', '저가', '종가', '거래량', '지표값1', '지표값2', '지표값3',
           '지표값4', '지표값5', '위치']

# CLNAQ00100
CLNAQ00100_IN_BLOCK_CODE = ['RecCnt', 'IsuNo', 'SecTpCode', 'LoanIntrstGrdCode', 'LoanTp']
CLNAQ00100_IN_BLOCK_NAME = ['레코드갯수', '종목번호', '유가증권구분', '대출이자등급코드', '대출구분']
CLNAQ00100_OUT_BLOCK_1_CODE = ['RecCnt', 'IsuNo', 'SecTpCode', 'LoanIntrstGrdCode', 'LoanTp']
CLNAQ00100_OUT_BLOCK_1_NAME = ['레코드갯수', '종목번호', '유가증권구분', '대출이자등급코드', '대출구분']
CLNAQ00100_OUT_BLOCK_2_CODE = [
           'IsuNo', 'IsuNm', 'Parprc', 'PrdayCprc', 'RatVal', 'SubstPrc', 'RegTpNm', 'SpotMgnLevyClssNm', 'FnoTrdStopRsnCnts', 'DgrsPtnNm',
           'AcdPtnNm', 'MktTpNm', 'LmtVal', 'AcntLmtVal', 'LoanGrdCode', 'LoanAmt', 'LoanAbleRat', 'LoanIntrat1', 'RegPsnId', 'Rat01',
           'Rat02']
CLNAQ00100_OUT_BLOCK_2_NAME = [
           '종목번호', '종목명', '액면가', '전일종가', '비율값', '대용가', '등록구분', '현물증거금징수분류명', '거래정지사유', '요주의유형명',
           '사고유형', '시장구분', '한도값', '계좌한도값', '대출등급코드', '대출금액', '대출가능율', '대출이율1', '등록자ID', '비율값',
           '비율값']
CLNAQ00100_OUT_BLOCK_3_CODE = ['RecCnt']
CLNAQ00100_OUT_BLOCK_3_NAME = ['레코드갯수']

# COSAQ00102
COSAQ00102_IN_BLOCK_CODE = [
           'RecCnt', 'BkseqTpCode', 'OrdMktCode', 'AcntNo', 'Pwd', 'BnsTpCode', 'IsuNo', 'SrtOrdNo', 'OrdDt', 'ExecYn',
           'CrcyCode', 'ThdayBnsAppYn', 'LoanBalHldYn']
COSAQ00102_IN_BLOCK_NAME = [
           '레코드갯수', '역순구분코드', '주문시장코드', '계좌번호', '비밀번호', '매매구분코드', '종목번호', '시작주문번호', '주문일자', '체결여부',
           '통화코드', '당일매매적용여부', '대출잔고보유여부']
COSAQ00102_OUT_BLOCK_1_CODE = [
           'RecCnt', 'BkseqTpCode', 'OrdMktCode', 'AcntNo', 'Pwd', 'BnsTpCode', 'IsuNo', 'SrtOrdNo', 'OrdDt', 'ExecYn',
           'CrcyCode', 'ThdayBnsAppYn', 'LoanBalHldYn']
COSAQ00102_OUT_BLOCK_1_NAME = [
           '레코드갯수', '역순구분코드', '주문시장코드', '계좌번호', '비밀번호', '매매구분코드', '종목번호', '시작주문번호', '주문일자', '체결여부',
           '통화코드', '당일매매적용여부', '대출잔고보유여부']
COSAQ00102_OUT_BLOCK_2_CODE = [
           'RecCnt', 'JpnMktHanglIsuNm', 'MgmtBrnNm', 'SellExecFcurrAmt', 'SellExecQty', 'BuyExecFcurrAmt', 'BuyExecQty']
COSAQ00102_OUT_BLOCK_2_NAME = [
           '레코드갯수', '일본시장한글종목명', '관리지점명', '매도체결외화금액', '매도체결수량', '매수체결외화금액', '매수체결수량']
COSAQ00102_OUT_BLOCK_3_CODE = [
           'MgmtBrnNo', 'AcntNo', 'AcntNm', 'ExecTime', 'OrdTime', 'OrdNo', 'OrgOrdNo', 'ShtnIsuNo', 'OrdTrxPtnNm', 'OrdTrxPtnCode',
           'MrcAbleQty', 'OrdQty', 'OvrsOrdPrc', 'ExecQty', 'OvrsExecPrc', 'OrdprcPtnCode', 'OrdprcPtnNm', 'OrdPtnNm', 'OrdPtnCode', 'MrcTpCode',
           'MrcTpNm', 'AllExecQty', 'CommdaCode', 'OrdMktCode', 'MktNm', 'CommdaNm', 'JpnMktHanglIsuNm', 'UnercQty', 'CnfQty', 'CrcyCode',
           'RegMktCode', 'IsuNo', 'BrkTpCode', 'OppBrkNm', 'BnsTpCode', 'LoanDt', 'LoanAmt']
COSAQ00102_OUT_BLOCK_3_NAME = [
           '관리지점번호', '계좌번호', '계좌명', '체결시각', '주문시각', '주문번호', '원주문번호', '단축종목번호', '주문처리유형명', '주문처리유형코드',
           '정정취소가능수량', '주문수량', '해외주문가', '체결수량', '해외체결가', '호가유형코드', '호가유형명', '주문유형명', '주문유형코드', '정정취소구분코드',
           '정정취소구분명', '전체체결수량', '통신매체코드', '주문시장코드', '시장명', '통신매체명', '일본시장한글종목명', '미체결수량', '확인수량', '통화코드',
           '등록시장코드', '종목번호', '중개인구분코드', '상대중개인명', '매매구분코드', '대출일자', '대출금액']

# COSAQ01400
COSAQ01400_IN_BLOCK_CODE = [
           'RecCnt', 'CntryCode', 'AcntNo', 'Pwd', 'SrtDt', 'EndDt', 'BnsTpCode', 'RsvOrdCndiCode', 'RsvOrdStatCode']
COSAQ01400_IN_BLOCK_NAME = [
           '레코드갯수', '국가코드', '계좌번호', '비밀번호', '시작일자', '종료일자', '매매구분코드', '예약주문조건코드', '예약주문상태코드']
COSAQ01400_OUT_BLOCK_1_CODE = [
           'RecCnt', 'CntryCode', 'AcntNo', 'Pwd', 'SrtDt', 'EndDt', 'BnsTpCode', 'RsvOrdCndiCode', 'RsvOrdStatCode']
COSAQ01400_OUT_BLOCK_1_NAME = [
           '레코드갯수', '국가코드', '계좌번호', '비밀번호', '시작일자', '종료일자', '매매구분코드', '예약주문조건코드', '예약주문상태코드']
COSAQ01400_OUT_BLOCK_2_CODE = [
           'AcntNo', 'AcntNm', 'OrdDt', 'OrdNo', 'RsvOrdInptDt', 'RsvOrdNo', 'ShtnIsuNo', 'JpnMktHanglIsuNm', 'OrdQty', 'OvrsOrdPrc',
           'BnsTpNm', 'ExecQty', 'UnercQty', 'TotExecQty', 'CrcyCode', 'RsvOrdStatCode', 'MktTpNm', 'ErrCnts', 'OrdprcPtnNm', 'LoanDt',
           'MgntrnCode']
COSAQ01400_OUT_BLOCK_2_NAME = [
           '계좌번호', '계좌명', '주문일자', '주문번호', '예약주문입력일자', '예약주문번호', '단축종목번호', '일본시장한글종목명', '주문수량', '해외주문가',
           '매매구분명', '체결수량', '미체결수량', '총체결수량', '통화코드', '예약주문상태코드', '시장구분명', '오류내용', '호가유형명', '대출일자',
           '신용거래코드']

# COSAT00301
COSAT00301_IN_BLOCK_CODE = [
           'RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'OrdMktCode', 'IsuNo', 'OrdQty', 'OvrsOrdPrc', 'OrdprcPtnCode', 'BrkTpCode']
COSAT00301_IN_BLOCK_NAME = [
           '레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '주문시장코드', '종목번호', '주문수량', '해외주문가', '호가유형코드', '중개인구분코드']
COSAT00301_OUT_BLOCK_1_CODE = [
           'RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'OrdMktCode', 'IsuNo', 'OrdQty', 'OvrsOrdPrc', 'OrdprcPtnCode', 'RegCommdaCode',
           'BrkTpCode']
COSAT00301_OUT_BLOCK_1_NAME = [
           '레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '주문시장코드', '종목번호', '주문수량', '해외주문가', '호가유형코드', '등록통신매체코드',
           '중개인구분코드']
COSAT00301_OUT_BLOCK_2_CODE = ['RecCnt', 'AcntNm', 'IsuNm']
COSAT00301_OUT_BLOCK_2_NAME = ['레코드갯수', '계좌명', '종목명']

# COSAT00311
COSAT00311_IN_BLOCK_CODE = [
           'RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'OrdMktCode', 'IsuNo', 'OrdQty', 'OvrsOrdPrc', 'OrdprcPtnCode', 'BrkTpCode']
COSAT00311_IN_BLOCK_NAME = [
           '레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '주문시장코드', '종목번호', '주문수량', '해외주문가', '호가유형코드', '중개인구분코드']
COSAT00311_OUT_BLOCK_1_CODE = [
           'RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'OrdMktCode', 'IsuNo', 'OrdQty', 'OvrsOrdPrc', 'OrdprcPtnCode', 'RegCommdaCode',
           'BrkTpCode']
COSAT00311_OUT_BLOCK_1_NAME = [
           '레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '주문시장코드', '종목번호', '주문수량', '해외주문가', '호가유형코드', '등록통신매체코드',
           '중개인구분코드']
COSAT00311_OUT_BLOCK_2_CODE = ['RecCnt', 'AcntNm', 'IsuNm']
COSAT00311_OUT_BLOCK_2_NAME = ['레코드갯수', '계좌명', '종목명']

# COSAT00400
COSAT00400_IN_BLOCK_CODE = [
           'RecCnt', 'CntryCode', 'RsvOrdInptDt', 'RsvOrdNo', 'BnsTpCode', 'AcntNo', 'Pwd', 'FcurrMktCode', 'IsuNo', 'OrdQty',
           'OvrsOrdPrc', 'OrdprcPtnCode', 'RsvOrdSrtDt', 'RsvOrdEndDt', 'RsvOrdCndiCode', 'MgntrnCode', 'LoanDt', 'LoanDtlClssCode']
COSAT00400_IN_BLOCK_NAME = [
           '레코드갯수', '국가코드', '예약주문입력일자', '예약주문번호', '매매구분코드', '계좌번호', '비밀번호', '외화시장코드', '종목번호', '주문수량',
           '해외주문가', '호가유형코드', '예약주문시작일자', '예약주문종료일자', '예약주문조건코드', '신용거래코드', '대출일자', '대출상세분류코드']
COSAT00400_OUT_BLOCK_1_CODE = [
           'RecCnt', 'CntryCode', 'RsvOrdInptDt', 'RsvOrdNo', 'BnsTpCode', 'AcntNo', 'Pwd', 'FcurrMktCode', 'IsuNo', 'OrdQty',
           'OvrsOrdPrc', 'RegCommdaCode', 'OrdprcPtnCode', 'RsvOrdSrtDt', 'RsvOrdEndDt', 'RsvOrdCndiCode', 'MgntrnCode', 'LoanDt', 'LoanDtlClssCode']
COSAT00400_OUT_BLOCK_1_NAME = [
           '레코드갯수', '국가코드', '예약주문입력일자', '예약주문번호', '매매구분코드', '계좌번호', '비밀번호', '외화시장코드', '종목번호', '주문수량',
           '해외주문가', '등록통신매체코드', '호가유형코드', '예약주문시작일자', '예약주문종료일자', '예약주문조건코드', '신용거래코드', '대출일자', '대출상세분류코드']
COSAT00400_OUT_BLOCK_2_CODE = ['RecCnt']
COSAT00400_OUT_BLOCK_2_NAME = ['레코드갯수']

# COSMT00300
COSMT00300_IN_BLOCK_CODE = [
           'RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'OrdMktCode', 'IsuNo', 'OrdQty', 'OvrsOrdPrc', 'OrdprcPtnCode', 'BrkTpCode',
           'MgntrnCode', 'LoanDt', 'LoanDtlClssCode']
COSMT00300_IN_BLOCK_NAME = [
           '레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '주문시장코드', '종목번호', '주문수량', '해외주문가', '호가유형코드', '중개인구분코드',
           '신용거래코드', '대출일자', '대출상세분류코드']
COSMT00300_OUT_BLOCK_1_CODE = [
           'RecCnt', 'OrgOrdNo', 'AcntNo', 'InptPwd', 'OrdMktCode', 'IsuNo', 'OrdQty', 'OvrsOrdPrc', 'OrdprcPtnCode', 'RegCommdaCode',
           'BrkTpCode', 'MgntrnCode', 'LoanDt', 'LoanDtlClssCode']
COSMT00300_OUT_BLOCK_1_NAME = [
           '레코드갯수', '원주문번호', '계좌번호', '입력비밀번호', '주문시장코드', '종목번호', '주문수량', '해외주문가', '호가유형코드', '등록통신매체코드',
           '중개인구분코드', '신용거래코드', '대출일자', '대출상세분류코드']
COSMT00300_OUT_BLOCK_2_CODE = ['RecCnt', 'AcntNm', 'IsuNm']
COSMT00300_OUT_BLOCK_2_NAME = ['레코드갯수', '계좌명', '종목명']

# COSOQ00201
COSOQ00201_IN_BLOCK_CODE = ['RecCnt', 'Pwd', 'BaseDt', 'CrcyCode', 'AstkBalTpCode']
COSOQ00201_IN_BLOCK_NAME = ['레코드갯수', '비밀번호', '기준일자', '통화코드', '해외증권잔고구분코드']
COSOQ00201_OUT_BLOCK_1_CODE = ['RecCnt', 'Pwd', 'BaseDt', 'CrcyCode', 'AstkBalTpCode']
COSOQ00201_OUT_BLOCK_1_NAME = ['레코드갯수', '비밀번호', '기준일자', '통화코드', '해외증권잔고구분코드']
COSOQ00201_OUT_BLOCK_2_CODE = [
           'RecCnt', 'DpsConvEvalAmt', 'StkConvEvalAmt', 'DpsastConvEvalAmt', 'WonEvalSumAmt', 'ConvEvalPnlAmt', 'WonDpsBalAmt', 'D2EstiDps', 'LoanAmt']
COSOQ00201_OUT_BLOCK_2_NAME = [
           '레코드갯수', '예수금환산평가금액', '주식환산평가금액', '예탁자산환산평가금액', '원화평가합계금액', '환산평가손익금액', '원화예수금잔고금액', 'D2추정예수금', '대출금액']
COSOQ00201_OUT_BLOCK_3_CODE = [
           'CrcyCode', 'FcurrDps', 'FcurrEvalAmt', 'FcurrEvalPnlAmt', 'PnlRat', 'BaseXchrat', 'DpsConvEvalAmt', 'PchsAmt', 'StkConvEvalAmt', 'ConvEvalPnlAmt',
           'FcurrBuyAmt', 'FcurrOrdAbleAmt', 'LoanAmt']
COSOQ00201_OUT_BLOCK_3_NAME = [
           '통화코드', '외화예수금', '외화평가금액', '외화평가손익금액', '손익율', '기준환율', '예수금환산평가금액', '매입금액', '주식환산평가금액', '환산평가손익금액',
           '외화매수금액', '외화주문가능금액', '대출금액']
COSOQ00201_OUT_BLOCK_4_CODE = [
           'CrcyCode', 'ShtnIsuNo', 'IsuNo', 'JpnMktHanglIsuNm', 'AstkBalTpCode', 'AstkBalTpCodeNm', 'AstkBalQty', 'AstkSellAbleQty', 'FcstckUprc', 'FcurrBuyAmt',
           'FcstckMktIsuCode', 'OvrsScrtsCurpri', 'FcurrEvalAmt', 'FcurrEvalPnlAmt', 'PnlRat', 'BaseXchrat', 'PchsAmt', 'DpsConvEvalAmt', 'StkConvEvalAmt', 'ConvEvalPnlAmt',
           'AstkSettQty', 'MktTpNm', 'FcurrMktCode', 'LoanDt', 'LoanDtlClssCode', 'LoanAmt', 'DueDt', 'AstkBasePrc']
COSOQ00201_OUT_BLOCK_4_NAME = [
           '통화코드', '단축종목번호', '종목번호', '일본시장한글종목명', '해외증권잔고구분코드', '해외증권잔고구분코드명', '해외증권잔고수량', '해외증권매도가능수량', '외화증권단가', '외화매수금액',
           '외화증권시장종목코드', '해외증권시세', '외화평가금액', '외화평가손익금액', '손익율', '기준환율', '매입금액', '예수금환산평가금액', '주식환산평가금액', '환산평가손익금액',
           '해외증권결제수량', '시장구분명', '외화시장코드', '대출일자', '대출상세분류코드', '대출금액', '만기일자', '해외증권기준가격']

# COSOQ02701
COSOQ02701_IN_BLOCK_CODE = ['RecCnt', 'Pwd', 'CrcyCode']
COSOQ02701_IN_BLOCK_NAME = ['레코드갯수', '비밀번호', '통화코드']
COSOQ02701_OUT_BLOCK_1_CODE = ['RecCnt', 'Pwd', 'CrcyCode']
COSOQ02701_OUT_BLOCK_1_NAME = ['레코드갯수', '비밀번호', '통화코드']
COSOQ02701_OUT_BLOCK_2_CODE = [
           'CrcyCode', 'FcurrBuyAdjstAmt1', 'FcurrBuyAdjstAmt2', 'FcurrBuyAdjstAmt3', 'FcurrBuyAdjstAmt4', 'FcurrSellAdjstAmt1', 'FcurrSellAdjstAmt2', 'FcurrSellAdjstAmt3', 'FcurrSellAdjstAmt4', 'PrsmptFcurrDps1',
           'PrsmptFcurrDps2', 'PrsmptFcurrDps3', 'PrsmptFcurrDps4', 'PrsmptMxchgAbleAmt1', 'PrsmptMxchgAbleAmt2', 'PrsmptMxchgAbleAmt3', 'PrsmptMxchgAbleAmt4']
COSOQ02701_OUT_BLOCK_2_NAME = [
           '통화코드', '외화매수정산금1', '외화매수정산금2', '외화매수정산금3', '외화매수정산금4', '외화매도정산금1', '외화매도정산금2', '외화매도정산금3', '외화매도정산금4', '추정외화예수금1',
           '추정외화예수금2', '추정외화예수금3', '추정외화예수금4', '추정환전가능금1', '추정환전가능금2', '추정환전가능금3', '추정환전가능금4']
COSOQ02701_OUT_BLOCK_3_CODE = [
           'CntryNm', 'CrcyCode', 'T4FcurrDps', 'FcurrDps', 'FcurrOrdAbleAmt', 'PrexchOrdAbleAmt', 'FcurrOrdAmt', 'FcurrPldgAmt', 'ExecRuseFcurrAmt', 'FcurrMxchgAbleAmt',
           'BaseXchrat']
COSOQ02701_OUT_BLOCK_3_NAME = [
           '국가명', '통화코드', 'T4외화예수금', '외화예수금', '외화주문가능금액', '가환전주문가능금액', '외화주문금액', '외화담보금액', '체결재사용외화금액', '외화환전가능금',
           '기준환율']
COSOQ02701_OUT_BLOCK_4_CODE = ['RecCnt', 'MnyoutAbleAmt', 'WonPrexchAbleAmt', 'OvrsMgn']
COSOQ02701_OUT_BLOCK_4_NAME = ['레코드갯수', '출금가능금액', '원화가환전가능금액', '해외증거금']
COSOQ02701_OUT_BLOCK_5_CODE = ['RecCnt']
COSOQ02701_OUT_BLOCK_5_NAME = ['레코드갯수']

# CSPAQ00600
CSPAQ00600_IN_BLOCK_CODE = [
           'RecCnt', 'InptPwd', 'LoanDtlClssCode', 'IsuNo', 'OrdPrc', 'CommdaCode']
CSPAQ00600_IN_BLOCK_NAME = [
           '레코드갯수', '입력비밀번호', '대출상세분류코드', '종목번호', '주문가', '통신매체코드']
CSPAQ00600_OUT_BLOCK_1_CODE = [
           'RecCnt', 'InptPwd', 'LoanDtlClssCode', 'IsuNo', 'OrdPrc', 'CommdaCode']
CSPAQ00600_OUT_BLOCK_1_NAME = [
           '레코드갯수', '입력비밀번호', '대출상세분류코드', '종목번호', '주문가', '통신매체코드']
CSPAQ00600_OUT_BLOCK_2_CODE = [
           'RecCnt', 'OrdPrc', 'SloanLmtAmt', 'SloanAmtSum', 'SloanNewAmt', 'SloanRfundAmt', 'MktcplMloanLmtAmt', 'MktcplMloanAmtSum', 'MktcplMloanNewAmt', 'MktcplMloanRfundAmt',
           'SfaccMloanLmtAmt', 'SfaccMloanAmtSum', 'SfaccMloanNewAmt', 'SfaccMloanRfundAmt', 'BrnMktcplMloanLmtAmt', 'BrnMktcplMloanNewAmt', 'BrnMktcplMloanRfundAmt', 'BrnMktcplMloanUseAmt', 'BrnSfaccMloanLmtAmt', 'BrnSfaccMloanNewAmt',
           'BrnSfaccMloanRfundAmt', 'BrnSfaccMloanUseAmt', 'FirmMloanLmtMgmtYn', 'FirmCrdtIsuRestrcTp', 'PldgMaintRat', 'FirmNm', 'PldgRat', 'DpsastSum', 'LmtChgAbleAmt', 'OrdAbleAmt',
           'OrdAbleQty', 'RcvblUablOrdAbleQty']
CSPAQ00600_OUT_BLOCK_2_NAME = [
           '레코드갯수', '주문가', '대주한도', '대주금액합계', '대주신규금액', '대주상환금액', '유통융자한도금액', '유통융자금액합계', '유통융자신규금액', '유통융자상환금액',
           '자기융자한도금액', '자기융자금액합계', '자기융자신규금액', '자기융자상환금액', '지점유통융자한도금액', '지점유통융자신규금액', '지점유통융자상환금액', '지점유통융자사용금액', '지점자기융자한도금액', '지점자기융자신규금액',
           '지점자기융자상환금액', '지점자기융자사용금액', '이용사융자한도관리여부', '이용사신용종목제한구분', '담보유지비율', '이용사명', '담보비율', '예탁자산합계', '한도변경가능금액', '주문가능금액',
           '주문가능수량', '미수불가주문가능수량']

# CSPAQ12200
CSPAQ12200_IN_BLOCK_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'BalCreTp']
CSPAQ12200_IN_BLOCK_NAME = ['레코드갯수', '계좌번호', '비밀번호', '잔고생성구분']
CSPAQ12200_OUT_BLOCK_1_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'BalCreTp']
CSPAQ12200_OUT_BLOCK_1_NAME = ['레코드갯수', '계좌번호', '비밀번호', '잔고생성구분']
CSPAQ12200_OUT_BLOCK_2_CODE = [
           'RecCnt', 'AcntNm', 'MnyOrdAbleAmt', 'MnyoutAbleAmt', 'SeOrdAbleAmt', 'KdqOrdAbleAmt', 'BalEvalAmt', 'RcvblAmt', 'DpsastTotamt', 'PnlRat',
           'InvstOrgAmt', 'InvstPlAmt', 'CrdtPldgOrdAmt', 'Dps', 'SubstAmt', 'D1Dps', 'D2Dps', 'MnyrclAmt', 'MgnMny', 'MgnSubst',
           'ChckAmt', 'SubstOrdAbleAmt', 'MgnRat100pctOrdAbleAmt', 'MgnRat35ordAbleAmt', 'MgnRat50ordAbleAmt', 'PrdaySellAdjstAmt', 'PrdayBuyAdjstAmt', 'CrdaySellAdjstAmt', 'CrdayBuyAdjstAmt', 'D1ovdRepayRqrdAmt',
           'D2ovdRepayRqrdAmt', 'D1PrsmptWthdwAbleAmt', 'D2PrsmptWthdwAbleAmt', 'DpspdgLoanAmt', 'Imreq', 'MloanAmt', 'ChgAfPldgRat', 'OrgPldgAmt', 'SubPldgAmt', 'RqrdPldgAmt',
           'OrgPdlckAmt', 'PdlckAmt', 'AddPldgMny', 'D1OrdAbleAmt', 'CrdtIntdltAmt', 'EtclndAmt', 'NtdayPrsmptCvrgAmt', 'OrgPldgSumAmt', 'CrdtOrdAbleAmt', 'SubPldgSumAmt',
           'CrdtPldgAmtMny', 'CrdtPldgSubstAmt', 'AddCrdtPldgMny', 'CrdtPldgRuseAmt', 'AddCrdtPldgSubst', 'CslLoanAmtdt1', 'DpslRestrcAmt']
CSPAQ12200_OUT_BLOCK_2_NAME = [
           '레코드갯수', '계좌명', '현금주문가능금액', '출금가능금액', '거래소금액', '코스닥금액', '잔고평가금액', '미수금액', '예탁자산총액', '손익율',
           '투자원금', '투자손익금액', '신용담보주문금액', '예수금', '대용금액', 'D1예수금', 'D2예수금', '현금미수금액', '증거금현금', '증거금대용',
           '수표금액', '대용주문가능금액', '증거금률100퍼센트주문가능금액', '증거금률35%주문가능금액', '증거금률50%주문가능금액', '전일매도정산금액', '전일매수정산금액', '금일매도정산금액', '금일매수정산금액', 'D1연체변제소요금액',
           'D2연체변제소요금액', 'D1추정인출가능금액', 'D2추정인출가능금액', '예탁담보대출금액', '신용설정보증금', '융자금액', '변경후담보비율', '원담보금액', '부담보금액', '소요담보금액',
           '원담보부족금액', '담보부족금액', '추가담보현금', 'D1주문가능금액', '신용이자미납금액', '기타대여금액', '익일추정반대매매금액', '원담보합계금액', '신용주문가능금액', '부담보합계금액',
           '신용담보금현금', '신용담보대용금액', '추가신용담보현금', '신용담보재사용금액', '추가신용담보대용', '매도대금담보대출금액', '처분제한금액']

# CSPAQ12300
CSPAQ12300_IN_BLOCK_CODE = [
           'RecCnt', 'Pwd', 'BalCreTp', 'CmsnAppTpCode', 'D2balBaseQryTp', 'UprcTpCode']
CSPAQ12300_IN_BLOCK_NAME = [
           '레코드갯수', '비밀번호', '잔고생성구분', '수수료적용구분', 'D2잔고기준조회구분', '단가구분']
CSPAQ12300_OUT_BLOCK_1_CODE = [
           'RecCnt', 'Pwd', 'BalCreTp', 'CmsnAppTpCode', 'D2balBaseQryTp', 'UprcTpCode']
CSPAQ12300_OUT_BLOCK_1_NAME = [
           '레코드갯수', '비밀번호', '잔고생성구분', '수수료적용구분', 'D2잔고기준조회구분', '단가구분']
CSPAQ12300_OUT_BLOCK_2_CODE = [
           'RecCnt', 'AcntNm', 'MnyOrdAbleAmt', 'MnyoutAbleAmt', 'SeOrdAbleAmt', 'KdqOrdAbleAmt', 'HtsOrdAbleAmt', 'MgnRat100pctOrdAbleAmt', 'BalEvalAmt', 'PchsAmt',
           'RcvblAmt', 'PnlRat', 'InvstOrgAmt', 'InvstPlAmt', 'CrdtPldgOrdAmt', 'Dps', 'D1Dps', 'D2Dps', 'OrdDt', 'MnyMgn',
           'SubstMgn', 'SubstAmt', 'PrdayBuyExecAmt', 'PrdaySellExecAmt', 'CrdayBuyExecAmt', 'CrdaySellExecAmt', 'EvalPnlSum', 'DpsastTotamt', 'Evrprc', 'RuseAmt',
           'EtclndAmt', 'PrcAdjstAmt', 'D1CmsnAmt', 'D2CmsnAmt', 'D1EvrTax', 'D2EvrTax', 'D1SettPrergAmt', 'D2SettPrergAmt', 'PrdayKseMnyMgn', 'PrdayKseSubstMgn',
           'PrdayKseCrdtMnyMgn', 'PrdayKseCrdtSubstMgn', 'CrdayKseMnyMgn', 'CrdayKseSubstMgn', 'CrdayKseCrdtMnyMgn', 'CrdayKseCrdtSubstMgn', 'PrdayKdqMnyMgn', 'PrdayKdqSubstMgn', 'PrdayKdqCrdtMnyMgn', 'PrdayKdqCrdtSubstMgn',
           'CrdayKdqMnyMgn', 'CrdayKdqSubstMgn', 'CrdayKdqCrdtMnyMgn', 'CrdayKdqCrdtSubstMgn', 'PrdayFrbrdMnyMgn', 'PrdayFrbrdSubstMgn', 'CrdayFrbrdMnyMgn', 'CrdayFrbrdSubstMgn', 'PrdayCrbmkMnyMgn', 'PrdayCrbmkSubstMgn',
           'CrdayCrbmkMnyMgn', 'CrdayCrbmkSubstMgn', 'DpspdgQty', 'BuyAdjstAmtD2', 'SellAdjstAmtD2', 'RepayRqrdAmtD1', 'RepayRqrdAmtD2', 'LoanAmt']
CSPAQ12300_OUT_BLOCK_2_NAME = [
           '레코드갯수', '계좌명', '현금주문가능금액', '출금가능금액', '거래소금액', '코스닥금액', 'HTS주문가능금액', '증거금률100퍼센트주문가능금액', '잔고평가금액', '매입금액',
           '미수금액', '손익율', '투자원금', '투자손익금액', '신용담보주문금액', '예수금', 'D1예수금', 'D2예수금', '주문일', '현금증거금액',
           '대용증거금액', '대용금액', '전일매수체결금액', '전일매도체결금액', '금일매수체결금액', '금일매도체결금액', '평가손익합계', '예탁자산총액', '제비용', '재사용금액',
           '기타대여금액', '가정산금액', 'D1수수료', 'D2수수료', 'D1제세금', 'D2제세금', 'D1결제예정금액', 'D2결제예정금액', '전일KSE현금증거금', '전일KSE대용증거금',
           '전일KSE신용현금증거금', '전일KSE신용대용증거금', '금일KSE현금증거금', '금일KSE대용증거금', '금일KSE신용현금증거금', '금일KSE신용대용증거금', '전일코스닥현금증거금', '전일코스닥대용증거금', '전일코스닥신용현금증거금', '전일코스닥신용대용증거금',
           '금일코스닥현금증거금', '금일코스닥대용증거금', '금일코스닥신용현금증거금', '금일코스닥신용대용증거금', '전일프리보드현금증거금', '전일프리보드대용증거금', '금일프리보드현금증거금', '금일프리보드대용증거금', '전일장외현금증거금', '전일장외대용증거금',
           '금일장외현금증거금', '금일장외대용증거금', '예탁담보수량', '매수정산금(D+2)', '매도정산금(D+2)', '변제소요금(D+1)', '변제소요금(D+2)', '대출금액']
CSPAQ12300_OUT_BLOCK_3_CODE = [
           'IsuNo', 'IsuNm', 'SecBalPtnCode', 'SecBalPtnNm', 'BalQty', 'BnsBaseBalQty', 'CrdayBuyExecQty', 'CrdaySellExecQty', 'SellPrc', 'BuyPrc',
           'SellPnlAmt', 'PnlRat', 'NowPrc', 'CrdtAmt', 'DueDt', 'PrdaySellExecPrc', 'PrdaySellQty', 'PrdayBuyExecPrc', 'PrdayBuyQty', 'LoanDt',
           'AvrUprc', 'SellAbleQty', 'SellOrdQty', 'CrdayBuyExecAmt', 'CrdaySellExecAmt', 'PrdayBuyExecAmt', 'PrdaySellExecAmt', 'BalEvalAmt', 'EvalPnl', 'MnyOrdAbleAmt',
           'OrdAbleAmt', 'SellUnercQty', 'SellUnsttQty', 'BuyUnercQty', 'BuyUnsttQty', 'UnsttQty', 'UnercQty', 'PrdayCprc', 'PchsAmt', 'RegMktCode',
           'LoanDtlClssCode', 'DpspdgLoanQty']
CSPAQ12300_OUT_BLOCK_3_NAME = [
           '종목번호', '종목명', '유가증권잔고유형코드', '유가증권잔고유형명', '잔고수량', '매매기준잔고수량', '금일매수체결수량', '금일매도체결수량', '매도가', '매수가',
           '매도손익금액', '손익율', '현재가', '신용금액', '만기일', '전일매도체결가', '전일매도수량', '전일매수체결가', '전일매수수량', '대출일',
           '평균단가', '매도가능수량', '매도주문수량', '금일매수체결금액', '금일매도체결금액', '전일매수체결금액', '전일매도체결금액', '잔고평가금액', '평가손익', '현금주문가능금액',
           '주문가능금액', '매도미체결수량', '매도미결제수량', '매수미체결수량', '매수미결제수량', '미결제수량', '미체결수량', '전일종가', '매입금액', '등록시장코드',
           '대출상세분류코드', '예탁담보대출수량']

# CSPAQ13700
CSPAQ13700_IN_BLOCK_CODE = [
           'RecCnt', 'InptPwd', 'OrdMktCode', 'BnsTpCode', 'IsuNo', 'ExecYn', 'OrdDt', 'SrtOrdNo2', 'BkseqTpCode', 'OrdPtnCode']
CSPAQ13700_IN_BLOCK_NAME = [
           '레코드갯수', '입력비밀번호', '주문시장코드', '매매구분', '종목번호', '체결여부', '주문일', '시작주문번호2', '역순구분', '주문유형코드']
CSPAQ13700_OUT_BLOCK_1_CODE = [
           'RecCnt', 'InptPwd', 'OrdMktCode', 'BnsTpCode', 'IsuNo', 'ExecYn', 'OrdDt', 'SrtOrdNo2', 'BkseqTpCode', 'OrdPtnCode']
CSPAQ13700_OUT_BLOCK_1_NAME = [
           '레코드갯수', '입력비밀번호', '주문시장코드', '매매구분', '종목번호', '체결여부', '주문일', '시작주문번호2', '역순구분', '주문유형코드']
CSPAQ13700_OUT_BLOCK_2_CODE = [
           'RecCnt', 'BuyExecAmt', 'SellExecQty', 'BuyExecQty', 'SellOrdQty', 'BuyOrdQty']
CSPAQ13700_OUT_BLOCK_2_NAME = [
           '레코드갯수', '매수체결금액', '매도체결수량', '매수체결수량', '매도주문수량', '매수주문수량']
CSPAQ13700_OUT_BLOCK_3_CODE = [
           'OrdDt', 'MgmtBrnNo', 'OrdMktCode', 'OrdNo', 'OrgOrdNo', 'IsuNo', 'IsuNm', 'BnsTpCode', 'BnsTpNm', 'OrdPtnCode',
           'OrdPtnNm', 'OrdTrxPtnCode', 'OrdTrxPtnNm', 'MrcTpCode', 'MrcTpNm', 'MrcQty', 'MrcAbleQty', 'OrdQty', 'OrdPrc', 'ExecQty',
           'ExecPrc', 'ExecTrxTime', 'LastExecTime', 'OrdprcPtnCode', 'OrdprcPtnNm', 'OrdCndiTpCode', 'AllExecQty', 'RegCommdaCode', 'CommdaNm', 'MbrNo',
           'RsvOrdYn', 'LoanDt', 'OrdTime', 'OpDrtnNo', 'OdrrId']
CSPAQ13700_OUT_BLOCK_3_NAME = [
           '주문일', '관리지점번호', '주문시장코드', '주문번호', '원주문번호', '종목번호', '종목명', '매매구분', '매매구분', '주문유형코드',
           '주문유형명', '주문처리유형코드', '주문처리유형명', '정정취소구분', '정정취소구분명', '정정취소수량', '정정취소가능수량', '주문수량', '주문가격', '체결수량',
           '체결가', '체결처리시각', '최종체결시각', '호가유형코드', '호가유형명', '주문조건구분', '전체체결수량', '통신매체코드', '통신매체명', '회원번호',
           '예약주문여부', '대출일', '주문시각', '운용지시번호', '주문자ID']

# CSPAQ22200
CSPAQ22200_IN_BLOCK_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'BalCreTp']
CSPAQ22200_IN_BLOCK_NAME = ['레코드갯수', '계좌번호', '비밀번호', '잔고생성구분']
CSPAQ22200_OUT_BLOCK_1_CODE = ['RecCnt', 'AcntNo', 'Pwd', 'BalCreTp']
CSPAQ22200_OUT_BLOCK_1_NAME = ['레코드갯수', '계좌번호', '비밀번호', '잔고생성구분']
CSPAQ22200_OUT_BLOCK_2_CODE = [
           'RecCnt', 'AcntNm', 'MnyOrdAbleAmt', 'SubstOrdAbleAmt', 'SeOrdAbleAmt', 'KdqOrdAbleAmt', 'CrdtPldgOrdAmt', 'MgnRat100pctOrdAbleAmt', 'MgnRat35ordAbleAmt', 'MgnRat50ordAbleAmt',
           'CrdtOrdAbleAmt', 'Dps', 'SubstAmt', 'MgnMny', 'MgnSubst', 'D1Dps', 'D2Dps', 'RcvblAmt', 'D1ovdRepayRqrdAmt', 'D2ovdRepayRqrdAmt',
           'MloanAmt', 'ChgAfPldgRat', 'RqrdPldgAmt', 'PdlckAmt', 'OrgPldgSumAmt', 'SubPldgSumAmt', 'CrdtPldgAmtMny', 'CrdtPldgSubstAmt', 'Imreq', 'CrdtPldgRuseAmt',
           'DpslRestrcAmt', 'PrdaySellAdjstAmt', 'PrdayBuyAdjstAmt', 'CrdaySellAdjstAmt', 'CrdayBuyAdjstAmt', 'CslLoanAmtdt1']
CSPAQ22200_OUT_BLOCK_2_NAME = [
           '레코드갯수', '계좌명', '현금주문가능금액', '대용주문가능금액', '거래소금액', '코스닥금액', '신용담보주문금액', '증거금률100퍼센트주문가능금액', '증거금률35%주문가능금액', '증거금률50%주문가능금액',
           '신용주문가능금액', '예수금', '대용금액', '증거금현금', '증거금대용', 'D1예수금', 'D2예수금', '미수금액', 'D1연체변제소요금액', 'D2연체변제소요금액',
           '융자금액', '변경후담보비율', '소요담보금액', '담보부족금액', '원담보합계금액', '부담보합계금액', '신용담보금현금', '신용담보대용금액', '신용설정보증금', '신용담보재사용금액',
           '처분제한금액', '전일매도정산금액', '전일매수정산금액', '금일매도정산금액', '금일매수정산금액', '매도대금담보대출금액']

# CSPAT00600
CSPAT00600_IN_BLOCK_CODE = [
           'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdPrc', 'BnsTpCode', 'OrdprcPtnCode', 'MgntrnCode', 'LoanDt', 'OrdCndiTpCode',
           'MbrNo']
CSPAT00600_IN_BLOCK_NAME = [
           '계좌번호', '입력비밀번호', '종목번호', '주문수량', '주문가', '매매구분', '호가유형코드', '신용거래코드', '대출일', '주문조건구분',
           '회원사번호']
CSPAT00600_OUT_BLOCK_1_CODE = [
           'RecCnt', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdPrc', 'BnsTpCode', 'OrdprcPtnCode', 'PrgmOrdprcPtnCode', 'StslAbleYn', 'StslOrdprcTpCode',
           'CommdaCode', 'MgntrnCode', 'LoanDt', 'MbrNo', 'OrdCndiTpCode', 'StrtgCode', 'GrpId', 'OrdSeqNo', 'PtflNo', 'BskNo',
           'TrchNo', 'ItemNo', 'OpDrtnNo', 'LpYn', 'CvrgTpCode']
CSPAT00600_OUT_BLOCK_1_NAME = [
           '레코드갯수', '입력비밀번호', '종목번호', '주문수량', '주문가', '매매구분', '호가유형코드', '프로그램호가유형코드', '공매도가능여부', '공매도호가구분',
           '통신매체코드', '신용거래코드', '대출일', '회원번호', '주문조건구분', '전략코드', '그룹ID', '주문회차', '포트폴리오번호', '바스켓번호',
           '트렌치번호', '아이템번호', '운용지시번호', '유동성공급자여부', '반대매매구분']
CSPAT00600_OUT_BLOCK_2_CODE = [
           'RecCnt', 'OrdTime', 'OrdMktCode', 'OrdPtnCode', 'ShtnIsuNo', 'MgempNo', 'OrdAmt', 'SpareOrdNo', 'CvrgSeqno', 'RsvOrdNo',
           'SpotOrdQty', 'RuseOrdQty', 'MnyOrdAmt', 'SubstOrdAmt', 'RuseOrdAmt', 'AcntNm', 'IsuNm']
CSPAT00600_OUT_BLOCK_2_NAME = [
           '레코드갯수', '주문시각', '주문시장코드', '주문유형코드', '단축종목번호', '관리사원번호', '주문금액', '예비주문번호', '반대매매일련번호', '예약주문번호',
           '실물주문수량', '재사용주문수량', '현금주문금액', '대용주문금액', '재사용주문금액', '계좌명', '종목명']

# CSPAT00700
CSPAT00700_IN_BLOCK_CODE = [
           'OrgOrdNo', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdprcPtnCode', 'OrdCndiTpCode', 'OrdPrc']
CSPAT00700_IN_BLOCK_NAME = [
           '원주문번호', '계좌번호', '입력비밀번호', '종목번호', '주문수량', '호가유형코드', '주문조건구분', '주문가']
CSPAT00700_OUT_BLOCK_1_CODE = [
           'RecCnt', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'OrdprcPtnCode', 'OrdCndiTpCode', 'OrdPrc', 'CommdaCode', 'StrtgCode',
           'GrpId', 'OrdSeqNo', 'PtflNo', 'BskNo', 'TrchNo', 'ItemNo']
CSPAT00700_OUT_BLOCK_1_NAME = [
           '레코드갯수', '계좌번호', '입력비밀번호', '종목번호', '주문수량', '호가유형코드', '주문조건구분', '주문가', '통신매체코드', '전략코드',
           '그룹ID', '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호']
CSPAT00700_OUT_BLOCK_2_CODE = [
           'RecCnt', 'PrntOrdNo', 'OrdTime', 'OrdMktCode', 'OrdPtnCode', 'ShtnIsuNo', 'PrgmOrdprcPtnCode', 'StslOrdprcTpCode', 'StslAbleYn', 'MgntrnCode',
           'LoanDt', 'CvrgOrdTp', 'LpYn', 'MgempNo', 'OrdAmt', 'BnsTpCode', 'SpareOrdNo', 'CvrgSeqno', 'RsvOrdNo', 'MnyOrdAmt',
           'SubstOrdAmt', 'RuseOrdAmt', 'AcntNm', 'IsuNm']
CSPAT00700_OUT_BLOCK_2_NAME = [
           '레코드갯수', '모주문번호', '주문시각', '주문시장코드', '주문유형코드', '단축종목번호', '프로그램호가유형코드', '공매도호가구분', '공매도가능여부', '신용거래코드',
           '대출일', '반대매매주문구분', '유동성공급자여부', '관리사원번호', '주문금액', '매매구분', '예비주문번호', '반대매매일련번호', '예약주문번호', '현금주문금액',
           '대용주문금액', '재사용주문금액', '계좌명', '종목명']

# CSPAT00800
CSPAT00800_IN_BLOCK_CODE = ['OrgOrdNo', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty']
CSPAT00800_IN_BLOCK_NAME = ['원주문번호', '계좌번호', '입력비밀번호', '종목번호', '주문수량']
CSPAT00800_OUT_BLOCK_1_CODE = [
           'RecCnt', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdQty', 'CommdaCode', 'GrpId', 'StrtgCode', 'OrdSeqNo', 'PtflNo',
           'BskNo', 'TrchNo', 'ItemNo']
CSPAT00800_OUT_BLOCK_1_NAME = [
           '레코드갯수', '계좌번호', '입력비밀번호', '종목번호', '주문수량', '통신매체코드', '그룹ID', '전략코드', '주문회차', '포트폴리오번호',
           '바스켓번호', '트렌치번호', '아이템번호']
CSPAT00800_OUT_BLOCK_2_CODE = [
           'RecCnt', 'PrntOrdNo', 'OrdTime', 'OrdMktCode', 'OrdPtnCode', 'ShtnIsuNo', 'PrgmOrdprcPtnCode', 'StslOrdprcTpCode', 'StslAbleYn', 'MgntrnCode',
           'LoanDt', 'CvrgOrdTp', 'LpYn', 'MgempNo', 'BnsTpCode', 'SpareOrdNo', 'CvrgSeqno', 'RsvOrdNo', 'AcntNm', 'IsuNm']
CSPAT00800_OUT_BLOCK_2_NAME = [
           '레코드갯수', '모주문번호', '주문시각', '주문시장코드', '주문유형코드', '단축종목번호', '프로그램호가유형코드', '공매도호가구분', '공매도가능여부', '신용거래코드',
           '대출일', '반대매매주문구분', '유동성공급자여부', '관리사원번호', '매매구분', '예비주문번호', '반대매매일련번호', '예약주문번호', '계좌명', '종목명']

# CSPBQ00200
CSPBQ00200_IN_BLOCK_CODE = [
           'RecCnt', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdPrc', 'RegCommdaCode']
CSPBQ00200_IN_BLOCK_NAME = [
           '레코드갯수', '계좌번호', '입력비밀번호', '종목번호', '주문가격', '통신매체코드']
CSPBQ00200_OUT_BLOCK_1_CODE = [
           'RecCnt', 'AcntNo', 'InptPwd', 'IsuNo', 'OrdPrc', 'RegCommdaCode']
CSPBQ00200_OUT_BLOCK_1_NAME = [
           '레코드갯수', '계좌번호', '입력비밀번호', '종목번호', '주문가격', '통신매체코드']
CSPBQ00200_OUT_BLOCK_2_CODE = [
           'RecCnt', 'IsuNm', 'Dps', 'SubstAmt', 'CrdtPldgRuseAmt', 'MnyOrdAbleAmt', 'SubstOrdAbleAmt', 'MnyMgn', 'SubstMgn', 'SeOrdAbleAmt',
           'KdqOrdAbleAmt', 'PrsmptDpsD1', 'PrsmptDpsD2', 'MnyoutAbleAmt', 'RcvblAmt', 'CmsnRat', 'AddLevyAmt', 'RuseObjAmt', 'MnyRuseObjAmt', 'FirmMgnRat',
           'SubstRuseObjAmt', 'IsuMgnRat', 'AcntMgnRat', 'TrdMgnrt', 'Cmsn', 'MgnRat20pctOrdAbleAmt', 'MgnRat20OrdAbleQty', 'MgnRat30pctOrdAbleAmt', 'MgnRat30OrdAbleQty', 'MgnRat40pctOrdAbleAmt',
           'MgnRat40OrdAbleQty', 'MgnRat100pctOrdAbleAmt', 'MgnRat100OrdAbleQty', 'MgnRat100MnyOrdAbleAmt', 'MgnRat100MnyOrdAbleQty', 'MgnRat20pctRuseAbleAmt', 'MgnRat30pctRuseAbleAmt', 'MgnRat40pctRuseAbleAmt', 'MgnRat100pctRuseAbleAmt', 'OrdAbleQty',
           'OrdAbleAmt']
CSPBQ00200_OUT_BLOCK_2_NAME = [
           '레코드갯수', '종목명', '예수금', '대용금액', '신용담보재사용금액', '현금주문가능금액', '대용주문가능금액', '현금증거금액', '대용증거금액', '거래소금액',
           '코스닥금액', '추정예수금(D+1)', '추정예수금(D+2)', '출금가능금액', '미수금액', '수수료율', '추가징수금액', '재사용대상금액', '현금재사용대상금액', '이용사증거금률',
           '대용재사용대상금액', '종목증거금률', '계좌증거금률', '거래증거금률', '수수료', '증거금률20퍼센트주문가능금액', '증거금률100퍼센트현금주문가능수량?', '증거금률30퍼센트주문가능금액', '증거금률30퍼센트주문가능수량??', '증거금률40퍼센트주문가능금액',
           '증거금률40퍼센트주문가능수량??', '증거금률100퍼센트주문가능금액', '증거금률100퍼센트주문가능수량??', '증거금률100퍼센트현금주문가능금액?', '증거금률100퍼센트현금주문가능수량', '증거금률20퍼센트재사용가능금액', '증거금률30퍼센트재사용가능금액', '증거금률40퍼센트재사용가능금액', '증거금률100퍼센트재사용가능금액', '주문가능수량',
           '주문가능금액']

# CUR
CUR_IN_BLOCK_CODE = ['base_id']
CUR_IN_BLOCK_NAME = ['기초자산ID']
CUR_OUT_BLOCK_CODE = [
           'time', 'offer', 'bid', 'open', 'high', 'low', 'price', 'sign', 'change', 'drate',
           'ctime', 'base_id']
CUR_OUT_BLOCK_NAME = [
           '전송시간', '매도호가', '매수호가', '시가', '고가', '저가', '체결가', '전일대비구분', '전일대비', '등락율',
           '데이타발생시간', '기초자산ID']

# DH1
DH1_IN_BLOCK_CODE = ['shcode']
DH1_IN_BLOCK_NAME = ['단축코드']
DH1_OUT_BLOCK_CODE = [
           'dan_hotime', 'dan_hstatus', 'dan_offerho1', 'dan_bidho1', 'dan_offerrem1', 'dan_bidrem1', 'dan_preoffercha1', 'dan_prebidcha1', 'dan_offerho2', 'dan_bidho2',
           'dan_offerrem2', 'dan_bidrem2', 'dan_preoffercha2', 'dan_prebidcha2', 'dan_offerho3', 'dan_bidho3', 'dan_offerrem3', 'dan_bidrem3', 'dan_preoffercha3', 'dan_prebidcha3',
           'dan_offerho4', 'dan_bidho4', 'dan_offerrem4', 'dan_bidrem4', 'dan_preoffercha4', 'dan_prebidcha4', 'dan_offerho5', 'dan_bidho5', 'dan_offerrem5', 'dan_bidrem5',
           'dan_preoffercha5', 'dan_prebidcha5', 'dan_totofferrem', 'dan_totbidrem', 'dan_preoffercha', 'dan_prebidcha', 'dan_yeprice', 'dan_yevolume', 'dan_preysign', 'dan_preychange',
           'dan_jnilysign', 'dan_jnilychange', 'shcode', 'volume']
DH1_OUT_BLOCK_NAME = [
           '시간외단일가호가시간', '시간외단일가장구분', '시간외단일가매도호가1', '시간외단일가매수호가1', '시간외단일가매도호가잔량1', '시간외단일가매수호가잔량1', '시간외단일가직전매도대비수량1', '시간외단일가직전매수대비수량1', '시간외단일가매도호가2', '시간외단일가매수호가2',
           '시간외단일가매도호가잔량2', '시간외단일가매수호가잔량2', '시간외단일가직전매도대비수량2', '시간외단일가직전매수대비수량2', '시간외단일가매도호가3', '시간외단일가매수호가3', '시간외단일가매도호가잔량3', '시간외단일가매수호가잔량3', '시간외단일가직전매도대비수량3', '시간외단일가직전매수대비수량3',
           '시간외단일가매도호가4', '시간외단일가매수호가4', '시간외단일가매도호가잔량4', '시간외단일가매수호가잔량4', '시간외단일가직전매도대비수량4', '시간외단일가직전매수대비수량4', '시간외단일가매도호가5', '시간외단일가매수호가5', '시간외단일가매도호가잔량5', '시간외단일가매수호가잔량5',
           '시간외단일가직전매도대비수량5', '시간외단일가직전매수대비수량5', '시간외단일가총매도호가잔량', '시간외단일가총매수호가잔량', '시간외단일가직전매도호가총대비수량', '시간외단일가직전매수호가총대비수량', '시간외단일가예상체결가격', '시간외단일가예상체결수량', '시간외단일가예상가직전가대비구분', '시간외단일가예상가직전가대비',
           '시간외단일가예상가전일가대비구분', '시간외단일가예상가전일가대비', '단축코드', '누적거래량']

# DHA
DHA_IN_BLOCK_CODE = ['shcode']
DHA_IN_BLOCK_NAME = ['단축코드']
DHA_OUT_BLOCK_CODE = [
           'dan_hotime', 'dan_hstatus', 'dan_offerho1', 'dan_bidho1', 'dan_offerrem1', 'dan_bidrem1', 'dan_preoffercha1', 'dan_prebidcha1', 'dan_offerho2', 'dan_bidho2',
           'dan_offerrem2', 'dan_bidrem2', 'dan_preoffercha2', 'dan_prebidcha2', 'dan_offerho3', 'dan_bidho3', 'dan_offerrem3', 'dan_bidrem3', 'dan_preoffercha3', 'dan_prebidcha3',
           'dan_offerho4', 'dan_bidho4', 'dan_offerrem4', 'dan_bidrem4', 'dan_preoffercha4', 'dan_prebidcha4', 'dan_offerho5', 'dan_bidho5', 'dan_offerrem5', 'dan_bidrem5',
           'dan_preoffercha5', 'dan_prebidcha5', 'dan_totofferrem', 'dan_totbidrem', 'dan_preoffercha', 'dan_prebidcha', 'dan_yeprice', 'dan_yevolume', 'dan_preysign', 'dan_preychange',
           'dan_jnilysign', 'dan_jnilychange', 'shcode', 'volume']
DHA_OUT_BLOCK_NAME = [
           '시간외단일가호가시간', '시간외단일가장구분', '시간외단일가매도호가1', '시간외단일가매수호가1', '시간외단일가매도호가잔량1', '시간외단일가매수호가잔량1', '시간외단일가직전매도대비수량1', '시간외단일가직전매수대비수량1', '시간외단일가매도호가2', '시간외단일가매수호가2',
           '시간외단일가매도호가잔량2', '시간외단일가매수호가잔량2', '시간외단일가직전매도대비수량2', '시간외단일가직전매수대비수량2', '시간외단일가매도호가3', '시간외단일가매수호가3', '시간외단일가매도호가잔량3', '시간외단일가매수호가잔량3', '시간외단일가직전매도대비수량3', '시간외단일가직전매수대비수량3',
           '시간외단일가매도호가4', '시간외단일가매수호가4', '시간외단일가매도호가잔량4', '시간외단일가매수호가잔량4', '시간외단일가직전매도대비수량4', '시간외단일가직전매수대비수량4', '시간외단일가매도호가5', '시간외단일가매수호가5', '시간외단일가매도호가잔량5', '시간외단일가매수호가잔량5',
           '시간외단일가직전매도대비수량5', '시간외단일가직전매수대비수량5', '시간외단일가총매도호가잔량', '시간외단일가총매수호가잔량', '시간외단일가직전매도호가총대비수량', '시간외단일가직전매수호가총대비수량', '시간외단일가예상체결가격', '시간외단일가예상체결수량', '시간외단일가예상가직전가대비구분', '시간외단일가예상가직전가대비',
           '시간외단일가예상가전일가대비구분', '시간외단일가예상가전일가대비', '단축코드', '누적거래량']

# DK3
DK3_IN_BLOCK_CODE = ['shcode']
DK3_IN_BLOCK_NAME = ['단축코드']
DK3_OUT_BLOCK_CODE = [
           'dan_chetime', 'dan_sign', 'dan_change', 'dan_drate', 'dan_price', 'dan_opentime', 'dan_open', 'dan_hightime', 'dan_high', 'dan_lowtime',
           'dan_low', 'dan_cgubun', 'dan_cvolume', 'dan_volume', 'dan_value', 'dan_mdvolume', 'dan_mdchecnt', 'dan_msvolume', 'dan_mschecnt', 'dan_prevolume',
           'dan_precvolume', 'dan_cpower', 'dan_status', 'shcode']
DK3_OUT_BLOCK_NAME = [
           '시간외단일가체결시간', '시간외단일가전일대비구분', '시간외단일가전일대비', '시간외단일가등락율', '시간외단일가현재가', '시간외단일가시가시간', '시간외단일가시가', '시간외단일가고가시간', '시간외단일가고가', '시간외단일가저가시간',
           '시간외단일가저가', '시간외단일가체결구분', '시간외단일가체결량', '시간외단일가누적거래량', '시간외단일가누적거래대금', '시간외단일가매도누적체결량', '시간외단일가매도누적체결건수', '시간외단일가매수누적체결량', '시간외단일가매수누적체결건수', '시간외단일가직전거래량',
           '시간외단일가직전체결수량', '시간외단일가체결강도', '시간외단일가장정보', '단축코드']

# DS3
DS3_IN_BLOCK_CODE = ['shcode']
DS3_IN_BLOCK_NAME = ['단축코드']
DS3_OUT_BLOCK_CODE = [
           'dan_chetime', 'dan_sign', 'dan_change', 'dan_drate', 'dan_price', 'dan_opentime', 'dan_open', 'dan_hightime', 'dan_high', 'dan_lowtime',
           'dan_low', 'dan_cgubun', 'dan_cvolume', 'dan_volume', 'dan_value', 'dan_mdvolume', 'dan_mdchecnt', 'dan_msvolume', 'dan_mschecnt', 'dan_prevolume',
           'dan_precvolume', 'dan_cpower', 'dan_status', 'shcode']
DS3_OUT_BLOCK_NAME = [
           '시간외단일가체결시간', '시간외단일가전일대비구분', '시간외단일가전일대비', '시간외단일가등락율', '시간외단일가현재가', '시간외단일가시가시간', '시간외단일가시가', '시간외단일가고가시간', '시간외단일가고가', '시간외단일가저가시간',
           '시간외단일가저가', '시간외단일가체결구분', '시간외단일가체결량', '시간외단일가누적거래량', '시간외단일가누적거래대금', '시간외단일가매도누적체결량', '시간외단일가매도누적체결건수', '시간외단일가매수누적체결량', '시간외단일가매수누적체결건수', '시간외단일가직전거래량',
           '시간외단일가직전체결수량', '시간외단일가체결강도', '시간외단일가장정보', '단축코드']

# DVI
DVI_IN_BLOCK_CODE = ['shcode']
DVI_IN_BLOCK_NAME = ['단축코드(KEY)']
DVI_OUT_BLOCK_CODE = [
           'vi_gubun', 'svi_recprice', 'dvi_recprice', 'vi_trgprice', 'shcode', 'ref_shcode', 'time', 'exchname']
DVI_OUT_BLOCK_NAME = [
           '구분(0:해제1:정적발동2:동적발동3:정적&동적)', '정적VI발동기준가격', '동적VI발동기준가격', 'VI발동가격', '단축코드(KEY)', '참조코드(미사용)', '시간', '거래소명']

# FOCCQ33600
FOCCQ33600_IN_BLOCK_CODE = ['RecCnt', 'Pwd', 'QrySrtDt', 'QryEndDt', 'TermTp']
FOCCQ33600_IN_BLOCK_NAME = ['레코드갯수', '비밀번호', '조회시작일', '조회종료일', '기간구분']
FOCCQ33600_OUT_BLOCK_1_CODE = ['RecCnt', 'Pwd', 'QrySrtDt', 'QryEndDt', 'TermTp']
FOCCQ33600_OUT_BLOCK_1_NAME = ['레코드갯수', '비밀번호', '조회시작일', '조회종료일', '기간구분']
FOCCQ33600_OUT_BLOCK_2_CODE = [
           'RecCnt', 'BnsctrAmt', 'MnyinAmt', 'MnyoutAmt', 'InvstAvrbalPramt', 'InvstPlAmt', 'InvstErnrat']
FOCCQ33600_OUT_BLOCK_2_NAME = [
           '레코드갯수', '매매약정금액', '입금금액', '출금금액', '투자원금평잔금액', '투자손익금액', '투자수익률']
FOCCQ33600_OUT_BLOCK_3_CODE = [
           'BaseDt', 'FdEvalAmt', 'EotEvalAmt', 'InvstAvrbalPramt', 'BnsctrAmt', 'MnyinSecinAmt', 'MnyoutSecoutAmt', 'EvalPnlAmt', 'TermErnrat', 'Idx']
FOCCQ33600_OUT_BLOCK_3_NAME = [
           '기준일', '기초평가금액', '기말평가금액', '투자원금평잔금액', '매매약정금액', '입금고액', '출금고액', '평가손익금액', '기간수익률', '지수']

# GSC
GSC_IN_BLOCK_CODE = ['keysymbol']
GSC_IN_BLOCK_NAME = ['종목코드']
GSC_OUT_BLOCK_CODE = [
           'symbol', 'ovsdate', 'kordate', 'trdtm', 'kortm', 'sign', 'price', 'diff', 'rate', 'open',
           'high', 'low', 'trdq', 'totq', 'cgubun', 'lSeq', 'amount', 'high52p', 'low52p']
GSC_OUT_BLOCK_NAME = [
           '종목코드', '체결일자(현지)', '체결일자(한국)', '체결시간(현지)', '체결시간(한국)', '전일대비구분', '체결가격', '전일대비', '등락율', '시가',
           '고가', '저가', '건별체결수량', '누적체결수량', '체결구분', '초당시퀀스', '누적거래대금', '52주고가', '52주저가']

# GSH
GSH_IN_BLOCK_CODE = ['keysymbol']
GSH_IN_BLOCK_NAME = ['종목코드']
GSH_OUT_BLOCK_CODE = [
           'symbol', 'loctime', 'kortime', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'offerno1', 'bidno1', 'offerho2',
           'bidho2', 'offerrem2', 'bidrem2', 'offerno2', 'bidno2', 'offerho3', 'bidho3', 'offerrem3', 'bidrem3', 'offerno3',
           'bidno3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'offerno4', 'bidno4', 'offerho5', 'bidho5', 'offerrem5',
           'bidrem5', 'offerno5', 'bidno5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'offerno6', 'bidno6', 'offerho7',
           'bidho7', 'offerrem7', 'bidrem7', 'offerno7', 'bidno7', 'offerho8', 'bidho8', 'offerrem8', 'bidrem8', 'offerno8',
           'bidno8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'offerno9', 'bidno9', 'offerho10', 'bidho10', 'offerrem10',
           'bidrem10', 'offerno10', 'bidno10', 'totoffercnt', 'totbidcnt', 'totofferrem', 'totbidrem']
GSH_OUT_BLOCK_NAME = [
           '종목코드', '현지호가시간', '한국호가시간', '매도호가1', '매수호가1', '매도호가잔량1', '매수호가잔량1', '매도호가건수1', '매수호가건수1', '매도호가2',
           '매수호가2', '매도호가잔량2', '매수호가잔량2', '매도호가건수2', '매수호가건수2', '매도호가3', '매수호가3', '매도호가잔량3', '매수호가잔량3', '매도호가건수3',
           '매수호가건수3', '매도호가4', '매수호가4', '매도호가잔량4', '매수호가잔량4', '매도호가건수4', '매수호가건수4', '매도호가5', '매수호가5', '매도호가잔량5',
           '매수호가잔량5', '매도호가건수5', '매수호가건수5', '매도호가6', '매수호가6', '매도호가잔량6', '매수호가잔량6', '매도호가건수6', '매수호가건수6', '매도호가7',
           '매수호가7', '매도호가잔량7', '매수호가잔량7', '매도호가건수7', '매수호가건수7', '매도호가8', '매수호가8', '매도호가잔량8', '매수호가잔량8', '매도호가건수8',
           '매수호가건수8', '매도호가9', '매수호가9', '매도호가잔량9', '매수호가잔량9', '매도호가건수9', '매수호가건수9', '매도호가10', '매수호가10', '매도호가잔량10',
           '매수호가잔량10', '매도호가건수10', '매수호가건수10', '매도호가총건수', '매수호가총건수', '매도호가총수량', '매수호가총수량']

# H1_
H1__IN_BLOCK_CODE = ['shcode']
H1__IN_BLOCK_NAME = ['단축코드']
H1__OUT_BLOCK_CODE = [
           'hotime', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'offerho3',
           'bidho3', 'offerrem3', 'bidrem3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'offerho5', 'bidho5', 'offerrem5',
           'bidrem5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'offerho8',
           'bidho8', 'offerrem8', 'bidrem8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'offerho10', 'bidho10', 'offerrem10',
           'bidrem10', 'totofferrem', 'totbidrem', 'donsigubun', 'shcode', 'alloc_gubun', 'volume', 'midprice', 'offermidsumrem', 'bidmidsumrem',
           'midsumrem', 'midsumremgubun']
H1__OUT_BLOCK_NAME = [
           '호가시간', '매도호가1', '매수호가1', '매도호가잔량1', '매수호가잔량1', '매도호가2', '매수호가2', '매도호가잔량2', '매수호가잔량2', '매도호가3',
           '매수호가3', '매도호가잔량3', '매수호가잔량3', '매도호가4', '매수호가4', '매도호가잔량4', '매수호가잔량4', '매도호가5', '매수호가5', '매도호가잔량5',
           '매수호가잔량5', '매도호가6', '매수호가6', '매도호가잔량6', '매수호가잔량6', '매도호가7', '매수호가7', '매도호가잔량7', '매수호가잔량7', '매도호가8',
           '매수호가8', '매도호가잔량8', '매수호가잔량8', '매도호가9', '매수호가9', '매도호가잔량9', '매수호가잔량9', '매도호가10', '매수호가10', '매도호가잔량10',
           '매수호가잔량10', '총매도호가잔량', '총매수호가잔량', '동시호가구분', '단축코드', '배분적용구분', '누적거래량', '중간가격', '매도중간가잔량합계수량', '매수중간가잔량합계수량',
           '중간가잔량합계수량', "중간가잔량구분('없음'1'매도'2'매수)"]

# H2_
H2__IN_BLOCK_CODE = ['shcode']
H2__IN_BLOCK_NAME = ['단축코드']
H2__OUT_BLOCK_CODE = [
           'hotime', 'tmofferrem', 'tmbidrem', 'pretmoffercha', 'pretmbidcha', 'shcode']
H2__OUT_BLOCK_NAME = [
           '호가시간', '시간외매도잔량', '시간외매수잔량', '시간외매도수량직전대비', '시간외매수수량직전대비', '단축코드']

# HA_
HA__IN_BLOCK_CODE = ['shcode']
HA__IN_BLOCK_NAME = ['단축코드']
HA__OUT_BLOCK_CODE = [
           'hotime', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'offerho3',
           'bidho3', 'offerrem3', 'bidrem3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'offerho5', 'bidho5', 'offerrem5',
           'bidrem5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'offerho8',
           'bidho8', 'offerrem8', 'bidrem8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'offerho10', 'bidho10', 'offerrem10',
           'bidrem10', 'totofferrem', 'totbidrem', 'donsigubun', 'shcode', 'alloc_gubun', 'volume', 'midprice', 'offermidsumrem', 'bidmidsumrem',
           'midsumrem', 'midsumremgubun']
HA__OUT_BLOCK_NAME = [
           '호가시간', '매도호가1', '매수호가1', '매도호가잔량1', '매수호가잔량1', '매도호가2', '매수호가2', '매도호가잔량2', '매수호가잔량2', '매도호가3',
           '매수호가3', '매도호가잔량3', '매수호가잔량3', '매도호가4', '매수호가4', '매도호가잔량4', '매수호가잔량4', '매도호가5', '매수호가5', '매도호가잔량5',
           '매수호가잔량5', '매도호가6', '매수호가6', '매도호가잔량6', '매수호가잔량6', '매도호가7', '매수호가7', '매도호가잔량7', '매수호가잔량7', '매도호가8',
           '매수호가8', '매도호가잔량8', '매수호가잔량8', '매도호가9', '매수호가9', '매도호가잔량9', '매수호가잔량9', '매도호가10', '매수호가10', '매도호가잔량10',
           '매수호가잔량10', '총매도호가잔량', '총매수호가잔량', '동시호가구분', '단축코드', '배분적용구분', '누적거래량', '중간가격', '매도중간가잔량합계수량', '매수중간가잔량합계수량',
           '중간가잔량합계수량', "중간가잔량구분('없음'1'매도'2'매수)"]

# HB_
HB__IN_BLOCK_CODE = ['shcode']
HB__IN_BLOCK_NAME = ['단축코드']
HB__OUT_BLOCK_CODE = [
           'hotime', 'tmofferrem', 'tmbidrem', 'pretmoffercha', 'pretmbidcha', 'shcode']
HB__OUT_BLOCK_NAME = [
           '호가시간', '시간외매도잔량', '시간외매수잔량', '시간외매도수량직전대비', '시간외매수수량직전대비', '단축코드']

# I5_
I5__IN_BLOCK_CODE = ['shcode']
I5__IN_BLOCK_NAME = ['단축코드']
I5__OUT_BLOCK_CODE = [
           'time', 'price', 'sign', 'change', 'volume', 'navdiff', 'nav', 'navchange', 'crate', 'grate',
           'jisu', 'jichange', 'jirate', 'shcode']
I5__OUT_BLOCK_NAME = [
           '시간', '현재가', '전일대비구분', '전일대비', '누적거래량', 'NAV대비', 'NAV', '전일대비', '추적오차', '괴리',
           '지수', '전일대비', '전일대비율', '단축코드']

# IJ_
IJ__IN_BLOCK_CODE = ['upcode']
IJ__IN_BLOCK_NAME = ['업종코드']
IJ__OUT_BLOCK_CODE = [
           'time', 'jisu', 'sign', 'change', 'drate', 'cvolume', 'volume', 'value', 'upjo', 'highjo',
           'unchgjo', 'lowjo', 'downjo', 'upjrate', 'openjisu', 'opentime', 'highjisu', 'hightime', 'lowjisu', 'lowtime',
           'frgsvolume', 'orgsvolume', 'frgsvalue', 'orgsvalue', 'upcode']
IJ__OUT_BLOCK_NAME = [
           '시간', '지수', '전일대비구분', '전일비', '등락율', '체결량', '거래량', '거래대금', '상한종목수', '상승종목수',
           '보합종목수', '하락종목수', '하한종목수', '상승종목비율', '시가지수', '시가시간', '고가지수', '고가시간', '저가지수', '저가시간',
           '외인순매수수량', '기관순매수수량', '외인순매수금액', '기관순매수금액', '업종코드']

# JIF
JIF_IN_BLOCK_CODE = ['jangubun']
JIF_IN_BLOCK_NAME = ['장구분']
JIF_OUT_BLOCK_CODE = ['jangubun', 'jstatus']
JIF_OUT_BLOCK_NAME = ['장구분', '장상태']

# K1_
K1__IN_BLOCK_CODE = ['shcode']
K1__IN_BLOCK_NAME = ['단축코드']
K1__OUT_BLOCK_CODE = [
           'offerno1', 'bidno1', 'offertrad1', 'bidtrad1', 'tradmdvol1', 'tradmsvol1', 'tradmdrate1', 'tradmsrate1', 'tradmdcha1', 'tradmscha1',
           'offerno2', 'bidno2', 'offertrad2', 'bidtrad2', 'tradmdvol2', 'tradmsvol2', 'tradmdrate2', 'tradmsrate2', 'tradmdcha2', 'tradmscha2',
           'offerno3', 'bidno3', 'offertrad3', 'bidtrad3', 'tradmdvol3', 'tradmsvol3', 'tradmdrate3', 'tradmsrate3', 'tradmdcha3', 'tradmscha3',
           'offerno4', 'bidno4', 'offertrad4', 'bidtrad4', 'tradmdvol4', 'tradmsvol4', 'tradmdrate4', 'tradmsrate4', 'tradmdcha4', 'tradmscha4',
           'offerno5', 'bidno5', 'offertrad5', 'bidtrad5', 'tradmdvol5', 'tradmsvol5', 'tradmdrate5', 'tradmsrate5', 'tradmdcha5', 'tradmscha5',
           'ftradmdvol', 'ftradmsvol', 'ftradmdrate', 'ftradmsrate', 'ftradmdcha', 'ftradmscha', 'shcode', 'tradmdval1', 'tradmsval1', 'tradmdavg1',
           'tradmsavg1', 'tradmdval2', 'tradmsval2', 'tradmdavg2', 'tradmsavg2', 'tradmdval3', 'tradmsval3', 'tradmdavg3', 'tradmsavg3', 'tradmdval4',
           'tradmsval4', 'tradmdavg4', 'tradmsavg4', 'tradmdval5', 'tradmsval5', 'tradmdavg5', 'tradmsavg5', 'ftradmdval', 'ftradmsval', 'ftradmdavg',
           'ftradmsavg']
K1__OUT_BLOCK_NAME = [
           '매도증권사코드1', '매수증권사코드1', '매도회원사명1', '매수회원사명1', '매도거래량1', '매수거래량1', '매도거래량비중1', '매도거래량비중1', '매도거래량직전대비1', '매수거래량직전대비1',
           '매도증권사코드2', '매수증권사코드2', '매도회원사명2', '매수회원사명2', '매도거래량2', '매수거래량2', '매도거래량비중2', '매수거래량비중2', '매도거래량직전대비2', '매수거래량직전대비2',
           '매도증권사코드3', '매수증권사코드3', '매도회원사명3', '매수회원사명3', '매도거래량3', '매수거래량3', '매도거래량비중3', '매수거래량비중3', '매도거래량직전대비3', '매수거래량직전대비3',
           '매도증권사코드4', '매수증권사코드4', '매도회원사명4', '매수회원사명4', '매도거래량4', '매수거래량4', '매도거래량비중4', '매수거래량비중4', '매도거래량직전대비4', '매수거래량직전대비4',
           '매도증권사코드5', '매수증권사코드5', '매도회원사명5', '매수회원사명5', '매도거래량5', '매수거래량5', '매도거래량비중5', '매수거래량비중5', '매도거래량직전대비5', '매수거래량직전대비5',
           '외국계증권사매도합계', '외국계증권사매수합계', '외국계증권사매도거래량비중', '외국계증권사매수거래량비중', '외국계증권사매도거래량직전대비', '외국계증권사매수거래량직전대비', '단축코드', '매도거래대금1', '매수거래대금1', '매도평균단가1',
           '매수평균단가1', '매도거래대금2', '매수거래대금2', '매도평균단가2', '매수평균단가2', '매도거래대금3', '매수거래대금3', '매도평균단가3', '매수평균단가3', '매도거래대금4',
           '매수거래대금4', '매도평균단가4', '매수평균단가4', '매도거래대금5', '매수거래대금5', '매도평균단가5', '매수평균단가5', '외국계증권사매도거래대금', '외국계증권사매수거래대금', '외국계증권사매도평균단가',
           '외국계증권사매수평균단가']

# K3_
K3__IN_BLOCK_CODE = ['shcode']
K3__IN_BLOCK_NAME = ['단축코드']
K3__OUT_BLOCK_CODE = [
           'chetime', 'sign', 'change', 'drate', 'price', 'opentime', 'open', 'hightime', 'high', 'lowtime',
           'low', 'cgubun', 'cvolume', 'volume', 'value', 'mdvolume', 'mdchecnt', 'msvolume', 'mschecnt', 'cpower',
           'w_avrg', 'offerho', 'bidho', 'status', 'jnilvolume', 'shcode', 'exchname']
K3__OUT_BLOCK_NAME = [
           '체결시간', '전일대비구분', '전일대비', '등락율', '현재가', '시가시간', '시가', '고가시간', '고가', '저가시간',
           '저가', '체결구분', '체결량', '누적거래량', '누적거래대금', '매도누적체결량', '매도누적체결건수', '매수누적체결량', '매수누적체결건수', '체결강도',
           '가중평균가', '매도호가', '매수호가', '장정보', '전일동시간대거래량', '단축코드', '거래소명']

# KH_
KH__IN_BLOCK_CODE = ['shcode']
KH__IN_BLOCK_NAME = ['종목코드']
KH__OUT_BLOCK_CODE = [
           'time', 'price', 'sign', 'change', 'volume', 'drate', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem',
           'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'dwcvolume', 'swcvolume', 'djcvolume', 'sjcvolume', 'tdvolume', 'tsvolume',
           'tvol', 'dwcvalue', 'swcvalue', 'djcvalue', 'sjcvalue', 'tdvalue', 'tsvalue', 'tval', 'pdgvolume', 'psgvolume',
           'shcode']
KH__OUT_BLOCK_NAME = [
           '수신시간', '현재가', '전일대비구분', '전일대비', '누적거래량', '등락율', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량',
           '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체매도체결수량', '전체매수체결수량',
           '전체순매수수량', '전체매도위탁체결금액', '전체매수위탁체결금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체매도체결금액', '전체매수체결금액', '전체순매수금액', '매도사전공시수량', '매수사전공시수량',
           '종목코드']

# KM_
KM__IN_BLOCK_CODE = ['gubun']
KM__IN_BLOCK_NAME = ['구분값']
KM__OUT_BLOCK_CODE = [
           'time', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem', 'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'cdwvolume',
           'cdjvolume', 'cswvolume', 'csjvolume', 'cwvol', 'cjvol', 'bdwvolume', 'bdjvolume', 'bswvolume', 'bsjvolume', 'bwvol',
           'bjvol', 'dwvolume', 'swvolume', 'wvol', 'djvolume', 'sjvolume', 'jvol', 'cdwvalue', 'cdjvalue', 'cswvalue',
           'csjvalue', 'cwval', 'cjval', 'bdwvalue', 'bdjvalue', 'bswvalue', 'bsjvalue', 'bwval', 'bjval', 'dwvalue',
           'swvalue', 'wval', 'djvalue', 'sjvalue', 'jval', 'k50jisu', 'k50sign', 'change', 'k50basis', 'cdvolume',
           'csvolume', 'cvol', 'bdvolume', 'bsvolume', 'bvol', 'tdvolume', 'tsvolume', 'tvol', 'cdvalue', 'csvalue',
           'cval', 'bdvalue', 'bsvalue', 'bval', 'tdvalue', 'tsvalue', 'tval', 'p_cdvolcha', 'p_csvolcha', 'p_cvolcha',
           'p_bdvolcha', 'p_bsvolcha', 'p_bvolcha', 'p_tdvolcha', 'p_tsvolcha', 'p_tvolcha', 'p_cdvalcha', 'p_csvalcha', 'p_cvalcha', 'p_bdvalcha',
           'p_bsvalcha', 'p_bvalcha', 'p_tdvalcha', 'p_tsvalcha', 'p_tvalcha', 'gubun']
KM__OUT_BLOCK_NAME = [
           '수신시간', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량', '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '차익매도위탁체결수량',
           '차익매도자기체결수량', '차익매수위탁체결수량', '차익매수자기체결수량', '차익위탁순매수수량', '차익자기순매수수량', '비차익매도위탁체결수량', '비차익매도자기체결수량', '비차익매수위탁체결수량', '비차익매수자기체결수량', '비차익위탁순매수수량',
           '비차익자기순매수수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체위탁순매수수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체자기순매수수량', '차익매도위탁체결금액', '차익매도자기체결금액', '차익매수위탁체결금액',
           '차익매수자기체결금액', '차익위탁순매수금액', '차익자기순매수금액', '비차익매도위탁체결금액', '비차익매도자기체결금액', '비차익매수위탁체결금액', '비차익매수자기체결금액', '비차익위탁순매수금액', '비차익자기순매수금액', '전체매도위탁체결금액',
           '전체매수위탁체결금액', '전체위탁순매수금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체자기순매수금액', 'KOSDAQ50지수', 'KOSDAQ50전일대비구분', 'KOSDAQ50전일대비', 'KOSDAQ50베이시스', '차익매도체결수량합계',
           '차익매수체결수량합계', '차익순매수수량합계', '비차익매도체결수량합계', '비차익매수체결수량합계', '비차익순매수수량합계', '전체매도체결수량합계', '전체매수체결수량합계', '전체순매수수량합계', '차익매도체결금액합계', '차익매수체결금액합계',
           '차익순매수금액합계', '비차익매도체결금액합계', '비차익매수체결금액합계', '비차익순매수금액합계', '전체매도체결금액합계', '전체매수체결금액합계', '전체순매수금액합계', '차익매도체결수량직전대비', '차익매수체결수량직전대비', '차익순매수수량직전대비',
           '비차익매도체결수량직전대비', '비차익매수체결수량직전대비', '비차익순매수수량직전대비', '전체매도체결수량직전대비', '전체매수체결수량직전대비', '전체순매수수량직전대비', '차익매도체결금액직전대비', '차익매수체결금액직전대비', '차익순매수금액직전대비', '비차익매도체결금액직전대비',
           '비차익매수체결금액직전대비', '비차익순매수금액직전대비', '전체매도체결금액직전대비', '전체매수체결금액직전대비', '전체순매수금액직전대비', '구분값']

# KS_
KS__IN_BLOCK_CODE = ['shcode']
KS__IN_BLOCK_NAME = ['단축코드']
KS__OUT_BLOCK_CODE = ['offerho', 'bidho', 'shcode']
KS__OUT_BLOCK_NAME = ['매도호가', '매수호가', '단축코드']

# MK2
MK2_IN_BLOCK_CODE = ['symbol']
MK2_IN_BLOCK_NAME = ['심볼코드']
MK2_OUT_BLOCK_CODE = [
           'date', 'time', 'kodate', 'kotime', 'open', 'high', 'low', 'price', 'sign', 'change',
           'uprate', 'bidho', 'bidrem', 'offerho', 'offerrem', 'volume', 'xsymbol', 'cvolume']
MK2_OUT_BLOCK_NAME = [
           '일자', '시간', '한국일자', '한국시간', '시가', '고가', '저가', '현재가', '전일대비구분', '전일대비',
           '등락율', '매수호가', '매수잔량', '매도호가', '매도잔량', '누적거래량', '심벌', '체결거래량']

# NBM
NBM_IN_BLOCK_CODE = ['ex_upcode']
NBM_IN_BLOCK_NAME = ['거래소별업종코드']
NBM_OUT_BLOCK_CODE = [
           'tjjcode', 'tjjtime', 'msvolume', 'mdvolume', 'msvol', 'p_msvol', 'msvalue', 'mdvalue', 'msval', 'p_msval',
           'upcode', 'ex_upcode']
NBM_OUT_BLOCK_NAME = [
           '투자자코드', '수신시간', '매수거래량', '매도거래량', '거래량순매수', '거래량순매수직전대비', '매수거래대금', '매도거래대금', '거래대금순매수', '거래대금순매수직전대비',
           '업종코드', '거래소별업종코드']

# NBT
NBT_IN_BLOCK_CODE = ['ex_upcode']
NBT_IN_BLOCK_NAME = ['거래소별업종코드']
NBT_OUT_BLOCK_CODE = [
           'tjjtime', 'tjjcode1', 'msvolume1', 'mdvolume1', 'msvol1', 'msvalue1', 'mdvalue1', 'msval1', 'tjjcode2', 'msvolume2',
           'mdvolume2', 'msvol2', 'msvalue2', 'mdvalue2', 'msval2', 'tjjcode3', 'msvolume3', 'mdvolume3', 'msvol3', 'msvalue3',
           'mdvalue3', 'msval3', 'tjjcode4', 'msvolume4', 'mdvolume4', 'msvol4', 'msvalue4', 'mdvalue4', 'msval4', 'tjjcode5',
           'msvolume5', 'mdvolume5', 'msvol5', 'msvalue5', 'mdvalue5', 'msval5', 'tjjcode6', 'msvolume6', 'mdvolume6', 'msvol6',
           'msvalue6', 'mdvalue6', 'msval6', 'tjjcode7', 'msvolume7', 'mdvolume7', 'msvol7', 'msvalue7', 'mdvalue7', 'msval7',
           'tjjcode8', 'msvolume8', 'mdvolume8', 'msvol8', 'msvalue8', 'mdvalue8', 'msval8', 'tjjcode9', 'msvolume9', 'mdvolume9',
           'msvol9', 'msvalue9', 'mdvalue9', 'msval9', 'tjjcode10', 'msvolume10', 'mdvolume10', 'msvol10', 'msvalue10', 'mdvalue10',
           'msval10', 'tjjcode11', 'msvolume11', 'mdvolume11', 'msvol11', 'msvalue11', 'mdvalue11', 'msval11', 'upcode', 'tjjcode0',
           'msvolume0', 'mdvolume0', 'msvol0', 'msvalue0', 'mdvalue0', 'msval0', 'ex_upcode']
NBT_OUT_BLOCK_NAME = [
           '수신시간', '투자자코드1(개인)', '매수거래량1', '매도거래량1', '거래량순매수1', '매수거래대금1', '매도거래대금1', '거래대금순매수1', '투자자코드2(외국인)', '매수거래량2',
           '매도거래량2', '거래량순매수2', '매수거래대금2', '매도거래대금2', '거래대금순매수2', '투자자코드3(기관계)', '매수거래량3', '매도거래량3', '거래량순매수3', '매수거래대금3',
           '매도거래대금3', '거래대금순매수3', '투자자코드4(증권)', '매수거래량4', '매도거래량4', '거래량순매수4', '매수거래대금4', '매도거래대금4', '거래대금순매수4', '투자자코드5(투신)',
           '매수거래량5', '매도거래량5', '거래량순매수5', '매수거래대금5', '매도거래대금5', '거래대금순매수5', '투자자코드6(은행)', '매수거래량6', '매도거래량6', '거래량순매수6',
           '매수거래대금6', '매도거래대금6', '거래대금순매수6', '투자자코드7(보험)', '매수거래량7', '매도거래량7', '거래량순매수7', '매수거래대금7', '매도거래대금7', '거래대금순매수7',
           '투자자코드8(종금)', '매수거래량8', '매도거래량8', '거래량순매수8', '매수거래대금8', '매도거래대금8', '거래대금순매수8', '투자자코드9(기금)', '매수거래량9', '매도거래량9',
           '거래량순매수9', '매수거래대금9', '매도거래대금9', '거래대금순매수9', '투자자코드10(선물업자)', '매수거래량10', '매도거래량10', '거래량순매수10', '매수거래대금10', '매도거래대금10',
           '거래대금순매수10', '투자자코드11(기타)', '매수거래량11', '매도거래량11', '거래량순매수11', '매수거래대금11', '매도거래대금11', '거래대금순매수11', '업종코드', '투자자코드0(사모펀드)',
           '매수거래량0', '매도거래량0', '거래량순매수0', '매수거래대금0', '매도거래대금0', '거래대금순매수0', '거래소별업종코드']

# NH1
NH1_IN_BLOCK_CODE = ['ex_shcode']
NH1_IN_BLOCK_NAME = ['거래소별단축코드']
NH1_OUT_BLOCK_CODE = [
           'hotime', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'offerho3',
           'bidho3', 'offerrem3', 'bidrem3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'offerho5', 'bidho5', 'offerrem5',
           'bidrem5', 'offerho6', 'bidho6', 'offerrem6', 'bidrem6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'offerho8',
           'bidho8', 'offerrem8', 'bidrem8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'offerho10', 'bidho10', 'offerrem10',
           'bidrem10', 'totofferrem', 'totbidrem', 'donsigubun', 'shcode', 'alloc_gubun', 'volume', 'midprice', 'offermidsumrem', 'bidmidsumrem',
           'midsumrem', 'midsumremgubun', 'ex_shcode']
NH1_OUT_BLOCK_NAME = [
           '호가시간', '매도호가1', '매수호가1', '매도호가잔량1', '매수호가잔량1', '매도호가2', '매수호가2', '매도호가잔량2', '매수호가잔량2', '매도호가3',
           '매수호가3', '매도호가잔량3', '매수호가잔량3', '매도호가4', '매수호가4', '매도호가잔량4', '매수호가잔량4', '매도호가5', '매수호가5', '매도호가잔량5',
           '매수호가잔량5', '매도호가6', '매수호가6', '매도호가잔량6', '매수호가잔량6', '매도호가7', '매수호가7', '매도호가잔량7', '매수호가잔량7', '매도호가8',
           '매수호가8', '매도호가잔량8', '매수호가잔량8', '매도호가9', '매수호가9', '매도호가잔량9', '매수호가잔량9', '매도호가10', '매수호가10', '매도호가잔량10',
           '매수호가잔량10', '총매도호가잔량', '총매수호가잔량', '동시호가구분', '단축코드', '배분적용구분', '누적거래량', '중간가격', '매도중간가잔량합계수량', '매수중간가잔량합계수량',
           '중간가잔량합계수량', "중간가잔량구분('없음'1'매도'2'매수)", '거래소별단축코드']

# NK1
NK1_IN_BLOCK_CODE = ['ex_shcode']
NK1_IN_BLOCK_NAME = ['거래소별단축코드']
NK1_OUT_BLOCK_CODE = [
           'offerno1', 'bidno1', 'offertrad1', 'bidtrad1', 'tradmdvol1', 'tradmsvol1', 'tradmdrate1', 'tradmsrate1', 'tradmdcha1', 'tradmscha1',
           'offerno2', 'bidno2', 'offertrad2', 'bidtrad2', 'tradmdvol2', 'tradmsvol2', 'tradmdrate2', 'tradmsrate2', 'tradmdcha2', 'tradmscha2',
           'offerno3', 'bidno3', 'offertrad3', 'bidtrad3', 'tradmdvol3', 'tradmsvol3', 'tradmdrate3', 'tradmsrate3', 'tradmdcha3', 'tradmscha3',
           'offerno4', 'bidno4', 'offertrad4', 'bidtrad4', 'tradmdvol4', 'tradmsvol4', 'tradmdrate4', 'tradmsrate4', 'tradmdcha4', 'tradmscha4',
           'offerno5', 'bidno5', 'offertrad5', 'bidtrad5', 'tradmdvol5', 'tradmsvol5', 'tradmdrate5', 'tradmsrate5', 'tradmdcha5', 'tradmscha5',
           'ftradmdvol', 'ftradmsvol', 'ftradmdrate', 'ftradmsrate', 'ftradmdcha', 'ftradmscha', 'shcode', 'tradmdval1', 'tradmsval1', 'tradmdavg1',
           'tradmsavg1', 'tradmdval2', 'tradmsval2', 'tradmdavg2', 'tradmsavg2', 'tradmdval3', 'tradmsval3', 'tradmdavg3', 'tradmsavg3', 'tradmdval4',
           'tradmsval4', 'tradmdavg4', 'tradmsavg4', 'tradmdval5', 'tradmsval5', 'tradmdavg5', 'tradmsavg5', 'ftradmdval', 'ftradmsval', 'ftradmdavg',
           'ftradmsavg', 'time', 'exchname', 'ex_shcode']
NK1_OUT_BLOCK_NAME = [
           '매도증권사코드1', '매수증권사코드1', '매도회원사명1', '매수회원사명1', '매도거래량1', '매수거래량1', '매도거래량비중1', '매도거래량비중1', '매도거래량직전대비1', '매수거래량직전대비1',
           '매도증권사코드2', '매수증권사코드2', '매도회원사명2', '매수회원사명2', '매도거래량2', '매수거래량2', '매도거래량비중2', '매수거래량비중2', '매도거래량직전대비2', '매수거래량직전대비2',
           '매도증권사코드3', '매수증권사코드3', '매도회원사명3', '매수회원사명3', '매도거래량3', '매수거래량3', '매도거래량비중3', '매수거래량비중3', '매도거래량직전대비3', '매수거래량직전대비3',
           '매도증권사코드4', '매수증권사코드4', '매도회원사명4', '매수회원사명4', '매도거래량4', '매수거래량4', '매도거래량비중4', '매수거래량비중4', '매도거래량직전대비4', '매수거래량직전대비4',
           '매도증권사코드5', '매수증권사코드5', '매도회원사명5', '매수회원사명5', '매도거래량5', '매수거래량5', '매도거래량비중5', '매수거래량비중5', '매도거래량직전대비5', '매수거래량직전대비5',
           '외국계증권사매도합계', '외국계증권사매수합계', '외국계증권사매도거래량비중', '외국계증권사매수거래량비중', '외국계증권사매도거래량직전대비', '외국계증권사매수거래량직전대비', '단축코드', '매도거래대금1', '매수거래대금1', '매도평균단가1',
           '매수평균단가1', '매도거래대금2', '매수거래대금2', '매도평균단가2', '매수평균단가2', '매도거래대금3', '매수거래대금3', '매도평균단가3', '매수평균단가3', '매도거래대금4',
           '매수거래대금4', '매도평균단가4', '매수평균단가4', '매도거래대금5', '매수거래대금5', '매도평균단가5', '매수평균단가5', '외국계증권사매도거래대금', '외국계증권사매수거래대금', '외국계증권사매도평균단가',
           '외국계증권사매수평균단가', '수신시간', '거래소명', '거래소별단축코드']

# NPH
NPH_IN_BLOCK_CODE = ['ex_shcode']
NPH_IN_BLOCK_NAME = ['거래소별단축코드']
NPH_OUT_BLOCK_CODE = [
           'time', 'price', 'sign', 'change', 'volume', 'drate', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem',
           'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'dwcvolume', 'swcvolume', 'djcvolume', 'sjcvolume', 'tdvolume', 'tsvolume',
           'tvol', 'dwcvalue', 'swcvalue', 'djcvalue', 'sjcvalue', 'tdvalue', 'tsvalue', 'tval', 'pdgvolume', 'psgvolume',
           'shcode', 'ex_shcode']
NPH_OUT_BLOCK_NAME = [
           '수신시간', '현재가', '전일대비구분', '전일대비', '누적거래량', '등락율', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량',
           '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체매도체결수량', '전체매수체결수량',
           '전체순매수수량', '전체매도위탁체결금액', '전체매수위탁체결금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체매도체결금액', '전체매수체결금액', '전체순매수금액', '매도사전공시수량', '매수사전공시수량',
           '종목코드', '거래소별단축코드']

# NPM
NPM_IN_BLOCK_CODE = ['ex_gubun']
NPM_IN_BLOCK_NAME = ['거래소별구분값']
NPM_OUT_BLOCK_CODE = [
           'time', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem', 'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'cdwvolume',
           'cdjvolume', 'cswvolume', 'csjvolume', 'cwvol', 'cjvol', 'bdwvolume', 'bdjvolume', 'bswvolume', 'bsjvolume', 'bwvol',
           'bjvol', 'dwvolume', 'swvolume', 'wvol', 'djvolume', 'sjvolume', 'jvol', 'cdwvalue', 'cdjvalue', 'cswvalue',
           'csjvalue', 'cwval', 'cjval', 'bdwvalue', 'bdjvalue', 'bswvalue', 'bsjvalue', 'bwval', 'bjval', 'dwvalue',
           'swvalue', 'wval', 'djvalue', 'sjvalue', 'jval', 'k200jisu', 'k200sign', 'change', 'k200basis', 'cdvolume',
           'csvolume', 'cvol', 'bdvolume', 'bsvolume', 'bvol', 'tdvolume', 'tsvolume', 'tvol', 'cdvalue', 'csvalue',
           'cval', 'bdvalue', 'bsvalue', 'bval', 'tdvalue', 'tsvalue', 'tval', 'p_cdvolcha', 'p_csvolcha', 'p_cvolcha',
           'p_bdvolcha', 'p_bsvolcha', 'p_bvolcha', 'p_tdvolcha', 'p_tsvolcha', 'p_tvolcha', 'p_cdvalcha', 'p_csvalcha', 'p_cvalcha', 'p_bdvalcha',
           'p_bsvalcha', 'p_bvalcha', 'p_tdvalcha', 'p_tsvalcha', 'p_tvalcha', 'gubun', 'ex_gubun']
NPM_OUT_BLOCK_NAME = [
           '수신시간', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량', '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '차익매도위탁체결수량',
           '차익매도자기체결수량', '차익매수위탁체결수량', '차익매수자기체결수량', '차익위탁순매수수량', '차익자기순매수수량', '비차익매도위탁체결수량', '비차익매도자기체결수량', '비차익매수위탁체결수량', '비차익매수자기체결수량', '비차익위탁순매수수량',
           '비차익자기순매수수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체위탁순매수수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체자기순매수수량', '차익매도위탁체결금액', '차익매도자기체결금액', '차익매수위탁체결금액',
           '차익매수자기체결금액', '차익위탁순매수금액', '차익자기순매수금액', '비차익매도위탁체결금액', '비차익매도자기체결금액', '비차익매수위탁체결금액', '비차익매수자기체결금액', '비차익위탁순매수금액', '비차익자기순매수금액', '전체매도위탁체결금액',
           '전체매수위탁체결금액', '전체위탁순매수금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체자기순매수금액', 'KOSPI200지수', 'KOSPI200전일대비구분', 'KOSPI200전일대비', 'KOSPI200베이시스', '차익매도체결수량합계',
           '차익매수체결수량합계', '차익순매수수량합계', '비차익매도체결수량합계', '비차익매수체결수량합계', '비차익순매수수량합계', '전체매도체결수량합계', '전체매수체결수량합계', '전체순매수수량합계', '차익매도체결금액합계', '차익매수체결금액합계',
           '차익순매수금액합계', '비차익매도체결금액합계', '비차익매수체결금액합계', '비차익순매수금액합계', '전체매도체결금액합계', '전체매수체결금액합계', '전체순매수금액합계', '차익매도체결수량직전대비', '차익매수체결수량직전대비', '차익순매수수량직전대비',
           '비차익매도체결수량직전대비', '비차익매수체결수량직전대비', '비차익순매수수량직전대비', '전체매도체결수량직전대비', '전체매수체결수량직전대비', '전체순매수수량직전대비', '차익매도체결금액직전대비', '차익매수체결금액직전대비', '차익순매수금액직전대비', '비차익매도체결금액직전대비',
           '비차익매수체결금액직전대비', '비차익순매수금액직전대비', '전체매도체결금액직전대비', '전체매수체결금액직전대비', '전체순매수금액직전대비', '구분값', '거래소별구분값']

# NS2
NS2_IN_BLOCK_CODE = ['ex_shcode']
NS2_IN_BLOCK_NAME = ['거래소별단축코드']
NS2_OUT_BLOCK_CODE = ['offerho', 'bidho', 'shcode', 'ex_shcode']
NS2_OUT_BLOCK_NAME = ['매도호가', '매수호가', '단축코드', '거래소별단축코드']

# NS3
NS3_IN_BLOCK_CODE = ['ex_shcode']
NS3_IN_BLOCK_NAME = ['거래소별단축코드']
NS3_OUT_BLOCK_CODE = [
           'chetime', 'sign', 'change', 'drate', 'price', 'opentime', 'open', 'hightime', 'high', 'lowtime',
           'low', 'cgubun', 'cvolume', 'volume', 'value', 'mdvolume', 'mdchecnt', 'msvolume', 'mschecnt', 'cpower',
           'w_avrg', 'offerho', 'bidho', 'status', 'jnilvolume', 'shcode', 'exchname', 'ex_shcode']
NS3_OUT_BLOCK_NAME = [
           '체결시간', '전일대비구분', '전일대비', '등락율', '현재가', '시가시간', '시가', '고가시간', '고가', '저가시간',
           '저가', '체결구분', '체결량', '누적거래량', '누적거래대금', '매도누적체결량', '매도누적체결건수', '매수누적체결량', '매수누적체결건수', '체결강도',
           '가중평균가', '매도호가', '매수호가', '장정보', '전일동시간대거래량', '단축코드', '거래소명', '거래소별단축코드']

# NVI
NVI_IN_BLOCK_CODE = ['ex_shcode']
NVI_IN_BLOCK_NAME = ['거래소별단축코드']
NVI_OUT_BLOCK_CODE = [
           'vi_gubun', 'svi_recprice', 'dvi_recprice', 'vi_trgprice', 'shcode', 'ref_shcode', 'time', 'exchname', 'ex_shcode']
NVI_OUT_BLOCK_NAME = [
           '구분(0:해제1:정적발동2:동적발동3:정적&동적)', '정적VI발동기준가격', '동적VI발동기준가격', 'VI발동가격', '단축코드', '참조코드(미사용)', '시간', '거래소명', '거래소별단축코드']

# NWS
NWS_IN_BLOCK_CODE = ['nwcode']
NWS_IN_BLOCK_NAME = ['뉴스코드']
NWS_OUT_BLOCK_CODE = [
           'date', 'time', 'id', 'realkey', 'title', 'code', 'bodysize']
NWS_OUT_BLOCK_NAME = [
           '날짜', '시간', '뉴스구분자', '키값', '제목', '단축종목코드', 'BODY길이']

# NYS
NYS_IN_BLOCK_CODE = ['ex_shcode']
NYS_IN_BLOCK_NAME = ['거래소별단축코드']
NYS_OUT_BLOCK_CODE = [
           'hotime', 'yeprice', 'yevolume', 'jnilysign', 'jnilchange', 'jnilydrate', 'yofferho0', 'ybidho0', 'yofferrem0', 'ybidrem0',
           'shcode', 'exchname', 'ex_shcode']
NYS_OUT_BLOCK_NAME = [
           '호가시간', '예상체결가격', '예상체결수량', '예상체결가전일종가대비구분', '예상체결가전일종가대비', '예상체결가전일종가등락율', '예상매도호가', '예상매수호가', '예상매도호가수량', '예상매수호가수량',
           '단축코드', '거래소명', '거래소별단축코드']

# OK_
OK__IN_BLOCK_CODE = ['shcode']
OK__IN_BLOCK_NAME = ['단축코드']
OK__OUT_BLOCK_CODE = [
           'offerno1', 'bidno1', 'offertrad1', 'bidtrad1', 'tradmdvol1', 'tradmsvol1', 'tradmdrate1', 'tradmsrate1', 'tradmdcha1', 'tradmscha1',
           'offerno2', 'bidno2', 'offertrad2', 'bidtrad2', 'tradmdvol2', 'tradmsvol2', 'tradmdrate2', 'tradmsrate2', 'tradmdcha2', 'tradmscha2',
           'offerno3', 'bidno3', 'offertrad3', 'bidtrad3', 'tradmdvol3', 'tradmsvol3', 'tradmdrate3', 'tradmsrate3', 'tradmdcha3', 'tradmscha3',
           'offerno4', 'bidno4', 'offertrad4', 'bidtrad4', 'tradmdvol4', 'tradmsvol4', 'tradmdrate4', 'tradmsrate4', 'tradmdcha4', 'tradmscha4',
           'offerno5', 'bidno5', 'offertrad5', 'bidtrad5', 'tradmdvol5', 'tradmsvol5', 'tradmdrate5', 'tradmsrate5', 'tradmdcha5', 'tradmscha5',
           'ftradmdvol', 'ftradmsvol', 'ftradmdrate', 'ftradmsrate', 'ftradmdcha', 'ftradmscha', 'shcode', 'tradmdval1', 'tradmsval1', 'tradmdavg1',
           'tradmsavg1', 'tradmdval2', 'tradmsval2', 'tradmdavg2', 'tradmsavg2', 'tradmdval3', 'tradmsval3', 'tradmdavg3', 'tradmsavg3', 'tradmdval4',
           'tradmsval4', 'tradmdavg4', 'tradmsavg4', 'tradmdval5', 'tradmsval5', 'tradmdavg5', 'tradmsavg5', 'ftradmdval', 'ftradmsval', 'ftradmdavg',
           'ftradmsavg']
OK__OUT_BLOCK_NAME = [
           '매도증권사코드1', '매수증권사코드1', '매도회원사명1', '매수회원사명1', '매도거래량1', '매수거래량1', '매도거래량비중1', '매도거래량비중1', '매도거래량직전대비1', '매수거래량직전대비1',
           '매도증권사코드2', '매수증권사코드2', '매도회원사명2', '매수회원사명2', '매도거래량2', '매수거래량2', '매도거래량비중2', '매수거래량비중2', '매도거래량직전대비2', '매수거래량직전대비2',
           '매도증권사코드3', '매수증권사코드3', '매도회원사명3', '매수회원사명3', '매도거래량3', '매수거래량3', '매도거래량비중3', '매수거래량비중3', '매도거래량직전대비3', '매수거래량직전대비3',
           '매도증권사코드4', '매수증권사코드4', '매도회원사명4', '매수회원사명4', '매도거래량4', '매수거래량4', '매도거래량비중4', '매수거래량비중4', '매도거래량직전대비4', '매수거래량직전대비4',
           '매도증권사코드5', '매수증권사코드5', '매도회원사명5', '매수회원사명5', '매도거래량5', '매수거래량5', '매도거래량비중5', '매수거래량비중5', '매도거래량직전대비5', '매수거래량직전대비5',
           '외국계증권사매도합계', '외국계증권사매수합계', '외국계증권사매도거래량비중', '외국계증권사매수거래량비중', '외국계증권사매도거래량직전대비', '외국계증권사매수거래량직전대비', '단축코드', '매도거래대금1', '매수거래대금1', '매도평균단가1',
           '매수평균단가1', '매도거래대금2', '매수거래대금2', '매도평균단가2', '매수평균단가2', '매도거래대금3', '매수거래대금3', '매도평균단가3', '매수평균단가3', '매도거래대금4',
           '매수거래대금4', '매도평균단가4', '매수평균단가4', '매도거래대금5', '매수거래대금5', '매도평균단가5', '매수평균단가5', '외국계증권사매도거래대금', '외국계증권사매수거래대금', '외국계증권사매도평균단가',
           '외국계증권사매수평균단가']

# PH_
PH__IN_BLOCK_CODE = ['shcode']
PH__IN_BLOCK_NAME = ['종목코드']
PH__OUT_BLOCK_CODE = [
           'time', 'price', 'sign', 'change', 'volume', 'drate', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem',
           'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'dwcvolume', 'swcvolume', 'djcvolume', 'sjcvolume', 'tdvolume', 'tsvolume',
           'tvol', 'dwcvalue', 'swcvalue', 'djcvalue', 'sjcvalue', 'tdvalue', 'tsvalue', 'tval', 'pdgvolume', 'psgvolume',
           'shcode']
PH__OUT_BLOCK_NAME = [
           '수신시간', '현재가', '전일대비구분', '전일대비', '누적거래량', '등락율', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량',
           '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체매도체결수량', '전체매수체결수량',
           '전체순매수수량', '전체매도위탁체결금액', '전체매수위탁체결금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체매도체결금액', '전체매수체결금액', '전체순매수금액', '매도사전공시수량', '매수사전공시수량',
           '종목코드']

# PM_
PM__IN_BLOCK_CODE = ['gubun']
PM__IN_BLOCK_NAME = ['구분값']
PM__OUT_BLOCK_CODE = [
           'time', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem', 'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'cdwvolume',
           'cdjvolume', 'cswvolume', 'csjvolume', 'cwvol', 'cjvol', 'bdwvolume', 'bdjvolume', 'bswvolume', 'bsjvolume', 'bwvol',
           'bjvol', 'dwvolume', 'swvolume', 'wvol', 'djvolume', 'sjvolume', 'jvol', 'cdwvalue', 'cdjvalue', 'cswvalue',
           'csjvalue', 'cwval', 'cjval', 'bdwvalue', 'bdjvalue', 'bswvalue', 'bsjvalue', 'bwval', 'bjval', 'dwvalue',
           'swvalue', 'wval', 'djvalue', 'sjvalue', 'jval', 'k200jisu', 'k200sign', 'change', 'k200basis', 'cdvolume',
           'csvolume', 'cvol', 'bdvolume', 'bsvolume', 'bvol', 'tdvolume', 'tsvolume', 'tvol', 'cdvalue', 'csvalue',
           'cval', 'bdvalue', 'bsvalue', 'bval', 'tdvalue', 'tsvalue', 'tval', 'p_cdvolcha', 'p_csvolcha', 'p_cvolcha',
           'p_bdvolcha', 'p_bsvolcha', 'p_bvolcha', 'p_tdvolcha', 'p_tsvolcha', 'p_tvolcha', 'p_cdvalcha', 'p_csvalcha', 'p_cvalcha', 'p_bdvalcha',
           'p_bsvalcha', 'p_bvalcha', 'p_tdvalcha', 'p_tsvalcha', 'p_tvalcha', 'gubun']
PM__OUT_BLOCK_NAME = [
           '수신시간', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량', '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '차익매도위탁체결수량',
           '차익매도자기체결수량', '차익매수위탁체결수량', '차익매수자기체결수량', '차익위탁순매수수량', '차익자기순매수수량', '비차익매도위탁체결수량', '비차익매도자기체결수량', '비차익매수위탁체결수량', '비차익매수자기체결수량', '비차익위탁순매수수량',
           '비차익자기순매수수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체위탁순매수수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체자기순매수수량', '차익매도위탁체결금액', '차익매도자기체결금액', '차익매수위탁체결금액',
           '차익매수자기체결금액', '차익위탁순매수금액', '차익자기순매수금액', '비차익매도위탁체결금액', '비차익매도자기체결금액', '비차익매수위탁체결금액', '비차익매수자기체결금액', '비차익위탁순매수금액', '비차익자기순매수금액', '전체매도위탁체결금액',
           '전체매수위탁체결금액', '전체위탁순매수금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체자기순매수금액', 'KOSPI200지수', 'KOSPI200전일대비구분', 'KOSPI200전일대비', 'KOSPI200베이시스', '차익매도체결수량합계',
           '차익매수체결수량합계', '차익순매수수량합계', '비차익매도체결수량합계', '비차익매수체결수량합계', '비차익순매수수량합계', '전체매도체결수량합계', '전체매수체결수량합계', '전체순매수수량합계', '차익매도체결금액합계', '차익매수체결금액합계',
           '차익순매수금액합계', '비차익매도체결금액합계', '비차익매수체결금액합계', '비차익순매수금액합계', '전체매도체결금액합계', '전체매수체결금액합계', '전체순매수금액합계', '차익매도체결수량직전대비', '차익매수체결수량직전대비', '차익순매수수량직전대비',
           '비차익매도체결수량직전대비', '비차익매수체결수량직전대비', '비차익순매수수량직전대비', '전체매도체결수량직전대비', '전체매수체결수량직전대비', '전체순매수수량직전대비', '차익매도체결금액직전대비', '차익매수체결금액직전대비', '차익순매수금액직전대비', '비차익매도체결금액직전대비',
           '비차익매수체결금액직전대비', '비차익순매수금액직전대비', '전체매도체결금액직전대비', '전체매수체결금액직전대비', '전체순매수금액직전대비', '구분값']

# S2_
S2__IN_BLOCK_CODE = ['shcode']
S2__IN_BLOCK_NAME = ['단축코드']
S2__OUT_BLOCK_CODE = ['offerho', 'bidho', 'shcode']
S2__OUT_BLOCK_NAME = ['매도호가', '매수호가', '단축코드']

# S3_
S3__IN_BLOCK_CODE = ['shcode']
S3__IN_BLOCK_NAME = ['단축코드']
S3__OUT_BLOCK_CODE = [
           'chetime', 'sign', 'change', 'drate', 'price', 'opentime', 'open', 'hightime', 'high', 'lowtime',
           'low', 'cgubun', 'cvolume', 'volume', 'value', 'mdvolume', 'mdchecnt', 'msvolume', 'mschecnt', 'cpower',
           'w_avrg', 'offerho', 'bidho', 'status', 'jnilvolume', 'shcode', 'exchname']
S3__OUT_BLOCK_NAME = [
           '체결시간', '전일대비구분', '전일대비', '등락율', '현재가', '시가시간', '시가', '고가시간', '고가', '저가시간',
           '저가', '체결구분', '체결량', '누적거래량', '누적거래대금', '매도누적체결량', '매도누적체결건수', '매수누적체결량', '매수누적체결건수', '체결강도',
           '가중평균가', '매도호가', '매수호가', '장정보', '전일동시간대거래량', '단축코드', '거래소명']

# S4_
S4__IN_BLOCK_CODE = ['shcode']
S4__IN_BLOCK_NAME = ['단축코드']
S4__OUT_BLOCK_CODE = [
           'sign', 'change', 'drate', 'price', 'opentime', 'open', 'hightime', 'high', 'lowtime', 'low',
           'shcode']
S4__OUT_BLOCK_NAME = [
           '전일대비구분', '전일대비', '등락율', '현재가', '시가시간', '시가', '고가시간', '고가', '저가시간', '저가',
           '단축코드']

# SC0
SC0_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'ordchegb', 'marketgb', 'ordgb',
           'orgordno', 'accno1', 'accno2', 'passwd', 'expcode', 'shtcode', 'hname', 'ordqty', 'ordprice', 'hogagb',
           'etfhogagb', 'pgmtype', 'gmhogagb', 'gmhogayn', 'singb', 'loandt', 'cvrgordtp', 'strtgcode', 'groupid', 'ordseqno',
           'prtno', 'basketno', 'trchno', 'itemno', 'brwmgmyn', 'mbrno', 'procgb', 'admbrchno', 'futaccno', 'futmarketgb',
           'tongsingb', 'lpgb', 'dummy', 'ordno', 'ordtm', 'prntordno', 'mgempno', 'orgordundrqty', 'orgordmdfyqty', 'ordordcancelqty',
           'nmcpysndno', 'ordamt', 'bnstp', 'spareordno', 'cvrgseqno', 'rsvordno', 'mtordseqno', 'spareordqty', 'orduserid', 'spotordqty',
           'ordruseqty', 'mnyordamt', 'ordsubstamt', 'ruseordamt', 'ordcmsnamt', 'crdtuseamt', 'secbalqty', 'spotordableqty', 'ordableruseqty', 'flctqty',
           'secbalqtyd2', 'sellableqty', 'unercsellordqty', 'avrpchsprc', 'pchsamt', 'deposit', 'substamt', 'csgnmnymgn', 'csgnsubstmgn', 'crdtpldgruseamt',
           'ordablemny', 'ordablesubstamt', 'ruseableamt']
SC0_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결구분', '시장구분', '주문구분',
           '원주문번호', '계좌번호', '계좌번호', '비밀번호', '종목번호', '단축종목번호', '종목명', '주문수량', '주문가격', '주문조건',
           '호가유형코드', '프로그램호가구분', '공매도호가구분', '공매도가능여부', '신용구분', '대출일', '반대매매주문구분', '전략코드', '그룹ID', '주문회차',
           '포트폴리오번호', '바스켓번호', '트렌치번호', '아아템번호', '차입구분', '회원사번호', '처리구분', '관리지점번호', '선물계좌번호', '선물상품구분',
           '통신매체구분', '유동성공급자구분', 'DUMMY', '주문번호', '주문시각', '모주문번호', '관리사원번호', '원주문미체결수량', '원주문정정수량', '원주문취소수량',
           '비회원사송신번호', '주문금액', '매매구분', '예비주문번호', '반대매매일련번호', '예약주문번호', '복수주문일련번호', '예비주문수량', '주문사원번호', '실물주문수량',
           '재사용주문수량', '현금주문금액', '주문대용금액', '재사용주문금액', '수수료주문금액', '사용신용담보재사용금', '잔고수량', '실물가능수량', '재사용가능수량(매도)', '변동수량',
           '잔고수량(D2)', '매도주문가능수량', '미체결매도주문수량', '평균매입가', '매입금액', '예수금', '대용금', '위탁증거금현금', '위탁증거금대용', '신용담보재사용금',
           '주문가능현금', '주문가능대용', '재사용가능금액']

# SC1
SC1_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'ordxctptncode', 'ordmktcode', 'ordptncode',
           'mgmtbrnno', 'accno1', 'accno2', 'acntnm', 'Isuno', 'Isunm', 'ordno', 'orgordno', 'execno', 'ordqty',
           'ordprc', 'execqty', 'execprc', 'mdfycnfqty', 'mdfycnfprc', 'canccnfqty', 'rjtqty', 'ordtrxptncode', 'mtiordseqno', 'ordcndi',
           'ordprcptncode', 'nsavtrdqty', 'shtnIsuno', 'opdrtnno', 'cvrgordtp', 'unercqty', 'orgordunercqty', 'orgordmdfyqty', 'orgordcancqty', 'ordavrexecprc',
           'ordamt', 'stdIsuno', 'bfstdIsuno', 'bnstp', 'ordtrdptncode', 'mgntrncode', 'adduptp', 'commdacode', 'Loandt', 'mbrnmbrno',
           'ordacntno', 'agrgbrnno', 'mgempno', 'futsLnkbrnno', 'futsLnkacntno', 'futsmkttp', 'regmktcode', 'mnymgnrat', 'substmgnrat', 'mnyexecamt',
           'ubstexecamt', 'cmsnamtexecamt', 'crdtpldgexecamt', 'crdtexecamt', 'prdayruseexecval', 'crdayruseexecval', 'spotexecqty', 'stslexecqty', 'strtgcode', 'grpId',
           'ordseqno', 'ptflno', 'bskno', 'trchno', 'itemno', 'orduserId', 'brwmgmtYn', 'frgrunqno', 'trtzxLevytp', 'lptp',
           'exectime', 'rcptexectime', 'rmndLoanamt', 'secbalqty', 'spotordableqty', 'ordableruseqty', 'flctqty', 'secbalqtyd2', 'sellableqty', 'unercsellordqty',
           'avrpchsprc', 'pchsant', 'deposit', 'substamt', 'csgnmnymgn', 'csgnsubstmgn', 'crdtpldgruseamt', 'ordablemny', 'ordablesubstamt', 'ruseableamt']
SC1_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '주문수량',
           '주문가격', '체결수량', '체결가격', '정정확인수량', '정정확인가격', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '비저축체결수량', '단축종목번호', '운용지시번호', '반대매매주문구분', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가격',
           '주문금액', '표준종목번호', '전표준종목번호', '매매구분', '주문거래유형코드', '신용거래코드', '수수료합산코드', '통신매체코드', '대출일', '회원/비회원사번호',
           '주문계좌번호', '집계지점번호', '관리사원번호', '선물연계지점번호', '선물연계계좌번호', '선물시장구분', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액',
           '대용체결금액', '수수료체결금액', '신용담보체결금액', '신용체결금액', '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹Id',
           '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호', '주문자Id', '차입관리여부', '외국인고유번호', '거래세징수구분', '유동성공급자구분',
           '체결시각', '거래소수신체결시각', '잔여대출금액', '잔고수량', '실물가능수량', '재사용가능수량(매도)', '변동수량', '잔고수량(d2)', '매도주문가능수량', '미체결매도주문수량',
           '평균매입가', '매입금액', '예수금', '대용금', '위탁증거금현금', '위탁증거금대용', '신용담보재사용금', '주문가능현금', '주문가능대용', '재사용가능금액']

# SC2
SC2_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'ordxctptncode', 'ordmktcode', 'ordptncode',
           'mgmtbrnno', 'accno1', 'accno2', 'acntnm', 'Isuno', 'Isunm', 'ordno', 'orgordno', 'execno', 'ordqty',
           'ordprc', 'execqty', 'execprc', 'mdfycnfqty', 'mdfycnfprc', 'canccnfqty', 'rjtqty', 'ordtrxptncode', 'mtiordseqno', 'ordcndi',
           'ordprcptncode', 'nsavtrdqty', 'shtnIsuno', 'opdrtnno', 'cvrgordtp', 'unercqty', 'orgordunercqty', 'orgordmdfyqty', 'orgordcancqty', 'ordavrexecprc',
           'ordamt', 'stdIsuno', 'bfstdIsuno', 'bnstp', 'ordtrdptncode', 'mgntrncode', 'adduptp', 'commdacode', 'Loandt', 'mbrnmbrno',
           'ordacntno', 'agrgbrnno', 'mgempno', 'futsLnkbrnno', 'futsLnkacntno', 'futsmkttp', 'regmktcode', 'mnymgnrat', 'substmgnrat', 'mnyexecamt',
           'ubstexecamt', 'cmsnamtexecamt', 'crdtpldgexecamt', 'crdtexecamt', 'prdayruseexecval', 'crdayruseexecval', 'spotexecqty', 'stslexecqty', 'strtgcode', 'grpId',
           'ordseqno', 'ptflno', 'bskno', 'trchno', 'itemno', 'orduserId', 'brwmgmtYn', 'frgrunqno', 'trtzxLevytp', 'lptp',
           'exectime', 'rcptexectime', 'rmndLoanamt', 'secbalqty', 'spotordableqty', 'ordableruseqty', 'flctqty', 'secbalqtyd2', 'sellableqty', 'unercsellordqty',
           'avrpchsprc', 'pchsant', 'deposit', 'substamt', 'csgnmnymgn', 'csgnsubstmgn', 'crdtpldgruseamt', 'ordablemny', 'ordablesubstamt', 'ruseableamt']
SC2_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '주문수량',
           '주문가격', '체결수량', '체결가격', '정정확인수량', '정정확인가격', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '비저축체결수량', '단축종목번호', '운용지시번호', '반대매매주문구분', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가격',
           '주문금액', '표준종목번호', '전표준종목번호', '매매구분', '주문거래유형코드', '신용거래코드', '수수료합산코드', '통신매체코드', '대출일', '회원/비회원사번호',
           '주문계좌번호', '집계지점번호', '관리사원번호', '선물연계지점번호', '선물연계계좌번호', '선물시장구분', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액',
           '대용체결금액', '수수료체결금액', '신용담보체결금액', '신용체결금액', '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹Id',
           '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호', '주문자Id', '차입관리여부', '외국인고유번호', '거래세징수구분', '유동성공급자구분',
           '체결시각', '거래소수신체결시각', '잔여대출금액', '잔고수량', '실물가능수량', '재사용가능수량(매도)', '변동수량', '잔고수량(d2)', '매도주문가능수량', '미체결매도주문수량',
           '평균매입가', '매입금액', '예수금', '대용금', '위탁증거금현금', '위탁증거금대용', '신용담보재사용금', '주문가능현금', '주문가능대용', '재사용가능금액']

# SC3
SC3_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'ordxctptncode', 'ordmktcode', 'ordptncode',
           'mgmtbrnno', 'accno1', 'accno2', 'acntnm', 'Isuno', 'Isunm', 'ordno', 'orgordno', 'execno', 'ordqty',
           'ordprc', 'execqty', 'execprc', 'mdfycnfqty', 'mdfycnfprc', 'canccnfqty', 'rjtqty', 'ordtrxptncode', 'mtiordseqno', 'ordcndi',
           'ordprcptncode', 'nsavtrdqty', 'shtnIsuno', 'opdrtnno', 'cvrgordtp', 'unercqty', 'orgordunercqty', 'orgordmdfyqty', 'orgordcancqty', 'ordavrexecprc',
           'ordamt', 'stdIsuno', 'bfstdIsuno', 'bnstp', 'ordtrdptncode', 'mgntrncode', 'adduptp', 'commdacode', 'Loandt', 'mbrnmbrno',
           'ordacntno', 'agrgbrnno', 'mgempno', 'futsLnkbrnno', 'futsLnkacntno', 'futsmkttp', 'regmktcode', 'mnymgnrat', 'substmgnrat', 'mnyexecamt',
           'ubstexecamt', 'cmsnamtexecamt', 'crdtpldgexecamt', 'crdtexecamt', 'prdayruseexecval', 'crdayruseexecval', 'spotexecqty', 'stslexecqty', 'strtgcode', 'grpId',
           'ordseqno', 'ptflno', 'bskno', 'trchno', 'itemno', 'orduserId', 'brwmgmtYn', 'frgrunqno', 'trtzxLevytp', 'lptp',
           'exectime', 'rcptexectime', 'rmndLoanamt', 'secbalqty', 'spotordableqty', 'ordableruseqty', 'flctqty', 'secbalqtyd2', 'sellableqty', 'unercsellordqty',
           'avrpchsprc', 'pchsant', 'deposit', 'substamt', 'csgnmnymgn', 'csgnsubstmgn', 'crdtpldgruseamt', 'ordablemny', 'ordablesubstamt', 'ruseableamt']
SC3_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '주문수량',
           '주문가격', '체결수량', '체결가격', '정정확인수량', '정정확인가격', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '비저축체결수량', '단축종목번호', '운용지시번호', '반대매매주문구분', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가격',
           '주문금액', '표준종목번호', '전표준종목번호', '매매구분', '주문거래유형코드', '신용거래코드', '수수료합산코드', '통신매체코드', '대출일', '회원/비회원사번호',
           '주문계좌번호', '집계지점번호', '관리사원번호', '선물연계지점번호', '선물연계계좌번호', '선물시장구분', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액',
           '대용체결금액', '수수료체결금액', '신용담보체결금액', '신용체결금액', '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹Id',
           '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호', '주문자Id', '차입관리여부', '외국인고유번호', '거래세징수구분', '유동성공급자구분',
           '체결시각', '거래소수신체결시각', '잔여대출금액', '잔고수량', '실물가능수량', '재사용가능수량(매도)', '변동수량', '잔고수량(d2)', '매도주문가능수량', '미체결매도주문수량',
           '평균매입가', '매입금액', '예수금', '대용금', '위탁증거금현금', '위탁증거금대용', '신용담보재사용금', '주문가능현금', '주문가능대용', '재사용가능금액']

# SC4
SC4_OUT_BLOCK_CODE = [
           'lineseq', 'accno', 'user', 'len', 'gubun', 'compress', 'encrypt', 'offset', 'trcode', 'comid',
           'userid', 'media', 'ifid', 'seq', 'trid', 'pubip', 'prvip', 'pcbpno', 'bpno', 'termno',
           'lang', 'proctm', 'msgcode', 'outgu', 'compreq', 'funckey', 'reqcnt', 'filler', 'cont', 'contkey',
           'varlen', 'varhdlen', 'varmsglen', 'trsrc', 'eventid', 'ifinfo', 'filler1', 'ordxctptncode', 'ordmktcode', 'ordptncode',
           'mgmtbrnno', 'accno1', 'accno2', 'acntnm', 'Isuno', 'Isunm', 'ordno', 'orgordno', 'execno', 'ordqty',
           'ordprc', 'execqty', 'execprc', 'mdfycnfqty', 'mdfycnfprc', 'canccnfqty', 'rjtqty', 'ordtrxptncode', 'mtiordseqno', 'ordcndi',
           'ordprcptncode', 'nsavtrdqty', 'shtnIsuno', 'opdrtnno', 'cvrgordtp', 'unercqty', 'orgordunercqty', 'orgordmdfyqty', 'orgordcancqty', 'ordavrexecprc',
           'ordamt', 'stdIsuno', 'bfstdIsuno', 'bnstp', 'ordtrdptncode', 'mgntrncode', 'adduptp', 'commdacode', 'Loandt', 'mbrnmbrno',
           'ordacntno', 'agrgbrnno', 'mgempno', 'futsLnkbrnno', 'futsLnkacntno', 'futsmkttp', 'regmktcode', 'mnymgnrat', 'substmgnrat', 'mnyexecamt',
           'ubstexecamt', 'cmsnamtexecamt', 'crdtpldgexecamt', 'crdtexecamt', 'prdayruseexecval', 'crdayruseexecval', 'spotexecqty', 'stslexecqty', 'strtgcode', 'grpId',
           'ordseqno', 'ptflno', 'bskno', 'trchno', 'itemno', 'orduserId', 'brwmgmtYn', 'frgrunqno', 'trtzxLevytp', 'lptp',
           'exectime', 'rcptexectime', 'rmndLoanamt', 'secbalqty', 'spotordableqty', 'ordableruseqty', 'flctqty', 'secbalqtyd2', 'sellableqty', 'unercsellordqty',
           'avrpchsprc', 'pchsant', 'deposit', 'substamt', 'csgnmnymgn', 'csgnsubstmgn', 'crdtpldgruseamt', 'ordablemny', 'ordablesubstamt', 'ruseableamt']
SC4_OUT_BLOCK_NAME = [
           '라인일련번호', '계좌번호', '조작자ID', '헤더길이', '헤더구분', '압축구분', '암호구분', '공통시작지점', 'TRCODE', '이용사번호',
           '사용자ID', '접속매체', 'I/F일련번호', '전문일련번호', 'TR추적ID', '공인IP', '사설IP', '처리지점번호', '지점번호', '단말번호',
           '언어구분', 'AP처리시간', '메세지코드', '메세지출력구분', '압축요청구분', '기능키', '요청레코드개수', '예비영역', '연속구분', '연속키값',
           '가변시스템길이', '가변해더길이', '가변메시지길이', '조회발원지', 'I/F이벤트ID', 'I/F정보', '예비영역', '주문체결유형코드', '주문시장코드', '주문유형코드',
           '관리지점번호', '계좌번호', '계좌번호', '계좌명', '종목번호', '종목명', '주문번호', '원주문번호', '체결번호', '주문수량',
           '주문가격', '체결수량', '체결가격', '정정확인수량', '정정확인가격', '취소확인수량', '거부수량', '주문처리유형코드', '복수주문일련번호', '주문조건',
           '호가유형코드', '비저축체결수량', '단축종목번호', '운용지시번호', '반대매매주문구분', '미체결수량(주문)', '원주문미체결수량', '원주문정정수량', '원주문취소수량', '주문평균체결가격',
           '주문금액', '표준종목번호', '전표준종목번호', '매매구분', '주문거래유형코드', '신용거래코드', '수수료합산코드', '통신매체코드', '대출일', '회원/비회원사번호',
           '주문계좌번호', '집계지점번호', '관리사원번호', '선물연계지점번호', '선물연계계좌번호', '선물시장구분', '등록시장코드', '현금증거금률', '대용증거금률', '현금체결금액',
           '대용체결금액', '수수료체결금액', '신용담보체결금액', '신용체결금액', '전일재사용체결금액', '금일재사용체결금액', '실물체결수량', '공매도체결수량', '전략코드', '그룹Id',
           '주문회차', '포트폴리오번호', '바스켓번호', '트렌치번호', '아이템번호', '주문자Id', '차입관리여부', '외국인고유번호', '거래세징수구분', '유동성공급자구분',
           '체결시각', '거래소수신체결시각', '잔여대출금액', '잔고수량', '실물가능수량', '재사용가능수량(매도)', '변동수량', '잔고수량(d2)', '매도주문가능수량', '미체결매도주문수량',
           '평균매입가', '매입금액', '예수금', '대용금', '위탁증거금현금', '위탁증거금대용', '신용담보재사용금', '주문가능현금', '주문가능대용', '재사용가능금액']

# SHC
SHC_IN_BLOCK_CODE = ['updnlmtgubun']
SHC_IN_BLOCK_NAME = ['상/하한구분']
SHC_OUT_BLOCK_CODE = [
           'sijanggubun', 'hname', 'price', 'sign', 'change', 'drate', 'volume', 'volincrate', 'updnlmtprice', 'updnlmtdrate',
           'jnilvolume', 'shcode', 'gwangubun', 'undergubun', 'tgubun', 'wgubun', 'dishonest', 'jkrate', 'updnlmtdaycnt']
SHC_OUT_BLOCK_NAME = [
           '거래소/코스닥구분', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래증가율', '상/하한가', '상/하한가대비율',
           '전일거래량', '단축코드', '관리구분', '이상급등구분', '투자유의구분', '우선주구분', '불성실구분', '증거금률', '상한가/하한가연속일수']

# SHD
SHD_IN_BLOCK_CODE = ['updnlmtgubun']
SHD_IN_BLOCK_NAME = ['상/하한구분']
SHD_OUT_BLOCK_CODE = [
           'sijanggubun', 'hname', 'price', 'sign', 'change', 'drate', 'volume', 'volincrate', 'updnlmtprice', 'updnlmtdrate',
           'jnilvolume', 'shcode', 'gwangubun', 'undergubun', 'tgubun', 'wgubun', 'dishonest', 'jkrate']
SHD_OUT_BLOCK_NAME = [
           '거래소/코스닥구분', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래증가율', '상/하한가', '상/하한가대비율',
           '전일거래량', '단축코드', '관리구분', '이상급등구분', '투자유의구분', '우선주구분', '불성실구분', '증거금률']

# SHI
SHI_IN_BLOCK_CODE = ['updnlmtgubun']
SHI_IN_BLOCK_NAME = ['상/하한구분']
SHI_OUT_BLOCK_CODE = [
           'sijanggubun', 'hname', 'price', 'sign', 'change', 'drate', 'volume', 'volincrate', 'totofferrem', 'totbidrem',
           'updnlmtstime', 'updnlmtdaycnt', 'jnilvolume', 'shcode', 'gwangubun', 'undergubun', 'tgubun', 'wgubun', 'dishonest', 'jkrate']
SHI_OUT_BLOCK_NAME = [
           '거래소/코스닥구분', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래증가율', '매도호가총수량', '매수호가총수량',
           '상한가/하한가최종진입시간', '상한가/하한가연속일수', '전일거래량', '단축코드', '관리구분', '이상급등구분', '투자유의구분', '우선주구분', '불성실구분', '증거금률']

# SHO
SHO_IN_BLOCK_CODE = ['updnlmtgubun']
SHO_IN_BLOCK_NAME = ['상/하한구분']
SHO_OUT_BLOCK_CODE = [
           'sijanggubun', 'hname', 'price', 'sign', 'change', 'drate', 'volume', 'volincrate', 'updnlmtprice', 'updnlmtchange',
           'updnlmtdrate', 'jnilvolume', 'shcode', 'gwangubun', 'undergubun', 'tgubun', 'wgubun', 'dishonest', 'jkrate']
SHO_OUT_BLOCK_NAME = [
           '거래소/코스닥구분', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래증가율', '상/하한가', '상/하한가대비',
           '상/하한가대비율', '전일거래량', '단축코드', '관리구분', '이상급등구분', '투자유의구분', '우선주구분', '불성실구분', '증거금률']

# UBM
UBM_IN_BLOCK_CODE = ['ex_upcode']
UBM_IN_BLOCK_NAME = ['거래소별업종코드']
UBM_OUT_BLOCK_CODE = [
           'tjjcode', 'tjjtime', 'msvolume', 'mdvolume', 'msvol', 'p_msvol', 'msvalue', 'mdvalue', 'msval', 'p_msval',
           'upcode', 'ex_upcode']
UBM_OUT_BLOCK_NAME = [
           '투자자코드', '수신시간', '매수거래량', '매도거래량', '거래량순매수', '거래량순매수직전대비', '매수거래대금', '매도거래대금', '거래대금순매수', '거래대금순매수직전대비',
           '업종코드', '거래소별업종코드']

# UBT
UBT_IN_BLOCK_CODE = ['ex_upcode']
UBT_IN_BLOCK_NAME = ['거래소별업종코드']
UBT_OUT_BLOCK_CODE = [
           'tjjtime', 'tjjcode1', 'msvolume1', 'mdvolume1', 'msvol1', 'msvalue1', 'mdvalue1', 'msval1', 'tjjcode2', 'msvolume2',
           'mdvolume2', 'msvol2', 'msvalue2', 'mdvalue2', 'msval2', 'tjjcode3', 'msvolume3', 'mdvolume3', 'msvol3', 'msvalue3',
           'mdvalue3', 'msval3', 'tjjcode4', 'msvolume4', 'mdvolume4', 'msvol4', 'msvalue4', 'mdvalue4', 'msval4', 'tjjcode5',
           'msvolume5', 'mdvolume5', 'msvol5', 'msvalue5', 'mdvalue5', 'msval5', 'tjjcode6', 'msvolume6', 'mdvolume6', 'msvol6',
           'msvalue6', 'mdvalue6', 'msval6', 'tjjcode7', 'msvolume7', 'mdvolume7', 'msvol7', 'msvalue7', 'mdvalue7', 'msval7',
           'tjjcode8', 'msvolume8', 'mdvolume8', 'msvol8', 'msvalue8', 'mdvalue8', 'msval8', 'tjjcode9', 'msvolume9', 'mdvolume9',
           'msvol9', 'msvalue9', 'mdvalue9', 'msval9', 'tjjcode10', 'msvolume10', 'mdvolume10', 'msvol10', 'msvalue10', 'mdvalue10',
           'msval10', 'tjjcode11', 'msvolume11', 'mdvolume11', 'msvol11', 'msvalue11', 'mdvalue11', 'msval11', 'upcode', 'tjjcode0',
           'msvolume0', 'mdvolume0', 'msvol0', 'msvalue0', 'mdvalue0', 'msval0', 'ex_upcode']
UBT_OUT_BLOCK_NAME = [
           '수신시간', '투자자코드1(개인)', '매수거래량1', '매도거래량1', '거래량순매수1', '매수거래대금1', '매도거래대금1', '거래대금순매수1', '투자자코드2(외국인)', '매수거래량2',
           '매도거래량2', '거래량순매수2', '매수거래대금2', '매도거래대금2', '거래대금순매수2', '투자자코드3(기관계)', '매수거래량3', '매도거래량3', '거래량순매수3', '매수거래대금3',
           '매도거래대금3', '거래대금순매수3', '투자자코드4(증권)', '매수거래량4', '매도거래량4', '거래량순매수4', '매수거래대금4', '매도거래대금4', '거래대금순매수4', '투자자코드5(투신)',
           '매수거래량5', '매도거래량5', '거래량순매수5', '매수거래대금5', '매도거래대금5', '거래대금순매수5', '투자자코드6(은행)', '매수거래량6', '매도거래량6', '거래량순매수6',
           '매수거래대금6', '매도거래대금6', '거래대금순매수6', '투자자코드7(보험)', '매수거래량7', '매도거래량7', '거래량순매수7', '매수거래대금7', '매도거래대금7', '거래대금순매수7',
           '투자자코드8(종금)', '매수거래량8', '매도거래량8', '거래량순매수8', '매수거래대금8', '매도거래대금8', '거래대금순매수8', '투자자코드9(기금)', '매수거래량9', '매도거래량9',
           '거래량순매수9', '매수거래대금9', '매도거래대금9', '거래대금순매수9', '투자자코드10(선물업자)', '매수거래량10', '매도거래량10', '거래량순매수10', '매수거래대금10', '매도거래대금10',
           '거래대금순매수10', '투자자코드11(기타)', '매수거래량11', '매도거래량11', '거래량순매수11', '매수거래대금11', '매도거래대금11', '거래대금순매수11', '업종코드', '투자자코드0(사모펀드)',
           '매수거래량0', '매도거래량0', '거래량순매수0', '매수거래대금0', '매도거래대금0', '거래대금순매수0', '거래소별업종코드']

# UH1
UH1_IN_BLOCK_CODE = ['ex_shcode']
UH1_IN_BLOCK_NAME = ['거래소별단축코드']
UH1_OUT_BLOCK_CODE = [
           'hotime', 'offerho1', 'bidho1', 'krx_offerrem1', 'nxt_offerrem1', 'unt_offerrem1', 'krx_bidrem1', 'nxt_bidrem1', 'unt_bidrem1', 'offerho2',
           'bidho2', 'krx_offerrem2', 'nxt_offerrem2', 'unt_offerrem2', 'krx_bidrem2', 'nxt_bidrem2', 'unt_bidrem2', 'offerho3', 'bidho3', 'krx_offerrem3',
           'nxt_offerrem3', 'unt_offerrem3', 'krx_bidrem3', 'nxt_bidrem3', 'unt_bidrem3', 'offerho4', 'bidho4', 'krx_offerrem4', 'nxt_offerrem4', 'unt_offerrem4',
           'krx_bidrem4', 'nxt_bidrem4', 'unt_bidrem4', 'offerho5', 'bidho5', 'krx_offerrem5', 'nxt_offerrem5', 'unt_offerrem5', 'krx_bidrem5', 'nxt_bidrem5',
           'unt_bidrem5', 'offerho6', 'bidho6', 'krx_offerrem6', 'nxt_offerrem6', 'unt_offerrem6', 'krx_bidrem6', 'nxt_bidrem6', 'unt_bidrem6', 'offerho7',
           'bidho7', 'krx_offerrem7', 'nxt_offerrem7', 'unt_offerrem7', 'krx_bidrem7', 'nxt_bidrem7', 'unt_bidrem7', 'offerho8', 'bidho8', 'krx_offerrem8',
           'nxt_offerrem8', 'unt_offerrem8', 'krx_bidrem8', 'nxt_bidrem8', 'unt_bidrem8', 'offerho9', 'bidho9', 'krx_offerrem9', 'nxt_offerrem9', 'unt_offerrem9',
           'krx_bidrem9', 'nxt_bidrem9', 'unt_bidrem9', 'offerho10', 'bidho10', 'krx_offerrem10', 'nxt_offerrem10', 'unt_offerrem10', 'krx_bidrem10', 'nxt_bidrem10',
           'unt_bidrem10', 'krx_totofferrem', 'nxt_totofferrem', 'unt_totofferrem', 'krx_totbidrem', 'nxt_totbidrem', 'unt_totbidrem', 'krx_donsigubun', 'nxt_donsigubun', 'shcode',
           'alloc_gubun', 'volume', 'krx_midprice', 'krx_offermidsumrem', 'krx_bidmidsumrem', 'nxt_midprice', 'nxt_offermidsumrem', 'nxt_bidmidsumrem', 'krx_midsumrem', 'krx_midsumremgubun',
           'nxt_midsumrem', 'nxt_midsumremgubun', 'ex_shcode']
UH1_OUT_BLOCK_NAME = [
           '호가시간', '매도호가1', '매수호가1', 'KRX매도호가잔량1', 'NXT매도호가잔량1', '통합매도호가잔량1', 'KRX매수호가잔량1', 'NXT매수호가잔량1', '통합매수호가잔량1', '매도호가2',
           '매수호가2', 'KRX매도호가잔량2', 'NXT매도호가잔량2', '통합매도호가잔량2', 'KRX매수호가잔량2', 'NXT매수호가잔량2', '통합매수호가잔량2', '매도호가3', '매수호가3', 'KRX매도호가잔량3',
           'NXT매도호가잔량3', '통합매도호가잔량3', 'KRX매수호가잔량3', 'NXT매수호가잔량3', '통합매수호가잔량3', '매도호가4', '매수호가4', 'KRX매도호가잔량4', 'NXT매도호가잔량4', '통합매도호가잔량4',
           'KRX매수호가잔량4', 'NXT매수호가잔량4', '통합매수호가잔량4', '매도호가5', '매수호가5', 'KRX매도호가잔량5', 'NXT매도호가잔량5', '통합매도호가잔량5', 'KRX매수호가잔량5', 'NXT매수호가잔량5',
           '통합매수호가잔량5', '매도호가6', '매수호가6', 'KRX매도호가잔량6', 'NXT매도호가잔량6', '통합매도호가잔량6', 'KRX매수호가잔량6', 'NXT매수호가잔량6', '통합매수호가잔량6', '매도호가7',
           '매수호가7', 'KRX매도호가잔량7', 'NXT매도호가잔량7', '통합매도호가잔량7', 'KRX매수호가잔량7', 'NXT매수호가잔량7', '통합매수호가잔량7', '매도호가8', '매수호가8', 'KRX매도호가잔량8',
           'NXT매도호가잔량8', '통합매도호가잔량8', 'KRX매수호가잔량8', 'NXT매수호가잔량8', '통합매수호가잔량8', '매도호가9', '매수호가9', 'KRX매도호가잔량9', 'NXT매도호가잔량9', '통합매도호가잔량9',
           'KRX매수호가잔량9', 'NXT매수호가잔량9', '통합매수호가잔량9', '매도호가10', '매수호가10', 'KRX매도호가잔량10', 'NXT매도호가잔량10', '통합매도호가잔량10', 'KRX매수호가잔량10', 'NXT매수호가잔량10',
           '통합매수호가잔량10', 'KRX총매도호가잔량', 'NXT총매도호가잔량', '통합총매도호가잔량', 'KRX총매수호가잔량', 'NXT총매수호가잔량', '통합총매수호가잔량', 'KRX동시호가구분', 'NXT동시호가구분', '단축코드',
           '배분적용구분', '누적거래량', 'KRX중간가격', 'KRX매도중간가잔량합계수량', 'KRX매수중간가잔량합계수량', 'NXT중간가격', 'NXT매도중간가잔량합계수량', 'NXT매수중간가잔량합계수량', 'KRX중간가잔량합계수량', "KRX중간가잔량구분('없음'1'매도'2'매수)",
           'NXT중간가잔량합계수량', "NXT중간가잔량구분('없음'1'매도'2'매수)", '거래소별단축코드']

# UK1
UK1_IN_BLOCK_CODE = ['ex_shcode']
UK1_IN_BLOCK_NAME = ['거래소별단축코드']
UK1_OUT_BLOCK_CODE = [
           'offerno1', 'bidno1', 'offertrad1', 'bidtrad1', 'tradmdvol1', 'tradmsvol1', 'tradmdrate1', 'tradmsrate1', 'tradmdcha1', 'tradmscha1',
           'offerno2', 'bidno2', 'offertrad2', 'bidtrad2', 'tradmdvol2', 'tradmsvol2', 'tradmdrate2', 'tradmsrate2', 'tradmdcha2', 'tradmscha2',
           'offerno3', 'bidno3', 'offertrad3', 'bidtrad3', 'tradmdvol3', 'tradmsvol3', 'tradmdrate3', 'tradmsrate3', 'tradmdcha3', 'tradmscha3',
           'offerno4', 'bidno4', 'offertrad4', 'bidtrad4', 'tradmdvol4', 'tradmsvol4', 'tradmdrate4', 'tradmsrate4', 'tradmdcha4', 'tradmscha4',
           'offerno5', 'bidno5', 'offertrad5', 'bidtrad5', 'tradmdvol5', 'tradmsvol5', 'tradmdrate5', 'tradmsrate5', 'tradmdcha5', 'tradmscha5',
           'ftradmdvol', 'ftradmsvol', 'ftradmdrate', 'ftradmsrate', 'ftradmdcha', 'ftradmscha', 'shcode', 'tradmdval1', 'tradmsval1', 'tradmdavg1',
           'tradmsavg1', 'tradmdval2', 'tradmsval2', 'tradmdavg2', 'tradmsavg2', 'tradmdval3', 'tradmsval3', 'tradmdavg3', 'tradmsavg3', 'tradmdval4',
           'tradmsval4', 'tradmdavg4', 'tradmsavg4', 'tradmdval5', 'tradmsval5', 'tradmdavg5', 'tradmsavg5', 'ftradmdval', 'ftradmsval', 'ftradmdavg',
           'ftradmsavg', 'time', 'exchname', 'ex_shcode']
UK1_OUT_BLOCK_NAME = [
           '매도증권사코드1', '매수증권사코드1', '매도회원사명1', '매수회원사명1', '매도거래량1', '매수거래량1', '매도거래량비중1', '매수거래량비중1', '매도거래량직전대비1', '매수거래량직전대비1',
           '매도증권사코드2', '매수증권사코드2', '매도회원사명2', '매수회원사명2', '매도거래량2', '매수거래량2', '매도거래량비중2', '매수거래량비중2', '매도거래량직전대비2', '매수거래량직전대비2',
           '매도증권사코드3', '매수증권사코드3', '매도회원사명3', '매수회원사명3', '매도거래량3', '매수거래량3', '매도거래량비중3', '매수거래량비중3', '매도거래량직전대비3', '매수거래량직전대비3',
           '매도증권사코드4', '매수증권사코드4', '매도회원사명4', '매수회원사명4', '매도거래량4', '매수거래량4', '매도거래량비중4', '매수거래량비중4', '매도거래량직전대비4', '매수거래량직전대비4',
           '매도증권사코드5', '매수증권사코드5', '매도회원사명5', '매수회원사명5', '매도거래량5', '매수거래량5', '매도거래량비중5', '매수거래량비중5', '매도거래량직전대비5', '매수거래량직전대비5',
           '외국계증권사매도합계', '외국계증권사매수합계', '외국계증권사매도거래량비중', '외국계증권사매수거래량비중', '외국계증권사매도거래량직전대비', '외국계증권사매수거래량직전대비', '단축코드', '매도거래대금1', '매수거래대금1', '매도평균단가1',
           '매수평균단가1', '매도거래대금2', '매수거래대금2', '매도평균단가2', '매수평균단가2', '매도거래대금3', '매수거래대금3', '매도평균단가3', '매수평균단가3', '매도거래대금4',
           '매수거래대금4', '매도평균단가4', '매수평균단가4', '매도거래대금5', '매수거래대금5', '매도평균단가5', '매수평균단가5', '외국계증권사매도거래대금', '외국계증권사매수거래대금', '외국계증권사매도평균단가',
           '외국계증권사매수평균단가', '수신시간', '거래소명', '거래소별단축코드']

# UPH
UPH_IN_BLOCK_CODE = ['ex_shcode']
UPH_IN_BLOCK_NAME = ['거래소별단축코드']
UPH_OUT_BLOCK_CODE = [
           'time', 'price', 'sign', 'change', 'volume', 'drate', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem',
           'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'dwcvolume', 'swcvolume', 'djcvolume', 'sjcvolume', 'tdvolume', 'tsvolume',
           'tvol', 'dwcvalue', 'swcvalue', 'djcvalue', 'sjcvalue', 'tdvalue', 'tsvalue', 'tval', 'pdgvolume', 'psgvolume',
           'shcode', 'ex_shcode']
UPH_OUT_BLOCK_NAME = [
           '수신시간', '현재가', '전일대비구분', '전일대비', '누적거래량', '등락율', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량',
           '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체매도체결수량', '전체매수체결수량',
           '전체순매수수량', '전체매도위탁체결금액', '전체매수위탁체결금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체매도체결금액', '전체매수체결금액', '전체순매수금액', '매도사전공시수량', '매수사전공시수량',
           '종목코드', '거래소별단축코드']

# UPM
UPM_IN_BLOCK_CODE = ['ex_gubun']
UPM_IN_BLOCK_NAME = ['거래소별구분값']
UPM_OUT_BLOCK_CODE = [
           'time', 'cdhrem', 'cshrem', 'bdhrem', 'bshrem', 'cdhvolume', 'cshvolume', 'bdhvolume', 'bshvolume', 'cdwvolume',
           'cdjvolume', 'cswvolume', 'csjvolume', 'cwvol', 'cjvol', 'bdwvolume', 'bdjvolume', 'bswvolume', 'bsjvolume', 'bwvol',
           'bjvol', 'dwvolume', 'swvolume', 'wvol', 'djvolume', 'sjvolume', 'jvol', 'cdwvalue', 'cdjvalue', 'cswvalue',
           'csjvalue', 'cwval', 'cjval', 'bdwvalue', 'bdjvalue', 'bswvalue', 'bsjvalue', 'bwval', 'bjval', 'dwvalue',
           'swvalue', 'wval', 'djvalue', 'sjvalue', 'jval', 'k200jisu', 'k200sign', 'change', 'k200basis', 'cdvolume',
           'csvolume', 'cvol', 'bdvolume', 'bsvolume', 'bvol', 'tdvolume', 'tsvolume', 'tvol', 'cdvalue', 'csvalue',
           'cval', 'bdvalue', 'bsvalue', 'bval', 'tdvalue', 'tsvalue', 'tval', 'p_cdvolcha', 'p_csvolcha', 'p_cvolcha',
           'p_bdvolcha', 'p_bsvolcha', 'p_bvolcha', 'p_tdvolcha', 'p_tsvolcha', 'p_tvolcha', 'p_cdvalcha', 'p_csvalcha', 'p_cvalcha', 'p_bdvalcha',
           'p_bsvalcha', 'p_bvalcha', 'p_tdvalcha', 'p_tsvalcha', 'p_tvalcha', 'gubun', 'ex_gubun']
UPM_OUT_BLOCK_NAME = [
           '수신시간', '차익매도호가잔량', '차익매수호가잔량', '비차익매도호가잔량', '비차익매수호가잔량', '차익매도호가수량', '차익매수호가수량', '비차익매도호가수량', '비차익매수호가수량', '차익매도위탁체결수량',
           '차익매도자기체결수량', '차익매수위탁체결수량', '차익매수자기체결수량', '차익위탁순매수수량', '차익자기순매수수량', '비차익매도위탁체결수량', '비차익매도자기체결수량', '비차익매수위탁체결수량', '비차익매수자기체결수량', '비차익위탁순매수수량',
           '비차익자기순매수수량', '전체매도위탁체결수량', '전체매수위탁체결수량', '전체위탁순매수수량', '전체매도자기체결수량', '전체매수자기체결수량', '전체자기순매수수량', '차익매도위탁체결금액', '차익매도자기체결금액', '차익매수위탁체결금액',
           '차익매수자기체결금액', '차익위탁순매수금액', '차익자기순매수금액', '비차익매도위탁체결금액', '비차익매도자기체결금액', '비차익매수위탁체결금액', '비차익매수자기체결금액', '비차익위탁순매수금액', '비차익자기순매수금액', '전체매도위탁체결금액',
           '전체매수위탁체결금액', '전체위탁순매수금액', '전체매도자기체결금액', '전체매수자기체결금액', '전체자기순매수금액', 'KOSPI200지수', 'KOSPI200전일대비구분', 'KOSPI200전일대비', 'KOSPI200베이시스', '차익매도체결수량합계',
           '차익매수체결수량합계', '차익순매수수량합계', '비차익매도체결수량합계', '비차익매수체결수량합계', '비차익순매수수량합계', '전체매도체결수량합계', '전체매수체결수량합계', '전체순매수수량합계', '차익매도체결금액합계', '차익매수체결금액합계',
           '차익순매수금액합계', '비차익매도체결금액합계', '비차익매수체결금액합계', '비차익순매수금액합계', '전체매도체결금액합계', '전체매수체결금액합계', '전체순매수금액합계', '차익매도체결수량직전대비', '차익매수체결수량직전대비', '차익순매수수량직전대비',
           '비차익매도체결수량직전대비', '비차익매수체결수량직전대비', '비차익순매수수량직전대비', '전체매도체결수량직전대비', '전체매수체결수량직전대비', '전체순매수수량직전대비', '차익매도체결금액직전대비', '차익매수체결금액직전대비', '차익순매수금액직전대비', '비차익매도체결금액직전대비',
           '비차익매수체결금액직전대비', '비차익순매수금액직전대비', '전체매도체결금액직전대비', '전체매수체결금액직전대비', '전체순매수금액직전대비', '구분값', '거래소별구분값']

# US2
US2_IN_BLOCK_CODE = ['ex_shcode']
US2_IN_BLOCK_NAME = ['거래소별단축코드']
US2_OUT_BLOCK_CODE = ['offerho', 'bidho', 'shcode', 'ex_shcode']
US2_OUT_BLOCK_NAME = ['매도호가', '매수호가', '단축코드', '거래소별단축코드']

# US3
US3_IN_BLOCK_CODE = ['ex_shcode']
US3_IN_BLOCK_NAME = ['거래소별단축코드']
US3_OUT_BLOCK_CODE = [
           'chetime', 'sign', 'change', 'drate', 'price', 'opentime', 'open', 'hightime', 'high', 'lowtime',
           'low', 'cgubun', 'cvolume', 'volume', 'value', 'mdvolume', 'mdchecnt', 'msvolume', 'mschecnt', 'cpower',
           'w_avrg', 'offerho', 'bidho', 'status', 'jnilvolume', 'shcode', 'exchname', 'ex_shcode']
US3_OUT_BLOCK_NAME = [
           '체결시간', '전일대비구분', '전일대비', '등락율', '현재가', '시가시간', '시가', '고가시간', '고가', '저가시간',
           '저가', '체결구분', '체결량', '누적거래량', '누적거래대금', '매도누적체결량', '매도누적체결건수', '매수누적체결량', '매수누적체결건수', '체결강도',
           '가중평균가', '매도호가', '매수호가', '장정보', '전일동시간대거래량', '단축코드', '거래소명', '거래소별단축코드']

# UVI
UVI_IN_BLOCK_CODE = ['ex_shcode']
UVI_IN_BLOCK_NAME = ['거래소별단축코드']
UVI_OUT_BLOCK_CODE = [
           'krx_vi_gubun', 'krx_svi_recprice', 'krx_dvi_recprice', 'krx_vi_trgprice', 'krx_time', 'nxt_vi_gubun', 'nxt_svi_recprice', 'nxt_dvi_recprice', 'nxt_vi_trgprice', 'nxt_time',
           'shcode', 'ref_shcode', 'exchname', 'ex_shcode']
UVI_OUT_BLOCK_NAME = [
           'KRXVI구분(0:해제1:정적발동2:동적발동3:정적&동적)', 'KRX정적VI발동기준가격', 'KRX동적VI발동기준가격', 'KRXVI발동가격', 'KRX시간', 'NXTVI구분(0:해제1:정적발동2:동적발동3:정적&동적)', 'NXT정적VI발동기준가격', 'NXT동적VI발동기준가격', 'NXTVI발동가격', 'NXT시간',
           '단축코드', '참조코드(미사용)', '거래소명', '거래소별단축코드']

# UYS
UYS_IN_BLOCK_CODE = ['ex_shcode']
UYS_IN_BLOCK_NAME = ['거래소별단축코드']
UYS_OUT_BLOCK_CODE = [
           'hotime', 'yeprice', 'yevolume', 'jnilysign', 'jnilchange', 'jnilydrate', 'yofferho0', 'ybidho0', 'yofferrem0', 'ybidrem0',
           'shcode', 'exchname', 'ex_shcode']
UYS_OUT_BLOCK_NAME = [
           '호가시간', '예상체결가격', '예상체결수량', '예상체결가전일종가대비구분', '예상체결가전일종가대비', '예상체결가전일종가등락율', '예상매도호가', '예상매수호가', '예상매도호가수량', '예상매수호가수량',
           '단축코드', '거래소명', '거래소별단축코드']

# VI_
VI__IN_BLOCK_CODE = ['shcode']
VI__IN_BLOCK_NAME = ['단축코드(KEY)']
VI__OUT_BLOCK_CODE = [
           'vi_gubun', 'svi_recprice', 'dvi_recprice', 'vi_trgprice', 'shcode', 'ref_shcode', 'time', 'exchname']
VI__OUT_BLOCK_NAME = [
           '구분(0:해제1:정적발동2:동적발동3:정적&동적)', '정적VI발동기준가격', '동적VI발동기준가격', 'VI발동가격', '단축코드(KEY)', '참조코드(미사용)', '시간', '거래소명']

# YJ_
YJ__IN_BLOCK_CODE = ['upcode']
YJ__IN_BLOCK_NAME = ['업종코드']
YJ__OUT_BLOCK_CODE = [
           'time', 'jisu', 'sign', 'change', 'drate', 'cvolume', 'volume', 'value', 'upcode']
YJ__OUT_BLOCK_NAME = [
           '시간', '예상지수', '예상전일대비구분', '예상전일비', '예상등락율', '예상체결량', '누적거래량', '예상거래대금', '업종코드']

# YK3
YK3_IN_BLOCK_CODE = ['shcode']
YK3_IN_BLOCK_NAME = ['단축코드']
YK3_OUT_BLOCK_CODE = [
           'hotime', 'yeprice', 'yevolume', 'jnilysign', 'jnilchange', 'jnilydrate', 'yofferho0', 'ybidho0', 'yofferrem0', 'ybidrem0',
           'shcode', 'exchname']
YK3_OUT_BLOCK_NAME = [
           '호가시간', '예상체결가격', '예상체결수량', '예상체결가전일종가대비구분', '예상체결가전일종가대비', '예상체결가전일종가등락율', '예상매도호가', '예상매수호가', '예상매도호가수량', '예상매수호가수량',
           '단축코드', '거래소명']

# YS3
YS3_IN_BLOCK_CODE = ['shcode']
YS3_IN_BLOCK_NAME = ['단축코드']
YS3_OUT_BLOCK_CODE = [
           'hotime', 'yeprice', 'yevolume', 'jnilysign', 'jnilchange', 'jnilydrate', 'yofferho0', 'ybidho0', 'yofferrem0', 'ybidrem0',
           'shcode', 'exchname']
YS3_OUT_BLOCK_NAME = [
           '호가시간', '예상체결가격', '예상체결수량', '예상체결가전일종가대비구분', '예상체결가전일종가대비', '예상체결가전일종가등락율', '예상매도호가', '예상매수호가', '예상매도호가수량', '예상매수호가수량',
           '단축코드', '거래소명']

# g3101
g3101_IN_BLOCK_CODE = ['delaygb', 'keysymbol', 'exchcd', 'symbol']
g3101_IN_BLOCK_NAME = ['지연구분', 'KEY종목코드', '거래소코드', '종목코드']
g3101_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'exchange', 'suspend', 'sellonly', 'symbol', 'korname', 'induname', 'floatpoint',
           'currency', 'price', 'sign', 'diff', 'rate', 'volume', 'amount', 'high52p', 'low52p', 'uplimit',
           'dnlimit', 'open', 'high', 'low', 'perv', 'epsv']
g3101_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '거래소ID', '거래상태', '매매구분', '종목코드', '한글종목명', '업종한글명', '소숫점자릿수',
           '외환코드', '현재가', '전일대비구분', '전일대비', '등락률', '거래량', '거래대금', '52주최고가', '52주최저가', '상한가',
           '하한가', '시가', '고가', '저가', 'PER', 'EPS']

# g3102
g3102_IN_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'readcnt', 'cts_seq']
g3102_IN_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '조회갯수', '연속시퀀스']
g3102_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'cts_seq', 'rec_count']
g3102_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '연속시퀀스', '레코드카운트']
g3102_OUT_BLOCK_1_CODE = [
           'locdate', 'loctime', 'kordate', 'kortime', 'price', 'sign', 'diff', 'rate', 'open', 'high',
           'low', 'exevol', 'cgubun', 'floatpoint']
g3102_OUT_BLOCK_1_NAME = [
           '현지일자', '현지시간', '한국일자', '한국시간', '현재가', '전일대비구분', '전일대비', '등락률', '시가', '고가',
           '저가', '체결량', '체결구분', '소숫점자릿수']

# g3103
g3103_IN_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'gubun', 'date']
g3103_IN_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '주기구분', '조회일자']
g3103_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'gubun', 'date']
g3103_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '주기구분', '조회일자']
g3103_OUT_BLOCK_1_CODE = [
           'chedate', 'price', 'sign', 'diff', 'rate', 'volume', 'open', 'high', 'low', 'floatpoint']
g3103_OUT_BLOCK_1_NAME = [
           '영업일자', '현재가', '전일대비구분', '전일대비', '등락률', '누적거래량', '시가', '고가', '저가', '소숫점자릿수']

# g3104
g3104_IN_BLOCK_CODE = ['delaygb', 'keysymbol', 'exchcd', 'symbol']
g3104_IN_BLOCK_NAME = ['지연구분', 'KEY종목코드', '거래소코드', '종목코드']
g3104_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'exchange', 'symbol', 'korname', 'engname', 'exchange_name', 'nation_name', 'induname',
           'instname', 'floatpoint', 'currency', 'suspend', 'sellonly', 'share', 'untprc', 'bidlotsize', 'asklotsize', 'volume',
           'amount', 'pcls', 'clos', 'open', 'high', 'low', 'high52p', 'low52p', 'shareprc', 'perv',
           'epsv', 'exrate', 'bidlotsize2', 'asklotsize2']
g3104_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '거래소ID', '종목코드', '한글종목명', '영문종목명', '거래소명', '국가명', '업종명',
           '증권종류', '소숫점자릿수', '거래통화', '거래상태', '매매구분', '발행주식수', '호가단위', '매수주문단위', '매도주문단위', '거래량',
           '거래대금', '전일종가', '기준가', '시가', '고가', '저가', '52주고가', '52주저가', '시가총액', 'PER',
           'EPS', '환율', '매수주문단위2', '매도주문단위2']

# g3106
g3106_IN_BLOCK_CODE = ['delaygb', 'keysymbol', 'exchcd', 'symbol']
g3106_IN_BLOCK_NAME = ['지연구분', 'KEY종목코드', '거래소코드', '종목코드']
g3106_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'korname', 'price', 'floatpoint', 'sign', 'diff', 'rate',
           'volume', 'amount', 'jnilclose', 'open', 'high', 'low', 'hotime', 'offerho1', 'bidho1', 'offercnt1',
           'bidcnt1', 'offerrem1', 'bidrem1', 'offerho2', 'bidho2', 'offercnt2', 'bidcnt2', 'offerrem2', 'bidrem2', 'offerho3',
           'bidho3', 'offercnt3', 'bidcnt3', 'offerrem3', 'bidrem3', 'offerho4', 'bidho4', 'offercnt4', 'bidcnt4', 'offerrem4',
           'bidrem4', 'offerho5', 'bidho5', 'offercnt5', 'bidcnt5', 'offerrem5', 'bidrem5', 'offerho6', 'bidho6', 'offercnt6',
           'bidcnt6', 'offerrem6', 'bidrem6', 'offerho7', 'bidho7', 'offercnt7', 'bidcnt7', 'offerrem7', 'bidrem7', 'offerho8',
           'bidho8', 'offercnt8', 'bidcnt8', 'offerrem8', 'bidrem8', 'offerho9', 'bidho9', 'offercnt9', 'bidcnt9', 'offerrem9',
           'bidrem9', 'offerho10', 'bidho10', 'offercnt10', 'bidcnt10', 'offerrem10', 'bidrem10', 'offercnt', 'bidcnt', 'offer',
           'bid']
g3106_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '한글종목명', '현재가', '소숫점자릿수', '전일대비구분', '전일대비', '등락률',
           '누적거래량', '누적거래대금', '전일종가', '시가', '고가', '저가', '호가수신시간', '매도호가1', '매수호가1', '매도호가건수1',
           '매수호가건수1', '매도호가잔량1', '매수호가잔량1', '매도호가2', '매수호가2', '매도호가건수2', '매수호가건수2', '매도호가잔량2', '매수호가잔량2', '매도호가3',
           '매수호가3', '매도호가건수3', '매수호가건수3', '매도호가잔량3', '매수호가잔량3', '매도호가4', '매수호가4', '매도호가건수4', '매수호가건수4', '매도호가잔량4',
           '매수호가잔량4', '매도호가5', '매수호가5', '매도호가건수5', '매수호가건수5', '매도호가잔량5', '매수호가잔량5', '매도호가6', '매수호가6', '매도호가건수6',
           '매수호가건수6', '매도호가잔량6', '매수호가잔량6', '매도호가7', '매수호가7', '매도호가건수7', '매수호가건수7', '매도호가잔량7', '매수호가잔량7', '매도호가8',
           '매수호가8', '매도호가건수8', '매수호가건수8', '매도호가잔량8', '매수호가잔량8', '매도호가9', '매수호가9', '매도호가건수9', '매수호가건수9', '매도호가잔량9',
           '매수호가잔량9', '매도호가10', '매수호가10', '매도호가건수10', '매수호가건수10', '매도호가잔량10', '매수호가잔량10', '매도호가건수합', '매수호가건수합', '매도호가잔량합',
           '매수호가잔량합']

# g3190
g3190_IN_BLOCK_CODE = ['delaygb', 'natcode', 'exgubun', 'readcnt', 'cts_value']
g3190_IN_BLOCK_NAME = ['지연구분', '국가구분', '거래소구분', '조회갯수', '연속구분']
g3190_OUT_BLOCK_CODE = ['delaygb', 'natcode', 'exgubun', 'cts_value', 'rec_count']
g3190_OUT_BLOCK_NAME = ['지연구분', '국가구분', '거래소구분', '연속구분', '레코드카운트']
g3190_OUT_BLOCK_1_CODE = [
           'keysymbol', 'natcode', 'exchcd', 'symbol', 'seccode', 'korname', 'engname', 'currency', 'isin', 'floatpoint',
           'indusury', 'share', 'marketcap', 'par', 'parcurr', 'bidlotsize2', 'asklotsize2', 'clos', 'listed_date', 'expire_date',
           'suspend', 'bymd', 'sellonly', 'stamp', 'ticktype', 'pcls', 'vcmf', 'casf', 'posf', 'point']
g3190_OUT_BLOCK_1_NAME = [
           'KEY종목코드', '국가코드', '거래소코드', '종목코드', '거래소종목코드', '한글종목명', '영문종목명', '외환코드', 'ISIN', 'FLOATPOINT',
           '업종코드', '상장주식수', '자본금', '액면가', '액면가외환코드', '매수주문단위2', '매도주문단위2', '기준가', '상장일자', '만기일자',
           '거래정지여부', '영업일자', 'SELLONLY구분', '인지세여부', 'TICKSIZETYPE', '전일종가', 'VCM대상종목', 'CAS대상종목', 'POS대상종목', '소수점매매가능종목']

# g3202
g3202_IN_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'ncnt', 'qrycnt', 'comp_yn', 'sdate', 'edate', 'cts_seq']
g3202_IN_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '단위(n틱)', '요청건수(최대-압축:2000비압축:500)', '압축여부(Y:압축N:비압축)', '시작일자', '종료일자', '연속시퀀스']
g3202_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'cts_seq', 'rec_count', 'preopen', 'prehigh', 'prelow', 'preclose',
           'prevolume', 'open', 'high', 'low', 'close', 's_time', 'e_time', 'last_count', 'timediff']
g3202_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '연속시퀀스', '레코드카운트', '전일시가', '전일고가', '전일저가', '전일종가',
           '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '마지막Tick건수', '시차']
g3202_OUT_BLOCK_1_CODE = [
           'date', 'loctime', 'open', 'high', 'low', 'close', 'exevol', 'jongchk', 'prtt_rate', 'pricechk',
           'sign']
g3202_OUT_BLOCK_1_NAME = [
           '날짜', '현지시간', '시가', '고가', '저가', '종가', '체결량', '수정구분', '수정비율', '수정주가반영항목',
           '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)']

# g3203
g3203_IN_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'ncnt', 'qrycnt', 'comp_yn', 'sdate', 'edate', 'cts_date',
           'cts_time']
g3203_IN_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '단위(n분)', '요청건수(최대-압축:2000비압축:500)', '압축여부(Y:압축N:비압축)', '시작일자', '종료일자', '연속일자',
           '연속시간']
g3203_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'cts_date', 'cts_time', 'rec_count', 'preopen', 'prehigh', 'prelow',
           'preclose', 'prevolume', 'open', 'high', 'low', 'close', 's_time', 'e_time', 'timediff']
g3203_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '연속일자', '연속시간', '레코드카운트', '전일시가', '전일고가', '전일저가',
           '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '시차']
g3203_OUT_BLOCK_1_CODE = [
           'date', 'loctime', 'open', 'high', 'low', 'close', 'exevol', 'amount']
g3203_OUT_BLOCK_1_NAME = [
           '날짜', '현지시간', '시가', '고가', '저가', '종가', '체결량', '거래대금']

# g3204
g3204_IN_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'gubun', 'qrycnt', 'comp_yn', 'sdate', 'edate', 'cts_date',
           'cts_info', 'sujung']
g3204_IN_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '주기구분(5:년)', '요청건수(최대-압축:2000비압축:500)', '압축여부(Y:압축N:비압축)', '시작일자', '종료일자', '연속일자',
           '연속정보', '수정주가여부(Y:적용N:비적용)']
g3204_OUT_BLOCK_CODE = [
           'delaygb', 'keysymbol', 'exchcd', 'symbol', 'cts_date', 'cts_info', 'rec_count', 'preopen', 'prehigh', 'prelow',
           'preclose', 'prevolume', 'open', 'high', 'low', 'close', 'uplimit', 'dnlimit', 's_time', 'e_time',
           'dshmin']
g3204_OUT_BLOCK_NAME = [
           '지연구분', 'KEY종목코드', '거래소코드', '종목코드', '연속일자', '연속정보', '레코드카운트', '전일시가', '전일고가', '전일저가',
           '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가', '상한가', '하한가', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)',
           '동시호가처리시간(MM:분)']
g3204_OUT_BLOCK_1_CODE = [
           'date', 'open', 'high', 'low', 'close', 'volume', 'amount', 'jongchk', 'prtt_rate', 'pricechk',
           'ratevalue', 'sign']
g3204_OUT_BLOCK_1_NAME = [
           '날짜', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율', '수정주가반영항목',
           '수정비율반영거래대금', '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)']

# t0150
t0150_IN_BLOCK_CODE = ['accno', 'cts_medosu', 'cts_expcode', 'cts_price', 'cts_middiv']
t0150_IN_BLOCK_NAME = ['계좌번호', 'CTS_매매구분', 'CTS_종목번호', 'CTS_단가', 'CTS_매체']
t0150_OUT_BLOCK_CODE = [
           'mdqty', 'mdamt', 'mdfee', 'mdtax', 'mdargtax', 'tmdtax', 'mdadjamt', 'msqty', 'msamt', 'msfee',
           'tmstax', 'msadjamt', 'tqty', 'tamt', 'tfee', 'tottax', 'targtax', 'ttax', 'tadjamt', 'cts_medosu',
           'cts_expcode', 'cts_price', 'cts_middiv']
t0150_OUT_BLOCK_NAME = [
           '매도수량', '매도약정금액', '매도수수료', '매도거래세', '매도농특세', '매도제비용합', '매도정산금액', '매수수량', '매수약정금액', '매수수수료',
           '매수제비용합', '매수정산금액', '합계수량', '합계약정금액', '합계수수료', '합계거래세', '합계농특세', '합계제비용합', '합계정산금액', 'CTS_매매구분',
           'CTS_종목번호', 'CTS_단가', 'CTS_매체']
t0150_OUT_BLOCK_1_CODE = [
           'medosu', 'expcode', 'qty', 'price', 'amt', 'fee', 'tax', 'argtax', 'adjamt', 'middiv']
t0150_OUT_BLOCK_1_NAME = [
           '매매구분', '종목번호', '수량', '단가', '약정금액', '수수료', '거래세', '농특세', '정산금액', '매체']

# t0151
t0151_IN_BLOCK_CODE = [
           'date', 'accno', 'cts_medosu', 'cts_expcode', 'cts_price', 'cts_middiv']
t0151_IN_BLOCK_NAME = [
           '일자', '계좌번호', 'CTS_매매구분', 'CTS_종목번호', 'CTS_단가', 'CTS_매체']
t0151_OUT_BLOCK_CODE = [
           'mdqty', 'mdamt', 'mdfee', 'mdtax', 'mdargtax', 'tmdtax', 'mdadjamt', 'msqty', 'msamt', 'msfee',
           'tmstax', 'msadjamt', 'tqty', 'tamt', 'tfee', 'tottax', 'targtax', 'ttax', 'tadjamt', 'cts_medosu',
           'cts_expcode', 'cts_price', 'cts_middiv']
t0151_OUT_BLOCK_NAME = [
           '매도수량', '매도약정금액', '매도수수료', '매도거래세', '매도농특세', '매도제비용합', '매도정산금액', '매수수량', '매수약정금액', '매수수수료',
           '매수제비용합', '매수정산금액', '합계수량', '합계약정금액', '합계수수료', '합계거래세', '합계농특세', '합계제비용합', '합계정산금액', 'CTS_매매구분',
           'CTS_종목번호', 'CTS_단가', 'CTS_매체']
t0151_OUT_BLOCK_1_CODE = [
           'medosu', 'expcode', 'qty', 'price', 'amt', 'fee', 'tax', 'argtax', 'adjamt', 'middiv']
t0151_OUT_BLOCK_1_NAME = [
           '매매구분', '종목번호', '수량', '단가', '약정금액', '수수료', '거래세', '농특세', '정산금액', '매체']

# t0167
t0167_IN_BLOCK_CODE = ['id']
t0167_IN_BLOCK_NAME = ['id']
t0167_OUT_BLOCK_CODE = ['dt', 'time']
t0167_OUT_BLOCK_NAME = ['일자(YYYYMMDD)', '시간(HHMMSSssssss)']

# t0424
t0424_IN_BLOCK_CODE = [
           'accno', 'passwd', 'prcgb', 'chegb', 'dangb', 'charge', 'cts_expcode']
t0424_IN_BLOCK_NAME = [
           '계좌번호', '비밀번호', '단가구분', '체결구분', '단일가구분', '제비용포함여부', 'CTS_종목번호']
t0424_OUT_BLOCK_CODE = [
           'sunamt', 'dtsunik', 'mamt', 'sunamt1', 'cts_expcode', 'tappamt', 'tdtsunik']
t0424_OUT_BLOCK_NAME = [
           '추정순자산', '실현손익', '매입금액', '추정D2예수금', 'CTS_종목번호', '평가금액', '평가손익']
t0424_OUT_BLOCK_1_CODE = [
           'expcode', 'jangb', 'janqty', 'mdposqt', 'pamt', 'mamt', 'sinamt', 'lastdt', 'msat', 'mpms',
           'mdat', 'mpmd', 'jsat', 'jpms', 'jdat', 'jpmd', 'sysprocseq', 'loandt', 'hname', 'marketgb',
           'jonggb', 'janrt', 'price', 'appamt', 'dtsunik', 'sunikrt', 'fee', 'tax', 'sininter']
t0424_OUT_BLOCK_1_NAME = [
           '종목번호', '잔고구분', '잔고수량', '매도가능수량', '평균단가', '매입금액', '대출금액', '만기일자', '당일매수금액', '당일매수단가',
           '당일매도금액', '당일매도단가', '전일매수금액', '전일매수단가', '전일매도금액', '전일매도단가', '처리순번', '대출일자', '종목명', '시장구분',
           '종목구분', '보유비중', '현재가', '평가금액', '평가손익', '수익율', '수수료', '제세금', '신용이자']

# t0425
t0425_IN_BLOCK_CODE = [
           'accno', 'passwd', 'expcode', 'chegb', 'medosu', 'sortgb', 'cts_ordno']
t0425_IN_BLOCK_NAME = [
           '계좌번호', '비밀번호', '종목번호', '체결구분', '매매구분', '정렬순서', '주문번호']
t0425_OUT_BLOCK_CODE = [
           'tqty', 'tcheqty', 'tordrem', 'cmss', 'tamt', 'tmdamt', 'tmsamt', 'tax', 'cts_ordno']
t0425_OUT_BLOCK_NAME = [
           '총주문수량', '총체결수량', '총미체결수량', '추정수수료', '총주문금액', '총매도체결금액', '총매수체결금액', '추정제세금', '주문번호']
t0425_OUT_BLOCK_1_CODE = [
           'ordno', 'expcode', 'medosu', 'qty', 'price', 'cheqty', 'cheprice', 'ordrem', 'cfmqty', 'status',
           'orgordno', 'ordgb', 'ordtime', 'ordermtd', 'sysprocseq', 'hogagb', 'price1', 'orggb', 'singb', 'loandt',
           'exchname']
t0425_OUT_BLOCK_1_NAME = [
           '주문번호', '종목번호', '구분', '주문수량', '주문가격', '체결수량', '체결가격', '미체결잔량', '확인수량', '상태',
           '원주문번호', '유형', '주문시간', '주문매체', '처리순번', '호가유형', '현재가', '주문구분', '신용구분', '대출일자',
           '거래소명']

# t1101
t1101_IN_BLOCK_CODE = ['shcode']
t1101_IN_BLOCK_NAME = ['단축코드']
t1101_OUT_BLOCK_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'jnilclose', 'offerho1', 'bidho1', 'offerrem1',
           'bidrem1', 'preoffercha1', 'prebidcha1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'preoffercha2', 'prebidcha2', 'offerho3',
           'bidho3', 'offerrem3', 'bidrem3', 'preoffercha3', 'prebidcha3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'preoffercha4',
           'prebidcha4', 'offerho5', 'bidho5', 'offerrem5', 'bidrem5', 'preoffercha5', 'prebidcha5', 'offerho6', 'bidho6', 'offerrem6',
           'bidrem6', 'preoffercha6', 'prebidcha6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'preoffercha7', 'prebidcha7', 'offerho8',
           'bidho8', 'offerrem8', 'bidrem8', 'preoffercha8', 'prebidcha8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'preoffercha9',
           'prebidcha9', 'offerho10', 'bidho10', 'offerrem10', 'bidrem10', 'preoffercha10', 'prebidcha10', 'offer', 'bid', 'preoffercha',
           'prebidcha', 'hotime', 'yeprice', 'yevolume', 'yesign', 'yechange', 'yediff', 'tmoffer', 'tmbid', 'ho_status',
           'shcode', 'uplmtprice', 'dnlmtprice', 'open', 'high', 'low', 'krx_midprice', 'krx_offermidsumrem', 'krx_bidmidsumrem', 'krx_midsumrem',
           'krx_midsumremgubun']
t1101_OUT_BLOCK_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '전일종가(기준가)', '매도호가1', '매수호가1', '매도호가수량1',
           '매수호가수량1', '직전매도대비수량1', '직전매수대비수량1', '매도호가2', '매수호가2', '매도호가수량2', '매수호가수량2', '직전매도대비수량2', '직전매수대비수량2', '매도호가3',
           '매수호가3', '매도호가수량3', '매수호가수량3', '직전매도대비수량3', '직전매수대비수량3', '매도호가4', '매수호가4', '매도호가수량4', '매수호가수량4', '직전매도대비수량4',
           '직전매수대비수량4', '매도호가5', '매수호가5', '매도호가수량5', '매수호가수량5', '직전매도대비수량5', '직전매수대비수량5', '매도호가6', '매수호가6', '매도호가수량6',
           '매수호가수량6', '직전매도대비수량6', '직전매수대비수량6', '매도호가7', '매수호가7', '매도호가수량7', '매수호가수량7', '직전매도대비수량7', '직전매수대비수량7', '매도호가8',
           '매수호가8', '매도호가수량8', '매수호가수량8', '직전매도대비수량8', '직전매수대비수량8', '매도호가9', '매수호가9', '매도호가수량9', '매수호가수량9', '직전매도대비수량9',
           '직전매수대비수량9', '매도호가10', '매수호가10', '매도호가수량10', '매수호가수량10', '직전매도대비수량10', '직전매수대비수량10', '매도호가수량합', '매수호가수량합', '직전매도대비수량합',
           '직전매수대비수량합', '수신시간', '예상체결가격', '예상체결수량', '예상체결전일구분', '예상체결전일대비', '예상체결등락율', '시간외매도잔량', '시간외매수잔량', '동시구분',
           '단축코드', '상한가', '하한가', '시가', '고가', '저가', 'KRX중간가격', 'KRX매도중간가잔량합계수량', 'KRX매수중간가잔량합계수량', 'KRX중간가잔량합계수량',
           "KRX중간가잔량구분('없음'1'매도'2'매수"]

# t1102
t1102_IN_BLOCK_CODE = ['shcode', 'exchgubun']
t1102_IN_BLOCK_NAME = ['단축코드', '거래소구분코드']
t1102_OUT_BLOCK_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'recprice', 'avg', 'uplmtprice', 'dnlmtprice',
           'jnilvolume', 'volumediff', 'open', 'opentime', 'high', 'hightime', 'low', 'lowtime', 'high52w', 'high52wdate',
           'low52w', 'low52wdate', 'exhratio', 'per', 'pbrx', 'listing', 'jkrate', 'memedan', 'offernocd1', 'bidnocd1',
           'offerno1', 'bidno1', 'dvol1', 'svol1', 'dcha1', 'scha1', 'ddiff1', 'sdiff1', 'offernocd2', 'bidnocd2',
           'offerno2', 'bidno2', 'dvol2', 'svol2', 'dcha2', 'scha2', 'ddiff2', 'sdiff2', 'offernocd3', 'bidnocd3',
           'offerno3', 'bidno3', 'dvol3', 'svol3', 'dcha3', 'scha3', 'ddiff3', 'sdiff3', 'offernocd4', 'bidnocd4',
           'offerno4', 'bidno4', 'dvol4', 'svol4', 'dcha4', 'scha4', 'ddiff4', 'sdiff4', 'offernocd5', 'bidnocd5',
           'offerno5', 'bidno5', 'dvol5', 'svol5', 'dcha5', 'scha5', 'ddiff5', 'sdiff5', 'fwdvl', 'ftradmdcha',
           'ftradmddiff', 'fwsvl', 'ftradmscha', 'ftradmsdiff', 'vol', 'shcode', 'value', 'jvolume', 'highyear', 'highyeardate',
           'lowyear', 'lowyeardate', 'target', 'capital', 'abscnt', 'parprice', 'gsmm', 'subprice', 'total', 'listdate',
           'name', 'bfsales', 'bfoperatingincome', 'bfordinaryincome', 'bfnetincome', 'bfeps', 'name2', 'bfsales2', 'bfoperatingincome2', 'bfordinaryincome2',
           'bfnetincome2', 'bfeps2', 'salert', 'opert', 'ordrt', 'netrt', 'epsrt', 'info1', 'info2', 'info3',
           'info4', 'janginfo', 't_per', 'tonghwa', 'dval1', 'sval1', 'dval2', 'sval2', 'dval3', 'sval3',
           'dval4', 'sval4', 'dval5', 'sval5', 'davg1', 'savg1', 'davg2', 'savg2', 'davg3', 'savg3',
           'davg4', 'savg4', 'davg5', 'savg5', 'ftradmdval', 'ftradmsval', 'ftradmdvag', 'ftradmsvag', 'info5', 'spac_gubun',
           'issueprice', 'alloc_gubun', 'alloc_text', 'shterm_text', 'svi_uplmtprice', 'svi_dnlmtprice', 'low_lqdt_gu', 'abnormal_rise_gu', 'lend_text', 'ty_text',
           'nxt_janginfo', 'nxt_shterm_text', 'nxt_svi_uplmtprice', 'nxt_svi_dnlmtprice', 'ex_shcode']
t1102_OUT_BLOCK_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '기준가(평가가격)', '가중평균', '상한가(최고호가가격)', '하한가(최저호가가격)',
           '전일거래량', '거래량차', '시가', '시가시간', '고가', '고가시간', '저가', '저가시간', '52최고가', '52최고가일',
           '52최저가', '52최저가일', '소진율', 'PER', 'PBRX', '상장주식수(천)', '증거금율', '수량단위', '매도증권사코드1', '매수증권사코드1',
           '매도증권사명1', '매수증권사명1', '총매도수량1', '총매수수량1', '매도증감1', '매수증감1', '매도비율1', '매수비율1', '매도증권사코드2', '매수증권사코드2',
           '매도증권사명2', '매수증권사명2', '총매도수량2', '총매수수량2', '매도증감2', '매수증감2', '매도비율2', '매수비율2', '매도증권사코드3', '매수증권사코드3',
           '매도증권사명3', '매수증권사명3', '총매도수량3', '총매수수량3', '매도증감3', '매수증감3', '매도비율3', '매수비율3', '매도증권사코드4', '매수증권사코드4',
           '매도증권사명4', '매수증권사명4', '총매도수량4', '총매수수량4', '매도증감4', '매수증감4', '매도비율4', '매수비율4', '매도증권사코드5', '매수증권사코드5',
           '매도증권사명5', '매수증권사명5', '총매도수량5', '총매수수량5', '매도증감5', '매수증감5', '매도비율5', '매수비율5', '외국계매도합계수량', '외국계매도직전대비',
           '외국계매도비율', '외국계매수합계수량', '외국계매수직전대비', '외국계매수비율', '회전율', '단축코드', '누적거래대금', '전일동시간거래량', '연중최고가', '연중최고일자',
           '연중최저가', '연중최저일자', '목표가', '자본금', '유동주식수', '액면가', '결산월', '대용가', '시가총액', '상장일',
           '전분기명', '전분기매출액', '전분기영업이익', '전분기경상이익', '전분기순이익', '전분기EPS', '전전분기명', '전전분기매출액', '전전분기영업이익', '전전분기경상이익',
           '전전분기순이익', '전전분기EPS', '전년대비매출액', '전년대비영업이익', '전년대비경상이익', '전년대비순이익', '전년대비EPS', '락구분', '관리/급등구분', '정지/연장구분',
           '투자/불성실구분', '장구분', 'T.PER', '통화ISO코드', '총매도대금1', '총매수대금1', '총매도대금2', '총매수대금2', '총매도대금3', '총매수대금3',
           '총매도대금4', '총매수대금4', '총매도대금5', '총매수대금5', '총매도평단가1', '총매수평단가1', '총매도평단가2', '총매수평단가2', '총매도평단가3', '총매수평단가3',
           '총매도평단가4', '총매수평단가4', '총매도평단가5', '총매수평단가5', '외국계매도대금', '외국계매수대금', '외국계매도평단가', '외국계매수평단가', '투자주의환기', '기업인수목적회사여부',
           '발행가격', '배분적용구분코드(1:배분발생2:배분해제그외:미발생)', '배분적용구분', '단기과열/VI발동', '정적VI상한가', '정적VI하한가', '저유동성종목여부', '이상급등종목여부', '대차불가표시', 'ETF/ETN투자유의',
           'NXT장구분', 'NXT단기과열/VI발동', 'NXT정적VI상한가', 'NXT정적VI하한가', '거래소별단축코드']

# t1104
t1104_IN_BLOCK_CODE = ['code', 'nrec', 'exchgubun']
t1104_IN_BLOCK_NAME = ['종목코드', '건수', '거래소구분코드']
t1104_IN_BLOCK_CODE = ['indx', 'gubn', 'dat1', 'dat2']
t1104_IN_BLOCK_NAME = ['인덱스', '조건구분', '데이타1', '데이타2']
t1104_OUT_BLOCK_CODE = ['nrec']
t1104_OUT_BLOCK_NAME = ['출력건수']
t1104_OUT_BLOCK_1_CODE = ['indx', 'gubn', 'vals']
t1104_OUT_BLOCK_1_NAME = ['인덱스', '조건구분', '출력값']

# t1105
t1105_IN_BLOCK_CODE = ['shcode', 'exchgubun']
t1105_IN_BLOCK_NAME = ['단축코드', '거래소구분코드']
t1105_OUT_BLOCK_CODE = [
           'shcode', 'pbot', 'offer1', 'supp1', 'offer2', 'supp2', 'stdprc', 'offerd', 'suppd']
t1105_OUT_BLOCK_NAME = [
           '단축코드', '피봇', '1차저항', '1차지지', '2차저항', '2차지지', '기준가격', 'D저항', 'D지지']

# t1109
t1109_IN_BLOCK_CODE = ['shcode', 'dan_chetime', 'idx']
t1109_IN_BLOCK_NAME = ['종목코드', '체결cts', 'IDX']
t1109_OUT_BLOCK_CODE = ['ctsshcode', 'ctschetime', 'idx']
t1109_OUT_BLOCK_NAME = ['종목cts', '체결cts', 'IDX']
t1109_OUT_BLOCK_1_CODE = [
           'dan_chetime', 'dan_price', 'dan_sign', 'dan_change', 'diff', 'dan_cvolume', 'chdegree', 'dan_volume']
t1109_OUT_BLOCK_1_NAME = [
           '시간', '현재가', '전일대비구분', '전일대비', '등락율', '체결량', '체결강도', '누적거래량']

# t1301
t1301_IN_BLOCK_CODE = ['shcode', 'cvolume', 'starttime', 'endtime', 'cts_time']
t1301_IN_BLOCK_NAME = ['단축코드', '특이거래량', '시작시간', '종료시간', '시간CTS']
t1301_OUT_BLOCK_CODE = ['cts_time']
t1301_OUT_BLOCK_NAME = ['시간CTS']
t1301_OUT_BLOCK_1_CODE = [
           'chetime', 'price', 'sign', 'change', 'diff', 'cvolume', 'chdegree', 'volume', 'mdvolume', 'mdchecnt',
           'msvolume', 'mschecnt', 'revolume', 'rechecnt']
t1301_OUT_BLOCK_1_NAME = [
           '시간', '현재가', '전일대비구분', '전일대비', '등락율', '체결수량', '체결강도', '거래량', '매도체결수량', '매도체결건수',
           '매수체결수량', '매수체결건수', '순체결량', '순체결건수']

# t1302
t1302_IN_BLOCK_CODE = ['shcode', 'gubun', 'time', 'cnt', 'exchgubun']
t1302_IN_BLOCK_NAME = ['단축코드', '작업구분', '시간', '건수', '거래소구분코드']
t1302_OUT_BLOCK_CODE = ['cts_time']
t1302_OUT_BLOCK_NAME = ['시간CTS']
t1302_OUT_BLOCK_1_CODE = [
           'chetime', 'close', 'sign', 'change', 'diff', 'chdegree', 'mdvolume', 'msvolume', 'revolume', 'mdchecnt',
           'mschecnt', 'rechecnt', 'volume', 'open', 'high', 'low', 'cvolume', 'mdchecnttm', 'mschecnttm', 'totofferrem',
           'totbidrem', 'mdvolumetm', 'msvolumetm']
t1302_OUT_BLOCK_1_NAME = [
           '시간', '종가', '전일대비구분', '전일대비', '등락율', '체결강도', '매도체결수량', '매수체결수량', '순매수체결량', '매도체결건수',
           '매수체결건수', '순체결건수', '거래량', '시가', '고가', '저가', '체결량', '매도체결건수(시간)', '매수체결건수(시간)', '매도잔량',
           '매수잔량', '시간별매도체결량', '시간별매수체결량']

# t1305
t1305_IN_BLOCK_CODE = [
           'shcode', 'dwmcode', 'date', 'idx', 'cnt', 'exchgubun']
t1305_IN_BLOCK_NAME = [
           '단축코드', '일주월구분', '날짜', 'IDX', '건수', '거래소구분코드']
t1305_OUT_BLOCK_CODE = ['cnt', 'date', 'idx', 'ex_shcode']
t1305_OUT_BLOCK_NAME = ['CNT', '날짜', 'IDX', '거래소별단축코드']
t1305_OUT_BLOCK_1_CODE = [
           'date', 'open', 'high', 'low', 'close', 'sign', 'change', 'diff', 'volume', 'diff_vol',
           'chdegree', 'sojinrate', 'changerate', 'fpvolume', 'covolume', 'shcode', 'value', 'ppvolume', 'o_sign', 'o_change',
           'o_diff', 'h_sign', 'h_change', 'h_diff', 'l_sign', 'l_change', 'l_diff', 'marketcap']
t1305_OUT_BLOCK_1_NAME = [
           '날짜', '시가', '고가', '저가', '종가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래증가율',
           '체결강도', '소진율', '회전율', '외인순매수', '기관순매수', '종목코드', '누적거래대금(단위:백만)', '개인순매수', '기준가기준시가대비구분', '기준가기준시가대비',
           '기준가기준시가등락율', '기준가기준고가대비구분', '기준가기준고가대비', '기준가기준고가등락율', '기준가기준저가대비구분', '기준가기준저가대비', '기준가기준저가등락율', '시가총액(단위:백만)']

# t1308
t1308_IN_BLOCK_CODE = ['shcode', 'starttime', 'endtime', 'bun_term', 'exchgubun']
t1308_IN_BLOCK_NAME = ['단축코드', '시작시간', '종료시간', '분간격', '거래소구분코드']
t1308_OUT_BLOCK_CODE = ['ex_shcode']
t1308_OUT_BLOCK_NAME = ['거래소별단축코드']
t1308_OUT_BLOCK_1_CODE = [
           'chetime', 'price', 'sign', 'change', 'diff', 'cvolume', 'chdegvol', 'chdegcnt', 'volume', 'mdvolume',
           'mdchecnt', 'msvolume', 'mschecnt', 'open', 'high', 'low']
t1308_OUT_BLOCK_1_NAME = [
           '시간', '현재가', '전일대비구분', '전일대비', '등락율', '체결수량', '체결강도(거래량)', '체결강도(건수)', '거래량', '매도체결수량',
           '매도체결건수', '매수체결수량', '매수체결건수', '시가', '고가', '저가']

# t1310
t1310_IN_BLOCK_CODE = [
           'daygb', 'timegb', 'shcode', 'endtime', 'cts_time', 'exchgubun']
t1310_IN_BLOCK_NAME = [
           '당일전일구분', '분틱구분', '단축코드', '종료시간', '시간CTS', '거래소구분코드']
t1310_OUT_BLOCK_CODE = ['cts_time']
t1310_OUT_BLOCK_NAME = ['시간CTS']
t1310_OUT_BLOCK_1_CODE = [
           'chetime', 'price', 'sign', 'change', 'diff', 'cvolume', 'chdegree', 'volume', 'mdvolume', 'mdchecnt',
           'msvolume', 'mschecnt', 'revolume', 'rechecnt', 'exchname']
t1310_OUT_BLOCK_1_NAME = [
           '시간', '현재가', '전일대비구분', '전일대비', '등락율', '체결수량', '체결강도', '거래량', '매도체결수량', '매도체결건수',
           '매수체결수량', '매수체결건수', '순체결량', '순체결건수', '거래소명']

# t1403
t1403_IN_BLOCK_CODE = ['gubun', 'styymm', 'enyymm', 'idx']
t1403_IN_BLOCK_NAME = ['구분', '시작상장월', '종료상장월', 'IDX']
t1403_OUT_BLOCK_CODE = ['idx']
t1403_OUT_BLOCK_NAME = ['IDX']
t1403_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'kmprice', 'date', 'recprice', 'kmdiff',
           'close', 'recdiff', 'shcode']
t1403_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '공모가', '등록일', '등록일기준가', '기준가등락율',
           '등록일종가', '등록일등락율', '종목코드']

# t1404
t1404_IN_BLOCK_CODE = ['gubun', 'jongchk', 'cts_shcode']
t1404_IN_BLOCK_NAME = ['구분', '종목체크', '종목코드_CTS']
t1404_OUT_BLOCK_CODE = ['cts_shcode']
t1404_OUT_BLOCK_NAME = ['종목코드_CTS']
t1404_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'date', 'tprice', 'tchange', 'tdiff',
           'reason', 'shcode', 'edate']
t1404_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '지정일', '지정일주가', '지정일대비', '대비율',
           '사유', '종목코드', '해제일']

# t1405
t1405_IN_BLOCK_CODE = ['gubun', 'jongchk', 'cts_shcode']
t1405_IN_BLOCK_NAME = ['구분', '종목체크', '종목코드_CTS']
t1405_OUT_BLOCK_CODE = ['cts_shcode']
t1405_OUT_BLOCK_NAME = ['종목코드_CTS']
t1405_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'date', 'edate', 'shcode']
t1405_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '지정일', '해제일', '종목코드']

# t1410
t1410_IN_BLOCK_CODE = ['gubun', 'cts_shcode']
t1410_IN_BLOCK_NAME = ['구분', '종목코드_CTS']
t1410_OUT_BLOCK_CODE = ['cts_shcode']
t1410_OUT_BLOCK_NAME = ['종목코드_CTS']
t1410_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'shcode']
t1410_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '종목코드']

# t1411
t1411_IN_BLOCK_CODE = ['gubun', 'jongchk', 'jkrate', 'shcode', 'idx']
t1411_IN_BLOCK_NAME = ['시장구분', '위탁신용구분', '증거금율구분', '종목코드', 'IDX']
t1411_OUT_BLOCK_CODE = ['jkrate', 'sjkrate', 'idx']
t1411_OUT_BLOCK_NAME = ['위탁증거금율', '신용증거금율', 'IDX']
t1411_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'jkrate', 'sjkrate', 'subprice', 'recprice', 'price', 'sign', 'change', 'diff',
           'volume']
t1411_OUT_BLOCK_1_NAME = [
           '종목코드', '종목명', '위탁증거금율', '신용증거금율', '대용가', '전일종가', '현재가', '전일대비구분', '전일대비', '등락율',
           '누적거래량']

# t1422
t1422_IN_BLOCK_CODE = [
           'qrygb', 'gubun', 'jnilgubun', 'sign', 'jc_num', 'sprice', 'eprice', 'volume', 'idx', 'jshex',
           'exchgubun']
t1422_IN_BLOCK_NAME = [
           '조회구분', '구분', '전일구분', '상하한구분', '대상제외', '시작가격', '종료가격', '거래량', 'IDX', '전일상하한제외(C:제외)',
           '거래소구분코드']
t1422_OUT_BLOCK_CODE = ['cnt', 'idx']
t1422_OUT_BLOCK_NAME = ['CNT', 'IDX']
t1422_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'diff_vol', 'offerrem1', 'bidrem1', 'last',
           'lmtdaycnt', 'jnilvolume', 'shcode', 'ex_shcode']
t1422_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래증가율', '매도잔량', '매수잔량', '최종진입',
           '연속', '전일거래량', '종목코드', '거래소별단축코드']

# t1427
t1427_IN_BLOCK_CODE = [
           'qrygb', 'gubun', 'signgubun', 'diff', 'jc_num', 'sprice', 'eprice', 'volume', 'idx', 'jshex']
t1427_IN_BLOCK_NAME = [
           '조회구분', '구분', '상하한가구분', '등락율', '대상제외', '시작가격', '종료가격', '거래량', 'IDX', '전일상하한제외']
t1427_OUT_BLOCK_CODE = ['cnt', 'idx']
t1427_OUT_BLOCK_NAME = ['CNT', 'IDX']
t1427_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'diff_vol', 'lmtprice', 'rate', 'shcode',
           'jnilvolume', 'open', 'high', 'low', 'lmtdaycnt', 'value', 'total']
t1427_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래증가율', '상한가/하한가', '대비율', '종목코드',
           '전일거래량', '시가', '고가', '저가', '연속', '거래대금', '시가총액']

# t1441
t1441_IN_BLOCK_CODE = [
           'gubun1', 'gubun2', 'gubun3', 'jc_num', 'sprice', 'eprice', 'volume', 'idx', 'jc_num2', 'exchgubun']
t1441_IN_BLOCK_NAME = [
           '구분', '상승하락', '당일전일', '대상제외', '시작가격', '종료가격', '거래량', 'IDX', '대상제외2', '거래소구분코드']
t1441_OUT_BLOCK_CODE = ['idx']
t1441_OUT_BLOCK_NAME = ['IDX']
t1441_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'offerrem1', 'offerho1', 'bidho1', 'bidrem1',
           'updaycnt', 'jnildiff', 'shcode', 'open', 'high', 'low', 'voldiff', 'value', 'total', 'ex_shcode']
t1441_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '매도잔량', '매도호가', '매수호가', '매수잔량',
           '연속', '전일등락율', '종목코드', '시가', '고가', '저가', '거래량대비율', '거래대금', '시가총액', '거래소별단축코드']

# t1442
t1442_IN_BLOCK_CODE = [
           'gubun', 'type1', 'type2', 'type3', 'jc_num', 'sprice', 'eprice', 'volume', 'idx', 'jc_num2']
t1442_IN_BLOCK_NAME = [
           '구분', '신고신저', '기간', '유지여부', '대상제외', '시작가격', '종료가격', '거래량', 'IDX', '대상제외2']
t1442_OUT_BLOCK_CODE = ['idx']
t1442_OUT_BLOCK_NAME = ['IDX']
t1442_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'pastprice', 'pastsign', 'pastchange',
           'pastdiff']
t1442_OUT_BLOCK_1_NAME = [
           '종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '이전가', '이전가대비구분', '이전가대비',
           '이전가대비율']

# t1444
t1444_IN_BLOCK_CODE = ['upcode', 'idx']
t1444_IN_BLOCK_NAME = ['업종코드', 'IDX']
t1444_OUT_BLOCK_CODE = ['idx']
t1444_OUT_BLOCK_NAME = ['IDX']
t1444_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'vol_rate', 'total', 'rate',
           'for_rate']
t1444_OUT_BLOCK_1_NAME = [
           '종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '거래비중', '시가총액', '비중',
           '외인비중']

# t1449
t1449_IN_BLOCK_CODE = ['shcode', 'dategb']
t1449_IN_BLOCK_NAME = ['단축코드', '일자구분']
t1449_OUT_BLOCK_CODE = [
           'price', 'sign', 'change', 'diff', 'volume', 'msvolume', 'mdvolume']
t1449_OUT_BLOCK_NAME = [
           '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '매수체결량', '매도체결량']
t1449_OUT_BLOCK_1_CODE = [
           'price', 'sign', 'change', 'tickdiff', 'cvolume', 'diff', 'mdvolume', 'msvolume', 'msdiff']
t1449_OUT_BLOCK_1_NAME = [
           '체결가', '전일대비구분', '전일대비', '등락율', '체결수량', '비중', '매도체결량', '매수체결량', '매수비율']

# t1452
t1452_IN_BLOCK_CODE = [
           'gubun', 'jnilgubun', 'sdiff', 'ediff', 'jc_num', 'sprice', 'eprice', 'volume', 'idx']
t1452_IN_BLOCK_NAME = [
           '구분', '전일구분', '시작등락율', '종료등락율', '대상제외', '시작가격', '종료가격', '거래량', 'IDX']
t1452_OUT_BLOCK_CODE = ['idx']
t1452_OUT_BLOCK_NAME = ['IDX']
t1452_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'vol', 'jnilvolume', 'bef_diff', 'shcode']
t1452_OUT_BLOCK_1_NAME = [
           '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '회전율', '전일거래량', '전일비', '종목코드']

# t1463
t1463_IN_BLOCK_CODE = [
           'gubun', 'jnilgubun', 'jc_num', 'sprice', 'eprice', 'volume', 'idx', 'jc_num2', 'exchgubun']
t1463_IN_BLOCK_NAME = [
           '구분', '전일구분', '대상제외', '시작가격', '종료가격', '거래량', 'IDX', '대상제외2', '거래소구분코드']
t1463_OUT_BLOCK_CODE = ['idx']
t1463_OUT_BLOCK_NAME = ['IDX']
t1463_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'value', 'jnilvalue', 'bef_diff', 'shcode',
           'filler', 'jnilvolume', 'ex_shcode']
t1463_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래대금', '전일거래대금', '전일비', '종목코드',
           'filler', '전일거래량', '거래소별단축코드']

# t1466
t1466_IN_BLOCK_CODE = [
           'gubun', 'type1', 'type2', 'jc_num', 'sprice', 'eprice', 'volume', 'idx', 'jc_num2', 'exchgubun']
t1466_IN_BLOCK_NAME = [
           '구분', '전일거래량', '거래급등율', '대상제외', '시작가격', '종료가격', '거래량', 'IDX', '대상제외2', '거래소구분코드']
t1466_OUT_BLOCK_CODE = ['hhmm', 'idx']
t1466_OUT_BLOCK_NAME = ['현재시분', 'IDX']
t1466_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'price', 'sign', 'change', 'diff', 'stdvolume', 'volume', 'voldiff', 'open',
           'high', 'low', 'ex_shcode']
t1466_OUT_BLOCK_1_NAME = [
           '종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '전일거래량', '당일거래량', '거래급등율', '시가',
           '고가', '저가', '거래소별단축코드']

# t1471
t1471_IN_BLOCK_CODE = ['shcode', 'gubun', 'time', 'cnt']
t1471_IN_BLOCK_NAME = ['종목코드', '분구분', '시간', '자료개수']
t1471_OUT_BLOCK_CODE = [
           'time', 'price', 'sign', 'change', 'diff', 'volume']
t1471_OUT_BLOCK_NAME = [
           '시간CTS', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량']
t1471_OUT_BLOCK_1_CODE = [
           'time', 'preoffercha1', 'offerrem1', 'offerho1', 'bidho1', 'bidrem1', 'prebidcha1', 'totofferrem', 'totbidrem', 'totsun',
           'msrate', 'close']
t1471_OUT_BLOCK_1_NAME = [
           '체결시간', '메도증감', '매도우선잔량', '매도우선호가', '매수우선호가', '매수우선잔량', '매수증감', '총매도', '총매수', '순매수',
           '매수비율', '종가']

# t1475
t1475_IN_BLOCK_CODE = [
           'shcode', 'vptype', 'datacnt', 'date', 'time', 'rankcnt', 'gubun']
t1475_IN_BLOCK_NAME = [
           '종목코드', '상승하락', '데이터개수', '기준일자', '기준시간', '랭크카운터', '조회구분']
t1475_OUT_BLOCK_CODE = ['date', 'time', 'rankcnt']
t1475_OUT_BLOCK_NAME = ['기준일자', '기준시간', '랭크카운터']
t1475_OUT_BLOCK_1_CODE = [
           'datetime', 'price', 'sign', 'change', 'diff', 'volume', 'todayvp', 'ma5vp', 'ma20vp', 'ma60vp']
t1475_OUT_BLOCK_1_NAME = [
           '일자', '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '당일VP', '5일MAVP', '20일MAVP', '60일MAVP']

# t1481
t1481_IN_BLOCK_CODE = ['gubun1', 'gubun2', 'jongchk', 'volume', 'idx']
t1481_IN_BLOCK_NAME = ['구분', '상승하락', '종목체크', '거래량', 'IDX']
t1481_OUT_BLOCK_CODE = ['idx']
t1481_OUT_BLOCK_NAME = ['IDX']
t1481_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'offerrem1', 'bidrem1', 'offerho1', 'bidho1',
           'shcode', 'value']
t1481_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '매도잔량', '매수잔량', '매도호가', '매수호가',
           '종목코드', '누적거래대금']

# t1482
t1482_IN_BLOCK_CODE = ['gubun', 'jongchk', 'idx', 'sort_gbn']
t1482_IN_BLOCK_NAME = ['구분', '거래량', 'IDX', '정렬구분(0:거래량1:거래대금)']
t1482_OUT_BLOCK_CODE = ['idx']
t1482_OUT_BLOCK_NAME = ['IDX']
t1482_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'vol', 'shcode', 'value']
t1482_OUT_BLOCK_1_NAME = [
           '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '회전율', '종목코드', '누적거래대금']

# t1485
t1485_IN_BLOCK_CODE = ['upcode', 'gubun']
t1485_IN_BLOCK_NAME = ['업종코드', '조회구분']
t1485_OUT_BLOCK_CODE = [
           'pricejisu', 'sign', 'change', 'volume', 'yhighjo', 'yupjo', 'yunchgjo', 'ylowjo', 'ydownjo', 'ytrajo']
t1485_OUT_BLOCK_NAME = [
           '현재지수', '지수전일대비구분', '전일대비', '거래량', '상승종목수', '상한종목수', '보합종목수', '하락종목수', '하한종목수', '거래형성수']
t1485_OUT_BLOCK_1_CODE = [
           'chetime', 'jisu', 'sign', 'change', 'volume', 'volcha', 'diff']
t1485_OUT_BLOCK_1_NAME = [
           '시간', '예상지수', '전일대비구분', '전일대비', '예상체결량', '예상체결량직전대비', '예상등락율']

# t1486
t1486_IN_BLOCK_CODE = ['shcode', 'cts_time', 'cnt', 'exchgubun']
t1486_IN_BLOCK_NAME = ['단축코드', '시간CTS', '조회건수', '거래소구분코드']
t1486_OUT_BLOCK_CODE = ['cts_time', 'ex_shcode']
t1486_OUT_BLOCK_NAME = ['시간CTS', '거래소별단축코드']
t1486_OUT_BLOCK_1_CODE = [
           'chetime', 'price', 'sign', 'change', 'diff', 'cvolume', 'offerho1', 'bidho1', 'offerrem1', 'bidrem1',
           'exchname']
t1486_OUT_BLOCK_1_NAME = [
           '시간', '예상체결가', '전일대비구분', '전일대비', '등락율', '예상체결량', '매도호가', '매수호가', '매도잔량', '매수잔량',
           '거래소명']

# t1488
t1488_IN_BLOCK_CODE = [
           'gubun', 'sign', 'jgubun', 'jongchk', 'idx', 'volume', 'yesprice', 'yeeprice', 'yevolume']
t1488_IN_BLOCK_NAME = [
           '거래소구분', '상하락구분', '장구분', '종목체크', 'IDX', '거래량', '예상체결시작가격', '예상체결종료가격', '예상체결량']
t1488_OUT_BLOCK_CODE = ['idx']
t1488_OUT_BLOCK_NAME = ['IDX']
t1488_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'offerrem', 'offerho', 'bidho', 'bidrem',
           'cnt', 'shcode', 'jkrate', 'jnilvolume']
t1488_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '매도잔량', '매도호가', '매수호가', '매수잔량',
           '연속일수', '종목코드', '증거금율', '전일거래량']

# t1489
t1489_IN_BLOCK_CODE = [
           'gubun', 'jgubun', 'jongchk', 'idx', 'yesprice', 'yeeprice', 'yevolume']
t1489_IN_BLOCK_NAME = [
           '거래소구분', '장구분', '종목체크', 'IDX', '예상체결시작가격', '예상체결종료가격', '예상체결량']
t1489_OUT_BLOCK_CODE = ['idx']
t1489_OUT_BLOCK_NAME = ['IDX']
t1489_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'offerho', 'bidho', 'shcode', 'jnilvolume']
t1489_OUT_BLOCK_1_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '예상거래량', '매도호가', '매수호가', '종목코드', '전일거래량']

# t1492
t1492_IN_BLOCK_CODE = ['gubun1', 'gubun2', 'jongchk', 'volume', 'idx']
t1492_IN_BLOCK_NAME = ['구분', '상승하락', '종목체크', '거래량', 'IDX']
t1492_OUT_BLOCK_CODE = ['idx']
t1492_OUT_BLOCK_NAME = ['IDX']
t1492_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'yevolume', 'volume', 'offerrem1', 'bidrem1', 'offerho1',
           'bidho1', 'shcode', 'value']
t1492_OUT_BLOCK_1_NAME = [
           '한글명', '예상체결가', '전일대비구분', '전일대비', '등락율', '예상체결량', '누적거래량', '매도잔량', '매수잔량', '매도호가',
           '매수호가', '종목코드', '누적거래대금']

# t1511
t1511_IN_BLOCK_CODE = ['upcode']
t1511_IN_BLOCK_NAME = ['업종코드']
t1511_OUT_BLOCK_CODE = [
           'gubun', 'hname', 'pricejisu', 'jniljisu', 'sign', 'change', 'diffjisu', 'jnilvolume', 'volume', 'volumechange',
           'volumerate', 'jnilvalue', 'value', 'valuechange', 'valuerate', 'openjisu', 'opendiff', 'opentime', 'highjisu', 'highdiff',
           'hightime', 'lowjisu', 'lowdiff', 'lowtime', 'whjisu', 'whchange', 'whjday', 'wljisu', 'wlchange', 'wljday',
           'yhjisu', 'yhchange', 'yhjday', 'yljisu', 'ylchange', 'yljday', 'firstjcode', 'firstjname', 'firstjisu', 'firsign',
           'firchange', 'firdiff', 'secondjcode', 'secondjname', 'secondjisu', 'secsign', 'secchange', 'secdiff', 'thirdjcode', 'thirdjname',
           'thirdjisu', 'thrsign', 'thrchange', 'thrdiff', 'fourthjcode', 'fourthjname', 'fourthjisu', 'forsign', 'forchange', 'fordiff',
           'highjo', 'upjo', 'unchgjo', 'lowjo', 'downjo']
t1511_OUT_BLOCK_NAME = [
           '업종구분', '업종명', '현재지수', '전일지수', '전일대비구분', '전일대비', '지수등락율', '전일거래량', '당일거래량', '거래량전일대비',
           '거래량비율', '전일거래대금', '당일거래대금', '거래대금전일대비', '거래대금비율', '시가지수', '시가등락율', '시가시간', '고가지수', '고가등락율',
           '고가시간', '저가지수', '저가등락율', '저가시간', '52주최고지수', '52주최고현재가대비', '52주최고지수일자', '52주최저지수', '52주최저현재가대비', '52주최저지수일자',
           '연중최고지수', '연중최고현재가대비', '연중최고지수일자', '연중최저지수', '연중최저현재가대비', '연중최저지수일자', '첫번째지수코드', '첫번째지수명', '첫번째지수', '첫번째대비구분',
           '첫번째전일대비', '첫번째등락율', '두번째지수코드', '두번째지수명', '두번째지수', '두번째대비구분', '두번째전일대비', '두번째등락율', '세번째지수코드', '세번째지수명',
           '세번째지수', '세번째대비구분', '세번째전일대비', '세번째등락율', '네번째지수코드', '네번째지수명', '네번째지수', '네번째대비구분', '네번째전일대비', '네번째등락율',
           '상승종목수', '상한종목수', '보합종목수', '하락종목수', '하한종목수']

# t1514
t1514_IN_BLOCK_CODE = [
           'upcode', 'gubun1', 'gubun2', 'cts_date', 'cnt', 'rate_gbn']
t1514_IN_BLOCK_NAME = [
           '업종코드', '구분1', '구분2', 'CTS_일자', '조회건수', '비중구분']
t1514_OUT_BLOCK_CODE = ['cts_date']
t1514_OUT_BLOCK_NAME = ['CTS_일자']
t1514_OUT_BLOCK_1_CODE = [
           'date', 'jisu', 'sign', 'change', 'diff', 'volume', 'diff_vol', 'value1', 'high', 'unchg',
           'low', 'uprate', 'frgsvolume', 'openjisu', 'highjisu', 'lowjisu', 'value2', 'up', 'down', 'totjo',
           'orgsvolume', 'upcode', 'rate', 'divrate']
t1514_OUT_BLOCK_1_NAME = [
           '일자', '지수', '전일대비구분', '전일대비', '등락율', '거래량', '거래증가율', '거래대금1', '상승', '보합',
           '하락', '상승종목비율', '외인순매수', '시가', '고가', '저가', '거래대금2', '상한', '하한', '종목수',
           '기관순매수', '업종코드', '거래비중', '업종배당수익률']

# t1516
t1516_IN_BLOCK_CODE = ['upcode', 'gubun', 'shcode']
t1516_IN_BLOCK_NAME = ['업종코드', '구분', '종목코드']
t1516_OUT_BLOCK_CODE = ['shcode', 'pricejisu', 'sign', 'change', 'jdiff']
t1516_OUT_BLOCK_NAME = ['종목코드', '지수', '전일대비구분', '전일대비', '등락율']
t1516_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'open', 'high', 'low', 'sojinrate',
           'beta', 'perx', 'frgsvolume', 'orgsvolume', 'diff_vol', 'shcode', 'total', 'value']
t1516_OUT_BLOCK_1_NAME = [
           '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '시가', '고가', '저가', '소진율',
           '베타계수', 'PER', '외인순매수', '기관순매수', '거래증가율', '종목코드', '시가총액', '거래대금']

# t1531
t1531_IN_BLOCK_CODE = ['tmname', 'tmcode']
t1531_IN_BLOCK_NAME = ['테마명', '테마코드']
t1531_OUT_BLOCK_CODE = ['tmname', 'avgdiff', 'tmcode']
t1531_OUT_BLOCK_NAME = ['테마명', '평균등락율', '테마코드']

# t1532
t1532_IN_BLOCK_CODE = ['shcode']
t1532_IN_BLOCK_NAME = ['종목코드']
t1532_OUT_BLOCK_CODE = ['tmname', 'avgdiff', 'tmcode']
t1532_OUT_BLOCK_NAME = ['테마명', '평균등락율', '테마코드']

# t1533
t1533_IN_BLOCK_CODE = ['gubun', 'chgdate']
t1533_IN_BLOCK_NAME = ['구분', '대비일자']
t1533_OUT_BLOCK_CODE = ['bdate']
t1533_OUT_BLOCK_NAME = ['일자']
t1533_OUT_BLOCK_1_CODE = [
           'tmname', 'totcnt', 'upcnt', 'dncnt', 'uprate', 'diff_vol', 'avgdiff', 'chgdiff', 'tmcode']
t1533_OUT_BLOCK_1_NAME = [
           '테마명', '전체', '상승', '하락', '상승비율', '거래증가율', '평균등락율', '대비등락율', '테마코드']

# t1537
t1537_IN_BLOCK_CODE = ['tmcode']
t1537_IN_BLOCK_NAME = ['테마코드']
t1537_OUT_BLOCK_CODE = ['upcnt', 'tmcnt', 'uprate', 'tmname']
t1537_OUT_BLOCK_NAME = ['상승종목수', '테마종목수', '상승종목비율', '테마명']
t1537_OUT_BLOCK_1_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'jniltime', 'shcode', 'yeprice', 'open',
           'high', 'low', 'value', 'marketcap']
t1537_OUT_BLOCK_1_NAME = [
           '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '전일동시간', '종목코드', '예상체결가', '시가',
           '고가', '저가', '누적거래대금(단위:백만)', '시가총액(단위:백만)']

# t1601
t1601_IN_BLOCK_CODE = ['gubun1', 'gubun2', 'gubun3', 'gubun4', 'exchgubun']
t1601_IN_BLOCK_NAME = ['주식금액수량구분1', '옵션금액수량구분2', '금액단위', '선물금액수량구분4', '거래소구분코드']
t1601_OUT_BLOCK_1_CODE = [
           'tjjcode_08', 'ms_08', 'md_08', 'rate_08', 'svolume_08', 'jjcode_17', 'ms_17', 'md_17', 'rate_17', 'svolume_17',
           'jjcode_18', 'ms_18', 'md_18', 'rate_18', 'svolume_18', 'jjcode_01', 'ms_01', 'md_01', 'rate_01', 'svolume_01',
           'jjcode_03', 'ms_03', 'md_03', 'rate_03', 'svolume_03', 'jjcode_04', 'ms_04', 'md_04', 'rate_04', 'svolume_04',
           'jjcode_02', 'ms_02', 'md_02', 'rate_02', 'svolume_02', 'jjcode_05', 'ms_05', 'md_05', 'rate_05', 'svolume_05',
           'jjcode_06', 'ms_06', 'md_06', 'rate_06', 'svolume_06', 'jjcode_11', 'ms_11', 'md_11', 'rate_11', 'svolume_11',
           'jjcode_07', 'ms_07', 'md_07', 'rate_07', 'svolume_07', 'jjcode_00', 'ms_00', 'md_00', 'rate_00', 'svolume_00']
t1601_OUT_BLOCK_1_NAME = [
           '개인투자자코드', '개인매수', '개인매도', '개인증감', '개인순매수', '외국인투자자코드', '외국인매수', '외국인매도', '외국인증감', '외국인순매수',
           '기관계투자자코드', '기관계매수', '기관계매도', '기관계증감', '기관계순매수', '증권투자자코드', '증권매수', '증권매도', '증권증감', '증권순매수',
           '투신투자자코드', '투신매수', '투신매도', '투신증감', '투신순매수', '은행투자자코드', '은행매수', '은행매도', '은행증감', '은행순매수',
           '보험투자자코드', '보험매수', '보험매도', '보험증감', '보험순매수', '종금투자자코드', '종금매수', '종금매도', '종금증감', '종금순매수',
           '기금투자자코드', '기금매수', '기금매도', '기금증감', '기금순매수', '국가투자코드', '국가매수', '국가매도', '국가증감', '국가순매수',
           '기타투자자코드', '기타매수', '기타매도', '기타증감', '기타순매수', '사모펀드투자자코드', '사모펀드매수', '사모펀드매도', '사모펀드증감', '사모펀드순매수']
t1601_OUT_BLOCK_2_CODE = [
           'tjjcode_08', 'ms_08', 'md_08', 'rate_08', 'svolume_08', 'jjcode_17', 'ms_17', 'md_17', 'rate_17', 'svolume_17',
           'jjcode_18', 'ms_18', 'md_18', 'rate_18', 'svolume_18', 'jjcode_01', 'ms_01', 'md_01', 'rate_01', 'svolume_01',
           'jjcode_03', 'ms_03', 'md_03', 'rate_03', 'svolume_03', 'jjcode_04', 'ms_04', 'md_04', 'rate_04', 'svolume_04',
           'jjcode_02', 'ms_02', 'md_02', 'rate_02', 'svolume_02', 'jjcode_05', 'ms_05', 'md_05', 'rate_05', 'svolume_05',
           'jjcode_06', 'ms_06', 'md_06', 'rate_06', 'svolume_06', 'jjcode_11', 'ms_11', 'md_11', 'rate_11', 'svolume_11',
           'jjcode_07', 'ms_07', 'md_07', 'rate_07', 'svolume_07', 'jjcode_00', 'ms_00', 'md_00', 'rate_00', 'svolume_00']
t1601_OUT_BLOCK_2_NAME = [
           '개인투자자코드', '개인매수', '개인매도', '개인증감', '개인순매수', '외국인투자자코드', '외국인매수', '외국인매도', '외국인증감', '외국인순매수',
           '기관계투자자코드', '기관계매수', '기관계매도', '기관계증감', '기관계순매수', '증권투자자코드', '증권매수', '증권매도', '증권증감', '증권순매수',
           '투신투자자코드', '투신매수', '투신매도', '투신증감', '투신순매수', '은행투자자코드', '은행매수', '은행매도', '은행증감', '은행순매수',
           '보험투자자코드', '보험매수', '보험매도', '보험증감', '보험순매수', '종금투자자코드', '종금매수', '종금매도', '종금증감', '종금순매수',
           '기금투자자코드', '기금매수', '기금매도', '기금증감', '기금순매수', '국가투자코드', '국가매수', '국가매도', '국가증감', '국가순매수',
           '기타투자자코드', '기타매수', '기타매도', '기타증감', '기타순매수', '사모펀드투자자코드', '사모펀드매수', '사모펀드매도', '사모펀드증감', '사모펀드순매수']
t1601_OUT_BLOCK_3_CODE = [
           'tjjcode_08', 'ms_08', 'md_08', 'rate_08', 'svolume_08', 'jjcode_17', 'ms_17', 'md_17', 'rate_17', 'svolume_17',
           'jjcode_18', 'ms_18', 'md_18', 'rate_18', 'svolume_18', 'jjcode_01', 'ms_01', 'md_01', 'rate_01', 'svolume_01',
           'jjcode_03', 'ms_03', 'md_03', 'rate_03', 'svolume_03', 'jjcode_04', 'ms_04', 'md_04', 'rate_04', 'svolume_04',
           'jjcode_02', 'ms_02', 'md_02', 'rate_02', 'svolume_02', 'jjcode_05', 'ms_05', 'md_05', 'rate_05', 'svolume_05',
           'jjcode_06', 'ms_06', 'md_06', 'rate_06', 'svolume_06', 'jjcode_11', 'ms_11', 'md_11', 'rate_11', 'svolume_11',
           'jjcode_07', 'ms_07', 'md_07', 'rate_07', 'svolume_07', 'jjcode_00', 'ms_00', 'md_00', 'rate_00', 'svolume_00']
t1601_OUT_BLOCK_3_NAME = [
           '개인투자자코드', '개인매수', '개인매도', '개인증감', '개인순매수', '외국인투자자코드', '외국인매수', '외국인매도', '외국인증감', '외국인순매수',
           '기관계투자자코드', '기관계매수', '기관계매도', '기관계증감', '기관계순매수', '증권투자자코드', '증권매수', '증권매도', '증권증감', '증권순매수',
           '투신투자자코드', '투신매수', '투신매도', '투신증감', '투신순매수', '은행투자자코드', '은행매수', '은행매도', '은행증감', '은행순매수',
           '보험투자자코드', '보험매수', '보험매도', '보험증감', '보험순매수', '종금투자자코드', '종금매수', '종금매도', '종금증감', '종금순매수',
           '기금투자자코드', '기금매수', '기금매도', '기금증감', '기금순매수', '국가투자코드', '국가매수', '국가매도', '국가증감', '국가순매수',
           '기타투자자코드', '기타매수', '기타매도', '기타증감', '기타순매수', '사모펀드투자자코드', '사모펀드매수', '사모펀드매도', '사모펀드증감', '사모펀드순매수']
t1601_OUT_BLOCK_4_CODE = [
           'tjjcode_08', 'ms_08', 'md_08', 'rate_08', 'svolume_08', 'jjcode_17', 'ms_17', 'md_17', 'rate_17', 'svolume_17',
           'jjcode_18', 'ms_18', 'md_18', 'rate_18', 'svolume_18', 'jjcode_01', 'ms_01', 'md_01', 'rate_01', 'svolume_01',
           'jjcode_03', 'ms_03', 'md_03', 'rate_03', 'svolume_03', 'jjcode_04', 'ms_04', 'md_04', 'rate_04', 'svolume_04',
           'jjcode_02', 'ms_02', 'md_02', 'rate_02', 'svolume_02', 'jjcode_05', 'ms_05', 'md_05', 'rate_05', 'svolume_05',
           'jjcode_06', 'ms_06', 'md_06', 'rate_06', 'svolume_06', 'jjcode_11', 'ms_11', 'md_11', 'rate_11', 'svolume_11',
           'jjcode_07', 'ms_07', 'md_07', 'rate_07', 'svolume_07', 'jjcode_00', 'ms_00', 'md_00', 'rate_00', 'svolume_00']
t1601_OUT_BLOCK_4_NAME = [
           '개인투자자코드', '개인매수', '개인매도', '개인증감', '개인순매수', '외국인투자자코드', '외국인매수', '외국인매도', '외국인증감', '외국인순매수',
           '기관계투자자코드', '기관계매수', '기관계매도', '기관계증감', '기관계순매수', '증권투자자코드', '증권매수', '증권매도', '증권증감', '증권순매수',
           '투신투자자코드', '투신매수', '투신매도', '투신증감', '투신순매수', '은행투자자코드', '은행매수', '은행매도', '은행증감', '은행순매수',
           '보험투자자코드', '보험매수', '보험매도', '보험증감', '보험순매수', '종금투자자코드', '종금매수', '종금매도', '종금증감', '종금순매수',
           '기금투자자코드', '기금매수', '기금매도', '기금증감', '기금순매수', '국가투자코드', '국가매수', '국가매도', '국가증감', '국가순매수',
           '기타투자자코드', '기타매수', '기타매도', '기타증감', '기타순매수', '사모펀드투자자코드', '사모펀드매수', '사모펀드매도', '사모펀드증감', '사모펀드순매수']
t1601_OUT_BLOCK_5_CODE = [
           'tjjcode_08', 'ms_08', 'md_08', 'rate_08', 'svolume_08', 'jjcode_17', 'ms_17', 'md_17', 'rate_17', 'svolume_17',
           'jjcode_18', 'ms_18', 'md_18', 'rate_18', 'svolume_18', 'jjcode_01', 'ms_01', 'md_01', 'rate_01', 'svolume_01',
           'jjcode_03', 'ms_03', 'md_03', 'rate_03', 'svolume_03', 'jjcode_04', 'ms_04', 'md_04', 'rate_04', 'svolume_04',
           'jjcode_02', 'ms_02', 'md_02', 'rate_02', 'svolume_02', 'jjcode_05', 'ms_05', 'md_05', 'rate_05', 'svolume_05',
           'jjcode_06', 'ms_06', 'md_06', 'rate_06', 'svolume_06', 'jjcode_11', 'ms_11', 'md_11', 'rate_11', 'svolume_11',
           'jjcode_07', 'ms_07', 'md_07', 'rate_07', 'svolume_07', 'jjcode_00', 'ms_00', 'md_00', 'rate_00', 'svolume_00']
t1601_OUT_BLOCK_5_NAME = [
           '개인투자자코드', '개인매수', '개인매도', '개인증감', '개인순매수', '외국인투자자코드', '외국인매수', '외국인매도', '외국인증감', '외국인순매수',
           '기관계투자자코드', '기관계매수', '기관계매도', '기관계증감', '기관계순매수', '증권투자자코드', '증권매수', '증권매도', '증권증감', '증권순매수',
           '투신투자자코드', '투신매수', '투신매도', '투신증감', '투신순매수', '은행투자자코드', '은행매수', '은행매도', '은행증감', '은행순매수',
           '보험투자자코드', '보험매수', '보험매도', '보험증감', '보험순매수', '종금투자자코드', '종금매수', '종금매도', '종금증감', '종금순매수',
           '기금투자자코드', '기금매수', '기금매도', '기금증감', '기금순매수', '국가투자코드', '국가매수', '국가매도', '국가증감', '국가순매수',
           '기타투자자코드', '기타매수', '기타매도', '기타증감', '기타순매수', '사모펀드투자자코드', '사모펀드매수', '사모펀드매도', '사모펀드증감', '사모펀드순매수']
t1601_OUT_BLOCK_6_CODE = [
           'tjjcode_08', 'ms_08', 'md_08', 'rate_08', 'svolume_08', 'jjcode_17', 'ms_17', 'md_17', 'rate_17', 'svolume_17',
           'jjcode_18', 'ms_18', 'md_18', 'rate_18', 'svolume_18', 'jjcode_01', 'ms_01', 'md_01', 'rate_01', 'svolume_01',
           'jjcode_03', 'ms_03', 'md_03', 'rate_03', 'svolume_03', 'jjcode_04', 'ms_04', 'md_04', 'rate_04', 'svolume_04',
           'jjcode_02', 'ms_02', 'md_02', 'rate_02', 'svolume_02', 'jjcode_05', 'ms_05', 'md_05', 'rate_05', 'svolume_05',
           'jjcode_06', 'ms_06', 'md_06', 'rate_06', 'svolume_06', 'jjcode_11', 'ms_11', 'md_11', 'rate_11', 'svolume_11',
           'jjcode_07', 'ms_07', 'md_07', 'rate_07', 'svolume_07', 'jjcode_00', 'ms_00', 'md_00', 'rate_00', 'svolume_00']
t1601_OUT_BLOCK_6_NAME = [
           '개인투자자코드', '개인매수', '개인매도', '개인증감', '개인순매수', '외국인투자자코드', '외국인매수', '외국인매도', '외국인증감', '외국인순매수',
           '기관계투자자코드', '기관계매수', '기관계매도', '기관계증감', '기관계순매수', '증권투자자코드', '증권매수', '증권매도', '증권증감', '증권순매수',
           '투신투자자코드', '투신매수', '투신매도', '투신증감', '투신순매수', '은행투자자코드', '은행매수', '은행매도', '은행증감', '은행순매수',
           '보험투자자코드', '보험매수', '보험매도', '보험증감', '보험순매수', '종금투자자코드', '종금매수', '종금매도', '종금증감', '종금순매수',
           '기금투자자코드', '기금매수', '기금매도', '기금증감', '기금순매수', '국가투자코드', '국가매수', '국가매도', '국가증감', '국가순매수',
           '기타투자자코드', '기타매수', '기타매도', '기타증감', '기타순매수', '사모펀드투자자코드', '사모펀드매수', '사모펀드매도', '사모펀드증감', '사모펀드순매수']

# t1602
t1602_IN_BLOCK_CODE = [
           'market', 'upcode', 'gubun1', 'gubun2', 'cts_time', 'cts_idx', 'cnt', 'gubun3', 'exchgubun']
t1602_IN_BLOCK_NAME = [
           '시장구분', '업종코드', '수량구분', '전일분구분', 'CTSTIME', 'CTSIDX', '조회건수', '직전대비구분(C:직전대비)', '거래소구분코드']
t1602_OUT_BLOCK_CODE = [
           'cts_time', 'tjjcode_08', 'ms_08', 'md_08', 'rate_08', 'svolume_08', 'jjcode_17', 'ms_17', 'md_17', 'rate_17',
           'svolume_17', 'jjcode_18', 'ms_18', 'md_18', 'rate_18', 'svolume_18', 'jjcode_01', 'ms_01', 'md_01', 'rate_01',
           'svolume_01', 'jjcode_03', 'ms_03', 'md_03', 'rate_03', 'svolume_03', 'jjcode_04', 'ms_04', 'md_04', 'rate_04',
           'svolume_04', 'jjcode_02', 'ms_02', 'md_02', 'rate_02', 'svolume_02', 'jjcode_05', 'ms_05', 'md_05', 'rate_05',
           'svolume_05', 'jjcode_06', 'ms_06', 'md_06', 'rate_06', 'svolume_06', 'jjcode_07', 'ms_07', 'md_07', 'rate_07',
           'svolume_07', 'jjcode_11', 'ms_11', 'md_11', 'rate_11', 'svolume_11', 'jjcode_00', 'ms_00', 'md_00', 'rate_00',
           'svolume_00', 'ex_upcode']
t1602_OUT_BLOCK_NAME = [
           'CTSTIME', '개인투자자코드', '개인매수', '개인매도', '개인증감', '개인순매수', '외국인투자자코드', '외국인매수', '외국인매도', '외국인증감',
           '외국인순매수', '기관계투자자코드', '기관계매수', '기관계매도', '기관계증감', '기관계순매수', '증권투자자코드', '증권매수', '증권매도', '증권증감',
           '증권순매수', '투신투자자코드', '투신매수', '투신매도', '투신증감', '투신순매수', '은행투자자코드', '은행매수', '은행매도', '은행증감',
           '은행순매수', '보험투자자코드', '보험매수', '보험매도', '보험증감', '보험순매수', '종금투자자코드', '종금매수', '종금매도', '종금증감',
           '종금순매수', '기금투자자코드', '기금매수', '기금매도', '기금증감', '기금순매수', '기타투자자코드', '기타매수', '기타매도', '기타증감',
           '기타순매수', '국가투자자코드', '국가매수', '국가매도', '국가증감', '국가순매수', '사모펀드코드', '사모펀드매수', '사모펀드매도', '사모펀드증감',
           '사모펀드순매수', '거래소별업종코드']
t1602_OUT_BLOCK_1_CODE = [
           'time', 'sv_08', 'sv_17', 'sv_18', 'sv_01', 'sv_03', 'sv_04', 'sv_02', 'sv_05', 'sv_06',
           'sv_07', 'sv_11', 'sv_00']
t1602_OUT_BLOCK_1_NAME = [
           '시간', '개인순매수', '외국인순매수', '기관계순매수', '증권순매수', '투신순매수', '은행순매수', '보험순매수', '종금순매수', '기금순매수',
           '기타순매수', '국가순매수', '사모펀드순매수']

# t1603
t1603_IN_BLOCK_CODE = [
           'market', 'gubun1', 'gubun2', 'cts_time', 'cts_idx', 'cnt', 'upcode', 'exchgubun']
t1603_IN_BLOCK_NAME = [
           '시장구분', '투자자구분', '전일분구분', 'CTSTIME', 'CTSIDX', '조회건수', '업종코드', '거래소구분코드']
t1603_OUT_BLOCK_CODE = ['cts_idx', 'cts_time', 'ex_upcode']
t1603_OUT_BLOCK_NAME = ['CTSIDX', 'CTSTIME', '거래소별업종코드']
t1603_OUT_BLOCK_1_CODE = [
           'time', 'tjjcode', 'msvolume', 'mdvolume', 'msvalue', 'mdvalue', 'svolume', 'svalue']
t1603_OUT_BLOCK_1_NAME = [
           '시간', '투자자구분', '매수수량', '매도수량', '매수금액', '매도금액', '순매수수량', '순매수금액']

# t1615
t1615_IN_BLOCK_CODE = ['gubun1', 'gubun2', 'exchgubun']
t1615_IN_BLOCK_NAME = ['주식구분', '옵션구분', '거래소구분코드']
t1615_OUT_BLOCK_CODE = [
           'dwvolume', 'dwvalue', 'djvolume', 'djvalue', 'sum_volume', 'sum_value']
t1615_OUT_BLOCK_NAME = [
           '위탁매도수량', '위탁매도금액', '자기매도수량', '자기매도금액', '합계수량', '합계금액']
t1615_OUT_BLOCK_1_CODE = ['hname', 'sv_08', 'sv_17', 'sv_18', 'sv_07']
t1615_OUT_BLOCK_1_NAME = ['시장명', '개인', '외국인', '기관계', '증권']

# t1617
t1617_IN_BLOCK_CODE = [
           'gubun1', 'gubun2', 'gubun3', 'cts_date', 'cts_time', 'gubun4', 'exchgubun']
t1617_IN_BLOCK_NAME = [
           '시장구분(1:코스피2:코스닥3:선물4:콜5:풋6:주식선물7:V선물8:M선물9:M콜0:M풋E:유로스톡스)', '수량금액구분(1:수량2:금액)', '일자구분(1:시간대별2:일별)', 'CTSDATE(연속키값-일자)', 'CTSTIME(연속키값-시간)', '직전대비증감(C:직전대비)', '거래소구분코드']
t1617_OUT_BLOCK_CODE = [
           'cts_date', 'cts_time', 'ms_08', 'md_08', 'sv_08', 'ms_17', 'md_17', 'sv_17', 'ms_18', 'md_18',
           'sv_18', 'ms_01', 'md_01', 'sv_01']
t1617_OUT_BLOCK_NAME = [
           'CTSDATE', 'CTSTIME', '개인매수', '개인매도', '개인순매수', '외국인매수', '외국인매도', '외국인순매수', '기관계매수', '기관계매도',
           '기관계순매수', '증권매수', '증권매도', '증권순매수']
t1617_OUT_BLOCK_1_CODE = [
           'date', 'time', 'sv_08', 'sv_17', 'sv_18', 'sv_01']
t1617_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '개인', '외국인', '기관계', '증권']

# t1621
t1621_IN_BLOCK_CODE = ['upcode', 'nmin', 'cnt', 'bgubun', 'exchgubun']
t1621_IN_BLOCK_NAME = ['업종코드', 'N분', '조회건수', '전일분', '거래소구분코드']
t1621_OUT_BLOCK_CODE = [
           'indcode', 'forcode', 'syscode', 'stocode', 'invcode', 'bancode', 'inscode', 'fincode', 'moncode', 'etccode',
           'natcode', 'pefcode', 'jisucd', 'jisunm', 'ex_upcode']
t1621_OUT_BLOCK_NAME = [
           '개인투자자코드', '외국인투자자코드', '기관계투자자코드', '증권투자자코드', '투신투자자코드', '은행투자자코드', '보험투자자코드', '종금투자자코드', '기금투자자코드', '기타투자자코드',
           '국가투자자코드', '사모펀드투자자코드', '기준지수코드', '기준지수명', '거래소별업종코드']
t1621_OUT_BLOCK_1_CODE = [
           'date', 'time', 'datetime', 'indmsvol', 'indmsamt', 'formsvol', 'formsamt', 'sysmsvol', 'sysmsamt', 'stomsvol',
           'stomsamt', 'invmsvol', 'invmsamt', 'banmsvol', 'banmsamt', 'insmsvol', 'insmsamt', 'finmsvol', 'finmsamt', 'monmsvol',
           'monmsamt', 'etcmsvol', 'etcmsamt', 'natmsvol', 'natmsamt', 'pefmsvol', 'pefmsamt', 'upclose', 'upcvolume', 'upvolume',
           'upvalue']
t1621_OUT_BLOCK_1_NAME = [
           '일자', '시간', '일자시간', '개인순매수거래량', '개인순매수거래대금', '외국인순매수거래량', '외국인순매수거래대금', '기관계순매수거래량', '기관계순매수거래대금', '증권순매수거래량',
           '증권순매수거래대금', '투신순매수거래량', '투신순매수거래대금', '은행순매수거래량', '은행순매수거래대금', '보험순매수거래량', '보험순매수거래대금', '종금순매수거래량', '종금순매수거래대금', '기금순매수거래량',
           '기금순매수거래대금', '기타순매수거래량', '기타순매수거래대금', '국가순매수거래량', '국가순매수거래대금', '사모펀드순매수거래량', '사모펀드순매수거래대금', '기준지수', '기준체결거래량', '기준누적거래량',
           '기준거래대금']

# t1631
t1631_IN_BLOCK_CODE = ['gubun', 'dgubun', 'sdate', 'edate', 'exchgubun']
t1631_IN_BLOCK_NAME = ['구분', '일자구분', '시작일자', '종료일자', '거래소구분코드']
t1631_OUT_BLOCK_CODE = [
           'cdhrem', 'bdhrem', 'tcdrem', 'tbdrem', 'cshrem', 'bshrem', 'tcsrem', 'tbsrem']
t1631_OUT_BLOCK_NAME = [
           '매도차익미체결잔량', '매도비차익미체결잔량', '매도차익주문수량', '매도비차익주문수량', '매수차익미체결잔량', '매수비차익미체결잔량', '매수차익주문수량', '매수비차익주문수량']
t1631_OUT_BLOCK_1_CODE = [
           'offervolume', 'offervalue', 'bidvolume', 'bidvalue', 'volume', 'value']
t1631_OUT_BLOCK_1_NAME = [
           '매도수량', '매도금액', '매수수량', '매수금액', '순매수수량', '순매수금액']

# t1632
t1632_IN_BLOCK_CODE = [
           'gubun', 'gubun1', 'gubun2', 'gubun3', 'date', 'time', 'exchgubun']
t1632_IN_BLOCK_NAME = [
           '구분', '금액수량구분', '직전대비증감', '전일구분', '일자', '시간', '거래소구분코드']
t1632_OUT_BLOCK_CODE = ['date', 'time', 'ex_gubun']
t1632_OUT_BLOCK_NAME = ['날짜CTS', '시간CTS', '거래소별구분코드']
t1632_OUT_BLOCK_1_CODE = [
           'time', 'k200jisu', 'sign', 'change', 'k200basis', 'tot3', 'tot1', 'tot2', 'cha3', 'cha1',
           'cha2', 'bcha3', 'bcha1', 'bcha2']
t1632_OUT_BLOCK_1_NAME = [
           '시간', 'KP200', '대비구분', '대비', 'BASIS', '전체순매수', '전체매수', '전체매도', '차익순매수', '차익매수',
           '차익매도', '비차익순매수', '비차익매수', '비차익매도']

# t1633
t1633_IN_BLOCK_CODE = [
           'gubun', 'gubun1', 'gubun2', 'gubun3', 'fdate', 'tdate', 'gubun4', 'date', 'exchgubun']
t1633_IN_BLOCK_NAME = [
           '시장구분', '금액수량구분', '수치누적구분', '일주월구분', 'from일자', 'to일자', '직전대비증감구분', '날짜', '거래소구분코드']
t1633_OUT_BLOCK_CODE = ['date', 'idx']
t1633_OUT_BLOCK_NAME = ['날짜', 'IDX']
t1633_OUT_BLOCK_1_CODE = [
           'date', 'jisu', 'sign', 'change', 'tot3', 'tot1', 'tot2', 'cha3', 'cha1', 'cha2',
           'bcha3', 'bcha1', 'bcha2', 'volume']
t1633_OUT_BLOCK_1_NAME = [
           '일자', 'KP200', '대비구분', '대비', '전체순매수', '전체매수', '전체매도', '차익순매수', '차익매수', '차익매도',
           '비차익순매수', '비차익매수', '비차익매도', '거래량']

# t1636
t1636_IN_BLOCK_CODE = [
           'gubun', 'gubun1', 'gubun2', 'shcode', 'cts_idx', 'exchgubun']
t1636_IN_BLOCK_NAME = [
           '구분', '금액수량구분', '정렬기준', '종목코드', 'IDXCTS', '거래소구분코드']
t1636_OUT_BLOCK_CODE = ['cts_idx']
t1636_OUT_BLOCK_NAME = ['IDXCTS']
t1636_OUT_BLOCK_1_CODE = [
           'rank', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'svalue', 'offervalue', 'stksvalue',
           'svolume', 'offervolume', 'stksvolume', 'sgta', 'rate', 'shcode', 'ex_shcode', 'mkcap_cmpr_val']
t1636_OUT_BLOCK_1_NAME = [
           '순위', '종목명', '현재가', '대비구분', '대비', '등락율', '거래량', '순매수금액', '매도금액', '매수금액',
           '순매수수량', '매도수량', '매수수량', '시가총액', '비중', '종목코드', '거래소별단축코드', '시총대비순매수비중']

# t1637
t1637_IN_BLOCK_CODE = [
           'gubun1', 'gubun2', 'shcode', 'date', 'time', 'cts_idx', 'exchgubun']
t1637_IN_BLOCK_NAME = [
           '수량금액구분(0:수량1:금액)', '시간일별구분(0:시간1:일자)', '종목코드', '일자', '시간', 'IDXCTS(9999:차트)', '거래소구분코드']
t1637_OUT_BLOCK_CODE = ['cts_idx']
t1637_OUT_BLOCK_NAME = ['IDXCTS']
t1637_OUT_BLOCK_1_CODE = [
           'date', 'time', 'price', 'sign', 'change', 'diff', 'volume', 'svalue', 'offervalue', 'stksvalue',
           'svolume', 'offervolume', 'stksvolume', 'shcode', 'ex_shcode']
t1637_OUT_BLOCK_1_NAME = [
           '일자', '시간', '현재가', '대비구분', '대비', '등락율', '거래량', '순매수금액', '매도금액', '매수금액',
           '순매수수량', '매도수량', '매수수량', '종목코드', '거래소별단축코드']

# t1638
t1638_IN_BLOCK_CODE = ['gubun1', 'shcode', 'gubun2', 'exchgubun']
t1638_IN_BLOCK_NAME = ['구분', '종목코드', '정렬', '거래소구분코드']
t1638_OUT_BLOCK_CODE = [
           'rank', 'hname', 'price', 'sign', 'change', 'diff', 'sigatotrt', 'obuyvol', 'buyrem', 'psgvolume',
           'sellrem', 'pdgvolume', 'sigatot', 'shcode']
t1638_OUT_BLOCK_NAME = [
           '순위', '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '시총비중', '순매수잔량', '매수잔량', '매수공시수량',
           '매도잔량', '매도공시수량', '시가총액', '종목코드']

# t1640
t1640_IN_BLOCK_CODE = ['gubun', 'exchgubun']
t1640_IN_BLOCK_NAME = ['구분', '거래소구분코드']
t1640_OUT_BLOCK_CODE = [
           'offervolume', 'bidvolume', 'volume', 'offerdiff', 'biddiff', 'sundiff', 'basis', 'offervalue', 'bidvalue', 'value',
           'offervaldiff', 'bidvaldiff', 'sunvaldiff']
t1640_OUT_BLOCK_NAME = [
           '매도수량', '매수수량', '순매수수량', '매도증감', '매수증감', '순매수증감', '베이시스', '매도금액', '매수금액', '순매수금액',
           '매도금액증감', '매수금액증감', '순매수증감']

# t1662
t1662_IN_BLOCK_CODE = ['gubun', 'gubun1', 'gubun3', 'exchgubun']
t1662_IN_BLOCK_NAME = ['구분', '금액수량구분', '전일구분', '거래소구분코드']
t1662_OUT_BLOCK_CODE = [
           'time', 'k200jisu', 'sign', 'change', 'k200basis', 'tot3', 'tot1', 'tot2', 'cha3', 'cha1',
           'cha2', 'bcha3', 'bcha1', 'bcha2', 'volume']
t1662_OUT_BLOCK_NAME = [
           '시간', 'KP200', '대비구분', '대비', 'BASIS', '전체순매수', '전체매수', '전체매도', '차익순매수', '차익매수',
           '차익매도', '비차익순매수', '비차익매수', '비차익매도', '거래량']

# t1664
t1664_IN_BLOCK_CODE = ['mgubun', 'vagubun', 'bdgubun', 'cnt', 'exchgubun']
t1664_IN_BLOCK_NAME = ['시장구분', '금액수량구분', '시간일별구분', '조회건수', '거래소구분코드']
t1664_OUT_BLOCK_1_CODE = [
           'dt', 'tjj01', 'tjj02', 'tjj03', 'tjj04', 'tjj05', 'tjj06', 'tjj07', 'tjj08', 'tjj17',
           'tjj18', 'cha', 'bicha', 'totcha', 'basis']
t1664_OUT_BLOCK_1_NAME = [
           '일자시간', '증권순매수', '보험순매수', '투신순매수', '은행순매수', '종금순매수', '기금순매수', '기타순매수', '개인순매수', '외국인순매수',
           '기관순매수', '차익순매수', '비차익순매수', '종합순매수', '베이시스']

# t1665
t1665_IN_BLOCK_CODE = [
           'market', 'upcode', 'gubun2', 'gubun3', 'from_date', 'to_date', 'exchgubun']
t1665_IN_BLOCK_NAME = [
           '시장구분(1:kospi2:kp2003:kosdaq4:선물5:풋옵션6:콜옵션)', '업종코드', '수치구분(1:수치2:누적)', '단위구분(1:일2:주3:월)', '시작날짜', '종료날짜', '거래소구분코드']
t1665_OUT_BLOCK_CODE = ['mcode', 'mname', 'ex_upcode']
t1665_OUT_BLOCK_NAME = ['시장코드', '시장명', '거래소별업종코드']
t1665_OUT_BLOCK_1_CODE = [
           'date', 'sv_08', 'sv_17', 'sv_18', 'sv_01', 'sv_03', 'sv_04', 'sv_02', 'sv_05', 'sv_06',
           'sv_07', 'sv_00', 'sv_09', 'sv_10', 'sv_11', 'sv_99', 'sa_08', 'sa_17', 'sa_18', 'sa_01',
           'sa_03', 'sa_04', 'sa_02', 'sa_05', 'sa_06', 'sa_07', 'sa_00', 'sa_09', 'sa_10', 'sa_11',
           'sa_99', 'jisu']
t1665_OUT_BLOCK_1_NAME = [
           '일자', '개인수량', '외인계수량(등록+미등록)', '기관계수량', '증권수량', '투신수량', '은행수량', '보험수량', '종금수량', '기금수량',
           '기타수량', '사모펀드수량', '등록외국인수량', '미등록외국인수량', '국가수량', '기타계수량(기타+국가)', '개인금액', '외인계금액(등록+미등록)', '기관계금액', '증권금액',
           '투신금액', '은행금액', '보험금액', '종금금액', '기금금액', '기타금액', '사모펀드금액', '등록외국인금액', '미등록외국인금액', '국가금액',
           '기타계금액(기타+국가)', '시장지수']

# t1702
t1702_IN_BLOCK_CODE = [
           'shcode', 'fromdt', 'todt', 'volvalgb', 'msmdgb', 'gubun', 'exchgubun']
t1702_IN_BLOCK_NAME = [
           '종목코드', '시작일자', '종료일자', '금액수량구분(0:금액1:수량2:단가)', '매수매도구분(0:순매수1:매수2:매도)', '누적구분(0:일간1:누적)', '거래소구분코드']
t1702_OUT_BLOCK_1_CODE = [
           'date', 'close', 'sign', 'change', 'diff', 'volume', 'tjj0000', 'tjj0001', 'tjj0002', 'tjj0003',
           'tjj0004', 'tjj0005', 'tjj0006', 'tjj0007', 'tjj0008', 'tjj0009', 'tjj0010', 'tjj0011', 'tjj0018', 'tjj0016',
           'tjj0017', 'value']
t1702_OUT_BLOCK_1_NAME = [
           '일자', '종가', '전일대비구분', '전일대비', '등락율', '누적거래량', '사모펀드', '증권', '보험', '투신',
           '은행', '종금', '기금', '기타법인', '개인', '등록외국인', '미등록외국인', '국가외', '기관', '외인계(등록+미등록)',
           '기타계(기타+국가)', '거래대금']

# t1716
t1716_IN_BLOCK_CODE = [
           'shcode', 'gubun', 'fromdt', 'todt', 'prapp', 'prgubun', 'orggubun', 'frggubun', 'exchgubun']
t1716_IN_BLOCK_NAME = [
           '종목코드', '구분(0:일간순매수1:기간누적순매수)', '시작일자', '종료일자', 'PR감산적용율', 'PR적용구분(0:적용안함1:적용)', '기관적용', '외인적용', '거래소구분코드']
t1716_OUT_BLOCK_CODE = [
           'date', 'close', 'sign', 'change', 'diff', 'volume', 'krx_0008', 'krx_0018', 'krx_0009', 'pgmvol',
           'fsc_listing', 'fsc_sjrate', 'fsc_0009', 'gm_volume', 'gm_value']
t1716_OUT_BLOCK_NAME = [
           '일자', '종가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래소_개인', '거래소_기관', '거래소_외국인', '프로그램',
           '금감원_외인보유주식수', '금감원_소진율', '금감원_외국인', '공매도수량', '공매도대금']

# t1717
t1717_IN_BLOCK_CODE = [
           'shcode', 'gubun', 'fromdt', 'todt', 'dan_gb', 'exchgubun']
t1717_IN_BLOCK_NAME = [
           '종목코드', '구분(0:일간순매수1:기간누적순매수)', '시작일자(일간조회일경우는space)', '종료일자', '단가구분(0:전체1:매수혹은매도단가)', '거래소구분코드']
t1717_OUT_BLOCK_CODE = [
           'date', 'close', 'sign', 'change', 'diff', 'volume', 'tjj0000_vol', 'tjj0001_vol', 'tjj0002_vol', 'tjj0003_vol',
           'tjj0004_vol', 'tjj0005_vol', 'tjj0006_vol', 'tjj0007_vol', 'tjj0008_vol', 'tjj0009_vol', 'tjj0010_vol', 'tjj0011_vol', 'tjj0018_vol', 'tjj0016_vol',
           'tjj0017_vol', 'tjj0000_dan', 'tjj0001_dan', 'tjj0002_dan', 'tjj0003_dan', 'tjj0004_dan', 'tjj0005_dan', 'tjj0006_dan', 'tjj0007_dan', 'tjj0008_dan',
           'tjj0009_dan', 'tjj0010_dan', 'tjj0011_dan', 'tjj0018_dan', 'tjj0016_dan', 'tjj0017_dan']
t1717_OUT_BLOCK_NAME = [
           '일자', '종가', '전일대비구분', '전일대비', '등락율', '누적거래량', '사모펀드(순매수량)', '증권(순매수량)', '보험(순매수량)', '투신(순매수량)',
           '은행(순매수량)', '종금(순매수량)', '기금(순매수량)', '기타법인(순매수량)', '개인(순매수량)', '등록외국인(순매수량)', '미등록외국인(순매수량)', '국가외(순매수량)', '기관(순매수량)', '외인계(순매수량)(등록+미등록)',
           '기타계(순매수량)(기타+국가)', '사모펀드(단가)', '증권(단가)', '보험(단가)', '투신(단가)', '은행(단가)', '종금(단가)', '기금(단가)', '기타법인(단가)', '개인(단가)',
           '등록외국인(단가)', '미등록외국인(단가)', '국가외(단가)', '기관(단가)', '외인계(단가)(등록+미등록)', '기타계(단가)(기타+국가)']

# t1752
t1752_IN_BLOCK_CODE = [
           'shcode', 'traddate1', 'traddate2', 'fwgubun1', 'cts_idx', 'exchgubun']
t1752_IN_BLOCK_NAME = [
           '종목코드', '조회날짜1', '조회날짜2', '외국계구분', 'CTSIDX', '거래소구분코드']
t1752_OUT_BLOCK_CODE = ['fwdvl', 'fwsvl', 'cts_idx']
t1752_OUT_BLOCK_NAME = ['외국계매도', '외국계매수', 'CTSIDX']
t1752_OUT_BLOCK_1_CODE = [
           'tradname', 'tradmdvol', 'tradmsvol', 'tradmssvol', 'wintrd', 'winrat', 'tradno', 'wgubun', 'swinrat']
t1752_OUT_BLOCK_1_NAME = [
           '회원사', '매도수량', '매수수량', '순매수', '창구거래', '비중', '회원사코드', '외국계여부', '순비중']

# t1764
t1764_IN_BLOCK_CODE = ['shcode', 'gubun1']
t1764_IN_BLOCK_NAME = ['종목코드', '구분1']
t1764_OUT_BLOCK_CODE = ['rank', 'tradno', 'tradname']
t1764_OUT_BLOCK_NAME = ['순위', '거래원번호', '거래원이름']

# t1771
t1771_IN_BLOCK_CODE = [
           'shcode', 'tradno', 'gubun1', 'traddate1', 'traddate2', 'cts_idx', 'cnt', 'exchgubun']
t1771_IN_BLOCK_NAME = [
           '종목코드', '거래원코드', '구분1', '거래원날짜1', '거래원날짜2', 'CTSIDX', '요청건수', '거래소구분']
t1771_OUT_BLOCK_CODE = ['cts_idx']
t1771_OUT_BLOCK_NAME = ['CTSIDX']
t1771_OUT_BLOCK_2_CODE = [
           'traddate', 'tradtime', 'price', 'sign', 'change', 'diff', 'volume', 'tradmdcha', 'tradmscha', 'tradmdval',
           'tradmsval', 'tradmsscha', 'tradmttvolume', 'tradavg', 'tradmttavg', 'exchname', 'ex_shcode']
t1771_OUT_BLOCK_2_NAME = [
           '날짜', '시간', '현재가', '대비구분', '대비', '등락율', '거래량', '매도', '매수', '매도대금',
           '매수대금', '순매수', '누적순매수', '평균단가', '누적평균단가', '거래소명', '거래소별단축코드']

# t1809
t1809_IN_BLOCK_CODE = ['gubun', 'jmGb', 'jmcode', 'cts']
t1809_IN_BLOCK_NAME = ['신호구분', '종목구분', '종목코드', 'NEXTKEY']
t1809_OUT_BLOCK_CODE = ['cts']
t1809_OUT_BLOCK_NAME = ['NEXTKEY']
t1809_OUT_BLOCK_1_CODE = [
           'date', 'time', 'signal_id', 'signal_desc', 'point', 'keyword', 'seq', 'gubun', 'jmcode', 'price',
           'sign', 'chgrate', 'volume', 'datetime']
t1809_OUT_BLOCK_1_NAME = [
           '일자', '시간', '신호ID', '신호명', '신호강도', '뉴스신호키워드', '신호별구분', '신호구분', '신호종목', '종목가격',
           '종목등락부호', '대비등락율', '거래량', '신호일시']

# t1825
t1825_IN_BLOCK_CODE = ['search_cd', 'gubun']
t1825_IN_BLOCK_NAME = ['검색코드', '구분(0:전체1:코스피2:코스닥)']
t1825_OUT_BLOCK_CODE = ['JongCnt']
t1825_OUT_BLOCK_NAME = ['검색종목수']
t1825_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'sign', 'signcnt', 'close', 'change', 'diff', 'volume', 'volumerate']
t1825_OUT_BLOCK_1_NAME = [
           '종목코드', '종목명', '전일대비구분', '연속봉수', '현재가', '전일대비', '등락율', '거래량', '거래량전일대비율']

# t1826
t1826_IN_BLOCK_CODE = ['search_gb']
t1826_IN_BLOCK_NAME = ['검색구분(0:핵심검색1:지표검색2:시세동향3:투자자동향)']
t1826_OUT_BLOCK_CODE = ['search_cd', 'search_nm']
t1826_OUT_BLOCK_NAME = ['검색코드', '검색명']

# t1857
t1857_IN_BLOCK_CODE = ['sRealFlag', 'query_index']
t1857_IN_BLOCK_NAME = ['실시간구분(0:조회1:실시간)', '종목검색입력값']
t1857_OUT_BLOCK_CODE = ['result_count', 'result_time', 'AlertNum']
t1857_OUT_BLOCK_NAME = ['검색종목수', '포착시간', '실시간키']
t1857_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'JobFlag']
t1857_OUT_BLOCK_1_NAME = [
           '종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '종목상태(N:진입R:재진입O:이탈)']

# t1866
t1866_IN_BLOCK_CODE = ['user_id', 'gb', 'group_name', 'cont', 'contkey']
t1866_IN_BLOCK_NAME = ['로그인ID', '조회구분', '그룹명', '연속여부', '연속키']
t1866_OUT_BLOCK_CODE = ['result_count', 'cont', 'contkey']
t1866_OUT_BLOCK_NAME = ['저장조건수', '연속여부', '연속키']
t1866_OUT_BLOCK_1_CODE = ['query_index', 'group_name', 'query_name']
t1866_OUT_BLOCK_1_NAME = ['서버저장인덱스', '그룹명', '조건저장명']

# t1901
t1901_IN_BLOCK_CODE = ['shcode']
t1901_IN_BLOCK_NAME = ['단축코드']
t1901_OUT_BLOCK_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'recprice', 'avg', 'uplmtprice', 'dnlmtprice',
           'jnilvolume', 'volumediff', 'open', 'opentime', 'high', 'hightime', 'low', 'lowtime', 'high52w', 'high52wdate',
           'low52w', 'low52wdate', 'exhratio', 'flmtvol', 'per', 'listing', 'jkrate', 'vol', 'shcode', 'value',
           'highyear', 'highyeardate', 'lowyear', 'lowyeardate', 'upname', 'upcode', 'upprice', 'upsign', 'upchange', 'updiff',
           'futname', 'futcode', 'futprice', 'futsign', 'futchange', 'futdiff', 'nav', 'navsign', 'navchange', 'navdiff',
           'cocrate', 'kasis', 'subprice', 'offerno1', 'bidno1', 'dvol1', 'svol1', 'dcha1', 'scha1', 'ddiff1',
           'sdiff1', 'offerno2', 'bidno2', 'dvol2', 'svol2', 'dcha2', 'scha2', 'ddiff2', 'sdiff2', 'offerno3',
           'bidno3', 'dvol3', 'svol3', 'dcha3', 'scha3', 'ddiff3', 'sdiff3', 'offerno4', 'bidno4', 'dvol4',
           'svol4', 'dcha4', 'scha4', 'ddiff4', 'sdiff4', 'offerno5', 'bidno5', 'dvol5', 'svol5', 'dcha5',
           'scha5', 'ddiff5', 'sdiff5', 'fwdvl', 'ftradmdcha', 'ftradmddiff', 'fwsvl', 'ftradmscha', 'ftradmsdiff', 'upname2',
           'upcode2', 'upprice2', 'jnilnav', 'jnilnavsign', 'jnilnavchange', 'jnilnavdiff', 'etftotcap', 'spread', 'leverage', 'taxgubun',
           'opcom_nmk', 'lp_nm1', 'lp_nm2', 'lp_nm3', 'lp_nm4', 'lp_nm5', 'etf_cp', 'etf_kind', 'vi_gubun', 'etn_kind_cd',
           'lastymd', 'payday', 'lastdate', 'issuernmk', 'last_sdate', 'last_edate', 'lp_holdvol', 'listdate', 'etp_gb', 'etn_elback_yn',
           'settletype', 'idx_asset_class1', 'ty_text', 'leverage2']
t1901_OUT_BLOCK_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '기준가', '가중평균', '상한가', '하한가',
           '전일거래량', '거래량차', '시가', '시가시간', '고가', '고가시간', '저가', '저가시간', '52최고가', '52최고가일',
           '52최저가', '52최저가일', '소진율', '외국인보유수량', 'PER', '상장주식수(천)', '증거금율', '회전율', '단축코드', '누적거래대금',
           '연중최고가', '연중최고일자', '연중최저가', '연중최저일자', '업종명', '업종코드', '업종현재가', '업종전일비구분', '업종전일대비', '업종등락율',
           '선물최근월물명', '선물최근월물코드', '선물현재가', '선물전일비구분', '선물전일대비', '선물등락율', 'NAV', 'NAV전일대비구분', 'NAV전일대비', 'NAV등락율',
           '추적오차율', '괴리율', '대용가', '매도증권사코드1', '매수증권사코드1', '총매도수량1', '총매수수량1', '매도증감1', '매수증감1', '매도비율1',
           '매수비율1', '매도증권사코드2', '매수증권사코드2', '총매도수량2', '총매수수량2', '매도증감2', '매수증감2', '매도비율2', '매수비율2', '매도증권사코드3',
           '매수증권사코드3', '총매도수량3', '총매수수량3', '매도증감3', '매수증감3', '매도비율3', '매수비율3', '매도증권사코드4', '매수증권사코드4', '총매도수량4',
           '총매수수량4', '매도증감4', '매수증감4', '매도비율4', '매수비율4', '매도증권사코드5', '매수증권사코드5', '총매도수량5', '총매수수량5', '매도증감5',
           '매수증감5', '매도비율5', '매수비율5', '외국계매도합계수량', '외국계매도직전대비', '외국계매도비율', '외국계매수합계수량', '외국계매수직전대비', '외국계매수비율', '참고지수명',
           '참고지수코드', '참고지수현재가', '전일NAV', '전일NAV전일대비구분', '전일NAV전일대비', '전일NAV등락율', '순자산총액(억원)', '스프레드', '레버리지', '과세구분',
           '운용사', 'LP1', 'LP2', 'LP3', 'LP4', 'LP5', '복제방법', '상품유형(Filler)', 'VI발동해제', 'ETN상품분류',
           'ETN만기일', 'ETN지급일', 'ETN최종거래일', 'ETN발행시장참가자', 'ETN만기상환가격결정시작일', 'ETN만기상환가격결정종료일', 'ETNLP보유수량', '상장일', 'ETP상품구분코드', 'ETN조기상환가능여부',
           '최종결제', '지수자산분류코드(대분류)', 'ETF/ETN투자유의', '추적수익률배수']

# t1902
t1902_IN_BLOCK_CODE = ['shcode', 'time']
t1902_IN_BLOCK_NAME = ['단축코드', '시간']
t1902_OUT_BLOCK_CODE = ['time', 'hname', 'upname']
t1902_OUT_BLOCK_NAME = ['시간', '종목명', '업종지수명']
t1902_OUT_BLOCK_1_CODE = [
           'time', 'price', 'sign', 'change', 'volume', 'navdiff', 'nav', 'navchange', 'crate', 'grate',
           'jisu', 'jichange', 'jirate']
t1902_OUT_BLOCK_1_NAME = [
           '시간', '현재가', '전일대비구분', '전일대비', '누적거래량', 'NAV대비', 'NAV', '전일대비', '추적오차', '괴리',
           '지수', '전일대비', '전일대비율']

# t1903
t1903_IN_BLOCK_CODE = ['shcode', 'date']
t1903_IN_BLOCK_NAME = ['단축코드', '일자']
t1903_OUT_BLOCK_CODE = ['date', 'hname', 'upname']
t1903_OUT_BLOCK_NAME = ['일자', '종목명', '업종지수명']
t1903_OUT_BLOCK_1_CODE = [
           'date', 'price', 'sign', 'change', 'volume', 'navdiff', 'nav', 'navchange', 'crate', 'grate',
           'jisu', 'jichange', 'jirate']
t1903_OUT_BLOCK_1_NAME = [
           '일자', '현재가', '전일대비구분', '전일대비', '누적거래량', 'NAV대비', 'NAV', '전일대비', '추적오차', '괴리',
           '지수', '전일대비', '전일대비율']

# t1904
t1904_IN_BLOCK_CODE = ['shcode', 'date', 'sgb']
t1904_IN_BLOCK_NAME = ['ETF단축코드', 'PDF적용일자', '정렬기준(1:평가금액2:증권수)']
t1904_OUT_BLOCK_CODE = [
           'chk_tday', 'date', 'price', 'sign', 'change', 'diff', 'volume', 'nav', 'navsign', 'navchange',
           'navdiff', 'jnilnav', 'jnilnavsign', 'jnilnavchange', 'jnilnavdiff', 'upname', 'upcode', 'upprice', 'upsign', 'upchange',
           'updiff', 'futname', 'futcode', 'futprice', 'futsign', 'futchange', 'futdiff', 'upname2', 'upcode2', 'upprice2',
           'etftotcap', 'etfnum', 'etfcunum', 'cash', 'opcom_nmk', 'tot_pval', 'tot_sigatval']
t1904_OUT_BLOCK_NAME = [
           '당일구분', 'PDF적용일자', 'ETF현재가', 'ETF전일대비구분', 'ETF전일대비', 'ETF등락율', 'ETF누적거래량', 'NAV', 'NAV전일대비구분', 'NAV전일대비',
           'NAV등락율', '전일NAV', '전일NAV전일대비구분', '전일NAV전일대비', '전일NAV등락율', '업종명', '업종코드', '업종현재가', '업종전일비구분', '업종전일대비',
           '업종등락율', '선물최근월물명', '선물최근월물코드', '선물현재가', '선물전일비구분', '선물전일대비', '선물등락율', '참고지수명', '참고지수코드', '참고지수현재가',
           '순자산총액(단위:억)', '구성종목수', 'CU주식수', '현금', '운용사명', '전종목평가금액합', '전종목구성시가총액합']
t1904_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'value', 'icux', 'parprice',
           'pvalue', 'sigatvalue', 'profitdate', 'weight', 'diff2']
t1904_OUT_BLOCK_1_NAME = [
           '단축코드', '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '거래대금(백만)', '단위증권수(계약수/원화현금/USD현금/창고증권)', '액면금액/설정현금액',
           '평가금액', '구성시가총액', 'PDF적용일자', '비중(평가금액)', 'ETF종목과등락차']

# t1906
t1906_IN_BLOCK_CODE = ['shcode']
t1906_IN_BLOCK_NAME = ['단축코드']
t1906_OUT_BLOCK_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'lp_offerrem1', 'lp_bidrem1', 'lp_offerrem2', 'lp_bidrem2',
           'lp_offerrem3', 'lp_bidrem3', 'lp_offerrem4', 'lp_bidrem4', 'lp_offerrem5', 'lp_bidrem5', 'lp_offerrem6', 'lp_bidrem6', 'lp_offerrem7', 'lp_bidrem7',
           'lp_offerrem8', 'lp_bidrem8', 'lp_offerrem9', 'lp_bidrem9', 'lp_offerrem10', 'lp_bidrem10', 'jnilclose', 'offerho1', 'bidho1', 'offerrem1',
           'bidrem1', 'preoffercha1', 'prebidcha1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'preoffercha2', 'prebidcha2', 'offerho3',
           'bidho3', 'offerrem3', 'bidrem3', 'preoffercha3', 'prebidcha3', 'offerho4', 'bidho4', 'offerrem4', 'bidrem4', 'preoffercha4',
           'prebidcha4', 'offerho5', 'bidho5', 'offerrem5', 'bidrem5', 'preoffercha5', 'prebidcha5', 'offerho6', 'bidho6', 'offerrem6',
           'bidrem6', 'preoffercha6', 'prebidcha6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'preoffercha7', 'prebidcha7', 'offerho8',
           'bidho8', 'offerrem8', 'bidrem8', 'preoffercha8', 'prebidcha8', 'offerho9', 'bidho9', 'offerrem9', 'bidrem9', 'preoffercha9',
           'prebidcha9', 'offerho10', 'bidho10', 'offerrem10', 'bidrem10', 'preoffercha10', 'prebidcha10', 'offer', 'bid', 'preoffercha',
           'prebidcha', 'hotime', 'yeprice', 'yevolume', 'yesign', 'yechange', 'yediff', 'tmoffer', 'tmbid', 'ho_status',
           'shcode', 'uplmtprice', 'dnlmtprice', 'open', 'high', 'low', 'midprice', 'offermidsumrem', 'bidmidsumrem']
t1906_OUT_BLOCK_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', 'LP매도호가수량1', 'LP매수호가수량1', 'LP매도호가수량2', 'LP매수호가수량2',
           'LP매도호가수량3', 'LP매수호가수량3', 'LP매도호가수량4', 'LP매수호가수량4', 'LP매도호가수량5', 'LP매수호가수량5', 'LP매도호가수량6', 'LP매수호가수량6', 'LP매도호가수량7', 'LP매수호가수량7',
           'LP매도호가수량8', 'LP매수호가수량8', 'LP매도호가수량9', 'LP매수호가수량9', 'LP매도호가수량10', 'LP매수호가수량10', '전일종가', '매도호가1', '매수호가1', '매도호가수량1',
           '매수호가수량1', '직전매도대비수량1', '직전매수대비수량1', '매도호가2', '매수호가2', '매도호가수량2', '매수호가수량2', '직전매도대비수량2', '직전매수대비수량2', '매도호가3',
           '매수호가3', '매도호가수량3', '매수호가수량3', '직전매도대비수량3', '직전매수대비수량3', '매도호가4', '매수호가4', '매도호가수량4', '매수호가수량4', '직전매도대비수량4',
           '직전매수대비수량4', '매도호가5', '매수호가5', '매도호가수량5', '매수호가수량5', '직전매도대비수량5', '직전매수대비수량5', '매도호가6', '매수호가6', '매도호가수량6',
           '매수호가수량6', '직전매도대비수량6', '직전매수대비수량6', '매도호가7', '매수호가7', '매도호가수량7', '매수호가수량7', '직전매도대비수량7', '직전매수대비수량7', '매도호가8',
           '매수호가8', '매도호가수량8', '매수호가수량8', '직전매도대비수량8', '직전매수대비수량8', '매도호가9', '매수호가9', '매도호가수량9', '매수호가수량9', '직전매도대비수량9',
           '직전매수대비수량9', '매도호가10', '매수호가10', '매도호가수량10', '매수호가수량10', '직전매도대비수량10', '직전매수대비수량10', '매도호가수량합', '매수호가수량합', '직전매도대비수량합',
           '직전매수대비수량합', '수신시간', '예상체결가격', '예상체결수량', '예상체결전일구분', '예상체결전일대비', '예상체결등락율', '시간외매도잔량', '시간외매수잔량', '동시구분',
           '단축코드', '상한가', '하한가', '시가', '고가', '저가', '중간가격', '매도중간가잔량합계수량', '매수중간가잔량합계수량']

# t1921
t1921_IN_BLOCK_CODE = ['shcode', 'gubun', 'date', 'idx']
t1921_IN_BLOCK_NAME = ['종목코드', '융자대주구분', '날짜', 'IDX']
t1921_OUT_BLOCK_CODE = ['cnt', 'date', 'idx']
t1921_OUT_BLOCK_NAME = ['CNT', '날짜', 'IDX']
t1921_OUT_BLOCK_1_CODE = [
           'mmdate', 'close', 'sign', 'jchange', 'diff', 'nvolume', 'svolume', 'jvolume', 'price', 'change',
           'gyrate', 'jkrate', 'shcode']
t1921_OUT_BLOCK_1_NAME = [
           '날짜', '종가', '전일대비구분', '전일대비', '등락율', '신규', '상환', '잔고', '금액', '대비',
           '공여율', '잔고율', '종목코드']

# t1926
t1926_IN_BLOCK_CODE = ['shcode']
t1926_IN_BLOCK_NAME = ['종목코드']
t1926_OUT_BLOCK_CODE = [
           'ynvolume', 'ysvolume', 'yjvolume', 'yvchange', 'ygrate', 'yjrate', 'ynprice', 'ysprice', 'yjprice', 'yachange',
           'dnvolume', 'dsvolume', 'djvolume', 'dvchange', 'dgrate', 'djrate', 'dnprice', 'dsprice', 'djprice', 'dachange',
           'mmdate', 'close', 'volume', 'value', 'pr5days', 'pr20days', 'yj5days', 'yj20days', 'dj5days', 'dj20days']
t1926_OUT_BLOCK_NAME = [
           '융자신규수량', '융자상환수량', '융자잔고수량', '융자수량대비', '융자공여율', '융자잔고율', '융자신규금액', '융자상환금액', '융자잔고금액', '융자금액대비',
           '대주신규수량', '대주상환수량', '대주잔고수량', '대주수량대비', '대주공여율', '대주잔고율', '대주신규금액', '대주상환금액', '대주잔고금액', '대주금액대비',
           '결제일', '결제일종가', '결제일거래량', '결제일거래대금', '주가5일증가율', '주가20일증가율', '융자5일증가율', '융자20일증가율', '대주5일증가율', '대주20일증가율']

# t1927
t1927_IN_BLOCK_CODE = ['shcode', 'date', 'sdate', 'edate']
t1927_IN_BLOCK_NAME = ['종목코드', '일자', '시작일자', '종료일자']
t1927_OUT_BLOCK_CODE = ['date']
t1927_OUT_BLOCK_NAME = ['일자CTS']
t1927_OUT_BLOCK_1_CODE = [
           'date', 'price', 'sign', 'change', 'diff', 'volume', 'value', 'gm_vo', 'gm_va', 'gm_per',
           'gm_avg', 'gm_vo_sum', 'gm_vo1', 'gm_va1', 'gm_vo2', 'gm_va2']
t1927_OUT_BLOCK_1_NAME = [
           '일자', '현재가', '전일대비구분', '전일대비', '등락율', '거래량', '거래대금', '공매도수량', '공매도대금', '공매도거래비중',
           '평균공매도단가', '누적공매도수량', '업틱룰적용공매도수량', '업틱룰적용공매도대금', '업틱룰예외공매도수량', '업틱룰예외공매도대금']

# t1941
t1941_IN_BLOCK_CODE = ['shcode', 'sdate', 'edate']
t1941_IN_BLOCK_NAME = ['종목코드', '시작일자', '종료일자']
t1941_OUT_BLOCK_1_CODE = [
           'date', 'price', 'sign', 'change', 'diff', 'volume', 'upvolume', 'dnvolume', 'tovolume', 'tovalue',
           'shcode', 'tovoldif']
t1941_OUT_BLOCK_1_NAME = [
           '일자', '종가', '대비구분', '대비', '등락율', '거래량', '당일체결', '당일상환', '당일잔고', '잔고금액',
           '종목코드', '대차증감']

# t3102
t3102_IN_BLOCK_CODE = ['sNewsno']
t3102_IN_BLOCK_NAME = ['뉴스번호']
t3102_OUT_BLOCK_CODE = ['sJongcode']
t3102_OUT_BLOCK_NAME = ['뉴스종목']
t3102_OUT_BLOCK_1_CODE = ['sBody']
t3102_OUT_BLOCK_1_NAME = ['뉴스본문']
t3102_OUT_BLOCK_2_CODE = ['sTitle']
t3102_OUT_BLOCK_2_NAME = ['뉴스타이틀']

# t3202
t3202_IN_BLOCK_CODE = ['shcode', 'date']
t3202_IN_BLOCK_NAME = ['종목코드', '조회일자']
t3202_OUT_BLOCK_CODE = [
           'recdt', 'tableid', 'upgu', 'custno', 'custnm', 'shcode', 'upunm']
t3202_OUT_BLOCK_NAME = [
           '기준일', '테이블아이디', '업무구분', '발행체번호', '발행회사명', '종목코드', '업무명']

# t3320
t3320_IN_BLOCK_CODE = ['gicode']
t3320_IN_BLOCK_NAME = ['종목코드']
t3320_OUT_BLOCK_CODE = [
           'upgubunnm', 'sijangcd', 'marketnm', 'company', 'baddress', 'btelno', 'gsyyyy', 'gsmm', 'gsym', 'lstprice',
           'gstock', 'homeurl', 'grdnm', 'foreignratio', 'irtel', 'capital', 'sigavalue', 'cashsis', 'cashrate', 'price',
           'jnilclose', 'notice1', 'notice2', 'notice3']
t3320_OUT_BLOCK_NAME = [
           '업종구분명', '시장구분', '시장구분명', '한글기업명', '본사주소', '본사전화번호', '최근결산년도', '결산월', '최근결산년월', '주당액면가',
           '주식수', 'Homepage', '그룹명', '외국인', '주담전화', '자본금', '시가총액', '배당금', '배당수익율', '현재가',
           '전일종가', '위험고지구분1_정리매매', '위험고지구분2_투자위험', '위험고지구분3_단기과열']
t3320_OUT_BLOCK_1_CODE = [
           'gicode', 'gsym', 'gsgb', 'per', 'eps', 'pbr', 'roa', 'roe', 'ebitda', 'evebitda',
           'par', 'sps', 'cps', 'bps', 't_per', 't_eps', 'peg', 't_peg', 't_gsym']
t3320_OUT_BLOCK_1_NAME = [
           '기업코드', '결산년월', '결산구분', 'PER', 'EPS', 'PBR', 'ROA', 'ROE', 'EBITDA', 'EVEBITDA',
           '액면가', 'SPS', 'CPS', 'BPS', 'T.PER', 'T.EPS', 'PEG', 'T.PEG', '최근분기년도']

# t3341
t3341_IN_BLOCK_CODE = ['gubun', 'gubun1', 'gubun2', 'idx']
t3341_IN_BLOCK_NAME = ['시장구분', '순위구분(1:매출액증가율2:영업이익증가율3:세전계속이익증가율4:부채비율5:유보율6:EPS7:BPS8:ROE9:PERa:PBRb:PEG)', '대비구분', 'IDX']
t3341_OUT_BLOCK_CODE = ['cnt', 'idx']
t3341_OUT_BLOCK_NAME = ['CNT', 'IDX']
t3341_OUT_BLOCK_1_CODE = [
           'rank', 'hname', 'salesgrowth', 'operatingincomegrowt', 'ordinaryincomegrowth', 'liabilitytoequity', 'enterpriseratio', 'eps', 'bps', 'roe',
           'shcode', 'per', 'pbr', 'peg']
t3341_OUT_BLOCK_1_NAME = [
           '순위', '기업명', '매출액증가율', '영업이익증가율', '경상이익증가율', '부채비율', '유보율', 'EPS', 'BPS', 'ROE',
           '종목코드', 'PER', 'PBR', 'PEG']

# t3401
t3401_IN_BLOCK_CODE = ['shcode', 'gubun1', 'tradno', 'cts_date']
t3401_IN_BLOCK_NAME = ['종목코드', '구분', '회원사코드', 'IDXDATE']
t3401_OUT_BLOCK_CODE = [
           'cts_date', 'price', 'sign', 'change', 'diff', 'volume', 'value']
t3401_OUT_BLOCK_NAME = [
           'IDXDATE', '현재가', '대비속성', '대비', '등락율', '거래량', '거래대금']
t3401_OUT_BLOCK_1_CODE = [
           'shcode', 'tradno', 'date', 'tradname', 'bopn', 'nopn', 'boga', 'noga', 'close']
t3401_OUT_BLOCK_1_NAME = [
           '종목코드', '회원사코드', '의견일자', '회원사명', '투자의견변경후', '투자의견변경전', '목표가변경전', '목표가변경후', '의견일종가']

# t3518
t3518_IN_BLOCK_CODE = [
           'kind', 'symbol', 'cnt', 'jgbn', 'nmin', 'cts_date', 'cts_time']
t3518_IN_BLOCK_NAME = [
           '종목종류', 'SYMBOL', '입력건수', '조회구분', 'N분', 'CTS_DATE', 'CTS_TIME']
t3518_OUT_BLOCK_CODE = ['cts_date', 'cts_time']
t3518_OUT_BLOCK_NAME = ['CTS_DATE', 'CTS_TIME']
t3518_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'price', 'sign', 'change', 'uprate', 'volume',
           'bidho', 'offerho', 'bidrem', 'offerrem', 'kind', 'symbol', 'exid', 'kodate', 'kotime']
t3518_OUT_BLOCK_1_NAME = [
           '일자', '시간', '시가', '고가', '저가', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량',
           '매수호가', '매도호가', '매수잔량', '매도잔량', '종목종류', 'SYMBOL', 'EXID', '한국일자', '한국시간']

# t3521
t3521_IN_BLOCK_CODE = ['kind', 'symbol']
t3521_IN_BLOCK_NAME = ['종목종류', 'SYMBOL']
t3521_OUT_BLOCK_CODE = [
           'symbol', 'hname', 'close', 'sign', 'change', 'diff', 'date']
t3521_OUT_BLOCK_NAME = [
           '심벌', '지수명', '지수', '대비구분', '대비', '등락율', '일자']

# t4203
t4203_IN_BLOCK_CODE = [
           'shcode', 'gubun', 'ncnt', 'qrycnt', 'tdgb', 'sdate', 'edate', 'cts_date', 'cts_time', 'cts_daygb']
t4203_IN_BLOCK_NAME = [
           '단축코드', '주기구분(0:틱1:분2:일3:주4:월)', '틱개수', '건수', '당일구분(0:전체1:당일만)', '시작일자', '종료일자', '연속일자', '연속시간', '연속당일구분(0:연속전체1:연속당일만2:연속전일만)']
t4203_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'disvalue', 'cts_date', 'cts_time', 'cts_daygb']
t4203_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '당일거래대금', '연속일자', '연속시간', '연속당일구분']
t4203_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value']
t4203_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '거래대금']

# t8407
t8407_IN_BLOCK_CODE = ['nrec', 'shcode']
t8407_IN_BLOCK_NAME = ['건수', '종목코드']
t8407_OUT_BLOCK_1_CODE = [
           'shcode', 'hname', 'price', 'sign', 'change', 'diff', 'volume', 'offerho', 'bidho', 'cvolume',
           'chdegree', 'open', 'high', 'low', 'value', 'offerrem', 'bidrem', 'totofferrem', 'totbidrem', 'jnilclose',
           'uplmtprice', 'dnlmtprice']
t8407_OUT_BLOCK_1_NAME = [
           '종목코드', '종목명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '매도호가', '매수호가', '체결수량',
           '체결강도', '시가', '고가', '저가', '거래대금(백만)', '우선매도잔량', '우선매수잔량', '총매도잔량', '총매수잔량', '전일종가',
           '상한가', '하한가']

# t8410
t8410_IN_BLOCK_CODE = [
           'shcode', 'gubun', 'qrycnt', 'sdate', 'edate', 'cts_date', 'comp_yn', 'sujung']
t8410_IN_BLOCK_NAME = [
           '단축코드', '주기구분(2:일3:주4:월5:년)', '요청건수(최대-압축:2000비압축:500)', '시작일자', '종료일자', '연속일자', '압축여부(Y:압축N:비압축)', '수정주가여부(Y:적용N:비적용)']
t8410_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'highend', 'lowend', 'cts_date', 's_time', 'e_time', 'dshmin', 'rec_count', 'svi_uplmtprice', 'svi_dnlmtprice']
t8410_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '상한가', '하한가', '연속일자', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트', '정적VI상한가', '정적VI하한가']
t8410_OUT_BLOCK_1_CODE = [
           'date', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value', 'jongchk', 'rate', 'pricechk',
           'ratevalue', 'sign']
t8410_OUT_BLOCK_1_NAME = [
           '날짜', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율', '수정주가반영항목',
           '수정비율반영거래대금', '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)']

# t8411
t8411_IN_BLOCK_CODE = [
           'shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time',
           'comp_yn']
t8411_IN_BLOCK_NAME = [
           '단축코드', '단위(n틱)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간',
           '압축여부(Y:압축N:비압축)']
t8411_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'highend', 'lowend', 'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count']
t8411_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '상한가', '하한가', '연속일자', '연속시간', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트']
t8411_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'jongchk', 'rate', 'pricechk']
t8411_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '수정구분', '수정비율', '수정주가반영항목']

# t8412
t8412_IN_BLOCK_CODE = [
           'shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time',
           'comp_yn']
t8412_IN_BLOCK_NAME = [
           '단축코드', '단위(n분)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간',
           '압축여부(Y:압축N:비압축)']
t8412_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'highend', 'lowend', 'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count']
t8412_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '상한가', '하한가', '연속일자', '연속시간', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트']
t8412_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value', 'jongchk', 'rate',
           'sign']
t8412_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율',
           '종가등락구분(1:상한2:상승3:보합4:하한5:하락)']

# t8417
t8417_IN_BLOCK_CODE = [
           'shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time',
           'comp_yn']
t8417_IN_BLOCK_NAME = [
           '단축코드', '단위(n틱)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간',
           '압축여부(Y:압축N:비압축)']
t8417_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count']
t8417_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '연속일자', '연속시간', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트']
t8417_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol']
t8417_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '시가', '고가', '저가', '종가', '거래량']

# t8418
t8418_IN_BLOCK_CODE = [
           'shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time',
           'comp_yn']
t8418_IN_BLOCK_NAME = [
           '단축코드', '단위(n분)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간',
           '압축여부(Y:압축N:비압축)']
t8418_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'disvalue', 'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count']
t8418_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '당일거래대금', '연속일자', '연속시간', '업종시작시간(HHMMSS)', '업종종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트']
t8418_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value']
t8418_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '거래대금']

# t8419
t8419_IN_BLOCK_CODE = [
           'shcode', 'gubun', 'qrycnt', 'sdate', 'edate', 'cts_date', 'comp_yn']
t8419_IN_BLOCK_NAME = [
           '단축코드', '주기구분(2:일3:주4:월)', '요청건수(최대-압축:2000비압축:500)', '시작일자', '종료일자', '연속일자', '압축여부(Y:압축N:비압축)']
t8419_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'disvalue', 'cts_date', 's_time', 'e_time', 'dshmin', 'rec_count']
t8419_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '당일거래대금', '연속일자', '업종시작시간', '업종종료시간', '동시호가처리시간(MM:분)', '레코드카운트']
t8419_OUT_BLOCK_1_CODE = [
           'date', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value']
t8419_OUT_BLOCK_1_NAME = [
           '날짜', '시가', '고가', '저가', '종가', '거래량', '거래대금']

# t8424
t8424_IN_BLOCK_CODE = ['gubun1']
t8424_IN_BLOCK_NAME = ['구분1']
t8424_OUT_BLOCK_CODE = ['hname', 'upcode']
t8424_OUT_BLOCK_NAME = ['업종명', '업종코드']

# t8425
t8425_IN_BLOCK_CODE = ['dummy']
t8425_IN_BLOCK_NAME = ['Dummy']
t8425_OUT_BLOCK_CODE = ['tmname', 'tmcode']
t8425_OUT_BLOCK_NAME = ['테마명', '테마코드']

# t8428
t8428_IN_BLOCK_CODE = [
           'fdate', 'tdate', 'gubun', 'key_date', 'upcode', 'cnt']
t8428_IN_BLOCK_NAME = [
           'from일자', 'to일자', '구분', '날짜', '업종코드', '조회건수']
t8428_OUT_BLOCK_CODE = ['date', 'idx']
t8428_OUT_BLOCK_NAME = ['날짜CTS', 'IDX']
t8428_OUT_BLOCK_1_CODE = [
           'date', 'jisu', 'sign', 'change', 'diff', 'volume', 'custmoney', 'yecha', 'vol', 'outmoney',
           'trjango', 'futymoney', 'stkmoney', 'mstkmoney', 'mbndmoney', 'bndmoney', 'bndsmoney', 'mmfmoney']
t8428_OUT_BLOCK_1_NAME = [
           '일자', '지수', '대비구분', '대비', '등락율', '거래량', '고객예탁금_억원', '예탁증감_억원', '회전율', '미수금_억원',
           '신용잔고_억원', '선물예수금_억원', '주식형_억원', '혼합형_억원(주식)', '혼합형_억원(채권)', '채권형_억원', '필러(구.단기채권)', 'MMF_억원(주식)']

# t8430
t8430_IN_BLOCK_CODE = ['gubun']
t8430_IN_BLOCK_NAME = ['구분(0:전체1:코스피2:코스닥)']
t8430_OUT_BLOCK_CODE = [
           'hname', 'shcode', 'expcode', 'etfgubun', 'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun']
t8430_OUT_BLOCK_NAME = [
           '종목명', '단축코드', '확장코드', 'ETF구분(1:ETF)', '상한가', '하한가', '전일가', '주문수량단위', '기준가', '구분(1:코스피2:코스닥)']

# t8436
t8436_IN_BLOCK_CODE = ['gubun']
t8436_IN_BLOCK_NAME = ['구분(0:전체1:코스피2:코스닥)']
t8436_OUT_BLOCK_CODE = [
           'hname', 'shcode', 'expcode', 'etfgubun', 'uplmtprice', 'dnlmtprice', 'jnilclose', 'memedan', 'recprice', 'gubun',
           'bu12gubun', 'spac_gubun', 'filler']
t8436_OUT_BLOCK_NAME = [
           '종목명', '단축코드', '확장코드', 'ETF구분(1:ETF2:ETN)', '상한가', '하한가', '전일가', '주문수량단위', '기준가', '구분(1:코스피2:코스닥)',
           '증권그룹', '기업인수목적회사여부(Y/N)', 'filler(미사용)']

# t8450
t8450_IN_BLOCK_CODE = ['shcode', 'exchgubun']
t8450_IN_BLOCK_NAME = ['단축코드', '거래소구분코드']
t8450_OUT_BLOCK_CODE = [
           'hname', 'price', 'sign', 'change', 'diff', 'volume', 'jnilclose', 'offerho1', 'bidho1', 'offerrem1',
           'bidrem1', 'offerho2', 'bidho2', 'offerrem2', 'bidrem2', 'offerho3', 'bidho3', 'offerrem3', 'bidrem3', 'offerho4',
           'bidho4', 'offerrem4', 'bidrem4', 'offerho5', 'bidho5', 'offerrem5', 'bidrem5', 'offerho6', 'bidho6', 'offerrem6',
           'bidrem6', 'offerho7', 'bidho7', 'offerrem7', 'bidrem7', 'offerho8', 'bidho8', 'offerrem8', 'bidrem8', 'offerho9',
           'bidho9', 'offerrem9', 'bidrem9', 'offerho10', 'bidho10', 'offerrem10', 'bidrem10', 'offer', 'bid', 'hotime',
           'yeprice', 'yevolume', 'yesign', 'yechange', 'yediff', 'tmoffer', 'tmbid', 'ho_status', 'shcode', 'uplmtprice',
           'dnlmtprice', 'open', 'high', 'low', 'nxt_offerrem1', 'nxt_bidrem1', 'nxt_offerrem2', 'nxt_bidrem2', 'nxt_offerrem3', 'nxt_bidrem3',
           'nxt_offerrem4', 'nxt_bidrem4', 'nxt_offerrem5', 'nxt_bidrem5', 'nxt_offerrem6', 'nxt_bidrem6', 'nxt_offerrem7', 'nxt_bidrem7', 'nxt_offerrem8', 'nxt_bidrem8',
           'nxt_offerrem9', 'nxt_bidrem9', 'nxt_offerrem10', 'nxt_bidrem10', 'nxt_offer', 'nxt_bid', 'nxt_yeprice', 'nxt_yevolume', 'nxt_yesign', 'nxt_yechange',
           'nxt_yediff', 'nxt_ho_status', 'unx_offerrem1', 'unx_bidrem1', 'unx_offerrem2', 'unx_bidrem2', 'unx_offerrem3', 'unx_bidrem3', 'unx_offerrem4', 'unx_bidrem4',
           'unx_offerrem5', 'unx_bidrem5', 'unx_offerrem6', 'unx_bidrem6', 'unx_offerrem7', 'unx_bidrem7', 'unx_offerrem8', 'unx_bidrem8', 'unx_offerrem9', 'unx_bidrem9',
           'unx_offerrem10', 'unx_bidrem10', 'unx_offer', 'unx_bid', 'krx_midprice', 'krx_offermidsumrem', 'krx_bidmidsumrem', 'nxt_midprice', 'nxt_offermidsumrem', 'nxt_bidmidsumrem',
           'ex_shcode', 'krx_midsumrem', 'krx_midsumremgubun', 'nxt_midsumrem', 'nxt_midsumremgubun']
t8450_OUT_BLOCK_NAME = [
           '한글명', '현재가', '전일대비구분', '전일대비', '등락율', '누적거래량', '전일종가(기준가)', '매도호가1', '매수호가1', '매도호가수량1',
           '매수호가수량1', '매도호가2', '매수호가2', '매도호가수량2', '매수호가수량2', '매도호가3', '매수호가3', '매도호가수량3', '매수호가수량3', '매도호가4',
           '매수호가4', '매도호가수량4', '매수호가수량4', '매도호가5', '매수호가5', '매도호가수량5', '매수호가수량5', '매도호가6', '매수호가6', '매도호가수량6',
           '매수호가수량6', '매도호가7', '매수호가7', '매도호가수량7', '매수호가수량7', '매도호가8', '매수호가8', '매도호가수량8', '매수호가수량8', '매도호가9',
           '매수호가9', '매도호가수량9', '매수호가수량9', '매도호가10', '매수호가10', '매도호가수량10', '매수호가수량10', '매도호가수량합', '매수호가수량합', '수신시간',
           '예상체결가격', '예상체결수량', '예상체결전일구분', '예상체결전일대비', '예상체결등락율', '시간외매도잔량', '시간외매수잔량', '동시구분', '단축코드', '상한가',
           '하한가', '시가', '고가', '저가', 'NXT매도호가수량1', 'NXT매수호가수량1', 'NXT매도호가수량2', 'NXT매수호가수량2', 'NXT매도호가수량3', 'NXT매수호가수량3',
           'NXT매도호가수량4', 'NXT매수호가수량4', 'NXT매도호가수량5', 'NXT매수호가수량5', 'NXT매도호가수량6', 'NXT매수호가수량6', 'NXT매도호가수량7', 'NXT매수호가수량7', 'NXT매도호가수량8', 'NXT매수호가수량8',
           'NXT매도호가수량9', 'NXT매수호가수량9', 'NXT매도호가수량10', 'NXT매수호가수량10', 'NXT매도호가수량합', 'NXT매수호가수량합', 'NXT예상체결가격', 'NXT예상체결수량', 'NXT예상체결전일구분', 'NXT예상체결전일대비',
           'NXT예상체결등락율', 'NXT동시구분', '통합매도호가수량1', '통합매수호가수량1', '통합매도호가수량2', '통합매수호가수량2', '통합매도호가수량3', '통합매수호가수량3', '통합매도호가수량4', '통합매수호가수량4',
           '통합매도호가수량5', '통합매수호가수량5', '통합매도호가수량6', '통합매수호가수량6', '통합매도호가수량7', '통합매수호가수량7', '통합매도호가수량8', '통합매수호가수량8', '통합매도호가수량9', '통합매수호가수량9',
           '통합매도호가수량10', '통합매수호가수량10', '통합매도호가수량합', '통합매수호가수량합', 'KRX중간가격', 'KRX매도중간가잔량합계수량', 'KRX매수중간가잔량합계수량', 'NXT중간가격', 'NXT매도중간가잔량합계수량', 'NXT매수중간가잔량합계수량',
           '거래소별단축코드', 'KRX중간가잔량합계수량', "KRX중간가잔량구분('없음'1'매도'2'매수)", 'NXT중간가잔량합계수량', "NXT중간가잔량구분('없음'1'매도'2'매수)"]

# t8451
t8451_IN_BLOCK_CODE = [
           'shcode', 'gubun', 'qrycnt', 'sdate', 'edate', 'cts_date', 'comp_yn', 'sujung', 'exchgubun']
t8451_IN_BLOCK_NAME = [
           '단축코드', '주기구분(2:일3:주4:월5:년)', '요청건수(최대-압축:2000비압축:500)', '시작일자', '종료일자', '연속일자', '압축여부(Y:압축N:비압축)', '수정주가여부(Y:적용N:비적용)', '거래소구분코드']
t8451_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'highend', 'lowend', 'cts_date', 's_time', 'e_time', 'dshmin', 'rec_count', 'svi_uplmtprice', 'svi_dnlmtprice', 'nxt_fm_s_time',
           'nxt_fm_e_time', 'nxt_fm_dshmin', 'nxt_am_s_time', 'nxt_am_e_time', 'nxt_am_dshmin']
t8451_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '상한가', '하한가', '연속일자', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트', '정적VI상한가', '정적VI하한가', 'NXT프리마켓장시작시간(HHMMSS)',
           'NXT프리마켓장종료시간(HHMMSS)', 'NXT프리마켓동시호가처리시간(MM:분)', 'NXT에프터마켓장시작시간(HHMMSS)', 'NXT에프터마켓장종료시간(HHMMSS)', 'NXT에프터마켓동시호가처리시간(MM:분)']
t8451_OUT_BLOCK_1_CODE = [
           'date', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value', 'jongchk', 'rate', 'pricechk',
           'ratevalue', 'sign']
t8451_OUT_BLOCK_1_NAME = [
           '날짜', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율', '수정주가반영항목',
           '수정비율반영거래대금', '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)']

# t8452
t8452_IN_BLOCK_CODE = [
           'shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time',
           'comp_yn', 'exchgubun']
t8452_IN_BLOCK_NAME = [
           '단축코드', '단위(n분)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간',
           '압축여부(Y:압축N:비압축)', '거래소구분코드']
t8452_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'highend', 'lowend', 'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count', 'nxt_fm_s_time', 'nxt_fm_e_time',
           'nxt_fm_dshmin', 'nxt_am_s_time', 'nxt_am_e_time', 'nxt_am_dshmin']
t8452_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '상한가', '하한가', '연속일자', '연속시간', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트', 'NXT프리마켓장시작시간(HHMMSS)', 'NXT프리마켓장종료시간(HHMMSS)',
           'NXT프리마켓동시호가처리시간(MM:분)', 'NXT에프터마켓장시작시간(HHMMSS)', 'NXT에프터마켓장종료시간(HHMMSS)', 'NXT에프터마켓동시호가처리시간(MM:분)']
t8452_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'value', 'jongchk', 'rate',
           'sign']
t8452_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '거래대금', '수정구분', '수정비율',
           '종가등락구분(1:상한2:상승3:보합4:하한5:하락)']

# t8453
t8453_IN_BLOCK_CODE = [
           'shcode', 'ncnt', 'qrycnt', 'nday', 'sdate', 'stime', 'edate', 'etime', 'cts_date', 'cts_time',
           'comp_yn', 'exchgubun']
t8453_IN_BLOCK_NAME = [
           '단축코드', '단위(n틱)', '요청건수(최대-압축:2000비압축:500)', '조회영업일수(0:미사용1>=사용)', '시작일자', '시작시간(현재미사용)', '종료일자', '종료시간(현재미사용)', '연속일자', '연속시간',
           '압축여부(Y:압축N:비압축)', '거래소구분코드']
t8453_OUT_BLOCK_CODE = [
           'shcode', 'jisiga', 'jihigh', 'jilow', 'jiclose', 'jivolume', 'disiga', 'dihigh', 'dilow', 'diclose',
           'highend', 'lowend', 'cts_date', 'cts_time', 's_time', 'e_time', 'dshmin', 'rec_count', 'nxt_fm_s_time', 'nxt_fm_e_time',
           'nxt_fm_dshmin', 'nxt_am_s_time', 'nxt_am_e_time', 'nxt_am_dshmin']
t8453_OUT_BLOCK_NAME = [
           '단축코드', '전일시가', '전일고가', '전일저가', '전일종가', '전일거래량', '당일시가', '당일고가', '당일저가', '당일종가',
           '상한가', '하한가', '연속일자', '연속시간', '장시작시간(HHMMSS)', '장종료시간(HHMMSS)', '동시호가처리시간(MM:분)', '레코드카운트', 'NXT프리마켓장시작시간(HHMMSS)', 'NXT프리마켓장종료시간(HHMMSS)',
           'NXT프리마켓동시호가처리시간(MM:분)', 'NXT에프터마켓장시작시간(HHMMSS)', 'NXT에프터마켓장종료시간(HHMMSS)', 'NXT에프터마켓동시호가처리시간(MM:분)']
t8453_OUT_BLOCK_1_CODE = [
           'date', 'time', 'open', 'high', 'low', 'close', 'jdiff_vol', 'jongchk', 'rate', 'pricechk']
t8453_OUT_BLOCK_1_NAME = [
           '날짜', '시간', '시가', '고가', '저가', '종가', '거래량', '수정구분', '수정비율', '수정주가반영항목']

# t8454
t8454_IN_BLOCK_CODE = [
           'shcode', 'cvolume', 'starttime', 'endtime', 'cts_time', 'exchgubun']
t8454_IN_BLOCK_NAME = [
           '단축코드', '특이거래량', '시작시간', '종료시간', '시간CTS', '거래소구분코드']
t8454_OUT_BLOCK_CODE = ['cts_time', 'ex_shcode']
t8454_OUT_BLOCK_NAME = ['시간CTS', '거래소별단축코드']
t8454_OUT_BLOCK_1_CODE = [
           'chetime', 'price', 'sign', 'change', 'diff', 'cvolume', 'chdegree', 'volume', 'mdvolume', 'mdchecnt',
           'msvolume', 'mschecnt', 'revolume', 'rechecnt', 'exchname']
t8454_OUT_BLOCK_1_NAME = [
           '시간', '현재가', '전일대비구분', '전일대비', '등락율', '체결수량', '체결강도', '거래량', '매도체결수량', '매도체결건수',
           '매수체결수량', '매수체결건수', '순체결량', '순체결건수', '거래소명']

# t9945
t9945_IN_BLOCK_CODE = ['gubun']
t9945_IN_BLOCK_NAME = ['구분(KSP:1KSD:2)']
t9945_OUT_BLOCK_CODE = [
           'hname', 'shcode', 'expcode', 'etfchk', 'nxt_chk', 'filler']
t9945_OUT_BLOCK_NAME = [
           '종목명', '단축코드', '확장코드', 'ETF구분', 'NXT상장구분', 'filler']

