# MRSL-1.0 vs. The SIL Open Font License (OFL): A Comparative Analysis

## 1. Scholarly Overview of The SIL Open Font License (OFL)

The SIL Open Font License (OFL) is the industry standard, FOSS-compliant license for fonts. Created by SIL International, it is recognized as a free license by the FSF and approved by the OSI.

The OFL is a weak copyleft license with specific terms tailored to the unique way fonts are used and distributed. Its key features are:

*   **Freedom to Use:** Fonts can be used freely in documents and artwork without the documents themselves becoming subject to the OFL.
*   **Freedom to Modify:** Users can modify the font for their own use.
*   **Share-Alike for Fonts:** If you distribute a modified font, it must be licensed under the OFL.
*   **No Selling Reserved Names:** You cannot sell the font on its own, and you must change the font's "Reserved Font Name" if you make significant modifications.
*   **Bundling:** Fonts can be bundled with software, but the software does not become subject to the OFL.

## 2. Detailed Feature Comparison Matrix

| Domain | Feature | The SIL Open Font License (OFL) | MitsuoLabs Framework (MRSL-1.0) |
| :--- | :--- | :--- | :--- |
| **Primary Target** | **Asset Type** | **Fonts:** Specifically designed for the unique legal and technical aspects of font distribution. | **Software & Associated Materials:** A holistic license covering code, documentation, and other assets as a single "Work." |
| **Reciprocity** | **Copyleft Scope** | **Weak (Font-Level):** Derivative fonts must be licensed under OFL. Does not apply to documents or software bundling the font. | **Strong (Work-Level):** If a font is part of an `Integrated Work`, the entire Work must be licensed under MRSL-1.0. |
| **Bundling** | **Effect on Software** | **None:** A font can be bundled with proprietary software without affecting the software's license. | **Triggers Copyleft:** If a font is an integral part of an `Integrated Work`, the entire work is subject to MRSL-1.0 copyleft (**§4**). |
| **Governance** | **Ethical Rules** | **No.** Ethically neutral. | **Yes (Optional Contract for Stewards):** The Ethical Use Covenant (**§25**) applies to how a Steward uses their contributions, including any fonts they contribute to The Work. |

## 3. Academic & Strategic Analysis

The OFL is a specialized tool for a specialized job. MRSL-1.0 is a general-purpose framework for building entire ecosystems. The choice between them for a font depends on the font's relationship to the broader project.

#### **OFL: The Perfect Font License**

The OFL is successful because it understands how fonts are used. It knows that a font is a component used to *create* other things (documents, websites, software UIs). The license is carefully crafted to ensure that the font itself and its derivatives remain free, without encumbering the works created with it. This allows for maximum adoption. A company can use an OFL font in their proprietary software without any fear that their software will become copyleft.

Its specialization is also its limitation. It is not designed for source code, and its copyleft does not extend beyond the font itself.

#### **MRSL-1.0: The Unified Work Approach**

MRSL-1.0 could be used for a font, but it would have a very different and much stronger effect than the OFL. If a font is released as part of a larger MRSL-1.0 "Work" (e.g., a game that includes a unique, custom-made font), the font becomes part of the unified whole.

1.  **Holistic Copyleft:** Under MRSL-1.0, the font is not a separate, modular component. It is an integral part of the Work. If a third party were to take that game, modify the font, and distribute the result, the entire `Integrated Work` (the game) would need to be released under MRSL-1.0. This is a far stronger copyleft than the OFL provides.

2.  **Unified Governance:** The `Community Bill of Rights` (**§14**) and the **Stewardship** model would apply to the font just as it does to the code. A significant contribution to the font could qualify someone for Stewardship, giving them a voice in the project's governance and access to legal protections.

## 4. Conclusion

*   **Choose the OFL** when you are releasing a **standalone font**. It is the industry standard for a reason. It provides the perfect balance of freedom, reciprocity, and ease of use for a component that is meant to be widely adopted and used in a variety of other works, both open and proprietary.

*   **Choose MRSL-1.0** for a font only when that font is an **inseparable part of a larger, integrated software project** that you are developing under the MRSL-1.0 framework. In this scenario, the font is not just a font; it is a feature of the Work, and it should be governed by the same powerful, holistic rules as the rest of the code and assets. For all general-purpose font releases, the OFL is the superior choice.
