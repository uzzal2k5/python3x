SELECT news.id FROM `news`
               WHERE (newstime between '2012-01-16 00:00:00' AND  '2012-01-16 23:59:59')
                     AND ((MATCH(titolo, testo) AGAINST('"Public Administration" "SOMETHING" "ELSE" "ROMA" "MILANO"' IN BOOLEAN MODE)))
ORDER BY newstime DESC LIMIT 23 OFFSET 0;
23sec


SELECT id FROM(SELECT * from news where newstime between '2012-01-16 00:00:00' AND  '2012-01-16 23:59:59') as N
          where ((MATCH(titolo, testo) AGAINST('"Public Administration" "FIAT" "SOMETHING" "ELSE" "ROMA" "MILANO"' IN BOOLEAN MODE)))
ORDER BY newstime DESC LIMIT 23 OFFSET 0;
.09sec




explain SELECT news.id FROM `news` WHERE (newstime between '2012-01-16 00:00:00' AND  '2012-01-16 23:59:59')
AND ((MATCH(titolo, testo) AGAINST('"Public Administration" "FIAT" "SOMETHING" "ELSE" "ROMA" "MILANO"' IN BOOLEAN MODE)))
ORDER BY newstime DESC LIMIT 23 OFFSET 0;


SELECT news.id
FROM `news`
USE INDEX (index_news_on_newstime)
WHERE (newstime between '2012-01-16 00:00:00' AND  '2012-01-16 23:59:59')
  AND ((MATCH(titolo, testo) AGAINST('"Public Administration" "SOMETHING" "ELSE" "ROMA" "MILANO"' IN BOOLEAN MODE)))
ORDER BY newstime DESC LIMIT 23 OFFSET 0;


SELECT news.id
FROM `news`
USE INDEX (index_news_on_newstime)
WHERE (newstime between '2012-01-16 00:00:00' AND  '2012-01-16 23:59:59')
  AND ((MATCH(titolo, testo) AGAINST('"Public Administration" "SOMETHING" "ELSE" "ROMA" "MILANO"' IN BOOLEAN MODE)))
ORDER BY newstime DESC LIMIT 23 OFFSET 0;