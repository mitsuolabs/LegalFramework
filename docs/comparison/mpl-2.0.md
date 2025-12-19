# MRSL-1.0 vs. Mozilla Public License 2.0 (MPL-2.0): A Comparative Legal & Strategic Analysis

## 1. Scholarly Overview of MPL-2.0

The Mozilla Public License 2.0 is a sophisticated "weak copyleft" license, occupying a legal space between permissive licenses (like MIT/Apache) and strong copyleft licenses (like the GPL family). Drafted by the Mozilla Foundation, it is engineered for pragmatism and is considered a cornerstone of modern open-source licensing.

Its defining characteristic is **file-level copyleft**. The reciprocity (copyleft) obligations of the MPL-2.0 apply only to modifications of the files originally licensed under MPL-2.0. These modified files must remain under the MPL-2.0 and their source must be made available. However, these files can be aggregated into a "Larger Work" with code licensed under different terms (including proprietary code) without requiring the entire Larger Work to adopt the MPL-2.0 license. This makes it a highly attractive license for commercial entities wishing to use and contribute to open-source components without risking their proprietary intellectual property.

## 2. Detailed Feature Comparison Matrix

| Domain | Feature | Mozilla Public License 2.0 (MPL-2.0) | MitsuoLabs Framework (MRSL-1.0) |
| :--- | :--- | :--- | :--- |
| **Reciprocity** | **Copyleft Scope** | **File-Level:** Modifications to MPL-licensed files must be MPL. New files in a Larger Work can be proprietary. | **Work-Level (Strong):** An "Integrated Work" (application) must be licensed entirely under MRSL-1.0 (**§4**). A "System Work" (library) allows linking from other licenses (**§5**). |
| | **Network Reciprocity** | **No.** The "SaaS loophole" remains open. Distribution is not triggered by providing network services. | **Yes (AGPL-style):** Running a modified version as a network service requires providing Corresponding Source to users (**§6**). |
| **IP Grants** | **Patent Grant** | **Explicit & Defensive:** Grants a patent license from contributors. This grant terminates if you sue any contributor for patent infringement ("defensive termination"). | **Explicit & Enhanced for Stewards:** Provides a core patent grant (**§12**). **Stewards** additionally receive patent *indemnification* from the licensor, a significant legal protection (**§26.a**). |
| | **Trademark Grant** | **No.** Explicitly does not grant trademark rights. | **No.** Explicitly does not grant trademark rights, with detailed rules on attribution vs. endorsement (**§10, §30**). |
| **Interoperability** | **GPL Family Compatibility** | **Yes, via Exhibit B:** Allows a distributor to re-license the work under a GPL-family license, creating a combined work under GPL terms. | **Yes, via Specific Exception:** Explicitly permits combining and distributing under a GPL-family license, provided MRSL source is also available and clearly marked (**§29**). |
| | **Permissive Linking** | **Yes.** A core feature, allowing combination with proprietary code into a "Larger Work". | **Yes (for System Works):** A "System Work" is designed to be linked by applications under other licenses, including proprietary ones (**§5**). |
| **Governance** | **Community Rights** | **Implicit.** Relies on community norms. No explicit, legally codified rights for the user community. | **Explicit & Contractual:** A "Community Bill of Rights" (**§14**), a "Right of Repair" for security vulnerabilities (**§17**), and the "Alexandria Clause" for preservation (**§19**). |
| | **Ethical Governance** | **No.** The license is ethically neutral by design. | **Yes (Opt-in Contract):** Part II provides an extensive, legally-specific **Ethical Use Covenant** that Stewards voluntarily accept in exchange for advanced rights (**§25, §26**). |
| **Risk & Liability** | **Indemnification** | **No.** Provides no indemnification to users or contributors. | **Yes (for Stewards):** Stewards receive patent indemnification from the licensor and give/receive mutual indemnification for their contributions (**§26.a, §26.c**). |
| | **Anti-Tivoization** | **No.** Does not address hardware lock-down preventing users from running modified code. | **Yes.** Explicitly prohibits Tivoization, requiring the provision of keys and information to run modified versions on User Products (**§8**). |
| **Modern Tech** | **AI & Blockchain** | **Not explicitly addressed.** Governed by general copyright and patent clauses. | **Explicitly Addressed:** Contains specific clauses for AI systems (**§11**) and Digital Assets/Blockchain (**§13**), providing legal clarity for modern technologies. |
| | **User Data Rights** | **No.** Does not impose data portability or erasure rights on service operators. | **Yes.** Service operators using the Work must provide users with a right to data export and erasure (**§18**). |

## 3. Academic & Strategic Analysis

The choice between MPL-2.0 and MRSL-1.0 is a fundamental strategic decision about the nature of the software ecosystem one intends to build.

#### **MPL-2.0: The Corporate-Friendly Component License**

MPL-2.0 is an act of legal genius for fostering collaboration on shared *components*. Its file-level copyleft is a minimal-friction invitation for corporations to use, modify, and contribute back to a specific file without fear of their broader proprietary codebase becoming "infected" by copyleft obligations. It is the perfect license for a browser engine (Gecko), a library, or a tool that is meant to be a piece of a larger, potentially closed-source puzzle.

However, this very feature makes it less suitable for building a self-sustaining *platform*. A large cloud provider can take MPL-2.0 code, integrate it deeply into a proprietary SaaS offering, and never release the vast majority of their value-adding code. The community's work subsidizes the proprietary platform, but the platform's core innovations are not reciprocated back to the community.

#### **MRSL-1.0: The Sustainable Ecosystem License**

MRSL-1.0 is architected to solve this exact problem. It is designed not for components, but for *ecosystems*.

1.  **Strong Reciprocity and Network Defense:** By adopting a strong, work-level copyleft for `Integrated Works` (**§4**) and an AGPL-style `Network Reciprocity` clause (**§6**), MRSL-1.0 ensures that an entire application ecosystem, whether distributed or offered as a service, remains within the commons. It compels reciprocity from all who build upon and derive value from the core platform.

2.  **Incentivizing High-Trust Contribution:** The masterstroke of the MRSL framework is the **Stewardship Rider (Part II)**. This is not a simple ethical add-on; it is a distinct, optional contract that creates a two-tiered system of participation.
    *   **Standard Users/Contributors (Part I):** Enjoy full FOSS rights, comparable to any strong copyleft license.
    *   **Stewards (Part II):** Voluntarily accept the strict **Ethical Use Covenant (§25)**. In exchange for this higher bar of conduct, they receive concrete, economically valuable legal protections unavailable in any standard FOSS license: **patent indemnification, mutual indemnification, and formalized governance rights (§26)**.
    This creates a powerful incentive for corporations and dedicated individuals to become Stewards. They gain a level of legal protection that radically de-risks their participation, fostering a core group of high-trust, long-term contributors. MPL-2.0 has no equivalent mechanism to reward and protect its most dedicated community members.

3.  **Engineered Interoperability:** MRSL-1.0's compatibility clause (**§29**) is a pragmatic acknowledgment of the GPL's dominance. It provides a one-way "escape hatch" allowing an MRSL work to be subsumed into a GPL-licensed project. This is a deliberate strategic choice to prevent the ecosystem from being isolated. It allows MRSL projects to "draft" behind the massive GPL ecosystem, while still providing compelling reasons (Stewardship) for projects to remain natively MRSL-licensed. MPL-2.0's Exhibit B provides a similar function but is structured as a choice for the distributor, whereas MRSL's is an explicit, built-in compatibility rule.

## 4. Conclusion

*   **Choose MPL-2.0** when your strategic goal is to create a best-in-class **component** and maximize its adoption within corporate and proprietary environments, accepting that it may be used in closed-source SaaS products without full reciprocity.

*   **Choose MRSL-1.0** when your strategic goal is to build a durable, self-sustaining **platform or ecosystem**. It provides stronger reciprocity to protect against free-riding by cloud providers, and its novel Stewardship model creates a powerful incentive structure to attract and retain a core of legally-protected, ethically-aligned, high-value contributors. It is a license for building movements, not just modules.
