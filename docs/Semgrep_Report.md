# Semgrep Static Analysis Report

## Project Information

| Item | Details |
|------|---------|
| Tool | Semgrep |
| Language | Python |
| Framework | Flask |
| Scan Type | Static Analysis |
| Scan Command | `semgrep scan app` |

---

# Scan Summary

| Severity | Count |
|----------|------:|
| Blocking | 2 |

**Total Findings:** 2

---

# Finding 1 – Missing Subresource Integrity (SRI)

**File**

app/templates/base.html

**Rule ID**

html.security.audit.missing-integrity.missing-integrity

**Severity**

Blocking

**Description**

Bootstrap CSS and JavaScript are loaded from a CDN without an `integrity` attribute.

**Security Impact**

If the external CDN resource is compromised, users may receive modified or malicious files.

**Recommendation**

Use the official Bootstrap CDN snippet with `integrity` and `crossorigin` attributes.

---

# Finding 2 – Missing CSRF Protection

**File**

app/templates/upload.html

**Rule ID**

python.django.security.django-no-csrf-token

**Severity**

Blocking

**Description**

Semgrep detected a form without a CSRF token.

**Analysis**

This project is built with **Flask**, not **Django**. The reported rule is intended for Django templates and is therefore **not applicable** to this project.

**Recommendation**

If CSRF protection is required in Flask, use **Flask-WTF** or another CSRF protection mechanism.

---

# Observation

Semgrep successfully identified:

- Missing Subresource Integrity (SRI)

It also reported a Django-specific CSRF rule, which is considered a **false positive** for this Flask-based application.

Manual review remains essential because automated tools cannot always distinguish framework-specific contexts.


## Final Result

Semgrep was executed after all security remediations.

### Findings Summary

- Total Findings: 1
- Critical Findings: 0
- High Findings: 0
- Medium Findings: 0

### False Positive

Semgrep reported the following rule:

- python.django.security.django-no-csrf-token

This application is built using Flask, not Django. Therefore, the reported finding is not applicable and is considered a false positive.

### Conclusion

All intended security vulnerabilities have been successfully remediated.

The remaining Semgrep finding is framework-specific and does not affect the security of this Flask application.