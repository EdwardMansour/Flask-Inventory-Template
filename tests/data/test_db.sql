INSERT INTO Product (id, name, amount, is_destroyed, user_id, expiry_date) VALUES
(1, 'item-1-1', 2.5, 0, 2, '2024-11-14'),
(2, 'item-1-2', 2.5, 0, 2, '2024-11-14'),
(3, 'item-1-3', 2.5, 0, 2, '2024-11-14'),
(4, 'item-1-4', 2.5, 0, 2, '2024-11-14'),
(5, 'item-1-5', 2.5, 0, 2, '2024-11-14'),
(6, 'item-1', 2.5, 0, 1, '2024-11-14'),
(7, 'item-2', 2.5, 0, 1, '2024-11-14'),
(8, 'item-3', 2.5, 0, 1, '2024-11-14'),
(9, 'item-4', 2.5, 0, 1, '2024-11-14'),
(10, 'item-5', 2.5, 0, 1, '2024-11-14'),
(11, 'item-1-admin', 2.5, 0, 3, '2024-11-14'),
(12, 'item-2-admin', 2.5, 0, 3, '2024-11-14'),
(13, 'item-3-admin', 2.5, 0, 3, '2024-11-14'),
(14, 'item-4-admin', 2.5, 0, 3, '2024-11-14'),
(15, 'item-5-admin', 2.5, 0, 3, '2024-11-14');

INSERT INTO User (id, username, date_of_birth, role, password_hash) VALUES
(1, 'edward', '1996-01-17', 'REGULAR', '$2b$12$wv7dLp1YiBQyQAH27Cars.2E1O6UJI7ZotjzoXb0EFTjfOh/7zBnW'),
(2, 'edward-1', '1996-01-17', 'REGULAR', '$2b$12$tCtcXMGalF5zvL3jQ0vHbe9bg7v8lolbncubfzqkM4JFevlXYFhFa'),
(3, 'admin', '2024-10-04', 'ADMIN', '$2b$12$Y1BWd5uFcFXEyzDnKxU.YuwIdaODwaS5EACqyH2ZSjq.B8SxoTccq');