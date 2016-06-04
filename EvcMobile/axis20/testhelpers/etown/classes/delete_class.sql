DECLARE @class_id INT
SET @class_id = {Class_id}

UPDATE Teachers..Class
SET ClassStatusCode = 'Canceled',
TeacherMember_id = -1,
EvcRoom_id = NULL
WHERE Class_id = @class_id

INSERT INTO Teachers..ClassAudit
        ( Class_id ,
          Action_id ,
          TeacherMember_id ,
          StudentMember_id ,
          Comment ,
          AuditDate ,
          OperateBy_id ,
          OperaterType ,
          FromStatus ,
          ToStatus
        )
VALUES  ( @class_id ,
          25 ,
          -1 ,
          NULL ,
          'ASD Automation clear data' ,
          GETDATE() ,
          -1 ,
          'SA' ,
          '' ,
          'Canceled'
        )

UPDATE Teachers.dbo.StudentClassBooking
SET Status_id = 2
WHERE Class_id = @class_id
