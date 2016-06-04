SELECT Course.CourseName
            ,CourseActivityContent.CourseActivityTopic
            ,CourseLevel.LevelCode
            ,CourseLevel.LevelNo
            ,CourseUnit.UnitNo
            ,CourseActivityContent.GradeMode
from axis20.SchoolPlatform..CourseStepActivity
-- Get StandardLevelCode, StandardLevelName
INNER JOIN SchoolPlatform..CourseStep
ON CourseStepActivity.CourseStep_id = CourseStep.CourseStep_id
INNER JOIN SchoolPlatform..CourseLesson
ON CourseStep.CourseLesson_id = CourseLesson.CourseLesson_id
INNER JOIN SchoolPlatform..CourseUnit
ON CourseLesson.CourseUnit_id = CourseUnit.CourseUnit_id
INNER JOIN SchoolPlatform..CourseLevel
ON CourseUnit.CourseLevel_id = CourseLevel.CourseLevel_id
-- Get CourseName
INNER JOIN SchoolPlatform..Course
ON CourseLevel.Course_id = Course.Course_id
-- Get GradeMode, CourseActivityTopic (Topic)
INNER JOIN SchoolPlatform..CourseActivityContent
ON CourseStepActivity.CourseActivityContent_id = CourseActivityContent.CourseActivityContent_id
WHERE CourseStepActivity.CourseStepActivity_id = {activity_id}