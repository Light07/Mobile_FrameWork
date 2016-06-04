DECLARE @Student_Member_ID INT
DECLARE @Subscription_ID INT

-- Parameters --
SET @Student_Member_ID = {member_id}

SELECT TOP 1 @Subscription_ID = SubscriptionId from axis20.ET_Commerce..Subscriptions
WHERE MemberId = @Student_Member_ID
ORDER BY SubscriptionId DESC

IF EXISTS ( SELECT DateExpires, IsActive
            from axis20.ET_Commerce..Subscriptions
            WHERE SubscriptionId = @Subscription_ID
                AND (DateExpires < GETDATE() OR IsActive = 0))
    BEGIN
        UPDATE ET_Commerce..Subscriptions
        SET IsActive = 1,
            DateExpires = DATEADD(year, 1, GETDATE())
        WHERE SubscriptionId = @Subscription_ID

        UPDATE ET_Commerce..FeatureAccessGrants
        SET ActiveTo = DATEADD(year, 1, GETDATE())
        WHERE MemberId = @Student_Member_ID
    END