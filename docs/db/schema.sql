PRAGMA foreign_keys = ON;

-- Создание таблиц

CREATE TABLE Roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    full_name TEXT NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES Roles(id)
);

CREATE TABLE Statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE Requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    assignee_id INTEGER,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    closed_at TEXT,
    FOREIGN KEY (category_id) REFERENCES Categories(id),
    FOREIGN KEY (status_id) REFERENCES Statuses(id),
    FOREIGN KEY (author_id) REFERENCES Users(id),
    FOREIGN KEY (assignee_id) REFERENCES Users(id)
);

CREATE TABLE Comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES Requests(id),
    FOREIGN KEY (author_id) REFERENCES Users(id)
);