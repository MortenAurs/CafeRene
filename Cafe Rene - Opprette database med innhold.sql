DROP SCHEMA IF EXISTS Caferene2018;
CREATE SCHEMA Caferene2018;

USE Caferene2018;


CREATE TABLE Kategori
(
KategoriID CHAR(2),
Kategorinavn CHAR(25),
CONSTRAINT KategoriPK Primary KEY (KategoriID)
);

CREATE TABLE Produkt
(
Produktnr CHAR(4),
Produktnavn CHAR(25),
KategoriID CHAR(2),
Pris DECIMAL(8,2),
Tilgjengelighet CHAR(7),
CONSTRAINT VarerPK PRIMARY KEY (Produktnr, Produktnavn),
CONSTRAINT VarerKategoriFK FOREIGN KEY (KategoriID) REFERENCES Kategori(KategoriID)
);

CREATE TABLE Solgt
(
Salgsnr CHAR(8),
Produktnr CHAR(4),
Tidspunkt TIMESTAMP,
Beløp DECIMAL(8,2),
CONSTRAINT SolgtPK PRIMARY KEY (Salgsnr),
CONSTRAINT SolgtProduktFK FOREIGN KEY (Produktnr) REFERENCES Produkt(Produktnr)
);

-- Legger data inn i tabeller --

INSERT INTO Kategori VALUES ('01','Kald drikke');
INSERT INTO Kategori VALUES ('02','Varm drikke');
INSERT INTO Kategori VALUES ('03','Middag');
INSERT INTO Kategori VALUES ('04','Rundstykker og boller');
INSERT INTO Kategori VALUES ('05','Dessert');

INSERT INTO Produkt VALUES ('1','Cola-Zero 0,5l', '01', 27.00, NULL);
INSERT INTO Produkt VALUES ('2','Cola 0,5l', '01', 30.00, NULL);
INSERT INTO Produkt VALUES ('3','Fanta 0,5l', '01', 30.00, NULL);
INSERT INTO Produkt VALUES ('4','Farris 0,5l', '01', 25.00, NULL);
INSERT INTO Produkt VALUES ('5','Villa 0,5l', '01', 30.00, NULL);
INSERT INTO Produkt VALUES ('6','Red Bull 0,33l', '01', 25.00, NULL);
INSERT INTO Produkt VALUES ('7','Bris Granateple 0,5l', '01', 25.00, NULL);
INSERT INTO Produkt VALUES ('8','Battery 0,5l', '01', 25.00, NULL);
INSERT INTO Produkt VALUES ('9','Eplejuice 0,33l', '01', 20.00, NULL);
INSERT INTO Produkt VALUES ('10','Appelsinjuice 0,33l', '01', 20.00, NULL);
INSERT INTO Produkt VALUES ('11','Kaffe liten', '02', 15.00, NULL);
INSERT INTO Produkt VALUES ('12','Kaffe stor', '02', 25.00, NULL);
INSERT INTO Produkt VALUES ('13','Te', '02', 15.00, NULL);
INSERT INTO Produkt VALUES ('14','Kakao liten', '02', 15.90, NULL);
INSERT INTO Produkt VALUES ('15','Kakao stor', '02', 25.90, NULL);
INSERT INTO Produkt VALUES ('16','Espresso', '02', 27.90, NULL);
INSERT INTO Produkt VALUES ('17','Kjøttboller', '03', 129.90, NULL);
INSERT INTO Produkt VALUES ('18','Sandwich', '03', 109.90, NULL);
INSERT INTO Produkt VALUES ('19','Gryterett', '03', 119.90, NULL);
INSERT INTO Produkt VALUES ('20','Ost- og skinkesmørbrød', '04', 29.90, NULL);
INSERT INTO Produkt VALUES ('21','Kanelbolle', '04', 20.00, NULL);
INSERT INTO Produkt VALUES ('22','Wienerbrød', '04', 14.90, NULL);
INSERT INTO Produkt VALUES ('23','Rosinboller', '04', 10.00, NULL);
INSERT INTO Produkt VALUES ('24','Solboller', '04', 19.90, NULL);
INSERT INTO Produkt VALUES ('25','Ostekake', '05', 30.00, NULL);
INSERT INTO Produkt VALUES ('26','Créme Brûlée', '05', 34.90, NULL);
INSERT INTO Produkt VALUES ('27','Dronning Maud', '05', 29.90, NULL);
INSERT INTO Produkt VALUES ('28','Kuleis', '05', 25.00, NULL);
INSERT INTO Produkt VALUES ('29','Soft-Is', '05', 19.90, NULL);
INSERT INTO Produkt VALUES ('30','Eplekake med vaniljeis', '05', 35.90, NULL);
INSERT INTO Produkt VALUES ('31','Frukt med vaniljeis', '05', 24.90, NULL);





DROP USER 'Cafesjef';
CREATE USER 'Cafesjef' IDENTIFIED BY 'Caferene';

GRANT ALL PRIVILEGES ON Caferene TO 'Cafesjef';

GRANT SELECT ON Kategori TO 'Cafesjef';
GRANT INSERT ON Kategori TO 'Cafesjef';
GRANT DELETE ON Kategori TO 'Cafesjef';
GRANT UPDATE ON Kategori TO 'Cafesjef';

GRANT SELECT ON Produkt TO 'Cafesjef';
GRANT INSERT ON Produkt TO 'Cafesjef';
GRANT DELETE ON Produkt TO 'Cafesjef';
GRANT UPDATE ON Produkt TO 'Cafesjef';

GRANT SELECT ON Solgt TO 'Cafesjef';
GRANT INSERT ON Solgt TO 'Cafesjef';
GRANT DELETE ON Solgt TO 'Cafesjef';
GRANT UPDATE ON Solgt TO 'Cafesjef';










