/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 80022
Source Host           : localhost:3306
Source Database       : python_test

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2021-05-23 16:12:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for studentinfo
-- ----------------------------
DROP TABLE IF EXISTS `studentinfo`;
CREATE TABLE `studentinfo` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `classID` int DEFAULT NULL,
  `sex` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of studentinfo
-- ----------------------------
INSERT INTO `studentinfo` VALUES ('1', '张三', '20', '2', '男');
INSERT INTO `studentinfo` VALUES ('2', '李四', '21', '1', '男');
INSERT INTO `studentinfo` VALUES ('3', '王五', '21', '3', '女');
INSERT INTO `studentinfo` VALUES ('4', '赵六', '20', '5', '女');
INSERT INTO `studentinfo` VALUES ('5', '钱七', '21', '4', '男');
INSERT INTO `studentinfo` VALUES ('6', '孙一', '20', '6', '女');
INSERT INTO `studentinfo` VALUES ('7', '周二', '21', '3', '中性');
INSERT INTO `studentinfo` VALUES ('8', '吴六', '20', '1', '保密');
INSERT INTO `studentinfo` VALUES ('9', '彭于晏', '30', '3', '男');
INSERT INTO `studentinfo` VALUES ('10', '刘德华', '50', '2', '男');
INSERT INTO `studentinfo` VALUES ('11', '周杰伦', '50', '5', '男');
INSERT INTO `studentinfo` VALUES ('12', '程坤', '30', '1', '男');
INSERT INTO `studentinfo` VALUES ('13', '郭靖', '35', '4', '男');
INSERT INTO `studentinfo` VALUES ('14', '小明', '26', '5', '女');
INSERT INTO `studentinfo` VALUES ('15', '小月月', '31', '6', '女');
INSERT INTO `studentinfo` VALUES ('16', '黄蓉', '35', '3', '女');
INSERT INTO `studentinfo` VALUES ('17', '王祖贤', '46', '5', '女');
INSERT INTO `studentinfo` VALUES ('18', '刘亦菲', '45', '6', '女');
INSERT INTO `studentinfo` VALUES ('19', '静香', '30', '2', '女');
INSERT INTO `studentinfo` VALUES ('20', '金星', '40', '3', '中性');
INSERT INTO `studentinfo` VALUES ('21', '黄一二', '30', '2', '男');
