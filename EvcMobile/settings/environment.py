class ENVIRONMENT(object):
    UAT = "apollouat"
    QA = "qa"
    STAGING  = "staging"
    WEBUS1 = "webus1"
    LIVE = "www"

class UAT_Account(object):
    EFEC_Account = {'username': 'stest10797', 'password': '1'}
    EFEC_EVC_Account = {'username': 'stest10015', 'password': '1'}
    EFEC_Invalid_Account = {'username': 'wrong_user_password', 'password': '1'}
    EFEC_BEG_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10856', 'password': '1'}
    EFEC_ELE_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10857', 'password': '1'}
    EFEC_ADV_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10858', 'password': '1'}
    EFEC_BEG_IN_EVC_ROLLOUT_Account = {'username': 'stest10861', 'password': '1'}
    EFEC_ELE_IN_EVC_ROLLOUT_Account = {'username': 'stest10862', 'password': '1'}
    EFEC_ADV_IN_EVC_ROLLOUT_Account = {'username': 'stest10863', 'password': '1'}
    EFEC_BEG_IN_WHITE_LIST_Account = {'username': 'stest10864', 'password': '1'}
    EFEC_ELE_IN_WHITE_LIST_Account = {'username': 'stest10866', 'password': '1'}
    EFEC_ADV_IN_WHITE_LIST_Account = {'username': 'stest10867', 'password': '1'}
    EFEC_BEG_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10868', 'password': '1'}
    EFEC_ELE_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10869', 'password': '1'}
    EFEC_ADV_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10872', 'password': '1'}
    B2C_Account = {'username': 'atest5174',  'password': '1'}
    B2B_Account = {'username': 'ck8', 'password': '1'}
    B2B_BEG_Account = {'username': 'ATEAM_B2B_BEG', 'password': '1'}
    B2B_ELE_Account = {'username': 'ATEAM_B2B_ELE', 'password': '1'}
    B2B_ADV_Account = {'username': 'ATEAM_B2B_ADV', 'password': '1'}
    EFTV_Account = {'username':'ck8', 'password':'1'}
    B2B_No_Coupon_Account = {'username': 'cman387', 'password': '1'}
    EFEC_No_Coupon_Account = {'username': 'stest9739', 'password': '1'}
    EFEC_No_Booked_Class_Account = {'username': 'stest9740', 'password': '1'}
    Admin_Account = {'username':'freshmeat', 'password':'vamper'}
    Bilingual_PL40_Teacher = {'displayname':'asd1 t', 'teacherid':'23660384'}
    Bilingual_PL20_Teacher = {'displayname': 'asd2 t', 'teacherid':'23684241'}
    Global_BEG_PL40_Teacher = {'displayname':'asd3 t','teacherid':'23669319'}
    Global_BEG_PL20_Teacher = {'displayname': 'asd4 t', 'teacherid': '23687647'}
    Global_BEG_PL40_CN_Teacher = {'displayname': 'asd5 t', 'teacherid': '23686057'}
    EFTV_TEACHER = {'displayname': 'asd6 t', 'teacherid':'23661336'}
    Bilingual_PL20_Trial_Teacher = {'displayname': 'asd7 t', 'teacherid':'23678029'}
    Global_BEG_PL20_Trial_Teacher = {'displayname': 'asd8 t', 'teacherid': '23645087'}
    Bilingual_EVC_PL20_Teacher = {'displayname': 'asd9 t', 'teacherid':'23643493'}
    Bilingual_GL_Teacher = {'displayname':'Eva Haridas', 'teacherid':'15432365'}
    Global_GL_Teacher = {'displayname':'fifiq bali','teacherid':'23657120'}

class QA_Account(object):
    EFEC_Account = {'username': 'stest651', 'password': '1'}
    EFEC_EVC_Account = {'username': 'stest651', 'password': '1'}
    EFEC_BEG_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10856', 'password': '1'}
    EFEC_ELE_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10857', 'password': '1'}
    EFEC_ADV_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10858', 'password': '1'}
    EFEC_BEG_IN_EVC_ROLLOUT_Account = {'username': 'stest10861', 'password': '1'}
    EFEC_ELE_IN_EVC_ROLLOUT_Account = {'username': 'stest10862', 'password': '1'}
    EFEC_ADV_IN_EVC_ROLLOUT_Account = {'username': 'stest10863', 'password': '1'}
    EFEC_BEG_IN_WHITE_LIST_Account = {'username': 'stest10864', 'password': '1'}
    EFEC_ELE_IN_WHITE_LIST_Account = {'username': 'stest10866', 'password': '1'}
    EFEC_ADV_IN_WHITE_LIST_Account = {'username': 'stest10867', 'password': '1'}
    EFEC_BEG_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10868', 'password': '1'}
    EFEC_ELE_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10869', 'password': '1'}
    EFEC_ADV_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10872', 'password': '1'}
    B2C_Account = {'username': 'atest155', 'password': '1'}
    B2B_Account = {'username': 'AATEAM', 'password': '1'}
    B2B_BEG_Account = {'username': 'AATEAM', 'password': '1'}
    B2B_ELE_Account = {'username': 'BATEAM', 'password': '1'}
    B2B_ADV_Account = {'username': 'CATEAM', 'password': '1'}
    EFTV_Account = {'username':'', 'password':''}
    B2B_No_Coupon_Account = {'username': '', 'password': ''}
    EFEC_No_Coupon_Account = {'username': '', 'password': ''}
    EFEC_No_Booked_Class_Account = {'username': 'stest9740', 'password': '1'}
    Admin_Account = {'username':'freshmeat', 'password':'1'}
    Bilingual_PL40_Teacher = {'displayname':'asd1 t', 'teacherid':'10651943'}
    Bilingual_PL20_Teacher = {'displayname': '', 'teacherid':''}
    Global_BEG_PL40_Teacher = {'displayname':'asd3 t','teacherid':'10651973'}
    Global_BEG_PL20_Teacher = {'displayname': '', 'teacherid': ''}
    Global_BEG_PL40_CN_Teacher = {'displayname': '', 'teacherid': ''}
    EFTV_TEACHER = {'displayname': '', 'teacherid':''}
    Bilingual_GL_Teacher = {'displayname':'', 'teacherid':''}
    Global_GL_Teacher = {'displayname':'','teacherid':''}
    Bilingual_EVC_PL20_Teacher = {'displayname':'','teacherid':''}
    Bilingual_PL20_Trial_Teacher = {'displayname': 'asd7 t', 'teacherid':'23678029'}
    Global_BEG_PL20_Trial_Teacher = {'displayname': 'asd8 t', 'teacherid': '23645087'}

class STG_Account(object):
    EFEC_Account = {'username': 'stest610', 'password': '1'}
    EFEC_EVC_Account = {'username': 'stest651', 'password': '1'}
    EFEC_BEG_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10856', 'password': '1'}
    EFEC_ELE_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10857', 'password': '1'}
    EFEC_ADV_NOT_IN_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10858', 'password': '1'}
    EFEC_BEG_IN_EVC_ROLLOUT_Account = {'username': 'stest10861', 'password': '1'}
    EFEC_ELE_IN_EVC_ROLLOUT_Account = {'username': 'stest10862', 'password': '1'}
    EFEC_ADV_IN_EVC_ROLLOUT_Account = {'username': 'stest10863', 'password': '1'}
    EFEC_BEG_IN_WHITE_LIST_Account = {'username': 'stest10864', 'password': '1'}
    EFEC_ELE_IN_WHITE_LIST_Account = {'username': 'stest10866', 'password': '1'}
    EFEC_ADV_IN_WHITE_LIST_Account = {'username': 'stest10867', 'password': '1'}
    EFEC_BEG_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10868', 'password': '1'}
    EFEC_ELE_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10869', 'password': '1'}
    EFEC_ADV_IN_BOTH_EVC_ROLLOUT_AND_WHITE_LIST_Account = {'username': 'stest10872', 'password': '1'}
    #cn gl account
    B2C_Account = {'username': 'ftetc', 'password': '1'}
    B2B_Account = {'username': 'qamotiprivate04@qp1.org', 'password': '1'}
    B2B_BEG_Account = {'username': 'ATEAM_B2B_BEG', 'password': '1'}
    B2B_ELE_Account = {'username': 'ATEAM_B2B_ELE', 'password': '1'}
    B2B_ADV_Account = {'username': 'ATEAM_B2B_ADV', 'password': '1'}
    EFTV_Account = {'username':'', 'password':''}
    B2B_No_Coupon_Account = {'username': '', 'password': ''}
    EFEC_No_Coupon_Account = {'username': 'stest9739', 'password': '1'}
    EFEC_No_Booked_Class_Account = {'username': 'stest9740', 'password': '1'}
    Admin_Account = {'username':'freshmeat', 'password':'vamper'}
    Bilingual_PL40_Teacher = {'displayname':'', 'teacherid':'12507908'}
    Bilingual_PL20_Teacher = {'displayname': '', 'teacherid':'10593582'}
    Global_BEG_PL40_Teacher = {'displayname':'', 'teacherid':'9660267'}
    Global_BEG_PL20_Teacher = {'displayname':'Alexander Bali', 'teacherid':'10593582'}
    Bilingual_GL_Teacher = {'displayname':'', 'teacherid':'10593582'}
    Global_GL_Teacher = {'displayname':'', 'teacherid':'9660267'}
    EFTV_TEACHER = {'displayname': 'asd6 t', 'teacherid':'23661336'}
    Bilingual_EVC_PL20_Teacher = {'displayname':'','teacherid':''}
    Bilingual_PL20_Trial_Teacher = {'displayname': 'asd7 t', 'teacherid':'23678029'}
    Global_BEG_PL20_Trial_Teacher = {'displayname': 'asd8 t', 'teacherid': '23645087'}