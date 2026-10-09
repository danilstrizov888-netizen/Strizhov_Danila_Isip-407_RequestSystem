-- 5 SELECT
SELECT * FROM Users;
SELECT * FROM Requests;
SELECT * FROM Statuses;
SELECT * FROM Categories;
SELECT * FROM Comments;

-- 3 SELECT с WHERE
SELECT * FROM Requests WHERE status_id = 1;
SELECT * FROM Requests WHERE category_id = 1;
SELECT * FROM Users WHERE role_id = 3;

-- 2 UPDATE
UPDATE Requests SET status_id = 2 WHERE id = 2;
UPDATE Users SET full_name = 'Козлов К.К. (обновлён)' WHERE id = 4;

-- 2 DELETE
DELETE FROM Comments WHERE id = 2;
DELETE FROM Requests WHERE id = 3;

-- 2 JOIN
SELECT r.id, r.title, s.name AS status, c.name AS category
FROM Requests r
JOIN Statuses s ON r.status_id = s.id
JOIN Categories c ON r.category_id = c.id;

SELECT r.id, r.title, u.full_name AS author
FROM Requests r
JOIN Users u ON r.author_id = u.id;