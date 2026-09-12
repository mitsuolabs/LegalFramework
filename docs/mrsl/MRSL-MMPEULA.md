# THE DUAL-LICENSE FRAMEWORK: MRSL-1.0 + MMPEULA-1.0

This is the flagship licensing model of the MitsuoLabs™ ecosystem. It combines a strong copyleft, FOSS-Compatible ethical-source license for the source code with a robust, commercial-grade EULA for the official binaries. This dual-license strategy creates a powerful, flexible, and sustainable framework for stewarding a FOSS project while building a commercial enterprise around it.

## The Core Strategy: FOSS Freedom, Commercial Stability

This model creates two distinct but complementary legal paths for your software:

1.  **The Source Code (Licensed under MRSL-1.0):** The complete source code is licensed under the MitsuoLabs™ Reciprocity and Stewardship License (MRSL-1.0). This ensures it remains perpetually FOSS/FOSS-Compatible. It guarantees the four fundamental freedoms for all users and developers who interact with the source: the right to use, study, modify, and distribute. The MRSL-1.0's strong copyleft provisions ensure that derivative works also remain free.

2.  **The Binaries (Licensed under MMPEULA-1.0):** The official, pre-compiled binaries are distributed exclusively under the MitsuoLabs™ MASTER PROFESSIONAL AND END USER LICENSE AGREEMENT (MMPEULA-1.0). This is a commercial EULA that governs the use of the ready-to-run software. It provides legal certainty, allocates risk, and establishes a clear commercial relationship with end-users.

This model is **not tivoization**. The FOSS license for the source code (MRSL-1.0) explicitly protects the user's right to modify the software and run their modified versions on their own hardware (MRSL-1.0, Section 8). The MMPEULA-1.0 only applies to the official binaries provided by the licensor.

### Key Advantages of the Dual-License Model

-   **Best of Both Worlds:** You get the community engagement, trust, and transparency of FOSS, combined with the legal protection and commercial viability of a professional EULA.
-   **Sustainable FOSS:** It provides a clear path to monetize a FOSS-Compatible project by selling commercially-licensed binaries, support, and services, funding further development.
-   **Ethical Stewardship:** By using the MRSL-1.0 for the source, you can invite contributors to become "Stewards," creating a community committed to the Ethical Use Covenant and providing them with enhanced legal protections (indemnity, patent grants).
-   **Legal Robustness:** The MMPEULA-1.0, with its mandatory Acceptance Protocol, is designed to be highly enforceable in a professional B2B context, protecting the licensor from liability and unauthorized use of the commercial product.

## How to Implement the Dual-License Model

1.  **License Your Repository Correctly:**
    *   Place the full text of `mrsl-1.0.txt` in your project's root directory as `LICENSE`.
    *   Place the full text of `mmpeula-1.0.txt` in a separate, clearly named file, such as `BINARY-EULA.md`.

2.  **Update Your README.md:** Your project's `README.md` file must clearly explain the licensing structure. This is essential for user and contributor clarity.
    ```markdown
    ## Licensing

    The source code of this project is licensed under the **MitsuoLabs™ Reciprocity and Stewardship License (MRSL-1.0)**, available in the `LICENSE` file.

    Official binaries are distributed exclusively under the **MitsuoLabs™ MASTER PROFESSIONAL AND END USER LICENSE AGREEMENT (MMPEULA-1.0)**, available in the `BINARY-EULA.md` file. By downloading and using the official binaries, you agree to the terms of the MMPEULA-1.0. You are always free to build the software from source under the terms of the MRSL-1.0.
    ```

3.  **Implement the Acceptance Protocol:** For all official binary distributions, you **must** implement the **MitsuoLabs™ Acceptance Protocol** as defined in Appendix 1 of the MMPEULA-1.0. This is the mechanism that ensures your end-users are legally bound by the commercial EULA.

4.  **Manage Stewardship (Optional but Recommended):**
    *   Create a `STEWARD.md` file in your repository.
    *   In your `CONTRIBUTING.md`, explain how contributors can opt-in to become Stewards by adding their name to the `STEWARD.md` file, thereby accepting the MRSL-1.0's Ethical Use Covenant in exchange for greater legal protections.
