-- Роли
INSERT INTO Roles (name) VALUES ('Администратор'), ('Оператор'), ('Исполнитель'), ('Заявитель');

-- Пользователи
INSERT INTO Users (login, password_hash, full_name, role_id) VALUES
('admin', 'hash1', 'Иванов И.И.', 1),
('operator', 'hash2', 'Петров П.П.', 2),
('executor', 'hash3', 'Сидоров С.С.', 3),
('user1', 'hash4', 'Козлов К.К.', 4);

-- Статусы
INSERT INTO Statuses (name) VALUES ('Новая'), ('В работе'), ('Выполнена'), ('Закрыта');

-- Категории
INSERT INTO Categories (name) VALUES ('IT'), ('Хозяйство'), ('Документы'), ('Ремонт');

-- Заявки
INSERT INTO Requests (title, description, category_id, status_id, author_id, assignee_id) VALUES
('Принтер не работает', 'Бумага застряла', 1, 2, 4, 3),
('Заказать бумагу', 'Закончилась', 2, 1, 4, NULL),
('Сломался стул', 'Ножка отвалилась', 4, 3, 4, 3);

-- Комментарии
INSERT INTO Comments (request_id, author_id, text) VALUES
(1, 3, 'Завтра посмотрю'),
(1, 4, 'Спасибо!');