/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : python_test

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2021-05-23 16:12:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for classinfo
-- ----------------------------
DROP TABLE IF EXISTS `classinfo`;
CREATE TABLE `classinfo` (
  `classID` int NOT NULL,
  `classname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of classinfo
-- ----------------------------
INSERT INTO `classinfo` VALUES ('1', '计算1901');
INSERT INTO `classinfo` VALUES ('2', '计算1902');
INSERT INTO `classinfo` VALUES ('3', '信安1901');
INSERT INTO `classinfo` VALUES ('4', '信安1902');
INSERT INTO `classinfo` VALUES ('5', '软件1901');
INSERT INTO `classinfo` VALUES ('6', '软件1902');
