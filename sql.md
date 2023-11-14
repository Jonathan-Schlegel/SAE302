# Colis :
```sql
CREATE TABLE `DB`.`colis` ( `pkey` INT NOT NULL AUTO_INCREMENT , `poids` INT NOT NULL , `hauteur` INT NOT NULL , `largeur` INT NOT NULL , `longueur` INT NOT NULL , `id_exp` INT NOT NULL , `id_transp` INT NOT NULL , `id_dest` INT NOT NULL , PRIMARY KEY (`pkey`)) ENGINE = InnoDB;
```

# State :
```sql
CREATE TABLE `DB`.`state` ( `pkey` INT NOT NULL AUTO_INCREMENT , `id_colis` INT NOT NULL , `embal` TIMESTAMP NULL DEFAULT NULL , `arrive` TIMESTAMP NULL DEFAULT NULL , `depart` TIMESTAMP NULL DEFAULT NULL , `livre` TIMESTAMP NULL DEFAULT NULL , `recu` TIMESTAMP NULL DEFAULT NULL , `id_livr` INT NULL DEFAULT NULL , `is_deleted` BOOLEAN NOT NULL DEFAULT FALSE , PRIMARY KEY (`pkey`)) ENGINE = InnoDB;
```

# Localisation :
```sql
CREATE TABLE `DB`.`location` ( `pkey` INT NOT NULL AUTO_INCREMENT , `id_colis` INT NOT NULL , `longitude` VARCHAR(255) NOT NULL , `latitude` VARCHAR(255) NOT NULL , `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`pkey`)) ENGINE = InnoDB;
```


# Expéditeur :
```sql
CREATE TABLE `DB`.`expéditeur` ( `pkey` INT NOT NULL AUTO_INCREMENT , `nom` VARCHAR(50) NOT NULL , PRIMARY KEY (`pkey`)) ENGINE = InnoDB;
```

# Transporteur :
```sql
CREATE TABLE `DB`.`transporteur` ( `pkey` INT NOT NULL AUTO_INCREMENT , `nom` VARCHAR(50) NOT NULL , PRIMARY KEY (`pkey`)) ENGINE = InnoDB;
```
# Destinataire :
```sql
CREATE TABLE `DB`.`destinataire` ( `pkey` INT NOT NULL AUTO_INCREMENT , `nom` VARCHAR(255) NOT NULL , `prénom` VARCHAR(255) NOT NULL , `adresse` TEXT NOT NULL , `code_postal` VARCHAR(32) NOT NULL , `ville` VARCHAR(255) NOT NULL , `mail` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL , `téléphone` TEXT NOT NULL , PRIMARY KEY (`pkey`)) ENGINE = InnoDB;
```

