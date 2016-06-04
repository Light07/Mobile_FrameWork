SELECT CG.ServiceTypeCode,
            CG.ServiceSubTypeCode,
            C.StartTime,
            C.EndTime,
            CG.LevelCode,
            CG.LanguageCode,
            CG.MarketCode,
            CG.PartnerCode,
            C.EvcServerCode,
            C.TeacherMember_id
FROM Teachers..Class AS C
JOIN Teachers..ClassGroup AS CG
ON C.ClassGroup_id = CG.ClassGroup_id
WHERE C.Class_id = {class_id}