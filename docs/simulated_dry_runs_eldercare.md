# ElderCare Chatbot: 3 Simulated Dry Runs

All runs use: `product_for_LEAs=no`, `uses_personal_data=yes`, `uses_AI=yes`.

| Run | Questions answered | Final score | API final_level | Message |
|---|---:|---:|---|---|
| TRL2 | 51 | -5.4 | LPERL -5 | LPERL 0 – Ethical, Legal, and Privacy considerations lacking. You should start by identifying ethical issues related to your project. |
| TRL6 | 100 | 1.95 | LPERL 1 | LPERL 2 – Characterized Ethical and Privacy Interactions. You have identified and characterized ethical issues relevant to your project. Now you should work on integrating them into a coherent ethical design. |
| TRL8 | 87 | 3.5 | LPERL 3 | LPERL 4 - Control Over Ethical, Legal, and Privacy Issues. Your project has sufficient working control mechanisms in place to manage its ethical and privacy considerations and ensure accountability and demonstrates ethical maturity. |

## TRL2 Waterfall

| Step | Indicator | Answer | Delta | Before | After | Question |
|---:|---|---|---:|---:|---:|---|
| 1 | `1` | YES | -0.720 | 4.000 | 3.280 | Can the product influence the user's decision-making? |
| 2 | `1.1` | NO | +0.000 | 3.280 | 3.280 | Have you implemented safeguards to prevent the product from unintentionally affecting users' autonomy? |
| 3 | `1.2` | YES | +0.000 | 3.280 | 3.280 | Is there a risk of users becoming overly reliant on the product? |
| 4 | `1.2.1` | NO | +0.000 | 3.280 | 3.280 | Are there measures to discourage users from over-relying on the product? |
| 5 | `2` | YES | -1.000 | 3.280 | 2.280 | Is it possible that technical design decisions will result in significant damage? |
| 6 | `2.1` | NO | +0.000 | 2.280 | 2.280 | Does the product comply with recognized cybersecurity standards? |
| 7 | `2.2` | NO | +0.000 | 2.280 | 2.280 | Are there additional security measures against potential attacks throughout the product's lifecycle? |
| 8 | `2.3` | YES | +0.080 | 2.280 | 2.360 | Does the timeframe for security updates match the expected lifespan of the product? |
| 9 | `2.3.1` | NO | -0.080 | 2.360 | 2.280 | Have you informed users about the duration of security update coverage? |
| 10 | `2.4` | YES | -0.270 | 2.280 | 2.010 | Can the product be misused for malicious or illegal purposes? |
| 11 | `2.4.1` | NO | +0.000 | 2.010 | 2.010 | Have you conducted a risk assessment to identify potential misuse scenarios? |
| 12 | `2.4.2` | NO | +0.000 | 2.010 | 2.010 | Can users or third parties report misuse to the product designer? |
| 13 | `3` | NO | -0.365 | 2.010 | 1.645 | Is the product designed to adapt to diverse user/operator preferences and abilities? |
| 14 | `4` | YES | -0.500 | 1.645 | 1.145 | Does the product have a negative impact on natural environment? |
| 15 | `4.1` | NO | +0.000 | 1.145 | 1.145 | Have you set up mechanisms to assess the product's environmental footprint? |
| 16 | `4.2` | NO | +0.000 | 1.145 | 1.145 | Did you minimize the product's environmental impact during its lifecycle? |
| 17 | `5` | YES | -0.730 | 1.145 | 0.415 | Does the product affect work conditions and organizational structures? |
| 18 | `5.1` | NO | +0.000 | 0.415 | 0.415 | Have you consulted with workers and their representatives or trade unions? |
| 19 | `5.2` | NO | +0.000 | 0.415 | 0.415 | Have you investigated the impact of the product on labor market? |
| 20 | `5.3` | YES | -0.230 | 0.415 | 0.185 | Can the product make workers less skilled or unemployed? |
| 21 | `5.3.1` | NO | +0.000 | 0.185 | 0.185 | Is there training in place to mitigate the risk of workforce de-skilling? |
| 22 | `5.3.2` | NO | +0.000 | 0.185 | 0.185 | Are there pedagogical resources to enhance worker skills in relation to the product? |
| 23 | `6` | NO | -0.500 | 0.185 | -0.315 | Have you established mechanisms to facilitate audits of the product? |
| 24 | `7` | NO | -0.270 | -0.315 | -0.585 | Are there oversight processes for ethical concerns and assigning responsibility? |
| 25 | `8` | YES | -0.750 | -0.585 | -1.335 | Does the product gather specialized categories of personal data, such as biometric or health-related information? |
| 26 | `8.1` | NO | +0.000 | -1.335 | -1.335 | Are there security protocols in place for safeguarding specialized categories of personal data? |
| 27 | `8.2` | YES | -0.250 | -1.335 | -1.585 | Does the product collect information concerning criminal convictions or offenses? |
| 28 | `8.2.1` | NO | +0.000 | -1.585 | -1.585 | Is the collection of such criminal data authorized by European Union or Member State law? |
| 29 | `8.2.2` | NO | +0.000 | -1.585 | -1.585 | Is the registry of criminal convictions exclusively controlled by an official authority? |
| 30 | `8.3` | NO | +0.000 | -1.585 | -1.585 | Are the objectives for collecting personal data clearly defined, explicit, and legitimate? |
| 31 | `9` | NO | -0.525 | -1.585 | -2.110 | Do you employ a Data Protection Officer (DPO) in accordance with European Union or Member State legislation? |
| 32 | `10` | NO | -0.375 | -2.110 | -2.485 | Are there methods to authenticate the identity of a data subject requesting access? |
| 33 | `11` | NO | -0.540 | -2.485 | -3.025 | Does the product support the "right to be forgotten," allowing for the erasure of personal data? |
| 34 | `12` | NO | -0.250 | -3.025 | -3.275 | Is all data processing information transparent and easily accessible to data subjects? |
| 35 | `13` | NO | -0.250 | -3.275 | -3.525 | Does the product consider a minor's consent (below the age of 13-16)? |
| 36 | `14` | YES | -0.150 | -3.525 | -3.675 | Does the product process personal data that is not needed for identification? |
| 37 | `14.1` | NO | +0.000 | -3.675 | -3.675 | If the processing objectives do not require identification, do you refrain from collecting additional identifying data? |
| 38 | `18` | YES | +0.000 | -3.675 | -3.675 | Is the AI system considered high-risk as per relevant regulation in the European Union (AI Act)? |
| 39 | `18.1` | NO | +0.000 | -3.675 | -3.675 | Does it comply with relevant requirements for high-risk systems in the AI Act or includes a compliance plan for the upcoming regulation? |
| 40 | `19` | NO | -0.315 | -3.675 | -3.990 | Is performance of the AI system evaluated and documented? |
| 41 | `20` | NO | -0.250 | -3.990 | -4.240 | Do users get sufficient information about the methods and capabilities of the AI system? |
| 42 | `21` | YES | -0.518 | -4.240 | -4.758 | Do decisions or outputs of the AI system influence or affect humans directly? |
| 43 | `21.1` | NO | +0.000 | -4.758 | -4.758 | Did you establish detection and response mechanisms for undesirable effects, for example false negatives or false positives? |
| 44 | `21.2` | NO | +0.000 | -4.758 | -4.758 | Can the AI system be controlled or overseen by humans during normal operation? |
| 45 | `21.3` | NO | +0.000 | -4.758 | -4.758 | Have you implemented technical measures to facilitate explicability of the outputs? |
| 46 | `22` | YES | -0.603 | -4.758 | -5.361 | Can the AI system be attacked resulting in unintended or unexpected harm? |
| 47 | `22.1` | NO | +0.000 | -5.361 | -5.361 | Is the training and application data stored securely with standard and robust authorisation and encryption requirements? |
| 48 | `22.2` | NO | +0.000 | -5.361 | -5.361 | Is the AI system robust against AI-specific adversarial attacks? |
| 49 | `22.3` | NO | +0.000 | -5.361 | -5.361 | Is the AI system resilient against model extraction and model replication attacks? |
| 50 | `22.4` | NO | +0.000 | -5.361 | -5.361 | Does the AI system have a functionality to report incidents or breaches to relevant authorities? |
| 51 | `23` | NO | -0.041 | -5.361 | -5.402 | Was there training to ensure sufficient AI literacy of the users? |

## TRL6 Waterfall

| Step | Indicator | Answer | Delta | Before | After | Question |
|---:|---|---|---:|---:|---:|---|
| 1 | `1` | YES | -0.720 | 4.000 | 3.280 | Can the product influence the user's decision-making? |
| 2 | `1.1` | YES | +0.360 | 3.280 | 3.640 | Have you implemented safeguards to prevent the product from unintentionally affecting users' autonomy? |
| 3 | `1.2` | YES | +0.000 | 3.640 | 3.640 | Is there a risk of users becoming overly reliant on the product? |
| 4 | `1.2.1` | YES | +0.360 | 3.640 | 4.000 | Are there measures to discourage users from over-relying on the product? |
| 5 | `2` | YES | -1.000 | 4.000 | 3.000 | Is it possible that technical design decisions will result in significant damage? |
| 6 | `2.1` | YES | +0.360 | 3.000 | 3.360 | Does the product comply with recognized cybersecurity standards? |
| 7 | `2.2` | YES | +0.310 | 3.360 | 3.670 | Are there additional security measures against potential attacks throughout the product's lifecycle? |
| 8 | `2.2.1` | NO | -0.280 | 3.670 | 3.390 | Have you conducted penetration tests or red-team exercises on the product? |
| 9 | `2.3` | YES | +0.080 | 3.390 | 3.470 | Does the timeframe for security updates match the expected lifespan of the product? |
| 10 | `2.3.1` | YES | +0.000 | 3.470 | 3.470 | Have you informed users about the duration of security update coverage? |
| 11 | `2.4` | YES | -0.270 | 3.470 | 3.200 | Can the product be misused for malicious or illegal purposes? |
| 12 | `2.4.1` | YES | +0.180 | 3.200 | 3.380 | Have you conducted a risk assessment to identify potential misuse scenarios? |
| 13 | `2.4.1.1` | YES | +0.000 | 3.380 | 3.380 | Have you implemented preventive measures to mitigate the risks of misuse? |
| 14 | `2.4.2` | YES | +0.090 | 3.380 | 3.470 | Can users or third parties report misuse to the product designer? |
| 15 | `3` | YES | +0.000 | 3.470 | 3.470 | Is the product designed to adapt to diverse user/operator preferences and abilities? |
| 16 | `3.1` | YES | +0.000 | 3.470 | 3.470 | Have you evaluated accessibility by individuals with special needs or those at risk of exclusion? |
| 17 | `3.2` | NO | -0.090 | 3.470 | 3.380 | Were accessibility standards followed during development? |
| 18 | `3.3` | YES | +0.000 | 3.380 | 3.380 | Have you studied and evaluated possible discrimination against affected persons? |
| 19 | `3.3.1` | YES | +0.000 | 3.380 | 3.380 | Have you implemented measures to minimize unfair or discriminatory effects? |
| 20 | `4` | NO | +0.000 | 3.380 | 3.380 | Does the product have a negative impact on natural environment? |
| 21 | `5` | YES | -0.730 | 3.380 | 2.650 | Does the product affect work conditions and organizational structures? |
| 22 | `5.1` | YES | +0.300 | 2.650 | 2.950 | Have you consulted with workers and their representatives or trade unions? |
| 23 | `5.2` | YES | +0.200 | 2.950 | 3.150 | Have you investigated the impact of the product on labor market? |
| 24 | `5.3` | YES | -0.230 | 3.150 | 2.920 | Can the product make workers less skilled or unemployed? |
| 25 | `5.3.1` | YES | +0.150 | 2.920 | 3.070 | Is there training in place to mitigate the risk of workforce de-skilling? |
| 26 | `5.3.2` | NO | +0.000 | 3.070 | 3.070 | Are there pedagogical resources to enhance worker skills in relation to the product? |
| 27 | `6` | YES | +0.000 | 3.070 | 3.070 | Have you established mechanisms to facilitate audits of the product? |
| 28 | `6.1` | YES | +0.000 | 3.070 | 3.070 | Can the product be audited by independent third parties for assigning responsibility? |
| 29 | `7` | YES | +0.000 | 3.070 | 3.070 | Are there oversight processes for ethical concerns and assigning responsibility? |
| 30 | `7.1` | YES | +0.000 | 3.070 | 3.070 | Is there ongoing oversight by a third party beyond the product's development phase? |
| 31 | `7.2` | NO | -0.090 | 3.070 | 2.980 | Have you considered establishing an ethics review board specifically for the product? |
| 32 | `7.3` | YES | +0.000 | 2.980 | 2.980 | Is there a process for third parties, such as suppliers or users, to report vulnerabilities or risks? |
| 33 | `7.3.1` | NO | -0.090 | 2.980 | 2.890 | Does the vulnerability reporting process contribute to updates in the product's risk management strategy? |
| 34 | `8` | YES | -0.750 | 2.890 | 2.140 | Does the product gather specialized categories of personal data, such as biometric or health-related information? |
| 35 | `8.1` | YES | +0.250 | 2.140 | 2.390 | Are there security protocols in place for safeguarding specialized categories of personal data? |
| 36 | `8.2` | NO | +0.000 | 2.390 | 2.390 | Does the product collect information concerning criminal convictions or offenses? |
| 37 | `8.3` | YES | +0.250 | 2.390 | 2.640 | Are the objectives for collecting personal data clearly defined, explicit, and legitimate? |
| 38 | `8.3.1` | YES | +0.000 | 2.640 | 2.640 | Is the acquired personal data strictly relevant and limited to what is essential for the intended purposes? |
| 39 | `8.3.2` | YES | +0.000 | 2.640 | 2.640 | Is the personal data you gather accurate and regularly updated? |
| 40 | `8.3.3` | NO | -0.063 | 2.640 | 2.577 | Is personal data stored in a way that allows for identification of subjects only for the duration needed for its intended use? |
| 41 | `9` | YES | +0.000 | 2.577 | 2.577 | Do you employ a Data Protection Officer (DPO) in accordance with European Union or Member State legislation? |
| 42 | `9.1` | YES | +0.000 | 2.577 | 2.577 | Is the DPO actively involved in all data protection matters? |
| 43 | `9.1.1` | YES | +0.000 | 2.577 | 2.577 | Does the DPO have a direct reporting line to the highest level of management? |
| 44 | `9.2` | NO | -0.075 | 2.577 | 2.502 | Is adequate resourcing provided for the DPO to execute their tasks? |
| 45 | `9.3` | YES | +0.000 | 2.502 | 2.502 | Is the DPO free from instructions that could compromise the impartial exercise of their responsibilities? |
| 46 | `9.4` | NO | -0.113 | 2.502 | 2.389 | Can data subjects directly communicate with the DPO regarding their personal data processing concerns? |
| 47 | `10` | YES | +0.000 | 2.389 | 2.389 | Are there methods to authenticate the identity of a data subject requesting access? |
| 48 | `10.1` | YES | +0.000 | 2.389 | 2.389 | Are the identity verification methods you employ both secure and reliable? |
| 49 | `10.1.1` | YES | +0.000 | 2.389 | 2.389 | Do you employ pseudonymization techniques as part of the identity verification process? |
| 50 | `10.1.2` | YES | +0.000 | 2.389 | 2.389 | Is personal data only retained for the purpose of responding to potential future requests? |
| 51 | `11` | YES | +0.000 | 2.389 | 2.389 | Does the product support the "right to be forgotten," allowing for the erasure of personal data? |
| 52 | `11.1` | YES | +0.000 | 2.389 | 2.389 | Can a data subject request erasure under some specified conditions? |
| 53 | `11.1.1` | YES | +0.000 | 2.389 | 2.389 | Can erasure be requested for data that is no longer necessary? |
| 54 | `11.1.2` | YES | +0.000 | 2.389 | 2.389 | Is erasure possible when the data subject withdraws consent and there's no other legal ground for processing? |
| 55 | `11.1.3` | YES | +0.000 | 2.389 | 2.389 | Can erasure be requested if the data subject contests the processing and no overriding legitimate reasons exist? |
| 56 | `11.1.4` | YES | +0.000 | 2.389 | 2.389 | Can erasure be executed when the personal data has been unlawfully processed? |
| 57 | `11.1.5` | NO | -0.088 | 2.389 | 2.301 | Is erasure possible to comply with legal obligations? |
| 58 | `11.1.6` | NO | -0.088 | 2.301 | 2.213 | Can erasure be requested for data gathered when the subject was a minor? |
| 59 | `12` | YES | +0.000 | 2.213 | 2.213 | Is all data processing information transparent and easily accessible to data subjects? |
| 60 | `12.1` | YES | +0.000 | 2.213 | 2.213 | Is data processing information also available in electronic formats? |
| 61 | `12.1.1` | YES | +0.000 | 2.213 | 2.213 | Is data processing information articulated in clear language that is easily understandable? |
| 62 | `12.1.2` | YES | +0.000 | 2.213 | 2.213 | Is the consent mechanism presented separately from other terms or conditions? |
| 63 | `12.1.3` | YES | +0.000 | 2.213 | 2.213 | Is it possible for data subjects to revoke their consent at any time? |
| 64 | `13` | YES | +0.000 | 2.213 | 2.213 | Does the product consider a minor's consent (below the age of 13-16)? |
| 65 | `13.1` | YES | +0.000 | 2.213 | 2.213 | Is the processing of data for subjects under 13-16 years of age based on parental consent? |
| 66 | `13.1.1` | YES | +0.000 | 2.213 | 2.213 | Are reasonable technological methods employed to confirm that parental consent is genuine? |
| 67 | `13.1.2` | YES | +0.000 | 2.213 | 2.213 | Does the product provide clear and age-appropriate information to subjects under 13-16 years about the data being collected? |
| 68 | `13.1.3` | YES | +0.000 | 2.213 | 2.213 | Is an option available for any minor to remove personal data? |
| 69 | `14` | YES | -0.150 | 2.213 | 2.063 | Does the product process personal data that is not needed for identification? |
| 70 | `14.1` | YES | +0.100 | 2.063 | 2.163 | If the processing objectives do not require identification, do you refrain from collecting additional identifying data? |
| 71 | `14.1.1` | YES | +0.050 | 2.163 | 2.213 | Is the restriction of such non-identifiable data clearly marked within the product? |
| 72 | `18` | YES | +0.000 | 2.213 | 2.213 | Is the AI system considered high-risk as per relevant regulation in the European Union (AI Act)? |
| 73 | `18.1` | YES | +0.000 | 2.213 | 2.213 | Does it comply with relevant requirements for high-risk systems in the AI Act or includes a compliance plan for the upcoming regulation? |
| 74 | `19` | YES | +0.000 | 2.213 | 2.213 | Is performance of the AI system evaluated and documented? |
| 75 | `19.1` | YES | +0.000 | 2.213 | 2.213 | Is the AI system performance continuously evaluated during normal operation? |
| 76 | `19.1.1` | YES | +0.000 | 2.213 | 2.213 | Is a description of the risk management system included in the technical documentation? |
| 77 | `19.1.2` | YES | +0.000 | 2.213 | 2.213 | Does technical documentation include changes made to the system through its lifecycle? |
| 78 | `19.2` | NO | -0.060 | 2.213 | 2.153 | Does technical documentation include information about energy consumption? |
| 79 | `19.3` | YES | +0.000 | 2.153 | 2.153 | Does technical documentation address the monitoring, functioning, and control of the AI system? |
| 80 | `20` | YES | +0.000 | 2.153 | 2.153 | Do users get sufficient information about the methods and capabilities of the AI system? |
| 81 | `20.1` | YES | +0.000 | 2.153 | 2.153 | Does the AI system make users aware that they are communicating or interacting with the AI system? |
| 82 | `20.2` | YES | +0.000 | 2.153 | 2.153 | Does the AI system inform users of its limitations? |
| 83 | `20.3` | YES | +0.000 | 2.153 | 2.153 | Are affected persons informed about their rights? |
| 84 | `21` | YES | -0.518 | 2.153 | 1.635 | Do decisions or outputs of the AI system influence or affect humans directly? |
| 85 | `21.1` | YES | +0.158 | 1.635 | 1.793 | Did you establish detection and response mechanisms for undesirable effects, for example false negatives or false positives? |
| 86 | `21.1.1` | YES | +0.000 | 1.793 | 1.793 | Is there a 'stop button' (if relevant) or a procedure for humans to safely abort operation of the AI system? |
| 87 | `21.2` | YES | +0.203 | 1.793 | 1.996 | Can the AI system be controlled or overseen by humans during normal operation? |
| 88 | `21.2.1` | YES | -0.203 | 1.996 | 1.793 | Was the AI system designed so as to be controlled or overseen by a human during operation? |
| 89 | `21.2.1.1` | YES | +0.203 | 1.793 | 1.996 | Have you evaluated the efficacy of oversight measures during normal operation? |
| 90 | `21.2.1.1.1` | NO | -0.203 | 1.996 | 1.793 | Were humans offered training on how to exercise control? |
| 91 | `21.3` | YES | +0.158 | 1.793 | 1.951 | Have you implemented technical measures to facilitate explicability of the outputs? |
| 92 | `21.3.1` | YES | +0.000 | 1.951 | 1.951 | Do these technical measures meet benchmarks and industry standards? |
| 93 | `22` | YES | -0.603 | 1.951 | 1.348 | Can the AI system be attacked resulting in unintended or unexpected harm? |
| 94 | `22.1` | YES | +0.171 | 1.348 | 1.519 | Is the training and application data stored securely with standard and robust authorisation and encryption requirements? |
| 95 | `22.2` | YES | +0.203 | 1.519 | 1.722 | Is the AI system robust against AI-specific adversarial attacks? |
| 96 | `22.3` | YES | +0.171 | 1.722 | 1.893 | Is the AI system resilient against model extraction and model replication attacks? |
| 97 | `22.4` | YES | +0.059 | 1.893 | 1.952 | Does the AI system have a functionality to report incidents or breaches to relevant authorities? |
| 98 | `23` | YES | +0.000 | 1.952 | 1.952 | Was there training to ensure sufficient AI literacy of the users? |
| 99 | `23.1` | YES | +0.000 | 1.952 | 1.952 | Was the training specifically adapted and contextualized for the use case? |
| 100 | `23.2` | YES | +0.000 | 1.952 | 1.952 | Does the training include basic concepts of machine learning and AI ethics? |

## TRL8 Waterfall

| Step | Indicator | Answer | Delta | Before | After | Question |
|---:|---|---|---:|---:|---:|---|
| 1 | `1` | YES | -0.720 | 4.000 | 3.280 | Can the product influence the user's decision-making? |
| 2 | `1.1` | YES | +0.360 | 3.280 | 3.640 | Have you implemented safeguards to prevent the product from unintentionally affecting users' autonomy? |
| 3 | `1.2` | NO | +0.360 | 3.640 | 4.000 | Is there a risk of users becoming overly reliant on the product? |
| 4 | `2` | YES | -1.000 | 4.000 | 3.000 | Is it possible that technical design decisions will result in significant damage? |
| 5 | `2.1` | YES | +0.360 | 3.000 | 3.360 | Does the product comply with recognized cybersecurity standards? |
| 6 | `2.2` | YES | +0.310 | 3.360 | 3.670 | Are there additional security measures against potential attacks throughout the product's lifecycle? |
| 7 | `2.2.1` | YES | +0.000 | 3.670 | 3.670 | Have you conducted penetration tests or red-team exercises on the product? |
| 8 | `2.3` | YES | +0.080 | 3.670 | 3.750 | Does the timeframe for security updates match the expected lifespan of the product? |
| 9 | `2.3.1` | YES | +0.000 | 3.750 | 3.750 | Have you informed users about the duration of security update coverage? |
| 10 | `2.4` | NO | +0.000 | 3.750 | 3.750 | Can the product be misused for malicious or illegal purposes? |
| 11 | `3` | YES | +0.000 | 3.750 | 3.750 | Is the product designed to adapt to diverse user/operator preferences and abilities? |
| 12 | `3.1` | YES | +0.000 | 3.750 | 3.750 | Have you evaluated accessibility by individuals with special needs or those at risk of exclusion? |
| 13 | `3.2` | YES | +0.000 | 3.750 | 3.750 | Were accessibility standards followed during development? |
| 14 | `3.3` | YES | +0.000 | 3.750 | 3.750 | Have you studied and evaluated possible discrimination against affected persons? |
| 15 | `3.3.1` | YES | +0.000 | 3.750 | 3.750 | Have you implemented measures to minimize unfair or discriminatory effects? |
| 16 | `4` | NO | +0.000 | 3.750 | 3.750 | Does the product have a negative impact on natural environment? |
| 17 | `5` | NO | +0.000 | 3.750 | 3.750 | Does the product affect work conditions and organizational structures? |
| 18 | `6` | YES | +0.000 | 3.750 | 3.750 | Have you established mechanisms to facilitate audits of the product? |
| 19 | `6.1` | YES | +0.000 | 3.750 | 3.750 | Can the product be audited by independent third parties for assigning responsibility? |
| 20 | `7` | YES | +0.000 | 3.750 | 3.750 | Are there oversight processes for ethical concerns and assigning responsibility? |
| 21 | `7.1` | YES | +0.000 | 3.750 | 3.750 | Is there ongoing oversight by a third party beyond the product's development phase? |
| 22 | `7.2` | YES | +0.000 | 3.750 | 3.750 | Have you considered establishing an ethics review board specifically for the product? |
| 23 | `7.3` | YES | +0.000 | 3.750 | 3.750 | Is there a process for third parties, such as suppliers or users, to report vulnerabilities or risks? |
| 24 | `7.3.1` | YES | +0.000 | 3.750 | 3.750 | Does the vulnerability reporting process contribute to updates in the product's risk management strategy? |
| 25 | `8` | YES | -0.750 | 3.750 | 3.000 | Does the product gather specialized categories of personal data, such as biometric or health-related information? |
| 26 | `8.1` | YES | +0.250 | 3.000 | 3.250 | Are there security protocols in place for safeguarding specialized categories of personal data? |
| 27 | `8.2` | NO | +0.000 | 3.250 | 3.250 | Does the product collect information concerning criminal convictions or offenses? |
| 28 | `8.3` | YES | +0.250 | 3.250 | 3.500 | Are the objectives for collecting personal data clearly defined, explicit, and legitimate? |
| 29 | `8.3.1` | YES | +0.000 | 3.500 | 3.500 | Is the acquired personal data strictly relevant and limited to what is essential for the intended purposes? |
| 30 | `8.3.2` | YES | +0.000 | 3.500 | 3.500 | Is the personal data you gather accurate and regularly updated? |
| 31 | `8.3.3` | YES | +0.000 | 3.500 | 3.500 | Is personal data stored in a way that allows for identification of subjects only for the duration needed for its intended use? |
| 32 | `9` | YES | +0.000 | 3.500 | 3.500 | Do you employ a Data Protection Officer (DPO) in accordance with European Union or Member State legislation? |
| 33 | `9.1` | YES | +0.000 | 3.500 | 3.500 | Is the DPO actively involved in all data protection matters? |
| 34 | `9.1.1` | YES | +0.000 | 3.500 | 3.500 | Does the DPO have a direct reporting line to the highest level of management? |
| 35 | `9.2` | YES | +0.000 | 3.500 | 3.500 | Is adequate resourcing provided for the DPO to execute their tasks? |
| 36 | `9.3` | YES | +0.000 | 3.500 | 3.500 | Is the DPO free from instructions that could compromise the impartial exercise of their responsibilities? |
| 37 | `9.4` | YES | +0.000 | 3.500 | 3.500 | Can data subjects directly communicate with the DPO regarding their personal data processing concerns? |
| 38 | `10` | YES | +0.000 | 3.500 | 3.500 | Are there methods to authenticate the identity of a data subject requesting access? |
| 39 | `10.1` | YES | +0.000 | 3.500 | 3.500 | Are the identity verification methods you employ both secure and reliable? |
| 40 | `10.1.1` | YES | +0.000 | 3.500 | 3.500 | Do you employ pseudonymization techniques as part of the identity verification process? |
| 41 | `10.1.2` | YES | +0.000 | 3.500 | 3.500 | Is personal data only retained for the purpose of responding to potential future requests? |
| 42 | `11` | YES | +0.000 | 3.500 | 3.500 | Does the product support the "right to be forgotten," allowing for the erasure of personal data? |
| 43 | `11.1` | YES | +0.000 | 3.500 | 3.500 | Can a data subject request erasure under some specified conditions? |
| 44 | `11.1.1` | YES | +0.000 | 3.500 | 3.500 | Can erasure be requested for data that is no longer necessary? |
| 45 | `11.1.2` | YES | +0.000 | 3.500 | 3.500 | Is erasure possible when the data subject withdraws consent and there's no other legal ground for processing? |
| 46 | `11.1.3` | YES | +0.000 | 3.500 | 3.500 | Can erasure be requested if the data subject contests the processing and no overriding legitimate reasons exist? |
| 47 | `11.1.4` | YES | +0.000 | 3.500 | 3.500 | Can erasure be executed when the personal data has been unlawfully processed? |
| 48 | `11.1.5` | YES | +0.000 | 3.500 | 3.500 | Is erasure possible to comply with legal obligations? |
| 49 | `11.1.6` | YES | +0.000 | 3.500 | 3.500 | Can erasure be requested for data gathered when the subject was a minor? |
| 50 | `12` | YES | +0.000 | 3.500 | 3.500 | Is all data processing information transparent and easily accessible to data subjects? |
| 51 | `12.1` | YES | +0.000 | 3.500 | 3.500 | Is data processing information also available in electronic formats? |
| 52 | `12.1.1` | YES | +0.000 | 3.500 | 3.500 | Is data processing information articulated in clear language that is easily understandable? |
| 53 | `12.1.2` | YES | +0.000 | 3.500 | 3.500 | Is the consent mechanism presented separately from other terms or conditions? |
| 54 | `12.1.3` | YES | +0.000 | 3.500 | 3.500 | Is it possible for data subjects to revoke their consent at any time? |
| 55 | `13` | YES | +0.000 | 3.500 | 3.500 | Does the product consider a minor's consent (below the age of 13-16)? |
| 56 | `13.1` | YES | +0.000 | 3.500 | 3.500 | Is the processing of data for subjects under 13-16 years of age based on parental consent? |
| 57 | `13.1.1` | YES | +0.000 | 3.500 | 3.500 | Are reasonable technological methods employed to confirm that parental consent is genuine? |
| 58 | `13.1.2` | YES | +0.000 | 3.500 | 3.500 | Does the product provide clear and age-appropriate information to subjects under 13-16 years about the data being collected? |
| 59 | `13.1.3` | YES | +0.000 | 3.500 | 3.500 | Is an option available for any minor to remove personal data? |
| 60 | `14` | NO | +0.000 | 3.500 | 3.500 | Does the product process personal data that is not needed for identification? |
| 61 | `18` | YES | +0.000 | 3.500 | 3.500 | Is the AI system considered high-risk as per relevant regulation in the European Union (AI Act)? |
| 62 | `18.1` | YES | +0.000 | 3.500 | 3.500 | Does it comply with relevant requirements for high-risk systems in the AI Act or includes a compliance plan for the upcoming regulation? |
| 63 | `19` | YES | +0.000 | 3.500 | 3.500 | Is performance of the AI system evaluated and documented? |
| 64 | `19.1` | YES | +0.000 | 3.500 | 3.500 | Is the AI system performance continuously evaluated during normal operation? |
| 65 | `19.1.1` | YES | +0.000 | 3.500 | 3.500 | Is a description of the risk management system included in the technical documentation? |
| 66 | `19.1.2` | YES | +0.000 | 3.500 | 3.500 | Does technical documentation include changes made to the system through its lifecycle? |
| 67 | `19.2` | YES | +0.000 | 3.500 | 3.500 | Does technical documentation include information about energy consumption? |
| 68 | `19.3` | YES | +0.000 | 3.500 | 3.500 | Does technical documentation address the monitoring, functioning, and control of the AI system? |
| 69 | `20` | YES | +0.000 | 3.500 | 3.500 | Do users get sufficient information about the methods and capabilities of the AI system? |
| 70 | `20.1` | YES | +0.000 | 3.500 | 3.500 | Does the AI system make users aware that they are communicating or interacting with the AI system? |
| 71 | `20.2` | YES | +0.000 | 3.500 | 3.500 | Does the AI system inform users of its limitations? |
| 72 | `20.3` | YES | +0.000 | 3.500 | 3.500 | Are affected persons informed about their rights? |
| 73 | `21` | YES | -0.518 | 3.500 | 2.982 | Do decisions or outputs of the AI system influence or affect humans directly? |
| 74 | `21.1` | YES | +0.158 | 2.982 | 3.140 | Did you establish detection and response mechanisms for undesirable effects, for example false negatives or false positives? |
| 75 | `21.1.1` | YES | +0.000 | 3.140 | 3.140 | Is there a 'stop button' (if relevant) or a procedure for humans to safely abort operation of the AI system? |
| 76 | `21.2` | YES | +0.203 | 3.140 | 3.343 | Can the AI system be controlled or overseen by humans during normal operation? |
| 77 | `21.2.1` | NO | +0.000 | 3.343 | 3.343 | Was the AI system designed so as to be controlled or overseen by a human during operation? |
| 78 | `21.3` | YES | +0.158 | 3.343 | 3.501 | Have you implemented technical measures to facilitate explicability of the outputs? |
| 79 | `21.3.1` | YES | +0.000 | 3.501 | 3.501 | Do these technical measures meet benchmarks and industry standards? |
| 80 | `22` | YES | -0.603 | 3.501 | 2.898 | Can the AI system be attacked resulting in unintended or unexpected harm? |
| 81 | `22.1` | YES | +0.171 | 2.898 | 3.069 | Is the training and application data stored securely with standard and robust authorisation and encryption requirements? |
| 82 | `22.2` | YES | +0.203 | 3.069 | 3.272 | Is the AI system robust against AI-specific adversarial attacks? |
| 83 | `22.3` | YES | +0.171 | 3.272 | 3.443 | Is the AI system resilient against model extraction and model replication attacks? |
| 84 | `22.4` | YES | +0.059 | 3.443 | 3.502 | Does the AI system have a functionality to report incidents or breaches to relevant authorities? |
| 85 | `23` | YES | +0.000 | 3.502 | 3.502 | Was there training to ensure sufficient AI literacy of the users? |
| 86 | `23.1` | YES | +0.000 | 3.502 | 3.502 | Was the training specifically adapted and contextualized for the use case? |
| 87 | `23.2` | YES | +0.000 | 3.502 | 3.502 | Does the training include basic concepts of machine learning and AI ethics? |