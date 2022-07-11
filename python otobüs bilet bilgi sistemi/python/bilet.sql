-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 14 May 2020, 15:36:35
-- Sunucu sürümü: 10.1.30-MariaDB
-- PHP Sürümü: 5.6.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `bilet`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `biletsatiss`
--

CREATE TABLE `biletsatiss` (
  `id` int(11) NOT NULL,
  `adi` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL,
  `tc` varchar(11) NOT NULL,
  `telefon` varchar(11) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `cinsiyet` varchar(6) NOT NULL,
  `kalkis` varchar(15) NOT NULL,
  `varis` varchar(15) NOT NULL,
  `tarih` varchar(20) NOT NULL,
  `saat` varchar(5) NOT NULL,
  `sefer` varchar(3) NOT NULL,
  `koltuk_no` varchar(2) NOT NULL,
  `otobus` varchar(50) NOT NULL,
  `ucret` varchar(10) NOT NULL,
  `otobus_id` int(11) NOT NULL,
  `calisan_giris_id` int(11) NOT NULL,
  `marka_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `biletsatiss`
--

INSERT INTO `biletsatiss` (`id`, `adi`, `soyad`, `tc`, `telefon`, `mail`, `cinsiyet`, `kalkis`, `varis`, `tarih`, `saat`, `sefer`, `koltuk_no`, `otobus`, `ucret`, `otobus_id`, `calisan_giris_id`, `marka_id`) VALUES
(15, 'berkan', 'tÃ¼rkyÄ±lmaz', '12568742926', '05267895462', 'turkyilmaz_berkan@hotmail.com', 'erkek', 'Antalya', 'NevÅŸehir', '2020-05-31', '12.00', '104', '1', '', '', 0, 0, 0),
(16, 'berkan', 'tÃ¼rkyÄ±lmaz', '12568742926', '05267895462', 'turkyilmaz_berkan@hotmail.com', 'erkek', 'Antalya', 'Gaziantep', '0000-00-00', '11.00', '103', '9', 'LÃ¼ks Karadeniz', '', 0, 0, 0),
(17, 'betül', 'türky?lmaz', '16857452624', '05354789686', 'turkyilmaz@gmail.com', 'Kad?n', 'ANKARA', 'ANTALYA', '0000-00-00', '12.00', '102', '3', '', '150', 0, 0, 0),
(18, 'beyza', 'türky?lmaz', '16978546212', '05326879555', 'beyzaturk@gmail.com', 'Kad?n', 'ANKARA', 'ANTALYA', '13Haziran2020', '12.00', '102', '5', '', '150', 0, 0, 0);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `calisan_bilgileri`
--

CREATE TABLE `calisan_bilgileri` (
  `id` int(11) NOT NULL,
  `ad` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL,
  `tc` varchar(11) NOT NULL,
  `telefon` varchar(11) NOT NULL,
  `cinsiyet` varchar(6) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `adres` text NOT NULL,
  `ise_giris_tarihi` date NOT NULL,
  `iban_no` varchar(30) NOT NULL,
  `calisan_maas` int(11) NOT NULL,
  `dogum_tarihi` date NOT NULL,
  `calisan_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `calisan_giris`
--

CREATE TABLE `calisan_giris` (
  `id` int(11) NOT NULL,
  `kadi` varchar(40) NOT NULL,
  `sifre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `calisan_giris`
--

INSERT INTO `calisan_giris` (`id`, `kadi`, `sifre`) VALUES
(1, 'admin', '1234');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `marka`
--

CREATE TABLE `marka` (
  `id` int(11) NOT NULL,
  `markaadi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `otobusler`
--

CREATE TABLE `otobusler` (
  `id` int(11) NOT NULL,
  `plaka` varchar(10) NOT NULL,
  `koltuksayisi` int(3) NOT NULL,
  `marka_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `seferler`
--

CREATE TABLE `seferler` (
  `id` int(11) NOT NULL,
  `sefer_no` int(11) NOT NULL,
  `baslangicsube` varchar(50) NOT NULL,
  `bitissube` varchar(50) NOT NULL,
  `saat` varchar(6) NOT NULL,
  `tarih` varchar(50) NOT NULL,
  `plaka` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Tablo döküm verisi `seferler`
--

INSERT INTO `seferler` (`id`, `sefer_no`, `baslangicsube`, `bitissube`, `saat`, `tarih`, `plaka`) VALUES
(1, 102, 'Ankara', 'Antalya', '12:00', '2020-05-13', '53 BT 352'),
(2, 103, 'Antalya', 'Rize', '13.00', '0000-00-00', '07 HH 458');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `biletsatiss`
--
ALTER TABLE `biletsatiss`
  ADD PRIMARY KEY (`id`),
  ADD KEY `otobus_id` (`otobus_id`),
  ADD KEY `calisan_giris_id` (`calisan_giris_id`);

--
-- Tablo için indeksler `calisan_bilgileri`
--
ALTER TABLE `calisan_bilgileri`
  ADD PRIMARY KEY (`id`),
  ADD KEY `calisan_id` (`calisan_id`);

--
-- Tablo için indeksler `calisan_giris`
--
ALTER TABLE `calisan_giris`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `marka`
--
ALTER TABLE `marka`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `otobusler`
--
ALTER TABLE `otobusler`
  ADD PRIMARY KEY (`id`),
  ADD KEY `marka_id` (`marka_id`);

--
-- Tablo için indeksler `seferler`
--
ALTER TABLE `seferler`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `biletsatiss`
--
ALTER TABLE `biletsatiss`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Tablo için AUTO_INCREMENT değeri `calisan_bilgileri`
--
ALTER TABLE `calisan_bilgileri`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `calisan_giris`
--
ALTER TABLE `calisan_giris`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `marka`
--
ALTER TABLE `marka`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `otobusler`
--
ALTER TABLE `otobusler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `seferler`
--
ALTER TABLE `seferler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `calisan_bilgileri`
--
ALTER TABLE `calisan_bilgileri`
  ADD CONSTRAINT `calisan_bilgileri_ibfk_1` FOREIGN KEY (`calisan_id`) REFERENCES `calisan_giris` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `otobusler`
--
ALTER TABLE `otobusler`
  ADD CONSTRAINT `otobusler_ibfk_1` FOREIGN KEY (`id`) REFERENCES `biletsatiss` (`otobus_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
