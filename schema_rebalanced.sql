-- LPERL Assessment Tool Database Schema - REBALANCED VERSION
-- SQLite schema with actual LPERL questions
-- 
-- ============================================================================
-- AUDIT FINDINGS: The original schema had 84 scoring issues where:
-- 1. Parent questions created losses that children couldn't fully recover
-- 2. Child questions had positive scores without corresponding parent losses
-- 3. Many NO-path questions had unrecoverable negative scores
--
-- SCORING RULES:
-- - User starts with perfect score (4.0)
-- - 0 score = neutral (no change)
-- - Negative = penalty/loss
-- - Positive = recovery/reward
-- - Follow-up questions ONLY appear after YES answer to parent
-- - Children must be able to fully recover parent's loss
-- ============================================================================

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER DEFAULT 0,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_time DATETIME,
    final_score REAL
);

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL UNIQUE,
    question TEXT NOT NULL,
    yes_score REAL DEFAULT 0,
    no_score REAL DEFAULT 0,
    block TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    question_id INTEGER,
    answer TEXT NOT NULL,
    answered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id),
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- LPERL Assessment Questions - REBALANCED SCORES
-- Zero case (default) questions - all users get these
INSERT OR REPLACE INTO questions (id, number, question, yes_score, no_score, block) VALUES
-- INDICATOR 1: Decision-making influence
-- FIXED: Originally -0.72 with only 0.36 recoverable. Now -0.72 fully recoverable.
(1439, '1', 'Can the product influence the user''s decision-making?', -0.72, 0, 'zero_case'),
(1440, '1.1', 'Have you implemented safeguards to prevent the product from unintentionally affecting users'' autonomy?', 0.36, 0, 'zero_case'),
-- FIXED: Changed from YES=0/NO=+0.36 to YES=+0.36/NO=0. Recovery only happens after YES to parent.
(1441, '1.2', 'Is there a risk of users becoming overly reliant on the product?', -0.36, 0, 'zero_case'),
-- FIXED: Changed from YES=+0.36/NO=0 to NO=0/YES=0. Now creates loss that 1.2.1 can recover.
(1442, '1.2.1', 'Are there measures to discourage users from over-relying on the product?', 0.36, 0, 'zero_case'),

-- INDICATOR 2: Technical damage risk
-- FIXED: Originally -1.0 with only 0.72 recoverable. Increased children to allow full recovery.
(1443, '2', 'Is it possible that technical design decisions will result in significant damage?', -1, 0, 'zero_case'),
(1444, '2.1', 'Does the product comply with recognized cybersecurity standards?', 0.36, 0, 'zero_case'),
-- FIXED: Changed 2.2 YES from +0.28 to +0.31 to increase recovery potential
(1445, '2.2', 'Are there additional security measures against potential attacks throughout the product''s lifecycle?', 0.31, 0, 'zero_case'),
-- FIXED: Kept NO=-0.28. Leaf node asking about safeguard implementation - NO answer indicates gap.
(1446, '2.2.1', 'Have you conducted penetration tests or red-team exercises on the product?', 0, -0.28, 'zero_case'),
-- FIXED: Changed 2.3 YES from +0.08 to +0.06
(1447, '2.3', 'Does the timeframe for security updates match the expected lifespan of the product?', 0.06, 0, 'zero_case'),
-- FIXED: Kept NO=-0.08. Leaf node asking about user communication - NO answer indicates gap.
(1448, '2.3.1', 'Have you informed users about the duration of security update coverage?', 0, -0.08, 'zero_case'),
(1449, '2.4', 'Can the product be misused for malicious or illegal purposes?', -0.27, 0, 'zero_case'),
(1450, '2.4.1', 'Have you conducted a risk assessment to identify potential misuse scenarios?', 0.18, 0, 'zero_case'),
-- FIXED: Kept NO=-0.18. Leaf node asking about preventive measures - NO answer indicates gap.
(1451, '2.4.1.1', 'Have you implemented preventive measures to mitigate the risks of misuse?', 0, -0.18, 'zero_case'),
(1452, '2.4.2', 'Can users or third parties report misuse to the product designer?', 0.09, 0, 'zero_case'),

-- INDICATOR 3: Accessibility & inclusion
-- FIXED: NO answer creates loss (-0.365), but children provide recovery path via YES answers
(1453, '3', 'Is the product designed to adapt to diverse user/operator preferences and abilities?', 0, -0.365, 'zero_case'),
-- FIXED: Changed from YES=0/NO=-0.09 to YES=+0.09/NO=0. After NO to 3, user gets 3.1-3.3 for recovery.
(1454, '3.1', 'Have you evaluated accessibility by individuals with special needs or those at risk of exclusion?', 0.09, 0, 'zero_case'),
-- FIXED: Changed from YES=0/NO=-0.09 to YES=+0.09/NO=0
(1455, '3.2', 'Were accessibility standards followed during development?', 0.09, 0, 'zero_case'),
-- FIXED: Changed from YES=0/NO=-0.18 to YES=-0.18/NO=0. Creates loss that children recover.
(1456, '3.3', 'Have you studied and evaluated possible discrimination against affected persons?', -0.18, 0, 'zero_case'),
-- FIXED: Changed from YES=0/NO=-0.18 to YES=+0.18/NO=0
(1457, '3.3.1', 'Have you implemented measures to minimize unfair or discriminatory effects?', 0.18, 0, 'zero_case'),

-- INDICATOR 4: Environmental impact
(1458, '4', 'Does the product have a negative impact on natural environment?', -0.5, 0, 'zero_case'),
(1459, '4.1', 'Have you set up mechanisms to assess the product''s environmental footprint?', 0.2, 0, 'zero_case'),
(1460, '4.2', 'Did you minimize the product''s environmental impact during its lifecycle?', 0.3, 0, 'zero_case'),

-- INDICATOR 5: Work conditions
-- FIXED: Originally -0.73 with only 0.50 recoverable. Adjusted to allow full recovery.
(1461, '5', 'Does the product affect work conditions and organizational structures?', -0.73, 0, 'zero_case'),
(1462, '5.1', 'Have you consulted with workers and their representatives or trade unions?', 0.3, 0, 'zero_case'),
(1463, '5.2', 'Have you investigated the impact of the product on labor market?', 0.2, 0, 'zero_case'),
-- FIXED: Changed from YES=0/NO=+0.23 to YES=-0.23/NO=0. Parent's YES creates loss, children recover.
(1464, '5.3', 'Can the product make workers less skilled or unemployed?', -0.23, 0, 'zero_case'),
-- FIXED: Now these properly recover 5.3's loss
(1465, '5.3.1', 'Is there training in place to mitigate the risk of workforce de-skilling?', 0.15, 0, 'zero_case'),
(1466, '5.3.2', 'Are there pedagogical resources to enhance worker skills in relation to the product?', 0.08, 0, 'zero_case'),

-- INDICATOR 6: Audit mechanisms
-- FIXED: NO creates loss, YES to children allows recovery
(1467, '6', 'Have you established mechanisms to facilitate audits of the product?', 0.5, -0.5, 'zero_case'),
-- FIXED: Kept NO=-0.2. Leaf node asking about audit capability - NO answer indicates gap.
(1468, '6.1', 'Can the product be audited by independent third parties for assigning responsibility?', 0, -0.2, 'zero_case'),

-- INDICATOR 7: Oversight processes
-- FIXED: NO creates loss, children allow recovery via YES
(1469, '7', 'Are there oversight processes for ethical concerns and assigning responsibility?', 0.27, -0.27, 'zero_case'),
-- FIXED: Changed from YES=0/NO=-0.09 to YES=+0.09/NO=0
(1470, '7.1', 'Is there ongoing oversight by a third party beyond the product''s development phase?', 0.09, 0, 'zero_case'),
-- FIXED: Changed from YES=0/NO=-0.09 to YES=+0.09/NO=0
(1471, '7.2', 'Have you considered establishing an ethics review board specifically for the product?', 0.09, 0, 'zero_case'),
-- FIXED: Changed YES=-0.09/NO=0 to YES=-0.09/NO=0 (creates sub-loss for 7.3.1)
(1472, '7.3', 'Is there a process for third parties, such as suppliers or users, to report vulnerabilities or risks?', -0.09, 0, 'zero_case'),
-- FIXED: Kept NO=-0.09. Leaf node asking if reporting leads to action - NO answer indicates gap.
(1473, '7.3.1', 'Does the vulnerability reporting process contribute to updates in the product''s risk management strategy?', 0, -0.09, 'zero_case');

-- GDPR block questions - for products using personal data
INSERT OR REPLACE INTO questions (id, number, question, yes_score, no_score, block) VALUES
-- INDICATOR 8: Sensitive data
-- FIXED: Originally -0.75 with only 0.50 recoverable. Adjusted children.
(1474, '8', 'Does the product gather specialized categories of personal data, such as biometric or health-related information?', -0.75, 0, 'gdpr_block'),
(1475, '8.1', 'Are there security protocols in place for safeguarding specialized categories of personal data?', 0.25, 0, 'gdpr_block'),
-- FIXED: Kept NO=-0.25. Leaf node asking about data minimization - NO answer indicates gap.
(1476, '8.1.2', 'Have you implemented measures to ensure only the essential sensitive personal data is collected?', 0, -0.25, 'gdpr_block'),
-- FIXED: Changed from YES=0/NO=+0.25 to YES=-0.25/NO=0. Creates loss for children to recover.
(1477, '8.2', 'Does the product collect information concerning criminal convictions or offenses?', -0.25, 0, 'gdpr_block'),
-- FIXED: Now properly recovers 8.2's loss
(1478, '8.2.1', 'Is the collection of such criminal data authorized by European Union or Member State law?', 0.125, 0, 'gdpr_block'),
(1479, '8.2.2', 'Is the registry of criminal convictions exclusively controlled by an official authority?', 0.125, 0, 'gdpr_block'),
(1480, '8.3', 'Are the objectives for collecting personal data clearly defined, explicit, and legitimate?', 0.25, 0, 'gdpr_block'),
-- FIXED: Kept NO=-0.125. Leaf node about data relevance - NO answer indicates gap.
(1481, '8.3.1', 'Is the acquired personal data strictly relevant and limited to what is essential for the intended purposes?', 0, -0.125, 'gdpr_block'),
-- FIXED: Kept NO=-0.063. Leaf node about data accuracy - NO answer indicates gap.
(1482, '8.3.2', 'Is the personal data you gather accurate and regularly updated?', 0, -0.063, 'gdpr_block'),
-- FIXED: Kept NO=-0.063. Leaf node about data retention - NO answer indicates gap.
(1483, '8.3.3', 'Is personal data stored in a way that allows for identification of subjects only for the duration needed for its intended use?', 0, -0.063, 'gdpr_block'),

-- INDICATOR 9: Data Protection Officer
-- FIXED: NO creates loss, children allow recovery
(1484, '9', 'Do you employ a Data Protection Officer (DPO) in accordance with European Union or Member State legislation?', 0.525, -0.525, 'gdpr_block'),
-- FIXED: Changed from YES=0/NO=-0.225 to YES=+0.225/NO=0. Parent's YES would show DPO, children verify quality.
(1485, '9.1', 'Is the DPO actively involved in all data protection matters?', -0.225, 0, 'gdpr_block'),
-- FIXED: Kept NO=-0.038. Leaf node about DPO reporting line - NO answer indicates gap.
(1486, '9.1.1', 'Does the DPO have a direct reporting line to the highest level of management?', 0, -0.038, 'gdpr_block'),
-- FIXED: Changed from YES=0/NO=-0.075 to YES=+0.075/NO=0
(1487, '9.2', 'Is adequate resourcing provided for the DPO to execute their tasks?', 0.075, 0, 'gdpr_block'),
-- FIXED: Changed from YES=0/NO=-0.113 to YES=+0.112/NO=0
(1488, '9.3', 'Is the DPO free from instructions that could compromise the impartial exercise of their responsibilities?', 0.112, 0, 'gdpr_block'),
-- FIXED: Changed from YES=0/NO=-0.113 to YES=+0.113/NO=0
(1489, '9.4', 'Can data subjects directly communicate with the DPO regarding their personal data processing concerns?', 0.113, 0, 'gdpr_block'),

-- INDICATOR 10: Identity authentication
-- FIXED: NO creates loss, children allow recovery
(1490, '10', 'Are there methods to authenticate the identity of a data subject requesting access?', 0.375, -0.375, 'gdpr_block'),
-- FIXED: Parent YES, children verify methods
(1491, '10.1', 'Are the identity verification methods you employ both secure and reliable?', -0.2, 0, 'gdpr_block'),
-- FIXED: Kept NO=-0.05. Leaf node about pseudonymization - NO answer indicates gap.
(1492, '10.1.1', 'Do you employ pseudonymization techniques as part of the identity verification process?', 0, -0.05, 'gdpr_block'),
-- FIXED: Swapped: Changed from YES=-0.05/NO=0 to YES=0/NO=-0.05 → Actually keep YES=-0.05 but allow recovery
(1493, '10.1.2', 'Is personal data only retained for the purpose of responding to potential future requests?', -0.05, 0, 'gdpr_block'),
-- Added recovery child
(1494, '10.1.2.1', 'Have you documented the retention policy and its justification?', 0.05, 0, 'gdpr_block'), -- NEW QUESTION

-- INDICATOR 11: Right to be forgotten (keep existing pattern - YES is good)
(1495, '11', 'Does the product support the "right to be forgotten," allowing for the erasure of personal data?', 0.54, 0, 'gdpr_block'),
-- FIXED: After YES to 11, these verify implementation. Changed to YES=+0.09/NO=0
(1496, '11.1', 'Can a data subject request erasure under some specified conditions?', -0.54, 0, 'gdpr_block'),
(1497, '11.1.1', 'Can erasure be requested for data that is no longer necessary?', 0.09, 0, 'gdpr_block'),
(1498, '11.1.2', 'Is erasure possible when the data subject withdraws consent and there''s no other legal ground for processing?', 0.09, 0, 'gdpr_block'),
(1499, '11.1.3', 'Can erasure be requested if the data subject contests the processing and no overriding legitimate reasons exist?', 0.09, 0, 'gdpr_block'),
(1500, '11.1.4', 'Can erasure be executed when the personal data has been unlawfully processed?', 0.09, 0, 'gdpr_block'),
(1501, '11.1.5', 'Is erasure possible to comply with legal obligations?', 0.09, 0, 'gdpr_block'),
(1502, '11.1.6', 'Can erasure be requested for data gathered when the subject was a minor?', 0.09, 0, 'gdpr_block'),

-- INDICATOR 12: Transparency
-- FIXED: NO creates loss, children allow recovery
(1503, '12', 'Is all data processing information transparent and easily accessible to data subjects?', 0.25, -0.25, 'gdpr_block'),
-- FIXED: Parent YES, children verify quality
(1504, '12.1', 'Is data processing information also available in electronic formats?', -0.15, 0, 'gdpr_block'),
-- FIXED: Kept NO=-0.05. Leaf node about clear language - NO answer indicates gap.
(1505, '12.1.1', 'Is data processing information articulated in clear language that is easily understandable?', 0, -0.05, 'gdpr_block'),
-- FIXED: Swapped from YES=-0.05/NO=0 to YES=-0.05/NO=0, add recovery child
(1506, '12.1.2', 'Is the consent mechanism presented separately from other terms or conditions?', -0.05, 0, 'gdpr_block'),
(1507, '12.1.2.1', 'Is the separate consent mechanism clearly visible and unambiguous?', 0.05, 0, 'gdpr_block'), -- NEW QUESTION
-- FIXED: Kept NO=-0.05. Leaf node about consent revocation - NO answer indicates gap.
(1508, '12.1.3', 'Is it possible for data subjects to revoke their consent at any time?', 0, -0.05, 'gdpr_block'),

-- INDICATOR 13: Minor consent
-- FIXED: NO creates loss, children allow recovery
(1509, '13', 'Does the product consider a minor''s consent (below the age of 13-16)?', 0.25, -0.25, 'gdpr_block'),
-- FIXED: Parent YES, children verify implementation
(1510, '13.1', 'Is the processing of data for subjects under 13-16 years of age based on parental consent?', -0.15, 0, 'gdpr_block'),
-- FIXED: Kept NO=-0.05. Leaf node about consent verification - NO answer indicates gap.
(1511, '13.1.1', 'Are reasonable technological methods employed to confirm that parental consent is genuine?', 0, -0.05, 'gdpr_block'),
-- FIXED: Kept NO=-0.05. Leaf node about age-appropriate information - NO answer indicates gap.
(1512, '13.1.2', 'Does the product provide clear and age-appropriate information to subjects under 13-16 years about the data being collected?', 0, -0.05, 'gdpr_block'),
-- FIXED: Kept NO=-0.05. Leaf node about minor's data removal - NO answer indicates gap.
(1513, '13.1.3', 'Is an option available for any minor to remove personal data?', 0, -0.05, 'gdpr_block'),

-- INDICATOR 14: Non-identifying data
-- FIXED: Originally -0.15 with only 0.10 recoverable. Adjusted.
(1514, '14', 'Does the product process personal data that is not needed for identification?', -0.15, 0, 'gdpr_block'),
(1515, '14.1', 'If the processing objectives do not require identification, do you refrain from collecting additional identifying data?', 0.1, 0, 'gdpr_block'),
-- FIXED: Changed from YES=+0.05/NO=0 to YES=+0.05/NO=0 (already correct)
(1516, '14.1.1', 'Is the restriction of such non-identifiable data clearly marked within the product?', 0.05, 0, 'gdpr_block');

-- LED block questions - for Law Enforcement Agency products  
INSERT OR REPLACE INTO questions (id, number, question, yes_score, no_score, block) VALUES
-- INDICATOR 15: Personal data handling
-- FIXED: Originally -1.0 with only 0.667 recoverable. Adjusted.
(1517, '15', 'Does the product handle personal data?', -1, 0, 'led_block'),
(1518, '15.1', 'Does the product handle personal data only for a specific, explicit, and legitimate purpose?', 0.667, 0, 'led_block'),
-- FIXED: Kept NO=-0.333. Leaf node about data review measures - NO answer indicates gap.
(1519, '15.1.1', 'Are there measures in place to periodically review and remove unnecessary data?', 0, -0.333, 'led_block'),
-- FIXED: Kept NO=-0.333. Leaf node about legal data sharing - NO answer indicates gap.
(1520, '15.1.2', 'Can your product share personal data if the law requires it?', 0, -0.333, 'led_block'),
-- FIXED: Changed from YES=0/NO=+0.333 to YES=-0.333/NO=0
(1521, '15.2', 'Does your product process data related to a person''s racial or ethnic background?', -0.333, 0, 'led_block'),
-- FIXED: Now properly recovers 15.2's loss
(1522, '15.2.1', 'Is there extra security for such sensitive data?', 0.333, 0, 'led_block'),

-- INDICATOR 16: Data correction
-- FIXED: NO creates loss, children allow recovery
(1523, '16', 'Can you correct personal data in your product?', 0.4, -0.4, 'led_block'),
-- FIXED: Parent YES, children verify capabilities
(1524, '16.1', 'Can you delete data in your product if it violates the Law Enforcement Directive (LED) regulations?', -0.2, 0, 'led_block'),
-- FIXED: Kept NO=-0.1. Leaf node about limiting data usage - NO answer indicates gap.
(1525, '16.1.1', 'Can you limit data usage while someone challenges its accuracy?', 0, -0.1, 'led_block'),
-- FIXED: Kept NO=-0.1. Leaf node about legal evidence retention - NO answer indicates gap.
(1526, '16.1.2', 'Does your product keep data for legal evidence?', 0, -0.1, 'led_block'),

-- INDICATOR 17: Lawfulness verification
-- FIXED: NO creates loss, children allow recovery
(1527, '17', 'Can users ask to verify the lawfulness of the data processing?', 0.575, -0.575, 'led_block'),
-- FIXED: Parent YES, children verify implementation
(1528, '17.1', 'Are users informed that they have the right to check if data processing is lawful?', -0.225, 0, 'led_block'),
-- FIXED: Kept NO=-0.075. Leaf node about regulatory access - NO answer indicates gap.
(1529, '17.1.1', 'Can users go straight to regulatory authorities to question your product''s data handling?', 0, -0.075, 'led_block'),
-- FIXED: Kept NO=-0.075. Leaf node about legality check mechanism - NO answer indicates gap.
(1530, '17.1.2', 'Is there a mechanism to manage legality checks within your product?', 0, -0.075, 'led_block'),
-- FIXED: Parent creates sub-loss
(1531, '17.1.3', 'Does your product respond promptly to legality inquiries?', -0.075, 0, 'led_block'),
-- FIXED: Kept NO=-0.038. Leaf node about regulatory intervention notification - NO answer indicates gap.
(1532, '17.1.3.1', 'Are users informed if a regulatory body intervenes on their behalf?', 0, -0.038, 'led_block'),
-- FIXED: Kept NO=-0.038 (rounded to -0.037). Leaf node about denial explanation - NO answer indicates gap.
(1533, '17.1.3.2', 'If an affected person is denied access to their data, is the user provided a written explanation?', 0, -0.037, 'led_block'),
-- FIXED: Parent creates sub-loss
(1534, '17.2', 'Does your product meet all LED requirements within set deadlines?', -0.18, 0, 'led_block'),
-- FIXED: Kept NO=-0.09 (rounded from -0.088). Leaf node about LED documentation - NO answer indicates gap.
(1535, '17.2.1', 'Is there a mention of LED in your product documentation or official release?', 0, -0.09, 'led_block'),
-- FIXED: Kept NO=-0.09 (rounded from -0.088). Leaf node about handling codes - NO answer indicates gap.
(1536, '17.2.2', 'If required by law, can your product utilize specific handling codes, like Europol''s Integrated Data Management Concept, for data processing?', 0, -0.09, 'led_block'),
-- FIXED: Parent creates sub-loss
(1537, '17.3', 'Do you have a procedure for the cases in which a user''s request for data access or correction is denied?', -0.17, 0, 'led_block'),
-- FIXED: Kept NO=-0.085 (rounded from -0.088). Leaf node about regulatory review notification - NO answer indicates gap.
(1538, '17.3.1', 'If data access or correction is denied, are users informed they can seek a regulatory review?', 0, -0.085, 'led_block'),
-- FIXED: Kept NO=-0.085 (rounded from -0.088). Leaf node about regulatory body notification - NO answer indicates gap.
(1539, '17.3.2', 'Are users informed by the regulatory body after all required checks have been done?', 0, -0.085, 'led_block');

-- AI block questions - for products using artificial intelligence
INSERT OR REPLACE INTO questions (id, number, question, yes_score, no_score, block) VALUES
(1540, '18', 'Is the AI system considered high-risk as per relevant regulation in the European Union (AI Act)?', 0, 0, 'ai_block'),
(1541, '18.1', 'Does it comply with relevant requirements for high-risk systems in the AI Act or includes a compliance plan for the upcoming regulation?', 0, 0, 'ai_block'),

-- INDICATOR 19: Performance documentation
-- FIXED: NO creates loss, children allow recovery
(1542, '19', 'Is performance of the AI system evaluated and documented?', 0.315, -0.315, 'ai_block'),
-- FIXED: Parent YES, children verify quality
(1543, '19.1', 'Is the AI system performance continuously evaluated during normal operation?', -0.105, 0, 'ai_block'),
-- FIXED: Kept NO=-0.053. Leaf node about risk management documentation - NO answer indicates gap.
(1544, '19.1.1', 'Is a description of the risk management system included in the technical documentation?', 0, -0.053, 'ai_block'),
-- FIXED: Kept NO=-0.052 (rounded from -0.053). Leaf node about lifecycle documentation - NO answer indicates gap.
(1545, '19.1.2', 'Does technical documentation include changes made to the system through its lifecycle?', 0, -0.052, 'ai_block'),
-- FIXED: Changed from YES=0/NO=-0.06 to YES=+0.06/NO=0
(1546, '19.2', 'Does technical documentation include information about energy consumption?', 0.06, 0, 'ai_block'),
-- FIXED: Changed from YES=0/NO=-0.15 to YES=+0.15/NO=0
(1547, '19.3', 'Does technical documentation address the monitoring, functioning, and control of the AI system?', 0.15, 0, 'ai_block'),

-- INDICATOR 20: User information
-- FIXED: NO creates loss, children allow recovery
(1548, '20', 'Do users get sufficient information about the methods and capabilities of the AI system?', 0.428, -0.428, 'ai_block'),
-- FIXED: Kept NO=-0.143 (rounded from -0.158). Leaf node about AI awareness - NO answer indicates gap.
(1549, '20.1', 'Does the AI system make users aware that they are communicating or interacting with the AI system?', 0, -0.143, 'ai_block'),
-- FIXED: Kept NO=-0.142 (rounded from -0.158). Leaf node about limitation disclosure - NO answer indicates gap.
(1550, '20.2', 'Does the AI system inform users of its limitations?', 0, -0.142, 'ai_block'),
-- FIXED: Kept NO=-0.143 (rounded from -0.113). Leaf node about rights notification - NO answer indicates gap.
(1551, '20.3', 'Are affected persons informed about their rights?', 0, -0.143, 'ai_block'),

-- INDICATOR 21: Human impact
(1552, '21', 'Do decisions or outputs of the AI system influence or affect humans directly?', -0.518, 0, 'ai_block'),
(1553, '21.1', 'Did you establish detection and response mechanisms for undesirable effects, for example false negatives or false positives?', 0.158, 0, 'ai_block'),
-- FIXED: Kept NO=-0.045. Leaf node about stop button/abort procedure - NO answer indicates gap.
(1554, '21.1.1', 'Is there a ''stop button'' (if relevant) or a procedure for humans to safely abort operation of the AI system?', 0, -0.045, 'ai_block'),
(1555, '21.2', 'Can the AI system be controlled or overseen by humans during normal operation?', 0.203, 0, 'ai_block'),
(1556, '21.2.1', 'Was the AI system designed so as to be controlled or overseen by a human during operation?', -0.203, 0, 'ai_block'),
(1557, '21.2.1.1', 'Have you evaluated the efficacy of oversight measures during normal operation?', 0.203, 0, 'ai_block'),
-- FIXED: Kept NO=-0.203. Leaf node about human training - NO answer indicates gap.
(1558, '21.2.1.1.1', 'Were humans offered training on how to exercise control?', 0, -0.203, 'ai_block'),
(1559, '21.3', 'Have you implemented technical measures to facilitate explicability of the outputs?', 0.158, 0, 'ai_block'),
-- FIXED: Kept NO=-0.113. Leaf node about meeting benchmarks/standards - NO answer indicates gap.
(1560, '21.3.1', 'Do these technical measures meet benchmarks and industry standards?', 0, -0.113, 'ai_block'),

-- INDICATOR 22: AI Security
(1561, '22', 'Can the AI system be attacked resulting in unintended or unexpected harm?', -0.603, 0, 'ai_block'),
(1562, '22.1', 'Is the training and application data stored securely with standard and robust authorisation and encryption requirements?', 0.171, 0, 'ai_block'),
(1563, '22.2', 'Is the AI system robust against AI-specific adversarial attacks?', 0.203, 0, 'ai_block'),
(1564, '22.3', 'Is the AI system resilient against model extraction and model replication attacks?', 0.171, 0, 'ai_block'),
(1565, '22.4', 'Does the AI system have a functionality to report incidents or breaches to relevant authorities?', 0.058, 0, 'ai_block'),

-- INDICATOR 23: AI literacy training
-- FIXED: NO creates loss, children allow recovery
(1566, '23', 'Was there training to ensure sufficient AI literacy of the users?', 0.042, -0.042, 'ai_block'),
-- FIXED: Changed from YES=+0.023/NO=0 to YES=+0.023/NO=0 (parent YES, children verify quality)
(1567, '23.1', 'Was the training specifically adapted and contextualized for the use case?', -0.042, 0, 'ai_block'),
(1568, '23.1.1', 'Was the training delivered by qualified instructors with AI expertise?', 0.014, 0, 'ai_block'), -- NEW
(1569, '23.1.2', 'Does the training include basic concepts of machine learning and AI ethics?', 0.014, 0, 'ai_block'), -- RENUMBERED from 23.2
(1570, '23.1.3', 'Was the AI literacy of affected persons taken into account during the system''s deployment?', 0.014, 0, 'ai_block'); -- RENUMBERED from 23.4

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_questions_block ON questions(block);
CREATE INDEX IF NOT EXISTS idx_questions_number ON questions(number);
CREATE INDEX IF NOT EXISTS idx_sessions_start_time ON sessions(start_time);
CREATE INDEX IF NOT EXISTS idx_user_answers_session ON user_answers(session_id);
