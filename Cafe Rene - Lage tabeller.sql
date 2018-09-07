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
CONSTRAINT VarerPK PRIMARY KEY (Produktnr),
CONSTRAINT VarerKategoriFK FOREIGN KEY (KategoriID) REFERENCES Kategori(KategoriID)
);


CREATE TABLE Solgt
(
Salgsnr CHAR(8),
Produktnr CHAR(4),
Tidspunkt TIMESTAMP,
Beløp DECIMAL(8,1),
CONSTRAINT SolgtPK PRIMARY KEY (Salgsnr),
CONSTRAINT SolgtProduktFK FOREIGN KEY (Produktnr) REFERENCES Produkt(Produktnr)
);

-- Legger data inn i tabeller --

INSERT INTO Kategori VALUES ('01','Kald drikke');
INSERT INTO Kategori VALUES ('02','Varm drikke');
INSERT INTO Kategori VALUES ('03','Middag');
INSERT INTO Kategori VALUES ('04','Rundstykker og boller');
INSERT INTO Kategori VALUES ('05','Dessert');

INSERT INTO Produkt VALUES ('0001','Cola-Zero 0,5l', '01', 27.00);
INSERT INTO Produkt VALUES ('0002','Cola 0,5l', '01', 30.00);
INSERT INTO Produkt VALUES ('0003','Fanta 0,5l', '01', 30.00);
INSERT INTO Produkt VALUES ('0004','Farris 0,5l', '01', 25.00);
INSERT INTO Produkt VALUES ('0005','Villa 0,5l', '01', 30.00);
INSERT INTO Produkt VALUES ('0006','Red Bull 0,33l', '01', 25.00);
INSERT INTO Produkt VALUES ('0007','Bris Granateple 0,5l', '01', 25.00);
INSERT INTO Produkt VALUES ('0008','Battery 0,5l', '01', 25.00);
INSERT INTO Produkt VALUES ('0009','Eplejuice 0,33l', '01', 20.00);
INSERT INTO Produkt VALUES ('0010','Appelsinjuice 0,33l', '01', 20.00);
INSERT INTO Produkt VALUES ('0011','Kaffe liten', '02', 15.00);
INSERT INTO Produkt VALUES ('0012','Kaffe stor', '02', 25.00);
INSERT INTO Produkt VALUES ('0013','Te', '02', 15.00);
INSERT INTO Produkt VALUES ('0014','Kakao liten', '02', 15.90);
INSERT INTO Produkt VALUES ('0015','Kakao stor', '02', 25.90);
INSERT INTO Produkt VALUES ('0016','Espresso', '02', 27.90);
INSERT INTO Produkt VALUES ('0017','Kjøttboller', '03', 129.90);
INSERT INTO Produkt VALUES ('0018','Sandwich', '03', 109.90);
INSERT INTO Produkt VALUES ('0019','Gryterett', '03', 119.90);
INSERT INTO Produkt VALUES ('0020','Ost- og skinkesmørbrød', '04', 29.90);
INSERT INTO Produkt VALUES ('0021','Kanelbolle', '04', 20.00);
INSERT INTO Produkt VALUES ('0022','Wienerbrød', '04', 14.90);
INSERT INTO Produkt VALUES ('0023','Rosinboller', '04', 10.00);
INSERT INTO Produkt VALUES ('0024','Solboller', '04', 19.90);
INSERT INTO Produkt VALUES ('0025','Ostekake', '05', 30.00);
INSERT INTO Produkt VALUES ('0026','Créme Brûlée', '05', 34.90);
INSERT INTO Produkt VALUES ('0027','Dronning Maud', '05', 29.90);
INSERT INTO Produkt VALUES ('0028','Kuleis', '05', 25.00);
INSERT INTO Produkt VALUES ('0029','Soft-Is', '05', 19.90);
INSERT INTO Produkt VALUES ('0030','Eplekake med vaniljeis', '05', 35.90);
INSERT INTO Produkt VALUES ('0031','Frukt med vaniljeis', '05', 24.90);

INSERT INTO Solgt VALUES ('1','0026', '2018-05-16 15:30:22', 34.90);




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










