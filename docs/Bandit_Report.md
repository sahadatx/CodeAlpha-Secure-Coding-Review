# Bandit Static Analysis Report

## Project Information

| Item | Details |
|------|---------|
| Tool | Bandit |
| Version | 1.9.4 |
| Language | Python |
| Framework | Flask |
| Scan Type | Recursive |
| Scan Command | `bandit -r app` |

---

# Scan Summary

| Severity | Count |
|----------|------:|
| High | 0 |
| Medium | 2 |
| Low | 1 |

**Total Issues:** 3

---

# Findings

## Finding 1 – B608: SQL Injection

**File**

`app/auth/routes.py`

**Severity**

Medium

**Confidence**

Low

**Description**

Bandit detected SQL query construction using string formatting, which may introduce SQL Injection vulnerabilities.

**Recommendation**

Use parameterized SQL queries.

---

## Finding 2 – B608: SQL Injection

**File**

`app/search/routes.py`

**Severity**

Medium

**Confidence**

Low

**Description**

The search query is built using user input and string formatting.

**Recommendation**

Use prepared statements or parameterized queries.

---

## Finding 3 – B105: Hardcoded Secret Key

**File**

`app/config.py`

**Severity**

Low

**Confidence**

Medium

**Description**

A hardcoded secret key was detected in the configuration file.

**Recommendation**

Store the secret key securely using environment variables.


---

# Comparison with Manual Review

| Vulnerability | Manual Review | Bandit |
|---------------|---------------|---------|
| SQL Injection | ✅ Yes | ✅ Yes |
| Plain Text Password Storage | ✅ Yes | ❌ No |
| Information Disclosure | ✅ Yes | ❌ No |
| Unsafe File Upload | ✅ Yes | ❌ No |
| Broken Access Control | ✅ Yes | ❌ No |
| Hardcoded Secret Key | ✅ Yes | ✅ Yes |


---

# Observation

Bandit successfully detected SQL Injection patterns and the hardcoded secret key.

However, it did not detect business logic issues such as:

- Plain Text Password Storage
- Information Disclosure
- Broken Access Control
- Unsafe File Upload

These vulnerabilities require manual secure code review in addition to automated static analysis.

