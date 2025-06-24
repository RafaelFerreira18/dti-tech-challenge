CREATE TABLE jogo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT,
    empresa TEXT,
    data_lancamento TEXT NOT NULL,
    preco INTEGER
);

CREATE TABLE genero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE jogo_genero (
    jogo_id INTEGER NOT NULL,
    genero_id INTEGER NOT NULL,
    FOREIGN KEY (jogo_id) REFERENCES jogo(id),
    FOREIGN KEY (genero_id) REFERENCES genero(id),
    PRIMARY KEY (jogo_id, genero_id)
);