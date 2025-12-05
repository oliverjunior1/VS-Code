CREATE TABLE tbl_types (
    id SERIAL PRIMARY KEY,
    typeName VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE tbl_stages (
    id SERIAL PRIMARY KEY,
    stageName VARCHAR(20) NOT NULL UNIQUE
);

ALTER TABLE tbl_cards
    DROP COLUMN type,
    DROP COLUMN stage,
    ADD COLUMN type_id INT,
    ADD COLUMN stage_id INT,
    ADD CONSTRAINT fk_type
        FOREIGN KEY (type_id)
        REFERENCES tbl_types (id)
        ON DELETE SET NULL,
    ADD CONSTRAINT fk_stage
        FOREIGN KEY (stage_id)
        REFERENCES tbl_stages (id)
        ON DELETE SET NULL;