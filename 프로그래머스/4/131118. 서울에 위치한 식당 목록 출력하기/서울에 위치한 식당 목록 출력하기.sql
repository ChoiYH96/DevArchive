-- 코드를 입력하세요
SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
FROM REST_INFO I INNER JOIN (SELECT REST_ID, ROUND(SUM(REVIEW_SCORE)/COUNT(REST_ID),2) AS SCORE FROM REST_REVIEW GROUP BY REST_ID) V ON I.REST_ID = V.REST_ID
WHERE ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC;