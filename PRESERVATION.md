## Digital Preservation and The Alexandria Clause

## 1. Commitment to Long-Term Preservation

In accordance with Section 19 of the MitsuoLabs™ Reciprocity and Stewardship License (MRSL-1.0), known as **The Alexandria Clause**, this project is formally committed to the long-term, durable preservation of of its source code and legal texts. We believe that a framework of this nature is a contribution to our shared digital heritage and must be protected against loss, censorship, or institutional decay.

This commitment is not merely a statement of intent; it is an operational protocol. We recognize that the value of this framework lies in its perpetual availability and the public's ability to access, study, and build upon it for generations to come.

## 2. Designated Public Archives

To fulfill this commitment, we have designated the following internationally recognized public archives as official repositories for the Corresponding Source of the MitsuoLabs Legal Framework. Upon every major version release, a good-faith effort will be made to submit the complete source code and documentation to these institutions.

1.  **Software Heritage**
    *   **Website:** [https://www.softwareheritage.org/](https://www.softwareheritage.org/)
    *   **Rationale:** As a universal source code archive, Software Heritage is the premier institution dedicated to collecting, preserving, and sharing the world's software. Its mission is directly aligned with the principles of The Alexandria Clause.

2.  **The Internet Archive**
    *   **Website:** [https://archive.org/](https://archive.org/)
    *   **Rationale:** The Internet Archive provides robust, long-term storage for all forms of digital content. Archiving the git repository and release tarballs here ensures a high degree of redundancy and public accessibility.

3.  **The GitHub Arctic Code Vault**
    *   **Website:** [https://archiveprogram.github.com/](https://archiveprogram.github.com/)
    *   **Rationale:** As a public repository on GitHub, this project is automatically included in the Arctic Code Vault program, which preserves open-source software for 1,000 years by archiving it in a vault in Svalbard, Norway. This provides an unparalleled level of long-term, disaster-proof preservation.

4.  **The Bodleian Libraries, University of Oxford**
    *   **Website:** [https://www.bodleian.ox.ac.uk/](https://www.bodleian.ox.ac.uk/)
    *   **Rationale:** As one of the oldest and most respected libraries in the world, the Bodleian has a centuries-long history of preserving humanity's most important written works. We will submit digital copies of the legal texts and a reference to the source code to their digital archiving program, entrusting a copy of this modern legal document to an institution with a proven commitment to long-term stewardship.

5.  **The InterPlanetary File System (IPFS)**
    *   **Website:** [https://ipfs.tech/](https://ipfs.tech/)
    *   **Rationale:** As a peer-to-peer, content-addressed network, IPFS provides a decentralized and censorship-resistant method of preservation. Pinning the framework's releases on IPFS ensures that the data persists as long as at least one node in the global network hosts it, creating a resilient "living archive" that is not dependent on any single institution. This aligns with the MRSL's own provisions for decentralized distribution.

6.  **Tor Onion Service**
    *   **Website:** To be determined (e.g., `[hash].onion`)
    *   **Rationale:** Providing an onion service makes the legal framework accessible via the Tor network, offering a high degree of censorship resistance and privacy for users worldwide. This ensures that the texts can be reached even in environments where access to the public internet or specific sites like GitHub is restricted. This practice is consistent with the license's support for privacy-preserving technologies (Axiom 25.13) and the project's core philosophy.

5.  **Harvard Law School Library**
    *   **Website:** [https://hls.harvard.edu/library/](https://hls.harvard.edu/library/)
    *   **Rationale:** As a world-leading institution in legal scholarship, the Harvard Law School Library is a natural home for a modern legal framework. Its prestige and commitment to preserving legal history make it an ideal partner for ensuring the long-term integrity and accessibility of these licenses.

6.  **Yale Law School, Lillian Goldman Law Library**
    *   **Website:** [https://library.law.yale.edu/](https://library.law.yale.edu/)
    *   **Rationale:** Yale's Lillian Goldman Law Library is renowned for its extensive collection, including the Avalon Project. Adding the MitsuoLabs licenses to their digital archives places them within a context of foundational legal and historical documents, ensuring they are available for future generations of legal scholars and practitioners.

7.  **Stanford Law School, Juelsgaard Intellectual Property and Innovation Clinic**
    *   **Website:** [https://law.stanford.edu/juelsgaard-intellectual-property-and-innovation-clinic/](https://law.stanford.edu/juelsgaard-intellectual-property-and-innovation-clinic/)
    *   **Rationale:** Situated at the heart of Silicon Valley and focused on the intersection of law, technology, and IP, the Juelsgaard Clinic is a perfect strategic partner. By submitting the licenses here, we are not just archiving them, but offering them as a living case study for the students and faculty who are shaping the future of technology law.

8.  **GitLab Repository**
    *   **Website:** [https://gitlab.com/mitsuolabs/licenses](https://gitlab.com/mitsuolabs/licenses)
    *   **Rationale:** Beyond simple code hosting, GitLab provides a robust, independent, and full-featured development platform. By maintaining a complete mirror on GitLab, we create a redundant, publicly accessible archive that is not dependent on a single commercial entity. The integrated CI/CD pipeline also serves as a living record of the project's own preservation and verification processes.

**Note on Phased Rollout:** For the initial **v1.0** release, preservation is guaranteed in the **GitHub Arctic Code Vault** (which is automatic) plus GitLab. For all subsequent major releases (**v2.0** and beyond), the project will be submitted to all nine archives (acceptance may vary).

## 3. Archival Procedure

This procedure is automated via the **`.github/workflows/release-archive.yml`** GitHub Action, which runs on every new release.

1.  **Automated Asset Generation:** The workflow automatically generates a complete, versioned tarball of the source code and documentation.
2.  **Automated Decentralized Pinning (IPFS):** The workflow adds the release tarball to IPFS to generate a Content Identifier (CID) and then uses a pinning service (via API keys stored in GitHub Secrets) to ensure its long-term persistence. The final CID is logged.
3.  **Semi-Automated Centralized Submission:** The workflow prepares the release assets and metadata for submission to centralized archives (Software Heritage, The Internet Archive). Some of these submissions may be completed automatically via API, while others may require a final manual confirmation step by a project Maintainer.
4.  **Manual Submission:** Submission to the Bodleian Libraries remains a manual process to be completed by a Maintainer.
5.  **Onion Service Update:** Following a release, the content hosted on the project's official Tor Onion Service will be manually updated by a Maintainer to reflect the new version.
6.  **Record Keeping:** All archival identifiers (CIDs, submission receipts, etc.) are automatically collected and logged as artifacts of the GitHub Actions workflow run, creating a permanent, auditable record.
