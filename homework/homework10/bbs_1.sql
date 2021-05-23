/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : python_test

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2021-05-23 16:12:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bbs_1
-- ----------------------------
DROP TABLE IF EXISTS `bbs_1`;
CREATE TABLE `bbs_1` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `text` varchar(500) DEFAULT NULL,
  `name1` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `date1` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `isdelete` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bbs_1
-- ----------------------------
INSERT INTO `bbs_1` VALUES ('1', '666', '小小', '2021-05-22 20:38:37', 'no');
INSERT INTO `bbs_1` VALUES ('2', 'ccc', '小红', '2021-05-22 20:34:17', 'no');
INSERT INTO `bbs_1` VALUES ('3', '123', '小亮', '2021-05-22 20:34:20', 'no');
