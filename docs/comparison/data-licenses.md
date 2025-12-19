# MRSL-1.0 vs. Data Licenses (ODbL & CDLA-Sharing): A Comparative Legal & Strategic Analysis

## 1. Scholarly Overview of Data Licenses

While most FOSS licenses are designed for source code, a specific class of licenses has emerged to govern the use of data, datasets, and databases. The Open Database License (ODbL) and the Community Data License Agreement - Sharing (CDLA-Sharing) are two of the most prominent.

*   **Open Database License (ODbL):** Published by Open Data Commons, ODbL is a "Share-Alike" (copyleft) license for databases. It allows users to freely use, modify, and share the database, but if they publicly use a derivative database, they must also share that derivative under ODbL. The license separates the rights to the database itself from the rights to the contents (which can be licensed separately) and the rights to a "Produced Work" (e.g., a visualization generated from the data), which is not covered by the license's copyleft.

*   **CDLA-Sharing:** Published by the Linux Foundation, CDLA-Sharing is a copyleft license specifically for data, particularly data used for AI/ML training. If you modify and redistribute the data, you must share your modifications. If you use the data to train an AI model and then distribute that model, you are encouraged, but not required, to share the model. The primary obligation is on the sharing of the data itself.

MRSL-1.0, while primarily a software license, includes explicit provisions for "associated materials," which include "model weights, datasets bundled with the project, etc." (**§1**), making it applicable to data in the context of a software project.

## 2. Detailed Feature Comparison Matrix

| Domain | Feature | ODbL & CDLA-Sharing | MitsuoLabs Framework (MRSL-1.0) |
| :--- | :--- | :--- | :--- |
| **Primary Target** | **Asset Type** | **Databases (ODbL) & Data (CDLA-Sharing):** Specifically drafted for structured and unstructured data. | **Software & Associated Materials:** Covers data when it is bundled as part of a larger software Work (**§1**). |
| **Reciprocity** | **Copyleft Trigger** | **Derivative Database (ODbL) or Modified Data (CDLA-Sharing):** Triggered by sharing modified versions of the data itself. | **Integrated Work:** Triggered by conveying an `Integrated Work` that includes the data. If the data is part of the Work, the entire application falls under MRSL copyleft (**§4**). |
| **Scope** | **Code vs. Data** | **Separates Data from Code:** These licenses govern the data layer only. The software that accesses the data can be under any license. | **Unifies Code and Data:** When data is part of The Work, it is governed by the same terms as the code, creating a single, unified legal entity. |
| **AI Provisions**| **Model Training** | **Permissive (CDLA-Sharing):** Encourages, but does not require, sharing of models trained on the data. | **Attribution & Disclosure:** Requires attribution for AI systems trained on The Work and disclosure of its MRSL-licensed origins (**§11**). The model itself would be part of the `Corresponding Source` if the Work is conveyed. |
| **Ethical Use** | **Provisions** | **No.** Ethically neutral. | **Yes (Optional Contract for Stewards):** The Ethical Use Covenant (**§25**) applies to how a Steward uses their contributions, including any data they contribute to The Work. |

## 3. Academic & Strategic Analysis

Data licenses like ODbL and CDLA-Sharing are designed to solve the problem of data sharing in isolation. MRSL-1.0 provides a solution for projects where code and data are inextricably linked parts of a single, holistic "Work."

#### **ODbL & CDLA-Sharing: The Data-Centric Approach**

The strength of these licenses is their specificity. They are purpose-built for data. They understand that a user might want to access a copyleft database with proprietary analytics software, and they allow for this by creating a clear legal separation between the data layer and the application layer. This is their primary strategic function: to encourage the growth of open data by providing a clear, safe harbor for proprietary software that needs to consume it.

Their weakness is that they do not and cannot govern the software itself. This creates a multi-license compliance burden for any project that involves both open code and open data, and it does not provide a holistic governance or sustainability model for the project as a whole.

#### **MRSL-1.0: The Unified Work Approach**

MRSL-1.0's strategy is to treat a project as a single, unified entity. When a dataset is "bundled with the project," it becomes part of "The Work" (**§1**). This has profound implications:

1.  **Holistic Copyleft:** The reciprocity of MRSL-1.0 (**§4**) applies to the entire `Integrated Work`. If an application is built on and distributed with an MRSL-licensed dataset, the entire application must be licensed under MRSL-1.0. This is a much stronger form of copyleft than what ODbL or CDLA-Sharing provide, as it extends from the data to the code that uses it. This prevents the scenario where a proprietary application becomes the only valuable way to access an open dataset.

2.  **Unified Governance and Ethics:** By treating data as part of The Work, the `Community Bill of Rights` (**§14**) and the `Ethical Use Covenant` (**§25**) automatically apply to how that data is governed and used by Stewards. For example, a Steward would be prohibited from using a bundled dataset as part of a mass surveillance system. This provides a level of ethical and governance protection for data that data-only licenses do not.

3.  **Incentivized Stewardship for Data:** The Stewardship model applies to the entire Work. A company that makes a critical improvement to a dataset within an MRSL-1.0 project can become a Steward, gaining patent indemnification and other protections. This creates a direct incentive to contribute to and curate high-quality open datasets within the MRSL ecosystem.

## 4. Conclusion

*   **Choose ODbL or CDLA-Sharing** when you want to release a **standalone dataset or database** and your primary goal is to ensure that derivatives of the *data itself* remain open. You want to allow any software, including proprietary software, to use and access this data with minimal restrictions on the software.

*   **Choose MRSL-1.0** when you are building a **project where code and data are tightly integrated**, such as an AI/ML application. You want a single, unified license to govern the entire project, ensuring that the value created by the combination of code and data remains within the commons. MRSL-1.0 provides a more holistic, powerful, and sustainable framework for projects that are more than just a dataset.
