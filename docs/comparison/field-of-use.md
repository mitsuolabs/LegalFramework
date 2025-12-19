# MRSL-1.0 vs. Field-of-Use Restricted Licenses: A Comparative Analysis

## 1. Scholarly Overview of Field-of-Use Restricted Licenses

A "Field-of-Use" restricted license is any license that prohibits the use of the software in certain business sectors, for certain purposes, or by certain types of users. Common examples include licenses with "non-commercial" clauses, "non-military" clauses, or clauses that forbid use by police departments.

These licenses are, by definition, not Open Source licenses according to the Open Source Initiative (OSI), whose Definition explicitly states that a license "must not restrict anyone from making use of the program in a specific field of endeavor" (Clause 6). Therefore, these are properly categorized as "source available" licenses.

The goal of such licenses is to allow for the free sharing of source code while preventing the software from being used for purposes the author finds objectionable.

## 2. Detailed Feature Comparison Matrix

| Domain | Feature | Field-of-Use Restricted License | MitsuoLabs Framework (MRSL-1.0) |
| :--- | :--- | :--- | :--- |
| **FOSS Compliance** | **No.** The field-of-use restriction is a direct violation of the Open Source Definition. | **Yes (by Design):** The license is architected with a two-part structure. Part I is a fully FOSS-compliant public license with no field-of-use restrictions. |
| **Ethical Scope** | **Restriction Method** | **Universal Prohibition:** A specific field of endeavor is prohibited for *all users* of the software. | **Conditional & Opt-In:** The Ethical Use Covenant (**§25**), which contains use restrictions, applies *only* to Stewards who voluntarily opt-in to gain additional rights. |
| **Enforcement** | **Breach Consequence** | **License Termination:** Use of the software in the prohibited field constitutes copyright infringement and terminates the license. | **Stewardship Termination:** A breach of the Ethical Use Covenant terminates only the *advanced rights* of the Steward (**§28**). Core FOSS rights under Part I remain. |
| **Sustainability** | **Model** | **None.** Relies on the appeal of its moral stance to attract like-minded contributors. | **Incentivized Stewardship:** The Stewardship model provides a direct economic and legal incentive (e.g., patent indemnification) for committing to the ethical principles, creating a sustainable growth model. |

## 3. Academic & Strategic Analysis

Field-of-Use licenses and MRSL-1.0 represent two different answers to the question of how to control the application of source-available software.

#### **Field-of-Use Licenses: The Direct Ban**

The strategy of a Field-of-Use license is simple and direct: identify a use you find objectionable and ban it in the license text. This provides moral clarity for the author and anyone who shares their convictions. If you don't want your software used for military applications, you simply say so.

The cost of this directness is exclusion from the mainstream FOSS ecosystem. The project cannot be called "Open Source," and the software cannot be integrated into many other FOSS projects or used by companies with strict OSI-approved license policies. It creates a walled garden of source-available code, separated from the larger open source commons.

#### **MRSL-1.0: The Constitutional, Two-Tier System**

MRSL-1.0 is engineered to provide powerful ethical controls without violating the principles of Open Source. It achieves this by creating a two-tier system of rights and obligations.

1.  **Tier 1: Universal FOSS Rights (Part I):** The core public license in Part I is a pure, OSI-compliant FOSS license. It grants everyone the right to use the software for any purpose. There are no field-of-use restrictions whatsoever in this part. This ensures that the project remains fully part of the open source ecosystem.

2.  **Tier 2: The Steward's Bargain (Part II):** The use restrictions are contained in the `Ethical Use Covenant` (**§25**) within the optional **Stewardship Rider**. This is not a universal ban. It is a specific set of contractual obligations that a user *voluntarily accepts* to become a **Steward**. In exchange for accepting these restrictions on their own use, the Steward gains access to powerful legal and financial benefits, such as **patent indemnification (§26.a)**.

This is a fundamentally different legal and social construct. The ethical restrictions are not a ban imposed on the public, but a promise made by a project's most invested partners in exchange for valuable considerations. It is a contract, not a sermon.

## 4. Conclusion

*   **Choose a Field-of-Use Restricted License** when your primary goal is to prevent your software from being used for a specific purpose, and you are willing to accept that your project will not be considered "Open Source" and will be excluded from the mainstream FOSS ecosystem.

*   **Choose MRSL-1.0** when you want to build a **major, FOSS-compliant project that also has strong, enforceable ethical guidelines**. MRSL-1.0's innovative two-part structure allows it to maintain full OSI compliance while creating a binding ethical framework for its most important contributors (Stewards). It offers a pragmatic and powerful way to foster responsible use without sacrificing the benefits of being a true open source project.
