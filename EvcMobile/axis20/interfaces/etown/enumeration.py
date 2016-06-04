__author__ = 'karl.gong'


class DataStore:
    US = "US1"
    CN = "CN1"


class CenterCode:
    Bali = "B"
    Bangalore = "BGL"
    Chile = "CHL"
    CHL_FT = "CHL-FT"
    CRCenter = "CR"
    SHL_FT = "FCL-FT"
    SHL_PT = "FCL-PT"
    Freelance = "FWW"
    FWW_FT = "FWW-FT"
    FWW_FX = "FWW-FX"
    FWW_PT = "FWW-PT"
    Photon = "I"
    Johannesburg = "JHB"
    Kazan = "KAZ"
    PCS = "PCS"
    PCT = "PCT"
    PPE = "PPE"
    PWC = "PWC"
    Shanghai = "S"
    Pangea = "SA"
    SHI_FT = "SHA-FT"
    TA = "TA"
    USA = "USA"
    USA_FT = "USA-FT"
    USA_FX = "USA-FX"
    USA_PT = "USA-PT"


class ClassServiceType:
    PL = "PL"
    GL = "GL"


class ClassServiceSubType:
    Global = "Global"
    CP20 = "CP20"
    EFT = "EFTV"


class ClassStatus:
    Assigned = "ASSIGNED"
    Booked = "BOOKED"
    Finished = "FINISHED"
    Subout = "SUBOUT"


class ClassType:
    PL = "PL"
    GL = "GL"
    CP20 = "CP20"
    EFT = "EFTV"


class ClassLevel:
    BEG = "BEG"
    ELE = "ELE"
    INT = "INT"
    UPINT = "UPINT"
    ADV = "ADV"


class MarketCode:
    Global = "Global"
    CN = "cn"
    ROLA = "SPLang"


class PartnerCode:
    Global = "Global"
    CNB2C = "CNB2C"


class LanguageCode:
    English = "en"
    Chinese = "cs"
    Spanish = "es"


class EvcServerCode:
    Adobe_us1 = "us1"
    Adobe_cn1 = "cn1"
    Evc_cn1 = "EvcCN1"


class WritingCorrectionActionType:
    SP = "SP"
    WC = "WC"
    MW = "MW"
    AR = "AR"
    PR = "PR"
    PU = "PU"
    DD = "DD"
    CC = "CC"
    VT = "VT"
    PL = "PL"
    AG = "AG"
    WO = "WO"
    CO = "CO"
    NS = "NS"
    SI = "SI"
    PO = "PO"
    EX = "EX"
    NSW = "NSW"
    AS = "AS"
    RS = "RS"
    UM = "UM"


class WritingGradeScore:
    Exceeds_Expectation = 100
    Distinction_95 = 95
    Meets_Expectation_90 = 90
    Meets_Expectation_80 = 80
    Meets_Expectation_70 = 70
    Needs_Improvement = 60
    Improvement_Essential = 40
    Plagiarised = 0


class WritingEscalateContent:
    Incorrect_Topic = "IncorrectTopic"
    Incomplete_Writing = "BlankWriting"
    Non_English = "NonEnglish"
    Nonsensical = "Nonsensical"


class Month:
    January = 1
    Jan = January
    February = 2
    Feb = February
    March = 3
    Mar = March
    April = 4
    Apr = April
    May = 5
    June = 6
    Jun = June
    July = 7
    Jul = July
    August = 8
    Aug = August
    September = 9
    Sep = September
    October = 10
    Oct = October
    November = 11
    Nov = November
    December = 12
    Dec = December


class Weekday:
    Monday = 0
    Mon = Monday
    Tuesday = 1
    Tue = Tuesday
    Wednesday = 2
    Wed = Wednesday
    Thursday = 3
    Thu = Thursday
    Friday = 4
    Fri = Friday
    Saturday = 5
    Sat = Saturday
    Sunday = 6
    Sun = Sunday


class TimeZone:
    Eastern = "US/Eastern"
    UTC = "UTC"
    China = "Asia/Shanghai"


class TimeSlot:
    S0_00_E0_30 = 0
    S0_30_E1_00 = 1
    S1_00_E1_30 = 2
    S1_30_E2_00 = 3
    S2_00_E2_30 = 4
    S2_30_E3_00 = 5
    S3_00_E3_30 = 6
    S3_30_E4_00 = 7
    S4_00_E4_30 = 8
    S4_30_E5_00 = 9
    S5_00_E5_30 = 10
    S5_30_E6_00 = 11
    S6_00_E6_30 = 12
    S6_30_E7_00 = 13
    S7_00_E7_30 = 14
    S7_30_E8_00 = 15
    S8_00_E8_30 = 16
    S8_30_E9_00 = 17
    S9_00_E9_30 = 18
    S9_30_E10_00 = 19
    S10_00_E10_30 = 20
    S10_30_E11_00 = 21
    S11_00_E11_30 = 22
    S11_30_E12_00 = 23
    S12_00_E12_30 = 24
    S12_30_E13_00 = 25
    S13_00_E13_30 = 26
    S13_30_E14_00 = 27
    S14_00_E14_30 = 28
    S14_30_E15_00 = 29
    S15_00_E15_30 = 30
    S15_30_E16_00 = 31
    S16_00_E16_30 = 32
    S16_30_E17_00 = 33
    S17_00_E17_30 = 34
    S17_30_E18_00 = 35
    S18_00_E18_30 = 36
    S18_30_E19_00 = 37
    S19_00_E19_30 = 38
    S19_30_E20_00 = 39
    S20_00_E20_30 = 40
    S20_30_E21_00 = 41
    S21_00_E21_30 = 42
    S21_30_E22_00 = 43
    S22_00_E22_30 = 44
    S22_30_E23_00 = 45
    S23_00_E23_30 = 46
    S23_30_E00_00 = 47
