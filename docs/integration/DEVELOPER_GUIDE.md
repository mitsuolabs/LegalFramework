# A Developer's Guide to the Integrated Framework (MRSL + MMPEULA)

## 1. The Dual-License Strategy: The Professional Open-Source Model

This guide explains how to use the **MitsuoLabs™ Reciprocity and Stewardship License (MRSL-1.0)** and the **MitsuoLabs™ Master Professional and End User License Agreement (MMPEULA-1.0)** together as a single, integrated framework. This is the model used by some of the most successful open-source companies in the world, like Red Hat.

The core principle is the legal and practical distinction between the **source code** (the blueprint) and the **compiled binary** (the product).

1.  **The Source Code is Free:** Governed by the MRSL-1.0, the source code is perpetually and irrevocably open. Anyone can study it, modify it, compile it, and share their modifications. This fosters a vibrant community of developers and ensures the technology can never be fully locked away.

2.  **The Official Binary is a Commercial Product:** Governed by the MMPEULA-1.0, the official binary that you compile and distribute is a professional, commercial product. Users of your binary are bound by the strict, protective terms of the MMPEULA, creating a stable and predictable commercial environment.

This model allows you to build a business around your open-source project by selling convenience, support, and a certified, official build, without ever compromising on the freedom of the underlying source code.

---

## Part I: Structuring Your Dual-License Project

Here is a step-by-step guide to structuring your repository and distribution for the dual-license model.

### In Your Source Code Repository (e.g., on GitHub)

1.  **License the Source Code under MRSL-1.0:**
    *   Place the full text of `mrsl-1.0.txt` into a file named `LICENSE` in your project's root directory.
    *   Update the placeholders in the `LICENSE` file with your project's information.
    *   This makes it unambiguously clear that all source code in the repository is FOSS-compatible.

2.  **Include the MMPEULA-1.0 Text:**
    *   Create a directory in your repository, for example, `legal/` or `eula/`.
    *   Place the full text of `mmpeula-1.0.html` inside that directory.
    *   This ensures that the EULA text is available within the source repository, but it does **not** govern the source code itself.

3.  **Create a Clear `README.md`:**
    *   Your project's `README.md` file must clearly explain the dual-license model to your users.
    *   It should state that the source code is licensed under MRSL-1.0 and that the official binary distributions are licensed under the MMPEULA-1.0.

### For Your Binary Distribution (e.g., in Your Installer)

1.  **Do Not Include the MRSL-1.0 Text:** Your installer or binary package should not contain the MRSL-1.0 `LICENSE` file. This avoids confusion. The user of the binary is not being granted rights under the MRSL-1.0 for the binary itself.

2.  **Implement the MMPEULA-1.0 Acceptance Protocol:**
    *   During installation, you must display the full text of the MMPEULA-1.0 to the user.
    *   You must implement the **MitsuoLabs™ Acceptance Protocol (MAP)** as described in the `docs/mmpeula/DEVELOPER_GUIDE.md`:
        *   The 300-second mandatory review timer.
        *   The seven-point affirmation checkbox sequence.
        *   The generation of a Cryptographic Proof of Consent.

---

## Part II: The Legal and Commercial Logic

### Why does this work?

This model is legally robust because you are offering two different things under two different sets of terms:

*   You are offering the **source code** to the world under the FOSS-compatible MRSL-1.0.
*   You are offering a **separate product** (the official, compiled binary) to a specific user under the commercial MMPEULA-1.0.

A user's rights depend on what they are using. If they download your binary, they are bound by the MMPEULA. If they clone your repository and compile the source code themselves, they are using the source under the MRSL-1.0 and are bound by its terms (including the strong-copyleft provisions).

### The "Right to Fork" as a Safety Valve

The MMPEULA-1.0 is intentionally strict. A user might not want to agree to its terms. The dual-license model provides them with a powerful alternative: the **right to fork**.

If a user objects to the MMPEULA, they are always free to take the MRSL-1.0 licensed source code, compile it themselves, and even create and distribute their own competing binary (provided they also comply with the MRSL-1.0's copyleft requirements).

This is a critical feature, not a bug. It ensures that the technology can never be completely controlled by you or any single entity, which is the core promise of open source. It provides a fundamental check on your power as the licensor and is a key reason why communities can trust projects built on this framework.

## Part III: Communicating Your Model

Clarity is essential for a successful dual-license strategy. You must be transparent with your community about how your project is licensed.

*   **Use your `README.md` effectively:** Clearly explain the difference between the source license and the binary EULA.
*   **Create a `LICENSE_FAQ.md`:** Answer common questions like "Is this project open source?" (Yes, the source is FOSS-compatible under MRSL-1.0), "What are the restrictions on the official binary?" (They are governed by the MMPEULA-1.0), and "Can I avoid the EULA?" (Yes, by compiling the source yourself).

## Conclusion

The integrated MRSL + MMPEULA framework is the definitive legal architecture for building a professional, sustainable business on an open-source foundation. It allows you to maintain full commercial control over your official product while simultaneously contributing to and benefiting from the FOSS ecosystem.

It provides:
*   **For developers:** The freedom to innovate with open source.
*   **For your business:** The protection of a rock-solid commercial EULA.
*   **For your users:** The choice between a commercially supported product and the freedom to build their own.

This is the model for serious, long-term open-source stewardship.
