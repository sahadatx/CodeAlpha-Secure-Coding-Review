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



