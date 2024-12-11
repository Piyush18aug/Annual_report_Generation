

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";



CREATE TABLE IF NOT EXISTS `user` (
  `names` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pass` bigint(8) NOT NULL,
  `confirm_password` bigint(8) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


INSERT INTO `user` (`names`, `email`, `username`, `pass`, `confirm_password`) VALUES
('Ojas.', 'ojasmaniyar.info@gmail.com', 'maniyarojas25', 12345678, 12345678);
