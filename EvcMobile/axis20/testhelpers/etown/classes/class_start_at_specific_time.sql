DECLARE @Specific_StartTime varchar(100)
DECLARE @Specific_EndTime  varchar(100)

SET @Specific_StartTime = '{Specific_time}'
SET @Specific_EndTime = DATEADD(hh,1,@Specific_StartTime)

;with CTE AS
(
SELECT
(CASE WHEN StartTime >= @Specific_StartTime AND StartTime < @Specific_EndTime THEN 1 ELSE 0 END) as C1,
(CASE WHEN StartTime < @Specific_StartTime AND EndTime > @Specific_StartTime THEN 1 ELSE 0 END) as C2,
* FROM Teachers.dbo.class
 WHERE ClassStatusCode != 'Canceled'
)
SELECT class_id from CTE WHERE C1 =1 or C2=1