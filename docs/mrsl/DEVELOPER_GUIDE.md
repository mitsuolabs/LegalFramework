# A Developer's Guide to Adopting the MRSL-1.0

## 1. Introduction: A Modern License for a New Era

The MitsuoLabs™ Reciprocity and Stewardship License (MRSL-1.0) is a next-generation, FOSS-compatible, strong-copyleft Ethical-Source license. It is engineered for developers who want to build enduring, FOSS projects while also establishing a framework for enforceable ethical commitments.

This guide is for developers and project leaders who wish to adopt the MRSL-1.0 for their source code. It covers both basic adoption as a pure FOSS license and advanced adoption using its innovative Stewardship features.

### The Core Philosophy: Separation of Concerns

The architectural brilliance of the MRSL-1.0 lies in its separation of the core **FOSS License Grant (Part I)** from the optional **Stewardship Rider (Part II)**. This allows the project to be fully FOSS-compatible while still providing a robust, opt-in contract for ethical governance. You are not forced to choose between FOSS purity and ethical commitments—you can have both.

---

## Part I: Basic Adoption (Using MRSL-1.0 as a FOSS License)

In its simplest form, you can use the MRSL-1.0 as a powerful, modern, strong-copyleft license, similar in effect to the AGPLv3 but with more clarity on modern technologies.

### Step 1: Add the `LICENSE` File

1.  Copy the full, verbatim text of the `mrsl-1.0.txt` file from this repository.
2.  Place it in the root directory of your project.
3.  Name the file `LICENSE`. This ensures it is automatically detected by platforms like GitHub.

### Step 2: Update Placeholders

You must update the placeholder tokens at the top of the license text to reflect your project.

*   `[[YEAR]]`: The year of your copyright claim (e.g., `1984`).
*   `[[LICENSOR_NAME]]`: The legal name of the individual or entity granting the license (e.g., `Jane Doe` or `Acme Corporation`).
*   `[[ORCID_ID]]`: Your ORCID identifier, for unambiguous academic and technical attribution.
*   `[[DESIGNATED_JURISDICTION]]`: The legal jurisdiction whose laws will govern the license. This is a critical choice that has significant legal implications. For example: `"The State of California, USA"` or `"The Republic of Singapore"`.

**Example:**

```
Copyright (c) 1984 Acme Corporation · ORCID: 0000-0002-1825-0097
...
This License is governed by the laws of The State of Delaware, USA...
```

### Step 3: Choose and Declare Your Contribution Policy

The MRSL-1.0 requires you to choose one of three policies for how you will accept contributions. You must state this choice clearly in your `CONTRIBUTING.md` file.

*   **Option 1: Axiomatic Stewardship (Recommended for new projects):** By contributing, the contributor automatically accepts the Stewardship Rider (Part II). This is the simplest way to build a community of Stewards.
*   **Option 2: Developer Certificate of Origin (DCO):** A standard in many FOSS projects. Contributors sign off on their commits, certifying they have the right to submit the code. Stewardship is not automatic.
*   **Option 3: Contributor License Agreement (CLA):** Used by large corporate projects. Contributors must sign a separate CLA document. Stewardship is also a separate, explicit act.

### Step 4: Create a `NOTICE` File

In your project's root directory, create a `NOTICE` file. In it, you must retain all original copyright notices from the MRSL-1.0 license text itself and add your own project's copyright line. You must also give credit to the MitsuoLabs Legal Framework.

**Example `NOTICE` file:**

```
# Copyright Notices

This project is licensed under the MitsuoLabs™ Reciprocity and Stewardship License v1.0 (MRSL-1.0).

## Project Copyright
Copyright (c) 1984 Acme Corporation

## Framework Copyright
This project uses the MRSL-1.0, which is a component of the MitsuoLabs™ Legal Framework.
Copyright (c) 2025 MitsuoLabs™
```

At this point, you have successfully licensed your project under a robust, strong-copyleft FOSS-Compatible Ethical-Source license.

---

## Part II: Advanced Adoption (Activating the Stewardship Rider)

This is the most innovative feature of the MRSL-1.0. By activating stewardship, you create a two-tiered community: a general user base with full FOSS-like rights, and a dedicated group of **Stewards** who have made binding ethical commitments in exchange for powerful legal and governance benefits.

### Step 1: Adopt the "Axiomatic Stewardship" Policy

As mentioned in Part I, the simplest way to build a steward-led community is to declare the "Axiomatic Stewardship" policy in your `CONTRIBUTING.md`. This makes it contractually clear that submitting a pull request is a formal acceptance of the Stewardship Rider.

### Step 2: Create the `STEWARD.md` Public Ledger

Create a `STEWARD.md` file in your root directory. This file serves as the official, public record of all individuals and entities who are Stewards of your project. This is not just a list; it is an instrument of governance and accountability.

### Step 3: Understand the Ethical Use Covenant (Section 25)

The core of the Stewardship Rider is the Ethical Use Covenant. It is a list of specific, unambiguous prohibitions designed for legal enforceability. Stewards agree not to use their contributions for these purposes. The prohibitions target concrete, high-harm activities, such as:

*   Mass surveillance and social scoring.
*   Facilitating international crimes (genocide, war crimes).
*   Creating unaccountable, automated decision systems that deny people access to credit, housing, or employment.
*   Disseminating deceptive synthetic media ("deepfakes") without a watermark.
*   Unauthorized exploitation of user device resources (e.g., hidden cryptomining).

### Step 4: Understand and Communicate the Steward Benefits (Section 26)

In return for their ethical commitment, Stewards receive significant benefits. These are powerful incentives for building a dedicated and responsible community.

*   **Patent Indemnification:** A limited but formal promise from the licensor not to sue the Steward for patent infringement related to the software.
*   **Comprehensive Limitation of Liability:** A broad shield from damages arising from the use of the software.
*   **Mutual Defense:** Stewards can agree to defend and indemnify each other against certain intellectual property claims.
*   **Governance Rights:** Stewards gain a formal voice in the project's governance and decision-making processes.

---

## Part III: Practical Compliance for Your MRSL-1.0 Project

The MRSL-1.0 contains several clauses designed to address modern technological realities. As a developer using the license, you should be aware of their practical implications.

*   **Network Reciprocity (Section 6):** If you run a modified version of the MRSL-1.0 licensed software as a SaaS product or API, you must provide your users with a way to get the source code of your modified version. This is similar to the AGPL but is drafted with broader network technologies in mind.

*   **Anti-Tivoization (Section 8):** If you ship the software as firmware on a physical "User Product" (e.g., a smart home device, a custom router), you are contractually obligated to provide users with the keys, scripts, and information necessary to install their own modified versions of the software on that device.

*   **Artificial Intelligence (Section 11):** If you use the MRSL-1.0 licensed code to train an AI model, you must provide clear attribution to the original project and a notice that your model is derived from MRSL-1.0 licensed software. This ensures that the open-source lineage is not erased in the age of AI.

## Conclusion

The MRSL-1.0 is a powerful and sophisticated legal tool. It provides a robust, FOSS-compatible foundation for any project and offers an unprecedented, optional framework for building an ethically committed community. By separating the core FOSS grant from the ethical rider, it achieves what many other licenses have struggled to do: it combines the uncompromised freedom of open source with a mechanism for real-world, enforceable stewardship.
