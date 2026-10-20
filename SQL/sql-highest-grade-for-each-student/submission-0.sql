-- Write your query below

WITH highest AS (
SELECT student_id, exam_id, score, ROW_NUMBER() OVER (
    PARTITION BY student_id
    ORDER BY score DESC, exam_id ASC
) as scores
FROM exam_results
)


SELECT student_id, exam_id, score FROM highest
WHERE scores = 1