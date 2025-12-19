# Frequently Asked Questions

This document answers common questions about the project.

---

## About The MitsuoLabs™ MASTER PROFESSIONAL AND END USER LICENSE AGREEMENT (MMPEULA-1.0)

This section addresses common legal and operational questions regarding the MMPEULA-1.0. The answers provided herein are for informational purposes and do not constitute legal advice. For binding interpretations, refer to the full text of the Agreement and consult with qualified legal counsel.

**1. Is the five-minute mandatory review period and the seven-checkbox affirmation protocol legally enforceable, or is it merely procedural theatre?**

This is not theatre; it is a meticulously designed consent-verification framework intended to be fully enforceable. The protocol, as detailed in Axiom 1 and Appendix 1, is engineered to create a robust, auditable, and legally defensible record of informed consent. By programmatically enforcing a 300-second review period (Clause 1.4) and requiring seven discrete affirmations for material terms (Clause 1.5), the protocol preemptively refutes any subsequent claim by the Licensee of surprise, ignorance, or lack of a meaningful opportunity to review. In any legal proceeding, Licensor would present the timestamped logs of these actions as conclusive evidence that assent was not just passive, but deliberate, informed, and procedurally sound, thereby shifting the burden to the Licensee to prove otherwise.

**2. Our startup developers sometimes use personal machines for work. Does this breach the "professional-use" warranty and expose us to risk?**

This is a critical point of compliance. The Agreement is explicitly structured as a business-to-business (B2B) contract, and Licensee represents and warrants that it is not a "consumer" (Clause 1.6). While the use of personal hardware for professional work is common, the legal character of the *use itself* must be professional. If your developers are using the Covered Binaries to perform work for the company, the use is professional. However, this situation is legally managed by Axiom 34 (Layered Defense and Consumer Fallback Protocol). If your entity could be re-characterised as a collection of consumers, you have an affirmative duty to declare this status (Clause 34.2). Failure to do so constitutes a material misrepresentation, and you would be estopped from later claiming consumer rights. The risk is not in the hardware, but in the legal nature of the Licensee entity and the purpose of the use.

**3. The Agreement claims jurisdiction in Brazil, the US, and the EU. How is a conflict of laws resolved, and isn't this "jurisdictional layering" unworkably complex?**

The jurisdictional layering described in Clause 1.2 is a sophisticated but necessary feature for a globally distributed professional tool. It is not intended to be complex, but robust. The primary governing law is designated by the Licensor (or Brazil by default, per Axiom 18.1), providing a predictable baseline. The layering serves as a compliance mechanism, acknowledging that mandatory, non-waivable laws in the Licensee's local jurisdiction (e.g., EU data protection law) will apply to the minimal extent required. In the event of a direct conflict, the provision is to be modified only to the degree necessary for local compliance, while preserving the Agreement's core risk allocations. This "blue-pencil" approach (Clause 2.6) ensures the Agreement does not fail in its entirety and remains enforceable across diverse legal environments.

**4. Our company policy forbids assigning Intellectual Property rights for employee feedback. Does Clause 4.3's mandatory assignment of Feedback rights create an unavoidable conflict?**

Yes, it creates a direct conflict that your organisation must resolve internally before accepting the Agreement. Clause 4.3 operates as an irrevocable assignment of all right, title, and interest in Feedback to the Licensor. This is a non-negotiable term, as it ensures the Licensor has the unfettered right to incorporate and commercialise valuable suggestions without future legal encumbrance or royalty obligations. If your internal policies are incompatible, you must either secure a waiver to your internal policy for this specific Agreement or refrain from providing any Feedback whatsoever. Providing Feedback while under a conflicting internal policy would place your organisation in breach of this Agreement.

**5. How can you provide the software "AS IS" (Axiom 6.2) while marketing it as a "professional-grade" tool? Is this not a contradiction?**

There is no legal contradiction. "Professional-grade" is a description of the tool's intended audience, complexity, and feature set. "AS IS" is a precise legal term that disclaims implied warranties (Axiom 6). The Agreement is transparent that while the tool is built for professionals, it is the professional's responsibility to validate its suitability for a specific purpose. A professional, unlike a general consumer, is expected to possess the skill to test, verify, and implement appropriate safeguards and redundancies. The Agreement provides a very limited 30-day warranty for media and delivery conformance only (Clause 6.1), and any further assurances require the purchase of a separate, enterprise-level support agreement.

**6. What precisely constitutes a "high-risk environment" under Clause 3.3, and what is the process for obtaining the required "explicit, written authorization"?**

A "high-risk environment" is defined inclusively in Clause 19.2 as any context where failure could result in death, personal injury, or significant environmental harm. This includes, but is not limited to, medical devices, aviation control, nuclear facilities, and critical infrastructure. The definition is intentionally broad to place a clear duty of care on the Licensee. The process for obtaining authorization is formal and rigorous, as detailed in Appendix 3 (High-Risk Deployment Framework). It requires the Licensee to fund a comprehensive third-party risk assessment, purchase an enhanced warranty with a higher liability cap, secure specific insurance policies naming the Licensor as an additional insured, and accept an expanded indemnification clause. Authorization is not granted lightly and is reserved for mission-critical applications where risk has been formally assessed and contractually re-allocated.

**7. How do you define "compete" regarding the restriction on training machine learning models in Clause 3.3(d)? Does this prohibit legitimate internal R&D?**

"Compete" is determined by the functional output and market position of the resulting model. If an ML model trained using the Covered Binaries produces outputs that are substantially similar to, and could serve as a commercial substitute for, Licensor's own offerings, it is deemed to be in competition. This clause is not intended to prohibit all internal R&D. Legitimate internal research that does not result in a competing commercial service is permissible. However, if your R&D efforts pivot to creating a product that directly challenges a Licensor product, you would be in breach. The onus is on the Licensee to ensure its use case does not cross this line or to negotiate a specific partnership or licensing agreement with the Licensor for such purposes.

**8. The Licensee indemnity in Axiom 9.1 seems exceptionally broad. Is this standard for B2B software, and under what circumstances would the "gross negligence" exception realistically apply?**

The indemnity obligation in Axiom 9.1 is indeed broad, which is a deliberate and essential risk-allocation feature in a professional tools agreement where the Licensor has no control over the Licensee's specific implementation. It is standard for Licensors to require indemnification for liabilities arising from the Licensee's use of the software. The "gross negligence or willful misconduct" exception is a high legal bar. It would typically apply only if a Licensor, for instance, knowingly and intentionally pushed a malicious update that directly caused the third-party claim, or demonstrated such a reckless disregard for the security and integrity of the software that it amounted to more than simple error. Ordinary bugs, design flaws, or operational mistakes by the Licensor would fall under ordinary negligence and would not typically negate the Licensee's indemnity obligation.

**9. Are the clauses in Axiom 31 covering "cosmic events" and "temporal anomalies" legally serious? What is their functional purpose?**

These clauses are legally serious and serve a critical long-term governance and risk-management function. Axiom 31 is a "future-proofing" mechanism designed to ensure the Agreement remains stable and interpretable in the face of low-probability, high-impact "black swan" events that would render conventional contracts ambiguous or moot. Its purpose is to establish, *a priori*, a clear protocol for evidence preservation, non-escalation, and responsible coordination. For example, in the event of a verified extraterrestrial contact, this clause prevents a Licensee from unilaterally acting in a way that could create global risk, and instead mandates coordination with competent authorities. These are not speculative fantasy; they are carefully drafted contingency plans for scenarios where the rule of law and contractual stability are most needed.

**10. If our platform is used by a third party for one of the "Worst Uses" prohibited in Axiom 25 without our knowledge, are we in material breach?**

Your liability hinges on your operational diligence. Simply being the platform for a third party's prohibited act does not automatically place you in breach. However, this Agreement imposes a duty of care. Axiom 24 requires you to implement "reasonable technical controls" (24.1), an internal Acceptable Use Policy (24.7), and to cooperate in investigations (24.3). If you can demonstrate that you had robust preventative measures in place and acted swiftly to remediate upon notice, you would have a strong defense. Conversely, if you exhibited willful blindness or failed to implement industry-standard moderation and security practices, you could be found in material breach for failing to meet your operational safeguard obligations.

**11. Who adjudicates what constitutes "extremist ideology" or "institutional racism" under Axiom 26, and what prevents this from being used to censor based on political viewpoints?**

The Licensor makes the initial determination, but this is not an arbitrary power. The enforcement is governed by the protocols in Appendix 4 and Appendix 14. An enforcement action can be appealed internally, and if necessary, challenged via the formal dispute resolution process in Axiom 18. The Agreement itself provides interpretive safeguards: Clause 35.7 mandates a narrow construction, and Clause 35.11 provides a safe harbor for lawful expression. A violation would require conduct that is demonstrably discriminatory or incites violence, not merely the expression of an unpopular political view. For "institutional racism," Appendix 14.1 provides an objective test: a policy that results in a "persistent, statistically significant, and negative disparate impact." Enforcement must be based on evidence and objective outcomes, not political disagreement.

**12. How can Axiom 33's warranty of mental capacity and sobriety be practically enforced? Isn't it an attempt to shift all liability for user error?**

Axiom 33 is an explicit assumption of risk by the Licensee. It is not about active enforcement by the Licensor, but about establishing a clear, pre-agreed legal fact: the responsibility for assessing one's fitness to perform high-stakes actions rests solely with the user. If a user performs a destructive action (e.g., deleting a production database) and later claims they were intoxicated or distressed, this clause serves to estop that claim. The "Cognitive State Verification" gateways (Appendix 6) further bolster this by creating a timestamped record where the user actively affirms their capacity at the moment of action. It does not absolve the Licensor of all liability (e.g., for a critical bug), but it firmly allocates the risk of impaired human judgment to the human exercising that judgment.

**13. Axiom 35 seems designed to procedurally block any legal challenge of unconscionability. Do these "defensive" clauses hold up in court?**

Axiom 35 is an aggressive but transparent attempt to structure the legal relationship between two sophisticated commercial parties. In a B2B context, courts are generally far more reluctant to invalidate agreements than in consumer contexts. This Axiom strengthens the Licensor's position by contractually defining the rules of engagement for such a challenge. Provisions like fee-shifting for failed challenges (Clause 35.4) and presumptions of validity (Clause 35.12) are designed to deter frivolous litigation. While no contract can completely strip a court of its ultimate authority to assess fairness, Axiom 35 ensures that any such assessment must contend with the fact that the Licensee explicitly acknowledged the terms, had the opportunity to negotiate, and agreed to these specific procedural rules as part of the bargain.

**14. If the source code is available under the FOSS MRSL-1.0 license, why can't we just compile it ourselves and ignore the highly restrictive MMPEULA?**

You are absolutely free to do so, but you misunderstand the dual-license architecture. The MRSL-1.0 governs the *source code*, and it grants you the FOSS rights to study, modify, and compile it. The MMPEULA governs the *official compiled binary* distributed by the Licensor.

If you compile the source yourself, you are not a Licensee of the MMPEULA. However, you are now a distributor of a new binary, and you are bound by the strong copyleft and network reciprocity terms of the MRSL-1.0. You gain FOSS freedom, but you lose the benefits of the official binary: the Licensor's commercial support, warranties (if any), indemnification, and the assurance of a professionally built and signed product. This model provides a choice: the convenience and protection of the commercial binary under the MMPEULA, or the freedom and responsibility of the FOSS source code under the MRSL.

**15. What is the legal and business rationale for including clauses on "faith-based support" (Axiom 31) in a software license?**

The inclusion of these clauses is a reflection of the Licensor's unique corporate philosophy and a proactive risk-management strategy for non-traditional scenarios. The legal rationale is to establish clear, auditable protocols *before* a crisis that might involve mass belief or community mobilization (whether inspired by an in-game event, an AI's output, or an external phenomenon). By defining rules for non-coercive, opt-in, and transparently administered aid (Clauses 31.5, 31.8), the Licensor insulates its core business operations from these activities and mitigates the immense legal and reputational risk of being seen as either exploiting or being hostile to belief systems during a crisis. The business rationale is to build long-term trust with diverse communities by demonstrating a documented, principled approach to complex ethical situations that other corporations ignore.

---

## About The MitsuoLabs™ Reciprocity and Stewardship License (MRSL-1.0)

This section addresses common legal and operational questions regarding the MRSL-1.0. The answers provided herein are for informational purposes and do not constitute legal advice. For binding interpretations, refer to the full text of the License and consult with qualified legal counsel.

**1. The MRSL-1.0 has two parts. Is Part II (The Stewardship Rider) optional? Can I use the software without accepting the Ethical Use Covenant?**

Yes, Part II is strictly optional. The MRSL-1.0 is a dual-framework license designed to be fully FOSS-compliant. Part I grants all the essential FOSS rights (the right to use, study, modify, and distribute) without any ethical field-of-use restrictions. You are free to use the software under the terms of Part I, which functions as a strong copyleft license, without ever accepting Part II. Part II is a separate, voluntary contractual rider. You only become a "Steward" and bind yourself to the Ethical Use Covenant (Section 25) if you make an explicit, documented declaration as outlined in Section 24 and Appendix 11.

**2. What are the material benefits of becoming a "Steward"? Why would I voluntarily accept the Ethical Use Covenant?**

Becoming a Steward is a calculated business and legal decision. In exchange for contractually committing to the Ethical Use Covenant, you are granted a suite of powerful legal protections and governance rights under Section 26 that are not available under Part I. These include:

*   **Patent and Trademark Indemnification:** The Licensor provides a limited but formal indemnification against certain IP claims.
*   **Comprehensive Limitation of Liability:** You receive a broad shield from liability for damages arising from the use of The Work.
*   **Mutual Indemnification:** You and other Stewards agree to defend each other against certain IP claims related to contributions.
*   **Governance Rights:** You gain a formal voice in project governance, with prioritized engagement from maintainers.

Essentially, you trade a degree of freedom in your use cases for a significant reduction in legal and financial risk, as well as a greater say in the project's future.

**3. How does the "Network Reciprocity" clause (Section 6) differ from the AGPL, and what does it require of SaaS providers?**

The MRSL-1.0's Network Reciprocity clause is philosophically similar to the AGPL's but is drafted with broader, more modern language. It applies not just to traditional web services but to any service provided over a network, including APIs, P2P services, and future network analogues. If you run a modified version of The Work to provide a network service, you must provide all users who interact with that service a "conspicuous and convenient" means to obtain the complete Corresponding Source of your modified version. This ensures that the freedom of the software extends to the cloud and that SaaS providers cannot create proprietary derivatives without sharing their improvements back with the community.

**4. The license mentions "Artificial Intelligence Systems" and "Synthetic Agents". What are a Contributor's obligations when submitting AI-generated code?**

Section 11 places a clear warranty obligation on the Contributor. By submitting a Contribution, you certify that you have the legal right to do so, even if it was generated or assisted by an AI. This means you are responsible for ensuring that the AI's output does not violate the licenses of its training data or infringe on third-party copyrights. The license anticipates the legal complexities of AI-generated code and places the burden of due diligence squarely on the human Contributor who submits it. You cannot use "the AI did it" as a defense against an infringement claim.

**5. Can I use MRSL-1.0 licensed code in a product that I sell in a device (Tivoization)?**

No, you cannot lock it down. Section 8, the "Freedom to Run, Modify, and Secure" clause, is a strong anti-tivoization provision. If you convey The Work in a User Product or as Firmware, you are contractually obligated to provide the user with any keys, signatures, or information necessary to install and run their own modified version of The Work on that device. Security measures are permitted, but they cannot be used as a pretext to prevent users from exercising their FOSS rights.

**6. The Ethical Use Covenant (Section 25) prohibits "Mass Surveillance". How is "mass" defined, and would this prevent legitimate security monitoring?**

The Covenant provides a bright-line rule. "Mass Surveillance" is defined as the collection and analysis of Personal Data from more than 10,000 individuals in a single jurisdiction *without* either their explicit, opt-in consent for each category of data collected, or a specific judicial warrant. This clause is not intended to prohibit legitimate, narrowly-scoped security monitoring (e.g., intrusion detection, log analysis for security incidents). It is designed to prevent the creation of large-scale, warrantless data collection systems for purposes of social control or broad population analysis.

**7. How is the MRSL-1.0 compatible with the GPL (Section 29)? This seems unusual for a custom license.**

This compatibility is a deliberate and pragmatic design choice. Section 29 provides a specific, one-way compatibility exception. You are permitted to combine MRSL-1.0 code with code from the GPL family (GPL, LGPL, AGPL) and convey the combined work under the terms of the GPL-family license. This allows projects to migrate from the GPL to the MRSL or to use MRSL components in existing GPL ecosystems. However, it's a one-way street; you cannot take GPL code and relicense the combined work solely under the MRSL. You must still satisfy the MRSL's attribution and source availability requirements for the MRSL-licensed portions.

**8. What is the purpose of "The Alexandria Clause" (Section 19)? Is it legally binding?**

The Alexandria Clause is a legally binding, good-faith obligation. It requires Contributors to make a reasonable effort to submit the Corresponding Source of major public releases to at least two public software heritage archives. Its purpose is to ensure the long-term preservation of the software, protecting it from being lost due to repository takedowns, company failures, or link rot. While a failure to do so might be difficult to enforce with damages, a court could grant specific performance, compelling the Contributor to fulfill their archival duty. It is a contractual commitment to digital preservation.

**9. Section 13 imposes specific conditions for use in blockchain or digital asset systems. What is the rationale?**

This section is a direct response to the risks and lack of transparency common in the blockchain space. The rationale is to ensure that if the software is used for systems managing assets of value, the core principles of FOSS are not subverted. It requires: (a) on-chain source code verification for smart contracts, preventing bait-and-switch deployments; (b) ensures that token rights cannot override the software's underlying FOSS license; and (c) mandates a link to a third-party security audit, providing a baseline of user protection against unaudited and potentially malicious financial infrastructure.

**10. What does it mean that the text of the license itself is licensed under MRSL-1.0?**

This means that you have the freedom to reuse, modify, and distribute the legal text of the MRSL-1.0 itself, as long as you comply with the MRSL-1.0. However, Section 30 is crucial: you may not use the names "MRSL-1.0" or "MitsuoLabs Reciprocity and Stewardship License" to describe your modified version. You can fork the license for your own purposes, but you must give it a new name to avoid confusion and protect the integrity of the official MRSL. This allows for legal innovation while maintaining a canonical version.

**11. The "Right of Repair" (Section 17) seems to grant a right to fork. How does this work in practice?**

This is a community-empowering backstop against project abandonment or negligence. If a critical security vulnerability (CVSS score of 9.0 or higher) is publicly known and the main project maintainers do not issue a patch within 90 days, this clause contractually permits any Contributor to create a "Repair Fork". This is not just a right to fork (which is inherent in FOSS), but a right to do so under a specific, legitimized protocol. The forker can create a repository, issue a signed release with clear versioning (e.g., `v1.2.3-repair.1`), and notify the community. It provides a legal and procedural framework for the community to save itself when maintainers fail to act on a critical security issue.

**12. The Stewardship Rider includes indemnification with a US$1,000 cap. What is the practical value of such a low cap?**

The value is not primarily financial; it is legal and procedural. The US$1,000 cap is a nominal amount designed to make the indemnification grant legally concrete and enforceable, satisfying the requirement for consideration in some legal systems. The true value for the Steward is in the legal architecture it creates: (a) it establishes a formal duty to defend from the Licensor, forcing them to be involved in a claim from the outset; and (b) it serves as a powerful signal in any legal dispute that the parties have explicitly considered and allocated risk, even if the monetary value is small. It turns an abstract promise into a concrete, if limited, contractual obligation.

**13. Does the "Temporal and Ontological Integrity" clause (Section 35) have any real-world legal effect?**

This clause serves as an interpretive guide for courts and arbitrators when dealing with novel technological scenarios. Its purpose is to prevent bad-faith arguments that the license somehow becomes void if the software is run in an unexpected environment (e.g., a quantum computer, a biological system, or a sufficiently advanced simulation). By stating that rights are bound to the causal history of the work, it asserts that the license's obligations travel with the code, regardless of its execution substrate. While untested in court, it provides a strong textual basis to argue for the license's continued applicability in the face of disruptive technological change, instructing a judge to uphold the original intent rather than declare the agreement void due to novelty.

**14. If a Steward breaches the Ethical Use Covenant, do they lose all rights to the software?**

No. The license is architected with a crucial separation of rights. A breach of the Ethical Use Covenant (Section 25) only terminates the *advanced rights* granted under the Stewardship Rider (Section 26) for that specific work. The Steward loses their patent indemnification, their liability shield, their governance rights, etc. However, they do not lose the core FOSS rights granted under Part I. If they cease their violation and are otherwise in compliance with Part I (e.g., providing source code), they retain the basic rights to use, modify, and distribute the software, just like any other non-Steward user. This makes enforcement more practical and proportionate.

**15. Why does the license designate Brazil as a default jurisdiction? What are the implications for a US or EU-based company?**

The designation of Brazil as a default jurisdiction (Section 32) provides a predictable legal baseline for a global license. For a US or EU company, the implications are:

*   **Predictability:** You know that in the absence of a different agreement, the dispute resolution framework is centered on a specific, known legal system.
*   **Consent to Jurisdiction:** By conveying The Work, you consent to the exclusive jurisdiction of the Brazilian courts for enforcement actions, which simplifies cross-border legal disputes.
*   **Mandatory Local Law Still Applies:** This choice of law does not override mandatory, non-waivable consumer or public order laws in your local jurisdiction. An EU court would still apply mandatory GDPR provisions, for example. The governing law clause primarily applies to the interpretation of the contract itself between commercial parties.

It is a standard practice in international contracts to choose a specific jurisdiction to avoid lengthy and complex preliminary battles over where a dispute should be heard.

## About Integration & Developer Implementation

This section addresses the practical and technical questions developers may have when integrating the MitsuoLabs™ dual-licence framework into their projects and automated workflows.

**1. What is the core integration concept for the MMPEULA and MRSL?**

The framework operates on a dual-licence architecture, which creates a clear legal separation between the source code and the compiled binary:

* **The Source Code** (Source Components): Governed by a Free and Open Source Software (FOSS) licence, typically the MitsuoLabs™ Reciprocity and Stewardship License (MRSL-1.0). This ensures the underlying code remains perpetually free, auditable, and open for community contribution, consistent with FOSS principles.
* **The Executable** (Covered Binary): Governed by the MitsuoLabs™ Master Professional and End User License Agreement (MMPEULA-1.0). This is a robust, professional-grade EULA that manages the terms of use for the ready-to-run software product, providing clear rules for distribution, liability, and acceptable use in a commercial context.
Integration requires maintaining this separation: developers work with the MRSL-licensed source, while the build and distribution process packages the resulting binary under the MMPEULA.

**2. How do I practically use placeholders like [[product-name]] and [[licensor-name]]?**

These placeholders are designed for automated substitution during your build process. The intended workflow is:

* **Configure**: You populate a central configuration file, project_config.json, with the specific details for your project (e.g., your company's legal name, product name, contact addresses).
* **Automate**: You execute the scripts/generate_license_files.py script as a step in your CI/CD pipeline.
* **Generate**: The script reads project_config.json and the licence templates (e.g., mmpeula-1.0.html, mrsl-1.0.txt). It then replaces all placeholder tokens with the values from your configuration file.
* **Output**: The script saves the finalized, project-specific licence files into a distribution directory (e.g., dist/ or generated_licenses/). These generated files are what you bundle with your final product.
This process ensures that your distributions always contain legally precise and correctly populated licence agreements without manual editing.

**3. What are the mandatory CI/CD checks for a project using these licences?**

Axiom 37.11 of the MMPEULA mandates that the repository hosting the licence templates includes a continuous integration (CI) pipeline with the following automated checks to ensure compliance and quality:

* **Placeholder Linter**: A check that fails if any non-standard or malformed placeholder tokens are found in the licence files. It must enforce the canonical [[placeholder-name]] format.
* **SPDX Scanner**: A check to verify the presence and basic validity of compliance artifacts like NOTICE files and SPDX-compatible licence inventories.
* **Spell/Grammar Check**: A basic smoke test to catch obvious typographical errors that could create legal ambiguity.
* **Manifest Generation**: The pipeline must produce a machine-readable manifest of licence information that can be used by installers and packaging tools.
* **Signing and Checksums**: All build artifacts intended for public distribution must be cryptographically signed, and their checksums must be included in the release metadata to ensure integrity.

**4. How should I implement the MMPEULA "Acceptance Protocol" in my application's installer?**

The protocol, detailed in Appendix 1 of the MMPEULA, requires a multi-stage process to create a legally robust record of consent. A compliant implementation must include:

* **Full Text Display**: Present the complete, final text of the MMPEULA in a scrollable view.
Mandatory Review Period: Upon display, start a non-skippable, client-side timer for 300 seconds (5 minutes). During this period, the "Accept" button must be disabled.
* **Affirmation Checkbox Sequence**: After the timer expires, the "Accept" button remains disabled until the user has actively toggled seven (7) mandatory checkboxes. Each checkbox corresponds to a key legal affirmation (e.g., accepting the "AS IS" warranty, the limitation of liability, and the arbitration clause).
* **Final Acceptance**: Only after the timer has elapsed and all seven checkboxes are ticked can the "Accept" button be enabled.
* **Proof of Consent**: Upon acceptance, your installer should generate and store a timestamped, auditable record (a "Cryptographic Proof of Consent") that includes a hash of the EULA text and a log of the user's actions.
**5. What compliance artifacts must I bundle with my final distributed product?**

To comply with both the MMPEULA and standard FOSS practices (as referenced in MRSL-1.0), your distribution package must include:

The generated MMPEULA file (e.g., mmpeula-1.0.html).
The generated MRSL file (or other applicable source licence, e.g., mrsl-1.0.txt).
A NOTICE file that includes all required attributions for third-party open-source components used in your project.
An SPDX-compatible inventory of all third-party components, their versions, and their specific licence identifiers (as required by Axiom 37.10). This is often included within the NOTICE file or as a separate licenses.json file.
The full, unmodified text of all third-party open-source licences in a LICENSES/ directory.
**6. My project uses other open-source libraries. How do I manage their licences alongside MRSL-1.0?**

You must adhere to the principle of Dual-Regime Coherence (Axiom 36) and the compatibility guidelines in MRSL-1.0 (Section 29 & Appendix 4).

* **Separation**: You must treat your proprietary code, the MRSL-licensed code, and other third-party FOSS components as distinct legal entities. The rights and obligations of one do not automatically "infect" the others.
* **Compliance**: You are responsible for complying with the terms of all licences simultaneously. For example, if you use an MIT-licensed library, you must include its copyright notice and licence text. If you modify an MPL-licensed file, you must keep that file under the MPL.
* **Strong Copyleft (MRSL)**: If you create an "Integrated Work" (e.g., a full application), MRSL-1.0's strong copyleft requires that the entire work be licensed under MRSL-1.0 when conveyed. However, its compatibility clause (Section 29) provides an exception for combining with GPL-family licences.

**7. How do I officially become a "Steward" for my project under MRSL-1.0?**

Becoming a Steward is a formal, voluntary act that grants you additional legal protections in exchange for accepting the Ethical Use Covenant. To do so, you must:

Create a file named STEWARD.md in the root of your project repository.
Add a formal declaration to this file, including your legal name (individual or organization), contact details, and the date.
The declaration must explicitly state your acceptance of the Stewardship Rider (Part II) for that specific project.
Submit this change with a signed commit message that clearly indicates the action, for example: Steward: Yes (MRSL-1.0) — My Company LLC [YYYY-MM-DD].
This creates a public, auditable record of your acceptance.

**8. My application is a web service. What are my obligations under MRSL's "Network Reciprocity" clause?**

Section 6 of MRSL-1.0 extends copyleft obligations to network services (SaaS, APIs, etc.). If you run a modified version of the MRSL-licensed software to provide a service over a network, you have the same core obligation as if you were distributing the software: you must provide all users who interact with the service with a conspicuous and convenient means to obtain the complete Corresponding Source of your modified, server-side version.

This is designed to close the "SaaS loophole" and ensures that the freedoms of the software are preserved even when it is not distributed directly to users' machines.

**9. What is the process for handling updates to the MMPEULA or MRSL licence templates?**

The licences are versioned (e.g., 1.0). When MitsuoLabs™ releases a new version, the following principles apply:

* **Non-Retroactivity**: A new licence version does not apply retroactively to software you have already distributed.
* **Developer Choice**: For new releases of your product, you may choose to adopt the updated licence version. Your CI/CD process would be updated to pull the new templates.
* **Notice for Material Changes**: For the MMPEULA, if an amendment materially alters a user's rights, it requires re-acceptance through the formal Acceptance Protocol (Axiom 23.3). For the MRSL, material changes to the canonical text undergo a public comment period (Section 42).
**10. What is the role of scripts/generate_license_files.py in the developer workflow?**

This script is a crucial piece of compliance automation. Its role is to:

**Ensure Accuracy**: Prevent manual copy-paste errors when populating licence details.
**Centralise Configuration**: Allow all project-specific legal variables to be managed in a single project_config.json file.
**Automate Compliance**: Serve as a reliable, repeatable step in a CI/CD pipeline to generate the final, legally binding licence documents that are bundled with a release.
Developers should not modify the licence templates directly. Instead, they should update project_config.json and run the script to propagate changes, ensuring every build is correctly and consistently licensed.

**11. The GOVERNANCE.md template in MRSL-1.0 Appendix 5 mentions a "Steward Council". Is this a mandatory part of the integration, and how is it formed?**

The Steward Council is an optional governance mechanism, not a mandatory one. As detailed in MRSL Appendix 5 and Appendix 13, it is provided as a ready-to-use template for projects that wish to formalize the role of Stewards in decision-making. If a project adopts it, the council is typically formed through an election where active Stewards vote for representatives for a defined term (e.g., 12 months). Its purpose is to provide a structured forum for Stewards to advise on the project's roadmap, resolve conflicts, and vote on major proposals. Small projects may not need this formality, but for larger projects, it provides a clear and transparent governance path.

**12. How do the licenses handle patent grants? Is there a difference between the core MRSL licence and the Stewardship Rider?**

Yes, there is a critical legal difference. This dual approach is a core part of the framework's risk management for developers.

* **Part I (Core License)**: Provides a standard, defensive patent grant (Section 12). Each contributor grants you a license to use their patented inventions that are necessarily infringed by the software. This protects you from being sued by other contributors for using the code they provided. However, it offers no protection or warranty against claims from third parties.
* **Part II (Stewardship Rider)**: When you become a Steward, you receive "Advanced Rights" under Section 26. This includes a formal, albeit capped (at US$1,000), patent indemnification from the Licensor and a mutual indemnification agreement with other Stewards. This means that if a third party sues you for patent infringement related to the software, you have a contractual right to seek a defense and limited financial coverage from the Licensor and other Stewards. This is a significant legal benefit not available to non-Steward users.

**13. What does "Corresponding Source" mean in practice for an AI model licensed under MRSL-1.0?**

"Corresponding Source" for an AI model is explicitly defined to be more than just the inference code. According to Section 1 of the MRSL, it includes all the artifacts "necessary to reproduce the running form." For an AI system, this contractually obligates you to provide:

The model architecture definition code.
The training scripts and all configuration files used.
The source code of any custom preprocessing or data augmentation logic.
A detailed list of all training datasets, including their names, versions, original sources, and their respective licenses (provenance).
Any model weights that are bundled with the project.
The goal is to provide downstream users with everything they need to understand, replicate, and modify the model, not just run it as a black box.

**14. The MMPEULA has an "Acceptable Use Policy" (AUP) and the MRSL has an "Ethical Use Covenant". How do these two legal constructs interact?**

They operate on two different layers and apply to two different groups, which is a key part of the integration's legal design:

* **MMPEULA Acceptable Use Policy (Axiom 19)**: This applies to every end user of the compiled binary. It is a broad set of rules prohibiting illegal and harmful activities. A breach of the AUP terminates the user's right to use the executable software.
* **MRSL Ethical Use Covenant (Section 25)**: This applies only to a developer who has voluntarily chosen to become a Steward of the source code. It is a set of specific prohibitions on high-harm activities (e.g., mass surveillance). A breach of the Covenant terminates the developer's Stewardship rights (like patent indemnity), but they still retain their underlying FOSS rights to the code under Part I of the MRSL.
* **In short**: All end users are bound by the AUP. Only developers who opt-in as Stewards are additionally bound by the Ethical Covenant, and only in relation to their own contributions.

**15. My build process uses containers (e.g., Docker). How do I satisfy the source code availability requirements of MRSL-1.0 in this context?**

In a containerized environment, the requirement to make the Corresponding Source "readily, reliably, and durably available" (MRSL Section 4) must be met with deliberate integration steps. Simply running the code inside a container does not negate this duty. Best practices include a combination of the following:

* **Dockerfile LABEL**: Use the org.opencontainers.image.source label in your Dockerfile to embed a permanent link to the exact source code commit hash from which the container image was built.
* **Bundled Artifacts**: COPY the generated NOTICE file, the LICENSES/ directory containing all third-party licenses, and a machine-readable MRSL_SOURCE.json (as described in MRSL Appendix 12) directly into the container image (e.g., into /usr/share/doc/my-app/licenses/).
* **Environment Variable**: Set a runtime environment variable within the container (e.g., MYAPP_SOURCE_COMMIT_URL) that provides a direct URL to the source.
* **Registry Documentation**: The README or documentation for your image on the container registry (e.g., Docker Hub, Quay.io) must include a clear, public-facing link to the source code repository.
The key is ensuring that any user who pulls or runs your container can easily and reliably trace it back to the exact Corresponding Source used in its creation.

**16. What is the legal status of the Appendices in the MMPEULA and MRSL? Are they binding?**

This is a crucial distinction between the two licenses, designed for different legal purposes:

* **MMPEULA Appendices**: Binding. Clause 23.1 of the MMPEULA states that the Appendices are "expressly incorporated by reference" and form part of the "entire agreement." They provide the detailed, operational frameworks that give the Axioms legal effect. For example, the Acceptance Protocol in Appendix 1 is not a suggestion; it is a contractually mandated procedure.
* **MRSL-1.0 Appendices**: Non-binding. The preamble to the MRSL Appendices explicitly states they are "non-binding operational materials" and "templates." They provide ready-to-use examples for CONTRIBUTING.md, governance models, and checklists. You are encouraged to use them, but you are not contractually required to do so. Their purpose is to promote best practices, not to impose additional legal obligations beyond what is in Parts I-III of the license.

**17. The MMPEULA mentions a Data Processing Addendum (DPA) in Appendix 7. When do I need to implement this?**

You are required to have a DPA in place if your application (the "Covered Binary") processes any "User Data" that falls under the definition of "personal data" according to applicable laws like the GDPR or LGPD. Appendix 7.1 clarifies that in this scenario, the Licensor (you) is the "Processor" and the Licensee (your user) is the "Controller." The DPA must be presented to and agreed upon by the user. Its purpose is to contractually document your data handling practices, security measures (like SOC 2 Type 2 or equivalent), and the legal basis for any international data transfers, ensuring compliance with global privacy regulations. If your application is purely offline and processes no personal data, a DPA may not be necessary.

**18. The licenses refer to "legal safe harbors" for security research. What does a developer need to do to qualify for this protection?**

To qualify for the safe harbor (MMPEULA Clause 19.22 and MRSL-1.0 Appendix 10.2), a security researcher must act in good faith and adhere to a strict protocol:

* **Authorization**: The research must be conducted on your own deployments or on systems for which you have prior, written, verifiable authorization from the owner.
* **Responsible Conduct**: The testing must be done in a way that minimizes harm, avoids disrupting production systems, and does not exfiltrate or publish sensitive data.
* **Private Disclosure**: Findings must be reported privately to the designated security contact (e.g., contact@mitsuolabs.com, as specified in SECURITY.md) with enough detail to allow for reproduction and remediation.
* **Coordinated Disclosure**: The researcher must not publicly disclose the vulnerability until a mutually agreed-upon timeline has passed (typically 90 days), allowing the project to issue a patch.
Any deviation from this protocol (e.g., public disclosure on social-medias (including, but not limited to p2p), causing a system outage, exceeding the scope of authorization) voids the safe harbor protection.

19. Can you provide a concrete example of what a NOTICE file should contain?

A NOTICE file is a critical compliance artifact. For a hypothetical application named "QuantumLeap" that uses components licensed under MRSL-1.0, Apache 2.0, and MIT, a minimal NOTICE file would look like this:

================================================================================
QuantumLeap v1.0
Copyright (c) 2025 My-Quantum-Company LLC.

This product is licensed under the MitsuoLabs™ MASTER PROFESSIONAL AND
END USER LICENSE AGREEMENT (MMPEULA-1.0).
The source code is licensed under the MitsuoLabs™ Reciprocity and
Stewardship License (MRSL-1.0).

================================================================================

This product includes software developed by the following third parties:

1.  **Chrono-Core Engine**
    Copyright (c) 2024 The Chrono-Core Authors.
    Licensed under the Apache License, Version 2.0.
    A copy of the license is available in the LICENSES/APACHE-2.0.txt file.

2.  **Array-Utils Library**
    Copyright (c) 2023 Jane Doe.
    Licensed under the MIT License.
    A copy of the license is available in the LICENSES/MIT.txt file.

For the full text of these licenses and a complete SPDX inventory,
please see the bundled license documentation.
================================================================================


This example fulfills the core requirements: it identifies the main product's licenses and provides clear attribution and license information for its third-party dependencies.

**20. Why is there such a strong emphasis on CI/CD automation for compliance? Can't we just manage this manually?**

While manual compliance is theoretically possible, it is highly discouraged and operationally fragile. The framework's emphasis on automation (Axiom 37.11) is a risk-management strategy rooted in several realities of modern software development:

* **Human Error**: Manual license management is prone to errors—forgetting to update a version, using the wrong placeholder, or failing to include a NOTICE file. These small errors can have significant legal consequences.
* **Scalability**: In a project with multiple dependencies and frequent releases, manual compliance becomes untenable. Automation ensures that every single build, from a nightly test build to a major public release, is correctly and consistently licensed.
* **Auditability**: An automated, script-driven process creates a clear, auditable trail. In the event of a compliance audit, you can point to the exact script and configuration file that generated the licenses for a specific build, providing irrefutable proof of your process.
* **Legal Defensibility**: In a legal dispute, being able to demonstrate a robust, automated, and consistently applied compliance process is far more defensible than relying on ad-hoc manual procedures. It shows a proactive and diligent approach to legal obligations.

21. **What does it mean that the text of the licenses (both the FOSS-like MRSL-1.0 and the proprietary MMPEULA-1.0) are themselves licensed under the copyleft MRSL-1.0?**

This "meta-licensing" is a core philosophical and strategic feature of the framework. It means that the legal text of the licenses is treated like open-source code. You have the freedom to copy, modify, and distribute the license text itself, as long as you adhere to the terms of the MRSL-1.0.

* **This has several crucial implications**:

It Creates a "Legal Commons": The primary goal is to foster a "share-alike" ecosystem for legal innovation. If you take the MMPEULA or MRSL, adapt it, and create a new license, the MRSL-1.0's copyleft provision requires you to release your new, derivative license text under the same MRSL-1.0 terms. This prevents others from taking this legal work, making minor changes, and then claiming it as a proprietary, closed-source legal product. It ensures that innovation in legal drafting is shared back with the community.

* **It Prevents Predatory Commercialization**: A law firm or company cannot simply take these templates, rebrand them, and sell them as their own proprietary "EULA-as-a-Service" without also open-sourcing their modifications. It ensures the framework remains a tool for the community, not a product to be enclosed.

* **It Preserves Attribution and Provenance**: The MRSL-1.0 requires that you give credit to the original work. This ensures that the intellectual lineage of the license is maintained, and the original authors (MitsuoLabs™) are recognized, even in derivative works.

* **It Protects the Brand while Allowing Forks**: Section 30 of the MRSL-1.0 is critical here. While you are free to fork the license text, you cannot call your new version "MRSL" or the "MitsuoLabs License." You must give it a new name. This is a brilliant move that allows for legal innovation while preventing brand dilution and legal confusion in the marketplace.

* **It Encourages Academic Study and Activism**: By making the legal text itself FOSS, the framework invites legal scholars, activists, and developers to study, critique, and build upon it without fear of copyright infringement. As the README.md file notes, it turns the license into a "field of study" and a tool for "advocating for a more just digital world." It transforms even the highly restrictive MMPEULA into a transparent artifact that can be openly analyzed and debated.