--fill sample SQL commands to save time

-- SQLite
INSERT INTO USERS (id, user_no, name, role, id_no, dob, gender, date_emp, end_date, remarks, password)
VALUES (1, 'user001', '6LACK', 'ADMIN', 12345678, '2000-1-1', 'MALE', '2021-11-11', '2021-11-12', 'BAD', '12345');
-- SQLite
INSERT INTO USERS (id, user_no, name, role, id_no, dob, gender, date_emp, end_date, remarks, password)
VALUES (2, 'user002', '6Locc', 'CASHIER', 12345678, '2000-1-1', 'MALE', '2021-11-11', '2021-11-12', 'BAD', 'cashier');

-- SQLite
INSERT INTO STOCK (id, item_code, category, item_name, quantity, price, supplier, date_added, exp_date, remarks)
VALUES (1, 'item_code', 'food', 'yoghurt', 20, 80, 'tuzo ltd', '2021-11-1', '2021-11-5', 'vanilla');