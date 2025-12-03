# payments-api

Demo repository for **GHAS Campaigns + Copilot Autofix** video script.

## ⚠️ Warning

This repository contains **intentionally vulnerable code** with SQL injection vulnerabilities for demonstration purposes.

**DO NOT use this code in production!**

## Purpose

This repo is used in Demo 2 of the video script to demonstrate:

- SQL injection vulnerabilities detected by CodeQL
- Copilot Autofix automatically generating secure fixes
- Committing fixes through the Security Campaigns workflow

## Files

- `src/user_service.py` - Contains multiple SQL injection vulnerabilities
- `.github/workflows/codeql.yml` - CodeQL scanning configuration

## Setup Instructions

1. Enable GitHub Advanced Security for this repository
2. Enable Code scanning (CodeQL is configured via the workflow file)
3. Enable Copilot Autofix in organization settings
4. Push code to trigger CodeQL scan
5. Wait for alerts to appear in Security tab
6. Create a Security Campaign targeting SQL injection alerts (CWE-89)

## Expected Alerts

The code should trigger multiple SQL injection alerts:

- `get_user()` - f-string interpolation
- `get_user_by_id()` - string concatenation
- `search_users()` - LIKE query with f-string
- `get_orders_for_user()` - JOIN query with concatenation

All alerts should have Copilot Autofix suggestions available.
