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

