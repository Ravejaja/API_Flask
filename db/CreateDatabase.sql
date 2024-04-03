CREATE DATABASE IF NOT EXISTS Biblioteca;
USE Biblioteca;

CREATE TABLE IF NOT EXISTS livros(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    ano INT NOT NULL
)



INSERT INTO livros(id, nome, autor,ano) VALUES (1, 'Livro 1', 'Autor 1', 2000)
INSERT INTO livros(id, nome, autor,ano) VALUES (2, 'Livro 2', 'Autor 2', 2000)
INSERT INTO livros(id, nome, autor,ano) VALUES (2, 'Livro 3', 'Autor 3', 2000)
INSERT INTO livros(id, nome, autor,ano) VALUES (2, 'Livro 4', 'Autor 4', 2000)
