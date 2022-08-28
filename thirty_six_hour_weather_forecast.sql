-- 主機： 127.0.0.1
-- 產生時間： 2022-08-28 10:39:55
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `cwb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `thirty_six_hour_weather_forecast`
--

CREATE TABLE `thirty_six_hour_weather_forecast` (
  `id` int(11) NOT NULL,
  `locationName` text NOT NULL,
  `36hwf01` text NOT NULL,
  `36hwf02` text NOT NULL,
  `36hwf03` text NOT NULL,
  `36hwf04` text NOT NULL,
  `36hwf05` text NOT NULL,
  `36hwf06` text NOT NULL,
  `36hwf07` text NOT NULL,
  `36hwf08` text NOT NULL,
  `36hwf09` text NOT NULL,
  `36hwf10` text NOT NULL,
  `36hwf11` text NOT NULL,
  `36hwf12` text NOT NULL,
  `36hwf13` text NOT NULL,
  `36hwf14` text NOT NULL,
  `36hwf15` text NOT NULL,
  `36hwf16` text NOT NULL,
  `36hwf17` text NOT NULL,
  `36hwf18` text NOT NULL,
  `36hwf19` text NOT NULL,
  `36hwf20` text NOT NULL,
  `36hwf21` text NOT NULL,
  `36hwf22` text NOT NULL,
  `36hwf23` text NOT NULL,
  `36hwf24` text NOT NULL,
  `36hwf25` text NOT NULL,
  `36hwf26` text NOT NULL,
  `36hwf27` text NOT NULL,
  `36hwf28` text NOT NULL,
  `36hwf29` text NOT NULL,
  `36hwf30` text NOT NULL,
  `36hwf31` text NOT NULL,
  `36hwf32` text NOT NULL,
  `36hwf33` text NOT NULL,
  `36hwf34` text NOT NULL,
  `36hwf35` text NOT NULL,
  `36hwf36` text NOT NULL,
  `36hwf37` text NOT NULL,
  `36hwf38` text NOT NULL,
  `36hwf39` text NOT NULL,
  `36hwf40` text NOT NULL,
  `36hwf41` text NOT NULL,
  `36hwf42` text NOT NULL,
  `36hwf43` text NOT NULL,
  `36hwf44` text NOT NULL,
  `36hwf45` text NOT NULL,
  `36hwf46` text NOT NULL,
  `36hwf47` text NOT NULL,
  `36hwf48` text NOT NULL,
  `36hwf49` text NOT NULL,
  `36hwf50` text NOT NULL,
  `36hwf51` text NOT NULL,
  `36hwf52` text NOT NULL,
  `36hwf53` text NOT NULL,
  `36hwf54` text NOT NULL,
  `36hwf55` text NOT NULL,
  `36hwf56` text NOT NULL,
  `36hwf57` text NOT NULL,
  `36hwf58` text NOT NULL,
  `36hwf59` text NOT NULL,
  `36hwf60` text NOT NULL,
  `36hwf61` text NOT NULL,
  `36hwf62` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `thirty_six_hour_weather_forecast`
--
ALTER TABLE `thirty_six_hour_weather_forecast`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `thirty_six_hour_weather_forecast`
--
ALTER TABLE `thirty_six_hour_weather_forecast`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
