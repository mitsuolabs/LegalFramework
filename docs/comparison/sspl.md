# MRSL-1.0 vs. The Server Side Public License (SSPL): A Comparative Legal & Strategic Analysis

## 1. Scholarly Overview of The Server Side Public License (SSPL)

The Server Side Public License (SSPL) is a source-available license created by MongoDB Inc. It is a modification of the GNU AGPL v3, but with an additional, much more demanding clause (Section 13) designed to address the "cloud provider problem." This problem refers to the situation where cloud companies offer open source databases as a service (DBaaS) for profit without contributing back to the projects they are monetizing.

Section 13 of the SSPL requires that anyone offering the software as a service must release not only the source code of the software itself (as AGPL would require) but also the source code of all supporting infrastructure—the management software, user interfaces, automation software, monitoring software, backup software, etc.—that is required to run the service. This obligation is so broad that the OSI has deemed it to be not an open source license.

## 2. Detailed Feature Comparison Matrix

| Domain | Feature | The Server Side Public License (SSPL) | MitsuoLabs Framework (MRSL-1.0) |
| :--- | :--- | :--- | :--- |
| **Reciprocity** | **Network Scope** | **Extreme:** If you offer the software as a service, you must release the source for your entire service stack under SSPL. | **Strong & Precise:** `Network Reciprocity` (**§6**) requires releasing the source of the modified Work and any `Integrated Works`, but not the entire operational stack. |
| **FOSS Compliance** | **No.** Considered source-available. The broad requirements of Section 13 are deemed to be a new kind of restriction. | **Yes (by Design):** MRSL-1.0 is architected to be fully FOSS-compliant. Part I is a standalone, OSI-approved license. |
| **Primary Goal** | **Strategic Intent** | **Anti-Competition:** Designed to make it economically and legally infeasible for cloud providers to offer a competing commercial service. | **Sustainability & Collaboration:** Designed to ensure reciprocity and foster a sustainable ecosystem through a combination of strong copyleft and incentivized partnership. |
| **Sustainability** | **Model** | **Defensive/Punitive:** Aims to force large commercial users to purchase a commercial license by making the free license too burdensome to comply with. | **Incentive-Based:** Aims to attract commercial users to become **Stewards** by offering valuable legal protections (like patent indemnification) in exchange for their commitment. |

## 3. Academic & Strategic Analysis

The SSPL and MRSL-1.0's Network Reciprocity clause both try to solve the SaaS loophole, but they do so with radically different philosophies and legal mechanics.

#### **SSPL: The Poison Pill**

The SSPL is not a tool for fostering a collaborative commons; it is a defensive business weapon. Its Section 13 is a "poison pill" designed to be so difficult and undesirable for a cloud provider to comply with that they are forced to negotiate a separate commercial license with the copyright holder instead. It is a strategy of coercion. By making the "free" license radioactive to its target (cloud providers), it creates a dual-licensing business model where the public license exists primarily to drive customers to the private one.

This strategy comes at the cost of being excluded from the FOSS ecosystem. The license is not open source, and its aggressive terms make it incompatible with almost every other license.

#### **MRSL-1.0: The Constitutional Mandate**

MRSL-1.0's `Network Reciprocity` clause (**§6**) is also strong, but it is precise, fair, and designed to be FOSS-compliant. It is a tool for ensuring reciprocity, not for killing competition.

1.  **Precision and Proportionality:** The SSPL demands the source code for the *entire service stack*. MRSL-1.0 demands the `Corresponding Source` for the *modified Work and any Integrated Works*. This is a crucial difference. It means you must share the application code, but not your unrelated deployment scripts, monitoring tools, or backup software. The obligation is proportional and focused on the software itself, not the entire business operation. This makes it a strong but reasonable copyleft provision, in the spirit of the AGPL.

2.  **A Path to Partnership, Not a Wall:** The SSPL is a wall intended to stop cloud providers. MRSL-1.0 provides a bridge. A cloud provider using MRSL-1.0 software has two choices: (a) comply with the fair and reasonable Network Reciprocity clause, or (b) become a **Steward**. By becoming a Steward, they accept the ethical covenant and commit to the project, and in return, they receive invaluable legal protections like **patent indemnification (§26.a)**. This transforms a potential adversary into a vested partner. It is a strategy of incentivization, not coercion.

3.  **FOSS-Native:** Because its reciprocity clause is fair and proportional, and because its ethical components are part of an optional, contractual rider, MRSL-1.0 remains fully FOSS-compliant. It achieves the goal of closing the SaaS loophole without sacrificing its identity as an open source license.

## 4. Conclusion

*   **Choose the SSPL** if your business model is based on dual-licensing and your primary goal is to use a source-available license as a tool to prevent large cloud providers from competing with you, thereby forcing them to purchase a commercial license. You are not building a FOSS project, but a commercial one with publicly visible source.

*   **Choose MRSL-1.0** when you want to build a **true FOSS project that is protected from the SaaS loophole**. Its `Network Reciprocity` clause ensures that those who build services with your work contribute back, while its innovative Stewardship model provides a powerful, positive incentive for commercial users to become partners, not just customers. It is a license for building a sustainable, collaborative, and FOSS-native ecosystem.
