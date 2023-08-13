-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
    student_id serial PRIMARY KEY,
    first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	birthday date,
    phone varchar
);

-- 2. Добавить в таблицу student колонку middle_name varchar


-- 3. Удалить колонку middle_name


-- 4. Переименовать колонку birthday в birth_date


-- 5. Изменить тип данных колонки phone на varchar(32)


-- 6. Вставить три любых записи с автогенерацией идентификатора


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
