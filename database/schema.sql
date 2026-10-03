CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS material_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contractor_id INT NOT NULL,
    material_id INT NOT NULL,
    request_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (contractor_id) REFERENCES users(id),
    FOREIGN KEY (material_id) REFERENCES materials(id)
);

CREATE TABLE IF NOT EXISTS material_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contractor_id INT NOT NULL,
    material_id INT NOT NULL,
    delivery_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (contractor_id) REFERENCES users(id),
    FOREIGN KEY (material_id) REFERENCES materials(id)
);

INSERT INTO users (name, email, password, role)
VALUES (
    'Supply Manager',
    'admin@example.com',
    'admin123',
    'Supply Manager'
)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    password = VALUES(password),
    role = VALUES(role);

INSERT INTO users (name, email, password, role)
VALUES (
    'Contractor User',
    'end_user@example.com',
    'user123',
    'Contractor'
)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    password = VALUES(password),
    role = VALUES(role);
