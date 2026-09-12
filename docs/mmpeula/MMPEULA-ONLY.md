# THE MMPEULA-ONLY DISTRIBUTION MODEL

The MitsuoLabs™ MASTER PROFESSIONAL AND END USER LICENSE AGREEMENT (MMPEULA-1.0) can be used as the exclusive license governing the **official binaries** of a project, even when the source code is available under a separate FOSS license. This creates a dual-license ecosystem where end-users of the binaries are bound by commercial terms, while developers retain the freedom to self-build from the source.

## Core Strategy: The "Front-Door" EULA

This model works by separating the license of the convenient, pre-compiled product (the binary) from the license of the underlying source code.

- **The Binaries (MMPEULA-1.0):** Official, pre-compiled binaries are distributed exclusively under the MMPEULA-1.0. An end-user who downloads and runs these binaries must agree to the EULA's commercial terms. This is the "front-door" for professional users who want a ready-to-use, supported product.

- **The Source Code (FOSS):** The source code itself is licensed under a FOSS license (like MRSL-1.0, GPL, or MIT). This ensures the project remains open-source, auditable, and community-driven.

This is **not tivoization**. Users always have the freedom to bypass the MMPEULA by downloading the FOSS-licensed source code and compiling it themselves. The MMPEULA only applies to the official, licensor-provided executables.

### Key Characteristics of this Model

1.  **Dual-Path Licensing:** Users have a choice. They can either accept the MMPEULA-1.0 to use the convenient official binaries, or they can exercise their FOSS rights by building the software from source.

2.  **Commercial-Ready Binaries:** It allows you to sell software or apply commercial terms to the distribution of your binaries, creating a direct revenue stream from a FOSS project.

3.  **Preservation of FOSS Freedoms:** The underlying source code remains free and open source, encouraging community contribution, transparency, and trust.

4.  **Use Cases:**
    *   **Open-Core/Community Edition:** Offer official builds with commercial terms (support, specific features) under the MMPEULA, while the community can self-build the core FOSS version.
    *   **FOSS Projects with a Commercial Arm:** A perfect model for a company that wants to steward a FOSS project while selling a commercial version of the product.

## Proprietary Source-Available Model

A secondary, less common use of MMPEULA-only is for proprietary, source-available projects, often for internal or B2B partner use. In this case, both the source and binaries are governed by the MMPEULA. This is a purely commercial model where source is provided for transparency and auditability, but no FOSS rights are granted.

## How to Implement the "Front-Door" Model

1.  **Dual Licensing in Your Repository:**
    *   Place the full text of your chosen FOSS license (e.g., `mrsl-1.0.txt`) in your repository as `LICENSE`.
    *   Place the full text of `mmpeula-1.0.txt` in a separate file, such as `BINARY-EULA.md`.

2.  **Clarify in README.md:** Your `README.md` must be very clear about the dual-license structure:
    ```markdown
    ## Licensing

    The source code of this project is licensed under the [Your FOSS License, e.g., MRSL-1.0].

    The official, pre-compiled binaries distributed by [Your Company] are licensed under the MitsuoLabs™ MASTER PROFESSIONAL AND END USER LICENSE AGREEMENT (MMPEULA-1.0), available in `BINARY-EULA.md`. By downloading and using the binaries, you agree to its terms. You are always free to build from source under the terms of the FOSS license.
    ```

3.  **Implement the Acceptance Protocol:** For all distributed binaries, you **must** implement the **MitsuoLabs™ Acceptance Protocol** as defined in Appendix 1 of the MMPEULA-1.0. This is non-negotiable for ensuring the EULA is legally binding.
