-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 08, 2025 at 08:43 AM
-- Server version: 10.11.10-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `u397527084_ELPRLV0`
--

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `number` varchar(20) NOT NULL,
  `question` varchar(500) NOT NULL,
  `yes_score` float NOT NULL,
  `no_score` float NOT NULL,
  `block` varchar(19) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `number`, `question`, `yes_score`, `no_score`, `block`) VALUES
(1439, '1', 'Can the product influence the user\'s decision-making?', -0.72, 0, 'zero_case'),
(1440, '1.1', 'Have you implemented safeguards to prevent the product from unintentionally affecting users\' autonomy?', 0.36, 0, 'zero_case'),
(1441, '1.2', 'Is there a risk of users becoming overly reliant on the product?', 0, 0.36, 'zero_case'),
(1442, '1.2.1', 'Are there measures to discourage users from over-relying on the product?', 0.36, -0.36, 'zero_case'),
(1443, '2', 'Is it possible that technical design decisions will result in significant damage?', -1, 0, 'zero_case'),
(1444, '2.1', 'Does the product comply with recognized cybersecurity standards?', 0.36, 0, 'zero_case'),
(1445, '2.2', 'Are there additional security measures against potential attacks throughout the product\'s lifecycle?', 0.28, 0, 'zero_case'),
(1446, '2.2.1', 'Have you conducted penetration tests or red-team exercises on the product?', 0, -0.28, 'zero_case'),
(1447, '2.3', 'Does the timeframe for security updates match the expected lifespan of the product?', 0.08, 0, 'zero_case'),
(1448, '2.3.1', 'Have you informed users about the duration of security update coverage?', 0, -0.08, 'zero_case'),
(1449, '2.4', 'Can the product be misused for malicious or illegal purposes?', -0.27, 0, 'zero_case'),
(1450, '2.4.1', 'Have you conducted a risk assessment to identify potential misuse scenarios? ', 0.18, 0, 'zero_case'),
(1451, '2.4.1.1', 'Have you implemented preventive measures to mitigate the risks of misuse? ', 0, -0.18, 'zero_case'),
(1452, '2.4.2', 'Can users or third parties report misuse to the product designer?', 0.09, 0, 'zero_case'),
(1453, '3', 'Is the product designed to adapt to diverse user/operator preferences and abilities?', 0, -0.365, 'zero_case'),
(1454, '3.1', 'Have you evaluated accessibility by individuals with special needs or those at risk of exclusion?', 0, -0.09, 'zero_case'),
(1455, '3.2', 'Were accessibility standards followed during development?', 0, -0.09, 'zero_case'),
(1456, '3.3', 'Have you studied and evaluated possible discrimination against affected persons?', 0, -0.18, 'zero_case'),
(1457, '3.3.1', 'Have you implemented measures to minimize unfair or discriminatory effects?', 0, -0.18, 'zero_case'),
(1458, '4', 'Does the product have a negative impact on natural environment?', -0.5, 0, 'zero_case'),
(1459, '4.1', 'Have you set up mechanisms to assess the product\'s environmental footprint?', 0.2, 0, 'zero_case'),
(1460, '4.2', 'Did you minimize the product\'s environmental impact during its lifecycle?', 0.3, 0, 'zero_case'),
(1461, '5', 'Does the product affect work conditions and organizational structures?', -0.73, 0, 'zero_case'),
(1462, '5.1', 'Have you consulted with workers and their representatives or trade unions?', 0.3, 0, 'zero_case'),
(1463, '5.2', 'Have you investigated the impact of the product on labor market?', 0.2, 0, 'zero_case'),
(1464, '5.3', 'Can the product make workers less skilled or unemployed?', 0, 0.23, 'zero_case'),
(1465, '5.3.1', 'Is there training in place to mitigate the risk of workforce de-skilling?', 0.15, 0, 'zero_case'),
(1466, '5.3.2', 'Are there pedagogical resources to enhance worker skills in relation to the product?', 0.08, 0, 'zero_case'),
(1467, '6', 'Have you established mechanisms to facilitate audits of the product?', 0, -0.5, 'zero_case'),
(1468, '6.1', 'Can the product be audited by independent third parties for assigning responsibility?', 0, -0.2, 'zero_case'),
(1469, '7', 'Are there oversight processes for ethical concerns and assigning responsibility?', 0, -0.27, 'zero_case'),
(1470, '7.1', 'Is there ongoing oversight by a third party beyond the product\'s development phase?', 0, -0.09, 'zero_case'),
(1471, '7.2', 'Have you considered establishing an ethics review board specifically for the product?', 0, -0.09, 'zero_case'),
(1472, '7.3', 'Is there a process for third parties, such as suppliers or users, to report vulnerabilities or risks?', 0, -0.09, 'zero_case'),
(1473, '7.3.1', 'Does the vulnerability reporting process contribute to updates in the product\'s risk management strategy?', 0, -0.09, 'zero_case'),
(1474, '8', 'Does the product gather specialized categories of personal data, such as biometric or health-related information?', -0.75, 0, 'gdpr_block'),
(1475, '8.1', 'Are there security protocols in place for safeguarding specialized categories of personal data?', 0.25, 0, 'gdpr_block'),
(1476, '8.1.2', 'Have you implemented measures to ensure only the essential sensitive personal data is collected?', 0, -0.25, 'gdpr_block'),
(1477, '8.2', 'Does the product collect information concerning criminal convictions or offenses?', 0, 0.25, 'gdpr_block'),
(1478, '8.2.1', 'Is the collection of such criminal data authorized by European Union or Member State law?', 0.125, 0, 'gdpr_block'),
(1479, '8.2.2', 'Is the registry of criminal convictions exclusively controlled by an official authority?', 0.125, 0, 'gdpr_block'),
(1480, '8.3', 'Are the objectives for collecting personal data clearly defined, explicit, and legitimate?', 0.25, 0, 'gdpr_block'),
(1481, '8.3.1', 'Is the acquired personal data strictly relevant and limited to what is essential for the intended purposes?', 0, -0.125, 'gdpr_block'),
(1482, '8.3.2', 'Is the personal data you gather accurate and regularly updated?', 0, -0.063, 'gdpr_block'),
(1483, '8.3.3', 'Is personal data stored in a way that allows for identification of subjects only for the duration needed for its intended use?', 0, -0.063, 'gdpr_block'),
(1484, '9', 'Do you employ a Data Protection Officer (DPO) in accordance with European Union or Member State legislation?', 0, -0.525, 'gdpr_block'),
(1485, '9.1', 'Is the DPO actively involved in all data protection matters?', 0, -0.225, 'gdpr_block'),
(1486, '9.1.1', 'Does the DPO have a direct reporting line to the highest level of management?', 0, -0.038, 'gdpr_block'),
(1487, '9.2', 'Is adequate resourcing provided for the DPO to execute their tasks?', 0, -0.075, 'gdpr_block'),
(1488, '9.3', 'Is the DPO free from instructions that could compromise the impartial exercise of their responsibilities?', 0, -0.113, 'gdpr_block'),
(1489, '9.4', 'Can data subjects directly communicate with the DPO regarding their personal data processing concerns?', 0, -0.113, 'gdpr_block'),
(1490, '10', 'Are there methods to authenticate the identity of a data subject requesting access?', 0, -0.375, 'gdpr_block'),
(1491, '10.1', 'Are the identity verification methods you employ both secure and reliable?', 0, -0.2, 'gdpr_block'),
(1492, '10.1.1', 'Do you employ pseudonymization techniques as part of the identity verification process?', 0, -0.05, 'gdpr_block'),
(1493, '10.1.2', 'Is personal data only retained for the purpose of responding to potential future requests?', -0.05, 0, 'gdpr_block'),
(1494, '11', 'Does the product support the \"right to be forgotten,\" allowing for the erasure of personal data?', 0.54, 0, 'gdpr_block'),
(1495, '11.1', 'Can a data subject request erasure under some specified conditions?', 0, -0.54, 'gdpr_block'),
(1496, '11.1.1', 'Can erasure be requested for data that is no longer necessary?', 0, -0.088, 'gdpr_block'),
(1497, '11.1.2', 'Is erasure possible when the data subject withdraws consent and there’s no other legal ground for processing?', 0, -0.088, 'gdpr_block'),
(1498, '11.1.3', 'Can erasure be requested if the data subject contests the processing and no overriding legitimate reasons exist?', 0, -0.088, 'gdpr_block'),
(1499, '11.1.4', 'Can erasure be executed when the personal data has been unlawfully processed?', 0, -0.088, 'gdpr_block'),
(1500, '11.1.5', 'Is erasure possible to comply with legal obligations?', 0, -0.088, 'gdpr_block'),
(1501, '11.1.6', 'Can erasure be requested for data gathered when the subject was a minor?', 0, -0.088, 'gdpr_block'),
(1502, '12', 'Is all data processing information transparent and easily accessible to data subjects?', 0, -0.25, 'gdpr_block'),
(1503, '12.1', 'Is data processing information also available in electronic formats?', 0, -0.15, 'gdpr_block'),
(1504, '12.1.1', 'Is data processing information articulated in clear language that is easily understandable?', 0, -0.05, 'gdpr_block'),
(1505, '12.1.2', 'Is the consent mechanism presented separately from other terms or conditions?', -0.05, 0, 'gdpr_block'),
(1506, '12.1.3', 'Is it possible for data subjects to revoke their consent at any time?', 0, -0.05, 'gdpr_block'),
(1507, '13', 'Does the product consider a minor\'s consent (below the age of 13-16)?', 0, -0.25, 'gdpr_block'),
(1508, '13.1', 'Is the processing of data for subjects under 13-16 years of age based on parental consent?', 0, -0.15, 'gdpr_block'),
(1509, '13.1.1', 'Are reasonable technological methods employed to confirm that parental consent is genuine?', 0, -0.05, 'gdpr_block'),
(1510, '13.1.2', 'Does the product provide clear and age-appropriate information to subjects under 13-16 years about the data being collected?', 0, -0.05, 'gdpr_block'),
(1511, '13.1.3', 'Is an option available for any minor to remove personal data?', 0, -0.05, 'gdpr_block'),
(1512, '14', 'Does the product process personal data that is not needed for identification?', -0.15, 0, 'gdpr_block'),
(1513, '14.1', 'If the processing objectives do not require identification, do you refrain from collecting additional identifying data?', 0.1, 0, 'gdpr_block'),
(1514, '14.1.1', 'Is the restriction of such non-identifiable data clearly marked within the product?', 0.05, 0, 'gdpr_block'),
(1515, '15', 'Does the product handle personal data?', -1, 0, 'led_block'),
(1516, '15.1', 'Does the product handle personal data only for a specific, explicit, and legitimate purpose?', 0.667, 0, 'led_block'),
(1517, '15.1.1', 'Are there measures in place to periodically review and remove unnecessary data?', 0, -0.333, 'led_block'),
(1518, '15.1.2', 'Can your product share personal data if the law requires it?', 0, -0.333, 'led_block'),
(1519, '15.2', 'Does your product process data related to a person\'s racial or ethnic background?', 0, 0.333, 'led_block'),
(1520, '15.2.1', 'Is there extra security for such sensitive data?', 0.333, 0, 'led_block'),
(1521, '16', 'Can you correct personal data in your product?', 0, -0.4, 'led_block'),
(1522, '16.1', 'Can you delete data in your product if it violates the Law Enforcement Directive (LED) regulations?', 0, -0.2, 'led_block'),
(1523, '16.1.1', 'Can you limit data usage while someone challenges its accuracy?', 0, -0.1, 'led_block'),
(1524, '16.1.2', 'Does your product keep data for legal evidence?', 0, -0.1, 'led_block'),
(1525, '17', 'Can users ask to verify the lawfulness of the data processing?', 0, -0.575, 'led_block'),
(1526, '17.1', 'Are users informed that they have the right to check if data processing is lawful?', 0.225, 0, 'led_block'),
(1527, '17.1.1', 'Can users go straight to regulatory authorities to question your product\'s data handling?', 0, -0.075, 'led_block'),
(1528, '17.1.2', 'Is there a mechanism to manage legality checks within your product?', 0, -0.075, 'led_block'),
(1529, '17.1.3', 'Does your product respond promptly to legality inquiries?', 0, -0.075, 'led_block'),
(1530, '17.1.3.1', 'Are users informed if a regulatory body intervenes on their behalf?', 0, -0.038, 'led_block'),
(1531, '17.1.3.2', 'If an affected person is denied access to their data, is the user provided a written explanation?', 0, -0.038, 'led_block'),
(1532, '17.2', 'Does your product meet all LED requirements within set deadlines?', 0, -0.18, 'led_block'),
(1533, '17.2.1', 'Is there a mention of LED in your product documentation or official release?', 0, -0.088, 'led_block'),
(1534, '17.2.2', 'If required by law, can your product utilize specific handling codes, like Europol\'s Integrated Data Management Concept, for data processing?', 0, -0.088, 'led_block'),
(1535, '17.3', 'Do you have a procedure for the cases in which a user\'s request for data access or correction is denied?', 0, -0.18, 'led_block'),
(1536, '17.3.1', 'If data access or correction is denied, are users informed they can seek a regulatory review?', 0, -0.088, 'led_block'),
(1537, '17.3.2', 'Are users informed by the regulatory body after all required checks have been done?', 0, -0.088, 'led_block'),
(1538, '18', 'Is the AI system considered high-risk as per relevant regulation in the European Union (AI Act)?', 0, 0, 'ai_block'),
(1539, '18.1', 'Does it comply with relevant requirements for high-risk systems in the AI Act or includes a complience plan for the upcoming regulation?', 0, 0, 'ai_block'),
(1540, '19', 'Is performance of the AI system evaluated and documented?', 0, -0.315, 'ai_block'),
(1541, '19.1', 'Is the AI system performance continuously evaluated during normal operation?', 0, -0.105, 'ai_block'),
(1542, '19.1.1', 'Is a description of the risk management system included in the technical documentation?', 0, -0.053, 'ai_block'),
(1543, '19.1.2', 'Does technical documentation include changes made to the system through its lifecycle?', 0, -0.053, 'ai_block'),
(1544, '19.2', 'Does technical documentation include information about energy consumption?', 0, -0.06, 'ai_block'),
(1545, '19.3', 'Does technical documentation address the monitoring, functioning, and control of the AI system?', 0, -0.15, 'ai_block'),
(1546, '20', 'Do users get sufficient information about the methods and capabilities of the AI system?', 0, -0.428, 'ai_block'),
(1547, '20.1', 'Does the AI system make users aware that they are communicating or interacting with the AI system?', 0, -0.158, 'ai_block'),
(1548, '20.2', 'Does the AI system inform users of its limitations?', 0, -0.158, 'ai_block'),
(1549, '20.3', 'Are affected persons informed about their rights?', 0, -0.113, 'ai_block'),
(1550, '21', 'Do decisions or outputs of the AI system influence or affect humans directly?', -0.518, 0, 'ai_block'),
(1551, '21.1', 'Did you establish detection and response mechanisms for undesirable effects, for example false negatives or false positives?', 0.158, 0, 'ai_block'),
(1552, '21.1.1', 'Is there a ‘stop button’ (if relevant) or a procedure for humans to safely abort operation of the AI system?', 0, -0.045, 'ai_block'),
(1553, '21.2', 'Can the AI system be controlled or overseen by humans during normal operation?', 0.203, 0, 'ai_block'),
(1554, '21.2.1', 'Was the AI system designed so as to be controlled or overseen by a human during operation?', -0.203, 0, 'ai_block'),
(1555, '21.2.1.1', 'Have you evaluated the efficacy of oversight measures during normal operation?', 0.203, 0, 'ai_block'),
(1556, '21.2.1.1.1', 'Were humans offered training on how to exercise control?', 0, -0.203, 'ai_block'),
(1557, '21.3', 'Have you implemented technical measures to facilitate explicability of the outputs?', 0.158, 0, 'ai_block'),
(1558, '21.3.1', 'Do these technical measures meet benchmarks and industry standards?', 0, -0.113, 'ai_block'),
(1559, '22', 'Can the AI system be attacked resulting in unintended or unexpected harm?', -0.603, 0, 'ai_block'),
(1560, '22.1', 'Is the training and application data stored securily with standard and robust authorisation and encryption requirements?', 0.171, 0, 'ai_block'),
(1561, '22.2', 'Is the AI system robust against AI-specific adversarial attacks?', 0.203, 0, 'ai_block'),
(1562, '22.3', 'Is the AI system resilient against model extraction and model replication attacks?', 0.171, 0, 'ai_block'),
(1563, '22.4', 'Does the AI system have a functionality to report incidents or breaches to relevant authorities?', 0.059, 0, 'ai_block'),
(1564, '23', 'Was there training to ensure sufficient AI literacy of the users?', 0, -0.041, 'ai_block'),
(1565, '23.1', 'Was the training specifically adapted and contextualized for the use case?', 0.023, 0, 'ai_block'),
(1566, '23.2', 'Does the training include basic concepts of machine learning and AI ethics?', 0.014, 0, 'ai_block'),
(1567, '23.4', 'Was the AI literacy of affected persons taken into account during the system\'s deployment?', 0.005, 0, 'ai_block');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1568;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
