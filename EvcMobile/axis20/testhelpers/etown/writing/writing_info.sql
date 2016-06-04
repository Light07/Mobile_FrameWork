SELECT Writing.Writing_id,
Activity_id,
ContentText,
LanguageCode,
LevelCode,
Marketcode,
PartnerCode,
StudentCourse_id,
StudentMember_id,
Topic,
WritingTypeCode,
CourseName,
LevelName,
CorrectorMember_id,
TemplateCode,
Grade,
Comment
from axis20.AcademicContent..Writing
LEFT JOIN AcademicContent..WritingQueue
ON Writing.Writing_id = WritingQueue.Writing_id
LEFT JOIN AcademicContent..WritingStorage
ON Writing.Storage_id = WritingStorage.Storage_id
LEFT JOIN AcademicContent..WritingStudentInfo
ON Writing.Writing_id = WritingStudentInfo.Writing_id
LEFT JOIN AcademicContent..WritingCorrection
ON WritingQueue.WritingQueue_id = WritingCorrection.WritingQueue_id
WHERE Writing.Writing_id = {writing_id}