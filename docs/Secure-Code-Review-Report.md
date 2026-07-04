# Secure Code Review Report

## Project Information

| Item | Details |
| :--- | :------ |
| Project Name | CodeAlpha Secure Coding Review |
| Programming Language | Python |
| Framework | Flask |
| Database | SQLite |
| Review Type | Manual Secure Code Review |
| Reviewer | Sahadat Hossain |
| Review Date | July 2026 |


---

# Review Objectives

The primary objective of this secure code review is to identify security vulnerabilities in the application through manual source code inspection. The review focuses on detecting common security weaknesses based on secure coding best practices and the OWASP Top 10.

The review aims to:

- Identify insecure coding practices.
- Detect common web application vulnerabilities.
- Assess the security impact of each issue.
- Recommend secure coding improvements.
- Prepare the application for static analysis using Bandit and Semgrep.

---

# Review Scope

The review covers the following components of the application:

- User Registration
- User Authentication
- Session Management
- Dashboard
- User Search
- User Profile
- File Upload
- Admin Panel
- Application Configuration
- Database Operations


---

# Review Methodology

The application was reviewed using manual source code inspection.

The review focused on identifying:

- SQL Injection
- Plain Text Password Storage
- Broken Access Control
- Information Disclosure
- Unsafe File Upload
- Session Security Issues
- Configuration Weaknesses

The identified issues will later be verified using static analysis tools such as Bandit and Semgrep.


---

# Files Reviewed

The following files were manually reviewed during the assessment:

- app/auth/routes.py
- app/main/routes.py
- app/search/routes.py
- app/profile/routes.py
- app/upload/routes.py
- app/admin/routes.py
- app/database.py
- app/decorators.py
- app/config.py
- app/app.py

---

# Security Findings

The manual secure code review identified several intentionally introduced security vulnerabilities. These findings are documented below along with their severity, impact, and recommended remediation.


---

## Finding 1 – Plain Text Password Storage

**Severity:** High

**Location:**

app/auth/routes.py

**Description:**

User passwords are stored directly in the database without hashing.

**Security Impact:**

If the database is compromised, attackers can immediately read all user passwords.

**Recommendation:**

Store passwords using a secure hashing algorithm such as Werkzeug Security or bcrypt.

---

## Finding 2 – SQL Injection (Login)

**Severity:** Critical

**Location:**

app/auth/routes.py

**Description:**

The login functionality constructs SQL queries using direct string formatting with user-supplied input.

**Security Impact:**

This may allow attackers to manipulate SQL queries and bypass authentication.

**Recommendation:**

Use parameterized queries instead of string concatenation.

---

## Finding 3 – SQL Injection (Search)

**Severity:** Critical

**Location:**

app/search/routes.py

**Description:**

The search functionality builds SQL queries directly from user input.

**Security Impact:**

Improper query construction can allow unauthorized SQL query manipulation.

**Recommendation:**

Use parameterized queries or prepared statements for database searches.


---

## Finding 4 – Information Disclosure

**Severity:** High

**Location:**

app/profile/routes.py

**Description:**

The application displays sensitive user information, including the user's password, on the profile page.

**Security Impact:**

Displaying sensitive information increases the risk of credential exposure and unauthorized disclosure.

**Recommendation:**

Sensitive information such as passwords should never be displayed to users. Only non-sensitive profile information should be shown.


---

## Finding 5 – Unsafe File Upload

**Severity:** High

**Location:**

app/upload/routes.py

**Description:**

The application accepts uploaded files without validating their type, extension, or size.

**Security Impact:**

Improper validation may allow unauthorized or malicious files to be uploaded, increasing security risk.

**Recommendation:**

Validate file extensions, MIME types, and file size before accepting uploaded files.


---

## Finding 6 – Broken Access Control

**Severity:** Critical

**Location:**

app/admin/routes.py

**Description:**

The admin panel is accessible to any authenticated user without verifying administrative privileges.

**Security Impact:**

Unauthorized users may gain access to administrative functionality.

**Recommendation:**

Implement role-based access control (RBAC) and verify user privileges before granting access to administrative resources.


---

# OWASP Top 10:2025 Mapping

| Finding | OWASP Top 10:2025 | Description |
|---------|-------------------|-------------|
| Plain Text Password Storage | A04: Cryptographic Failures | Passwords are stored without hashing. |
| SQL Injection (Login) | A05: Injection | User input is directly inserted into SQL queries. |
| SQL Injection (Search) | A05: Injection | Search input is concatenated into SQL queries. |
| Information Disclosure | A01: Broken Access Control | Sensitive user information is exposed to authenticated users. |
| Unsafe File Upload | A02: Security Misconfiguration | File upload validation is not implemented. |
| Broken Access Control | A01: Broken Access Control | Administrative functionality is accessible without proper authorization. |


---

# CWE Mapping

| Finding | CWE ID | Description |
|---------|---------|-------------|
| Plain Text Password Storage | CWE-256 | Plaintext Storage of Password |
| SQL Injection (Login) | CWE-89 | SQL Injection |
| SQL Injection (Search) | CWE-89 | SQL Injection |
| Information Disclosure | CWE-200 | Exposure of Sensitive Information |
| Unsafe File Upload | CWE-434 | Unrestricted File Upload |
| Broken Access Control | CWE-284 | Improper Access Control |


---

# Summary

A total of **6 security vulnerabilities** were identified during the manual secure code review.

| Severity | Count |
|----------|------:|
| Critical | 2 |
| High | 4 |
| Medium | 0 |
| Low | 0 |

The identified issues primarily affect authentication, authorization, input validation, and file handling. These vulnerabilities were intentionally introduced for educational purposes and will be remediated in the next phase of the project.



---

# Risk Assessment Matrix

| Finding | Severity | Risk Level |
|---------|----------|------------|
| Plain Text Password Storage | High | High |
| SQL Injection (Login) | Critical | Critical |
| SQL Injection (Search) | Critical | Critical |
| Information Disclosure | High | High |
| Unsafe File Upload | High | High |
| Broken Access Control | Critical | Critical |



---

# Remediation Plan

| Finding | Recommended Fix | Priority |
|---------|-----------------|----------|
| Plain Text Password Storage | Hash passwords using Werkzeug Security or bcrypt. | High |
| SQL Injection (Login) | Replace string concatenation with parameterized SQL queries. | Critical |
| SQL Injection (Search) | Use prepared statements for search queries. | Critical |
| Information Disclosure | Remove sensitive information from the profile page. | High |
| Unsafe File Upload | Validate file type, extension, MIME type, and file size before saving uploads. | High |
| Broken Access Control | Implement role-based access control (RBAC) for administrative pages. | Critical |


---

# Conclusion

A manual secure code review was successfully completed for the **CodeAlpha Secure Coding Review** project.

The assessment identified **six intentionally introduced security vulnerabilities** for educational purposes. These issues demonstrate common web application security risks, including insecure authentication, injection flaws, information disclosure, unrestricted file upload, and broken access control.

The findings have been documented and mapped to the latest OWASP Top 10 and CWE standards. In the next phase of the project, static analysis tools such as **Bandit** and **Semgrep** will be used to validate the findings. Finally, all identified vulnerabilities will be remediated by applying secure coding best practices.

This review demonstrates a structured approach to secure code assessment and provides a foundation for improving the application's overall security posture.



