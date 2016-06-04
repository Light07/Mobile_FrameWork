DECLARE @TeacherMember_id INT

SET @TeacherMember_id = '{TeacherMember_id}'

SELECT class_id
FROM Teachers.dbo.class
WHERE ClassStatusCode != 'Canceled'
AND TeacherMember_id = @TeacherMember_id