SELECT UserName
             ,Password
             ,CenterCode
FROM ET_Main..Members
INNER JOIN Teachers..Teacher
ON Members.MemberId = Teacher.Member_id
WHERE MemberId = {member_id}