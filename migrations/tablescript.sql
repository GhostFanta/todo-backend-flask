
# Create Schema
CREATE DATABASE IF NOT EXISTS todolists;
USE todolists;


# Create table
CREATE TABLE todo_list
(
  todolist_id        INT AUTO_INCREMENT
    PRIMARY KEY,
  useremail          VARCHAR(200) NOT NULL,
  title              VARCHAR(200) NOT NULL,
  created_date       DATETIME     NOT NULL,
  last_modified_date DATETIME     NOT NULL,
  items              JSON         NOT NULL
)
  ENGINE = InnoDB;

-- auto-generated definition
CREATE TABLE modified_date
(
  modified_date_id INT AUTO_INCREMENT
    PRIMARY KEY,
  modified_date    DATETIME NOT NULL,
  todolist_id      INT      NOT NULL,
  CONSTRAINT modified_date_ibfk_1
  FOREIGN KEY (todolist_id) REFERENCES todo_list (todolist_id)
)
  ENGINE = InnoDB;

CREATE INDEX todolist_id
  ON modified_date (todolist_id);
-- auto-generated definition
CREATE TABLE alembic_version
(
  version_num VARCHAR(32) NOT NULL
    PRIMARY KEY
)
  ENGINE = InnoDB;

# Seed data migration

INSERT INTO todolists.todo_list (todolist_id, useremail, title, created_date, last_modified_date, items) VALUES (1, 'zichu@test1.com', 'I am From Migration', '2018-07-30 06:49:41', '2018-07-30 06:49:41', '"[{\\"id\\":1,\\"isCompleted\\":false,\\"content\\":\\"Item1\\"},{\\"id\\":2,\\"isCompleted\\":false,\\"content\\":\\"Item2\\"}]"');
INSERT INTO todolists.modified_date (modified_date_id, modified_date, todolist_id) VALUES (1, '2018-07-30 06:53:44', 1);

